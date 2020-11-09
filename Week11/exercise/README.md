# Exercise1:  
1)  Load datasetet digits fra sklearn `load_digits`  
	a) Plot a digit [0] as an image.  
	`plt.gray()`  
	`plt.matshow(digits.images[0])`  
  
2) Do dimensionality reduction with `NCA neighbourhood components analysis` and standard scalar.  
	a) Hint, use the following link  
	`https://scikit-learn.org/stable/auto_examples/neighbors/plot_nca_dim_reduction.html#sphx-glr-auto-examples-neighbors-plot-nca-dim-reduction-py`  
	b) Make the model  
	c) Train the model  
	d) Check accuracy of the data dimensionality reduction, using KNN  
	e) Show the scatterplot  
  
3) Use MeanShift with Bandwith=80 and fit it with the reduced dimensionality data from exercise 2.  
	a) Use numpy to print all the unique cluster `labels_`  
	a.1) Note that we have the same amount of labels, as we did clusters in different collors from the previous task  
	b) Scatter plot meanshift output, including the cluster centers  

### Made by:  
## *Lucky drawing*  