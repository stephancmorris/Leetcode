# Machine Learning Algorithms Deep Dive

## Supervised Learning Algorithms

### 1. Linear Regression
**Concept**: Predicts continuous values using linear relationships
**Mathematical Foundation**: y = β₀ + β₁x₁ + β₂x₂ + ... + βₙxₙ + ε
**Key Points**:
- Assumes linear relationship between features and target
- Minimizes sum of squared residuals
- Sensitive to outliers
- Requires feature scaling for multiple features

**Interview Questions**:
- How do you handle multicollinearity in linear regression?
- What's the difference between L1 and L2 regularization?
- How do you interpret R² and adjusted R²?

### 2. Logistic Regression
**Concept**: Binary classification using logistic function
**Mathematical Foundation**: P(y=1) = 1/(1 + e^(-z)) where z = β₀ + β₁x₁ + ... + βₙxₙ
**Key Points**:
- Uses sigmoid function to map linear combination to probabilities
- Maximum likelihood estimation for parameter fitting
- Can be extended to multiclass (one-vs-rest, multinomial)
- Provides probability estimates, not just predictions

**Interview Questions**:
- Why can't we use linear regression for classification?
- How do you interpret logistic regression coefficients?
- What's the difference between logistic regression and SVM?

### 3. Decision Trees
**Concept**: Hierarchical decision-making using if-then rules
**Algorithm**: 
- Choose best feature to split on (using Gini, entropy, or variance)
- Create branches for each possible value
- Repeat recursively until stopping criteria met
**Key Points**:
- Non-parametric, can handle non-linear relationships
- Prone to overfitting
- Can handle both numerical and categorical features
- Easy to interpret and visualize

**Interview Questions**:
- How do you prevent overfitting in decision trees?
- What's the difference between Gini impurity and entropy?
- How do you handle missing values in decision trees?

### 4. Random Forest
**Concept**: Ensemble of decision trees with bagging
**Algorithm**:
- Bootstrap sampling to create multiple datasets
- Train decision tree on each bootstrap sample
- Use random subset of features at each split
- Average predictions for regression, majority vote for classification
**Key Points**:
- Reduces overfitting compared to single decision tree
- Handles missing values well
- Provides feature importance
- Parallelizable training

**Interview Questions**:
- Why does random forest work better than a single decision tree?
- How do you choose the number of trees?
- What's the difference between bagging and boosting?

### 5. Support Vector Machines (SVM)
**Concept**: Find optimal hyperplane that separates classes with maximum margin
**Mathematical Foundation**: Maximize margin while minimizing classification errors
**Key Points**:
- Works well with high-dimensional data
- Can use different kernels (linear, polynomial, RBF)
- Memory efficient
- Sensitive to feature scaling

**Interview Questions**:
- What's the difference between hard margin and soft margin SVM?
- How do you choose the right kernel?
- What's the role of the C parameter in SVM?

### 6. Naive Bayes
**Concept**: Probabilistic classifier based on Bayes' theorem
**Mathematical Foundation**: P(y|x) = P(x|y) * P(y) / P(x)
**Key Points**:
- Assumes feature independence (naive assumption)
- Fast training and prediction
- Works well with small datasets
- Can handle multiple classes naturally

**Interview Questions**:
- Why is the "naive" assumption often violated in practice?
- How do you handle continuous features in Naive Bayes?
- What's the difference between Gaussian and Multinomial Naive Bayes?

## Unsupervised Learning Algorithms

### 1. K-Means Clustering
**Concept**: Partition data into k clusters by minimizing within-cluster sum of squares
**Algorithm**:
1. Initialize k centroids randomly
2. Assign each point to nearest centroid
3. Update centroids to mean of assigned points
4. Repeat until convergence
**Key Points**:
- Requires specifying number of clusters
- Sensitive to initialization
- Works best with spherical clusters
- Fast and scalable

**Interview Questions**:
- How do you choose the optimal number of clusters?
- What are the limitations of K-means?
- How do you handle categorical data in K-means?

### 2. Hierarchical Clustering
**Concept**: Build tree of clusters using bottom-up (agglomerative) or top-down (divisive) approach
**Algorithm**:
- Agglomerative: Start with each point as cluster, merge closest pairs
- Divisive: Start with all points in one cluster, split recursively
**Key Points**:
- No need to specify number of clusters
- Creates dendrogram showing cluster hierarchy
- Computationally expensive O(n³)
- Deterministic results

**Interview Questions**:
- What's the difference between single, complete, and average linkage?
- How do you interpret a dendrogram?
- When would you use hierarchical vs K-means clustering?

### 3. DBSCAN
**Concept**: Density-based clustering that groups points with many neighbors
**Algorithm**:
- Core points: Have at least minPts neighbors within eps distance
- Border points: Within eps of core point but not core themselves
- Noise points: Neither core nor border
**Key Points**:
- Can find clusters of arbitrary shape
- Identifies outliers as noise
- Doesn't require specifying number of clusters
- Sensitive to eps and minPts parameters

**Interview Questions**:
- How do you choose eps and minPts parameters?
- What are the advantages of DBSCAN over K-means?
- How does DBSCAN handle clusters of different densities?

