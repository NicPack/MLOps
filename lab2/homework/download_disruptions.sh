#!/bin/bash

mkdir -p data/disruptions

for i in {11..23}; do
  wget "https://opendata.rijdendetreinen.nl/public/disruptions/disruptions-20${i}.csv" \
       -O "data/disruptions/disruptions_20${i}.csv"
done
