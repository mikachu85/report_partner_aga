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


def print_statement1():
    a = str("<component component_type=\"1\" horiz_pos=\"0\" vert_pos=\"2\" span=\"1\" duration=\"1:00:00:00.00\" resolution=\"01:00:00.00\" description=\"")
    b = str("text=\"\"")
    with open("../input_data/ar_nodes_1004.txt", 'r') as file:
        node = csv.reader(file)
        for row in node:
            for i in range (0, len(row)):
                print (a + row[i] + "\" " + b)

def print_statement2():
    c = str("<source key=\"probe_group\" value=\"")
    d = str("\"/>")
    with open("../input_data/ar_nodes_1004.txt", 'r') as file:
        node = csv.reader(file)
        for row in node:
            for i in range (0, len(row)):
                print(c + row[i] + d)

def print_settings():
    f1 = open("../settings_data/settings_1.txt", 'r')
    f2 = open("../settings_data/settings_2.txt", 'r')
    f3 = open("../settings_data/settings_3.txt", 'r')
    f4 = open("../settings_data/settings_4.txt", 'r')
    f5 = open("../settings_data/settings_5.txt", 'r')
    file_contents1 = f1.read()
    file_contents2 = f2.read()
    file_contents3 = f3.read()
    file_contents4 = f4.read()
    file_contents5 = f5.read()