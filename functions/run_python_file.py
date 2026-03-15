import os
import subprocess
from google.genai import types

def run_python_file(working_directory, file_path, args=None):
    try:
        absolute_path = os.path.abspath(working_directory)
        target_direct = os.path.normpath(os.path.join(absolute_path, file_path))

        valid_path = os.path.commonpath([absolute_path, target_direct]) == absolute_path

        if valid_path == False:
            return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'
        
        if not os.path.isfile(target_direct):
            return f'Error: "{file_path}" does not exist or is not a regular file'

        if not target_direct.endswith('.py'):
            return f'Error: "{file_path}" is not a Python file'

        command = ["python", target_direct]
        if args:
            command.extend(args)

        complete_process = subprocess.run(command, cwd=absolute_path, capture_output=True, text=True, timeout=30)
        
        #output string
        string_output = ""
        if complete_process.returncode != 0:
            string_output =  f'Process exited with code {complete_process.returncode}'
        if not complete_process.stdout and not complete_process.stderr:
            string_output += " No output produced"
        else:
            string_output += f'STDOUT: {complete_process.stdout}STDERR: {complete_process.stderr}'
        
        return string_output

    except Exception as e:
        return f"Error: executing Python file: {e}"

schema_run_python_file = types.FunctionDeclaration(
    name="run_python_file",
    description="Runs a python file by path, providing completed process information",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="File path",
            ),
            "args": types.Schema(
                type=types.Type.ARRAY,
                items=types.Schema(type=types.Type.STRING),
                description="optional arguments to run the file",
            ),
        },
        required=["file_path"]
    ),
)