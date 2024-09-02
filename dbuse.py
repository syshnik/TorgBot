import small
import db

# класс как предок для использования бд

class dbuse:
    def __init__(self, cursor, conn):   
        self._SamConnect=False
        self._conn=None
        self._cursor = None
        if cursor is not None and  conn is not None:
            # уже законектился
            self._conn=conn
            self._cursor = cursor
        else:
            # сам подключается
            self.ConnectToBase()

    def __del__(self):
        self.CloseConnect()

    def GetConn(self):
        return self._conn
    
    def GetCursor(self):
        return self._cursor
    
    def ConnectToBase(self):
        self._conn=db.GetConnect()
        self._cursor = self._conn.cursor()
        self._SamConnect=True

    def CloseConnect(self):
        if self._SamConnect != True: return False
        if small.ItInTry():
            # курсор-соед-е уже может быть сборошено
            try:
                self._conn.commit()
                self._cursor.close()
                self._conn.close()
            except:
                print("uje sbrosil")
        else:
                self._conn.commit()
                self._cursor.close()
                self._conn.close()
        
        return True

    def GetSell(self, zapros):
        # поучение запроса
        ret=None
        if small.ItInTry():
            # сначала пробуем получить
            try:
                ret=self.WorkGetSel(zapros)
                # все нормально, выходим
                return ret
            except:
                print('Error 4447778')
                # переподключаемся
                self.CloseConnect()
                self.ConnectToBase()
        # и пробуем получить
        ret=self.WorkGetSel(zapros)
        # все нормально, (или не нормально), выходим
        return ret
    
    def MakeCommand(self, commandzapros, andcommit=True, retid=False):
        # выполнение команды
        ret=None
        if small.ItInTry():
            # сначала пробуем 
            try:
                ret  = self.WorkMakeCommand(commandzapros, andcommit, retid)
                # все нормально, выходим
                return ret
            except:
                print('Error 444777228')
                # переподключаемся
                self.CloseConnect()
                self.ConnectToBase()
        # и пробуем 
        ret  = self.WorkMakeCommand(commandzapros, andcommit, retid)
        # все нормально, (или не нормально), выходим
        return ret
    
    def WorkMakeCommand(self, commandzapros, andcommit,  retid):
        # выполнение команды
        save_lastrowid = self._cursor.lastrowid
        self._cursor.execute(commandzapros)
        id_of_new_row=None
        if retid:
            # self._cursor.execute('SELECT LASTVAL()')
            # self._conn.commit()
            # r2=self._cursor.fetchone()
            if save_lastrowid != self._cursor.lastrowid and self._cursor.lastrowid is not None:
                id_of_new_row = self._cursor.lastrowid
        if andcommit:
            self._conn.commit()
        return id_of_new_row
    

    def Commit(self):
        self._conn.commit()

    def WorkGetSel(self, zapros):
        # поучение запроса
        self._cursor.execute(zapros)
        ret=[]
        for row in self._cursor:
            ret.append(row)
        return ret
