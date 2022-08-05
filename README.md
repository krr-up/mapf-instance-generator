### Instance generator for the [lightweight MAPF instance format](https://github.com/krr-up/mapf-instance-format)

![instance examples](https://github.com/krr-up/mapf-instance-generators/blob/main/examples/example.png "instance examples")

To generate instances use [gen.py](https://github.com/krr-up/mapf-instance-generators/blob/main/gen.py) as follows:

```
usage: gen.py (maze | random -c [0-100] | room -w WIDTH) -s SIZE -a AGENTS [-v] [-h]

positional arguments:
  {maze,random,room}

optional arguments:
  -h,         --help           show this help message and exit
  -v,         --visualize      convert generated instance to asprilo format and visualize it with asprilo visualizer

required arguments for all:
  -s SIZE,    --size SIZE      size of instance
  -a AGENTS,  --agents AGENTS  number of agents

required arguments for room:
  -w WIDTH,   --width WIDTH    width of rooms

required arguments for random:
  -c [0-100], --cover [0-100]  percentage of vertices covered
  ```
The generator makes use of the following encodings that can also be used without the generator as follows:

- [random.lp](https://github.com/krr-up/mapf-instance-generators/blob/main/encodings/random.lp): Generates a random instance

  usage: `clingo random.lp --rand-freq=1 -c s=5 -c v=15`
  
- [maze.lp](https://github.com/krr-up/mapf-instance-generators/blob/main/encodings/maze.lp): Generates a fully connected maze with dead ends

  usage: `clingo maze.lp --rand-freq=1 -c s=4`

- [maze_inf.lp](https://github.com/krr-up/mapf-instance-generators/blob/main/encodings/maze_inf.lp): Generates a fully connected infinite maze

  usage: `clingo maze_inf.lp --rand-freq=1 -c s=4`

- [room.lp](https://github.com/krr-up/mapf-instance-generators/blob/main/encodings/room.lp): Generates instances with rooms

  usage: `clingo room.lp --rand-freq=1 --configuration=frumpy -c s=20 -c w=5` 

- [task.lp](https://github.com/krr-up/mapf-instance-generators/blob/main/encodings/task.lp): Inserts agents, starts and goals

  usage: `clingo instance.lp task.lp --rand-freq=1 -c r=2 `

To be able to visualize the instances with the asprilo visualizer, use the converter: [mif_to_asprilo.lp](https://github.com/krr-up/mapf-instance-format/blob/main/mif_to_asprilo.lp).
___
### Literature:
- [Answer Set Programming for Procedural Content Generation: A Design Space Approach](https://doi.org/10.1109/TCIAIG.2011.2158545)
- [ASP with Applications to Mazes and Levels](https://doi.org/10.1007/978-3-319-42716-4_8)
- [Stepping through an Answer-Set Program](https://doi.org/10.1007/978-3-642-20895-9_13)
