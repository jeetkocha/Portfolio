install.packages("CausalImpact") 

# Calling the package 
library(CausalImpact)

# Creating example data set 
set.seed(1)
x1 <- 100 + arima.sim(model = list(ar = 0.999), n = 100)
y <- 1.2 * x1 + rnorm(100)
y[71:100] <- y[71:100] + 10
data <- cbind(y, x1)

dim(data)

head(data)

# We can now visualize this data 

matplot(data, type = "l")

# Running an analysis 

pre.period <- c(1, 70)
post.period <- c(71, 100)


# To perform inference, Let's run the anaysis using:

impact <- CausalImpact(data, pre.period, post.period)

# Let's plot the results 
plot(impact)

# Working the dates and times 
time.points <- seq.Date(as.Date("2014-01-01"), by = 1, length.out = 100)
data <- zoo(cbind(y, x1), time.points)
head(data)


# We can now specify pre-period and the post-period in terms of time points rather than indices:

pre.period <- as.Date(c("2014-01-01", "2014-03-11"))
post.period <- as.Date(c("2014-03-12", "2014-04-10"))

impact <- CausalImpact(data, pre.period, post.period)
plot(impact)


summary(impact, "report")







