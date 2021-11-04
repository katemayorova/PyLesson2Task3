import os


def read_files(dir_path):
    file_data = {}
    file_names = os.listdir(dir_path)
    file_names.sort()
    for file_path in file_names:
        lines = []
        with open(os.path.join(dir_path, file_path)) as file:
            for line in file:
                lines.append(line)
        file_data[file_path] = lines
    return file_data


file_contents = read_files("sorted")
with open("out.txt", "w+") as result:
    for file_tuple in sorted(file_contents.items(), key=lambda key: len(key[1])):
        result.write(file_tuple[0] + "\n")
        result.write(str(len(file_tuple[1])) + "\n")
        result.writelines(file_tuple[1])
