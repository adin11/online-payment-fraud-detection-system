import streamlit as st
import pandas as pd
import joblib


@st.cache_resource
def load_model():
    model_data = joblib.load('fraud_detection_model.pkl')  # Update with your file path
    return model_data

st.set_page_config(page_icon='⚡',page_title='Fraud Checker')

model_data = load_model()
loaded_model = model_data['model']
loaded_features = model_data['features']
label_mapping = model_data['label_mapping']

# Transaction type mapping
transaction_mapping = {
    "CASH_OUT": 1,
    "PAYMENT": 2,
    "CASH_IN": 3,
    "TRANSFER": 4,
    "DEBIT": 5
}

st.title("Online Payment Fraud Detection System")
st.subheader("Enter the transaction details below:")

with st.expander("Description"):
    st.info("""
**Note**: This app uses a machine learning model to predict the likelihood of a transaction being fraudulent based on the provided inputs. Always exercise caution when using predictions for decision-making.
""")

transaction_type = st.selectbox(
    "Transaction Type",
    options=list(transaction_mapping.keys()),
    help="Select the type of transaction"
)

amount = st.number_input(
    "Transaction Amount",
    min_value=0,
    step=1,
    help="Enter the transaction amount"
)

old_balance = st.number_input(
    "Old Balance (Origin)",
    min_value=0,
    step=1,
    help="Enter the account balance before the transaction"
)

new_balance = st.number_input(
    "New Balance (Origin)",
    min_value=0,
    step=1,
    help="Enter the account balance after the transaction"
)

if st.button("Check"):
    # Validate input values
    if amount <= 0 or old_balance < 0 or new_balance < 0:
        st.error("Please enter valid positive values for all amounts.")
    else:
        # Prepare input data
        transaction_type_encoded = transaction_mapping[transaction_type]
        input_data = pd.DataFrame(
            [[transaction_type_encoded, amount, old_balance, new_balance]],
            columns=loaded_features
        )
       
        st.write("Input Data Sent to Model: 📤")
        st.write(input_data)
        
        y_pred_prob = loaded_model.predict_proba(input_data)[0][1]  # Probability of fraud

        loaded_threshold = 0.5
        y_pred_custom = (y_pred_prob >= loaded_threshold).astype(float)

        predicted_label = label_mapping[y_pred_custom]

        st.subheader("Prediction Results")
        st.write(f"Probability of fraud: {y_pred_prob:.2f}") 
        st.write(f"Fraud Status: {predicted_label}")
