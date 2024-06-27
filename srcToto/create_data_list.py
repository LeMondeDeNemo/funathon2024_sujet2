import yaml

def create_data_list(source_file):

    with open(source_file, 'r') as file:
        catalogue = yaml.safe_load(file)
    return catalogue

urls = create_data_list("sources.yml")
print(urls)