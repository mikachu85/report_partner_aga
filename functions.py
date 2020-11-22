__author__ = 'Damien Jeremiah'

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

# def output_html_page():
#     f1 = open("../settings_data/settings_1.txt", 'r')
#     f2 = open("../settings_data/settings_2.txt", 'r')
#     f3 = open("../settings_data/settings_3.txt", 'r')
#     f4 = open("../settings_data/settings_4.txt", 'r')
#     f5 = open("../settings_data/settings_5.txt", 'r')
#     file_contents1 = f1.read()
#     file_contents2 = f2.read()
#     file_contents3 = f3.read()
#     file_contents4 = f4.read()
#     file_contents5 = f5.read()
#     with open("../html_config/html_output_1004.txt", "a") as textfile:
#         textfile.write(file_contents1 + "\n")
#         a = str("<component component_type=\"1\" horiz_pos=\"0\" vert_pos=\"2\" span=\"1\" duration=\"1:00:00:00.00\" resolution=\"01:00:00.00\" description=\"")
#         b = str("text=\"\">")
#         with open("../input_data/ar_nodes_1004.txt", 'r') as file:
#             node = csv.reader(file)
#             for row in node:
#                 for i in range(0, len(row)):
#                     textfile.write(file_contents2 + "\n" + a + row[i] + "\" " + b + "\n")
#         textfile.write(file_contents3)
#         with open("../input_data/ar_nodes_1004.txt", 'r') as file:
#             node = csv.reader(file)
#             for row in node:
#                 for i in range(0, len(row)):
#                     textfile.write("<source key=\"probe_group\" value=\"" + row[i] + "\"/>" + "\n")
#         textfile.write(file_contents4 + "\n")
#         textfile.write(file_contents5)


def output_html_page():
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
    with open("../html_config/html_output_1004.txt", "a") as textfile:
        textfile.write(file_contents1 + "\n")
        a = str("<component component_type=\"1\" horiz_pos=\"0\" vert_pos=\"2\" span=\"1\" duration=\"1:00:00:00.00\" resolution=\"01:00:00.00\" description=\"")
        b = str("text=\"\">")
        with open("../input_data/ar_nodes_1004.txt", 'r') as file:
            node = csv.reader(file)
            for row in node:
                for i in range(0, len(row)):
                    textfile.write(file_contents2 + "\n" + a + row[i] + "\" " + b + "\n")
                    textfile.write(file_contents3)
                    textfile.write("<source key=\"probe_group\" value=\"" + row[i] + "\"/>" + "\n")
                    textfile.write(file_contents4 + "\n")
        textfile.write(file_contents5)


def output_node_part():
    f2 = open("../settings_data/settings_2.txt", 'r')
    f3 = open("../settings_data/settings_3.txt", 'r')
    f4 = open("../settings_data/settings_4.txt", 'r')
    f5 = open("../settings_data/settings_5.txt", 'r')
    file_contents2 = f2.read()
    file_contents3 = f3.read()
    file_contents4 = f4.read()
    file_contents5 = f5.read()
    with open("../html_config/html_output_1004.txt", "a") as textfile:
        #a = str("<component component_type=\"1\" horiz_pos=\"0\" vert_pos=\"2\" span=\"1\" duration=\"1:00:00:00.00\" resolution=\"01:00:00.00\" description=\"")
        a = str("<component component_type=\"1\" horiz_pos=\"0\" vert_pos=\"")
        b = str("\" span=\"1\" duration=\"1:00:00:00.00\" resolution=\"01:00:00.00\" description=\"")
        d = str("text=\"\">")
        with open("../input_data/ar_nodes_1004.txt", 'r') as file:
            node = csv.reader(file)
            for row in node:
                for i in range(0, len(row)):
                    textfile.write(file_contents2 + "\n" + a + str(i+2) + b + row[i] + "\" " + d + "\n")
                    #textfile.write(file_contents2 + "\n" + a + row[i] + "\" " + d + "\n")
                    textfile.write(file_contents3)
                    textfile.write("<source key=\"probe_group\" value=\"" + row[i] + "\"/>" + "\n")
                    textfile.write("</sources>\n" + "</measurement>\n")
                    textfile.write("<measurement measurement_id=\"qoe_distribution_minor\" scope=\"1\" source_id=\"2\">\n")
                    textfile.write("<sources>\n")
                    textfile.write("<source key=\"probe_group\" value=\"" + row[i] + "\"/>" + "\n" + "</sources>\n" + "</measurement>\n" )
                    textfile.write("<measurement measurement_id=\"qoe_distribution_major\" scope=\"1\" source_id=\"2\">\n")
                    textfile.write("<sources>\n")
                    textfile.write("<source key=\"probe_group\" value=\"" + row[i] + "\"/>" + "\n" + "</sources>\n" + "</measurement>\n" )
                    textfile.write("<measurement measurement_id=\"qoe_distribution_unavailable\" scope=\"1\" source_id=\"2\">\n")
                    textfile.write("<sources>\n")
                    textfile.write("<source key=\"probe_group\" value=\"" + row[i] + "\"/>" + "\n" + "</sources>\n" + "</measurement>\n")
                    textfile.write("</measurements>\n" "<settings>\n")
                    textfile.write("\n")