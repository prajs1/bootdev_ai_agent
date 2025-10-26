import os

def write_file(working_directory, file_path, content):
    try:
        joined_path = os.path.join(working_directory, file_path)
        working_abs_path = os.path.abspath(working_directory)
        abs_joined_path = os.path.abspath(joined_path)
    except Exception as e:
        return f"Error: {e}"

    if not abs_joined_path.startswith(working_abs_path):
        return f'Error: Cannot write to "{file_path}" as it is outside the permitted working directory'
    
    with open(joined_path, "w") as f:
        try:
            f.write(content)
        except Exception as e:
            return f"Error: {e}"
    
    return f'Successfully wrote to "{file_path}" ({len(content)} characters written)'
