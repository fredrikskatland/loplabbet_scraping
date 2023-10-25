import os

def get_windows_env(var_name):
    try:
        result = os.popen(f"powershell.exe -c 'echo $env:{var_name}'").read().strip()
        return result
    except Exception as e:
        print(f"An error occurred: {e}")
        return None

# Example usage
windows_path = get_windows_env("PINECONE_ENV_FINN")
print(f"Windows PINECONE_ENV_FINN: {windows_path}")
