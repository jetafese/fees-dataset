import os
import subprocess
import sys


def create_smt(base_dir):
    for root, _, files in os.walk(base_dir):
        for file in files:
            if file.endswith(".bl"):
                bl_path = os.path.join(root, file)
                smt_path = os.path.join(root, "prog.smt2")
                
                # Path to main.py (relative to this script)
                main_script = os.path.join(os.path.dirname(__file__), "../../language/main.py")

                # Normalize path
                main_script = os.path.abspath(main_script)

                # Build the command
                command = ["python", main_script, bl_path]

                # Run the command
                try:
                    subprocess.run(command, check=True)
                    print(f"✅ Ran main.py on {bl_path}")
                except subprocess.CalledProcessError as e:
                    print(f"❌ Error running main.py on {bl_path}: {e}")

                print(f"✅ Created {smt_path}")

# Example usage:
if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python bl-to-smt.py <base_dir>")
        sys.exit(1)

    base_dir = sys.argv[1]
    create_smt(base_dir)
