import argparse, random
from subprocess import getoutput


def choose_agents(num_agents, poss_agents):
    agents = f'{num_agents}\n'
    agents_list = (random.sample(poss_agents, num_agents))
    for agent in agents_list:
        agents += f'{agent}\n'
    return agents


def get_poss_agents(map_file):
    for row in range(4):
        if 'type' in map_file[0] or 'height' in map_file[0] or 'width' in map_file[0] or 'map' in map_file[0]:
            map_file.pop(0)
            
    poss_agents = []
    for row in range(len(map_file)):
        for col in range(len(map_file[row])):
            if map_file[row][col] != '@':
                poss_agents.append(f'{row * len(map_file[row]) + col}')
    return poss_agents


def load_map(map_path):
    with open(f'{map_path}', 'r') as map_file:
        return map_file.read().splitlines()


def save_file(agents):
    with open(f'{args.map[:-4]}.agents', 'w') as agents_file:
        agents_file.write(agents)


parser = argparse.ArgumentParser()
parser.add_argument('map', help='path to map file', type=str)
parser.add_argument('-n', help='number of agents', type=int, required=True)
args = parser.parse_args()


if args.n < 1:
    raise parser.error('Number of agents n<1 !')
else:
    save_file(choose_agents(args.n, get_poss_agents(load_map(args.map))))
