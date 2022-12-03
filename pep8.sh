#!/bin/bash
autopep8 --in-place -r --exclude="main.py" .; isort .
