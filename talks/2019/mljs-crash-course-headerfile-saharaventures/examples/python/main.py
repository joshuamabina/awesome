from sklearn import tree

# 1. import the data
training_set = [[140, 0], [120, 0], [500, 1], [900, 1], [100, 0]]
training_labels = [0, 0, 1, 1, 0]

# 2. train the classifier
classifier = tree.DecisionTreeClassifier()
classifier = classifier.fit(training_set, training_labels)

# 3. predict
print classifier.predict([[300, 0]])
