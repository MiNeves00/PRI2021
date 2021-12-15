FROM solr:8.10

COPY data/csv/new_champions.csv /data/champions.csv

COPY data/schema.json /data/schema.json

COPY startup.sh /scripts/startup.sh

COPY data/schema.xml /conf/schema.xml

ENTRYPOINT ["/scripts/startup.sh"]

