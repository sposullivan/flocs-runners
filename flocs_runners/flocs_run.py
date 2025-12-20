#!/usr/bin/env python
import cyclopts

from . import linc_runner, vlbi_runner


def main():
    app = cyclopts.App()
    app.command(linc_runner.app, name="linc")
    app.command(vlbi_runner.app, name="vlbi")

    app()


if __name__ == "__main__":
    main()
# vim: ft=python
