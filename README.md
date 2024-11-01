**---Scientist Graph Visualization---**

This project visualizes a graph of scientists, where the names of scientists are represented as nodes, and connections between them are created if they have lived during the same time period. The visualization provides a unique way to explore relationships between scientists based on their lifetimes.


**Project Overview**

The primary goal of this project is to visualize connections between scientists based on historical data, using graph theory. The project utilises Python libraries to create and display an interactive graph where:

Nodes represent individual scientists.
Edges (connections) exist between scientists if they have lived during overlapping time periods.


**Key Features**

Graph Theory Application: The project builds a graph where each scientist is a node, and edges are drawn between nodes based on the scientists' lifetimes.
Data Visualization: The graph is visually represented using pyvis.network module.


**Dependencies**

Python 3.x
pyvis: For graph creation and manipulation.


**Installation**

1. Clone the repository:
git clone https://github.com/N1kTop/ScientistsConnectionGraph
cd ScientistsConnectionGraphGeneration

2. Install dependencies: Install required Python libraries
pip install pyvis

3. Run the project: You can run the project with:
python scientistsConnectionGraph.py


**Usage**

The dataset includes information about the names of scientists and their birth and death years.
The data is loaded into the program, and a graph is constructed where nodes represent scientists.
The graph is generated and saved as graph.html.

The project uses a CSV file with the following structure:
Name | Birth Year | Death Year | Field of Science | Rationale
This data is processed to create a graph where the nodes are connected if their lifetimes overlap.
If you want to use a different dataset, change the file name in the main function when calling loadData(filename).


**Results**

The resultant graph consists from one big interconnected family. However there are a few outliers, such as Thales of Miletus, who was a philosopher, living in around 600 BC.
From this small experiment we can tell that most of the well known researchers who majorly contributed towards modern science have lived in a reletively close time period, mostly around years 1700-2000.


![graph1](https://github.com/user-attachments/assets/0bb042bc-1419-43c5-8143-56e5b19f8739)
![main](https://github.com/user-attachments/assets/d1f06405-75a6-4e47-baf4-61d0c3d25aba)


**Future Improvements**

Expand Dataset: Add more scientists and refine the dataset for more comprehensive graphs.
Different Dataset: This program can work with other datasets as long as the CSV file format stays the same. 
Enhance Visualization: Improve the visual layout by using libraries such as jaal or plotly.


**Note**

Thank you for checking my small python project.
