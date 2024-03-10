# JunkPurge

A simple Python script to recursively delete common build and install directories for various programming languages, helping you clean up unnecessary files and free up space.

## Supported Languages

- JavaScript (js)
- Rust (rust)
- Python (python)
- C++ (cpp)
- Java (java)
- C# (csharp)
- Go (go)
- Ruby (ruby)
- PHP (php)
- Dart (dart)
- Flutter (flutter)

## Installation

You can install JunkPurge directly from PyPI:

```bash
pip install junkpurge
```

Once installed, you can use it as a command-line tool:

```bash
junkpurge <directory> <language>
```

For example, to clean the build directories for a JavaScript project:

```bash
junkpurge my_project js
```

This will remove directories like node_modules, dist, and build from the specified my_project directory.

## License

This project is licensed under the MIT License - see the LICENSE file for details.
