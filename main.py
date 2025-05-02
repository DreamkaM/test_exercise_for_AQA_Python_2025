import os
from parsers.xmi_parser import XMIParser
from generators.config_generator import ConfigXMLGenerator
from generators.meta_generator import MetaJSONGenerator

INPUT_FILE = 'impulse_test_input.xml'
OUTPUT_DIR = 'out'

def main():
    os.makedirs(OUTPUT_DIR, exist_ok=True)

    parser = XMIParser(INPUT_FILE)
    model = parser.parse()

    config_generator = ConfigXMLGenerator(model)
    config_generator.generate(os.path.join(OUTPUT_DIR, 'config.xml'))

    meta_generator = MetaJSONGenerator(model)
    meta_generator.generate(os.path.join(OUTPUT_DIR, 'meta.json'))

if __name__ == '__main__':
    main()