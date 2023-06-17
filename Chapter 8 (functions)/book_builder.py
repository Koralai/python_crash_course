def describe_book(title, author_first, author_last, **book_info):
    """
    Create a dictionary to store a book's title and author, plus
    any other info added during the function call.
    """
    book_info['title'] = title
    book_info['author_first_name'] = author_first
    book_info['author_last_name'] = author_last
    return book_info