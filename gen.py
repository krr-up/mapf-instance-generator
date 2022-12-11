import argparse, os, time, signal
from subprocess import getoutput
from random import randint

def add_agents(timeout):
	instance_filled = getoutput('clingo ' + instanceFileName + ' encodings/agents.lp -c d=' + args.distance + ' -c a=' + args.agents + ' --init-watches=rnd --sign-def=rnd --rand-freq=1 -V0 --out-atomf=%s. --out-ifs="\n" --time-limit=' + str(round(timeout)) + ' | head -n -1')
	write('w', instance_filled)
	if 'INTERRUPTED' in instance_filled: clean_up('\nTIMEOUT')

def add_header(timeout):
	header = '%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%\n%\n% Size X and Y:\t\t' + str(int(args.size)*2) + '\n% Number of Agents:\t\t' + args.agents
	if   args.type == 'random': header = header + '\n% Vertices used (in %):\t' + args.cover
	elif args.type == 'room':   header = header + '\n% Room Width:\t\t\t'       + args.width
	header = header + '\n%\n%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%\n\n#program base.\n\n'
	with open(instanceFileName, 'r') as instance:
		instance_without_header = instance.read()
	write('w', header + instance_without_header)

def create_instance(timeout):
	global instanceFileName, instance_unfilled
	if   args.type == 'maze': instanceFileName  = 'maze_s' + args.size + '_a' + args.agents +'.lp'
	elif args.type == 'random': instanceFileName  = 'random_s' + args.size + '_a' + args.agents + '_c' + args.cover +'.lp'
	elif args.type == 'room': instanceFileName  = 'room_s' + args.size + '_a' + args.agents + '_w' + str(args.width) +'.lp'
	elif args.type == 'warehouse': instanceFileName  = 'warehouse_s' + args.size + '_a' + args.agents + '_w' + str(args.width) +'.lp'
	if   args.type == 'maze': instance_unfilled = getoutput('clingo encodings/maze.lp -c s=' + args.size + ' --sign-def=rnd --init-watches=rnd --rand-freq=1 -V0 --out-atomf=%s. --out-ifs="\n" --time-limit=' + str(timeout) + ' | head -n -1')
	elif args.type == 'random': instance_unfilled = getoutput('clingo encodings/random.lp -c s=' + args.size + ' -c c=' + args.cover + ' --sign-def=rnd --init-watches=rnd --rand-freq=1 -V0 --out-atomf=%s. --out-ifs="\n" --time-limit=' + str(timeout) + ' | head -n -1')
	elif args.type == 'room': instance_unfilled = getoutput('clingo encodings/room.lp -c s=' + args.size + ' -c w=' + args.width + ' --rand-freq=1 --init-watches=rnd --sign-def=rnd -V0 --out-atomf=%s. --out-ifs="\n" --time-limit=' + str(timeout) + ' | head -n -1')
	elif args.type == 'warehouse': instance_unfilled = getoutput('clingo encodings/warehouse.lp -c s=' + args.size + ' -c w=' + args.width + ' -c a=' + args.agents + ' --rand-freq=1 --init-watches=rnd --sign-def=rnd -V0 --out-atomf=%s. --out-ifs="\n" --time-limit=' + str(timeout) + ' | head -n -1')
	if 'INTERRUPTED' in instance_unfilled: clean_up('\nTIMEOUT')
	write('w', instance_unfilled)

def add_durations(timeout):
	with open(instanceFileName, 'r+') as instance:
		instance_with_durations = instance.readlines()
		instance.seek(0)
		for line in instance_with_durations:
			if 'edge' in line: line = line.replace('))','),'+str(randint(int(args.durations[0]),int(args.durations[1])))+')')
			instance.writelines(line)

def get_horizon(timeout):
	global instanceFileName
	time_elapsed_meta = 0
	time_start_meta = time.time()
	if args.durations: solution = getoutput('clingo encodings/mif_inc_dur.lp ' + instanceFileName + ' -W none --outf=1 --time-limit=' + str(round(timeout)))
	else: solution = getoutput('clingo encodings/mif_inc.lp ' + instanceFileName + ' -W none --outf=1 --time-limit=' + str(round(timeout)))
	if (timeout<0) or ('INTERRUPTED' in solution): clean_up('\nTIMEOUT')
	if int(args.timeout) > 0: time_elapsed_meta = time.time() - time_start_meta
	if 'Calls' in solution:
		solution = solution.split("Calls          : ",1)[1]
		horizon = str(int(solution.split("% Time",1)[0])-1)

		if args.durations:
			acyc_out = getoutput('clingo encodings/mif_dur.lp -c acyclic=1 -c horizon=' + horizon + ' ' + instanceFileName + '--time-limit=' + str(round(timeout-time_elapsed_meta)))
		else: acyc_out = getoutput('clingo encodings/mif.lp -c acyclic=1 -c horizon=' + horizon + ' ' + instanceFileName + '--time-limit=' + str(round(timeout-time_elapsed_meta)))
		if ((timeout-time_elapsed_meta)<0) or ('INTERRUPTED' in acyc_out): clean_up('\nTIMEOUT')
		elif 'UN' in acyc_out: acyclic = ''
		else: acyclic = 'acyclic.'

		with open(instanceFileName[:-3] + '_meta.lp', 'w') as metaFile:
			metaFile.write('% meta information:\n' + '#const horizon=' + horizon + '.\nmakespan(horizon).\n' + acyclic)
	
	else: print(solution)

