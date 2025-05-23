// DFS used to solve problem 1038 in Javascript
/**
 * Definition for a binary tree node.
 * function TreeNode(val, left, right) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.left = (left===undefined ? null : left)
 *     this.right = (right===undefined ? null : right)
 * }
 */
/**
 * @param {TreeNode} root
 * @return {TreeNode}
 */
var bstToGst = function(root) {
    function dfs(node,total){
        if (node.right){
            total = dfs(node.right,total);
        };
        total += node.val;
        node.val = total;
        if (node.left){
            total = dfs(node.left,total)
        };
        return total;
    };
    dfs(root,0);
    return root;
};
