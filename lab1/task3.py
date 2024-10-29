# TODO Найдите количество книг, которое можно разместить на дискете

diskette_size_mb = 1.44
pages = 100
lines_per_pages = 50
chars_per_line = 25
bytes_per_char = 4

diskette_size_bytes = diskette_size_mb * 1024 * 1024

book_size_bytes = pages * lines_per_pages * chars_per_line * bytes_per_char

numbers_of_books = diskette_size_bytes // book_size_bytes

print("Количество книг, помещающихся на дискету:", int(numbers_of_books))
