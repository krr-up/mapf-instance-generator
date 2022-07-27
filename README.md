### Various MAPF instance generators for the [lightweight MAPF instance format](https://github.com/krr-up/mapf-instance-format)
___

To generate instances use [gen.py](https://github.com/krr-up/mapf-instance-generators/blob/main/gen.py) as follows:

```
usage: gen.py [-h] [-s SIZE] [-a AGENTS] [-c COVER] [-m] [-r] [-v]

optional arguments:
  -h,        --help           Show this help message and exit
  -s SIZE,   --size SIZE      Size of instance
  -a AGENTS, --agents AGENTS  Number of agents
  -c COVER,  --cover COVER    Percentage of vertices covered
  -m,        --maze           Generate a maze
  -r,        --random         Generate a random instance
  -v,        --visualize      Convert generated instance to asprilo format and visualize it with asprilo visualizer
  ```
The generator makes use of the following encodings that can also be used without the generator as follows:

- [random.lp](https://github.com/krr-up/mapf-instance-generators/blob/main/encodings/random.lp): Generates a random instance

  usage: `clingo random.lp --rand-freq=1 -c x=5 -c y=5 -c v=15`
  <details><summary><strong>Example</strong></summary>
  
  ![example of a random instance](https://github.com/krr-up/mapf-instance-generators/blob/main/examples/random.png "random instance example")
  
  </details>
  
- [maze.lp](https://github.com/krr-up/mapf-instance-generators/blob/main/encodings/maze.lp): Generates a fully connected maze with dead ends

  usage: `clingo maze.lp --rand-freq=1 -c w=4`
  <details><summary><strong>Example</strong></summary>
  
  ![example of a maze](https://github.com/krr-up/mapf-instance-generators/blob/main/examples/maze.png "maze example")
  
  </details>

- [maze_inf.lp](https://github.com/krr-up/mapf-instance-generators/blob/main/encodings/maze_inf.lp): Generates a fully connected infinite maze

  usage: `clingo maze_inf.lp --rand-freq=1 -c w=4`
  <details><summary><strong>Example</strong></summary>
  
  ![example of a maze](https://github.com/krr-up/mapf-instance-generators/blob/main/examples/maze_inf.png "infinite maze example")
  
  </details>
  
- [task.lp](https://github.com/krr-up/mapf-instance-generators/blob/main/encodings/task.lp): Inserts agents, starts and goals

  usage: `clingo instance.lp task.lp -c r=2`

- rooms.lp: (WIP) Generates instances with rooms

To be able to visualize the instances with the asprilo visualizer, use the converter: [mif_to_asprilo.lp](https://github.com/krr-up/mapf-instance-format/blob/main/mif_to_asprilo.lp).
___
### Literature:
- [Answer Set Programming for Procedural Content Generation: A Design Space Approach](https://doi.org/10.1109/TCIAIG.2011.2158545)
- [ASP with Applications to Mazes and Levels](https://doi.org/10.1007/978-3-319-42716-4_8)
- [Stepping through an Answer-Set Program](https://doi.org/10.1007/978-3-642-20895-9_13)
