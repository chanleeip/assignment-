FROM ubuntu:latest

WORKDIR /app


RUN apt-get update && apt-get install -y \
    python3 python3-pip \
    curl gnupg && \
    curl -fsSL https://deb.nodesource.com/setup_23.x | bash - && \
    apt-get install -y nodejs && \
    apt-get clean && rm -rf /var/lib/apt/lists/*

COPY . .

CMD ["bash"]