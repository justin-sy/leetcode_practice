from collections import defaultdict
# Hashmap used to solve problem
class Solution:
    def findCommonResponse(self, responses: List[List[str]]) -> str:
        Hashmap = defaultdict(int) # Hashmap to store responses
        res = [0,""] # Store most common response
        for day in responses: # Iteratre through responses
            for answer in set(day): # Iteratrate through the responses of  each day
                Hashmap[answer] += 1 # Increment the count of each response by one in Hashmap
                if Hashmap[answer] > res[0] or Hashmap[answer] == res[0] and answer < res[1]: # Check if lexographically smaller or more common than most common
                    res = [Hashmap[answer],answer] # Replace if so
        return res[1] # Return most common response
