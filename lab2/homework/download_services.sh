#!/bin/bash

mkdir -p data/services

for i in {19..25}; do
  wget "https://opendata.rijdendetreinen.nl/public/services/services-20${i}.csv.gz" \
       -O "data/services/services_20${i}.csv.gz" && \
        gzip -f -d "data/services/services_20${i}.csv.gz"
done