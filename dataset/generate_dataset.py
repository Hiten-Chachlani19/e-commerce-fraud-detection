import pandas as pd
import numpy as np

def generate_ecom_fraud_data(n_samples=2000, random_state=42):
    np.random.seed(random_state)
    
    # Feature Engineering for Credit Card / E-commerce Fraud
    transaction_amount = np.round(np.random.exponential(scale=120, size=n_samples) + 5, 2)
    transaction_hour = np.random.randint(0, 24, size=n_samples)
    distance_from_home_km = np.round(np.random.exponential(scale=15, size=n_samples) + 0.5, 2)
    failed_login_attempts = np.random.choice([0, 1, 2, 3, 4], size=n_samples, p=[0.75, 0.15, 0.06, 0.03, 0.01])
    is_foreign_ip = np.random.choice([0, 1], size=n_samples, p=[0.88, 0.12])
    is_high_risk_country = np.random.choice([0, 1], size=n_samples, p=[0.92, 0.08])
    shipping_billing_address_match = np.random.choice([1, 0], size=n_samples, p=[0.85, 0.15])
    device_type = np.random.choice([0, 1, 2], size=n_samples, p=[0.55, 0.35, 0.10]) # 0: Mobile, 1: Desktop, 2: Tablet
    
    # Fraud Risk Logic Score
    risk_score = (
        (transaction_amount > 400).astype(int) * 2.5 +
        (is_foreign_ip == 1).astype(int) * 3.0 +
        (shipping_billing_address_match == 0).astype(int) * 2.0 +
        (failed_login_attempts >= 2).astype(int) * 2.0 +
        (is_high_risk_country == 1).astype(int) * 3.5 +
        ((transaction_hour < 4) | (transaction_hour > 23)).astype(int) * 1.5 +
        (distance_from_home_km > 50).astype(int) * 1.5
    )
    
    # Calculate probability and target class (0: Legitimate, 1: Fraudulent)
    fraud_prob = 1 / (1 + np.exp(-(risk_score - 5.5)))
    is_fraud = (np.random.rand(n_samples) < fraud_prob).astype(int)
    
    df = pd.DataFrame({
        'transaction_amount': transaction_amount,
        'transaction_hour': transaction_hour,
        'distance_from_home_km': distance_from_home_km,
        'failed_login_attempts': failed_login_attempts,
        'is_foreign_ip': is_foreign_ip,
        'is_high_risk_country': is_high_risk_country,
        'shipping_billing_address_match': shipping_billing_address_match,
        'device_type': device_type,
        'is_fraud': is_fraud
    })
    
    return df

if __name__ == "__main__":
    df = generate_ecom_fraud_data(3000)
    df.to_csv('fraud_dataset.csv', index=False)
    print("✅ Dataset successfully generated: fraud_dataset.csv")
    print(f"Total Records: {len(df)} | Fraud Cases: {df['is_fraud'].sum()} ({round(df['is_fraud'].mean()*100, 2)}%)")