## Scientists Graph
# Author: Nik Topolskis
# Date: 17/10/2024
# Version: 1.2
#
# Description:
# This program generates a graph to represent scientists who lived in the same time period.
# If two scientists were alive at the same time at any point, they would be represented as two connected nodes.
# Scientists who lived in a different time are not connected.
# pyvis.network packege is used to visualize the graph.

import csv, sys
from pyvis.network import Network


# Opens a CSV file and reads scientists names, and years of birth and death.
# Returns 2D list ppl:
# ppl[0] = name, ppl[1] = initial_year, ppl[2] = final_year
def loadData(filename):

    # List of people
    ppl = []

    # Open CSV file
    with open(filename, "r") as file:
        reader = csv.reader(file)
        next(reader, None) # skip header

        # Loop through each row in the CSV
        for row in reader:
            # Get name and years of life
            name = row[0]
            initial_year = row[1]
            final_year = row[2]

            # Convert years to integers:
            # If BC, then set year to be negative
            if "BC" in initial_year:
                initial_year = -int(initial_year.strip("BC"))
            else:
                initial_year = int(initial_year)

            # Repeat for final year:
            if final_year == "Present": # if still alive, set year high
                final_year = 3000
            elif "BC" in final_year:
                final_year = -int(final_year.strip("BC"))
            else:
                final_year = int(final_year)

            # Append all data to people list:
            ppl.append([name, initial_year, final_year])

    return ppl


# This method takes 2D list of people sorted by their final_year
# and itterates through them adding any 2 people who lived at the same time to the edges list
# The year of birth increases with each itteration, and the program uses dictionary {map} to keep track who is still alive at current year of itteration
# Finally, the method generates the graph as an HTML file using generateGraph() method
def generateNodesAndEdges(ppl_sorted):
    # Dictionary to store year of death as keys
    # and list of people names who share this year as values
    map = {}

    # List of all nodes
    nodes = []

    # List of all edges
    edges = []

    for person in ppl_sorted:
        nodes.append(person[0]) # add each person to node list

        # After each iteration years that are below current itteration year should be deleted from the dictionary
        # years_to_delete is going to store those years
        years_to_delete = []
        for year in map:
            if person[1] > year: # if final_year > year in dictionary
                years_to_delete.append(year) # the year should be deleted
            else:
                # If final_year < year_in dictionary, then every person in map[year] share their time with current person and should be added to edges lsit
                for person2 in map[year]:
                    edges.append([person[0], person2])

        # Delete requried years:
        for year in years_to_delete:
            map.pop(year, None)

        # Add person name (person[0]) to the dictionary
        # with key being their final_year (person[2])
        if person[2] in map:
            map[person[2]].append(person[0])
        else:
            map[person[2]] = [person[0]]

    # Genearte the graph
    generateGraph(nodes, edges)


# Takes 2 lists nodes and edges to generate a graph using pyvis.Network module
def generateGraph(nodes, edges):
    # Initialize network
    net = Network(notebook = True, cdn_resources = "remote",
                    bgcolor = "#222222",
                    font_color = "white",
                    height = "750px",
                    width = "100%",
                    select_menu = True,
                    filter_menu = True,
    )
    # Add nodes
    net.add_nodes(nodes)
    # Add edges
    net.add_edges(edges)
    # Generate the html file
    net.show("graph.html")

def main():
    # Load data
    ppl = loadData("scientists.csv")

    # Sort people list by initial_year value:
    ppl_sorted = sorted(ppl, key=lambda l:l[1])

    # Calculate nodes and edges, then generate the graph:
    generateNodesAndEdges(ppl_sorted)


if __name__ == "__main__":
    sys.exit(main())