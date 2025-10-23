# Deep Learning Fundamentals

## Neural Network Basics

### 1. Perceptron
**Concept**: Single-layer neural network for binary classification
**Mathematical Foundation**: y = f(w₁x₁ + w₂x₂ + ... + wₙxₙ + b)
**Activation Function**: Step function (0 or 1)
**Limitations**: Can only learn linearly separable patterns

**Interview Questions**:
- What are the limitations of a single perceptron?
- How does the perceptron learning algorithm work?
- What's the difference between a perceptron and a logistic regression?

### 2. Multi-Layer Perceptron (MLP)
**Concept**: Feedforward neural network with multiple hidden layers
**Architecture**: Input layer → Hidden layers → Output layer
**Key Components**:
- Weights and biases
- Activation functions
- Forward propagation
- Backpropagation

**Interview Questions**:
- Why do we need hidden layers in neural networks?
- How does backpropagation work?
- What's the vanishing gradient problem?

### 3. Activation Functions
**Sigmoid**: σ(x) = 1/(1 + e^(-x))
- Range: (0, 1)
- Smooth gradient
- Suffers from vanishing gradient problem

**Tanh**: tanh(x) = (e^x - e^(-x))/(e^x + e^(-x))
- Range: (-1, 1)
- Zero-centered
- Still has vanishing gradient problem

**ReLU**: f(x) = max(0, x)
- Range: [0, ∞)
- Solves vanishing gradient problem
- Can cause dead neurons

**Leaky ReLU**: f(x) = max(0.01x, x)
- Prevents dead neurons
- Small negative slope for negative inputs

**Softmax**: f(x_i) = e^(x_i) / Σe^(x_j)
- Used in output layer for multi-class classification
- Outputs probability distribution

**Interview Questions**:
- Why is ReLU preferred over sigmoid/tanh?
- What's the dead neuron problem in ReLU?
- When would you use softmax vs sigmoid?

## Convolutional Neural Networks (CNNs)

### 1. CNN Architecture
**Components**:
- Convolutional layers: Apply filters to detect features
- Pooling layers: Reduce spatial dimensions
- Fully connected layers: Final classification

**Key Concepts**:
- Local connectivity: Each neuron connects to local region
- Weight sharing: Same filter applied across entire image
- Translation invariance: Detects features regardless of position

### 2. Convolution Operation
**Mathematical Foundation**: (f * g)(t) = ∫f(τ)g(t-τ)dτ
**In Practice**: Element-wise multiplication and summation
**Parameters**:
- Filter size (kernel size)
- Stride: Step size for filter movement
- Padding: Adding zeros around input
- Number of filters

**Interview Questions**:
- How do you choose the filter size?
- What's the difference between valid and same padding?
- How do you calculate output dimensions after convolution?

### 3. Pooling Layers
**Max Pooling**: Takes maximum value in each region
- Reduces overfitting
- Provides translation invariance
- Reduces computational load

**Average Pooling**: Takes average value in each region
- Smoother output
- Less aggressive than max pooling

**Global Average Pooling**: Averages entire feature map
- Reduces parameters
- Prevents overfitting
- Used in modern architectures

**Interview Questions**:
- Why do we use pooling layers?
- What's the difference between max and average pooling?
- How does pooling help with overfitting?

### 4. Popular CNN Architectures
**LeNet-5**: Early CNN for digit recognition
- 2 convolutional + 3 fully connected layers
- Pioneered CNN architecture

**AlexNet**: Breakthrough in ImageNet competition
- 8 layers (5 conv + 3 FC)
- ReLU activation
- Dropout regularization
- Data augmentation

**VGG**: Very deep networks with small filters
- 3x3 filters throughout
- Up to 19 layers
- Simple architecture
- High memory usage

**ResNet**: Residual connections solve vanishing gradient
- Skip connections (identity mappings)
- Enables training of very deep networks (100+ layers)
- Batch normalization

**Inception**: Multiple filter sizes in parallel
- 1x1, 3x3, 5x5 convolutions
- Reduces computational cost
- Better feature extraction

**Interview Questions**:
- How does ResNet solve the vanishing gradient problem?
- What's the advantage of using 1x1 convolutions?
- How do you choose between different CNN architectures?

## Recurrent Neural Networks (RNNs)

