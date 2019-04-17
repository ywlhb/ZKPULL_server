#FROM    ywlhb/flask-python-winsvrcore

#ADD     ["./nginx-1.13.8","C:/nginx"]

#ADD     ["./scr","\"C:/Program Files/Python36\""]

#CMD     ["\"C:/Program Files (x86)/Python35-32/python\"", "\"C:/Program Files (x86)/Python35-32/hello.py\""]

#FROM    ywlhb/pull 
#WORKDIR nginx
#CMD ["nginx"]
#CMD powershell.exe -Command start nginx
#WORKDIR app
#ENTRYPOINT [ "python","home.py" ]

FROM    ywlhb/nginx-tornado-swagger-flask-winsvrcore:x86-32
ADD     ["./python_add","\"C:/Program Files (x86)/Python36-32\""]
ADD     ["./app","\"C:/app\""]
ADD     ["./nginxconf","\"C:/nginx/conf\""]
CMD     ["python","c:/app/home.py"]





