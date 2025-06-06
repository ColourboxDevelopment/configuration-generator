"""
Read the README.md
"""
#!/usr/bin/env python3
import fileinput
import re
import sys
import boto3

PATTERN = '{{ ?([^ ]*) ?}}'
FILE_CONTENTS = "".join(fileinput.input())

names = re.findall(PATTERN, FILE_CONTENTS)
if len(names) > 0:
    CHUNK_SIZE = 10
    chunks = [names[i:i + CHUNK_SIZE] for i in range(0, len(names), CHUNK_SIZE)]

    for n in chunks:
        r = boto3.client('ssm').get_parameters(Names=n, WithDecryption=True)

        for p in r['Parameters']:
            FILE_CONTENTS = re.sub('{{ ?' + p['Name'] + ' ?}}', p['Value'], FILE_CONTENTS)

names = re.findall(PATTERN, FILE_CONTENTS)
if len(names) > 0:
    for name in names:
        err = f"ERROR: Configuration parameter was not replaced: \n\n\t{name}\n\n"
        sys.stderr.write(err)
    sys.exit(1)

if re.search('{{|}}|{ ?([^ ]*) ?}', FILE_CONTENTS):
    filename = fileinput.filename()
    err = f"ERROR: Configuration template contains malformed template strings: {filename}\n"
    sys.stderr.write(err)
    sys.exit(1)

print(FILE_CONTENTS)
