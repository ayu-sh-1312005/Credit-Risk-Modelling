import joblib
import pandas as pd
import numpy as np

MODEL_PATH='artifacts/model_data.joblib'
model_data = joblib.load(MODEL_PATH)
model = model_data['model']
scaler=model_data['scaler']
features=model_data['features']
cols_to_scale=model_data['cols_to_scale']
def prepare_df(input_data):
    data = {
        'credit_utilization_ratio':input_data['credit_utilization_ratio'],
        'loan_tenure_months': input_data['loan_tenure_months'],
        'delinquency_ratio':round(input_data['delinquent_months']/input_data['loan_tenure_months'],2) if input_data['loan_tenure_months']>0 else 0,
         'loan_to_income':round(input_data['loan_amount']/input_data['income'],2) if input_data['income']>0 else 0,
         'avg_dpd_per_delinquency':round(input_data['total_dpd']/input_data['delinquent_months'],2) if input_data['delinquent_months']>0 else 0,
        'delinquent_months': input_data['delinquent_months'],
         'age':input_data['age'],
        'number_of_open_accounts':input_data['number_of_open_accounts'],
         'loan_purpose_Education':1 if input_data['loan_purpose']=='Education' else 0,
         'loan_purpose_Home':1 if input_data['loan_purpose']=='Home' else 0,
         'loan_purpose_Personal': 1 if input_data['loan_purpose']=='Personal' else 0,
        'residence_type_Owned':1 if input_data['residence_type']=='Owned' else 0,
         'residence_type_Rented':1 if input_data['residence_type']=='Rented' else 0,
         'loan_type_Unsecured': 1 if input_data['loan_type']=='Unsecured' else 0,
        # for scaler adding dummy values
        'gst': 0,
        'number_of_dependants': 0,
        'years_at_current_address': 0,
        'number_of_closed_accounts': 0,
        'enquiry_count': 0,
        'sanction_amount': 0,
        'processing_fee': 0,
        'net_disbursement': 0,
        'principal_outstanding': 0,
        'bank_balance_at_application': 0
    }
    df=pd.DataFrame([data])
    df[cols_to_scale]=scaler.transform(df[cols_to_scale])
    df=df[features]
    return df
def get_rating(credit_score):
    if credit_score<500:
        return 'Poor'
    elif credit_score<650:
        return 'Average'
    elif credit_score<750:
        return 'Good'
    elif credit_score<900:
        return 'Excellent'
    return None
def calculate_credit_score(df,base_score=300,scale_length=600):
    x=np.dot(df.values,model.coef_.T)+model.intercept_
    default_prob=1/(1+np.exp(-x))
    non_default_prob=1-default_prob
    credit_score=base_score+non_default_prob.flatten()*scale_length # high non-default prob -> credit score high
    rating=get_rating(credit_score[0])
    return default_prob[0][0],int(credit_score[0]),rating
def predict(input_data):
    df=prepare_df(input_data)
    probability, credit_score,rating=calculate_credit_score(df)
    return round(probability*100,2),credit_score,rating
