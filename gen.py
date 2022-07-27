# TODO:	- enable generation of multiple instances in folder structure
#		- include number of vertices in header of maze instances
#		- in case of multiple generations of instances with same parameters, change randomness and append number to filename
#		- test if instance is SAT with mif encoding and enabling via argument (maybe also add min. horizon to instance)
#		- enable generation of same instance with variations of agent numbers
#		- get length of shortest paths for each agent and append to instance

import argparse, os
from subprocess import getoutput

parser = argparse.ArgumentParser()
parser.add_argument("-s", "--size",		help="Size of instance",			type=str)
parser.add_argument("-a", "--agents",		help="Number of agents",			type=str)
parser.add_argument("-c", "--cover",		help="Percentage of vertices covered",	type=int)
parser.add_argument("-m", "--maze",		help="Generate a maze",			action='store_true')
parser.add_argument("-r", "--random",		help="Generate a random instance",		action='store_true')
parser.add_argument("-v", "--visualize",	help="Convert generated instance to asprilo format and visualize it with asprilo visualizer", action='store_true')
# TODO: parser.add_argument("-t", "--test",		help="Tests if generated instance is solvable",		action='store_true')
args = parser.parse_args()

if args.maze:
	instanceFileName  = 'maze_s' + args.size + '_a' + args.agents +'.lp'
	instance_unfilled = getoutput('clingo encodings/maze.lp -c w=' + args.size + ' --rand-freq=1 -V0 --out-atomf=%s. --out-ifs="\n" | head -n -1') 
	instanceHeader    = '%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%\n%\n% Grid Size X:\t\t\t' + str(int(args.size)*2) + '\n% Grid Size Y:\t\t\t' + str(int(args.size)*2) + '\n% Number of Agents:\t\t' + args.agents + '\n%\n%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%\n\n#program base.\n\n'

if args.random:
	instanceFileName  = 'random_s' + args.size + '_a' + args.agents + '_c' + str(args.cover) +'.lp'
	numVertices       = str(int(((int(args.size)*int(args.size))/100)*args.cover))
	instance_unfilled = getoutput('clingo encodings/random.lp -c w=' + args.size + ' -c v=' + numVertices + ' --rand-freq=1 -V0 --out-atomf=%s. --out-ifs="\n" | head -n -1')
	instanceHeader    = '%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%\n%\n% Grid Size X:\t\t\t\t' + args.size + '\n% Grid Size Y:\t\t\t\t' + args.size + '\n% Possible vertices used (in %):\t' + str(args.cover) + '\n% Number of Vertices:\t\t\t' + numVertices + '\n% Number of Agents:\t\t\t' + args.agents + '\n%\n%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%\n\n#program base.\n\n'

with open(instanceFileName, "w") as instance:
	instance.write(instance_unfilled)
	
instance_filled = getoutput('clingo ' + instanceFileName + ' encodings/task.lp -c r=' + args.agents + ' --rand-freq=1 -V0 --out-atomf=%s. --out-ifs="\n" | head -n -1')

with open(instanceFileName, "w") as instance:
	instance.write(instanceHeader)

with open(instanceFileName, "a") as instance:
	instance.write(instance_filled)
	
if args.visualize: os.system('clingo ' + instanceFileName + ' encodings/mif_to_asprilo.lp | viz')
