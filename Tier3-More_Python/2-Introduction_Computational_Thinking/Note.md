## Unit 3
### 7-Inferential Statistics

#### Law of large numbers:
In repeated independant test with a probability P of a particular outcome, the fraction of time this event will occur converge to p as the number of trial goes to infinity

#### Regression to the Mean
Following an extrem event is likely to be less extreme

#### Formulas
variance(X) = sum for each eleemnt x in X of (x - mean)**2/len(X)
standard deviation (**sigma**)(X) = sqrt(variance(X)) == **ecart type**

#### Empirical Rule
* 68% within one std dev of the mean
* 95% within 2 (or more precisely 1.96)
* 99.7 within 3

Assumption :
* mean estimation error = 0
* The distribution of the error is normal

#### Defining Distributions
**histogram**: Depiction of the frequency of a distribution
**Probability Distribution**: Discrete or continuous.

#### Central Limit theorem
Given a sufficiently large
1. The means of the samples in a set of samples will be approximately normally
distributed, independently of the distribution of the population.
2. This normal distribution will have a mean close to the mean of the population.
3. The variance of the sample means will be close to the variance of the population divided
by the size of the sample.

#### Standard Error of the Mean
SE = stdDev / sqrt(n)
with n the size of the sample

## Unit 4
### 10- Experimental Data Part

#### Mean Square Error

#### Coefficient of determination (**R²**)
R² = 1 - (sum of the (yi - pi)²)/(sum of the (yi - mean)²)
where yi = Measured value
      pi = Predicted value
Compare the estimation errors(numerator) with the variability of the orginal value (denominator). A good way to measure the absolute goodness of a fit.

#### Cross validation
