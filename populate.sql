INSERT INTO phones(phone_id, label, battery_power, clock_speed, int_memory, m_dep, mobile_wt, camera_focus, blue, dual_sim, four_g)
VALUES (1, 'IPhone', 1043, 1.8, 5, 0.1, 193, 14, TRUE, TRUE, FALSE),
	   (2, 'Huawei', 841, 0.5, 61, 0.8, 191, 4, TRUE, TRUE, TRUE),
	   (3, 'Samsung', 1807, 2.8, 27, 0.9, 186, 1, TRUE, FALSE, FALSE),
	   (4, 'Nokia', 1546, 0.5, 25, 0.5, 96, 18, FALSE, TRUE, TRUE),
	   (5, 'Xiaomi', 1434, 1.4, 49, 0.5, 108, 11, FALSE, FALSE, TRUE);

INSERT INTO customers(cust_id, phone_id, cust_name, age, country)
VALUES (1, 5, 'Alice', 18, 'USA'),
	   (2, 3, 'Bob', 30, 'England'),
	   (3, 1, 'Annie', 40, 'Germany'),
	   (4, 2, 'Marta', 70, 'Spain'),
	   (5, 4, 'Mike', 15, 'USA');