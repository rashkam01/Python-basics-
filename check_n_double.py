from typing import List

class Solution:
    def CheckIfExist(self, arr: List[int]) -> bool:
        for i in range(len(arr)):
            #print(f"Element at index {i}: {arr[i]}") 
            for j in range(len(arr)):
                if i!=j and arr[i] == 2* arr[j]:
                    return True
        return False

                
sol = Solution()

bo = sol.CheckIfExist([10,2,3,3])
print(bo)


# from typing import List

# class Solution:
#     def CheckIfExist(self, arr: List[int]) -> bool:
#         for i in range(len(arr)):
#             print(f"Element at index {i}: {arr[i]}")  # Print each element
#             for j in range(len(arr)):
#                 if i != j and arr[i] == 2 * arr[j]:  # Check that i != j and arr[i] == 2 * arr[j]
#                     return True
#         return False
                
# sol = Solution()

# # Corrected input
# bo = sol.CheckIfExist([10, 2, 5, 3])
# print("Result:", bo)  # Should print True