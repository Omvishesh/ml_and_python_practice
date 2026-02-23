class Book:
    
    def __init__(self, title, author, reviews):
        self.title = title
        self.author = author
        self.review = reviews
        
    def add_review(self, review):
        self.review.append(review)
        print("review appended")
    
    def count_reviews(self):
        count_review = 0
        for i in self.review:
            count_review += 1   
        print(f"count = {count_review}")
        
    def display_all_reviews(self):
        for n in self.review:
            print(n)

book1 = Book("programming with Python", "om", ["good book"])
book1.add_review("book needs a more detail view on OOPs")
book1.count_reviews()
book1.display_all_reviews()