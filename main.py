import sys
import json
import yaml
import xml.etree.ElementTree as ET

def load_json(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            data = json.load(file)
        return data
    except FileNotFoundError:
        print(f"Plik {file_path} nie zostal znaleziony.")
        sys.exit(1)
    except json.JSONDecodeError as e:
        print(f"Blad skladni JSON w pliku {file_path}: {e}")
        sys.exit(1)

def load_yaml(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            data = yaml.safe_load(file)
        return data
    except FileNotFoundError:
        print(f"Plik {file_path} nie zostal znaleziony.")
        sys.exit(1)
    except yaml.YAMLError as e:
        print(f"Blad skladni YAML w pliku {file_path}: {e}")
        sys.exit(1)

def load_xml(file_path):
    try:
        tree = ET.parse(file_path)
        root = tree.getroot()
        return root
    except ET.ParseError as e:
        print(f"Blad skladni XML w pliku {file_path}: {e}")
        sys.exit(1)
    except FileNotFoundError:
        print(f"Plik {file_path} nie zostal znaleziony.")
        sys.exit(1)

def save_json(data, file_path):
    try:
        with open(file_path, 'w', encoding='utf-8') as file:
            json.dump(data, file, ensure_ascii=False, indent=4)
        print(f"Dane zostaly zapisane do pliku {file_path}")
    except Exception as e:
        print(f"Nie udalo się zapisać danych do pliku {file_path}: {e}")
        sys.exit(1)

def save_yaml(data, file_path):
    try:
        with open(file_path, 'w', encoding='utf-8') as file:
            yaml.dump(data, file, default_flow_style=False, allow_unicode=True)
        print(f"Dane zostaly zapisane do pliku {file_path}")
    except Exception as e:
        print(f"Nie udalo sie zapisac danych do pliku {file_path}: {e}")
        sys.exit(1)

def save_xml(data, file_path):
    root = ET.Element("data")
    for key, value in data.items():
        child = ET.SubElement(root, key)
        child.text = str(value)

    tree = ET.ElementTree(root)
    try:
        with open(file_path, 'wb') as file:
            tree.write(file, encoding='utf-8', xml_declaration=True)
        print(f"Dane zostaly zapisane do pliku {file_path}")
    except Exception as e:
        print(f"Nie udalo sie zapisac danych do pliku {file_path}: {e}")
        sys.exit(1)

def main():
    if len(sys.argv) != 3:
        print("Uzycie: python main.py <input_file> <output_file>")
        sys.exit(1)

    input_file = sys.argv[1]
    output_file = sys.argv[2]

    # Wczytanie i weryfikacja pliku .json, .yaml lub .xml
    if input_file.endswith('.json'):
        data = load_json(input_file)
        print("Dane z pliku JSON zostaly poprawnie wczytane.")
    elif input_file.endswith(('.yml', '.yaml')):
        data = load_yaml(input_file)
        print("Dane z pliku YAML zostaly poprawnie wczytane.")
    elif input_file.endswith('.xml'):
        data = load_xml(input_file)
        print("Dane z pliku XML zostaly poprawnie wczytane.")
    else:
        print("Obslugiwane formaty to .json, .yml, .yaml, .xml")
        sys.exit(1)

    # Zapis danych do pliku .json, .yaml lub .xml w zależności od formatu pliku wyjściowego
    if output_file.endswith('.json'):
        save_json(data, output_file)
    elif output_file.endswith(('.yml', '.yaml')):
        save_yaml(data, output_file)
    elif output_file.endswith('.xml'):
        save_xml(data, output_file)
    else:
        print("Obslugiwany jest tylko format JSON lub YAML dla pliku wyjsciowego.")
        sys.exit(1)

    print("Plik wejsciowy:", input_file)
    print("Plik wyjsciowy:", output_file)

if __name__ == "__main__":
    main()
