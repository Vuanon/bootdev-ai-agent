import os

def get_files_info(working_directory: str, directory: str = ".") -> str:
    dir_name = "current" if "." else f'"{directory}"'
    result = f"Result for {dir_name} directory:"
    try:
        working_dir_abs = os.path.abspath(working_directory)
        target_dir = os.path.normpath(os.path.join(working_dir_abs, directory))
        valid_target_dir = os.path.commonpath([working_dir_abs, target_dir]) == working_dir_abs
        if not valid_target_dir:
            return result + f'\nError: Cannot list "{directory}" as it is outside the permitted working directory'
        if not os.path.isdir(target_dir):
            return result + f'\nError: "{directory}" is not a directory'
        for file in os.listdir(target_dir):
            file_path = os.path.normpath(os.path.join(target_dir, file))
            size = os.path.getsize(file_path)
            is_dir = os.path.isdir(file_path)
            result += f"\n  - {file}: file_size={size} bytes, is_dir={is_dir}"
        return result
    except Exception as e:
        return result + f'\nError: {e}'


