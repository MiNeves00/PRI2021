#!/bin/bash

precreate-core champions

# Start Solr in background mode so we can use the API to upload the schema
solr start

# Schema definition via API
curl -X POST -H 'Content-type:application/json' \
    --data-binary @/data/schema.json \
    http://localhost:8983/solr/champions/schema




sleep 5

# Populate collection
bin/post -c champions /data/champions.csv

# Restart in foreground mode so we can access the interface
solr restart -f
