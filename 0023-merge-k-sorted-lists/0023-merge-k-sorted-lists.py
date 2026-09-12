# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return None
            
        dummy = ListNode()
        current = dummy 
        k = len(lists)
        while True :
            smallest = -1
            for i in range(k):
                if lists[i]:
                    if smallest == -1 or lists[i].val < lists[smallest].val:
                        smallest = i
            if smallest == -1:
                break

            current.next = lists[smallest]
            lists[smallest] = lists[smallest].next
            current = current.next
        return dummy.next
        

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna