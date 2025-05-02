import json
from models.uml_model import UMLModel, UMLClass, UMLAggregation

class MetaJSONGenerator:
    def __init__(self, model: UMLModel):
        self.model = model
        self.source_map = self._build_source_map()
        self.target_map = self._build_target_map()

    def generate(self, path: str):
        meta_data = []

        for cls in self.model.classes.values():
            class_meta = {
                "class": cls.name,
                "documentation": cls.documentation,
                "isRoot": cls.is_root,
                "parameters": []
            }

            for attr in cls.attributes:
                class_meta["parameters"].append({
                    "name": attr.name,
                    "type": attr.type
                })


            for agg in self.target_map.get(cls.name, []):
                class_meta["parameters"].append({
                    "name": agg.source,
                    "type": "class"
                })


            source_aggs = self.source_map.get(cls.name, [])
            if source_aggs:

                first = source_aggs[0]
                class_meta["min"] = self._parse_multiplicity(first.source_multiplicity)
                class_meta["max"] = self._parse_multiplicity(first.source_multiplicity, upper=True)

            meta_data.append(class_meta)

        with open(path, 'w', encoding='utf-8') as f:
            json.dump(meta_data, f, indent=4)

    def _build_source_map(self):
        result = {}
        for agg in self.model.aggregations:
            result.setdefault(agg.source, []).append(agg)
        return result

    def _build_target_map(self):
        result = {}
        for agg in self.model.aggregations:
            result.setdefault(agg.target, []).append(agg)
        return result

    def _parse_multiplicity(self, mult: str, upper=False):
        if '..' in mult:
            parts = mult.split('..')
            return parts[1] if upper else parts[0]
        return mult
