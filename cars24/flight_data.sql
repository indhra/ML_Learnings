
-- Create table1: cust_data
CREATE TABLE cust_data (
  cust_id VARCHAR(4),
  ticket_id INT,
  first_cust_port VARCHAR(50),
  last_cust_port VARCHAR(50),
  cust_start INT,
  cust_end INT
);

-- Create table2: flight_data
CREATE TABLE flight_data (
  flight_no VARCHAR(3),
  date DATE,
  orig_port VARCHAR(50),
  dest_port VARCHAR(50),
  flight_start INT,
  flight_end INT
);

-- Insert sample data into cust_data table
INSERT INTO cust_data (cust_id, ticket_id, first_cust_port, last_cust_port, cust_start, cust_end)
VALUES
    ('A123', 9342312, 'Delhi', 'Mumbai', 815, 1730),
    ('A456', 6542312, 'Delhi', 'Mumbai', 830, 1015),
    ('A789', 7542312, 'Delhi', 'Mumbai', 845, 1330);

-- Insert sample data into flight_data table
INSERT INTO flight_data (flight_no, date, orig_port, dest_port, flight_start, flight_end)
VALUES
    ('B99', '2014-04-04', 'Delhi', 'Mumbai', 830, 1015),
    ('B89', '2014-04-04', 'Delhi', 'Jaipur', 845, 1045),
     ('B669', '2014-04-04', 'Jaipur', 'Tirupati', 1030, 1330),
    ('B69', '2014-04-04', 'Jaipur', 'Mumbai', 1130, 1330),
    ('B79', '2014-04-04', 'Delhi', 'Agra', 815, 1130),
    ('B59', '2014-04-04', 'Agra', 'Surat', 1230, 1430),
    ('B49', '2014-04-04', 'Surat', 'Pune', 1445, 1530),
    ('B39', '2014-04-04', 'Pune', 'Mumbai', 1615, 1730);

-- Recursive CTE to find the flight path
WITH RECURSIVE FlightPath AS (
    -- Base case: Select the initial flight for the given customer and ticket
    SELECT 
        f.flight_no,
        f.date,
        f.orig_port,
        f.dest_port,
        f.flight_start,
        f.flight_end,
        1 AS leg
    FROM 
        flight_data f
    JOIN 
        cust_data c ON f.orig_port = c.first_cust_port
    WHERE 
        c.cust_id = 'A123' AND c.ticket_id = 9342312 AND c.cust_start=f.flight_start
    
    UNION ALL
    
    -- Recursive case: Find the next connecting flight
    SELECT 
        f.flight_no,
        f.date,
        f.orig_port,
        f.dest_port,
        f.flight_start,
        f.flight_end,
        fp.leg + 1 AS leg
    
    FROM 
        flight_data f
    INNER JOIN 
        FlightPath fp ON f.orig_port = fp.dest_port 
    WHERE 
       f.flight_start > fp.flight_end
)
SELECT 
    flight_no,
    date,
    orig_port,
    dest_port,
    flight_start,
    flight_end,
    leg
FROM 
    FlightPath
ORDER BY 
    leg;