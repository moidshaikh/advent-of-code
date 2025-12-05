# Advent of Code Solutions

This repository contains solutions for the Advent of Code challenges, organized by year and day. The project structure promotes code reuse while keeping the challenges manageable.

## Directory Structure
```
advent_of_code/
├── inputs/
│   ├── 2021/
│   │   ├── dec01.in         # Input file for Day 1 of 2021
│   │   ├── dec02.in         # Input file for Day 2 of 2021
│   │   └── ...              # Additional inputs for 2021
│   ├── 2022/
│   │   ├── dec01.in         # Input file for Day 1 of 2022
│   │   ├── dec02.in         # Input file for Day 2 of 2022
│   │   └── ...              # Additional inputs for 2022
├── solutions/
│   ├── 2021/
│   │   ├── dec01.py         # Solution file for Day 1 of 2021
│   │   ├── dec02.py         # Solution file for Day 2 of 2021
│   │   └── ...              # Additional solutions for 2021
│   ├── 2022/
│   │   ├── dec01.py         # Solution file for Day 1 of 2022
│   │   ├── dec02.py         # Solution file for Day 2 of 2022
│   │   └── ...              # Additional solutions for 2022
├── common.py                # Common utility functions for all years
└── main.py                  # Centralized entry point for all years
```
## Usage

To run a specific problem for a given year, use the following command in your terminal:

python main.py <year> <problem_number> <problem_part>

- `<year>`: The year of the challenge (e.g., `2021`).
- `<problem_number>`: The day of the challenge (e.g., `1` for December 1st).
- `<problem_part>`: The part of the problem to solve (either `1` or `2`).

### Example Commands
✔ Normal run
python main.py 2015 3 1

✔ Run tests for that day
python main.py 2015 3 1 --test

✔ Measure time
python main.py 2015 3 1 --time

✔ Scalability
python main.py 2015 3 1 --scale

### Sample Commands for Makefile

✔ **Create solution folder/files:**  
`make create YEAR=2025 DAY=03`  

✔ **Normal run:**  
`make run YEAR=2025 DAY=03 PART=1`  

✔ **Run tests for that day:**  
`make test YEAR=2025 DAY=03`  

✔ **Measure time:**  
`make time YEAR=2025 DAY=03 PART=1`  

✔ **Scalability test:**  
- need to write inputs for scalability performance
`make scale YEAR=2023 DAY=10 PART=1`  

✔ **Download input file:**  
[TODO]
`make download YEAR=2022 DAY=07`  

✔ **Clean temporary files:**  
`make clean`  


## Features

- **Modular Solutions**: Each year's problem solutions are encapsulated in individual files located in the `solutions/` directory for that year.
- **Common Utilities**: Shared functions and helpers are maintained in `common.py`, promoting code reuse across different years.
- **Input Handling**: Inputs are read from the `inputs/` directory corresponding to each year, ensuring easy management of data files.
- **Logging**: Comprehensive logging for both successes and errors facilitates debugging and tracking progress.
- **Makefile**: Added Makefile and commands for basic usage.

## Contributions

Feel free to contribute to the solutions or improvements to the utilities in `common.py`. When adding a new problem, simply create a new file in the corresponding `solutions/` directory and add the appropriate input file in the `inputs/` directory.

## License

This project is licensed under the MIT License. See the LICENSE file for more details.


## iPython:
Using below 2 commands will reload the functions before execution
In [1]: %load_ext autoreload

In [2]: %autoreload 2