import ast

def load_config(config: dict, key: str, default_value=None):
    if key not in config:
        return default_value
    else:
        return config[key]
    
config_string = input("Enter config dictionary: ")
key = input("Enter key: ")

config = ast.literal_eval(config_string)

value = load_config(config, key)

print(value)    