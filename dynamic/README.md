### N<sup>th</sup> Fibonacci Number

As an introduction to dynamic programming a simple algorithm to calculate the n<sup>th</sup> number in the fibonacci sequence is used. This algorithm receives an integer &ge; 0 as input and returns the value of such index in the sequence.  

The general formula for calculating the n<sup>th</sup> number is:

  *F<sub>0</sub> = 0*  
  *F<sub>1</sub> = 1*  
  *F<sub>n &ge; 2</sub> = F<sub>n-1</sub> + F<sub>n-2</sub>*  
  
 #### Recursive approach
 This formula can later be translated as a recursive algorithm in pseudocode: 
  
```
Fibonacci(n):
  if n = 0  
    return 0  
  if n = 1  
    return 1  
  return Fibonacci(n-1) + Fibonacci(n-2)
  ```
This algorithm has a time complexity of *T(n) &le; O(1) + T(n-1) + T(n-2)*, which ultimately equals to *T(n) &le; T(n-1) + T(n-2)* and as we could have expected it is the very same fibonacci recursive formula. Since the fibonacci sequence's [growth rate](https://math.stackexchange.com/questions/2981007/is-the-fibonacci-sequence-exponential) has already been studied, we can use its exponential growth to summarized its time complexity, having then: 
  
*T(n) &ge; F<sub>n</sub>*, which translates to *&sim;O(&phi;<sup>n</sup>/&radic;5)*, an exponential time complexity. This recursive implementation can be found [here](https://github.com/Tortolala/Introduction-to-Graduate-Algorithms/blob/master/fibonacci/fibonacci_recursive.py).

#### Dynamic approach

The problem with the recursive approach can be well illustrated when we trace the recursion tree of the algorithm, since we would see that many identical subproblems are being calculated over and over again, making it inefficient.  

The dynamic approach solves this by implementing a lookup table that stores the results from subproblems *F(n-1)* and *F(n-2)*. This way we only calculate each subproblem once. The pseudocode of this algorithm looks like this:

```
Fibonacci(n):
  F = []
  F[0] = 0
  F[1] = 1
  
  for i=2 -> i=n:
    F[i] = F[i-1] + F[i-2]
    
  return F[n]
```

As seen, this approach uses the recursive nature of the fibonacci sequence, but it does not uses recursion at all. Instead of start solving the problem top-down as a recursive tree would do, it solves the subproblems ascendantly until it reaches the n<sup>th</sup> number.

This little but elegant shift in paradigm takes our previous exponential time complexity to a linear one created by the *for* loop. Having then: *O(n)*. Its python implementation can be found [here](https://github.com/Tortolala/Introduction-to-Graduate-Algorithms/blob/master/fibonacci/fibonacci_dynamic.py).
