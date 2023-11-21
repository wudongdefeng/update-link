import re
import os
# Read the file
with open('README.md', 'r') as file:
    content = file.read()


# Find the SSR section
pattern1 = r'v2ray\s+```([\s\S]*?)```'
match1 = re.search(pattern1, content)

# Extract the SSR content
if match:
    v2ray_content = match1.group(1)
    v2ray_content = re.sub(r'v2ray\s+|```', '', v2ray_content)
    v2ray_content = re.sub(r'^\s*\n', '', v2ray_content)
    parent_dir = os.path.dirname(os.getcwd())
    # Create the "files" directory if it doesn't exist
    files_dir = os.path.join(parent_dir, 'files')
    os.makedirs(files_dir, exist_ok=True)
    # Save the content to a file in the "files" directory
    file_path = os.path.join(files_dir, 'v2ray')
    with open(file_path, 'w') as v2ray_file:
        v2ray_file.write(v2ray_content)
        print("v2ray content saved successfully.")
else:
    print("v2ray content not found.")
