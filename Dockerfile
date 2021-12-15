FROM solr:8.10

COPY data/csv/new_champions.csv /data/champions.csv

COPY data/schema.json /data/schema.json

COPY startup.sh /scripts/startup.sh

ENTRYPOINT ["/scripts/startup.sh"]

