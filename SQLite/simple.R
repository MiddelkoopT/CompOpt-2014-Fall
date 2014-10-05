# Simple RSQlite.

print("simple.R>")

# install.packages("RSQLite")
# setwd("~/GitHub/CompOpt-2014-Fall/SQLite")

library(DBI)
library(RSQLite)

drv <- dbDriver("SQLite")
db <- dbConnect(drv, dbname="simple.db")

d <- dbGetQuery(db,"SELECT key,value FROM Data")

summary(d)
sum(d$value)

# close
sqliteCloseConnection(db)
sqliteCloseDriver(drv)
