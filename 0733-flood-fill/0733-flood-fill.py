class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        crr = image[sr][sc]
        if crr == color:
            return image

        directions = [(-1,0), (1,0), (0,-1), (0,1)]

        rows = len(image)
        cols = len(image[0])

        def dfs(sr, sc):

            image[sr][sc] = color

            for dr, dc in directions:

                nr = sr + dr
                nc = sc + dc

                if 0 <= nr < rows and 0 <= nc < cols:
                    if image[nr][nc] == crr:
                        dfs(nr, nc)

        dfs(sr, sc)

        return image