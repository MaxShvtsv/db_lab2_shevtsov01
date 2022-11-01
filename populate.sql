INSERT INTO connections(id, blue, dual_sim, four_g)
VALUES (1, TRUE, TRUE, FALSE),
	   (2, TRUE, TRUE, TRUE),
	   (3, TRUE, FALSE, FALSE),
	   (4, FALSE, TRUE, TRUE),
	   (5, FALSE, FALSE, TRUE);

INSERT INTO features(id, battery_power, clock_speed, int_memory)
VALUES (1, 1043, 1.8, 5),
	   (2, 841, 0.5, 61),
	   (3, 1807, 2.8, 27),
	   (4, 1546, 0.5, 25),
	   (5, 1434, 1.4, 49);

INSERT INTO dimensions(id, m_dep, mobile_wt)
VALUES (1, 0.1, 193),
	   (2, 0.8, 191),
	   (3, 0.9, 186),
	   (4, 0.5, 96),
	   (5, 0.5, 108);

INSERT INTO camera(id, fc)
VALUES (1, 14),
	   (2, 4),
	   (3, 1),
	   (4, 18),
	   (5, 11);