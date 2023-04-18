### Encodings
The generator makes use of the following ASP encodings that can also be used without the generator as follows:

- [random.lp](https://github.com/krr-up/mapf-instance-generators/blob/main/encodings/random.lp): Generates a random instance

  usage: `clingo random.lp --rand-freq=1 -c s=5 -c c=50`
  
- [maze.lp](https://github.com/krr-up/mapf-instance-generators/blob/main/encodings/maze.lp): Generates a fully connected maze with dead ends

  usage: `clingo maze.lp --rand-freq=1 -c s=4`

- [maze_inf.lp](https://github.com/krr-up/mapf-instance-generators/blob/main/encodings/maze_inf.lp): Generates a fully connected infinite maze (not part of gen.py as instances are not of much use)

  usage: `clingo maze_inf.lp --rand-freq=1 -c s=4`

- [room.lp](https://github.com/krr-up/mapf-instance-generators/blob/main/encodings/room.lp): Generates instance with rooms

  usage: `clingo room.lp --rand-freq=1 --configuration=frumpy -c s=20 -c w=5`
  
- [warehouse.lp](https://github.com/krr-up/mapf-instance-generators/blob/main/encodings/warehouse.lp): Generates warehouse instance

  usage: `clingo warehouse.lp -c s=20 -c a=10 -c w=5` 

- [agents.lp](https://github.com/krr-up/mapf-instance-generators/blob/main/encodings/agents.lp): Inserts agents, starts and goals

  usage: `clingo instance.lp agents.lp --rand-freq=1 --configuration=frumpy -c a=2 -c d=5`
