FROM solr:8.10

COPY data/csv/new_champions.csv /data/champions.csv

COPY data/schema.json /data/schema.json

COPY data/csv/new_items.csv /data/items.csv

COPY data/items_schema.json /data/items_schema.json

COPY startup.sh /scripts/startup.sh

ENTRYPOINT ["/scripts/startup.sh"]