### 1. RNN Architecture
**Concept**: Networks with memory, process sequences
**Mathematical Foundation**: h_t = f(W_hh * h_{t-1} + W_xh * x_t + b_h)
**Key Properties**:
- Shared parameters across time steps
- Can process variable-length sequences
- Suffers from vanishing/exploding gradients

**Interview Questions**:
- Why do RNNs have memory?
- What's the difference between RNNs and feedforward networks?
- How do you handle variable-length sequences?

### 2. LSTM (Long Short-Term Memory)
**Concept**: RNN variant that can learn long-term dependencies
**Components**:
- Forget gate: Decides what to discard
- Input gate: Decides what to store
- Output gate: Decides what to output
- Cell state: Long-term memory

**Mathematical Foundation**:
- f_t = σ(W_f * [h_{t-1}, x_t] + b_f)  # Forget gate
- i_t = σ(W_i * [h_{t-1}, x_t] + b_i)  # Input gate
- C̃_t = tanh(W_C * [h_{t-1}, x_t] + b_C)  # Candidate values
- C_t = f_t * C_{t-1} + i_t * C̃_t  # Cell state
- o_t = σ(W_o * [h_{t-1}, x_t] + b_o)  # Output gate
- h_t = o_t * tanh(C_t)  # Hidden state

**Interview Questions**:
- How does LSTM solve the vanishing gradient problem?
- What's the role of each gate in LSTM?
- When would you use LSTM vs GRU?

### 3. GRU (Gated Recurrent Unit)
**Concept**: Simplified version of LSTM
**Components**:
- Reset gate: Decides how much past information to forget
- Update gate: Decides how much past information to keep
- Hidden state: Combines past and current information

**Mathematical Foundation**:
- r_t = σ(W_r * [h_{t-1}, x_t] + b_r)  # Reset gate
- z_t = σ(W_z * [h_{t-1}, x_t] + b_z)  # Update gate
- h̃_t = tanh(W_h * [r_t * h_{t-1}, x_t] + b_h)  # Candidate
- h_t = (1 - z_t) * h_{t-1} + z_t * h̃_t  # Hidden state

**Interview Questions**:
- What's the difference between LSTM and GRU?
- Why is GRU simpler than LSTM?
- When would you choose GRU over LSTM?

## Transformers and Attention

### 1. Attention Mechanism
**Concept**: Focus on relevant parts of input when making predictions
**Types**:
- Self-attention: Attention within same sequence
- Cross-attention: Attention between different sequences
- Multi-head attention: Multiple attention mechanisms in parallel

**Mathematical Foundation**:
- Attention(Q,K,V) = softmax(QK^T/√d_k)V
- Q: Query matrix
- K: Key matrix  
- V: Value matrix
- d_k: Dimension of key vectors

**Interview Questions**:
- How does attention work mathematically?
- What's the purpose of the scaling factor √d_k?
- How does multi-head attention help?

### 2. Transformer Architecture
**Components**:
- Encoder: Processes input sequence
- Decoder: Generates output sequence
- Self-attention layers
- Feed-forward networks
- Layer normalization
- Residual connections

**Key Innovations**:
- Parallel processing (unlike RNNs)
- Self-attention captures long-range dependencies
- Positional encoding for sequence information

**Interview Questions**:
- How do transformers process sequences in parallel?
- What's the role of positional encoding?
- How do transformers compare to RNNs?

### 3. BERT (Bidirectional Encoder Representations)
**Concept**: Pre-trained transformer encoder for NLP tasks
**Key Features**:
- Bidirectional: Reads text in both directions
- Masked Language Model: Predicts masked tokens
- Next Sentence Prediction: Predicts if sentences follow each other
- Transfer learning: Fine-tune for specific tasks

**Interview Questions**:
- How does BERT achieve bidirectional understanding?
- What's the difference between BERT and GPT?
- How do you fine-tune BERT for specific tasks?

### 4. GPT (Generative Pre-trained Transformer)
**Concept**: Autoregressive language model using transformer decoder
**Key Features**:
- Unidirectional: Generates text left-to-right
- Causal attention: Can't see future tokens
- Next token prediction: Predicts next word in sequence
- Zero-shot learning: Can perform tasks without fine-tuning

