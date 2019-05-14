#!/usr/bin/env python3
import boto3
import fileinput
import re
import sys

pattern = '{{ ?([^ ]*) ?}}'
c = "".join(fileinput.input())

names = re.findall(pattern, c)
if len(names) > 0:
    r = boto3.client('ssm').get_parameters(Names=re.findall(pattern, c), WithDecryption=True)

    for p in r['Parameters']:
        c = re.sub('{{ ?' + p['Name'] + ' ?}}', p['Value'], c)

names = re.findall(pattern, c)
if len(names) > 0:
    for name in names:
        sys.stderr.write("\nERROR: Configuration parameter was not replaced: \n\n\t{}\n\n".format(name))
    sys.exit(1)

print(c)
