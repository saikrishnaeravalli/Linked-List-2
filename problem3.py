# Time Complexity : O(1)
# Space Complexity : O(1)
# Did this code successfully run on Leetcode :
# Any problem you faced while coding this : No


# Your code here along with comments explaining your approach

class Solution:
    #Function to delete a node without any reference to head pointer.
    def deleteNode(self,curr_node):
        #code here
        curr_node.data = curr_node.next.data
        curr_node.next = curr_node.next.next