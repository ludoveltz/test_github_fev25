class Pagination:
    def __init__(self, items=None, pageSize=10):
        # Initialize with empty list if no items provided
        self.items = items if items is not None else []
        # Convert pageSize to integer
        self.pageSize = int(pageSize)
        # Calculate total pages
        self.totalPages = max(1, (len(self.items) + self.pageSize - 1) // self.pageSize)
        # Start at first page
        self.currentPage = 1

    def getVisibleItems(self):
        """Returns the current page's items"""
        start = (self.currentPage - 1) * self.pageSize
        end = start + self.pageSize
        return self.items[start:end]

    def prevPage(self):
        """Go to previous page"""
        self.currentPage = max(1, self.currentPage - 1)
        return self

    def nextPage(self):
        """Go to next page"""
        self.currentPage = min(self.totalPages, self.currentPage + 1)
        return self

    def firstPage(self):
        """Go to first page"""
        self.currentPage = 1
        return self

    def lastPage(self):
        """Go to last page"""
        self.currentPage = self.totalPages
        return self

    def goToPage(self, pageNum):
        """Go to specific page"""
        # Convert pageNum to integer
        pageNum = int(pageNum)
        # Ensure page number is within valid range
        self.currentPage = max(1, min(self.totalPages, pageNum))
        return self

# Test the implementation
if __name__ == "__main__":
    # Test with alphabet list
    alphabetList = list("abcdefghijklmnopqrstuvwxyz")
    p = Pagination(alphabetList, 4)

    # Test 1: Initial page
    print("Initial page:", p.getVisibleItems())

    # Test 2: Next page
    p.nextPage()
    print("After nextPage:", p.getVisibleItems())

    # Test 3: Last page
    p.lastPage()
    print("After lastPage:", p.getVisibleItems())

    # Test 4: Previous page
    p.prevPage()
    print("After prevPage:", p.getVisibleItems())

    # Test 5: First page
    p.firstPage()
    print("After firstPage:", p.getVisibleItems())

    # Test 6: Go to specific page
    p.goToPage(4)
    print("After goToPage(4):", p.getVisibleItems())

    # Test 7: Chain methods
    print("After chaining methods:",
          p.firstPage().nextPage().nextPage().getVisibleItems())

    # Test 8: Try to go to invalid page
    p.goToPage(10)
    print("After trying to go to page 10:", p.getVisibleItems())