from unittest import TestCase, expectedFailure
from parameterized import parameterized
from main import unique_name, sort_durations, namesake, courses, mentors, durations, create_folder, delete_folder, token


class TestUniqueName(TestCase):

    @parameterized.expand([
        (mentors, list),
        (mentors[0], list),
        (mentors[0][1], str),
        (mentors, dict)
    ])
    def test_type(self, a, b):
        self.assertIsInstance(a, b)

    @parameterized.expand([
        ('Адилет',),
        ('Александр',),
        ('Петр',)
    ])
    def test_result(self, name):
        res = unique_name(mentors)
        self.assertIn(name, res)


class TestSortDurations(TestCase):

    @parameterized.expand([
        (r'\w*-\w*\s\w*\s\w*\s-\s\d{2}\s\w*', 0),
        (r'\w*-\w*\s\w*\s\w*\s-\s\d{2}\s\w*', 4),
        (r'(Java){1}.*', 1)
    ])
    def test_regex(self, pattern, index):
        result = sort_durations(courses, mentors, durations)
        self.assertRegex(result.split('\n')[index], pattern)


class TestNamesake(TestCase):

    @parameterized.expand([
        (1,),
        (5,)
    ])
    def test_result_len(self, res_len):
        result = namesake(courses, mentors, durations)
        self.assertGreaterEqual(len(result), res_len)

    @parameterized.expand([
        (0, 2, 'Java-разработчик'),
        (1, 4, 'Python')
    ])
    def test_result(self, indexlist, indexstr, some):
        result = namesake(courses, mentors, durations)
        self.assertEqual(result[indexlist].split(' ')[indexstr], some)


class TestYandexNewFolder(TestCase):

    def tearDown(self):
        delete_folder(token, 'удалить')

    @parameterized.expand([
        (token, 'удалить', 201),
        ('token', 'удалить', 201)
    ])
    def test_status_code(self, ya_token, folder, status_code):
        result = create_folder(ya_token, folder)
        self.assertEqual(result, status_code)

    @parameterized.expand([
        ('123456', 201),
        ('token', 401),
        (token, 201)
    ])
    @expectedFailure
    def test_non_auth(self, ya_token, status_code):
        result = create_folder(ya_token, 'удалить')
        self.assertEqual(result, status_code)
