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


    // 225 Implement Stack using Queues
    Queue<Integer> que1;
    Queue<Integer> que2;
    public MyStack() {
        que1 = new LinkedList<>();
        que2 = new LinkedList<>();
    }
    
    public void push(int x) {
        que2.offer(x);
        while(!que1.isEmpty()) {
            que2.offer(que1.poll());
        }
        Queue<Integer> tmp = que1;
        que1 = que2;
        que2 = tmp;
    }
    
    public int pop() {
        return que1.poll();
    }
    
    public int top() {
        return que1.peek();
    }
    
    public boolean empty() {
        return que1.isEmpty();
    }


    // 20 Valid Parentheses
    public boolean isValid(String s) {
        Stack<Character> stack = new Stack<>();

        for (int i = 0; i < s.length(); i++) {
            char c = s.charAt(i);
            if (c == '(') {
                stack.push(')');
            }
            else if (c == '{') {
                stack.push('}');
            }
            else if (c == '[') {
                stack.push(']');
            }
            else if (stack.isEmpty()) {
                return false;
            }
            else if (c == stack.peek()) {
                stack.pop();
            }
            else return false;
        }
        return stack.isEmpty();
    }
}