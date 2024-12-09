CREATE TABLE finals AS
  SELECT "RSF" AS hall, "61A" as course UNION
  SELECT "Wheeler"    , "61A"           UNION
  SELECT "Pimentel"   , "61A"           UNION
  SELECT "Li Ka Shing", "61A"           UNION
  SELECT "Stanley"    , "61A"           UNION
  SELECT "RSF"        , "61B"           UNION
  SELECT "Wheeler"    , "61B"           UNION
  SELECT "Morgan"     , "61B"           UNION
  SELECT "Wheeler"    , "61C"           UNION
  SELECT "Pimentel"   , "61C"           UNION
  SELECT "Soda 310"   , "61C"           UNION
  SELECT "Soda 306"   , "10"            UNION
  SELECT "RSF"        , "70";

CREATE TABLE sizes AS
  SELECT "RSF" AS room, 900 as seats    UNION
  SELECT "Wheeler"    , 700             UNION
  SELECT "Pimentel"   , 500             UNION
  SELECT "Li Ka Shing", 300             UNION
  SELECT "Stanley"    , 300             UNION
  SELECT "Morgan"     , 100             UNION
  SELECT "Soda 306"   , 80              UNION
  SELECT "Soda 310"   , 40              UNION
  SELECT "Soda 320"   , 30;


CREATE TABLE sharing AS
  SELECT b.course , COUNT(DISTINCT b.hall) AS bob
  FROM finals AS a, finals AS b
  WHERE a.hall=b.hall and a.course != b.course  GROUP BY b.course;


-- CREATE TABLE sharing AS
--   SELECT a.course, COUNT(DISTINCT a.hall) AS shared
--   FROM finals AS a, finals AS b
--   WHERE a.hall=b.hall and a.course != b.course  GROUP BY a.course;


CREATE TABLE pairs AS
  SELECT a.room, b.room , a.seats+b.seats
  FROM  sizes AS a, sizes AS b WHERE a.room != b.room and (a.seats + b.seats)>=1000
  ORDER BY a.seats+b.seats DESC;
  -- SELECT a.room || "and" || "together have" || a.seats+b.seats || "seats" AS rooms
  -- FROM  sizes AS a, sizes AS b WHERE a.room != b.room and (a.seats + b.seats)>=1000
  -- ORDER BY a.seats+b.seats DESC;

CREATE TABLE big AS
  SELECT "REPLACE THIS LINE WITH YOUR SOLUTION";

CREATE TABLE remaining AS
  SELECT "REPLACE THIS LINE WITH YOUR SOLUTION";

