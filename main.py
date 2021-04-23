#!/usr/bin/env python
import click

@click.command()
def main():
    click.secho("main", fg="green")


if __name__ == "__main__":
    main()
