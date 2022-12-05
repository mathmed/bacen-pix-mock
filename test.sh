#!/bin/bash
docker exec bacen-pix-mock bash -c "cd /home/app; pytest --cov-config=.coveragerc --cov-report html --cov=. app/"
