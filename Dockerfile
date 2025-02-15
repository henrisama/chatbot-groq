FROM python:3.9-slim

WORKDIR /app
COPY . /app

RUN pip install -r requirements.txt

CMD ["streamlit", "run", "src/app.py", "--server.port=8501"]
