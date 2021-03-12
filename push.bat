@echo off
python -m twine upload --skip-existing dist/*
echo Push Complete...
pause > nul
