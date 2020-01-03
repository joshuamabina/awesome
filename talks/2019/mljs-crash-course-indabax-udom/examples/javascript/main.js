import { DecisionTreeClassifier as DTClassifier } from 'ml-cart';

// 1. import the data
let trainingSet = [[140, 0], [120, 0], [700, 1], [500, 1], [900, 1], [100, 0]]
let trainingLabels = [0, 0, 1, 1, 1, 0];

// 2. train the classifier
let classifier = new DTClassifier();
classifier.train(trainingSet, trainingLabels);

// 3. predict
console.log(classifier.predict([[300, 0]]));
