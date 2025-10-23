# AI Interview Questions & Answers

## Machine Learning Fundamentals

### Q1: What's the difference between supervised and unsupervised learning?
**Answer**: 
- **Supervised Learning**: Uses labeled training data to learn a mapping from inputs to outputs. Examples include classification and regression.
- **Unsupervised Learning**: Finds patterns in data without labeled examples. Examples include clustering and dimensionality reduction.
- **Key Difference**: Supervised learning has ground truth labels, unsupervised learning discovers hidden patterns.

### Q2: Explain the bias-variance tradeoff.
**Answer**:
- **Bias**: Error due to oversimplified assumptions in the learning algorithm (underfitting)
- **Variance**: Error due to sensitivity to small fluctuations in training data (overfitting)
- **Tradeoff**: As model complexity increases, bias decreases but variance increases
- **Optimal Point**: Balance between bias and variance for best generalization

### Q3: How do you handle overfitting?
**Answer**:
- **Regularization**: L1 (Lasso) and L2 (Ridge) regularization
- **Cross-validation**: Use k-fold CV to assess model performance
- **Feature selection**: Remove irrelevant features
- **Ensemble methods**: Random Forest, Bagging, Boosting
- **More data**: Increase training dataset size
- **Early stopping**: Stop training when validation performance plateaus

### Q4: What's the difference between precision and recall?
**Answer**:
- **Precision**: True Positives / (True Positives + False Positives) - "How many selected items are relevant?"
- **Recall**: True Positives / (True Positives + False Negatives) - "How many relevant items are selected?"
- **Tradeoff**: Increasing precision often decreases recall and vice versa
- **Use Cases**: High precision for spam detection, high recall for medical diagnosis

### Q5: When would you use Random Forest vs SVM?
**Answer**:
- **Random Forest**: 
  - Good for tabular data with mixed feature types
  - Handles missing values well
  - Provides feature importance
  - Less sensitive to hyperparameters
- **SVM**:
  - Good for high-dimensional data
  - Works well with clear margin of separation
  - Memory efficient
  - Requires feature scaling

## Deep Learning

### Q6: What's the vanishing gradient problem?
**Answer**:
- **Definition**: Gradients become exponentially smaller as they propagate backward through deep networks
- **Cause**: Multiplying small gradients through many layers
- **Solutions**: 
  - ReLU activation functions
  - Batch normalization
  - Residual connections (ResNet)
  - LSTM/GRU for RNNs
  - Proper weight initialization

### Q7: Explain how backpropagation works.
**Answer**:
1. **Forward Pass**: Compute predictions using current weights
2. **Compute Loss**: Calculate error between predictions and targets
3. **Backward Pass**: 
   - Compute gradients using chain rule
   - Propagate gradients backward through network
   - Update weights using gradient descent
4. **Repeat**: Continue until convergence

### Q8: What's the difference between CNN and RNN?
**Answer**:
- **CNN (Convolutional Neural Networks)**:
  - Designed for spatial data (images)
  - Uses convolution and pooling layers
  - Translation invariant
  - Processes entire input simultaneously
- **RNN (Recurrent Neural Networks)**:
  - Designed for sequential data (text, time series)
  - Has memory through hidden states
  - Processes input step by step
  - Can handle variable-length sequences

### Q9: How does attention mechanism work?
**Answer**:
- **Concept**: Focus on relevant parts of input when making predictions
- **Mathematical**: Attention(Q,K,V) = softmax(QK^T/√d_k)V
- **Components**:
  - Query (Q): What we're looking for
  - Key (K): What we're looking in
  - Value (V): What we extract
- **Benefits**: Captures long-range dependencies, interpretable

### Q10: What's transfer learning?
**Answer**:
- **Definition**: Using knowledge from one task to improve performance on another task
- **Approaches**:
  - Feature extraction: Use pre-trained features, train new classifier
  - Fine-tuning: Adjust pre-trained weights for new task
- **Benefits**: Faster training, better performance with less data
- **Examples**: Using ImageNet pre-trained models for medical imaging

## Natural Language Processing

### Q11: What's the difference between Word2Vec and BERT?
**Answer**:
- **Word2Vec**:
  - Static word embeddings
  - Same representation regardless of context
  - Trained on large corpus
  - Fast inference
- **BERT**:
  - Contextual embeddings
  - Same word has different representations in different contexts
  - Pre-trained transformer model
  - Better performance but slower

### Q12: How do you handle text preprocessing?
**Answer**:
- **Tokenization**: Split text into words/subwords
- **Normalization**: Lowercasing, stemming, lemmatization
- **Cleaning**: Remove special characters, URLs, stop words
- **Encoding**: Convert text to numerical representations
- **Padding/Truncation**: Handle variable-length sequences

### Q13: What's the difference between extractive and abstractive summarization?
**Answer**:
- **Extractive**: Selects important sentences from original text
  - Preserves original wording
  - Easier to implement
  - May lack coherence
- **Abstractive**: Generates new sentences summarizing content
  - More natural summaries
  - Harder to implement
  - Requires language generation capabilities

## Computer Vision

### Q14: How does object detection work?
**Answer**:
- **Two-stage Detectors** (R-CNN family):
  - Generate region proposals
  - Classify and refine each proposal
  - More accurate but slower
