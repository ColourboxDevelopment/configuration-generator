#!/usr/bin/env python3
import boto3
import sys
import fileinput
import re
from botocore.exceptions import ParamValidationError

c = "".join(fileinput.input())

names = re.findall('{{ ?([^ ]*) ?}}', c)
if len(names) > 0:
    r = boto3.client('ssm').get_parameters(Names=re.findall('{{ ?([^ ]*) ?}}', c), WithDecryption=True)

    for p in r['Parameters']:
        c = re.sub('{{ ?' + p['Name'] + ' ?}}', p['Value'], c)

print(c)
