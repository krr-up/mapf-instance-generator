import argparse, os, time, signal, cv2
from subprocess import getoutput
from random import randint, shuffle
from itertools import product
import numpy as np

def add_agents(timeout):	# Adds agents to the instance
	if args.distance != '0':
		instance_filled = getoutput(f'clingo {instanceFileName} encodings/agents.lp -c d={args.distance} -c a={args.agents} --init-watches=rnd --sign-def=rnd --rand-freq=1 -V0 --out-atomf=%s. --out-ifs="\n" --time-limit={str(round(timeout))} | head -n -1')
		if 'INTERRUPTED' in instance_filled: clean_up('\nTIMEOUT')
	else:
		list_of_vertices = []
		for line in instance_unfilled.splitlines():
			if 'vertex' in line:
				line = line.split("vertex(",1)[1]
				line = line.split(").",1)[0]
				list_of_vertices.append(line)
		if len(list_of_vertices) < int(args.agents): clean_up(f'\nNumber of agents ({args.agents}) exceeds number of vertices ({str(len(list_of_vertices))})!')
		list_of_starts = list_of_vertices.copy()
		list_of_goals  = list_of_vertices.copy()
		shuffle(list_of_starts)
		shuffle(list_of_goals)
		instance_filled = instance_unfilled + '\n'
		for agent in range(1, int(args.agents)+1): instance_filled = instance_filled + (f'start({str(agent)},{str(list_of_starts.pop())}).\n') + (f'goal({str(agent)},{str(list_of_goals.pop())}).\n' + f'agent({str(agent)}).')
	write('w', instance_filled)

def add_header(timeout):	# Adds a header to the instance file
	header = f'%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%\n%\n% Size X and Y:\t\t{str(int(args.size))}\n% Number of Agents:\t\t{args.agents}'
	if   args.type == 'random': header += f'\n% Vertices used (in %):\t{args.cover}'
	elif args.type == 'room':   header += f'\n% Room Width:\t\t\t{args.width}'
	header += '\n%\n%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%\n\n#program base.\n\n'
	with open(instanceFileName, 'r') as instance:
		instance_without_header = instance.read()
	write('w', header + instance_without_header)

def clean_instance(instanceFileName):	# Cleans the instance (remove all agents)
	global instance_unfilled
	instance_unfilled = ''
	with open(instanceFileName, 'r') as instance:
		instance_uncleaned = instance.readlines()
		instance.seek(0)
		for line in instance_uncleaned:
			if 'agent' not in line and 'start' not in line and 'goal' not in line:
				instance_unfilled += line

def create_instance(timeout):	# Creates an instance based on the type
	global instanceFileName, instance_unfilled

	if   args.type == 'maze'               : instanceFileName  = f'{args.type}_s{args.size}_a{args.agents}.lp'
	elif args.type == 'random'             : instanceFileName  = f'{args.type}_s{args.size}_a{args.agents}_c{args.cover}.lp'
	elif args.type in ['room', 'warehouse']: instanceFileName  = f'{args.type}_s{args.size}_a{args.agents}_w{str(args.width)}.lp'
	
	if   args.type == 'maze':      instance_unfilled = getoutput(f'clingo encodings/{args.type}.lp -c s={args.size}                                      --sign-def=rnd --init-watches=rnd --rand-freq=1 -V0 --out-atomf=%s. --out-ifs="\n" --time-limit={str(timeout)} | head -n -1')
	elif args.type == 'random':    instance_unfilled = getoutput(f'clingo encodings/{args.type}.lp -c s={args.size} -c c={args.cover}                    --sign-def=rnd --init-watches=rnd --rand-freq=1 -V0 --out-atomf=%s. --out-ifs="\n" --time-limit={str(timeout)} | head -n -1')
	elif args.type == 'room':      instance_unfilled = getoutput(f'clingo encodings/{args.type}.lp -c s={args.size} -c w={args.width}                    --sign-def=rnd --init-watches=rnd --rand-freq=1 -V0 --out-atomf=%s. --out-ifs="\n" --time-limit={str(timeout)} | head -n -1')
	elif args.type == 'warehouse': instance_unfilled = getoutput(f'clingo encodings/{args.type}.lp -c s={args.size} -c w={args.width} -c a={args.agents} --sign-def=rnd --init-watches=rnd --rand-freq=1 -V0 --out-atomf=%s. --out-ifs="\n" --time-limit={str(timeout)} | head -n -1')
	if 'INTERRUPTED' in instance_unfilled: clean_up('\nTIMEOUT')
	write('w', instance_unfilled)

