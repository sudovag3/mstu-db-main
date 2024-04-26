from tkinter import *
from mysql.connector import connect, Error


def create_update(self, form):
    st1 = self.titles2[self.bd][1:-1].split(',')
    query = 'SELECT * FROM ' + self.tbs[self.bd]
    query += ' WHERE ' + self.ids[self.bd] + '=' + str(self.tr)
    data2 = self.my_sql(query, True)[0]
    data = []
    a = 0
    if self.bd != 6: a = 1; data.append(data2[0])
    for i in range(len(data2) - a):
        if self.dtypes[self.bd][i] == 'dt' and data2[i + a] is not None:
            data.append(data2[i + a].date())
        else:
            data.append(data2[i + a])

    tb = [form.copy()]
    vst1 = -1
    vst2 = -1
    vst3 = -1
    vst4 = -1
    vst5 = -1
    
    options1=['None']
    options2=['None']
    options3=['None']
    options4=['None']
    options5=['None']

    if 'Категория' in tb[0]:
        vst1 = tb[0].index('Категория')
        query = 'SELECT * FROM ' + self.tbs[0]
        data2 = self.my_sql(query, True)
        dct1 = {}
        for d in data2:
            dct1[str(d[0])] = d[1]
            options1.append(d[1])
    if 'Оборудование' in tb[0]:
        vst2 = tb[0].index('Оборудование')
        query = 'SELECT * FROM ' + self.tbs[3]
        data2 = self.my_sql(query, True)
        dct2 = {}
        for d in data2:
            dct2[str(d[0])] = d[1]
            options2.append(d[1])
    if 'Руководитель' in tb[0]:
        vst3 = tb[0].index('Руководитель')
        query = 'SELECT * FROM ' + self.tbs[2]
        data2 = self.my_sql(query, True)
        dct3 = {}
        for d in data2:
            dct3[str(d[0])] = d[2]
            options3.append(d[2])
    if 'Проект' in tb[0]:
        vst4 = tb[0].index('Проект')
        query = 'SELECT * FROM ' + self.tbs[4]
        data2 = self.my_sql(query, True)
        dct4 = {}
        for d in data2:
            dct4[str(d[0])] = str(d[0])
            options4.append(str(d[0]))
    if 'Заказчик' in tb[0]:
        vst5 = tb[0].index('Заказчик')
        query = 'SELECT * FROM ' + self.tbs[5]
        data2 = self.my_sql(query, True)
        dct5 = {}
        for d in data2:
            dct5[str(d[0])] = d[1]
            options5.append(d[1])
    i = 0
    for rw in data:

        if i == vst1:
            data[i] = (dct1.get(str(rw), str(rw)))
        elif i == vst2:
            data[i] = (dct2.get(str(rw), str(rw)))
        elif i == vst3:
            data[i] = (dct3.get(str(rw), str(rw)))
        elif i == vst4:
            data[i] = (dct4.get(str(rw), str(rw)))
        elif i == vst5:
            data[i] = (dct5.get(str(rw), str(rw)))
        i += 1

    if self.bd != 6: data.pop(0)

    check = (self.win.register(self.date_is_valid), "%P")
    check2 = (self.win.register(self.bool_is_valid), "%P")

    self.obj = []
    xs = self.xs
    ys = self.ys

    # xs=19
    # ys=40
    xd = 10
    yd = 10

    btn = Button(text='Назад', command=self.accept_back)
    self.tableim2.append(self.canvas.create_window(self.width - 10, yd, window=btn, anchor='ne'))
    yd += ys * 2.5
    btn = Button(text='Подвердить', command=self.accept_update)
    self.tableim2.append(self.canvas.create_window(self.width - 10, yd, window=btn, anchor='ne'))
    yd += ys * 2.5
    btn2 = Button(text='Удалить', command=self.accept_delete)
    self.tableim2.append(self.canvas.create_window(self.width - 10, yd, window=btn2, anchor='ne'))
    yd += ys * 2.5
    aind=0

    if self.bd != 6: form.pop(0);aind=1

    for i in range(len(form)):
        tr = form[i]
        self.tableim2.append(self.canvas.create_text(xd, yd, text=tr, anchor='nw'))
        if i==vst1-aind:
            self.obj.append(['s',StringVar()])
            opt=options1.copy()
        elif i==vst2-aind:
            self.obj.append(['s',StringVar()])
            opt=options2.copy()
        elif i==vst3-aind:
            self.obj.append(['s',StringVar()])
            opt=options3.copy()
        elif i==vst4-aind:
            self.obj.append(['s',StringVar()])
            opt=options4.copy()
        elif i==vst5-aind:
            self.obj.append(['s',StringVar()])
            opt=options5.copy()
        elif self.dtypes[self.bd][i] == 'dt':
            self.obj.append(['e',Entry(validate="key", validatecommand=check)])
        elif self.dtypes[self.bd][i] == 'b':
            self.obj.append(['e',Entry(validate="key", validatecommand=check2)])
        else:
            self.obj.append(['e',Entry()])
        if self.obj[-1][0]=='e':
            self.obj[-1][1].insert(0, str(data[i]))
            self.tableim2.append(self.canvas.create_window(self.width - 10, yd, window=self.obj[-1][1], anchor='ne'))
        else:
            self.obj[-1][1].set(data[i])
            self.tableim2.append(self.canvas.create_window(self.width-10,yd,window=OptionMenu(self.win,self.obj[-1][1],*opt),anchor='ne'))
        yd += ys * 1.5

    self.set_scroll(self.width, yd + 100)


