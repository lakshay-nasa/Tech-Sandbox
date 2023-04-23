import pandas as pd
import numpy as np

# Load the data
df = pd.read_csv("./datasetb2d9982/dataset/train.csv")

# Print the number of missing values in each column
print(df.isnull().sum())

# Drop any rows with missing values
df.dropna(inplace=True)

# Preprocess the text data
import nltk
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
nltk.download('stopwords')

# Function to preprocess the text data
def preprocess_text(text):
    # Tokenize the text
    tokens = nltk.word_tokenize(text.lower())
    
    # Remove stop words
    stop_words = set(stopwords.words('english'))
    filtered_tokens = [token for token in tokens if token not in stop_words]
    
    # Stem the words
    stemmer = PorterStemmer()
    stemmed_tokens = [stemmer.stem(token) for token in filtered_tokens]
    
    # Join the tokens back into a single string
    preprocessed_text = " ".join(stemmed_tokens)
    
    return preprocessed_text

# Preprocess the text data in the TITLE, DESCRIPTION, and BULLET_POINTS columns
df["TITLE"] = df["TITLE"].apply(preprocess_text)
df["DESCRIPTION"] = df["DESCRIPTION"].apply(preprocess_text)
df["BULLET_POINTS"] = df["BULLET_POINTS"].apply(preprocess_text)


from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer

# Define the feature columns
text_columns = ["TITLE", "DESCRIPTION", "BULLET_POINTS"]
categorical_columns = ["PRODUCT_TYPE_ID"]

# Vectorize the text data
vectorizer = TfidfVectorizer()
text_features = vectorizer.fit_transform(df[text_columns].apply(lambda x: " ".join(x), axis=1))

# One-hot encode the categorical features
encoder = OneHotEncoder()
categorical_features = encoder.fit_transform(df[categorical_columns])

# Combine the features
feature_names = vectorizer.get_feature_names() + encoder.get_feature_names(categorical_columns)
X = np.concatenate((text_features.toarray(), categorical_features.toarray()), axis=1)
y = df["PRODUCT_LENGTH"].values

# Define a column transformer to apply the same preprocessing to new data
preprocessor = ColumnTransformer([
    ("text", vectorizer, text_columns),
    ("cat", encoder, categorical_columns)
])


from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.linear_model import LinearRegression, Lasso, Ridge
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor, GradientBoostingRegressor
from sklearn.metrics import mean_absolute_percentage_error
import numpy as np

# Split the data into training and testing sets
# X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Evaluate the performance of different models using cross-validation
models = [
    LinearRegression(),
    Lasso(),
    Ridge(),
    DecisionTreeRegressor(),
    RandomForestRegressor(),
    GradientBoostingRegressor()
]
for model in models:
    scores = cross_val_score(model, X_train, y_train, cv=5, scoring="neg_mean_absolute_percentage_error")
    print(type(model).__name__)
    print("Mean absolute percentage error: {:.2f}%".format(-100 * np.mean(scores)))
    print()

# Train and evaluate the best model on the test set
best_model = GradientBoostingRegressor()
best_model.fit(X_train, y_train)
y_pred = best_model.predict(X_test)
mape = mean_absolute_percentage_error(y_test, y_pred)
print("Mean absolute percentage error on test set: {:.2f}%".format(100 * mape))

