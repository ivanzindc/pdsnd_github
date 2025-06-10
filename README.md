## Original Project Instructions from Udacity
>**Note**: Please **fork** the current Udacity repository so that you will have a **remote** repository in **your** Github account. Clone the remote repository to your local machine. Later, as a part of the project "Post your Work on Github", you will push your proposed changes to the remote repository in your Github account.

### Date created
This README file was created on 6/10/25.
The project itself was developed in May of 2025.

### Project Title
Exploration of US Bikeshare Data

### Description
This Python program loads, filters, displays data (on request) and computes statistics on bikeshare data 
for Chicago, New York City, and Washington, DC based on user inputs.

## Table of Contents
1. [Prerequisites](#prerequisites)  
2. [Installation](#installation)  
3. [Instructions and Explanations](#instructions-and-explanations)  
4. [Files used](#files-used)  
5. [Project Structure](#project-structure)  
6. [Credits](#credits)  

### Prerequisites
- Python 3.7+
- pandas, NumPy, matplotlib (`pip install -r requirements.txt`)

## Installation
```bash
git clone https://github.com/ivanzindc/pdsnd_github.git
cd pdsnd_github
pip install -r requirements.txt
```

### Instructions and Explanations

Please run the script in the terminal and follow the prompts.

I added a matplotlib visualization of busiest locations for chosen filters.
It will be produced in a separate window if your terminal allows GUI.

### Files used
Data for queries resides in 3 files:
- chicago.csv
- new_york_city.csv
- washington.csv

Udacity specifically asked not to upload working datasets 
(Randomly selected data for the first six months of 2017 for all three cities) 
to github, but similar datasets live on:

- [Capital Bikeshare](https://capitalbikeshare.com/system-data)
- [Citi Bike NYC](https://citibikenyc.com/system-data)
- [DivvyBikes (for Chicago)](https://divvybikes.com/system-data)

Project template file was provided by Udacity.

### Project Structure
- **pdsnd_github/**
  - `.gitignore` # Git ignore rules
  - `bikeshare_2.py` # Main script
  - `requirements.txt` # Python dependencies
  - `README.md` # Project documentation

### Credits
Documentation and troubleshooting resources used include: 
   * [pandas documentation](https://pandas.pydata.org/)
   * [Official Python docs](https://docs.python.org/)
   * [StackOverflow](https://stackoverflow.com/)
   * [GeeksforGeeks educational portal](https://www.geeksforgeeks.org/)
