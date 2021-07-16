#!/usr/bin/env python

import json
import sys
import os
from detect_secrets import SecretsCollection
from detect_secrets.settings import default_settings
from os import walk

NAME = "Detect Secrets"
API_VERSION = 1

def emitStartInfo():
    info = { "version": API_VERSION, "name": NAME }
    print(json.dumps(info))

def emitVersion():
    print(API_VERSION)

def emitName():
    print(NAME)

def emitApplicable(path):
    # for (dirpath, dirnames, filenames) in os.walk(path):
    #     for file in filenames:
    #         if file.endswth(".js"):
    #             print(json.dumps(True))
    #             return
    # print(json.dumps(False))
    print(json.dumps(True))

def convertReportToLift(secrets):
    reports_with_messages = []
    
    secrets_json = secrets.json()
    
    for filename, results in secrets_json.items():
        for secret in results:
            if secret['hashed_secret']:
                reports_with_messages.append(createLiftNote(filename, secret))

    return reports_with_messages

def createLiftNote(scan_file, report):
    return {
        'type'      : report['type'],
        # 'message'   : report['hashed_secret'],
        'message'   : "detect-secrets finding",
        'file'      : scan_file,
        'line'      : report['line_number']
    }

def run(args):
    
    secrets = SecretsCollection()
    with default_settings():
        for (dirpath, dirnames, filenames) in os.walk("test_data"):
            for file in filenames:
                filename = os.path.join(dirpath, file)
                secrets.scan_file(filename)
                
    lift_report = convertReportToLift(secrets)
    print(json.dumps(lift_report, indent=2))

def main():
    args = sys.argv
    if (len(args) < 2):
        emitStartInfo()
    else:
        cmd = args[1]
        if cmd == "run":
            run(args)
        elif cmd == "applicable":
            emitApplicable(args[1])
        elif cmd == "name":
            emitName()
        else:
            emitVersion()


if __name__ == "__main__":
    main()