def get_shortest_paths(timeout):
	with open(instanceFileName[:-3] + '_SPs.lp', 'w') as SP_file:
		SP_file.write('')
	global max_SP_length
	max_SP_length = 0
	time_elapsed_SP_inloop = 0
	for agent in range(1,int(args.agents)+1):
		time_start_SP_inloop = time.time()
		time_remaining_SP = timeout - time_elapsed_SP_inloop
		numSPs='1'
		if args.allSPs: numSPs='0'
		if args.durations: shortest_paths = getoutput('clingo encodings/SP_dur.lp ' + instanceFileName + ' -c agent=' + str(agent) + ' -W none --out-atomf=%s. -V0 ' + numSPs + ' --time-limit=' + str(round(time_remaining_SP)) + ' | head -n -1')
		else: shortest_paths = getoutput('clingo encodings/SP.lp ' + instanceFileName + ' -c agent=' + str(agent) + ' -W none --out-atomf=%s. -V0 ' + numSPs + ' --time-limit=' + str(round(time_remaining_SP)) + ' | head -n -1')
		if 'INTERRUPTED' in shortest_paths: clean_up('\nTIMEOUT')
		
		with open(instanceFileName[:-3] + '_SPs.lp', 'a') as SP_file:
			SP_file.write('% agent ' + str(agent) + ':\n' + shortest_paths + '\n\n')
		if timeout>0: time_elapsed_SP_inloop = time_elapsed_SP_inloop + (time.time() - time_start_SP_inloop)

def run(function):
	global time_elapsed
	start_time = time.time()
	if not args.quiet: print('Running', '{:15s}'.format(function) + ' \t...', end=' ', flush=True)
	eval(function + '(' + str(int(args.timeout)-time_elapsed) + ')')
	if int(args.timeout) > 0: time_elapsed = time_elapsed + (time.time()-start_time)
	if not args.quiet: print('done (in ', "{:5.1f}".format(time.time()-start_time), ' seconds).')

def write(mode, string):
	with open(instanceFileName, mode) as instance:
		instance.write(string)

def clean_up(msg):
	print(msg)
	filenames_to_delete = [instanceFileName, instanceFileName[:-3]+'_SPs.lp', instanceFileName[:-3]+'_meta.lp']
	for filename in filenames_to_delete:
		if os.path.exists(filename):
			os.remove(filename)
			print('removed ' + filename)
	raise SystemExit()

def signal_handler(sig, frame): clean_up('\nKILLED BY SIGNAL')
signal.signal(signal.SIGINT,  signal_handler)
signal.signal(signal.SIGTERM, signal_handler)

parser       = argparse.ArgumentParser(usage='python gen.py (maze | random -c [0-100] | room -w WIDTH | warehouse -w WIDTH) -s SIZE -a AGENTS [-d DISTANCE] [-dur MINDUR MAXDUR] [-m] [-t TIMEOUT] [-v] [-h] [-q]')
req_group    = parser.add_argument_group('required arguments for all instance types')
room_group   = parser.add_argument_group('required arguments for room / warehouse type')
random_group = parser.add_argument_group('required arguments for random type')
parser.add_argument(      'type',                  help='type of instance to be generated',           choices=('maze', 'random', 'room', 'warehouse'))
parser.add_argument(             '--allSPs',       help='generates all shortest paths instead of one',action='store_true')
parser.add_argument(      '-d',  '--distance',     help='min. manhatten distance from start to goal', type=str, default='0')
parser.add_argument(      '-dur','--durations',    help='generates instances with durations',         type=str, nargs=2, metavar=('MINDUR', 'MAXDUR'))
parser.add_argument(      '-m',  '--meta',         help='gets and adds meta informations',            action='store_true')
parser.add_argument(      '-q',  '--quiet',        help='turns on quiet mode',                        action='store_true')
parser.add_argument(      '-t',  '--timeout',      help='sets a timeout in seconds',                  type=str, default='0')
parser.add_argument(      '-v',  '--visualize',    help='convert to and visualize with asprilo',      action='store_true')
req_group.add_argument(   '-s',  '--size',         help='size of instance',                           type=str, required=True)
req_group.add_argument(   '-a',  '--agents',       help='number of agents',                           type=str, required=True)
room_group.add_argument(  '-w',  '--width',        help='width of rooms',                             type=str)
random_group.add_argument('-c',  '--cover',        help='percentage of vertices covered',             type=str, metavar='[0-100]')
args = parser.parse_args()
if args.type == 'random' and (args.cover is None or int(args.cover) < 0 or int(args.cover) > 100): raise parser.error('random requires -c/--cover: percentage of vertices covered (must be INT between 0 and 100)')
if (args.type == 'room' or args.type == 'warehouse') and args.width is None: raise parser.error('room/warehouse require -w/--width: width of rooms/shelves')

time_elapsed = 0
run('create_instance')
run('add_agents')
if args.durations: run('add_durations')
run('add_header')
if args.meta:
	run('get_shortest_paths')
	run('get_horizon')

if args.visualize: os.system('clingo ' + instanceFileName + ' encodings/mif_to_asprilo.lp | viz')
