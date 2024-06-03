import sys
import json

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

def save_json(data, file_path):
    try:
        with open(file_path, 'w', encoding='utf-8') as file:
            json.dump(data, file, ensure_ascii=False, indent=4)
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

    # Wczytanie i weryfikacja pliku .json
    if input_file.endswith('.json'):
        data = load_json(input_file)
        print("Dane z pliku JSON zostaly poprawnie wczytane.")
    else:
        print("Obslugiwany jest tylko format JSON w tym przykladzie.")
        sys.exit(1)

    # Zapis danych do pliku .json
    if output_file.endswith('.json'):
        save_json(data, output_file)
    else:
        print("Obslugiwany jest tylko format JSON w tym przykladzie.")
        sys.exit(1)

    print("Plik wejsciowy:", input_file)
    print("Plik wyjsciowy:", output_file)

if __name__ == "__main__":
    main()
