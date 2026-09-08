import os
import subprocess

def run_python_file(working_directory: str, file_path: str, args: list[str] | None = None) -> str:

    try:
        abs_working_dir = os.path.abspath(working_directory)
        abs_file_path = os.path.normpath(os.path.join(abs_working_dir, file_path))
        file_within_working_dir = os.path.commonpath([abs_working_dir, abs_file_path]) == abs_working_dir
        if not file_within_working_dir:
            return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'
        if not os.path.isfile(abs_file_path):
            return f'Error: "{file_path}" does not exist or is not a regular file'
        if not file_path.endswith('.py'):
            return f'Error: "{file_path}" is not a Python file'
        command = ["python", abs_file_path]
        if args:
            command.extend(args)
        res = subprocess.run(
            command, 
            cwd=abs_working_dir, 
            capture_output=True,
            timeout=30,
            text=True
        )
        output = []
        if res.returncode:
            output.append(f'Process exited with code {res.returncode}\n')
        if res.stdout + res.stderr == "":
            output.append(f'No output produced\n')
        if res.stdout:
            output.append(f'STDOUT: {res.stdout}')
        if res.stderr:
            output.append(f'STDERR: {res.stderr}')
        return '\n'.join(output)

    except Exception as e:
        return f'Error: {e}'


schema_run_python_file = {
    "type": "function",
    "function": {
        "name": "run_python_file",
        "description": "Run or execute a specified Python file within the working directory and returns its output.",
        "parameters": {
            "type": "object",
            "required": ["file_path"],
            "properties": {
                "file_path": {
                    "type": "string",
                    "description": "Path of the python file to run, relative to the working directory",
                },
                "args": {
                    "type": "list of strings",
                    "description": "Optional list of arguments to pass the Python script. (default is None)",
                },
            },
        },
    },
}
