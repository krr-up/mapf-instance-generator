# Generator for the [league of robot runners](https://www.leagueofrobotrunners.org/) format

A detailed description of the format can be found [here](https://github.com/MAPF-Competition/Start-Kit/blob/main/Input_Output_Format.md)

## Usage
### Map:
Requieres type of map to be generated and the map size.  
`python map_gen.py warehouse -x 50 -y 25`
### Agents:
Requieres path to the map file and the number of agents.  
`python agents_gen.py example.map -n 100`
### Tasks:
Requieres path to the map file and the number of tasks.  
`python tasks_gen.py example.map -n 1000`
