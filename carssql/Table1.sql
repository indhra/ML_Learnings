-- Create table1: customer_trips
CREATE TABLE customer_trips (
  customer_id INT,
  ticket_id INT,
  origin VARCHAR(50),
  destination VARCHAR(50),
  start_time DATETIME,
  end_time DATETIME
);

-- Create table2: flights
CREATE TABLE flights (
  flight_number VARCHAR(10),
  date DATE,
  origin VARCHAR(50),
  destination VARCHAR(50),
  start_time DATETIME,
  end_time DATETIME
);

-- Insert sample data into customer_trips table
INSERT INTO customer_trips (customer_id, ticket_id, origin, destination, start_time, end_time)
VALUES
  (1, 1, 'New York', 'Los Angeles', '2024-12-12 08:00:00', '2024-12-12 18:00:00'),
  (2, 2, 'Chicago', 'San Francisco', '2024-12-12 09:00:00', '2024-12-12 19:00:00');

-- Insert sample data into flights table
INSERT INTO flights (flight_number, date, origin, destination, start_time, end_time)
VALUES
  ('AA101', '2024-12-12', 'New York', 'Denver', '2024-12-12 08:00:00', '2024-12-12 10:00:00'),
  ('UA202', '2024-12-12', 'Denver', 'Los Angeles', '2024-12-12 11:00:00', '2024-12-12 13:00:00'),
  ('DL303', '2024-12-12', 'Chicago', 'Dallas', '2024-12-12 09:00:00', '2024-12-12 11:00:00'),
  ('UA404', '2024-12-12', 'Dallas', 'San Francisco', '2024-12-12 12:00:00', '2024-12-12 14:00:00');

-- Recursive CTE to retrieve flight sequence
WITH RECURSIVE flight_sequence AS (
  SELECT 
    ct.customer_id,
    ct.ticket_id,
    f.flight_number,
    f.origin,
    f.destination,
    f.start_time,
    f.end_time,
    1 AS level
  FROM 
    customer_trips ct
    INNER JOIN flights f ON ct.origin = f.origin AND ct.start_time = f.start_time
  WHERE 
    ct.customer_id = 1 AND ct.ticket_id = 1
  UNION ALL
  SELECT 
    fs.customer_id,
    fs.ticket_id,
    f.flight_number,
    f.origin,
    f.destination,
    f.start_time,
    f.end_time,
    fs.level + 1
  FROM 
    flight_sequence fs
    INNER JOIN flights f ON fs.destination = f.origin AND fs.end_time = f.start_time
)
SELECT 
  customer_id,
  ticket_id,
  flight_number,
  origin,
  destination,
  start_time,
  end_time
FROM 
  flight_sequence
ORDER BY 
  level;