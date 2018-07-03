class ListNode(object):
    """docstring for ListNode"""
    def __init__(self, x):
        self.val = x
        self.next = None

def ReverseLinkedList(head):
    pre = None
    while head:
        cur = head
        head = head.next
        cur.next = pre
        pre = cur
    return pre

def hasCycle(head):
    '''
    一个快节点，每次走两格
    一个慢节点，每次走一格
    '''
    try:
        slow = head
        fast = head.next
        while slow is not fast:
            slow = slow.next
            fast = fast.next.next
        return True
    except:
        return False

def printListFromTailToHead(ListNode):
    result = []
    while ListNode:
        result.insert(0, ListNode.val)
        ListNode = ListNode.next
    return result




