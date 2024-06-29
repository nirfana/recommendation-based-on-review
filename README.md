# Recommendation Based on Sephora Review

## Objective 
The primary objective of this project is to analyze Sephora skincare product reviews to determine whether a product is recommended or not that expressed in user reviews. This involves building and evaluating an NLP model using a dataset from Kaggle.

Data source [here](https://www.kaggle.com/datasets/nadyinky/sephora-products-and-skincare-reviews/data).

---
## Process

1. Data Acquisition<br>
    - **Kaggle API Setup**: The Kaggle API was installed and configured to access the required dataset.<br>
    - **Dataset Download**: The dataset containing Sephora product reviews was downloaded from Kaggle using the API.
2. Data Preparation<br>
    - **Unzipping the Dataset**: The downloaded dataset was unzipped to extract the data files.<br>
    - **Data Cleaning**: Only select related columns for the model building.<br>
    - **Data Exploration**: Initial exploration of the data to understand the structure and content of the reviews.
3. Model Building
    - **Text Preprocessing**: Reviews were tokenized, and stopwords were removed. Additional preprocessing steps such as stemming or lemmatization were applied as necessary.<br>
    - **Model Training**: The ANN model was trained on the preprocessed data.
    - **Model Evaluation**: The model's performance was evaluated using metrics such as accuracy, precision, recall, and F1-score. The base model then re-train using another ANN architecture to get better metrics.

---
## Model Limitation
- **Data Quality**: The accuracy of the model heavily depends on the quality of the review data. Incomplete or biased reviews like sarcasm can affect model performance. The nuances of human sentiment can be challenging to capture accurately, especially in cases of sarcasm or ambiguous language.
- **Generalization**: The model is trained on a specific dataset from Sephora and may not generalize well to reviews from other platforms or product categories.

---
## Future Work
- **Advanced Models**: Exploring more sophisticated NLP models like BERT or GPT for better performance.
- **Feature Engineering**: Experimenting with different feature extraction techniques to capture more context from the reviews. Apply techniques like stemming, lemmatization, and spell checking to reduce vocabulary size and improve model generalization.
- **Learning Rate Scheduling**: Implement learning rate schedules (e.g., decay schedules, cyclical learning rates) to optimize convergence and improve model training efficiency.
- **Class Weight Adjustment**: Adjust class weights during training to penalize misclassifications of minority classes more heavily, addressing class imbalance issues.
- **Pre-trained Embeddings**: Utilize pre-trained word embeddings (e.g., Word2Vec, GloVe, BERT embeddings) to initialize LSTM layers, leveraging transfer learning to improve model performance on specific tasks.

--- 
## Deployment
Try the model [here](https://huggingface.co/spaces/dnirfana/recommendation-based-on-review?logs=build).