def add_durations(timeout):	# Adds random durations between two values to edges of an instance
	with open(instanceFileName, 'r+') as instance:
		instance_with_durations = instance.readlines()
		instance.seek(0)
		for line in instance_with_durations:
			if 'edge' in line: line = line.replace('))', f'),{str(randint(int(args.durations[0]),int(args.durations[1])))})')
			instance.writelines(line)

def get_horizon(timeout):	# Finds the minimal makespan (horizon) of an instance
	global instanceFileName
	time_elapsed_meta = 0
	time_start_meta = time.time()
	if args.durations: solution = getoutput(f'clingo encodings/mif_inc_dur.lp {instanceFileName} -W none --outf=1 --time-limit={str(round(timeout))}')
	else:              solution = getoutput(f'clingo encodings/mif_inc.lp     {instanceFileName} -W none --outf=1 --time-limit={str(round(timeout))}')
	if (timeout<0) or ('INTERRUPTED' in solution): clean_up('\nTIMEOUT')
	if int(args.timeout) > 0: time_elapsed_meta = time.time() - time_start_meta
	if 'Calls' in solution:
		solution = solution.split("Calls          : ",1)[1]
		horizon = str(int(solution.split("% Time",1)[0])-1)

		if args.durations: acyc_out = getoutput(f'clingo encodings/mif_dur.lp -c acyclic=1 -c horizon={horizon} {instanceFileName} --time-limit={str(round(timeout-time_elapsed_meta))}')
		else:              acyc_out = getoutput(f'clingo encodings/mif.lp     -c acyclic=1 -c horizon={horizon} {instanceFileName} --time-limit={str(round(timeout-time_elapsed_meta))}')
		if ((timeout-time_elapsed_meta)<0) or ('INTERRUPTED' in acyc_out): clean_up('\nTIMEOUT')
		elif 'UN' in acyc_out: acyclic = ''
		else: acyclic = 'acyclic.'

		with open(instanceFileName[:-3] + '_meta.lp', 'w') as metaFile:
			metaFile.write(f'% meta information:\n#const horizon={horizon}.\nmakespan(horizon).\n{acyclic}')
	
	else: print(solution)

def get_shortest_paths(timeout):	# Finds one shortest path for each agent
	with open(instanceFileName[:-3] + '_SPs.lp', 'w') as SP_file:
		SP_file.write('')
	global max_SP_length
	max_SP_length = 0
	time_elapsed_SP_inloop = 0
	with open(instanceFileName, 'r') as instance:
		inst = instance.read()
	
	for agent in range(1,inst.count('agent')+1):
		time_start_SP_inloop = time.time()
		time_remaining_SP = timeout - time_elapsed_SP_inloop
		numSPs='1'
		if args.allSPs: numSPs='0'
		if args.durations: shortest_paths = getoutput(f'clingo encodings/SP_dur.lp {instanceFileName} -c agent={str(agent)} -W none --out-atomf=%s. -V0 {numSPs} --time-limit={str(round(time_remaining_SP))} | head -n -1')
		else:              shortest_paths = getoutput(f'clingo encodings/SP.lp     {instanceFileName} -c agent={str(agent)} -W none --out-atomf=%s. -V0 {numSPs} --time-limit={str(round(time_remaining_SP))} | head -n -1')
		if 'INTERRUPTED' in shortest_paths: clean_up('\nTIMEOUT')

		with open(instanceFileName[:-3] + '_SPs.lp', 'a') as SP_file:
			SP_file.write(f'% agent {str(agent)}:\n{shortest_paths}\n\n')
		if timeout>0: time_elapsed_SP_inloop += (time.time() - time_start_SP_inloop)

def img2inst(timeout):	# Converts an image to an instance of a given size
    global instanceFileName
    global instance_unfilled
    instance_unfilled = ''
    if not args.agents: args.agents = '0'
    instanceFileName  = (args.type.split('/')[-1]).split('.')[0] + f'_s{args.size}_a{args.agents}.lp'
    image = cv2.imread(args.type, cv2.IMREAD_GRAYSCALE)
    resized_image = cv2.resize(image, (int(args.size), int(args.size)), interpolation=cv2.INTER_NEAREST)

    for y in range(0, int(args.size)):
        for x in range(0, int(args.size)):
            if not is_dark_pixel(resized_image, x, y):
                instance_unfilled  += (f"vertex(({x + 1},{y + 1})).\n")

                if x > 0 and not is_dark_pixel(resized_image, x - 1, y    ):
                    instance_unfilled += (f"edge(({x    },{y + 1}),({x + 1},{y + 1})).\n")
                    instance_unfilled += (f"edge(({x + 1},{y + 1}),({x    },{y + 1})).\n")
                if y > 0 and not is_dark_pixel(resized_image, x    , y - 1):
                    instance_unfilled += (f"edge(({x + 1},{y    }),({x + 1},{y + 1})).\n")
                    instance_unfilled += (f"edge(({x + 1},{y + 1}),({x + 1},{y    })).\n")

    write('w', instance_unfilled)

