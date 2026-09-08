import os
from config import READ_FILE_MAX_CHARS

def get_file_content(working_directory: str, file_path: str) -> str:
    try:
        abs_working_dir = os.path.abspath(working_directory)
        abs_file_path = os.path.normpath(os.path.join(abs_working_dir, file_path))
        file_within_working_dir = os.path.commonpath([abs_working_dir, abs_file_path]) == abs_working_dir
        if not file_within_working_dir:
            return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'
        if not os.path.isfile(abs_file_path):
            return f'Error: File not found or is not a regular file: "{file_path}"'
        with open(abs_file_path, 'r') as f:
            file_content = f.read(READ_FILE_MAX_CHARS)
            if f.read(1):
                file_content += f'[...File "{file_path}" truncated at {READ_FILE_MAX_CHARS} characters]'
        return file_content
    except Exception as e:
        return f'Error: {e}'

schema_get_file_content = {
    "type": "function",
    "function": {
        "name": "get_file_content",
        "description": "Gets content of a file in a specified directory relative to the working directory. Will return up to 10,000 characters of the file, and will specify if output is truncated.",
        "parameters": {
            "type": "object",
            "required": ["file_path"],
            "properties": {
                "file_path": {
                    "type": "string",
                    "description": "Path of file containing content to read, relative to the working directory",
                },
            },
        },
    },
}
