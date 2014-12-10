DROP TABLE IF EXISTS Experiments;
CREATE TABLE Experiments (
  EID INTEGER PRIMARY KEY,
  alpha DOUBLE,
  beta DOUBLE,
  epsilon DOUBLE
);

INSERT INTO Experiments (EID,alpha,beta,epsilon) VALUES (1,3,6,0.2);
INSERT INTO Experiments (EID,alpha,beta,epsilon) VALUES (2,3,9,0.2), (4,6,4,0.1);
    
DROP TABLE IF EXISTS RUNS;
CREATE TABLE Runs (
  EID INTEGER,
  RUNID INTEGER PRIMARY KEY,
  solution DOUBLE,
  start DATETIME,
  finish DATETIME
);

INSERT INTO Runs (EID,RUNID) VALUES (1,1),(1,2),(1,3),(2,4),(2,5),(2,6);

SELECT * FROM Experiments JOIN Runs USING (EID);