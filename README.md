# Diamond_price_prediction

# 💎 Diamond Price Prediction Using Machine Learning
![Uploading image.png…]()

## 1. Project Overview

The **Diamond Price Prediction** project is a Machine Learning-based web application that predicts the estimated price of a diamond based on its characteristics and measurements.

The application uses a trained Machine Learning regression model and Streamlit to provide an interactive interface where users can enter diamond details and receive an estimated price in USD.

## 2. Objectives

- Predict diamond prices using Machine Learning.
- Understand the relationship between diamond characteristics and price.
- Perform predictions using a trained regression model.
- Build an interactive web application using Streamlit.

## 3. Technologies Used

- **Programming Language:** Python
- **Libraries:** NumPy, Pandas, Scikit-learn
- **Data Visualization:** Matplotlib
- **Web Framework:** Streamlit
- **Model Storage:** Pickle

## 4. Features Used for Prediction

The application accepts the following inputs:

| Feature | Description |
|---|---|
| Carat | Weight of the diamond |
| Cut | Quality of diamond cut |
| Color | Diamond color grade |
| Clarity | Diamond clarity grade |
| Depth | Diamond depth percentage |
| Table | Diamond table percentage |
| X | Length in mm |
| Y | Width in mm |
| Z | Depth in mm |

### Additional Features

The application also creates additional features:

- Volume = X × Y × Z
- Log Carat = Logarithm of carat weight
- Carat Group = Category based on carat weight

## 5. Machine Learning Approach

This project uses a trained regression model to estimate diamond prices.

The application loads the saved model and supporting feature files to generate predictions.

## 6. Project Structure

```text
Diamond-Price-Prediction/
│
├── app.py
├── model.pkl
├── feature_columns.pkl
├── maps.pkl
├── requirements.txt
└── README.md
```

**File descriptions:**

- `app.py` – Streamlit application.
- `model.pkl` – Trained Machine Learning model.
- `feature_columns.pkl` – Stores the feature column order expected by the model.
- `maps.pkl` – Stores mappings for categorical features.
- `requirements.txt` – Required Python libraries.
- `README.md` – Project documentation.

## 7. Installation and Setup

### Step 1: Clone the Repository

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
```

### Step 2: Navigate to the Project Folder

```bash
cd Diamond-Price-Prediction
```

### Step 3: Create a Virtual Environment

```bash
python -m venv diamond_env
```

### Step 4: Activate the Environment

For Windows:

```bash
diamond_env\Scripts\activate
```

### Step 5: Install Required Libraries

```bash
pip install -r requirements.txt
```

### Step 6: Run the Streamlit Application

```bash
streamlit run app.py
```

The application will open in your browser.

## 8. How to Use the Application

1. Open the Diamond Price Prediction application.
2. Enter the carat weight.
3. Select the cut, color, and clarity.
4. Enter the diamond measurements.
5. Click **Estimate Diamond Price**.
6. View the predicted diamond price in USD.

## 9. Output

The application displays an estimated diamond price based on the entered characteristics.

**Note:** The predicted price is a Machine Learning-generated estimate. It is intended as a guide and is not a formal diamond appraisal.

## 10. Future Improvements

- Improve prediction accuracy through model tuning.
- Compare different regression algorithms.
- Add more data visualizations.
- Deploy the application online.
- Monitor prediction performance and retrain the model when necessary.

## 11. Conclusion

This project demonstrates how Machine Learning can be used to predict diamond prices based on diamond characteristics. By integrating a trained regression model with Streamlit, the project provides a simple and interactive application for diamond price estimation.

---

**Project Title:** Diamond Price Prediction Using Machine Learning  
**Domain:** Machine Learning – Regression  
**Application:** Streamlit Web Application
