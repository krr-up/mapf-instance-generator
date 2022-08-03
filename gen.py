#TODO:	- enable generation of multiple instances in folder structure
#	- include number of vertices in header of maze instances
#	- in case of multiple generations of instances with same parameters, change randomness and append number to filename instead of overwriting
#	- test if instance is SAT with mif encoding (or something faster but suboptimal) and allow enabling via argument (maybe also add min. horizon to instance)
#	- enable generation of same instance with variations of agent numbers
#	- get length of shortest paths for each agent and append to instance

import argparse, os
from subprocess import getoutput

################ Argument Parser ################
parser      = argparse.ArgumentParser(usage='gen.py (maze | random -c [0-100] | room -w WIDTH) -s SIZE -a AGENTS [-v] [-h]')
subparsers  = parser.add_subparsers()
maze_parser = subparsers.add_parser('maze')
rand_parser = subparsers.add_parser('random')
room_parser = subparsers.add_parser('room')
maze_parser.add_argument("maze",		help="generate maze",			action='store_true')
rand_parser.add_argument("random",		help="generate random instance",	action='store_true')
room_parser.add_argument("room",		help="generate instance with rooms",	action='store_true')
req_group    = parser.add_argument_group('required arguments for all')
room_group   = parser.add_argument_group('required arguments for room')
random_group = parser.add_argument_group('required arguments for random')
req_group.add_argument("-s", "--size",	help="size of instance",			type=str, required=True)
req_group.add_argument("-a", "--agents",	help="number of agents",			type=str, required=True)
random_group.add_argument("-c", "--cover",	help="percentage of vertices covered",	type=int, default=50, metavar="[0-100]")
room_group.add_argument("-w", "--width",	help="width of rooms",				type=str)
parser.add_argument("-v", "--visualize",	help="convert generated instance to asprilo format and visualize it with asprilo visualizer", action='store_true')
# TODO: parser.add_argument("-t", "--test",		help="Tests if generated instance is solvable",		action='store_true')
args = parser.parse_args()
if args.cover < 0 or args.cover > 100: raise argparse.ArgumentTypeError('argument -c/--cover: int value must be between 0 and 100')

################ Maze generation ################
if args.maze:
	instanceFileName  = 'maze_s' + args.size + '_a' + args.agents +'.lp'
	instance_unfilled = getoutput('clingo encodings/maze.lp -c w=' + args.size + ' --rand-freq=1 -V0 --out-atomf=%s. --out-ifs="\n" | head -n -1') 
	instanceHeader    = '''%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%
% Grid Size X:\t\t\t''' + str(int(args.size)*2) + '''
% Grid Size Y:\t\t\t''' + str(int(args.size)*2) + '''
% Number of Agents:\t\t''' + args.agents + '''
%
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

#program base.

'''

################ Random generation ##############
if args.random:
	instanceFileName  = 'random_s' + args.size + '_a' + args.agents + '_c' + str(args.cover) +'.lp'
	numVertices       = str(int(((int(args.size)*int(args.size))/100)*args.cover))
	instance_unfilled = getoutput('clingo encodings/random.lp -c x=' + args.size + ' -c y=' + args.size + ' -c v=' + numVertices + ' --rand-freq=1 -V0 --out-atomf=%s. --out-ifs="\n" | head -n -1')
	instanceHeader    ='''%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%
% Grid Size X:\t\t\t\t''' + args.size + '''
% Grid Size Y:\t\t\t\t''' + args.size + '''
% Possible vertices used (in %):\t''' + str(args.cover) + '''
% Number of Vertices:\t\t\t''' + numVertices + '''
% Number of Agents:\t\t\t''' + args.agents + '''
%
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

#program base.

'''

################ Room generation ################
if args.room:
	instanceFileName  = 'room_s' + args.size + '_a' + args.agents + '_w' + str(args.width) +'.lp'
	instance_unfilled = getoutput('clingo encodings/room.lp -c x=' + args.size + ' -c y=' + args.size + ' -c w=' + args.width + ' --rand-freq=1 --configuration=frumpy -V0 --out-atomf=%s. --out-ifs="\n" | head -n -1')
	instanceHeader    ='''%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%
% Grid Size X:\t\t''' + args.size + '''
% Grid Size Y:\t\t''' + args.size + '''
% Room Width:\t\t''' + args.width + '''
% Number of Agents:\t''' + args.agents + '''
%
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

#program base.

'''

with open(instanceFileName, "w") as instance:
	instance.write(instance_unfilled)
	
instance_filled = getoutput('clingo ' + instanceFileName + ' encodings/task.lp -c r=' + args.agents + ' --rand-freq=1 -V0 --out-atomf=%s. --out-ifs="\n" | head -n -1')

with open(instanceFileName, "w") as instance:
	instance.write(instanceHeader)

with open(instanceFileName, "a") as instance:
	instance.write(instance_filled)

################ Convert to asprilo and visualize ################
if args.visualize: os.system('clingo ' + instanceFileName + ' encodings/mif_to_asprilo.lp | viz')
