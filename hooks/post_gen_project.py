#!/usr/bin/env python
import os
import pathlib
import shutil

PROJECT_DIRECTORY = pathlib.Path.cwd().expanduser().resolve()


def delete(relpath):
    target = PROJECT_DIRECTORY / relpath
    rm(target)


def rm(target: pathlib.Path):
    if target.is_file():
        target.unlink()
    elif target.is_dir():
        shutil.rmtree(target)
    else:
        raise ValueError(f"Invalid argument, {target} is not a file or directory.")


if __name__ == "__main__":

    if "True" == "{{ cookiecutter.virtual }}":
        keep = {".gitignore", ".python-version", "LICENSE", "pyproject.toml", "README.md"}
        for p in PROJECT_DIRECTORY.iterdir():
            if p.name not in keep:
                rm(p)
    else:
        if "no" in "{{ cookiecutter.command_line_interface|lower }}":
            cli_file = os.path.join("src", "{{ cookiecutter.package_name }}", "cli.py")
            delete(cli_file)

    if "Not open source" == "{{ cookiecutter.open_source_license }}":
        delete("LICENSE")
