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


    // 101 Symmetric Tree
    public boolean compare(TreeNode left, TreeNode right) {
        if (left == null && right != null) return false;
        else if (left != null && right == null) return false;
        else if (left == null && right == null) return true;
        else if (left.val != right.val) return false;

        boolean outside = compare(left.left, right.right);
        boolean inside = compare(left.right, right.left);
        boolean result = outside && inside;
        return result;
    }
    public boolean isSymmetric(TreeNode root) {
        boolean result = compare(root.left, root.right);
        return result;
    }


    // 104 Maximum Depth of Binary Tree
    public int maxDepth(TreeNode root) {
        if (root == null) return 0;
        int left = maxDepth(root.left);
        int right = maxDepth(root.right);
        return Math.max(left, right) + 1;
    }

    // 111 Minimum Depth of Binary Tree
    public int minDepth(TreeNode root) {
        if (root == null) return 0;
        int left = minDepth(root.left);
        int right = minDepth(root.right);

        if (root.left != null && root.right == null) return 1 + left;
        if (root.left == null && root.right != null) return 1 + right;

        return Math.min(left, right) + 1;
    }


    // 222 Count Complete Tree Nodes
    public int countNodes(TreeNode root) {
        if (root == null) return 0;
        int left = countNodes(root.left);
        int right = countNodes(root.right);
        return left + right + 1;
    }


    // 110 Balanced Binary tree
    public int getHeight(TreeNode root) {
        if (root == null) return 0;

        int left = getHeight(root.left);
        if (left == -1) return -1;
        int right = getHeight(root.right);
        if (right == -1) return -1;
        return Math.abs(left - right) > 1 ? -1 : Math.max(left, right) + 1;
    }

    public boolean isBalanced(TreeNode root) {
        return getHeight(root) == -1 ? false: true;
    }


    // 404 Sum of Left Leaves
    public int sumOfLeftLeaves(TreeNode root) {
        if (root == null) return 0;
        int val = 0;
        if (root.left != null && root.left.left == null && root.left.right == null) val = root.left.val;
        int left = sumOfLeftLeaves(root.left);
        int right = sumOfLeftLeaves(root.right);
        return left + right + val;
    }


    // 700 Search in a Binary Search Tree
    public TreeNode searchBST(TreeNode root, int val) {
        if (root == null || root.val == val) return root;

        TreeNode result = null;
        if (root.val > val) result = searchBST(root.left, val);
        if (root.val < val) result = searchBST(root.right, val);
        return result;
    }


    // 98 Validate Binary Search Tree
    List<Integer> vec = new ArrayList<>();
    void traversal(TreeNode root) {
        if (root == null) return;
        traversal(root.left);
        vec.add(root.val);
        traversal(root.right);
    }
    public boolean isValidBST(TreeNode root) {
        traversal(root);
        for (int i = 1; i < vec.size(); i++) {
            if (vec.get(i) <= vec.get(i-1)) return false;
        }
        return true;
    }


    // 530 Minimum Absolute Difference in BST
    TreeNode pre = null;
    int result = Integer.MAX_VALUE;
    public void traversal(TreeNode root) {
        if (root == null) return;
        traversal(root.left);
        if (pre != null) result = Math.min(result, root.val - pre.val);
        pre = root;
        traversal(root.right);
    }
    public int getMinimumDifference(TreeNode root) {
        traversal(root);
        return result;
    }


    // 501 Find Mode in Binary Search Tree
    int maxCount = 0;
    int count = 0;
    TreeNode pre = null;
    List<Integer> resList =  new ArrayList<>();
    public void traversal(TreeNode root) {
        if (root == null) return;

        traversal(root.left);
        if (pre == null || root.val != pre.val) count = 1;
        if (pre != null && root.val == pre.val) count++;

        if (count >= maxCount) {
            if (count > maxCount) {
                resList.clear();
            }
            maxCount = count;
            resList.add(root.val);
        }
        pre = root;
        traversal(root.right);
    }
    public int[] findMode(TreeNode root) {
        traversal(root);
        int[] res = new int[resList.size()];
        for (int i = 0; i < resList.size(); i++) {
            res[i] = resList.get(i);
        }
        return res;
    }

    // 236 Lowest Common Ancestor of a Binary Tree
    public TreeNode lowestCommonAncestor(TreeNode root, TreeNode p, TreeNode q) {
        if (root == null || root == p || root == q) return root;
        TreeNode left = lowestCommonAncestor(root.left, p, q);
        TreeNode right = lowestCommonAncestor(root.right, p, q);

        if (left == p && right == q || left == q && right == p) return root;
        if (left != null && right == null) return left;
        else if (right != null && left == null) return right;
        return null;
    }


    // 235 Lowest Common Ancestor of a Binary Search Tree
    public TreeNode lowestCommonAncestor(TreeNode root, TreeNode p, TreeNode q) {
        if (root == null || root.val <= p.val && root.val >= q.val ||root.val <= q.val && root.val >= p.val) return root;
        TreeNode left = lowestCommonAncestor(root.left, p, q);
        TreeNode right = lowestCommonAncestor(root.right, p, q);
        
        if (left != null) return left;
        else if (right != null) return right;
        return null;
    }


    // 701 Insert into a Binary Search Tree
    public TreeNode insertIntoBST(TreeNode root, int val) {
        if (root == null) {
            return new TreeNode(val);
        }

        if (root.val < val) root.right = insertIntoBST(root.right, val);
        if (root.val > val) root.left = insertIntoBST(root.left, val);

        return root;
    }


    // 450 Delete Node in a BST
    public TreeNode deleteNode(TreeNode root, int key) {
        if (root == null) return root;

        if (root.val == key) {
            if (root.left == null) {
                return root.right;
            }
            else if (root.right == null) {
                return root.left;
            }
            else {
                TreeNode cur = root.right;
                while(cur.left != null) {
                    cur = cur.left;
                }
                cur.left = root.left;
                root = root.right;
                return root;
            }
        }

        if (root.val < key) root.right = deleteNode(root.right, key);
        if (root.val > key) root.left = deleteNode(root.left, key);
        return root;
    }


    // 100 Tree Node
    public boolean isSameTree(TreeNode p, TreeNode q) {
        if (p == null && q == null) {
            return true;
        }        
        else if (p == null || q == null) {
            return false;
        }

        boolean left = isSameTree(p.left, q.left);
        boolean right = isSameTree(p.right, q.right);

        return left && right && (p.val == q.val);
    }


    // 112 Path Sum
    public boolean hasPathSum(TreeNode root, int targetSum) {
        if (root == null) return false;
        if (root.val == targetSum && root.left == null && root.right == null) return true;

        targetSum -= root.val;
        boolean left = hasPathSum(root.left, targetSum);
        boolean right = hasPathSum(root.right, targetSum);
        return left || right;
    }
}