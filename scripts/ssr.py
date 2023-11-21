import re
import os
# Read the file
with open('README.md', 'r') as file:
    content = file.read()

# Find the SSR section
pattern = r'>🚀免费SSR节点列表\s+```([\s\S]*?)```'
match = re.search(pattern, content)

# Extract the SSR content
if match:
    ssr_content = match.group(1)
    ssr_content = re.sub(r'>🚀免费SSR节点列表\s+|```', '', ssr_content)
    ssr_content = re.sub(r'^\s*\n', '', ssr_content)
    parent_dir = os.path.dirname(os.getcwd())
    # Create the "files" directory if it doesn't exist
    files_dir = os.path.join(parent_dir, 'files')
    os.makedirs(files_dir, exist_ok=True)
    # Save the content to a file in the "files" directory
    file_path = os.path.join(files_dir, 'ssr')
    with open(file_path, 'w') as ssr_file:
        ssr_file.write(ssr_content)
        print("SSR content saved successfully.")
else:
    print("SSR content not found.")

# Find the SSR section
pattern1 = r'>🚀免费v2rayN节点列表\s+```([\s\S]*?)```'
match1 = re.search(pattern1, content)

# Extract the SSR content
if match:
    v2ray_content = match1.group(1)
    v2ray_content = re.sub(r'>🚀免费SSR节点列表\s+|```', '', v2ray_content)
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
