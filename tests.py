import pytest
from main import BooksCollector


class TestBooksCollector:

    # ТЕСТ 1: Параметризованный тест на добавление одной книги
    @pytest.mark.parametrize('book_name', [
        'Гарри Поттер',
        'Война и мир',
        'Дюна'
    ])
    def test_add_new_book_add_one_book(self, book_name):
        collector = BooksCollector()
        collector.add_new_book(book_name)
        assert book_name in collector.get_books_genre()
        assert collector.get_books_genre()[book_name] == ''

    # ТЕСТ 2: Книгу с именем длиннее 40 символов добавить нельзя
    def test_add_new_book_name_too_long(self):
        collector = BooksCollector()
        long_name = 'А' * 41
        collector.add_new_book(long_name)
        assert long_name not in collector.get_books_genre()

    # ТЕСТ 3: Одну и ту же книгу нельзя добавить дважды
    def test_add_new_book_duplicate(self):
        collector = BooksCollector()
        collector.add_new_book('Мастер и Маргарита')
        collector.add_new_book('Мастер и Маргарита')
        assert len(collector.get_books_genre()) == 1

    # ТЕСТ 4: Установить жанр книги (параметризованный)
    @pytest.mark.parametrize('genre', [
        'Фантастика',
        'Ужасы',
        'Детективы',
        'Мультфильмы',
        'Комедии'
    ])
    def test_set_book_genre(self, genre):
        collector = BooksCollector()
        collector.add_new_book('Три мушкетёра')
        collector.set_book_genre('Три мушкетёра', genre)
        assert collector.get_books_genre()['Три мушкетёра'] == genre

    # ТЕСТ 5: Получить жанр книги по имени
    def test_get_book_genre(self):
        collector = BooksCollector()
        collector.add_new_book('Властелин колец')
        collector.set_book_genre('Властелин колец', 'Фантастика')
        assert collector.get_book_genre('Властелин колец') == 'Фантастика'

    # ТЕСТ 6: Получить список книг с определённым жанром
    def test_get_books_with_specific_genre(self):
        collector = BooksCollector()
        collector.add_new_book('Книга 1')
        collector.set_book_genre('Книга 1', 'Ужасы')
        collector.add_new_book('Книга 2')
        collector.set_book_genre('Книга 2', 'Ужасы')
        collector.add_new_book('Книга 3')
        collector.set_book_genre('Книга 3', 'Комедии')
        
        result = collector.get_books_with_specific_genre('Ужасы')
        assert 'Книга 1' in result
        assert 'Книга 2' in result
        assert 'Книга 3' not in result

    # ТЕСТ 7: Получить весь словарь книг и жанров
    def test_get_books_genre(self):
        collector = BooksCollector()
        collector.add_new_book('Книга А')
        collector.add_new_book('Книга Б')
        result = collector.get_books_genre()
        assert len(result) == 2
        assert 'Книга А' in result
        assert 'Книга Б' in result

    # ТЕСТ 8: Получить книги для детей (без возрастного рейтинга)
    def test_get_books_for_children(self):
        collector = BooksCollector()
        collector.add_new_book('Сказка')
        collector.set_book_genre('Сказка', 'Мультфильмы')
        
        collector.add_new_book('Страшилка')
        collector.set_book_genre('Страшилка', 'Ужасы')
        
        result = collector.get_books_for_children()
        assert 'Сказка' in result
        assert 'Страшилка' not in result

    # ТЕСТ 9: Добавить книгу в избранное
    def test_add_book_in_favorites(self):
        collector = BooksCollector()
        collector.add_new_book('Любимая книга')
        collector.add_book_in_favorites('Любимая книга')
        assert 'Любимая книга' in collector.get_list_of_favorites_books()

    # ТЕСТ 10: Нельзя добавить в избранное книгу, которой нет в словаре
    def test_add_book_in_favorites_not_in_dict(self):
        collector = BooksCollector()
        collector.add_book_in_favorites('Неизвестная книга')
        assert 'Неизвестная книга' not in collector.get_list_of_favorites_books()

    # ТЕСТ 11: Удалить книгу из избранного
    def test_delete_book_from_favorites(self):
        collector = BooksCollector()
        collector.add_new_book('Книга для удаления')
        collector.add_book_in_favorites('Книга для удаления')
        collector.delete_book_from_favorites('Книга для удаления')
        assert 'Книга для удаления' not in collector.get_list_of_favorites_books()

    # ТЕСТ 12: Получить список избранных книг
    def test_get_list_of_favorites_books(self):
        collector = BooksCollector()
        collector.add_new_book('Избранное 1')
        collector.add_new_book('Избранное 2')
        collector.add_book_in_favorites('Избранное 1')
        collector.add_book_in_favorites('Избранное 2')
        
        result = collector.get_list_of_favorites_books()
        assert len(result) == 2
        assert 'Избранное 1' in result
        assert 'Избранное 2' in result