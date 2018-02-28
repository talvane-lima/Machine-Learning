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

def knn(dataset, example, k):
	distance_dict = {}
	for i in range(len(dataset)):
		point = dataset[i][0:len(dataset[i]) -1]
		distance = euclidean_distance(point, example)
		distance_dict[i] = distance
	neighbors = []
	while len(neighbors) < k:
		flag = True
		for n in distance_dict:
			if flag:
				flag = False
				menor = n
				continue
			if distance_dict[n] < distance_dict[menor]:
				menor = n
		del distance_dict[menor]
		neighbors.append(dataset[menor][-1])
	return neighbors



if '-help' in sys.argv:
	print "Options and arguments: "
	print "-d: Set your dataset."
	print "-p: Percentual of dataset to train (0,1)."
	print "-c: Define your dataset for the classifier."
	print "-k: Number of K-neighbors."

if '-h' in sys.argv:
	print "Options and arguments: "
	print "-d: Set your dataset."
	print "-p: Percentual of dataset to train (0,1)."
	print "-c: Define your dataset for the classifier."
	print "-k: Number of K-neighbors."

if '-version' in sys.argv:
	print "Author: Talvane Lima - Belem - Pa - Brazil\nDate: 18/01/2018\nScript KNN version 1."
	sys.exit(1)
if '-v' in sys.argv:
	print "Author: Talvane Lima - Belem - Pa - Brazil\nDate: 18/01/2018\nScript KNN version 1."
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

if '-p' in sys.argv:
	tax = float(sys.argv[sys.argv.index('-p') + 1])
	if tax < 0 or tax > 1:
		print "Set an interval between 0 and 1."
		sys.exit(1)
else:
	tax = 0.9

if '-c' in sys.argv:
	file_index = sys.argv.index('-c') + 1
	try:
		file = open(sys.argv[file_index], 'r')
	except:
		print "Impossible open file."
		sys.exit(1)
	csv_file = csv.reader(file)
	dataset_c = []
	for row in csv_file:
		dataset_c.append(row)
else:
	print "Set your dataset for the classifier."
	sys.exit(1)

if '-k' in sys.argv:
	k = int(sys.argv[sys.argv.index('-k') + 1])
else:
	k = 5

numDataSetTrain = int(tax * len(dataset))

#Divide dataset - Train e Test
dataset_train = []
for i in range(0,numDataSetTrain):
	index = random.randint(0, len(dataset) -1)
	dataset_train.append(dataset[index])
	dataset.pop(index)
dataset_test = dataset

#test
error = 0.0
for e in dataset_test:
	if collections.Counter(knn(dataset_train, e[0:len(e)-1], k)).most_common(1)[0][0] != e[-1]:
		error += 1

print 'Number of tests: %d' %len(dataset_test)
print 'Number of errors in test: %d' %error
print 'Accuracy: %f%%' %((1-(error/len(dataset_test)))*100)

for n in dataset_c:
	print n, collections.Counter(knn(dataset_train, n, k)).most_common(1)[0][0]