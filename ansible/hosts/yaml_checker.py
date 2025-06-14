import yaml

def check_yaml_indentation(file_path):
    try:
        with open(file_path, 'r') as f:
            yaml.safe_load(f)
        print(" YAML syntax and indentation looks good")
    except yaml.YAMLError as exc:
        print("YAML Error detected")
        if hasattr(exc, 'problem_mark'):
            mark = exc.problem_mark
            print(f" Error at line {mark.line +1}, column {mark.column +1}")
        print(str(exc))

if __name__=="__main__":
    filepath = input("Enter path to your YAML file:")
    check_yaml_indentation(filepath)
