SELECT
    transaction_id,
    user_id,
    amount,
    location,
    device,
    timestamp,
    CASE WHEN amount > 500 THEN 1 ELSE 0 END AS is_fraud
FROM raw.transactions
