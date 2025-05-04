FROM python:3.13.3-alpine

WORKDIR /code

COPY requirement.txt /code/requirement.txt

RUN pip install --no-cache-dir --upgrade -r /code/requirement.txt

COPY main.py /code/main.py

CMD ["fastapi", "run", "main.py", "--port", "8000"]