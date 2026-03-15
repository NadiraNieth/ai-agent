import os
from google.genai import types

def get_files_info(working_directory, directory="."):
    try:
        absolute_path = os.path.abspath(working_directory)
        target_direct = os.path.normpath(os.path.join(absolute_path, directory))

        valid_path = os.path.commonpath([absolute_path, target_direct]) == absolute_path

        if valid_path == False:
            return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'
        
        if not os.path.isdir(target_direct):
            return f'Error: "{directory}" is not a directory'

        items = os.listdir(target_direct)
        lines = []

        for item_name in items:
            item_path = os.path.join(target_direct, item_name)
            
            data_line = f"- {item_name}: file_size={os.path.getsize(item_path)} bytes, is_dir={os.path.isdir(item_path)}"
            lines.append(data_line)

        return "\n".join(lines)
    except Exception as e:
        return f"Error: {e}"

schema_get_files_info = types.FunctionDeclaration(
    name="get_files_info",
    description="Lists files in a specified directory relative to the working directory, providing file size and directory status",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "directory": types.Schema(
                type=types.Type.STRING,
                description="Directory path to list files from, relative to the working directory (default is the working directory itself)",
            ),
        },
    ),
)