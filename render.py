#!/usr/bin/env python3
import boto3
import sys
import fileinput
import re
from botocore.exceptions import ParamValidationError

c = "".join(fileinput.input())

try:
    r = boto3.client('ssm').get_parameters(Names=re.findall('{{ ?([^ ]*) ?}}', c), WithDecryption=True)
except ParamValidationError:
    r = {'Parameters': []}

for p in r['Parameters']:
    c = re.sub('{{ ?' + p['Name'] + ' ?}}', p['Value'], c)

print(c)