def create_form(self, form):
    
    
    tb = [form.copy()]
    vst1 = -1
    vst2 = -1
    vst3 = -1
    vst4 = -1
    vst5 = -1
    
    options1=['None']
    options2=['None']
    options3=['None']
    options4=['None']
    options5=['None']

    if 'Категория' in tb[0]:
        vst1 = tb[0].index('Категория')
        query = 'SELECT * FROM ' + self.tbs[0]
        data2 = self.my_sql(query, True)
        for d in data2:
            options1.append(d[1])
    if 'Оборудование' in tb[0]:
        vst2 = tb[0].index('Оборудование')
        query = 'SELECT * FROM ' + self.tbs[3]
        data2 = self.my_sql(query, True)
        for d in data2:
            options2.append(d[1])
    if 'Руководитель' in tb[0]:
        vst3 = tb[0].index('Руководитель')
        query = 'SELECT * FROM ' + self.tbs[2]
        data2 = self.my_sql(query, True)
        for d in data2:
            options3.append(d[2])
    if 'Проект' in tb[0]:
        vst4 = tb[0].index('Проект')
        query = 'SELECT * FROM ' + self.tbs[4]
        data2 = self.my_sql(query, True)
        for d in data2:
            options4.append(str(d[0]))
    if 'Заказчик' in tb[0]:
        vst5 = tb[0].index('Заказчик')
        query = 'SELECT * FROM ' + self.tbs[5]
        data2 = self.my_sql(query, True)
        for d in data2:
            options5.append(d[1])
    
    check = (self.win.register(self.date_is_valid), "%P")
    check2 = (self.win.register(self.bool_is_valid), "%P")

    self.obj = []
    xs = self.xs
    ys = self.ys

    # xs=19
    #   ys=40
    xd = 10
    yd = 10

    btn = Button(text='Назад', command=self.accept_back)
    self.tableim2.append(self.canvas.create_window(self.width - 10, yd, window=btn, anchor='ne'))
    yd += ys * 2.5
    btn = Button(text='Подвердить', command=self.accept_create)
    self.tableim2.append(self.canvas.create_window(self.width - 10, yd, window=btn, anchor='ne'))
    yd += ys * 2.5

    aind=0

    if self.bd != 6: form.pop(0);aind=1

    for i in range(len(form)):
        tr = form[i]
        self.tableim2.append(self.canvas.create_text(xd, yd, text=tr, anchor='nw'))
        if i==vst1-aind:
            self.obj.append(['s',StringVar()])
            opt=options1.copy()
        elif i==vst2-aind:
            self.obj.append(['s',StringVar()])
            opt=options2.copy()
        elif i==vst3-aind:
            self.obj.append(['s',StringVar()])
            opt=options3.copy()
        elif i==vst4-aind:
            self.obj.append(['s',StringVar()])
            opt=options4.copy()
        elif i==vst5-aind:
            self.obj.append(['s',StringVar()])
            opt=options5.copy()
        elif self.dtypes[self.bd][i] == 'dt':
            self.obj.append(['e',Entry(validate="key", validatecommand=check)])
        elif self.dtypes[self.bd][i] == 'b':
            self.obj.append(['e',Entry(validate="key", validatecommand=check2)])
        else:
            self.obj.append(['e',Entry()])

        if self.obj[-1][0]=='e':
            self.tableim2.append(self.canvas.create_window(self.width - 10, yd, window=self.obj[-1][1], anchor='ne'))
        else:
            self.tableim2.append(self.canvas.create_window(self.width-10,yd,window=OptionMenu(self.win,self.obj[-1][1],*opt),anchor='ne'))
        yd += ys * 1.5
    self.set_scroll(self.width, yd + 100)


