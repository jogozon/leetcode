# 0022-generate-parentheses
Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

 

Example 1:

Input: n = 3
Output: ["((()))","(()())","(())()","()(())","()()()"]
Example 2:

Input: n = 1
Output: ["()"]

---

notes: 
- DFS is usually used when memory is limited and shortest path isn't necessary / all options need to be checked (backtracking) while BFS is when memory isn't a constraint and the optimal path is wanted
- when an exhaustive adjective like 'generate all' is used then most likely a backtracking solution would need to be used
- backtracking can be pretty runtime intensive as it tends to scale very poorly

---

runtime: two branching factors so the runtime is O(2^n)
memory: O(n) b/c of the sizes of the two stacks