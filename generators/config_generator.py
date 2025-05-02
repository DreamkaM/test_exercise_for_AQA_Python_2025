import xml.etree.ElementTree as ET
from xml.dom import minidom
from models.uml_model import UMLModel, UMLClass

class ConfigXMLGenerator:
    def __init__(self, model: UMLModel):
        self.model = model

    def generate(self, path: str):
        root_class = self.model.get_root_class()
        if not root_class:
            raise ValueError("No root class found in model")

        root_elem = self._build_class_element(root_class)
        tree = ET.ElementTree(root_elem)

        xml_str = ET.tostring(root_elem, encoding='unicode')
        parsed = minidom.parseString(xml_str)

        for node in parsed.getElementsByTagName('*'):
            if not node.firstChild:
                node.appendChild(parsed.createTextNode(" "))


        pretty_xml_as_str = parsed.toprettyxml(indent="    ")

        with open(path, 'w', encoding='utf-8') as f:
            f.write(pretty_xml_as_str)

    def _build_class_element(self, cls: UMLClass) -> ET.Element:
        elem = ET.Element(cls.name)

        for attr in cls.attributes:
            attr_elem = ET.SubElement(elem, attr.name)
            attr_elem.text = attr.type

        for child in cls.children:
            child_elem = self._build_class_element(child)
            elem.append(child_elem)

        return elem