def start(self):
    self.tableim = []
    self.tableim2 = []
    self.obj = []
    self.d_zone = []
    self.end = 0
    self.db = ''
    self.route = ''
    self.canvas.bind_all('<Motion>', self.motion)
    self.canvas.bind_all('<ButtonPress-1>', self.bpress1)
    self.x = 0
    self.y = 0

    self.bd = 0
    self.tr = 0
    self.tbs = [
        'Category',
        'Department',
        'Employee',
        'Equipment',
        'Project',
        'Customer',
        'Contract'
    ]

    self.titles = [
        ['Код категории', 'Название категории', 'Код оборудования'],
        ['Код департамента', 'Название департамента', 'Категория'],
        ['Код сотрудника', 'Категория', 'ФИО сотрудника', 'Дата приёма', 'Дата увольнения',
         'Число авторских свидетельств', 'Наименование аутстафф-компании',
         'Возможность занимания руководящей должности'],
        ['Код оборудования', 'Название оборудования', 'Категория', ],
        ['Код проекта', 'Материалы проекта', 'Оборудование', 'Руководитель', 'Категория', 'Название проекта'],
        ['Код заказчика', 'ФИО заказчика', 'Паспортные данные заказчика', 'Адрес заказчика',
         'Номер телефона заказчика'],
        ['Код договора', 'Проект', 'Заказчик', 'Стоимость работ', 'Дата окончания работ', ]
    ]

    self.titles2 = [
        '(category_name,equipment_code)',
        '(department_name,category_id)',
        '(category_id,employee_full_name,hire_date, fire_date, copyright_certificates_number, outstaff_company_name, head_position_possible)',
        '(equipment_name,category_id)',
        '(project_materials,equipment_id,head_employee_id,category_id,project_name)',
        '(customer_full_name,customer_passport_data,customer_address,customer_phone)',
        '(contract_id,project_id,customer_id,deal_cost,work_finish_date)'
    ]

    self.ids = ['category_id', 'department_id', 'employee_id', 'equipment_id', 'project_id', 'customer_id',
                'contract_id']

    self.dtypes = [
        ['s', 'i'],
        ['s', 'i'],
        ['i', 's', 'dt', 'dt', 'i', 's', 'b'],
        ['s', 'i'],
        ['s', 'i', 'i', 'i', 's'],
        ['s', 's', 's', 's'],
        ['i', 'i', 'i', 'i', 'dt']
    ]

    self.queres = [
        'select * from Project',
        'select category_name as name from Category',
        'select employee_full_name from Employee where head_position_possible = true',
        'select deal_cost, work_finish_date from Contract where work_finish_date > (SELECT AVG(deal_cost) FROM Contract)',
        'select count(1) FROM Employee',
        "select contract_id as 'Код договора', customer_id as 'Код заказчика', work_finish_date as 'Дата окончания работ' from Contract Where customer_id = 2 and work_finish_date > curdate()",
        "select count(1) as 'Кол-во проектов', (select department_name from Department where Department.category_id = Project.category_id limit 1) as 'Название команды' from Project group by category_id",
        "select count(1) as 'Кол-во проектов c несколькими командами' from Project where (select count(1) from Department where Department.category_id = Project.category_id) > 1",

        '''select 
            Department.department_name from(
            select * from Project)
            as Projects, (select * from Department) as Department 
            where (
                select count(1) 
                from Department where Department.category_id = Projects.category_id) > 1
            group by Department.department_name''',
        '''select Employee.employee_full_name as 'ФИО сотрудника', (select Department.department_name from Department where Department.category_id = Employee.category_id limit 1) as 'Название команды'  from (select 
                Department.category_id from(
                select * from Project)
                as Projects, (select * from Department) as Department 
                where (
                    select count(1) 
                    from Department where Department.category_id = Projects.category_id) > 1
                group by Department.category_id) as Department, (select * from Employee) as Employee
                where Employee.category_id = Department.category_id''',
        "Select count(1) from Employee where outstaff_company_name = 'None'",
        "Select customer_full_name, (select sum(deal_cost) from Contract where Contract.customer_id = Customer.customer_id) from Customer;",
        "select count(*) as 'Кол-во заказов', (select customer_full_name from Customer where Customer.customer_id = Contract.customer_id) as 'ФИО заказчика' from Contract group by Contract.customer_id order by customer_id desc"
    ]

    self.que = 0

    self.qtitles = [
        ['Код проекта', 'Материалы проекта', 'Код оборудования', 'Код руководителя', 'Категория', 'Название проекта'],
        ['Название категории'],
        ['ФИО сотрудника'],
        ['Стоимость работ', 'Дата окончания работ'],
        ['Количество сотрудников'],
        ['Код договора', 'Код заказчика', 'Дата окончания работ', ],
        ['Кол-во проектов', 'Название команды'],
        ['Кол-во проектов c несколькими командами'],
        ['Название команды'],
        ['ФИО сотрудника', 'Название команды'],
        ['Кол-во сотрудников, которые не пришли из аутстафф-компаний'],
        ['ФИО заказчика', 'Общее кол-во денег, которое принёс  заказчик'],
        ['Кол-во заказов', 'ФИО заказчика']
    ]

    self.thead = [
        'Категории',
        'Команды',
        'Сотрудники',
        'Оборудование',
        'Проекты',
        'Заказчики',
        'Договора'
    ]
    self.qhead = [
        'Проекты',
        'Названия категорий',
        'Сотрудники, способные занять руководящую должность',
        'Договора в работе',
        'Количество сотрудников',
        'Кол-во активных проектов с конкретным заказчиком',
        'Количество проектов, над которым работает каждая команда',
        'Кол-во проектов с несколькими командами',
        'Названия команд, работающих над несколькими проектами',
        'ФИО сотрудника и название команды, работающих над несколькими проектами',
        'Кол-во сотрудников, которые не пришли из аутстафф-компаний',
        'Общее кол-во денег, которое принёс каждый заказчик',
        'Кол-во заказов от каждого заказчика по убыванию'
    ]
