#!/bin/bash
set -e
set -x

# Get Environment Variables
read_var() {
    VAR=$(grep $1 $2 | xargs)
    IFS="=" read -ra VAR <<< "$VAR"
    echo ${VAR[1],,}
}

LOGURU_LOGGING_LEVEL=$(read_var LOGURU_LOGGING_LEVEL .env)
#delete db
if [[ -f ~/starlette-template/src/sqlite_db/api.db ]]
then
    echo "deleting db"
    rm ~/starlette-template/src/sqlite_db/api.db
fi
# delete db in container
if [[ -f /workspaces/starlette-template/src/sqlite_db/api.db ]]
then
    echo "deleting db - container"
    rm /workspaces/starlette-template/src/sqlite_db/api.db
fi

#delete logs
if [[ -f  ~/starlette-template/src/log/log.log ]]
then
    echo "deleting log"
    rm  ~/starlette-template/src/log/log.log
fi
# delete log in container
if [[ -f /workspaces/starlette-template/src/log/log.log ]]
then
    echo "deleting log - container"
    rm /workspaces/starlette-template/src/log/log.log
fi

# run dev
LOGURU_LOGGING_LEVEL=$(read_var LOGURU_LOGGING_LEVEL .env)

uvicorn main:app --port 5000 --reload --log-level ${LOGURU_LOGGING_LEVEL,,}
