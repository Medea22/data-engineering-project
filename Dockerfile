FROM mongo:6.0

RUN apt-get update && apt-get install -y python3 python3-pip

RUN pip3 install pymongo

COPY scripts/ /app/scripts/
COPY data/ /app/data/

WORKDIR /app

CMD mongod --fork --logpath /var/log/mongod.log && \
    sleep 3 && \
    python3 scripts/setup_db.py && \
    python3 scripts/load_data.py && \
    tail -f /var/log/mongod.log