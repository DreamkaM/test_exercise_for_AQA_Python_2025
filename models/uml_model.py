from typing import List, Dict, Optional

class UMLAttribute:
    def __init__(self, name: str, attr_type: str):
        self.name = name
        self.type = attr_type

class UMLClass:
    def __init__(self, name: str, is_root: bool, documentation: str):
        self.name = name
        self.is_root = is_root
        self.documentation = documentation
        self.attributes: List[UMLAttribute] = []
        self.children: List['UMLClass'] = []

    def add_attribute(self, attr: UMLAttribute):
        self.attributes.append(attr)

class UMLAggregation:
    def __init__(self, source: str, target: str, source_multiplicity: str, target_multiplicity: str):
        self.source = source
        self.target = target
        self.source_multiplicity = source_multiplicity
        self.target_multiplicity = target_multiplicity

class UMLModel:
    def __init__(self):
        self.classes: Dict[str, UMLClass] =  {}
        self.aggregations: List[UMLAggregation] = []

    def add_class(self, uml_class: UMLClass):
        self.classes[uml_class.name] = uml_class

    def add_aggregation(self, aggregation: UMLAggregation):
        self.aggregations.append(aggregation)

    def get_root_class(self) -> Optional[UMLClass]:
        for cls in self.classes.values():
            if cls.is_root:
                return cls
        return None