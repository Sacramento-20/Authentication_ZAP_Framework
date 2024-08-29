import os

# Caminho da pasta onde estão os arquivos .txt
folder_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "regex_words/")

# Obtém todos os arquivos .txt na pasta
files = [f for f in os.listdir(folder_path) if f.endswith(".txt")]
files = sorted(files)


def read_files(file):
    with open(f"{folder_path}{file}", "r") as f:
        return [line.strip() for line in f]


keywords = {}

for file in files:
    key = file.split(".")[0]
    keywords[key] = read_files(file)


invalid_values_urls = keywords["invalid_urls"]  # invalid_urls.txt
type_elements = keywords["type_elements"]  # type_elements.txt
valid_values_elements = keywords["valid_elements"]  # valid_elements.txt
url_words = keywords["valid_urls"]  # valid_urls.txt


password_field_identifiers = ("password", "senha", "txtPassword")  # *
parameters_types = ("form", "json")
parameter_types_found = {"form": 0, "json": 0, "script": 0}
