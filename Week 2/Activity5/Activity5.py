import json
import elementpath
from xml.etree import ElementTree as ET
from xml.dom import minidom


def recursiveTree(parent, attribute):

    if type(attribute) is dict:
        for child in list(attribute.keys()):
            subElement = ET.SubElement(parent, child)
            if type(attribute.get(child)) is dict:
                recursiveTree(subElement, attribute.get(child))
            elif type(attribute.get(child)) is list:
                for item in attribute.get(child):
                    subElement.text = str(item)
                    if item != attribute.get(child)[-1]:
                        subElement = ET.SubElement(parent, child)
            else:
                subElement.text = str(attribute.get(child))

def jsonToXml():
    infile = open("People.json")
    datafile = json.load(infile)
    infile.close()
    #print(datafile)

    root = ET.Element(*datafile.keys())

    for student in datafile.get(*datafile.keys()):
        element = ET.SubElement(root, "student")
        for attr in list(student.keys()):
            subElement = ET.SubElement(element, attr)
            if type(student.get(attr)) is dict:
                recursiveTree(subElement, student.get(attr))
            elif type(student.get(attr)) is list:
                for item in student.get(attr):
                    subElement.text = str(item)
                    if item != attribute.get(child)[-1]:
                        subElement = ET.SubElement(parent, child)
            else:
                subElement.text = str(student.get(attr))

    xmlstr = minidom.parseString(ET.tostring(root)).toprettyxml(indent="   ")
    with open("People.xml", "w") as f:
        f.write(xmlstr)

def main():
    jsonToXml()

if __name__ == "__main__":
    main()
