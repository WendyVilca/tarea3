From python:3.11.7

COPY ./ /app
WORKDIR /app
RUN pip install -r requerements.txt
EXPOSE 5000

CMD ["python", "-m", "flask", "run", "--host=0.0.0.0"]