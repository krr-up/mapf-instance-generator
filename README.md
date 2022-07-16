### Various MAPF instance generators for the [lightweight MAPF instance format](https://github.com/krr-up/mapf-instance-format)
___
To be able to visualize the instances with the asprilo visualizer, use the converter: [mif_to_asprilo.lp](https://github.com/krr-up/mapf-instance-format/blob/main/mif_to_asprilo.lp).
- [random.lp](https://github.com/krr-up/mapf-instance-generators/blob/main/random.lp): Generates a random instance

  usage: `clingo random.lp --rand-freq=1 -c x=5 -c y=5 -c v=15`
  <details><summary><strong>Example</strong></summary>
  
  ![example of a random instance](https://github.com/krr-up/mapf-instance-generators/blob/main/examples/random.png "random instance example")
  
  </details>
  
- [maze.lp](https://github.com/krr-up/mapf-instance-generators/blob/main/maze.lp): Generates a fully connected maze with dead ends

  usage: `clingo maze.lp --rand-freq=1 -c w=4`
  <details><summary><strong>Example</strong></summary>
  
  ![example of a maze](https://github.com/krr-up/mapf-instance-generators/blob/main/examples/maze.png "maze example")
  
  </details>

- [maze_inf.lp](https://github.com/krr-up/mapf-instance-generators/blob/main/maze_inf.lp): Generates a fully connected infinite maze

  usage: `clingo maze_inf.lp --rand-freq=1 -c w=4`
  <details><summary><strong>Example</strong></summary>
  
  ![example of a maze](https://github.com/krr-up/mapf-instance-generators/blob/main/examples/maze_inf.png "infinite maze example")
  
  </details>
  
- [task.lp](https://github.com/krr-up/mapf-instance-generators/blob/main/task.lp): (WIP) Inserts tasks

  usage: `clingo instance.lp task.lp -c r=2`

- rooms.lp: (WIP) Generates instances with rooms

___
### Literature:
- [Answer Set Programming for Procedural Content Generation: A Design Space Approach](https://doi.org/10.1109/TCIAIG.2011.2158545)
- [ASP with Applications to Mazes and Levels](https://doi.org/10.1007/978-3-319-42716-4_8)
- [Stepping through an Answer-Set Program](https://doi.org/10.1007/978-3-642-20895-9_13)
