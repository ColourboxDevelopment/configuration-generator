#!/usr/bin/env python3
import boto3
import sys
import fileinput
import re

c = "".join(fileinput.input())

r = boto3.client('ssm').get_parameters(Names=re.findall('{{ ?(.*) ?}}', c), WithDecryption=True)
for p in r['Parameters']:
    c = c.replace('{{' + p['Name'] + '}}', p['Value'])

print(c)
