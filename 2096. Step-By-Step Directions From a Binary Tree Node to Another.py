class Solution:
    
    def getDirections(self, root: Optional[TreeNode], startValue: int, destValue: int) -> str:
        
        final_paths = [[], []]

        def path_to_node(root, cur_path, direction):
            nonlocal final_paths, startValue, destValue
            
            if not root:
                return
        
            cur_path.append(direction)
            
            if root.val == startValue:
                final_paths[0] = cur_path.copy()
            
            if root.val == destValue:
                final_paths[1] = cur_path.copy()
            
            path_to_node(root.left, cur_path, 'L')
            path_to_node(root.right, cur_path, 'R')
            
            cur_path.pop(-1)
        
        path_to_node(root, [], 'S')

        start_path = final_paths[0]
        dest_path = final_paths[1]

        while len(start_path) > 0 and len(dest_path) > 0:
                
            if start_path[0] != dest_path[0]:
                break
            
            start_path.pop(0)
            dest_path.pop(0)
        
        return 'U'*len(start_path) + ''.join(dest_path)
