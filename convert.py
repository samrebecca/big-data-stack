import csv
import sys

txt_file = "/Users/Rebecca/Downloads/results.txt"
csv_file = "/Users/Rebecca/Downloads/results-csv.csv"

in_txt = csv.reader(open(txt_file, "rb"), delimiter = '\t')
out_csv = csv.writer(open(csv_file, 'wb'))

out_csv.writerows(in_txt)