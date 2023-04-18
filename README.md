### Instance generator for the [lightweight MAPF instance format](https://github.com/krr-up/mapf-instance-format)

![instance examples](https://github.com/krr-up/mapf-instance-generators/blob/main/examples/example.png "instance examples")

### Generator
#### Installation
Requires Conda to be installed.

To install download this repository and run  `conda env create --file reqs.yml` from the main folder. This will create a new environment called "gen" and install all required packages. Please remember to activate the correct environment using `conda activate gen` to be able to use the generator.

#### Usage
To generate instances use [gen.py](https://github.com/krr-up/mapf-instance-generators/blob/main/gen.py) as follows:

```
usage: python gen.py (maze | random -c [0-100] | room -w WIDTH | warehouse -w WIDTH | *.jpg | *.png | *.lp) -s SIZE -a AGENTS [-d DISTANCE] [-dur MINDUR MAXDUR] [-m] [-t TIMEOUT] [-v] [-h] [-q]


positional arguments:
  {maze,random,room,warehouse,*.jpg,*.png,*.lp}  type of instance to be generated, path to image to be converted or path to instance to be loaded

optional arguments:
  -h,                 --help                     show this help message and exit
                      --allSPs                   generates all shortest paths instead of one
  -d DISTANCE,        --distance DISTANCE        min. manhatten distance from start to goal
  -dur MINDUR MAXDUR, --durations MINDUR MAXDUR  generates instances with durations
  -m,                 --meta                     gets and adds meta informations
  -q,                 --quiet                    turns on quiet mode
  -t,                 --timeout                  sets a timeout in seconds
  -v,                 --visualize                convert to and visualize with asprilo


required arguments for all instance types:
  -s SIZE,            --size SIZE                size of instance
  -a AGENTS,          --agents AGENTS            number of agents

required arguments for room / warehouse type:
  -w WIDTH,           --width WIDTH              width of rooms / shelves

required arguments for random type:
  -c [0-100],         --cover [0-100]            percentage of vertices covered
  ```
Warning: As the used arguments impact the problem difficulty, long runtime is to be expected e.g. for high values for --size or low values for --cover.

### Visualize
To be able to visualize the instances with the asprilo visualizer, use the converter: [mif_to_asprilo.lp](https://github.com/krr-up/mapf-instance-format/blob/main/mif_to_asprilo.lp) like this:

usage: `clingo instance.lp mif_to_asprilo.lp | viz`
___
### Literature
- [Answer Set Programming for Procedural Content Generation: A Design Space Approach](https://doi.org/10.1109/TCIAIG.2011.2158545)
- [ASP with Applications to Mazes and Levels](https://doi.org/10.1007/978-3-319-42716-4_8)
- [Stepping through an Answer-Set Program](https://doi.org/10.1007/978-3-642-20895-9_13)
