from ftplib import FTP

#FTP сервер
ftp = FTP('')
ftp.login()

#Дириктория из корня
ftp.cwd('')

#Команда на вывод содержимого корня или дириктории
data = ftp.retrlines('LIST')
print(data)

