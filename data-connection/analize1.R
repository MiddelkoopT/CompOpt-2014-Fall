# Analize CSV file example Copyright 2014 by Timothy Middelkoop License CC by SA


d <- read.csv('dataset1-convert.csv',header=TRUE)
names(d)
length(d)
n <- nrow(d) ; n
plot(x2~x1,d)
