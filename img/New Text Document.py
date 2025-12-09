import os

# Change this to the folder path you want to process
base_path = "."

for name in os.listdir(base_path):
    old_path = os.path.join(base_path, name)

    # Only rename folders
    if os.path.isdir(old_path):
        # Split by underscore, capitalize each part
        parts = name.split('_')
        new_name = '_'.join(part.capitalize() for part in parts)

        new_path = os.path.join(base_path, new_name)

        # Rename only if name is different
        if old_path != new_path:
            print(f"Renaming: {name} -> {new_name}")
            os.rename(old_path, new_path)
