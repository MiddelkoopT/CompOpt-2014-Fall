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

sum(d$value)
mean(d$value)
sd(d$value)



## Close
sqliteCloseConnection(db)
sqliteCloseDriver(drv)

print("simple.R> Done")