**Interview Questions**:
- How does GPT generate text?
- What's the difference between BERT and GPT?
- How does GPT achieve zero-shot learning?

## Training and Optimization

### 1. Loss Functions
**Cross-Entropy Loss**: For classification
- Binary: L = -[y*log(ŷ) + (1-y)*log(1-ŷ)]
- Multi-class: L = -Σy_i*log(ŷ_i)

**Mean Squared Error**: For regression
- L = (1/n)Σ(y_i - ŷ_i)²

**Hinge Loss**: For SVM-like classification
- L = max(0, 1 - y*ŷ)

**Interview Questions**:
- When would you use cross-entropy vs MSE?
- How do you handle class imbalance in loss functions?
- What's the difference between categorical and sparse categorical cross-entropy?

### 2. Optimization Algorithms
**SGD (Stochastic Gradient Descent)**:
- Updates weights using gradient of loss
- Can get stuck in local minima
- Sensitive to learning rate

**Adam (Adaptive Moment Estimation)**:
- Combines momentum and adaptive learning rates
- Computes running averages of gradients
- Generally works well out of the box

**RMSprop**:
- Adapts learning rate based on gradient magnitude
- Good for non-stationary objectives

**Interview Questions**:
- What's the difference between SGD and Adam?
- How do you choose the learning rate?
- What's the difference between batch, mini-batch, and stochastic gradient descent?

### 3. Regularization Techniques
**Dropout**: Randomly set neurons to zero during training
- Prevents overfitting
- Forces network to be robust
- Usually applied to fully connected layers

**Batch Normalization**: Normalize inputs to each layer
- Accelerates training
- Reduces internal covariate shift
- Acts as regularizer

**Weight Decay (L2 Regularization)**: Add penalty for large weights
- Prevents overfitting
- Encourages smaller weights

**Early Stopping**: Stop training when validation loss stops improving
- Prevents overfitting
- Saves computational resources

**Interview Questions**:
- How does dropout prevent overfitting?
- What's the difference between batch norm and layer norm?
- How do you choose the dropout rate?

## Advanced Topics

### 1. Transfer Learning
**Concept**: Use pre-trained models for new tasks
**Approaches**:
- Feature extraction: Use pre-trained features, train new classifier
- Fine-tuning: Adjust pre-trained weights for new task
- Domain adaptation: Adapt to different data distribution

**Interview Questions**:
- When would you use transfer learning?
- How do you choose between feature extraction and fine-tuning?
- What's the difference between transfer learning and multi-task learning?

### 2. Generative Models
**GANs (Generative Adversarial Networks)**:
- Generator: Creates fake data
- Discriminator: Distinguishes real from fake
- Adversarial training: Generator and discriminator compete

**VAEs (Variational Autoencoders)**:
- Encoder: Maps data to latent space
- Decoder: Reconstructs data from latent space
- Probabilistic approach to generation

**Interview Questions**:
- How do GANs work?
- What's the difference between GANs and VAEs?
- How do you evaluate generative models?

### 3. Reinforcement Learning
**Q-Learning**: Learn action-value function
- Q(s,a) = expected future reward for action a in state s
- Uses Bellman equation for updates

**Policy Gradient**: Directly optimize policy
- REINFORCE algorithm
- Actor-critic methods

**Interview Questions**:
- What's the difference between Q-learning and policy gradient?
- How does the exploration vs exploitation trade-off work?
- What's the difference between on-policy and off-policy learning?

## Common Interview Scenarios

### 1. Architecture Design
**Scenario**: "Design a CNN for image classification with 1M images and 1000 classes"
**Considerations**:
- Model capacity vs overfitting
- Computational constraints
- Transfer learning opportunities
- Data augmentation strategies

### 2. Training Issues
**Scenario**: "Your model isn't learning. What could be wrong?"
**Debugging Steps**:
- Check data preprocessing
- Verify loss function
- Examine learning rate
- Check for gradient flow
- Validate model architecture

### 3. Performance Optimization
**Scenario**: "Your model is too slow for production. How do you optimize it?"
**Strategies**:
- Model compression (quantization, pruning)
- Architecture optimization
- Hardware acceleration
- Batch processing
- Model distillation

This comprehensive guide covers the essential deep learning concepts and architectures commonly tested in AI/ML interviews.
