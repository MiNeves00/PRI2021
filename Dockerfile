FROM solr:8.10

COPY champions.csv /data/champions.csv

COPY schema.json /data/schema.json

COPY startup.sh /scripts/startup.sh

COPY startup.sh /scripts/s.sh

ENTRYPOINT ["/scripts/startup.sh"]

