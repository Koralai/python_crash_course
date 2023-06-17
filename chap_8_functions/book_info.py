def describe_book(title, author_first, author_last, **book_info):
    """
    Create a dictionary to store a book's title and author, plus
    any other info added during the function call.
    """
    book_info['title'] = title
    book_info['author_first_name'] = author_first
    book_info['author_last_name'] = author_last
    return book_info
    
book_1 = describe_book(
            'pride and prejudice',
            'jane',
            'austen',
            author_living=False,
            genre=['romance', 'satire'],
            words=122_189,
            main_characters=['elizabeth bennett', 'fitzwilliam darcy']
    )

print(book_1)