## Dimensionality Reduction

### 1. Principal Component Analysis (PCA)
**Concept**: Find orthogonal directions of maximum variance in data
**Mathematical Foundation**: Eigenvalue decomposition of covariance matrix
**Algorithm**:
1. Center the data
2. Compute covariance matrix
3. Find eigenvalues and eigenvectors
4. Select top k eigenvectors as principal components
**Key Points**:
- Linear transformation
- Preserves most variance with fewer dimensions
- Components are orthogonal
- Sensitive to feature scaling

**Interview Questions**:
- How do you choose the number of principal components?
- What's the difference between PCA and LDA?
- Can you interpret the meaning of principal components?

### 2. t-SNE
**Concept**: Non-linear dimensionality reduction for visualization
**Algorithm**:
- Computes probabilities based on pairwise distances
- Minimizes divergence between high-dimensional and low-dimensional distributions
- Uses gradient descent optimization
**Key Points**:
- Great for visualization
- Preserves local neighborhood structure
- Non-deterministic results
- Computationally expensive

**Interview Questions**:
- What's the difference between PCA and t-SNE?
- How do you choose perplexity parameter?
- Why is t-SNE good for visualization but not for feature reduction?

## Model Evaluation & Validation

### 1. Cross-Validation
**Types**:
- K-Fold: Split data into k folds, train on k-1, test on 1
- Stratified K-Fold: Maintains class distribution in each fold
- Leave-One-Out: Each sample is a test set
- Time Series: Respects temporal order

**Interview Questions**:
- When would you use stratified vs regular k-fold?
- How do you handle time series data in cross-validation?
- What's the trade-off between k-fold and holdout validation?

### 2. Evaluation Metrics
**Classification**:
- Accuracy: Correct predictions / Total predictions
- Precision: True Positives / (True Positives + False Positives)
- Recall: True Positives / (True Positives + False Negatives)
- F1-Score: 2 * (Precision * Recall) / (Precision + Recall)
- ROC-AUC: Area under receiver operating characteristic curve

**Regression**:
- MSE: Mean Squared Error
- RMSE: Root Mean Squared Error
- MAE: Mean Absolute Error
- R²: Coefficient of determination

**Interview Questions**:
- When would you use precision vs recall?
- How do you interpret ROC-AUC?
- What's the difference between MSE and MAE?

## Feature Engineering

### 1. Feature Selection
**Methods**:
- Filter: Statistical tests (chi-square, mutual information)
- Wrapper: Forward/backward selection, recursive feature elimination
- Embedded: L1 regularization, tree-based importance

**Interview Questions**:
- What's the difference between filter and wrapper methods?
- How do you handle multicollinearity in feature selection?
- When would you use univariate vs multivariate feature selection?

### 2. Feature Scaling
**Methods**:
- Standardization: (x - mean) / std
- Normalization: (x - min) / (max - min)
- Robust Scaling: (x - median) / IQR

**Interview Questions**:
- When would you use standardization vs normalization?
- How do you handle outliers in feature scaling?
- Which algorithms require feature scaling?

## Hyperparameter Tuning

### 1. Grid Search
**Concept**: Exhaustively search predefined hyperparameter space
**Pros**: Guaranteed to find best combination in search space
**Cons**: Computationally expensive, curse of dimensionality

### 2. Random Search
**Concept**: Randomly sample hyperparameter combinations
**Pros**: More efficient than grid search, can find good solutions quickly
**Cons**: No guarantee of finding optimal solution

### 3. Bayesian Optimization
**Concept**: Use previous results to guide next hyperparameter choice
**Pros**: More efficient than random search, balances exploration/exploitation
**Cons**: More complex to implement

**Interview Questions**:
- When would you use grid search vs random search?
- How do you choose hyperparameter ranges?
- What's the difference between hyperparameter tuning and model selection?

## Common Interview Scenarios

### 1. Algorithm Selection
**Scenario**: "Given a dataset with 1 million samples and 1000 features, which algorithm would you choose?"
**Considerations**:
- Dataset size and dimensionality
- Training time requirements
- Interpretability needs
- Accuracy requirements
- Memory constraints

### 2. Overfitting Solutions
**Scenario**: "Your model performs well on training data but poorly on test data. How do you fix this?"
**Solutions**:
- Regularization (L1, L2)
- Cross-validation
- Feature selection
- Ensemble methods
- More training data
- Early stopping

### 3. Missing Data Handling
**Scenario**: "Your dataset has 30% missing values. How do you handle this?"
**Strategies**:
- Deletion (listwise, pairwise)
- Imputation (mean, median, mode, regression)
- Advanced methods (KNN, iterative imputation)
- Model-based approaches

### 4. Class Imbalance
**Scenario**: "Your dataset has 95% negative and 5% positive examples. How do you handle this?"
**Solutions**:
- Resampling (oversampling, undersampling)
- Cost-sensitive learning
- Ensemble methods
- Anomaly detection approaches
- Evaluation metrics (precision, recall, F1)

This comprehensive guide covers the essential machine learning algorithms and concepts that are commonly tested in AI/ML interviews.
