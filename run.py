#!/usr/bin/env python3
"""The app's entry point."""

from app import create_app

app = create_app()

if __name__ == '__main__':
    app.run()
