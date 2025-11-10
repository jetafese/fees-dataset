import json
import os
import sys


def create_convo_json(base_dir):
    for root, _, files in os.walk(base_dir):
        for file in files:
            if file.endswith(".txt"):
                txt_path = os.path.join(root, file)
                json_path = os.path.join(root, "convo.json")

                # Read the content of the .txt file
                with open(txt_path, "r", encoding="utf-8") as f:
                    txt_content = f.read().strip()

                # Create the JSON structure
                convo_data = [
                    {
                        "role": "USER",
                        "content": "How much do I owe in taxes?"
                    },
                    {
                        "role": "AGENT",
                        "content": txt_content
                    }
                ]
                # Write convo.json (unquoted, pretty-formatted)
                with open(json_path, "w", encoding="utf-8") as f:
                    json.dump(convo_data, f, indent=2, ensure_ascii=False)

                print(f"✅ Created {json_path}")

# Example usage:
if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python convo-fitter.py <base_dir>")
        sys.exit(1)

    base_dir = sys.argv[1]
    create_convo_json(base_dir)
