#!/usr/bin/env bash
function run() {
    for f in config.* ; do
        echo "Processing file: $f"
        # if ! jq $i >/dev/null 2>/dev/null ; then
        #     echo "[ { \"type\" : \"bad json\", \"file\" : \"$i\", \"line\": 1,\
        #               \"message\" : \"JSON is many things, but it is not this.\",\
        #               \"details_url\": null } ]"
        #     exit 0
        # fi
    done
    echo "[ ]" ; exit 0
}

[[ "$1" = "version" ]] && echo "1"
[[ "$1" = "applicable" ]] && echo "true"
[[ "$1" = "run" ]] && run
[[ -z "$1" ]] && echo '{ "version" : 1, "name" : "json-verifier" }'
