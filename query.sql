-- SELECT phone_id, label, int_memory
-- FROM phones

-- SELECT customers.country, COUNT(*) AS phone_count
-- FROM customers, phones
-- WHERE customers.phone_id = phones.phone_id
-- GROUP BY customers.country

-- SELECT phones.phone_id, phones.label, customers.cust_name, customers.age
-- FROM phones, customers
-- WHERE customers.phone_id = phones.phone_id AND customers.age > 20