# Data Preprocessing Template

# Importing the dataset
dataset = read.csv('Data.csv')

# taking care of missing values
dataset$Age = ifelse(is.na(dataset$Age), 
                     ave(dataset$Age, FUN = function(x) mean(x, na.rm = TRUE)), 
                     dataset$Age
                     )

dataset$Salary = ifelse(is.na(dataset$Salary), 
                        ave(dataset$Salary, FUN= function(x) mean(x, na.rm = TRUE)),
                        dataset$Salary)

# Encoding categorial value
dataset$Country = factor(dataset$Country, levels = c('France', 'Spain', 'Germany'), labels = c(1,2,3))

dataset$Purchased = factor(dataset$Purchased, levels = c('No', 'Yes'), labels = c(0,1))

# splitting the data
#install.packages('caTools')

library(caTools)
set.seed(123)
split = sample.split(dataset$Purchased, SplitRatio =  0.8)
train_data = subset(dataset , split== TRUE)
test_data = subset(dataset, split == FALSE)

# Feature Scaling
train_data[,2:3] = scale(train_data[,2:3])
test_data[,2:3] = scale(test_data[,2:3])

