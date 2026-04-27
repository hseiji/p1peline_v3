FROM python:3.10-slim

RUN apt-get update && \
    apt-get install -y default-jre-headless && \
    apt-get clean

# Dynamically set JAVA_HOME
RUN ln -s /usr/lib/jvm/java-1.11.0-openjdk-*/ /usr/lib/jvm/default-java || true
ENV JAVA_HOME=/usr/lib/jvm/default-java
ENV PATH="$JAVA_HOME/bin:$PATH"

WORKDIR /app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["python", "main.py"]