#TODO:	- enable generation of multiple instances in folder structure
#	- in case of multiple generations of instances with same parameters, change randomness and append number to filename instead of overwriting
#	- test if instance is SAT with mif encoding (or something faster but suboptimal) and allow enabling via argument (maybe also add min. horizon to instance)
#	- enable generation of same instance with variations of agent numbers
#	- get length of shortest paths for each agent and append to instance

import argparse, os
from subprocess import getoutput

def agents():
	global instance_filled
	instance_filled = getoutput('clingo ' + instanceFileName + ' encodings/task.lp -c r=' + args.agents + ' --rand-freq=1 -V0 --out-atomf=%s. --out-ifs="\n" | head -n -1')

def header():
	header = '%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%\n%\n% Size X and Y:\t\t' + str(int(args.size)*2) + '\n% Number of Agents:\t\t' + args.agents
	if args.type == 'random': header = header + '\n% Vertices used (in %):\t' + str(args.cover)
	if args.type == 'room':   header = header + '\n% Room Width:\t\t\t' + args.width
	header = header + '\n%\n%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%\n\n#program base.\n\n'
	return header

def maze():
	global instanceFileName, instance_unfilled
	instanceFileName  = 'maze_s' + args.size + '_a' + args.agents +'.lp'
	instance_unfilled = getoutput('clingo encodings/maze.lp -c w=' + args.size + ' --rand-freq=1 -V0 --out-atomf=%s. --out-ifs="\n" | head -n -1') 

def random():
	global instanceFileName, instance_unfilled
	if args.cover is None: raise parser.error('random requires -c/--cover: percentage of vertices covered')
	elif args.cover < 0 or args.cover > 100: raise argparse.ArgumentTypeError('argument -c/--cover: int value must be between 0 and 100')
	instanceFileName  = 'random_s' + args.size + '_a' + args.agents + '_c' + str(args.cover) +'.lp'
	numVertices       = str(int(((int(args.size)*int(args.size))/100)*args.cover))
	instance_unfilled = getoutput('clingo encodings/random.lp -c x=' + args.size + ' -c y=' + args.size + ' -c v=' + numVertices + ' --rand-freq=1 -V0 --out-atomf=%s. --out-ifs="\n" | head -n -1')

def room():
	global instanceFileName, instance_unfilled
	if args.width is None: raise parser.error('room requires -w/--width: width of rooms')
	instanceFileName  = 'room_s' + args.size + '_a' + args.agents + '_w' + str(args.width) +'.lp'
	instance_unfilled = getoutput('clingo encodings/room.lp -c x=' + args.size + ' -c y=' + args.size + ' -c w=' + args.width + ' --rand-freq=1 --configuration=frumpy -V0 --out-atomf=%s. --out-ifs="\n" | head -n -1')

def write(mode, string):
	with open(instanceFileName, mode) as instance:
		instance.write(string)

parser = argparse.ArgumentParser(usage='gen.py (maze | random -c [0-100] | room -w WIDTH) -s SIZE -a AGENTS [-v] [-h]')
parser.add_argument('type', 			help='type of instance to be generated', choices=('maze', 'random', 'room'))
parser.add_argument("-v", "--visualize",	help="convert generated instance to asprilo format and visualize it with asprilo visualizer", action='store_true')
# TODO: parser.add_argument("-t", "--test",		help="test if generated instance is solvable",		action='store_true')
req_group = parser.add_argument_group('required arguments for all')
req_group.add_argument("-s", "--size",	help="size of instance",			type=str, required=True)
req_group.add_argument("-a", "--agents",	help="number of agents",			type=str, required=True)
room_group = parser.add_argument_group('required arguments for room')
room_group.add_argument("-w", "--width",	help="width of rooms",				type=str)
random_group = parser.add_argument_group('required arguments for random')
random_group.add_argument("-c", "--cover",	help="percentage of vertices covered",	type=int, metavar="[0-100]")
args = parser.parse_args()

if args.type == 'maze': maze()
if args.type == 'random': random()
if args.type == 'room': room()
write('w', instance_unfilled)
agents()
write('w', header())
write('a', instance_filled)
if args.visualize: os.system('clingo ' + instanceFileName + ' encodings/mif_to_asprilo.lp | viz')
