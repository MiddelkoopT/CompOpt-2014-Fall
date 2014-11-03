# Simple experiments (NSF dataset)

# setwd("~/GitHub/CompOpt-2014-Fall/SQLite")

library(DBI)
library(RSQLite)
drv <- dbDriver("SQLite")

db <- dbConnect(drv, dbname = "experiment-1-NSF.sqlite")

e <- dbGetQuery(db,"SELECT eid, problem, threads, chunks FROM Experiments")
hist(e$threads)
factor(d$problem)

r <- dbGetQuery(db,"SELECT eid, strftime('%s',stop)-strftime('%s',start) AS wtime FROM Runs")

hist(r$wtime)

u <- dbGetQuery(db,"SELECT run, iterations, steps, time FROM Results")
u
plot(u$time)

d <- dbGetQuery(db,"SELECT run,problem,iterations,time, strftime('%s',stop)-strftime('%s',start) AS wtime 
                FROM Experiments JOIN Runs USING(eid) JOIN Results USING (run)")
d
plot(time~wtime,d)
m <- lm(time~wtime,d)
summary(m)

dg <- dbGetQuery(db,"SELECT problem,AVG(iterations) AS iter,AVG(time) as time 
                FROM Experiments JOIN Runs USING(eid) JOIN Results USING (run)
                GROUP BY problem")

d$wtime-d$time/1000000
