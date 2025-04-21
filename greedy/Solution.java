class Solution {
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


    // 55
    public boolean canJump(int[] nums) {
        int i = 0;
        int cover = 0;
        while (i <= cover) {
            cover = Math.max(cover, i + nums[i]);
            if (cover >= nums.length - 1) return true;
            i++;
        }
        return false;
    }


    // 45
    public int jump(int[] nums) {
        int cur = 0;
        int next = 0;
        int result = 0;

        if (nums.length == 0) return 0;

        for (int i = 0; i < nums.length; i++) {
            next = Math.max(next, nums[i] + i);
            if (i == cur) {
                if (cur != nums.length - 1) {
                    cur = next;
                    result++;
                    if (cur >= nums.length) break;
                }
            }
        }

        return result;
    }

    // 1005
    public int largestSumAfterKNegations(int[] nums, int k) {
        Arrays.sort(nums);
        
        for (int i = 0; i < nums.length; i++) {
            if (nums[i] < 0 && k > 0) {
                nums[i] *= -1;
                k--;
            }
        }

        if (k % 2 == 1) {
            Arrays.sort(nums);
            nums[0] *= -1;
        }

        int sum = 0;
        for (int i = 0; i < nums.length; i++) {
            sum += nums[i];
        }
        return sum;
    }


    //  134
    public int canCompleteCircuit(int[] gas, int[] cost) {
        int len = gas.length;
        int curSum = 0;
        int start = 0;
        int totalSum = 0;

        for (int i = 0; i < len; i++) {
           curSum += gas[i] - cost[i];
            totalSum += gas[i] - cost[i];

            if (curSum < 0) {
                start = (i + 1) % len;
                curSum = 0;
            }
        }

        if (totalSum < 0) return -1;
        return start;
    }
}