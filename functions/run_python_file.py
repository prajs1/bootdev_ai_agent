import os
import subprocess


def run_python_file(working_directory, file_path, args=[]):
    joined_path = os.path.join(working_directory, file_path)
    abs_path = os.path.abspath(joined_path)
    working_abs_path = os.path.abspath(working_directory)

    if not abs_path.startswith(working_abs_path):
        return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'

    if not os.path.exists(abs_path):
        return f'Error: File "{file_path}" not found.'

    if not abs_path.endswith(".py"):
        return f'Error: "{file_path}" is not a Python file.'

    try:
        comp_process = subprocess.run(
            ["python", abs_path, *args],
            cwd=working_abs_path,
            timeout=30,
            capture_output=True,
            text=True,
        )

        if comp_process.stdout or comp_process.stderr:
            return_stmt = f"STDOUT: {comp_process.stdout}\nSTDERR: {comp_process.stderr}"
        else:
            return_stmt = "No output produced."

        if comp_process.returncode != 0:
            return_stmt += f"\nProcess exited with code {comp_process.returncode}"
        return return_stmt
    except Exception as e:
        return f"Error: executing Python file: {e}"
