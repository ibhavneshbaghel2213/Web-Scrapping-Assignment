FROM python:3.10-slim

ENV PYTHONUNBUFFERED 1

# Install system dependencies
RUN apt-get update && apt-get install -y \
    gcc \
    libxml2-dev \
    libxslt-dev \
    libffi-dev \
    libssl-dev

# Install Scrapy
RUN pip install scrapy

# Copy the Scrapy project files into the Docker image
COPY . /app

# Set the working directory
WORKDIR /app

# Run the Scrapy spider
CMD ["scrapy", "crawl", "testSite", "-o", "output.json"]
