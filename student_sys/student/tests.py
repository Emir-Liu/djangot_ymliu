from django.test import TestCase, Client

from .models import Student

# Create your tests here.

class StudentModelTestCase(TestCase):
    '''
    model层单元测试
    '''
    def setUp(self) -> None:
        Student.objects.create(
            name='test',
            sex=1,
            email='test@qq.com',
            qq='123',
            phone='234'
        )

    def test_create_and_sex_show(self):
        student = Student.objects.create(
            name='huyang',
            sex=1,
            email='123@qq.com',
            profession='程序员',
            qq='3232',
            phone='2344',
        )

        self.assertEqual(student.sex_show, '男', '性别字段内容和展示不一致')

    def test_filter(self):
        Student.objects.create(
            name='huyang',
            sex=1,
            email='123@qq.com',
            profession='程序员',
            qq='3232',
            phone='2344',
        )

        name ='test'
        students = Student.objects.filter(name=name)
        self.assertEqual(students.count(), 1,'应该只存在一个名称为{}的记录'.format(name))

    '''
    View层单元测试
    '''
    def test_get_index(self):
        client = Client()
        response = client.get('/')
        self.assertEqual(response.status_code, 200, 'status code must be 200')

    def test_post_student(self):
        client = Client()

        data = dict(
            name = 'test_for_post',
            sex = 1,
            email = '11@qq.com',
            profession = 'code',
            qq = '222',
            phone = '3232'
        )

        response = client.post('/', data)

        self.assertEqual(response.status_code, 302, 'status code must be 302')

        response = client.get('/')

        self.assertTrue(b'test_for_post' in response.content,
                        'response content must contain test_for_post')
