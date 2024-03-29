The **MAPF Instance Generator** is a tool for generating instances of the Multi-Agent Path Finding (MAPF) problem in the [lightweight MAPF instance format](https://github.com/krr-up/mapf-instance-format). It is designed to help students and researchers create custom MAPF instances for testing and benchmarking purposes.

![instance examples](https://github.com/krr-up/mapf-instance-generators/blob/main/examples/example.png "instance examples")

<details open>
<summary>

### Installation
</summary>
Requires Conda to be installed.

To install download this repository and run  `conda env create --file reqs.yml` from the main folder. This will create a new environment called "gen" and install all required packages. Please remember to activate the correct environment using `conda activate gen` to be able to use the generator.
</details>

### Usage
<details open>
<summary>

#### Help message
</summary>

```
usage: python gen.py (empty | maze | random -c [0-100] | room -w WIDTH | warehouse -w WIDTH) -s SIZE -a AGENTS [-d DISTANCE] [-dir DIRECTORY] [-dur MINDUR MAXDUR] [-m] [-suf SUFFIX] [-t TIMEOUT] [-v] [-h] [-q]


positional arguments:
  {empty, maze, random, room, warehouse, *.jpg, *.png, *.lp}
                                                 type of instance to be generated, path to image to be converted or path to instance to be loaded
optional arguments:
  -h,                 --help                     show this help message and exit
  -a AGENTS,          --agents AGENTS            number of agents
  -acyc,              --acyclicity               checks acyclicity
                      --allSPs                   generates all shortest paths instead of one
  -c [0-100],         --cover [0-100]            percentage of vertices covered (default=75)
  -d DISTANCE,        --distance DISTANCE        min. manhatten distance from start to goal
  -dir DIRECTORY      --directory DIRECTORY      sets directory
  -dur MINDUR MAXDUR, --durations MINDUR MAXDUR  generates instances with durations
  -m,                 --makespan                 searches for minimal makespan
  -q,                 --quiet                    turns on quiet mode
  -sp,                --shortest_paths           searches for shortest paths
  -suf SUFFIX,        --suffix SUFFIX            appends suffix to filename
  -t,                 --timeout                  sets a timeout in seconds
  -v,                 --visualize                convert to and visualize with asprilo
  -w WIDTH,           --width WIDTH              width of rooms / shelves (default=5)

required arguments for all instance types:
  -s X-SIZE Y-SIZE,   --size X-SIZE Y-SIZE       size of instance
  ```
</details>

### Examples

#### Generation
##### Empty
`python gen.py empty -s 10 10 -a 5 -dur 1 5` generates an empty 10x10 instance with 5 agents and random durations between 1 and 5 of the edges.
##### Maze
`python gen.py maze -s 10 10 -a 5 -dir "mazes"` generates a 10x10 maze instance with 5 agents and saves it in the directory "mazes".
##### Random
`python gen.py random -s 10 10 -a 5 -c 55` generates a 10x10 random instance with 5 agents where 55% of the space is covered by nodes resulting in 45% being random obstacles.
##### Room
`python gen.py room -s 10 10 -a 5 -w 5` generates a 10x10 room instance with 5 agents where every room has a size of 5x5 nodes.

#### Change instance
`python gen.py instance.lp -a 12` changes the number of agents of an instance to 12.
  
<details open>
<summary>

#### Convert image to instance
</summary>

`python gen.py image.jpg -s 10 10` converts an image to a 10x10 instance.
<table>
  <thead>
    <tr>
      <th width="600px align="center""><img src="https://user-images.githubusercontent.com/80356280/233345961-daa686b4-9ce1-4498-8b6b-75a26a0020a3.jpg"></th>
      <th width="600px align="center""><img src="https://user-images.githubusercontent.com/80356280/233345833-9fbc98f7-7a1a-4868-b708-5b1e7e114bec.png"></th>
    </tr>
  </thead>
  <tbody>
  <tr width="600px" align="center">
      <td>
        <img src="https://user-images.githubusercontent.com/80356280/233344560-25b5a86e-05b7-4a09-a831-080a11ce9cf8.png">
      </td>
      <td>
        <img src="https://user-images.githubusercontent.com/80356280/233344577-d8eba2f2-0b03-45be-b5f6-2f29e29b2db6.png">
      </td>
  </tr>
  </tbody>
</table>
</details>

#### Meta Information
##### Makespan
The `-m` option saves the minimal makespan in a seperate meta file.
##### Shortest Paths
The `-sp` option saves the shortest path in a seperate file.
##### Acyclicity
The `-acyc` option checks if the instance is solvable without any of the agents performing cycles. If so the fact `acyclic.` is added to the meta file.
#### Timeout
`-t 600` sets a 10 minutes timeout for the generation. 
#### Quiet
Use `-q` to have no status output at all
#### Visualization
To automatically visualize the instance at the end of the process use the `-v` option.

To visualize the instances at a later time use the asprilo visualizer with the converter: [mif_to_asprilo.lp](https://github.com/krr-up/mapf-instance-format/blob/main/mif_to_asprilo.lp) like this: `clingo instance.lp mif_to_asprilo.lp | viz`
___
### Literature
- [Answer Set Programming for Procedural Content Generation: A Design Space Approach](https://doi.org/10.1109/TCIAIG.2011.2158545)
- [ASP with Applications to Mazes and Levels](https://doi.org/10.1007/978-3-319-42716-4_8)
- [Stepping through an Answer-Set Program](https://doi.org/10.1007/978-3-642-20895-9_13)
