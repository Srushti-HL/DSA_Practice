class Solution:
    def nodesBetweenCriticalPoints(self, head):
        prev = head
        curr = head.next
        pos = 1

        first = -1
        prev_cp = -1

        min_dist = float('inf')
        max_dist = -1

        while curr.next:
            next_node = curr.next

            # Check if current node is a critical point
            if ((curr.val > prev.val and curr.val > next_node.val) or
                (curr.val < prev.val and curr.val < next_node.val)):

                # First critical point
                if first == -1:
                    first = pos

                # If this is not the first critical point
                if prev_cp != -1:
                    min_dist = min(min_dist, pos - prev_cp)

                # Distance from first critical point
                max_dist = pos - first

                prev_cp = pos

            prev = curr
            curr = next_node
            pos += 1

        # Fewer than two critical points
        if min_dist == float('inf'):
            return [-1, -1]

        return [min_dist, max_dist]