def change_accept(self, arr):
    st = ''
    dt = self.dtypes[self.bd]
    for i in range(len(arr)):
        if arr[i] == '' and dt[i] == 's':
            st += '\"None\",'
        elif arr[i] == '':
            st += 'null,'
        elif dt[i] == 'i':
            st += str(int(arr[i])) + ','
        elif dt[i] == 's':
            st += '\"' + arr[i] + '\",'
        elif dt[i] == 'dt':
            st += '"' + arr[i] + '",'
        elif dt[i] == 'b':
            st += '1,'
    st = st[:-1]
    return st


def create_table(self):
    tb = []
    tb.append(self.titles[self.bd])
    query = 'SELECT * FROM ' + self.tbs[self.bd]
    data = self.my_sql(query, True)

    vst1 = -1
    vst2 = -1
    vst3 = -1
    vst4 = -1
    vst5 = -1

    if 'Категория' in tb[0]:
        vst1 = tb[0].index('Категория')
        query = 'SELECT * FROM ' + self.tbs[0]
        data2 = self.my_sql(query, True)
        dct1 = {}
        for d in data2:
            dct1[str(d[0])] = d[1]
    if 'Оборудование' in tb[0]:
        vst2 = tb[0].index('Оборудование')
        query = 'SELECT * FROM ' + self.tbs[3]
        data2 = self.my_sql(query, True)
        dct2 = {}
        for d in data2:
            dct2[str(d[0])] = d[1]
    if 'Руководитель' in tb[0]:
        vst3 = tb[0].index('Руководитель')
        query = 'SELECT * FROM ' + self.tbs[2]
        data2 = self.my_sql(query, True)
        dct3 = {}
        for d in data2:
            dct3[str(d[0])] = d[2]
    if 'Проект' in tb[0]:
        vst4 = tb[0].index('Проект')
        query = 'SELECT * FROM ' + self.tbs[4]
        data2 = self.my_sql(query, True)
        dct4 = {}
        for d in data2:
            dct4[str(d[0])] = str(d[0])
    if 'Заказчик' in tb[0]:
        vst5 = tb[0].index('Заказчик')
        query = 'SELECT * FROM ' + self.tbs[5]
        data2 = self.my_sql(query, True)
        dct5 = {}
        for d in data2:
            dct5[str(d[0])] = d[1]

    for rw in data:
        arr = []
        for i in range(len(rw)):
            if i == vst1:
                arr.append(dct1.get(str(rw[i]), str(rw[i])))
            elif i == vst2:
                arr.append(dct2.get(str(rw[i]), str(rw[i])))
            elif i == vst3:
                arr.append(dct3.get(str(rw[i]), str(rw[i])))
            elif i == vst4:
                arr.append(dct4.get(str(rw[i]), str(rw[i])))
            elif i == vst5:
                arr.append(dct5.get(str(rw[i]), str(rw[i])))
            else:
                arr.append(str(rw[i]))
        tb.append(arr)
    return tb


