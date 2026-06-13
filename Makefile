run:
	uv run uvicorn main:app --reload

req:
	uv pip freeze > requirements.txt