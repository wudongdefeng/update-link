import re
curl -O https://raw.githubusercontent.com/tolinkshare/freenode/main/README.md
# Read the file
with open('README.md', 'r') as file:
    content = file.read()

# Find the SSR section
pattern = r'>🚀免费SSR节点列表\s+```([\s\S]*?)```'
match = re.search(pattern, content)

# Extract the SSR content
if match:
    ssr_content = match.group(1)
    # Save the content to a file named "ssr"
    with open('ssr', 'w') as ssr_file:
        ssr_file.write(ssr_content)
        print("SSR content saved successfully.")
else:
    print("SSR content not found.")
cat ssr  
# Find the SSR section
pattern1 = r'>🚀免费v2rayN节点列表\s+```([\s\S]*?)```'
match1 = re.search(pattern1, content)

# Extract the SSR content
if match:
    v2ray_content = match1.group(1)
    # Save the content to a file named "ssr"
    with open('v2ray', 'w') as ssr_file:
        ssr_file.write(v2ray_content)
        print("v2ray content saved successfully.")
else:
    print("v2ray content not found.")
