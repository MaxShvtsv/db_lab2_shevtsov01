CREATE TABLE connections (
  id 	   INT  NOT NULL,
  blue	   BOOL NOT NULL,
  dual_sim BOOL NOT NULL,
  four_g   BOOL NOT NULL
);

CREATE TABLE dimensions (
  id        INT   NOT NULL,
  m_dep 	FLOAT NOT NULL,
  mobile_wt INT   NOT NULL
);

CREATE TABLE camera (
  id INT NOT NULL,
  fc INT NOT NULL
);

CREATE TABLE features (
  id            INT   NOT NULL,
  battery_power INT   NOT NULL,
  clock_speed   FLOAT NOT NULL,
  int_memory    INT   NOT NULL
);

ALTER TABLE connections ADD PRIMARY KEY (id);

ALTER TABLE dimensions ADD CONSTRAINT FK_dimensions_connections FOREIGN KEY (id) REFERENCES connections (id);
ALTER TABLE camera ADD CONSTRAINT FK_camera_connections FOREIGN KEY (id) REFERENCES connections (id);
ALTER TABLE features ADD CONSTRAINT FK_features_connections FOREIGN KEY (id) REFERENCES connections (id);