- **One-stage Detectors** (YOLO, SSD):
  - Directly predict bounding boxes and classes
  - Faster but less accurate
- **Key Components**: Feature extraction, region proposal, classification, regression

### Q15: What's the difference between semantic and instance segmentation?
**Answer**:
- **Semantic Segmentation**: Classifies each pixel into semantic categories
  - Doesn't distinguish between instances
  - Example: All cars are labeled as "car"
- **Instance Segmentation**: Identifies and segments individual objects
  - Distinguishes between instances
  - Example: Car1, Car2, Car3 are separate

## Model Evaluation & Validation

### Q16: How do you choose evaluation metrics?
**Answer**:
- **Classification**:
  - Accuracy: Balanced datasets
  - Precision/Recall: Imbalanced datasets
  - F1-score: Balance between precision and recall
  - ROC-AUC: Overall performance across thresholds
- **Regression**:
  - MSE: Penalizes large errors more
  - MAE: Robust to outliers
  - R²: Proportion of variance explained

### Q17: What's cross-validation and why use it?
**Answer**:
- **Definition**: Technique to assess model performance by splitting data into multiple folds
- **Types**: K-fold, stratified, leave-one-out, time series
- **Benefits**:
  - More reliable performance estimate
  - Reduces overfitting
  - Better use of limited data
- **Use Case**: Model selection, hyperparameter tuning

## Feature Engineering

### Q18: How do you handle missing data?
**Answer**:
- **Deletion**: Remove rows/columns with missing values
- **Imputation**:
  - Mean/median for numerical data
  - Mode for categorical data
  - Regression-based imputation
  - KNN imputation
- **Advanced**: Matrix completion, deep learning methods
- **Consideration**: Understand why data is missing (MCAR, MAR, MNAR)

### Q19: What's feature scaling and when is it needed?
**Answer**:
- **Definition**: Normalizing feature values to similar scales
- **Methods**: Standardization, normalization, robust scaling
- **When needed**: Distance-based algorithms (KNN, SVM), neural networks
- **When not needed**: Tree-based algorithms (Random Forest, XGBoost)

## Hyperparameter Tuning

### Q20: How do you tune hyperparameters?
**Answer**:
- **Grid Search**: Exhaustive search over predefined parameter space
- **Random Search**: Random sampling of parameter combinations
- **Bayesian Optimization**: Uses previous results to guide next search
- **Automated**: Optuna, Hyperopt, Ray Tune
- **Considerations**: Computational budget, parameter importance, search space

## System Design

### Q21: How would you design a recommendation system?
**Answer**:
- **Data Collection**: User interactions, item features, user profiles
- **Approaches**:
  - Collaborative filtering: User-based, item-based
  - Content-based: Item features
  - Hybrid: Combine multiple approaches
- **Architecture**: Real-time vs batch processing
- **Evaluation**: A/B testing, offline metrics
- **Scalability**: Distributed training, model serving

### Q22: How would you deploy a machine learning model?
**Answer**:
- **Model Packaging**: Containerization (Docker)
- **Serving**: REST API, gRPC, batch processing
- **Infrastructure**: Cloud platforms, Kubernetes
- **Monitoring**: Model performance, data drift, system metrics
- **CI/CD**: Automated testing, deployment pipelines
- **Scaling**: Load balancing, auto-scaling

## Ethics & Responsible AI

### Q23: How do you ensure AI fairness?
**Answer**:
- **Data**: Representative datasets, bias detection
- **Model**: Fairness constraints, adversarial debiasing
- **Evaluation**: Fairness metrics across groups
- **Monitoring**: Ongoing bias detection
- **Governance**: Diverse teams, ethical guidelines

### Q24: What are the risks of AI systems?
**Answer**:
- **Bias**: Unfair treatment of certain groups
- **Privacy**: Data leakage, re-identification
- **Security**: Adversarial attacks, model extraction
- **Transparency**: Black box decisions
- **Accountability**: Responsibility for AI decisions
- **Job Displacement**: Economic impact

## Practical Scenarios

### Q25: Your model performs well on training data but poorly on test data. What do you do?
**Answer**:
1. **Diagnose**: Check for overfitting
2. **Solutions**:
   - Increase regularization
   - Reduce model complexity
   - Get more training data
   - Improve feature engineering
   - Use cross-validation
   - Check for data leakage

### Q26: How do you handle a dataset with 95% negative and 5% positive examples?
**Answer**:
- **Resampling**: Oversample minority class, undersample majority class
- **Cost-sensitive learning**: Assign higher cost to misclassifying positive examples
- **Evaluation**: Use precision, recall, F1-score instead of accuracy
- **Algorithms**: Use algorithms robust to imbalance (Random Forest, SVM)
- **Data**: Collect more positive examples if possible

### Q27: How do you choose between different machine learning algorithms?
**Answer**:
- **Data size**: Small data → simple algorithms, large data → complex algorithms
- **Interpretability**: Need explanations → linear models, trees
- **Performance**: Need best accuracy → ensemble methods, deep learning
- **Speed**: Real-time → simple models, batch → complex models
- **Data type**: Text → NLP models, images → CNNs, tabular → traditional ML

This comprehensive Q&A covers the most common AI/ML interview questions and provides detailed answers to help you prepare effectively.
