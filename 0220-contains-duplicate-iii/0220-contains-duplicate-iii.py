class Solution:
    def containsNearbyAlmostDuplicate(self, nums, indexDiff, valueDiff):

        if valueDiff < 0:
            return False

        buckets = {}
        size = valueDiff + 1

        def get_bucket(num):
            return num // size

        for i, num in enumerate(nums):

            bucket_id = get_bucket(num)

            # Same bucket
            if bucket_id in buckets:
                return True

            # Left bucket
            if (bucket_id - 1 in buckets and
                    abs(num - buckets[bucket_id - 1]) <= valueDiff):
                return True

            # Right bucket
            if (bucket_id + 1 in buckets and
                    abs(num - buckets[bucket_id + 1]) <= valueDiff):
                return True

            buckets[bucket_id] = num

            # Maintain sliding window
            if i >= indexDiff:
                old_bucket = get_bucket(nums[i - indexDiff])
                del buckets[old_bucket]

        return False