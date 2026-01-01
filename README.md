uv init task-test

cd task-test

uv add "fastapi[standard]"
       OR 
uv add fastapi && uv add uvicorn

CODE in main.py for API

uv run uvicorn main:app --reload  (for activley reload browser responce)

/pytest


 Bash command

   cd /mnt/d/code/claude-code-skills-lab-main/task-test && uv run pytest tests/ -v --cov=. --cov-report=term-missing



