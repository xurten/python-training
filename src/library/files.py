import keyword


def get_files_content(file_path):
    with open(file_path) as f:
        lines = f.readlines()
    return lines


print(get_files_content('python_keywords.txt'))
result = ""
for i in get_files_content('python_keywords.txt'):
    result = result + str(i) + " "

result_without_end_of_line = result.replace('\n', '')
print(result_without_end_of_line)
# keywords from keyword.py
print(keyword.kwlist)
