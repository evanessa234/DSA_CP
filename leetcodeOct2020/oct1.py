# You have a RecentCounter class which counts the number of recent requests within a certain time frame.

# Implement the RecentCounter class:

# RecentCounter() Initializes the counter with zero recent requests.
# int ping(int t) Adds a new request at time t, where t represents some time in milliseconds, and returns the number of requests that has happened in the past 3000 milliseconds (including the new request). Specifically, return the number of requests that have happened in the inclusive range [t - 3000, t].
# It is guaranteed that every call to ping uses a strictly larger value of t than the previous call.

 

# Example 1:

# Input
# ["RecentCounter", "ping", "ping", "ping", "ping"]
# [[], [1], [100], [3001], [3002]]
# Output
# [null, 1, 2, 3, 3]

# Explanation
# RecentCounter recentCounter = new RecentCounter();
# recentCounter.ping(1);     // requests = [1], range is [-2999,1], return 1
# recentCounter.ping(100);   // requests = [1, 100], range is [-2900,100], return 2
# recentCounter.ping(3001);  // requests = [1, 100, 3001], range is [1,3001], return 3
# recentCounter.ping(3002);  // requests = [1, 100, 3001, 3002], range is [2,3002], return 3
 

# Constraints:

# 1 <= t <= 104
# Each test case will call ping with strictly increasing values of t.
# At most 104 calls will be made to ping.


class RecentCounter:
   def __init__(self):
      self.request_count = []
    #   print("Hey1", self.request_count)
   def ping(self, t: int) -> int:
      self.request_count.append(t) 
      while len(self.request_count) and t - self.request_count[0] > 3000:
         self.request_count.pop(0)     
      return len(self.request_count)
ob = RecentCounter()
print(ob.ping(1))
print(ob.ping(100))
print(ob.ping(3001))
print(ob.ping(3002))

# Code to work upon
# class RecentCounter:
#     def __init__(self):
#         self.input_string1 = input("1")
#         self.input_string2 = input("2")
#         self.counter = 0
#         self.input_list = self.input_string2.strip("").split(",")
#     def ping(self, t):
#         counter = self.counter
#         self.t = t
#         print(self.input_list)
#         for i in self.input_list[1: len(self.input_list)]:
#             if int(i.strip("][ ")) in range(t-3000, t+1):
#                 counter += 1
#         return counter
# recentCounter = RecentCounter()

# print(recentCounter.ping(1))
# print(recentCounter.ping(100))
# print(recentCounter.ping(3001))
# print(recentCounter.ping(3002))