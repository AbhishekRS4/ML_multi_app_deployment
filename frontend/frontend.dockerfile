FROM python:3.8.10-slim

WORKDIR /app

# install linux package dependencies
RUN apt-get update -y

# can copy files only from current working directory where docker builds
# cannot copy files from arbitrary directories

COPY ./requirements.txt .

RUN pip install -r requirements.txt

COPY ./*.py .

EXPOSE 8501

CMD ["streamlit", "run", "app_frontend.py", "--server.port=8501"]
