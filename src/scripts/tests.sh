#!/bin/bash
set -e
set -x

# run isort recursively
# isort -rc .

# Update pre-commit
pre-commit autoupdate
#run pre-commit
pre-commit run -a

# bash scripts/test.sh --cov-report=html ${@}
python3 -m pytest

# change path for coverage.xml
sed -i "s/<source>\/workspaces\/starlette-template\/src<\/source>/<source>\/github\/workspace\/src<\/source>/g" /workspaces/starlette-template/src/coverage.xml
# create coverage-badge
coverage-badge -o ../coverage.svg -f

# generate flake8 report
flake8 --tee . > flake8_report/report.txt

