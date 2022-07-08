### Various MAPF instance generators for the [lightweight MAPF instance format](https://github.com/krr-up/mapf-instance-format)
___

- [maze.lp](https://github.com/krr-up/mapf-instance-generators/blob/main/maze.lp): Generates a fully connected maze with dead ends

  usage: `clingo maze.lp --rand-freq=1 -c w=4`
  <details><summary><strong>Example</strong></summary>
  
  ![example of a maze](https://github.com/krr-up/mapf-instance-generators/blob/main/examples/maze.png "")
  
  </details>

- [maze_inf.lp](https://github.com/krr-up/mapf-instance-generators/blob/main/maze_inf.lp): Generates a fully connected infinite maze

  usage: `clingo maze_inf.lp --rand-freq=1 -c w=4`
  <details><summary><strong>Example</strong></summary>
  
  ![example of a maze](https://github.com/krr-up/mapf-instance-generators/blob/main/examples/maze_inf.png "")
  
  </details>
  
- [task.lp](https://github.com/krr-up/mapf-instance-generators/blob/main/task.lp): Inserts tasks

  usage: `clingo instance.lp task.lp -c r=2`
