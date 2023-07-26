# frontend/Dockerfile

FROM python:3.9

WORKDIR /app

RUN apt-get update
COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .

EXPOSE 8501

CMD ["streamlit", "run", "app.py"]