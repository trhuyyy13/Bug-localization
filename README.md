# Bug Localization Model

## Project Description

This project builds a **Bug Localization** model using **Deep Learning** to detect bugs in source code based on bug reports. The model is trained using **k-fold cross-validation** and uses **Focal Loss** to address the class imbalance problem between positive and negative samples.

## Steps Taken

### 1. **Data Preprocessing**:
   - **Stopwords Removal**: Removes common **stop words** and **Java keywords** from both bug reports and source code to focus on more meaningful words.
   - **Tokenization**: Breaks down bug reports and source code into individual words.
   - **Stemming**: Applies **Porter Stemmer** to reduce words to their root form.
   - **Normalization**: Removes punctuation, numbers, and converts words to lowercase.
   - **POS Tagging**: Assigns part-of-speech tags to words in bug reports and source code.
   - **Stack Trace Parsing**: Extracts stack traces from bug reports to identify errors related to the source code.

### 2. **Feature Extraction**:
   - **Lexical Similarity**: Measures lexical similarity between bug reports and source code using **TF-IDF**.
   - **Semantic Similarity**: Measures semantic similarity using **GloVe** or **Word2Vec** embeddings.
   - **Bug Fix History**: Uses information from previous bug reports to enhance the prediction accuracy for recurring issues.

### 3. **Model Training**:
   - Uses a **Deep Neural Network (DNN)** to learn from the extracted features.
   - Applies **Focal Loss** to address the class imbalance problem (few bug reports, many source files).

### 4. **Model Evaluation**:
   - Uses **k-fold cross-validation** to evaluate the model.
   - Calculates performance metrics:
     - **MAP (Mean Average Precision)**: Measures the effectiveness of the model in detecting bugs.
     - **MRR (Mean Reciprocal Rank)**: Evaluates the ranking accuracy of the model.
     - **Top-k Accuracy**: Measures the number of correct bug files identified in the top-k predicted source files.

### 5. **Optimization and Deployment**:
   - **Parameter Tuning**: Optimizes model parameters such as **learning rate**, **batch size**, and network depth.
   - **Regularization**: Uses **L2 Regularization** and **Dropout** to prevent overfitting.
   - **Model Deployment**: Integrates the trained model into a real-world system to automatically detect bugs when new bug reports are generated.

## Libraries Used
- **PyTorch**: The primary library for building and training the deep learning model.
- **Scikit-learn**: Used for evaluating metrics such as **MAP** and **MRR**.
- **NumPy**: Handles array operations and numerical computations.
- **GloVe/Word2Vec**: Used for calculating semantic similarity between words in the bug report and source code.

## Installation and Usage

### 1. **Clone the Repository**
   Clone this repository to your local machine:
   ```bash
   git clone <repository_url>
   ```
### 2. Install the Required Libraries
   ```bash
Install the required libraries using:

pip install -r requirements.txt
```
### 3. Run Model Training and Evaluation
To train and evaluate the model, run the following command:
```bash
python run_model.py
```
### 4. Results
After training and evaluation, the results will be printed with metrics MAP, MRR, and Top-k Accuracy (k = 1, 5, 10, 15) for each fold and the overall model.
