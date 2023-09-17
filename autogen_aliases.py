#!/usr/bin/env python3

import sys
import json
import argparse
import requests
requests.packages.urllib3.disable_warnings()

__ver__ = '0.0.1a'
__author__ = "Karol D. Sz"
__doc__ = 'Simple script to crate bash aliases with ssh connection base on Foreman Hosts'

def main():
  parser = argparse.ArgumentParser(description=__doc__)
  parser.add_argument('-v', '--version', action='version', version='%(prog)s ' + __ver__, help='Print version')
  parser.add_argument('--url', dest='url', type=str, help='Type domain or IP of Foreman')
  parser.add_argument('--pwd', dest='pwd', type=str, help='Enter passwd of Foreman\'s admin')
  parser.add_argument('-u', dest='user', type=str, help='Type your user for ssh session')
  parser.add_argument('--output', dest='output', default='bash_ssh_aliases_autogen', help='Optionally specify the name of output file')
  args = parser.parse_args()

  try:
    if not (args.url and args.pwd and args.user):
      parser.print_help()
      sys.exit(1)
    elif all(args.url and args.pwd and args.user):
      pass
  except Exception as e:
    print(f'Some kind of problems with arguments passed to script - {e}')
    sys.exit(1)

  try:
    r = requests.get(
        f'https://{args.url}/api/v2/hosts?per_page=9999', 
        headers = {
          'Content-Type': 'application/json',
          'Accept': 'application/json',
        }, verify=False,
        auth=('admin', f'{args.pwd}')
    )
    hosts = json.loads(r.content)
    for k,v in hosts.items():
      if 'results' in k :
        for i in v:
          with open(f'{args.output}', 'a') as f:
            f.write(f'ssh_{i.get("name").split(".")[0]}="sshpass -p $PASSWD ssh user@{i.get("ip")}"\n')
  except Exception as e:
    print(f'Unexpected script interruption due to: {e}')


if __name__ == '__main__':
  main()
