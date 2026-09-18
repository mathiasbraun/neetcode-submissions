class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        return self.paint(image, sr, sc, image[sr][sc], color, set())

    def paint(self, image: List[List[int]], sr: int, sc: int, anchor: int, color: int, visit) -> List[List[int]]:
        rows, cols = len(image), len(image[0])
        
        if (min(sr, sc) < 0                 # do not leave image left or top
            or sr == rows or sc == cols     # do not leave image bottom or right
            or (sr, sc) in visit):          # node already visited
                return image
        if image[sr][sc] != anchor:
            return image
        else:
            image[sr][sc] = color

        visit.add((sr, sc))
        image = self.paint(image, sr + 1, sc, anchor, color, visit)
        image = self.paint(image, sr, sc + 1, anchor, color, visit)
        image = self.paint(image, sr - 1, sc, anchor, color, visit)      
        image = self.paint(image, sr, sc - 1, anchor, color, visit)
        visit.remove((sr, sc))

        return image