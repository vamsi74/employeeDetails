import xmltodict
import xml.etree.ElementTree as ET

class xmltojson:

    def convert_json(path):

        if path.endswith(".xml"):
            #Convert XML to JSON
            xml_string = ET.tostring(ET.parse(path).getroot())
            root=xmltodict.parse(xml_string)
            return root

def homerun():
    data = xmltojson.convert_json("data.xml")
    return data