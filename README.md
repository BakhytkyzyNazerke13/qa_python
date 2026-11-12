# Проект: Юнит-тестирование BooksCollector

Реализованные тесты:
1. `test_add_new_book_add_one_book` — параметризованный тест добавления книги.
2. `test_add_new_book_name_too_long` — проверка ограничения на длину имени книги (>40 символов).
3. `test_add_new_book_duplicate` — проверка, что одну книгу нельзя добавить дважды.
4. `test_set_book_genre` — параметризованный тест установки жанра.
5. `test_get_book_genre` — проверка получения жанра по имени книги.
6. `test_get_books_with_specific_genre` — проверка получения списка книг по жанру.
7. `test_get_books_genre` — проверка получения всего словаря книг.
8. `test_get_books_for_children` — проверка фильтрации книг без возрастного рейтинга.
9. `test_add_book_in_favorites` — проверка добавления книги в избранное.
10. `test_add_book_in_favorites_not_in_dict` — проверка, что книгу без жанра нельзя добавить в избранное.
11. `test_delete_book_from_favorites` — проверка удаления книги из избранного.
12. `test_get_list_of_favorites_books` — проверка получения списка избранных книг.