import collections
import csv
import sys

def csv_merge(f1,f2):

    with open(f1+".csv", 'r') as infile:
        obj = csv.reader(infile)
        header_a = next(obj)
        dict_a = {row[0]: row[1:] for row in obj}

    with open(f2+".csv", 'r') as infile:
        obj = csv.reader(infile)
        header_b = next(obj)
        dict_b = collections.defaultdict(list)

        for row in obj:
            dict_b[row[0]].append(row[1:])

    with open('newfile.csv', 'w') as newfile:
        w = csv.writer(newfile)
        w.writerow(header_a + header_b[1:])

        for i_a in dict_a.keys():
            for i_b in dict_b.get(i_a, [[]]):
                w.writerow([i_a] + dict_a[i_a] + i_b)

if __name__ == "__main__":

    if sys.argv[1] == "merge":
        csv_merge(sys.argv[2], sys.argv[3])
