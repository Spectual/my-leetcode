
class Solution {

    // 19
    public ListNode removeNthFromEnd(ListNode head, int n) {
        ListNode dummy = new ListNode(0, head);
        ListNode slow = dummy;
        ListNode fast = dummy.next;

        for (int i = 0; i < n; i++){
            fast = fast.next;
        }

        while (fast != null) {
            fast = fast.next;
            slow = slow.next;
        }

        slow.next = slow.next.next;

        return dummy.next;
    }

    // 24
    public ListNode swapPairs(ListNode head) {
        ListNode dummy = new ListNode(0, head);
        ListNode pre = dummy;
        ListNode cur = dummy;
        ListNode temp = dummy;

        while (pre.next != null && cur.next.next != null){
            pre = pre.next;
            cur.next = pre.next;
            cur = pre.next;
            temp = cur.next;
            cur.next = pre;
            pre.next = temp;
            cur = pre;
        }

        return dummy.next;
    }
    
    // 142
    public ListNode detectCycle(ListNode head) {
        ListNode fast = head;
        ListNode slow = head;

        while (fast != null && fast.next != null) {
            fast = fast.next.next;
            slow = slow.next;

            if (fast == slow) {
                slow = head;
                while (fast != slow) {
                    fast = fast.next;
                    slow = slow.next;
                }
                return fast;
            }
        }
        return null;
    }
    
    // 203
    public ListNode removeElements(ListNode head, int val) {
        ListNode dummyHead = new ListNode(0);
        dummyHead.next = head;
        ListNode temp = dummyHead;
        while (temp.next != null) {
            if (temp.next.val == val) {
                temp.next = temp.next.next;
            } else {
                temp = temp.next;
            }
        }
        return dummyHead.next;
    }

    // 206
    public ListNode reverseList(ListNode head) {
        ListNode cur = head;
        ListNode pre = null;
        ListNode temp = cur;
        while (temp != null) {
            temp = cur.next;
            cur.next = pre;
            pre = cur;
            cur = temp;
        }
        head = pre;

        return head;
    }   

    // 面试题 02.07. 链表相交
    public ListNode getIntersectionNode(ListNode headA, ListNode headB) {
        int sizeA = 0;
        int sizeB = 0;
        ListNode temp;

        temp = headA;
        while (temp != null) {
            temp = temp.next;
            sizeA++;
        }

        temp = headB;
        while (temp != null) {
            temp = temp.next;
            sizeB++;
        }

        ListNode nodeA = headA;
        ListNode nodeB = headB;

        int repSize = Math.min(sizeA, sizeB);
        for (int i = 0; i < sizeA - repSize; i++) {
            nodeA = nodeA.next;    
        }

        for (int i = 0; i < sizeB - repSize; i++) {
            nodeB = nodeB.next;    
        }
        
        while (nodeA != null && nodeB != null) {
            if (nodeA == nodeB) {
                return nodeA;
            }
            nodeA = nodeA.next;
            nodeB = nodeB.next;
        }

        return null;
    }



}