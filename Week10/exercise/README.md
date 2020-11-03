### [Boston_housing.csv](https://github.com/Tunoc/sem4python_notebooks/blob/master/Week10/exercise/housing.csv)  
1)	download the Boston_housing.csv
    a) Click the `Boston_housing.csv` link above.
    b) Click the `Raw` button on the right side.
    c) Right click and press `[CTRL] + S` or `[CMD] + S` and download the file.

# Exercise1:  
1)  In the .ipynb convert the bad formatted data to something useable.  
	a)	The following column names are in correct order;  
		`column_names = ['CRIM', 'ZN', 'INDUS', 'CHAS', 'NOX', 'RM', 'AGE', 'DIS', 'RAD', 'TAX', 'PTRATIO', 'B', 'LSTAT', 'MEDV']`  
			`CRIM` - per capita crime rate by town  
			`ZN` - proportion of residential land zoned for lots over 25,000 sq.ft.  
			`INDUS` - proportion of non-retail business acres per town.  
			`CHAS` - Charles River dummy variable (1 if tract bounds river; 0 otherwise)  
			`NOX` - nitric oxides concentration (parts per 10 million)  
			`RM` - average number of rooms per dwelling  
			`AGE` - proportion of owner-occupied units built prior to 1940  
			`DIS` - weighted distances to five Boston employment centres  
			`RAD` - index of accessibility to radial highways  
			`TAX` - full-value property-tax rate per $10,000  
			`PTRATIO` - pupil-teacher ratio by town  
			`B` - 1000(Bk - 0.63)^2 where Bk is the proportion of blacks by town  
			`LSTAT` - % lower status of the population  
            (Target variable) - `MEDV` - Median value of owner-occupied homes in $1000's  

2)  Explore the dataset;  
	a)	shape/dimensions  
	b)	describe  
	c)	histogram/bin plot all columns  
	d)	"Optional" make heatmap using seaborn(Because it's cool)  

3)  Split the dataset into training and test.  
	https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.train_test_split.html  

4)  Check the accuracy on both the training data and the test data, using `.score(x, y)`  

5)  Plot target prices(x) vs predicted prices(y)  

### Made by:  
## *Lucky drawing*  
