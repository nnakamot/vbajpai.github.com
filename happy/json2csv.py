import json
import csv
import os

def main(filename):

  with open(filename, 'r') as fr:
    data = json.load(fr)

  fname = os.path.splitext(filename)[0]
  with open('%s.csv'%fname, 'w') as fw:
    csv_file = csv.writer(fw)
    for item in data:
      csv_file.writerow([item['msmid'], item['version'], item['timestamp'],
          item['status'], item['service'], item['port'], item['endpoint'],
          item['time']])

if __name__ == '__main__':
  import sys

  def usage():
    print 'usage: %s filename'%sys.argv[0]
    sys.exit(1)

  if len(sys.argv) != 2: print usage()
  main(sys.argv[1])
