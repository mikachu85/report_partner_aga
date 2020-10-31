# Insert list of AR nodes
import input_data
import csv

# When running this function please insert the nodes with comma seperator.
# Example, damien1ar1,damien1ar2, etc. Close with end.
def ar_nodes():
    ar_list = "a"
    while (ar_list) != "end":
        ar_list = input("Please insert AR nodes list for partner:" + "\n")
        with open("../input_data/ar_nodes_1004.txt", "a") as textfile:
            textfile.write(ar_list + "\n")

# This function will read the CSV file that you inserted.
# Do a quick overview to see that it looks correct.
def csv_node_list():
    with open("../input_data/ar_nodes_1004.txt", 'r') as file:
        node = csv.reader(file)
        for row in node:
            for i in range (0, len(row)):
                print(row[i])


