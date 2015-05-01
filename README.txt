
# Anchor Loans Test

The proplem solution using **knapsack problem**

But first, I've calculated the total of each combination for each coins as following:

```python
from itertools import *

coins = [1, 5, 7, 9, 11]


def combination(items):
    return ( set(compress(items,mask)) \
        for mask in product(*[[0,1]]*len(items)) )


def determineCoins():
    for x in combination(coins):
        print x
```

So, I found 32 possible combination given the list of coins

```python
list(combination(range(len(coins))))

[set(),
 {4},
 {3},
 {3, 4},
 {2},
 {2, 4},
 {2, 3},
 {2, 3, 4},
 {1},
 {1, 4},
 {1, 3},
 {1, 3, 4},
 {1, 2},
 {1, 2, 4},
 {1, 2, 3},
 {1, 2, 3, 4},
 {0},
 {0, 4},
 {0, 3},
 {0, 3, 4},
 {0, 2},
 {0, 2, 4},
 {0, 2, 3},
 {0, 2, 3, 4},
 {0, 1},
 {0, 1, 4},
 {0, 1, 3},
 {0, 1, 3, 4},
 {0, 1, 2},
 {0, 1, 2, 4},
 {0, 1, 2, 3},
 {0, 1, 2, 3, 4}]

 ```

With the list o all possible combination, I added each of then

```python
map(sum,list(combination(coins)))
[0,
 11,
 9,
 20,
 7,
 18,
 16,
 27,
 5,
 16,
 14,
 25,
 12,
 23,
 21,
 32,
 1,
 12,
 10,
 21,
 8,
 19,
 17,
 28,
 6,
 17,
 15,
 26,
 13,
 24,
 22,
 33]
 ```

 So if the sum is 23 in the 14th position I have [1,2,4] which is [5,7,11].
 That was my solution withou the **knapsack problem**.

 But, in terms of computional thinking, I suppose that the use of **knapsack problem** was the best aproach. In the general this problem is NP-Complete, I choose use it as recursive function and memoization (see *views.py*).
