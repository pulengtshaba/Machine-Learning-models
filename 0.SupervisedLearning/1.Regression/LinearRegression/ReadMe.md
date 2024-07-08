# MultipleLR

There are multiple features or independent variables (R&D Spend,
Administration, Marketing Spend, State). Again, the goal here is to reveal or discover a relationship between the independent variables and the target (Profit).

Also notice that under the column ‘State’, the data is in text (not numbers). You’ll see New York, California, and Florida instead of numbers. How do you deal with this kind of data?
One convenient way to do that is by transforming categorical data (New York, California, Florida) into numerical data.

we have the following data with categorical variables: 3.5, New
York 2.0, California 6.7, Florida If we use dummy variables, the above data will be transformed into this: 
3.5, 1, 0, 0
2.0, 0, 1, 0
6.7, 0, 0, 1

## Backward Elimination

Is that all there is? Are all the variables (R&D Spend, Administration, Marketing Spend, State) responsible for the target (Profit). 

Many data analysts perform additional steps to create better models and predictors. They might be doing Backward Elimination (e.g. eliminating variables one by one until there’s one or two left) so we’ll know which of the variables is making the biggest
contribution to our results (and therefore more accurate predictions). 
