class MyQueue {
    // 232 Implement Queue using Stacks
    Stack<Integer> stack;
    Stack<Integer> tmp;

    public MyQueue() {
        stack = new Stack<>();
        tmp = new Stack<>();
    }
    
    public void push(int x) {
        tmp.push(x);
    }
    
    public int pop() {
        if (!stack.isEmpty()) {
            return stack.pop();
        }
        else{
            while(!tmp.isEmpty()) {
                int i = tmp.pop();
                stack.push(i);
            }
            return stack.pop();
        }
    }
    
    public int peek() {        
        if (!stack.isEmpty()) {
            return stack.peek();
        }
        else{
            while(!tmp.isEmpty()) {
                int i = tmp.pop();
                stack.push(i);
            }
            return stack.peek();
        }
    }
    
    public boolean empty() {      
        return tmp.isEmpty() && stack.isEmpty();
    }
}