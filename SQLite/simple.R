# Simple RSQlite

# install.packages("RSQLite")
setwd("~/GitHub/CompOpt-2014-Fall/SQLite")

print("simple.R>")

library(DBI)
library(RSQLite)

drv <- dbDriver("SQLite")
db <- dbConnect(drv, dbname="simple.db")

d <- dbGetQuery(db,"SELECT key,value FROM Data")

d

rs <- sum(d$value)
rm <- mean(d$value)
rsd <- sd(d$value)

sql <- "INSERT INTO Results (experiment,result,value) VALUES (:e,:r,:v)"
dbGetPreparedQuery(db,sql,data.frame(e='all',r='sum',v=rs))

r <- dbGetQuery(db,"SELECT experiment,result,value FROM Results")
r

## Close
sqliteCloseConnection(db)
sqliteCloseDriver(drv)

print("simple.R> Done")
