#!/bin/bash
set -e
set -x

# run isort recursively
# isort -rc .

# Update pre-commit
pre-commit autoupdate

#run pre-commit
pre-commit run -a

#copy .env file to .env_orginal
cp .env .env_orginal

# change to test environment in .env file
sed -i "s/RELEASE_ENV='dev'/RELEASE_ENV='test'/" .env

# bash scripts/test.sh --cov-report=html ${@}
python3 -m pytest

# replace copy with original .env file
cp .env_orginal .env
# delete .env_orginal file
rm .env_orginal
# change path for coverage.xml
sed -i "s/<source>\/workspaces\/starlette-template\/src<\/source>/<source>\/github\/workspace\/src<\/source>/g" /workspaces/starlette-template/src/coverage.xml
# create coverage-badge
coverage-badge -o ../coverage.svg -f

# generate flake8 report
flake8 --tee . > flake8_report/report.txt

