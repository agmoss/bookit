import os
import shutil
from typing import Optional

from pathspec import PathSpec
from pathspec.patterns import GitWildMatchPattern
from pygments.lexers import get_lexer_for_filename


def is_git_related(dirpath: str, filename: str) -> bool:
    return ".bookit" in dirpath or ".git" in dirpath or ".git" in filename


def get_language(file_path: str) -> Optional[str]:
    try:
        return get_lexer_for_filename(file_path).name.lower()
    except:
        return None


def read_file(file_path: str) -> str:
    with open(file_path, "r") as file:
        return file.read()


def create_markdown_content(
    filename: str, file_content: str, language: Optional[str] = None
) -> str:
    md_content = f"# {filename}\n\n"
    if language:
        md_content += f"```{language}\n{file_content}\n```\n"
    else:
        md_content += f"```\n{file_content}\n```\n"
    return md_content


def write_markdown_file(md_content: str, new_file_path: str) -> None:
    with open(new_file_path, "w") as file:
        file.write(md_content)


def process_files_in_dir(
    dirpath: str,
    filenames: list,
    repo_path: str,
    book_path: str,
    gitignore_spec: PathSpec,
) -> None:
    for filename in filenames:
        relative_file_path = os.path.relpath(os.path.join(dirpath, filename), repo_path)
        if gitignore_spec.match_file(relative_file_path) or is_git_related(
            dirpath, filename
        ):
            continue

        file_path = os.path.join(dirpath, filename)
        new_dir = dirpath.replace(repo_path, book_path, 1)

        if filename.endswith(".md"):
            new_file_path = os.path.join(new_dir, filename)
            shutil.copy(file_path, new_file_path)
            continue

        new_file_path = os.path.join(new_dir, f"{filename}.md")

        if not os.path.exists(new_dir):
            os.makedirs(new_dir)

        language = get_language(file_path)

        file_content = read_file(file_path)

        md_content = create_markdown_content(filename, file_content, language)

        write_markdown_file(md_content, new_file_path)


def load_gitignore_spec(repo_path: str) -> PathSpec:
    gitignore_file_path = os.path.join(repo_path, ".gitignore")
    if os.path.exists(gitignore_file_path):
        with open(gitignore_file_path, "r") as file:
            gitignore_lines = file.readlines()
    else:
        gitignore_lines = []

    gitignore_spec = PathSpec.from_lines(GitWildMatchPattern, gitignore_lines)
    return gitignore_spec
