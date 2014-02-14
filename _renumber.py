import os.path

order = (
    'hello_world',
    'calculator',
    'variables',
    'types',
    'lists',
    'if',
    'while',
    'for',
    'functions',
    'files',
    'csv_files',
)

my_dir_path = os.path.dirname(__file__)
if len(my_dir_path) == 0:
    my_dir_path = os.getcwd()

for file_name in os.listdir(my_dir_path):
    if os.path.splitext(file_name)[1] != '.py':
        continue
    elif file_name[0] == '_' or file_name[0] == '.':
        continue
    file_path = os.path.join(my_dir_path, file_name)
    file_name_split = file_name.split('_', 1)
    if len(file_name_split) == 1:
        continue
    try:
        file_number = int(file_name_split[0])
    except ValueError:
        continue
    new_file_path = os.path.join(my_dir_path, file_name_split[1])
    print file_path, 'to', new_file_path
    os.rename(file_path, new_file_path)

for file_i, file_base_name in enumerate(order):
    file_path = os.path.join(my_dir_path, file_base_name + '.py')
    assert os.path.exists(file_path), file_path
    new_file_path = os.path.join(my_dir_path, "%02u_%s.py" % (file_i+1, file_base_name))
    print file_path, 'to', new_file_path
    os.rename(file_path, new_file_path)