def draw_table(self, x, y, table):
    xs = self.xs
    ys = self.ys

    #     xs=19
    #     ys=40

    trs = []
    bin=0
    if self.bd!=6: bin=1

    if table != []:
        for a in range(len(table[0])):
            trs.append(0)
    for tr in table:
        for i in range(len(tr)):
            trs[i] = max(trs[i], (len(tr[i]) + 2) * xs)
    xd = x
    yd = y
    mxd = self.width
    
    
    if self.route=='view':
        y1d=yd
        
        yd += ys * 2.5
    y3d=yd+25
    yd+=50
    y1=yd
    y2d=(y1-y)//2
    
    for tr in table:

        mxd = max(mxd, xd)
        xd = x
        for i in range(bin,len(tr)):
            self.tableim2.append(self.canvas.create_rectangle(xd, yd, xd + trs[i], yd + ys))
            self.tableim2.append(self.canvas.create_text(xd + trs[i] / 2, yd + ys / 2, text=tr[i]))

            xd += trs[i]
        if yd != y1 and self.route == 'view': self.d_zone.append([x, yd, xd, yd + ys, tr[0]])
        yd += ys

    if self.route == 'view':
        title = self.thead[self.bd]
    elif self.route == 'query':
        title = self.qhead[self.que]
    else:
        title = ''
        if table[0][0]=='Код договора': title='Договора в рамках проекта'
        elif table[0][0]=='Код сотрудника': title='Сотрудники, работающие в рамках проекта'
        elif table[0][0]=='Код оборудования': title='Оборудование, задействанное в проекте'
        elif table[0][0]=='Код проекта': title='Проект - '+table[1][-1]
    self.tableim2.append(self.canvas.create_text(mxd / 2, y3d, text=title))
    if self.route=='view':
        btn = Button(text='Создать', command=self.button_create2)
        self.tableim2.append(self.canvas.create_window(mxd- 20, y2d, window=btn, anchor='ne'))
    self.set_scroll(mxd + 40, yd + 100)
    return mxd, yd


def send_query(self):
    query = self.queres[self.que]
    data = self.my_sql(query, True)
    tb = [self.qtitles[self.que]]

    vst1 = -1
    vst2 = -1
    vst3 = -1
    vst4 = -1
    vst5 = -1

    if 'Категория' in tb[0]:
        vst1 = tb[0].index('Категория')
        query = 'SELECT * FROM ' + self.tbs[0]
        data2 = self.my_sql(query, True)
        dct1 = {}
        for d in data2:
            dct1[str(d[0])] = d[1]
    if 'Оборудование' in tb[0]:
        vst2 = tb[0].index('Оборудование')
        query = 'SELECT * FROM ' + self.tbs[3]
        data2 = self.my_sql(query, True)
        dct2 = {}
        for d in data2:
            dct2[str(d[0])] = d[1]
    if 'Руководитель' in tb[0]:
        vst3 = tb[0].index('Руководитель')
        query = 'SELECT * FROM ' + self.tbs[2]
        data2 = self.my_sql(query, True)
        dct3 = {}
        for d in data2:
            dct3[str(d[0])] = d[2]
    if 'Проект' in tb[0]:
        vst4 = tb[0].index('Проект')
        query = 'SELECT * FROM ' + self.tbs[4]
        data2 = self.my_sql(query, True)
        dct4 = {}
        for d in data2:
            dct4[str(d[0])] = str(d[0])
    if 'Заказчик' in tb[0]:
        vst5 = tb[0].index('Заказчик')
        query = 'SELECT * FROM ' + self.tbs[5]
        data2 = self.my_sql(query, True)
        dct5 = {}
        for d in data2:
            dct5[str(d[0])] = d[1]
    for rw in data:
        arr = []
        for i in range(len(rw)):
            if i == vst1:
                arr.append(dct1.get(str(rw[i]), str(rw[i])))
            elif i == vst2:
                arr.append(dct2.get(str(rw[i]), str(rw[i])))
            elif i == vst3:
                arr.append(dct3.get(str(rw[i]), str(rw[i])))
            elif i == vst4:
                arr.append(dct4.get(str(rw[i]), str(rw[i])))
            elif i == vst5:
                arr.append(dct5.get(str(rw[i]), str(rw[i])))
            else:
                arr.append(str(rw[i]))
        tb.append(arr)
    self.draw_table(self, 10, 10, tb)


