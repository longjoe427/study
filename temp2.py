# class Role(object):
#     n = 123  # 类变量
#     name = '类名称'
#
#     def __init__(self, name, role, weapon, life_value):
#         self.name = name  # 实例变量
#         self.role = role
#         self.weapon = weapon
#         self.life_value = life_value
#
#     def shot(self):
#         print('%s die' % self.name)
# print(Role.n)
# r1 = Role('ak', 'terrist', 'ak47', 100)
# r1.shot()
# print(Role.name)
#
# print(r1.life_value)
# print(r1.n)
# å
# r1.name = 'gg'
# print(r1.name)
# del r1.name
# print(r1.name)
# print(r1.__dict__)
# r1.bullet_prove = True
# print(r1.bullet_prove)
# r1.bullet_prove = False
#
# print(r1.bullet_prove)
import gc


# class School:
#     members = 0
#
#     def __init__(self, name, addr):
#         self.name = name
#         self.addr = addr
#         self.students = []
#         self.staffs = []
#
#     def enroll(self, stu):
#         print("为%s提供注册手续" % stu.name)
#         self.students.append(stu)
#
#     def hire(self, staff_obj):
#         print("雇佣新员工%s" % staff_obj.name)
#         self.staffs.append(staff_obj)
#
#
# class SchoolMember(object):
#     def __init__(self, name, age, sex):
#         self.name = name
#         self.age = age
#         self.sex = sex
#
#     def tell(self):
#         pass
#
#
# class Teacher(SchoolMember):
#     def __init__(self, name, age, sex, salary, course):
#         super(Teacher, self).__init__(name, age, sex)
#         self.salary = salary
#         self.course = course
#
#     def tell(self):
#         print('''
#         ----  info of Teacher：%s   ----
#         Name:%s
#         Age:%s
#         Sex:%s
#         Salary:%s
#         Course:%s
#
#         ''' % (self.name, self.name, self.age, self.sex, self.salary, self.course))
#
#     def teach(self):
#         print('%s is teaching course[%s]' % (self.name, self.course))
#
#
# class Students(SchoolMember):
#     def __init__(self, name, age, sex, stu_id, grade):
#         super(Students, self).__init__(name, age, sex)
#         self.stu_id = stu_id
#         self.grade = grade
#
#     def tell(self):
#         print('''
#         ----info of Students：%s ----
#         Name:%s
#         Age:%s
#         Sex:%s
#         stu_id:%s
#         grade:%s
#
#         ''') % (self.name, self.name, self.age, self.sex, self.stu_id, self.grade)
#
#     def pay_tuition(self, amount):
#         print('%s has paied tuition for [%s]' % (self.name, amount))


# school = School('old boy', 'beijing')
# print(school)
# # s = School('11', 'beijing')
# t1 = Teacher('ff', 56, 'f', 2000, 'python')
# t2 = Teacher('kk', 50, 'f', 4000, 'linux')
# t3 = Teacher('yy', 50, 'f', 4000, 'linux')
# s1 = Students('huahua', 20, 'M', 1, 'python')
# s2 = Students('huahua1', 25, 'M', 2, 'linux')
#
# t1.tell()
# school.hire(t1)
# school.hire(t2)
# school.hire(t3)
# school.enroll(s1)
# # print(school.students)
# print(school.staffs)
# school.staffs[0].teach()
# for stu in school.students:
#     stu.pay_tuition(1000)
# from tem import ALL
#
#
# class Son:
#     def __init__(self, instance):
#         self.mBattle = instance
#
#     def getSon(self):
#         return self.mBattle.getAlltest()
#
#
# s = Son()
# s.getAll()


user, passwd = 'll', '123'


def auth(auth_type):
    print('auth func:', auth_type)

    def out_wrapper(func):
        def wrapper(*args, **kwargs):
            print('wrapper func args:', *args, **kwargs)
            username = input('username:').strip()
            password = input('password:').strip()
            if auth_type == 'local':
                if user == username and passwd == password:
                    print('\033[32;1mUser has passes authenticatiion]\033[0m')
                    res = func(*args, **kwargs)
                    print('----after-----')
                    return res
                else:
                    exit('\033[31;1mInvalid id username or password]\033[0m')
            elif auth_type == 'ldap':
                print('还没搞定诶，下次再来')

        return wrapper

    return out_wrapper


def index():
    print('welcome to index')


@auth(auth_type='local')
def home():
    print('welcome to home')
    return "from home"


@auth(auth_type='ldap')
def bbs():
    print('welcome to bbs')


index()
print(home())
bbs()
