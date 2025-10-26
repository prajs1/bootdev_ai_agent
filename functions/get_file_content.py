import os
from config import MAX_FILE_CHARS

def get_file_content(working_directory, file_path):
    try:
        joined_path = os.path.join(working_directory, file_path)
        working_abs_path = os.path.abspath(working_directory)
        abs_path = os.path.abspath(joined_path)
    except Exception as e:
        return f"Error: {e}"

    if not abs_path.startswith(working_abs_path):
        return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'

    if not os.path.isfile(abs_path):
        return f'Error: File not found or is not a regular file: "{file_path}"'

    with open(abs_path, "r") as f:
        try:
            file_content = f.read(MAX_FILE_CHARS)
        except Exception as e:
            return f"Error: {e}"
    file_content += '[...File "{file_path}" truncated at 10000 characters]'

    return file_content
