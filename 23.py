# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        dummy = ListNode()
        curr = dummy
        while True:
            are_all_nodes_expended = True
            minimum = float('inf')
            for node in lists:
                if node is None:
                    are_all_nodes_expended =  are_all_nodes_expended and True
                else:
                    are_all_nodes_expended = False
                    minimum = min(node.val, minimum)

            for i in range(len(lists)):
                node = lists[i]
                if node and node.val == minimum:
                    new_node = ListNode(node.val)
                    curr.next = new_node
                    curr = curr.next
                    lists[i] = node.next
                    
            if are_all_nodes_expended:
                break
        return dummy.next
