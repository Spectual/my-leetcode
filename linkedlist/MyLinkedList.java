// 707
class MyLinkedList {
    ListNode head;
    int size;

    public MyLinkedList() {
        this.head = new ListNode(-1, null);
        this.size = 0;
    }
    
    public int get(int index) {
        ListNode temp = head;

        if (index < 0 || index >= size) {
            return -1;
        }

        for (int i = -1; i < index; i++) {
            temp = temp.next;
        }
        return temp.val;
    }
    
    public void addAtHead(int val) {
        addAtIndex(0, val);
    }
    
    public void addAtTail(int val) {
        addAtIndex(size, val);
    }
    
    public void addAtIndex(int index, int val) {
        ListNode node = new ListNode(val);
        ListNode temp = head;

        if (index < 0 || index > size) {
            return; 
        }

        for (int i = -1; i < index - 1; i++) {
            temp = temp.next;
        }
        node.next = temp.next;
        temp.next = node;
        size++;
    }
    
    public void deleteAtIndex(int index) {
        ListNode temp = head;

        if (index < 0 || index >= size) {
            return;
        }

        for (int i = -1; i < index - 1; i++) {
            temp = temp.next;
        }

        temp.next = temp.next.next;
        size--;
    }
}

/**
 * Your MyLinkedList object will be instantiated and called as such:
 * MyLinkedList obj = new MyLinkedList();
 * int param_1 = obj.get(index);
 * obj.addAtHead(val);
 * obj.addAtTail(val);
 * obj.addAtIndex(index,val);
 * obj.deleteAtIndex(index);
 */