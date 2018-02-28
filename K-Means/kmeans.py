import math
import sys
import csv
import random
import collections

def euclidean_distance(point1, point2):
	if len(point1) != len(point2):
		print "It is not possible to calculate the Euclidean distance!"
		sys.exit(1)
	sum = 0
	for i in range(len(point1)):
		sum += (float(point2[i]) - float(point1[i]))**2
	return math.sqrt(sum)

def kmeans(dataset, k):
	centroids = {}
	for i in range(k):
		centroids[i] = []
	clusters = {}
	length = len(dataset[0])
	
	for l in range(length):
		maxi = 0-sys.maxint
		mini = sys.maxint
		for row in dataset:
			if float(row[l]) < mini:
				mini = float(row[l])
			if float(row[l]) > maxi:
				maxi = float(row[l])
		for i in range(k):
			centroids[i].append(random.uniform(mini, maxi))
	flag = True
	while flag:
		for i in range(k):
			clusters[i] = []
		
		for d in dataset:
			menor = sys.maxint
			menor_index = 0
			for c in centroids:
				distance = euclidean_distance(d, centroids[c])
				if distance < menor:
					menor = distance
					menor_index = c
			clusters[menor_index].append(d)

		for c in clusters:
			newCenter = []
			for l in range(length):
				s = 0
				for row in clusters[c]:
					s += float(row[l])
				newCenter.append(s/len(clusters[c]))
			for cnt in range(len(centroids[c])):
				if centroids[c][cnt] != newCenter[cnt]:
					centroids[c] = newCenter
					break
				if c == (len(clusters) - 1) and cnt == (len(centroids[c])-1):
					flag = False
	return clusters


if '-help' in sys.argv:
	print "Options and arguments: "
	print "-d: Set your dataset."
	print "-p: Percentual of dataset to train (0,1)."
	print "-c: Define your dataset for the classifier."
	print "-k: Number of K-means."

if '-h' in sys.argv:
	print "Options and arguments: "
	print "-d: Set your dataset."
	print "-p: Percentual of dataset to train (0,1)."
	print "-c: Define your dataset for the classifier."
	print "-k: Number of K-means."

if '-version' in sys.argv:
	print "Author: Talvane Lima - Belem - Pa - Brazil\nDate: 26/01/2018\nScript K-means version 1."
	sys.exit(1)
if '-v' in sys.argv:
	print "Author: Talvane Lima - Belem - Pa - Brazil\nDate: 26/01/2018\nScript K-means version 1."
	sys.exit(1)


if '-d' in sys.argv:
	file_index = sys.argv.index('-d') + 1
	try:
		file = open(sys.argv[file_index], 'r')
	except:
		print "Impossible open file."
		sys.exit(1)
	csv_file = csv.reader(file)
	dataset = []
	for row in csv_file:
		if len(row) == 0:
			continue
		dataset.append(row)
else:
	print "Set your dataset."
	sys.exit(1)

if '-k' in sys.argv:
	k = int(sys.argv[sys.argv.index('-k') + 1])
else:
	k = 5


cluster = kmeans(dataset, k)
output = ''
d = []
for c in cluster:
	for row in cluster[c]:
		d.append(row)
		for col in row:
			output += col+","
		output += 'Cluster'+str(c)+"\n"

file = open('output.txt', 'w')
file.write(output)
file.close()