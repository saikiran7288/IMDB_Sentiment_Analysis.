import os

def print_tree(startpath, indent=0):
    for item in os.listdir(startpath):
        path = os.path.join(startpath, item)
        if os.path.isdir(path):
            print(" " * indent + "📂 " + item)
            print_tree(path, indent + 4)  # Recursively print subdirectories
        else:
            print(" " * indent + "📄 " + item)

# Change '.' to your project path if needed
print_tree(".")
