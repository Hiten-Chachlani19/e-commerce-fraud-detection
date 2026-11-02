document.getElementById('fraudForm').addEventListener('submit', async function(e) {
    e.preventDefault();
    
    const payload = {
        transaction_amount: document.getElementById('transaction_amount').value,
        transaction_hour: document.getElementById('transaction_hour').value,
        distance_from_home_km: document.getElementById('distance_from_home_km').value,
        failed_login_attempts: document.getElementById('failed_login_attempts').value,
        is_foreign_ip: document.getElementById('is_foreign_ip').value,
        is_high_risk_country: document.getElementById('is_high_risk_country').value,
        shipping_billing_address_match: document.getElementById('shipping_billing_address_match').value,
        device_type: document.getElementById('device_type').value
    };

    const btnSubmit = document.getElementById('btnSubmit');
    btnSubmit.innerText = "Analyzing...";
    btnSubmit.disabled = true;

    try {
        const response = await fetch('http://127.0.0.1:5000/predict', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(payload)
        });

        const data = await response.json();
        
        const resultCard = document.getElementById('resultCard');
        const statusBadge = document.getElementById('statusBadge');
        const riskScore = document.getElementById('riskScore');

        resultCard.classList.remove('hidden');
        statusBadge.innerText = data.status;
        riskScore.innerText = `${data.fraud_probability}%`;

        if(data.is_fraud === 1) {
            statusBadge.className = "badge fraud";
        } else {
            statusBadge.className = "badge safe";
        }

    } catch (err) {
        alert("Error connecting to backend API!");
    } finally {
        btnSubmit.innerText = "Analyze Transaction";
        btnSubmit.disabled = false;
    }
});