def main_menu(self):
    ys = self.ys
    xd = 20
    yd = 10
    labels = ['Категории', 'Новая запись', 'Департаменты', 'Новая запись', 'Сотрудники', 'Новая запись', 'Оборудование',
              'Новая запись',
              'Проекты', 'Новая запись', 'Заказчики', 'Новая запись', 'Договора', 'Новая запись']
    arrx = []
    arry = []
    arran = []
    for i in range(10):
        arrx.append(xd)
        arry.append(yd)
        arran.append('nw')
        arrx.append(self.width - xd)
        arry.append(yd)
        arran.append('ne')
        yd += ys * 2.5
    ind = 0

    btn = Button(text=labels[ind], command=self.bd1_view)
    self.tableim2.append(self.canvas.create_window(arrx[ind], arry[ind], window=btn, anchor=arran[ind]))
    ind += 1
    btn = Button(text=labels[ind], command=self.bd1_create)
    self.tableim2.append(self.canvas.create_window(arrx[ind], arry[ind], window=btn, anchor=arran[ind]))
    ind += 1
    btn = Button(text=labels[ind], command=self.bd2_view)
    self.tableim2.append(self.canvas.create_window(arrx[ind], arry[ind], window=btn, anchor=arran[ind]))
    ind += 1
    btn = Button(text=labels[ind], command=self.bd2_create)
    self.tableim2.append(self.canvas.create_window(arrx[ind], arry[ind], window=btn, anchor=arran[ind]))
    ind += 1
    btn = Button(text=labels[ind], command=self.bd3_view)
    self.tableim2.append(self.canvas.create_window(arrx[ind], arry[ind], window=btn, anchor=arran[ind]))
    ind += 1
    btn = Button(text=labels[ind], command=self.bd3_create)
    self.tableim2.append(self.canvas.create_window(arrx[ind], arry[ind], window=btn, anchor=arran[ind]))
    ind += 1
    btn = Button(text=labels[ind], command=self.bd4_view)
    self.tableim2.append(self.canvas.create_window(arrx[ind], arry[ind], window=btn, anchor=arran[ind]))
    ind += 1
    btn = Button(text=labels[ind], command=self.bd4_create)
    self.tableim2.append(self.canvas.create_window(arrx[ind], arry[ind], window=btn, anchor=arran[ind]))
    ind += 1
    btn = Button(text=labels[ind], command=self.bd5_view)
    self.tableim2.append(self.canvas.create_window(arrx[ind], arry[ind], window=btn, anchor=arran[ind]))
    ind += 1
    btn = Button(text=labels[ind], command=self.bd5_create)
    self.tableim2.append(self.canvas.create_window(arrx[ind], arry[ind], window=btn, anchor=arran[ind]))
    ind += 1
    btn = Button(text=labels[ind], command=self.bd6_view)
    self.tableim2.append(self.canvas.create_window(arrx[ind], arry[ind], window=btn, anchor=arran[ind]))
    ind += 1
    btn = Button(text=labels[ind], command=self.bd6_create)
    self.tableim2.append(self.canvas.create_window(arrx[ind], arry[ind], window=btn, anchor=arran[ind]))
    ind += 1
    btn = Button(text=labels[ind], command=self.bd7_view)
    self.tableim2.append(self.canvas.create_window(arrx[ind], arry[ind], window=btn, anchor=arran[ind]))
    ind += 1
    btn = Button(text=labels[ind], command=self.bd7_create)
    self.tableim2.append(self.canvas.create_window(arrx[ind], arry[ind], window=btn, anchor=arran[ind]))
    ind += 1

    self.set_scroll(self.width, yd + 100)


