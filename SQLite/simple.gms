SETS
       I   canning plants   / SEATTLE, SAN-DIEGO /
       J   markets          / NEW-YORK, CHICAGO, TOPEKA / ;
  PARAMETERS
       A(I)  capacity of plant i in cases
         /    SEATTLE     350
              SAN-DIEGO   600  /
       B(J)  demand at market j in cases
         /    NEW-YORK    325
              CHICAGO     300
              TOPEKA      275  / ;
  TABLE D(I,J)  distance in thousands of miles
                    NEW-YORK       CHICAGO      TOPEKA
      SEATTLE          2.5           1.7          1.8
      SAN-DIEGO        2.5           1.8          1.4  ;
  SCALAR F  freight in dollars per case per thousand miles  /90/ ;
  PARAMETER C(I,J)  transport cost in thousands of dollars per case ;
            C(I,J) = F * D(I,J) / 1000 ;
  VARIABLES
       X(I,J)  shipment quantities in cases
       Z       total transportation costs in thousands of dollars ;
  POSITIVE VARIABLE X ;
  EQUATIONS
       COST        define objective function
       SUPPLY(I)   observe supply limit at plant i
       DEMAND(J)   satisfy demand at market j ;
  COST ..        Z  =E=  SUM((I,J), C(I,J)*X(I,J)) ;
  SUPPLY(I) ..   SUM(J, X(I,J))  =L=  A(I) ;
  DEMAND(J) ..   SUM(I, X(I,J))  =G=  B(J) ;
  MODEL TRANSPORT /ALL/ ;
  SOLVE TRANSPORT USING LP MINIMIZING Z ;
  