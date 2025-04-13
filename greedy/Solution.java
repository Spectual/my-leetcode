class Solution:
    // 455
    public int findContentChildren(int[] g, int[] s) {
        Arrays.sort(g);
        Arrays.sort(s);
        int start = 0;
        int count = 0;
        for (int i = 0; i < s.length && start < g.length; i++) {
            if (s[i] >= g[start]) {
                start++;
                count++;
            }
        }
        return count;
    }


    // 53
    public int maxSubArray(int[] nums) {
        int result = Integer.MIN_VALUE;
        int count = 0;
        for (int i = 0; i < nums.length; i++) {
            count += nums[i];
            if (count > result) result = count;
            if (count < 0) count = 0;
        }
        return result;
    }


    // 122
    public int maxProfit(int[] prices) {
        int result = 0;
        int cur = 0;
        for (int i = 1; i < prices.length; i++) {
            cur = prices[i] - prices[i-1];
            if (cur > 0) result += cur;
        }
        return result;
    }