def create_project(self):
    money=0
    xs = self.xs
    ys = self.ys

    xd = 10
    yd = 10
    y1d = []

    y1d.append(yd)
    yd += ys * 2.5

    y1d.append(yd)
    yd += ys * 2.5

    y1d.append(yd)
    yd += ys * 2.5

    y1d.append(yd)
    yd += ys * 2.5

    tbs = []
    tb = []
    tb.append(self.titles[4])
    query = 'SELECT * FROM ' + self.tbs[self.bd]
    query += ' WHERE ' + self.ids[self.bd] + '=' + str(self.tr)
    data = self.my_sql(query, True)
    for rw in data:
        arr = []
        for i in range(len(rw)):
            arr.append(str(rw[i]))
        tb.append(arr)
        ind_b = arr[2]
        ind_a = arr[4]
    tbs.append(tb)

    tb = []
    tb.append(self.titles[6])
    query = 'SELECT * FROM Contract WHERE project_id = ' + str(self.tr)
    data = self.my_sql(query, True)
    for rw in data:
        arr = []
        for i in range(len(rw)):
            arr.append(str(rw[i]))
            if i==3: money+=int(rw[i])
        tb.append(arr)
    tbs.append(tb)

    tb = []
    tb.append(self.titles[2])
    query = 'SELECT * FROM Employee WHERE category_id = ' + str(ind_a)
    data = self.my_sql(query, True)
    for rw in data:
        arr = []
        for i in range(len(rw)):
            arr.append(str(rw[i]))
        tb.append(arr)
    tbs.append(tb)

    tb = []
    tb.append(self.titles[3])
    query = 'SELECT * FROM Equipment WHERE equipment_id = ' + str(ind_b)
    data = self.my_sql(query, True)
    for rw in data:
        arr = []
        for i in range(len(rw)):
            arr.append(str(rw[i]))
        tb.append(arr)
    tbs.append(tb)
    
    

    for tb in tbs:
        vst1 = -1
        vst2 = -1
        vst3 = -1
        vst4 = -1
        vst5 = -1

        if 'Категория' in tb[0]:
            vst1 = tb[0].index('Категория')
            query = 'SELECT * FROM ' + self.tbs[0]
            data2 = self.my_sql(query, True)
            dct1 = {}
            for d in data2:
                dct1[str(d[0])] = d[1]
        if 'Оборудование' in tb[0]:
            vst2 = tb[0].index('Оборудование')
            query = 'SELECT * FROM ' + self.tbs[3]
            data2 = self.my_sql(query, True)
            dct2 = {}
            for d in data2:
                dct2[str(d[0])] = d[1]
        if 'Руководитель' in tb[0]:
            vst3 = tb[0].index('Руководитель')
            query = 'SELECT * FROM ' + self.tbs[2]
            data2 = self.my_sql(query, True)
            dct3 = {}
            for d in data2:
                dct3[str(d[0])] = d[2]
        if 'Проект' in tb[0]:
            vst4 = tb[0].index('Проект')
            query = 'SELECT * FROM ' + self.tbs[4]
            data2 = self.my_sql(query, True)
            dct4 = {}
            for d in data2:
                dct4[str(d[0])] = str(d[0])
        if 'Заказчик' in tb[0]:
            vst5 = tb[0].index('Заказчик')
            query = 'SELECT * FROM ' + self.tbs[5]
            data2 = self.my_sql(query, True)
            dct5 = {}
            for d in data2:
                dct5[str(d[0])] = d[1]

        for j in range(1, len(tb)):
            rw = tb[j]
            for i in range(len(rw)):
                if i == vst1:
                    rw[i] = (dct1.get(str(rw[i]), str(rw[i])))
                elif i == vst2:
                    rw[i] = (dct2.get(str(rw[i]), str(rw[i])))
                elif i == vst3:
                    rw[i] = (dct3.get(str(rw[i]), str(rw[i])))
                elif i == vst4:
                    rw[i] = (dct4.get(str(rw[i]), str(rw[i])))
                elif i == vst5:
                    rw[i] = (dct5.get(str(rw[i]), str(rw[i])))
    mxd = self.width
    y2d=[]
    arr=[
    [ 'Материалы проекта', 'Оборудование, используемое в проекте', 'Руководитель проекта', 'Категория'],
    []
    ]
    yd+=ys*0.5
    y2d.append(yd)
    yd+=ys*1.5
    gtitle='Проект - '+tbs[0][1][-1]
    for i in range(4):
        y2d.append(yd)
        yd+=ys
        arr[1].append(tbs[0][1][i+1])
    tbs.pop(0)
    for tb in tbs:
        x1, yd = self.draw_table(self, 10, yd + 40, tb)
        mxd = max(mxd, x1)
    self.generate = tbs
    self.generate2=[
    'Проект - '+str(tbs[0][1][-1]),
    'В рамках проекта заработано: '+str(money)
    ]
    

    btn = Button(text='Назад', command=self.accept_back)
    self.tableim2.append(self.canvas.create_window(mxd - 30, y1d[0], window=btn, anchor='ne'))
    btn = Button(text='Изменить', command=self.button_update)
    self.tableim2.append(self.canvas.create_window(mxd - 30, y1d[1], window=btn, anchor='ne'))
    btn = Button(text='Удалить', command=self.accept_delete)
    self.tableim2.append(self.canvas.create_window(mxd - 30, y1d[2], window=btn, anchor='ne'))
    btn = Button(text='Создать отчет', command=self.accept_generate)
    self.tableim2.append(self.canvas.create_window(mxd - 30, y1d[3], window=btn, anchor='ne'))
    
    self.tableim2.append(self.canvas.create_text(mxd//2,y2d[0],text=gtitle))
    for i in range(4):
        txt=arr[0][i]+': '+arr[1][i]
        self.tableim2.append(self.canvas.create_text(15,y2d[i+1],text=txt,anchor='nw'))

    self.set_scroll(mxd, yd + 100)