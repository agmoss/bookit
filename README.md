# `bookit`

> Doc site generator

[![pypi](https://img.shields.io/pypi/v/bookit?style=for-the-badge)](https://pypi.org/project/bookit/)

## Overview

This Python program converts all files in a Git repository to markdown files. It's useful for creating doc sites of your code.

The converted markdown files are placed in a `.bookit` subdirectory. The directory structure inside `.bookit` is an exact mirror of the original repository.

## Usage

```bash
python -m bookit /path/to/your/repo
```

## How it works

Each file is converted into a markdown file, with the file name being the `#title` of the markdown file and the contents of the original file placed inside a code block, highlighted according to the original file's language.

Here's an example of the directory structure transformation:

Before:

```bash
repo/
├── README.md
├── file1.py
├── file2.js
```

After:

```bash
repo/
├── .bookit/
│ ├── file1.py.md
│ └── file2.py.md
├── README.md
├── file1.py
└── file2.js
```

## DEV

### Setup

```bash
make install
```

This will setup a virtualenv, upgrade pip, install dependencies, and install pre-commit

**note**: This does not activate your virtualenv! You must run `source env/bin/activate` to use the venv.

### Test

```bash
make test
```

### Format

```bash
make format
```

```bash
make lint
```

### Version & Release

```bash
make version-<major/minor/patch>
```

```bash
make release
```

**note** Don't forget to `git push` with `--tags`

### pre-commit

#### Setup

```bash
make install-pre-commit
```

#### Run all

```bash
make pre-commit
```
