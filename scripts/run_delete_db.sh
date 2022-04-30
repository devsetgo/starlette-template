#!/bin/bash
set -e
set -x

#delete db
if [[ -f ~/pynote_2/src/sqlite_db/api.db ]]
then
    echo "deleting db"
    rm ~/pynote_2/src/sqlite_db/api.db
fi
# delete db in container
if [[ -f /workspaces/pynote_2/src/sqlite_db/api.db ]]
then
    echo "deleting db - container"
    rm /workspaces/pynote_2/src/sqlite_db/api.db
fi

#delete logs
if [[ -f  ~/pynote_2/src/log/log.log ]]
then
    echo "deleting log"
    rm  ~/pynote_2/src/log/log.log
fi
# delete log in container
if [[ -f /workspaces/pynote_2/src/log/log.log ]]
then
    echo "deleting log - container"
    rm /workspaces/pynote_2/src/log/log.log
fi

# run dev
read_var() {
    VAR=$(grep $1 $2 | xargs)
    IFS="=" read -ra VAR <<< "$VAR"
    echo ${VAR[1],,}
}

LOGURU_LOGGING_LEVEL=$(read_var LOGURU_LOGGING_LEVEL .env)

uvicorn main:app --port 5000 --reload --log-level ${LOGURU_LOGGING_LEVEL,,}
