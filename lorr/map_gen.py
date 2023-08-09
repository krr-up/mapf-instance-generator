import argparse
from subprocess import getoutput


def sortation(x, y, instance):
    instance_lp = getoutput(f'clingo sortation.lp -V0 --out-ifs="\n" -c x={args.x} -c y={args.y} | head -n -1')

    for line in instance_lp.split('\n'):
        if 'vertex' in line:
            col = int(line.split('vertex((')[1].split(',')[0])-1
            row = int(line.split(',')[1].split('))')[0])-1
            if instance[row * (args.x + 1) + col] != 'E' and  instance[row * (args.x + 1) + col] != 'S':
                instance[row * (args.x + 1) + col] = '.'

        if 'emitter' in line:
            col = int(line.split('emitter((')[1].split(',')[0])-1
            row = int(line.split(',')[1].split('))')[0])-1
            instance[row * (args.x + 1) + col] = 'E'
        
        if 'service' in line:
            col = int(line.split('service((')[1].split(',')[0])-1
            row = int(line.split(',')[1].split('))')[0])-1
            instance[row * (args.x + 1) + col] = 'S'

    return instance


def warehouse(x, y, instance):
    instance_lp = getoutput(f'clingo warehouse.lp -V0 --out-ifs="\n" -c x={args.x} -c y={args.y} | head -n -1')

    for line in instance_lp.split('\n'):
        if 'vertex' in line:
            col = int(line.split('vertex((')[1].split(',')[0])-1
            row = int(line.split(',')[1].split('))')[0])-1
            if instance[row * (args.x + 1) + col] != 'E' and  instance[row * (args.x + 1) + col] != 'S':
                instance[row * (args.x + 1) + col] = '.'

        if 'emitter' in line:
            col = int(line.split('emitter((')[1].split(',')[0])-1
            row = int(line.split(',')[1].split('))')[0])-1
            instance[row * (args.x + 1) + col] = 'E'
        
        if 'service' in line:
            col = int(line.split('service((')[1].split(',')[0])-1
            row = int(line.split(',')[1].split('))')[0])-1
            instance[row * (args.x + 1) + col] = 'S'

    return instance


parser = argparse.ArgumentParser()
parser.add_argument('type', help='warehouse or sortation', type=str)
parser.add_argument('-x', type=int, required=True)
parser.add_argument('-y', type=int, required=True)
args = parser.parse_args()

instance = (['@'] * args.x + ['\n']) * args.y

if args.type == 'warehouse':
    if args.x > 18 and args.y > 17:
        instance = warehouse(args.x, args.y, instance)
    else:
        raise parser.error('Invalid warehouse map size! Make sure that: x>18 and y>17')
elif args.type == 'sortation':
    if args.x > 12 and args.y > 12:
        instance = sortation(args.x, args.y, instance)
    else:
        raise parser.error('Invalid sortation map size! Make sure that: x>12 and y>12')

header = f'''type octile
height {args.y}
width {args.x}
map 
'''
with open(f'{args.type}_x{args.x}_y{args.y}.map', 'w') as map_file:
    map_file.write(header + ''.join(instance))
