import os
from google.genai import types

MAX_CHARS = 10000

def get_file_content(working_directory, file_path):
    try:
        absolute_path = os.path.abspath(working_directory)
        target_direct = os.path.normpath(os.path.join(absolute_path, file_path))
        valid_path = os.path.commonpath([absolute_path, target_direct]) == absolute_path

        if valid_path == False:
            return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'

        if not os.path.isfile(target_direct):
            return f'Error: File not found or is not a regular file: "{file_path}"'
        
        with open(target_direct, "r") as f:
            file_content_string = f.read(MAX_CHARS)
            # After reading the first MAX_CHARS...
            if f.read(1):
                file_content_string += f'[...File "{file_path}" truncated at {MAX_CHARS} characters]'

        return file_content_string
    except Exception as e:
        return f"Error: {e}"

schema_get_file_content = types.FunctionDeclaration(
    name="get_file_content",
    description="Reads file content in a specified directory relative to the working directory, providing file content up to 10000 char",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="Path to file",
            ),
        },
        required=["file_path"]
    ),
)