134. Gas Station
Solved
Medium
Topics
premium lock icon
Companies
There are n gas stations along a circular route, where the amount of gas at the ith station is gas[i].

You have a car with an unlimited gas tank and it costs cost[i] of gas to travel from the ith station to its next (i + 1)th station. You begin the journey with an empty tank at one of the gas stations.

Given two integer arrays gas and cost, return the starting gas station's index if you can travel around the circuit once in the clockwise direction, otherwise return -1. If there exists a solution, it is guaranteed to be unique.

 

Example 1:

Input: gas = [1,2,3,4,5], cost = [3,4,5,1,2]
Output: 3
Explanation:
Start at station 3 (index 3) and fill up with 4 unit of gas. Your tank = 0 + 4 = 4
Travel to station 4. Your tank = 4 - 1 + 5 = 8
Travel to station 0. Your tank = 8 - 2 + 1 = 7
Travel to station 1. Your tank = 7 - 3 + 2 = 6
Travel to station 2. Your tank = 6 - 4 + 3 = 5
Travel to station 3. The cost is 5. Your gas is just enough to travel back to station 3.
Therefore, return 3 as the starting index.
Example 2:

Input: gas = [2,3,4], cost = [3,4,3]
Output: -1
Explanation:
You can't start at station 0 or 1, as there is not enough gas to travel to the next station.
Let's start at station 2 and fill up with 4 unit of gas. Your tank = 0 + 4 = 4
Travel to station 0. Your tank = 4 - 3 + 2 = 3
Travel to station 1. Your tank = 3 - 3 + 3 = 3
You cannot travel back to station 2, as it requires 4 unit of gas but you only have 3.
Therefore, you can't travel around the circuit once no matter where you start.
 

Constraints:

n == gas.length == cost.length
1 <= n <= 105
0 <= gas[i], cost[i] <= 104
The input is generated such that the answer is unique.



#### Key Ideas

- If sum of gas < the sum of cost, then it's impossible
- Find the diff btwn corresponding cost and gas values
- Keep adding the diff[i] value to total
- When total < 0, update index to i+1 and set total to 0

```bash

You keep track of your current gas tank level. As you move from one station to the next, your tank changes by gas[i] - cost[i].

Now, imagine that while driving from station i to i + 1, your tank drops below zero. This means you are stranded. What can we conclude from this?

You definitely cannot start at station i.

More importantly, you also cannot start at any of the stations you have already passed (from your last starting point up to i). Why? Because if you had started at any of those earlier stations, you would have had less gas in your tank when you reached station i, and you would have still gotten stranded.

Therefore, if you get stuck when traveling from station i to i+1, none of the stations from your starting point up to i can be the answer. The next possible valid starting point must be i + 1.
```
