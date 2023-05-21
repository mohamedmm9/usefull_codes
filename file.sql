%%sql 
postgresql:///lending

SELECT
  client.client_id,
  client.date_of_birth,
  client.employment_status,
  client.country,
  repayment.repayment_amount,
  CASE
    WHEN repayment_amount > 4000 THEN 'bank account'
    ELSE 'mail'
  END AS repayment_channel
FROM client, repayment
WHERE repayment_channel LIKE '-';
