"""Console script for {{cookiecutter.package_name}}."""

import sys

{% if cookiecutter.command_line_interface|lower == 'click' -%}
import click
{%- endif %}

{% if cookiecutter.command_line_interface|lower == 'click' %}
@click.command()
def main() -> int:
    """Console script for {{cookiecutter.package_name}}."""
    click.echo("Replace this message by putting your code into {{cookiecutter.package_name}}.cli:main")
    click.echo("See click documentation at https://click.palletsprojects.com/")
    return 0
{%- endif %}


if __name__ == "__main__":
    sys.exit(main())  # pragma: no cover
