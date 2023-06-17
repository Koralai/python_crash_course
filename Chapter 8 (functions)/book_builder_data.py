from book_builder import describe_book

book_1 = describe_book(
            'brotherhood',
            'mike',
            'chen',
            year_published=2022,
            pages=352,
            series='star wars',
            number_in_series=9,
            amazon_rating=4.6,
)

print(book_1)