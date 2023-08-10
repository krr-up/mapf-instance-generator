import argparse, random
from subprocess import getoutput


def choose_tasks(num_tasks, poss_tasks):
    tasks = f'{num_tasks}\n'
    for n in range(num_tasks):
        tasks += f'{random.choice(poss_tasks)}\n'
    return tasks


def get_poss_tasks(map_file):
    for row in range(4):
        if 'type' in map_file[0] or 'height' in map_file[0] or 'width' in map_file[0] or 'map' in map_file[0]:
            map_file.pop(0)

    poss_tasks = []
    for row in range(len(map_file)):
        for col in range(len(map_file[row])):
            if map_file[row][col] in ['E', 'S']:
                poss_tasks.append(f'{row * len(map_file[row]) + col}')
    return poss_tasks


def load_map(map_path):
    with open(f'{map_path}', 'r') as map_file:
        return map_file.read().splitlines()


def save_file(tasks):
    with open(f'{args.map[:-4]}.tasks', 'w') as task_file:
        task_file.write(tasks)


parser = argparse.ArgumentParser()
parser.add_argument('map', help='path to map file', type=str)
parser.add_argument('-n', help='number of tasks', type=int, required=True)
args = parser.parse_args()


if args.n < 1:
    raise parser.error('Number of tasks n<1 !')
else:
    save_file(choose_tasks(args.n, get_poss_tasks(load_map(args.map))))
