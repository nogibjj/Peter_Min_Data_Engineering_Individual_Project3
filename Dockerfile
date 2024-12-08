FROM python:3.11-slim

WORKDIR /app

COPY . /app

RUN pip3 install --no-cache-dir -r requirements.txt

EXPOSE 5000

ENV GROQ_API_KEY=${GROQ_API_KEY}

CMD ["flask", "run", "--host=0.0.0.0"]