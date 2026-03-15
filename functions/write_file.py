import os
from google.genai import types

def write_file(working_directory, file_path, content):
    try:
        absolute_path = os.path.abspath(working_directory)
        target_direct = os.path.normpath(os.path.join(absolute_path, file_path))
        valid_path = os.path.commonpath([absolute_path, target_direct]) == absolute_path

        if valid_path == False:
            return f'Error: Cannot write to "{file_path}" as it is outside the permitted working directory'

        if os.path.isdir(target_direct):
            return f'Error: Cannot write to "{file_path}" as it is a directory'
        else:
            os.makedirs(os.path.dirname(target_direct), exist_ok=True)
            
        with open(target_direct, "w") as f:
            f.write(content)
                
        return f'Successfully wrote to "{file_path}" ({len(content)} characters written)'

    except Exception as e:
        return f"Error: {e}"

schema_write_file = types.FunctionDeclaration(
    name="write_file",
    description="Write or overwrite a file, providing info to where it was written and how long the content was",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="Path of the file to be written",
            ),
            "content": types.Schema(
                type=types.Type.STRING,
                description="text content to be written into the file",  
            ),
        },
        required=["file_path", "content"]
    ),
)