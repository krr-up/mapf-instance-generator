### Various MAPF instance generators for the [lightweight MAPF instance format](https://github.com/krr-up/mapf-instance-format)
___

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
