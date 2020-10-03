# Given an array of distinct integers candidates and a target integer target, return a list of all unique combinations of candidates where the chosen numbers sum to target. You may return the combinations in any order.

# The same number may be chosen from candidates an unlimited number of times. Two combinations are unique if the frequency of at least one of the chosen numbers is different.

# It is guaranteed that the number of unique combinations that sum up to target is less than 150 combinations for the given input.

 

# Example 1:

# Input: candidates = [2,3,6,7], target = 7
# Output: [[2,2,3],[7]]
# Explanation:
# 2 and 3 are candidates, and 2 + 2 + 3 = 7. Note that 2 can be used multiple times.
# 7 is a candidate, and 7 = 7.
# These are the only two combinations.

class Solution(object):
   def combinationSum(self, candidates, target):
      result = []
      unique={}
      candidates = list(set(candidates))
      self.solve(candidates,target,result,unique)
      return result
   def solve(self,candidates,target,result,unique,i = 0,current=[]):
      if target == 0:
         temp = [i for i in current]
         temp1 = temp
         temp.sort()
         temp = tuple(temp)
         if temp not in unique:
            unique[temp] = 1
            result.append(temp1)
         return
      if target <0:
         return
      for x in range(i,len(candidates)):
         current.append(candidates[x])
         self.solve(candidates,target-candidates[x],result,unique,i,current)
         current.pop(len(current)-1)

        #  add another code too
        