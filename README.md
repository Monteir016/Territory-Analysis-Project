# Territory-Analysis-Project

## Overview

This project implements a set of functions to analyze and manipulate territories represented as grids. It includes operations such as validating territories, identifying chains of connected intersections, and calculating specific properties like the number of mountains or valleys. This was my first coding project ever, marking the beginning of my programming journey.

## Features

- **Territory Validation**: Ensures the grid structure and its elements are valid.
- **Intersection Analysis**: Identifies adjacent intersections, checks connectivity, and determines free intersections.
- **Chain and Valley Calculations**: Computes chains of connected intersections and identifies valleys within the territory.
- **Graphical Representation**: Converts territories into a string format for visualization.

## How to Run

### Prerequisites

- **Python 3.x**: Ensure Python is installed on your system.

### Running the Program

1. Open a Python interpreter or create a script.
2. Import the functions from the project files:
   ```python
   from FP2324P1 import *
   ```
3. Use the functions to analyze territories.

**Example Usage**
1. Validate a Territory:
```
t = ((0, 1, 0), (1, 0, 1), (0, 1, 0))
print(eh_territorio(t))
```
2. Get the Last Intersection:
`print(obtem_ultima_intersecao(t))`
3. Calculate the Number of Mountains:
`print(calcula_numero_montanhas(t))`
4. Visualize the Territory:
`print(territorio_para_str(t))`

Output:
```
  A B C
3 . X .
2 X . X
1 . X .
  A B C
```

## Challenges and Learning
This project introduced me to the fundamentals of programming, including data structures, algorithms, and problem-solving. It was a challenging yet rewarding experience that laid the foundation for my coding skills.

## Author
Developed by Guilherme Monteiro. For more information, visit [my GitHub profile](https://github.com/Monteir016).
