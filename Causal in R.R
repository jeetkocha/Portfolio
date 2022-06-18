rhc = read.csv("data/rhc.csv", header = TRUE, sep = ",")
head(rhc)


xvars <- c("ARF", "CHF", "Cirr", "colcan", "Coma", "lungcan",
           "MOSF", "sepsis", "age", "female")



library(tableone)
table1 <- CreateTableOne(vars = xvars, strata = "treatment", data = rhc)
# including standardized mean difference (SMD)
print(table1, smd = TRUE)

library(cobalt)
bal.tab(treatment ~ ARF + CHF + Cirr + colcan + Coma + lungcan +
          MOSF + sepsis + age + female, data = rhc, estimand = "ATE")



# full matching
library(MatchIt)
m.out <- matchit(treatment ~ ARF + CHF + Cirr + colcan + Coma + lungcan +
                   MOSF + sepsis + age + female, data = rhc,
                 method = "full", estimand = "ATE") # it may take time..
print(summary(m.out, standardize = TRUE))

# vweight 
library(WeightIt)
w.out <- weightit(treatment ~ ARF + CHF + Cirr + colcan + Coma + lungcan +
                    MOSF + sepsis + age + female, data = rhc, estimand = "ATE")
summary(w.out)



bal.tab(m.out, stats = "m", thresholds = c(m = 0.1))
love.plot(m.out, binary = "std", thresholds = c(m = 0.1))

bal.tab(w.out, stats = "m", thresholds = c(m = 0.1))
love.plot(w.out, binary = "std", thresholds = c(m = 0.1))


fit.m <- glm(died ~ treatment +ARF + CHF + Cirr + colcan + Coma + lungcan +
               MOSF + sepsis + age + female,
             data = match.data(m.out), family = binomial())
summary(fit.m)
confint(fit.m)[2,]

library(survey)
design.w <- svydesign(~1, weights = w.out$weights, data = rhc)
fit.w <- svyglm(died ~ treatment +ARF + CHF + Cirr + colcan + Coma + lungcan +
                  MOSF + sepsis + age + female,
                design = design.w, family = binomial())
## the target estimand w.out was ATE
confint(fit.w)[2,]

