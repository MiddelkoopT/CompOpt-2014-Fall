# Simple experiments (NSF dataset)

# setwd("~/GitHub/CompOpt-2014-Fall/SQLite")

library(DBI)
library(RSQLite)
drv <- dbDriver("SQLite")

db <- dbConnect(drv, dbname = "experiment-1-NSF.sqlite")

d <- dbGetQuery(db,"SELECT eid, strftime('%s',stop)-strftime('%s',start) AS wtime FROM Runs")
d
d <- dbGetQuery(db,"SELECT eid, problem, threads, chunks FROM Experiments")

## Combined
d <- dbGetQuery(db,"
  SELCT run
                
                
                ")
