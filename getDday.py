# 기간입력: 20191210-20200520
# 휴일입력: 20191225 20200101 20200124 20200127 20200415 20200430 20200501 20200504 20200505
import calendar
import time

class Period:
    def __init__(self):
        self.prd = input("기간입력:")
        self.dff = input("휴일입력:")  

    def prop(self):
        tmpStr = self.dff.split() #['20191225', '20200101']
        self.sYear = int(self.prd[0:4])
        self.sMonth = int(self.prd[4:6])
        self.sDay = int(self.prd[6:8])
        self.eYear = int(self.prd[9:13])
        self.eMonth = int(self.prd[13:15])
        self.eDay = int(self.prd[15:])
        self.a = [(self.sYear,self.sMonth,self.sDay),(self.eYear,self.eMonth,self.eDay)]
        self.holiple = []
        for i in tmpStr:
            holiday = int(i[0:4]), int(i[4:6]), int(i[6:8])
            self.holiple.append(holiday)
        return self.holiple

    def yearAndmonth(self):
        self.yearL = []
        self.monthL = []
        while True:
            self.yearL.append(self.sYear)
            self.monthL.append(self.sMonth)
            self.sYear = self.sYear
            self.sMonth += 1
            if self.sMonth ==13:
                self.sYear += 1
                self.sMonth =1
            if self.sYear ==self.eYear and self.sMonth ==self.eMonth+1:
                break

    def dayday(self):
        c = calendar.Calendar()
        self.result =[] 
        while self.yearL:
            year = self.yearL.pop(0)
            month = self.monthL.pop(0)
            tmp = []
            for i in c.itermonthdays3(year, month):
                tmp.append(i)
            firstWday_and_monLen = calendar.monthrange(year,month)
            firstWday = firstWday_and_monLen[0]
            monLen = firstWday_and_monLen[1]
            lastWday = calendar.weekday(year,month,monLen)
            if firstWday != 0:
                tmp = tmp[firstWday:]
            if lastWday != 6:
                tmp = tmp[:monLen]
            for j in tmp:
                a = calendar.weekday(j[0],j[1],j[2])
                if a != 5 and a != 6:
                    self.result.append(j)
        start = self.result.index(self.a[0])
        self.result = self.result[start:]
        end = self.result.index(self.a[1])
        self.result = self.result[:end+1]
        for holiday in self.holiple:
            self.result.remove(holiday)
        return self.result

    def prompt(self):
        totalday = len(self.result)
        todayStr = time.strftime("오늘은 %Y년 %m월 %d일입니다.\n")
        today = time.strftime("%Y%m%d")
        todayyear = int(today[:4])
        todaymonth = int(today[4:6])
        todayday = int(today[6:])
        todayidx = self.result.index((todayyear, todaymonth, todayday)) 
        fromtoday = self.result[todayidx:]                      
        print( todayStr+ "총 작업일수는 %s일 중에\n" %totalday + "남은 작업일수는 %s입니다." %len(fromtoday))
        f=open("text.txt", 'w')
        f.write(todayStr+ "총 작업일수는 %s일 중에\n" %totalday + "남은 작업일수는 %s입니다." %len(fromtoday))
        f.close()

        
period = Period()
period.prop()
period.yearAndmonth()
period.dayday()
period.prompt()