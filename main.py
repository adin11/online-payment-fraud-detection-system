import streamlit as st
import pandas as pd
import joblib
import streamlit as st
from datetime import time, datetime

@st.cache_resource
def load_model():
    model_data = joblib.load('fraud_detection_model.pkl')
    return model_data

st.set_page_config(page_icon='🛡️',page_title='Fraud Shield')

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

st.markdown("<h1 style='white-space: nowrap;'>🛡️ Fraud Shield</h1>", unsafe_allow_html=True)
st.subheader(" Your Online Payment Fraud Detection System")
st.info("Enter the transaction details below to get accurate probability of a transaction being Fradulent ")

with st.expander("🚨ALERT"):
    st.warning("""
Fraud risk scores are estimates only. Cross-check suspicious activity before taking action. No tool is foolproof—this fraud detector may miss threats or flag legitimate transactions as Fraudulent.
""")
    
hour = st.selectbox("Transaction Time (24 hour format)", list(range(0, 24)),help='Enter the transaction time in hours')

transaction_type = st.selectbox(
    "Transaction Type",
    options=list(transaction_mapping.keys()),
    help="Select the type of transaction"
)

amount = st.number_input(
    "Transaction Amount",
    min_value=0,
    step=1000,
    help="Enter the transaction amount"
)

old_balance = st.number_input(
    "Old Balance (Origin)",
    min_value=0,
    step=1000,
    help="Account balance of the sender before the transaction"
)

new_balance = st.number_input(
    "New Balance (Origin)",
    min_value=0,
    step=1000,
    help="Account balance of the sender after the transaction"
)

if st.button("Check"):
    # Validate input values
    if amount <= 0 or old_balance < 0 or new_balance < 0:
        st.error("Please enter valid positive values for all amounts.")
    else:
        # Prepare input data
        transaction_type_encoded = transaction_mapping[transaction_type]
        input_data = pd.DataFrame(
            [[hour,transaction_type_encoded, amount, old_balance, new_balance]],
            columns=loaded_features
        )
       
        st.write("Input Data Sent to Model: 📤")
        st.write(input_data)
        
        y_pred_prob = loaded_model.predict_proba(input_data)[0][1] # Probability of fraud

        loaded_threshold = 0.5
        y_pred_custom = (y_pred_prob >= loaded_threshold).astype(float)

        predicted_label = label_mapping[y_pred_custom]

        st.subheader("Prediction Results")
        st.write(f"Probability of fraud: {y_pred_prob:.2f}") 
        st.write(f"Fraud Status: {predicted_label}")


# Hamburger Icon
st.markdown("""
<style>
/* Target the header button using its data-testid */
[data-testid="baseButton-headerNoPadding"] {
    background: none; /* Remove default background */
    border: none; /* Remove border */
    cursor: pointer; /* Change cursor to pointer */
}

/* Replace the SVG with a hamburger icon */
[data-testid="baseButton-headerNoPadding"] svg {
    display: none; /* Hide the default SVG */
}

[data-testid="baseButton-headerNoPadding"]::before {
    content: '\\2630'; /* Unicode for hamburger icon */
    font-size: 24px; /* Adjust icon size */
    color: currentColor; /* Inherit color for consistency */
    display: block;
}
</style>
""", unsafe_allow_html=True)


# Footer
st.markdown("---")
st.markdown("""
<div style='text-align: center;'>
    <h4>A Project by ~ Adin Raja ✌️</h4>
    <p>
        <a href='https://github.com/adin11' target='_blank'>GitHub</a> | 
        <a href='https://www.linkedin.com/in/adin-raja-492a78194/' target='_blank'>LinkedIn</a> | 
        <a href='mailto:adinraja78@gmail.com'>Email</a>
    </p>
    <small>© 2025 Adin Raja. All rights reserved.</small>
</div>
""", unsafe_allow_html=True)

# Optional Sidebar for About Section
with st.sidebar:
    
    with st.sidebar:
     st.markdown("### About This App") 

    st.info(
        """
        This app can help banks, digital wallets or payment platforms to automatically flag suspicious transactions, helping to prevent financial loss, alert fraud detection teams.\n
        **Made by ~ Adin Raja**
        """ 
    )
    st.markdown("### 📬 Contact") 
    st.write("""
    - ✉️ Email: [adinraja78@gmail.com](mailto:your_email@example.com)
    - 💼 [LinkedIn](https://www.linkedin.com/in/adin-raja-492a78194/)
    - 🖥️ [GitHub](https://github.com/adin11)
    """)