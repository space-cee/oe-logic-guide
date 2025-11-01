import os, re, json

root_dir = "docs"
output_file = "blockData.json"
data = {}

for subdir, _, files in os.walk(root_dir):
    for file in files:
        if file.endswith(".md"):
            path = os.path.join(subdir, file)
            with open(path, "r", encoding="utf-8") as f:
                text = f.read()

            # Extract block name (from first header)
            name_match = re.search(r"#\s*(.+)", text)
            name = name_match.group(1).strip() if name_match else file.replace(".md", "")

            # Extract category
            category_match = re.search(r"\*\*Category:\*\*\s*(.+)", text)
            category = category_match.group(1).replace("OE Logic >", "").strip() if category_match else "Misc"

            # Extract description
            desc_match = re.search(r"\*\*Description:\*\*\s*(.+)", text)
            description = desc_match.group(1).strip() if desc_match else ""

            # Extract input/output types
            inputs = re.findall(r"-\s*([\w\d\(\)]+)", re.search(r"\*\*Input types:\*\*([\s\S]*?)\*\*Output", text, re.MULTILINE).group(1)) if "**Input types:**" in text else []
            outputs = re.findall(r"-\s*([\w\d\(\)]+)", re.search(r"\*\*Output types:\*\*([\s\S]*?)(\*\*Example|\Z)", text, re.MULTILINE).group(1)) if "**Output types:**" in text else []

            # Extract examples (lines under **Example:**)
            example_match = re.search(r"\*\*Example:\*\*([\s\S]*)", text)
            examples = [line.strip() for line in example_match.group(1).splitlines() if line.strip()] if example_match else []

            # Build structure
            if category not in data:
                data[category] = {}

            data[category][name] = {
                "name": name,
                "description": description,
                "inputs": [{"type": inputs}],
                "outputs": [{"type": outputs}],
                "sim": [{"head": "Examples"}] + [{"in": [ex.split("=")[0].strip()], "out": [ex.split("=")[1].strip()]} for ex in examples if "=" in ex]
            }

# Save JSON
with open(output_file, "w", encoding="utf-8") as f:
    json.dump(data, f, indent=4)

print(f"✅ Generated {output_file} with {sum(len(v) for v in data.values())} blocks.")
