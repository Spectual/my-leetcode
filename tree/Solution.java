class Solution {

    // 94 DFS
    public List<Integer> inorderTraversal(TreeNode root) {
        List<Integer> res= new ArrayList<>();
        inorder(root, res);
        return res;
    }

    public List<Integer> inorder(TreeNode root, List<integer> list) {
        if (root == null) return null;
        inorder(root.left, list);
        list.add(root.val);
        inorder(root.right, list);
        return list;
    }


    // 102 BFS
    public List<List<Integer>> resList = new ArrayList<List<Integer>>();

    public List<List<Integer>> levelOrder(TreeNode root) {
        order(root);
        return resList;    
    }

    public void order(TreeNode root) {
        if (root == null) return;
        
        Queue<TreeNode> que = new LinkedList<TreeNode>();
        que.offer(root);

        while(!que.isEmpty()) {
            List<Integer> itemList = new ArrayList<Integer>();
            int len = que.size();

            while(len > 0) {
                TreeNode item = que.poll();
                if (item.left != null) que.offer(item.left);
                if (item.right != null) que.offer(item.right);
                itemList.add(item.val);
                len--;
            }

            resList.add(itemList);
        }
    }


    // 199 Binary Tree Right Side View(BFS)
    public List<Integer> rightSideView(TreeNode root) {
        List<Integer> result = new ArrayList<>();
        Queue<TreeNode> que = new LinkedList<>();

        if (root == null) return result;

        que.offer(root);

        while(!que.isEmpty()) {
            int size = que.size();
            for (int i = 0; i < size; i++) {
                TreeNode temp = que.poll();
                if (temp.left != null) que.offer(temp.left);
                if (temp.right != null) que.offer(temp.right);
                if (i == size - 1) result.add(temp.val);
            }
        }
        
        return result;
    }


    // 116 Populating Next Right Pointers in Each Node(BFS)
    public Node connect(Node root) {
        Queue<Node> que = new LinkedList<>();
        if (root != null) que.offer(root);

        while(!que.isEmpty()) {
            int levelSize = que.size();
            for (int i = 0; i < levelSize; i++) {
                Node poll = que.poll();
                Node next = que.peek();
                if (poll.left != null) que.offer(poll.left);
                if (poll.right != null) que.offer(poll.right);
                poll.next = i == levelSize - 1 ? null : next;
            }
        }

        return root;
    }


    // 226 Invert Binary Tree
    public TreeNode invertTree(TreeNode root) {
        if (root == null) return null;

        TreeNode temp;
        temp = root.left;
        root.left = root.right;
        root.right = temp;
        invertTree(root.left);
        invertTree(root.right);

        return root;
    }
}