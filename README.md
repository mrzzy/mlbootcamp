# mlbootcamp
ML Bootcamp - Learning materials

## Introduction 
This repository contains the learning materials for ML boocamp.

## Prerequisites
`git` has to be installed

## Setup
1. Install [miniconda](https://docs.conda.io/en/latest/miniconda.html).
2. Open a terminal/cmd and create conda environment with Jupyterlab
```
conda create -n mlbootcamp jupyterlab python=3.6
```
3. Activate the conda environment with 
```
conda activate mlbootcamp
```
4. Create a kernel for conda environment to use it in Jupyterlab
```
python -m ipykernel install --user --name mlbootcamp --display-name "mlbootcamp-py3"
```
5. Clone this repository by
```
git clone https://github.com/mrzzy/mlbootcamp.git
```
6. Change directory into the repository
```
cd mlbootcamp
```
7. Profit. You are all set

## Usage
Once you have complete setup, to use your installation:
1. Change directory into the repository - use '\\' on windows instead of '/'
```
cd <where you put the mlbootcamp>/mlbootcamp 
```
2. Acivate the conda environment
```
conda activate mlbootcamp
```
3. Start the Jupyterlab server
```
python -m jupyter lab
```
4. Profit. You are all set.

## Project Infomation
### Project Structure
- practicals/ - jupyter notebooks for practicals
    - setup_install.ipynb - setup and module install
    - day_1/ - jupyter notebooks for day 1
        - practical_1_1 - practical 1.1
        - practical_1_2 - practical 1.2
        - practical_2 - practical 2
    - day_2/ - jupyter notebooks for day 2
        - practical_1_1 - practical 1.1
        - practical_1_2 - practical 1.2
        - practical_2 - practical 2
    - day_3/ - jupyter notebooks for day 3
- assignments/ - assignment infomatio

### Project Status
- OK project syllabus
- OK practicals
    - OK practical 1.1
    - OK practical 1.2
    - OK practical 2
    - OK practical 3
    - practical 4
    - practical 5
    - practical 6
