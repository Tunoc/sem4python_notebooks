# Exercise1:  
1)  Generate 2 blobs with sklearns `make_blobs(n_samples=150, centers=2, n_features=2, cluster_std=0.5, random_state=0)`  
	a) Look at the dataset (Show the first line of the matrix)  
	b) Print the target  
2)  Scatterplot the dataset with matplotlib  
	a) Use different colors for each of the `n_features=`, created in the blob data. - I use red and green  
3)  Use the `activation_function` and `perceptron` fuction given in the `12-1-Perceptron-Classifier`  
4)  Use the `pla` function given in the `12-1-Perceptron-Classifier`  
5)  In exercise 1.b we found out that our data_blob set only contains 1 and 0 as target values  
	a) Turn all the 0's into -1's. Now when we print our target, we should only have, 1 and -1  
	b) Turn all the new targets with our daata into an array that has the following format;  
	`[(array([data.x, data.y]), 1), (array([data.x, data.y]), -1)]`  
	Note that the 1 and -1 are our target values  
6)  Using the pla function that we used copied in before, find the `learned_weights` of our training data from 5.b  
7)  Use the `predict` function given in `12-1-Perceptron-Classifier`  
    a) Try to see if we can predict a couple of values to be either 1 or -1  
8)  Visualize the linear seperability by using the `compute_line` function given in `12-1-Perceptron-Classifier`

### Made by:  
## *Lucky drawing*  