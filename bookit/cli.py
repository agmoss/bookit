import os

import click

from .bookit import load_gitignore_spec, process_files_in_dir


@click.command()
@click.argument("repo_path", type=click.Path(exists=True))
def git_files_to_md(repo_path: str) -> None:
    """
    Converts all files in a git repo to markdown files in a .bookit subdirectory.
    REPO_PATH is the path of the git repository.
    """
    book_path = os.path.join(repo_path, ".bookit")

    if not os.path.exists(book_path):
        os.makedirs(book_path)

    gitignore_spec = load_gitignore_spec(repo_path)

    for dirpath, dirnames, filenames in os.walk(repo_path):
        process_files_in_dir(dirpath, filenames, repo_path, book_path, gitignore_spec)

    click.echo(f"Successfully created markdown files in {book_path}")


if __name__ == "__main__":
    git_files_to_md()
