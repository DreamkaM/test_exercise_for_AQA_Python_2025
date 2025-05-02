import xml.etree.ElementTree as ET
from models.uml_model import UMLModel, UMLClass, UMLAttribute, UMLAggregation

class XMIParser:
    def __init__(self, xml_path: str):
        self.xml_path = xml_path

    def parse(self) -> UMLModel:
        tree = ET.parse(self.xml_path)
        root = tree.getroot()

        model = UMLModel()

        for cls in root.findall(".//Class"):
            name = cls.get("name")
            is_root = cls.get("isRoot") == "true"
            documentation = cls.get("documentation", "")
            uml_class = UMLClass(name, is_root, documentation)

            for attr in cls.findall("Attribute"):
                attr_name = attr.get("name")
                attr_type = attr.get("type")
                uml_class.add_attribute(UMLAttribute(attr_name, attr_type))

            model.add_class(uml_class)

        for aggr in root.findall("Aggregation"):
            source = aggr.get("source")
            target = aggr.get("target")
            src_mult = aggr.get("sourceMultiplicity")
            tgt_mult = aggr.get("targetMultiplicity")
            model.add_aggregation(UMLAggregation(source, target, src_mult, tgt_mult))

        for aggr in model.aggregations:
            parent = model.classes.get(aggr.target)
            child = model.classes.get(aggr.source)
            if parent and child:
                parent.children.append(child)

        return model