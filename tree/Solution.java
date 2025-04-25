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
}