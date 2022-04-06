# Blog Post 4

## Project gets proprietary from this point on

### But here is a General Idea of what I did

I will continue with the "Quick and Dirty" Dataset form this point on for the sake of this project. I will not being including code from here on out as I have not had the chance to code this out for python

Next Course of Action is to then find the range of Premiums that you could play that would maintain a High Percent return while staying far enough away from the Current price to get initial investment back.

So to do this with the "Quick & Dirty" dataset, I would recommend to use a NEAT algorithm.

A [N.E.A.T.](https://neat-python.readthedocs.io/en/latest/) algorithm is also known as Neuro-Evolution of Augmentating Topologies, with is a form of a  Genetic Neural Network.

*In the Properitary side of the project I had access to tools that allowed me to use a Genetic Neural Network, which took about 2 & 1/2 weeks to get trained for multiple models. The reaseon it took so long is because I used a Machine Learning - Random Forest Classifier, to verify if the Genetic Neural Network was moving in a positive direction as a Fitness Function for classifying the Options data.*

## What to do next is to to Back Test the Algorithm.

With the tools I had access too while working on this project, it was really simple to back test it and verify how well the Neat Algorithm did in predicting the Stirke Price with the highest Percent return while minimizing the chances of the options geting "Exercised".

## Verify the Probabilties

Next I used once again one of the tools that I was provided that would give me the distributions of the likeley hood of the Underslying stock rising from its current price to a Strike Price.

Using this to Verify what I was getting from the GANN with what I was getting from the Distributions.

## Answers I got

The GANN Performed Very Admirably it would get about a 7% return per option play, and maintained an average of 1 in 20 probability of the Option being Exercised.

## How well the GANN Did over the course of a Year versuses 10 years?

The GANN could only use a max of $10,000 to play with for every  Option Play.
And there is a max of 150 times in a year that it can be done.

### 1 Year
The GANN averaged about $700 per Option Play
After playing 20 times it would make about ~ $12,000 to $14,000, then it would lose $10,000 becaue the option was excercised. Which would mean that it would make about $2,000 - $4,000 every 20 periods.

150 periods / 20 periods = 7.5 times
7.5 times X $2,000 - $4,000 = $15,000 - $30,000 per year

#### What actually happend?
The GANN actually made $24,691 over the course of the year.

### 10 Years
predicted to make between $150,000 - $300,000.
Actually made $175,222 over 10 years.

### Thoughts about what can be changed
If I had to do this differently I would remove using Fridays from number of times that we can do this in the year.
If I dropped using Fridays, then my chances of getting your Option exercised goes from 1 in 20 to about 1 in 33 and my average Percent return drops to 6.45%.

#### Predicted amount made in year with Changes
1 period = $645
$645 X 33 periods = $21,285 for every 33 periods
$21,285 - $10,000 = $11,285 made every 33 periods

104 periods / 33 periods = 3.15 times
$11,285 X 3.15 times ~ $35,550 in 1 year