def is_dark_pixel(image, x, y, threshold=128):	# Decides if a pixel is dark or not
    return np.mean(image[y, x]) < threshold

def run(function):	# Runs a function and prints out its runtime
	global time_elapsed
	start_time = time.time()
	if not args.quiet: print('Running', '{:15s}'.format(function) + ' \t...', end=' ', flush=True)
	eval(function + '(' + str(int(args.timeout)-time_elapsed) + ')')
	if int(args.timeout) > 0: time_elapsed = time_elapsed + (time.time()-start_time)
	if not args.quiet: print('done (in ', "{:5.1f}".format(time.time()-start_time), ' seconds).')

def write(mode, string):	# Writes a file with a given name in the given mode
	with open(instanceFileName, mode) as instance:
		instance.write(string)

def clean_up(msg):	# Cleans up (incomplete) files if program times out or is interrupted
	print(msg)
	filenames_to_delete = [instanceFileName, instanceFileName[:-3]+'_SPs.lp', instanceFileName[:-3]+'_meta.lp']
	for filename in filenames_to_delete:
		if os.path.exists(filename):
			os.remove(filename)
			print(f'removed {filename}')
	raise SystemExit()

def signal_handler(sig, frame): clean_up('\nKILLED BY SIGNAL')
signal.signal(signal.SIGINT,  signal_handler)
signal.signal(signal.SIGTERM, signal_handler)

parser       = argparse.ArgumentParser(usage='python gen.py (maze | random -c [0-100] | room -w WIDTH | warehouse -w WIDTH) -s SIZE -a AGENTS [-d DISTANCE] [-dur MINDUR MAXDUR] [-m] [-t TIMEOUT] [-v] [-h] [-q]')
req_group    = parser.add_argument_group('required arguments for all instance types')
parser.add_argument(   'type',                  help='', metavar=['maze', 'random', 'room', 'warehouse', '*.jpg', '*.png', '*.lp'])
parser.add_argument(          '--allSPs',       help='generates all shortest paths instead of one',action='store_true')
parser.add_argument(   '-d',  '--distance',     help='min. manhatten distance from start to goal', type=str, default='0')
parser.add_argument(   '-dur','--durations',    help='generates instances with durations',         type=str, nargs=2, metavar=('MINDUR', 'MAXDUR'))
parser.add_argument(   '-m',  '--meta',         help='gets and adds meta informations',            action='store_true')
parser.add_argument(   '-q',  '--quiet',        help='turns on quiet mode',                        action='store_true')
parser.add_argument(   '-t',  '--timeout',      help='sets a timeout in seconds',                  type=str, default='0')
parser.add_argument(   '-v',  '--visualize',    help='convert to and visualize with asprilo',      action='store_true')
parser.add_argument(   '-w',  '--width',        help='width of rooms (default=5)',                 type=str, default='5')
parser.add_argument(   '-c',  '--cover',        help='percentage of vertices covered (default=75)',type=str, default='75', metavar='[0-100]')
req_group.add_argument('-s',  '--size',         help='size of instance',                           type=str)
req_group.add_argument('-a',  '--agents',       help='number of agents',                           type=str)
args = parser.parse_args()
if args.type not in ['maze', 'random', 'room', 'warehouse'] and '.jpg' not in args.type and '.png' not in args.type and '.lp' not in args.type:
	print('File type must be: maze, random, room or warehouse or end with .jpg, .png or .lp')
	raise SystemExit()
if '.lp' not in args.type and not args.size: raise parser.error('--size required')

if '.lp' in args.type:
	instanceFileName  = (args.type.split('/')[-1])
	if args.agents: clean_instance(instanceFileName)
	if args.agents: instanceFileName = instanceFileName.split('_a')[0] + f'_a{args.agents}.lp'   
	
if '.' not in args.type and not args.agents: args.agents = '0'

time_elapsed = 0

if '.jpg' in args.type or '.png' in args.type:
	if os.path.isfile(args.type): run('img2inst')
	else:
		print(f'File \'{args.type}\' not found')
		raise SystemExit()

if '.' not in args.type: run('create_instance')
if args.agents:          run('add_agents')
if args.durations:       run('add_durations')
if '.' not in args.type: run('add_header')
if args.meta:
	run('get_shortest_paths')
	run('get_horizon')

if args.visualize: os.system(f'clingo {instanceFileName} encodings/mif_to_asprilo.lp | viz')	# Uses clingo to translate the instance from mif- to asprilo-format and opens it with the asprilo visualizer
