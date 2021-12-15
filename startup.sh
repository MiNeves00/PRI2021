#!/bin/bash

precreate-core champions
precreate-core items
# Start Solr in background mode so we can use the API to upload the schema
solr start

sleep 10

# Schema definition via API
curl -X POST -H 'Content-type:application/json' \
    --data-binary @/data/schema.json \
    http://localhost:8983/solr/champions/schema 

curl -X POST -H 'Content-type:application/json' \
    --data-binary @/data/items_schema.json \
    http://localhost:8983/solr/items/schema 

# Populate collection
bin/post -c champions /data/champions.csv
bin/post -c items /data/items.csv

# Restart in foreground mode so we can access the interface
solr restart -f
