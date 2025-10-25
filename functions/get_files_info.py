import os

def get_files_info(working_directory, directory="."):
    joined_path = os.path.join(working_directory, directory)
    working_abs_path = os.path.abspath(working_directory)
    abs_path_directory = os.path.abspath(joined_path)

    if not abs_path_directory.startswith(working_abs_path):
        return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'

    if not os.path.isdir(joined_path):
        return f'Error: "{directory}" is not a directory'

    dir_content = os.listdir(joined_path)
    str_return = "Result for currect directory:\n"

    for obj in dir_content:
        item = os.path.join(abs_path_directory, obj)
        try:
            is_dir = os.path.isdir(item)
            size = os.path.getsize(item)
        except Exception as e:
            return f"Error: {e}"
        str_return += f"- {obj}: file_size={size} bytes, is_dir={is_dir}\n"

    return str_return
