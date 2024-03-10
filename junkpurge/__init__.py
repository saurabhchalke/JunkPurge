import os
import sys
import shutil

# Define common build and install directories for different languages/frameworks
build_dirs = {
    "js": ["node_modules", "dist", "build"],
    "rust": ["target"],
    "python": ["build", "dist", "*.egg-info"],
    "cpp": ["build", "bin", "obj"],
    "java": ["target", "out"],
    "csharp": ["bin", "obj"],
    "go": ["bin", "pkg"],
    "ruby": ["tmp"],
    "php": ["vendor"],
    "dart": ["build"],
    "flutter": ["build"],
}


def delete_directories(root_dir, directories):
    for dir_name in directories:
        for root, dirs, files in os.walk(root_dir, topdown=False):
            for name in dirs:
                if name == dir_name:
                    dir_path = os.path.join(root, name)
                    print(f"Deleting {dir_path}...")
                    shutil.rmtree(dir_path)


def main():
    if len(sys.argv) != 3:
        print("Usage: python clean_build_dirs.py <directory> <language>")
        sys.exit(1)

    directory = sys.argv[1]
    language = sys.argv[2].lower()

    if language not in build_dirs:
        print(f"Unsupported language: {language}")
        sys.exit(1)

    delete_directories(directory, build_dirs[language])


if __name__ == "__main__":
    main()
