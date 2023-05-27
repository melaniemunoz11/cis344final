Python 3.11.3 (v3.11.3:f3909b8bc8, Apr  4 2023, 20:12:10) [Clang 13.0.0 (clang-1300.0.29.30)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.

============ RESTART: /Users/melaniemunoz/Downloads/portalServer.py ============

Warning (from warnings module):
  File "/Users/melaniemunoz/Downloads/portalServer.py", line 4
    import cgi
DeprecationWarning: 'cgi' is deprecated and slated for removal in Python 3.13
Starting httpd on port 8000

============ RESTART: /Users/melaniemunoz/Downloads/portalServer.py ============
Starting httpd on port 8000

============ RESTART: /Users/melaniemunoz/Downloads/portalServer.py ============
Starting httpd on port 8000
Error while connecting to MySQL 2005 (HY000): Unknown MySQL server host 'banks_portal' (8)
----------------------------------------
Exception occurred during processing of request from ('127.0.0.1', 61118)
Traceback (most recent call last):
  File "/Library/Frameworks/Python.framework/Versions/3.11/lib/python3.11/socketserver.py", line 317, in _handle_request_noblock
    self.process_request(request, client_address)
  File "/Library/Frameworks/Python.framework/Versions/3.11/lib/python3.11/socketserver.py", line 348, in process_request
    self.finish_request(request, client_address)
  File "/Library/Frameworks/Python.framework/Versions/3.11/lib/python3.11/socketserver.py", line 361, in finish_request
    self.RequestHandlerClass(request, client_address, self)
  File "/Users/melaniemunoz/Downloads/portalServer.py", line 10, in __init__
    BaseHTTPRequestHandler.__init__(self, *args)
  File "/Library/Frameworks/Python.framework/Versions/3.11/lib/python3.11/socketserver.py", line 755, in __init__
    self.handle()
  File "/Library/Frameworks/Python.framework/Versions/3.11/lib/python3.11/http/server.py", line 432, in handle
    self.handle_one_request()
  File "/Library/Frameworks/Python.framework/Versions/3.11/lib/python3.11/http/server.py", line 420, in handle_one_request
    method()
  File "/Users/melaniemunoz/Downloads/portalServer.py", line 63, in do_GET
    records = self.database.getAllAccounts()
              ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/Users/melaniemunoz/Downloads/portalDatabase.py", line 38, in getAllAccounts
    if self.connection.is_connected():
       ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
AttributeError: 'NoneType' object has no attribute 'is_connected'
----------------------------------------
Error while connecting to MySQL 2005 (HY000): Unknown MySQL server host 'banks_portal' (8)
----------------------------------------
Exception occurred during processing of request from ('127.0.0.1', 61120)
Traceback (most recent call last):
  File "/Library/Frameworks/Python.framework/Versions/3.11/lib/python3.11/socketserver.py", line 317, in _handle_request_noblock
    self.process_request(request, client_address)
  File "/Library/Frameworks/Python.framework/Versions/3.11/lib/python3.11/socketserver.py", line 348, in process_request
    self.finish_request(request, client_address)
  File "/Library/Frameworks/Python.framework/Versions/3.11/lib/python3.11/socketserver.py", line 361, in finish_request
    self.RequestHandlerClass(request, client_address, self)
  File "/Users/melaniemunoz/Downloads/portalServer.py", line 10, in __init__
    BaseHTTPRequestHandler.__init__(self, *args)
  File "/Library/Frameworks/Python.framework/Versions/3.11/lib/python3.11/socketserver.py", line 755, in __init__
    self.handle()
  File "/Library/Frameworks/Python.framework/Versions/3.11/lib/python3.11/http/server.py", line 432, in handle
    self.handle_one_request()
  File "/Library/Frameworks/Python.framework/Versions/3.11/lib/python3.11/http/server.py", line 420, in handle_one_request
    method()
  File "/Users/melaniemunoz/Downloads/portalServer.py", line 63, in do_GET
    records = self.database.getAllAccounts()
              ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/Users/melaniemunoz/Downloads/portalDatabase.py", line 38, in getAllAccounts
    if self.connection.is_connected():
       ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
AttributeError: 'NoneType' object has no attribute 'is_connected'
----------------------------------------
Error while connecting to MySQL 2005 (HY000): Unknown MySQL server host 'banks_portal' (8)
----------------------------------------
Exception occurred during processing of request from ('127.0.0.1', 61122)
Traceback (most recent call last):
  File "/Library/Frameworks/Python.framework/Versions/3.11/lib/python3.11/socketserver.py", line 317, in _handle_request_noblock
    self.process_request(request, client_address)
  File "/Library/Frameworks/Python.framework/Versions/3.11/lib/python3.11/socketserver.py", line 348, in process_request
    self.finish_request(request, client_address)
  File "/Library/Frameworks/Python.framework/Versions/3.11/lib/python3.11/socketserver.py", line 361, in finish_request
    self.RequestHandlerClass(request, client_address, self)
  File "/Users/melaniemunoz/Downloads/portalServer.py", line 10, in __init__
    BaseHTTPRequestHandler.__init__(self, *args)
  File "/Library/Frameworks/Python.framework/Versions/3.11/lib/python3.11/socketserver.py", line 755, in __init__
    self.handle()
  File "/Library/Frameworks/Python.framework/Versions/3.11/lib/python3.11/http/server.py", line 432, in handle
    self.handle_one_request()
  File "/Library/Frameworks/Python.framework/Versions/3.11/lib/python3.11/http/server.py", line 420, in handle_one_request
    method()
  File "/Users/melaniemunoz/Downloads/portalServer.py", line 63, in do_GET
    records = self.database.getAllAccounts()
              ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/Users/melaniemunoz/Downloads/portalDatabase.py", line 38, in getAllAccounts
    if self.connection.is_connected():
       ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
AttributeError: 'NoneType' object has no attribute 'is_connected'
----------------------------------------
Error while connecting to MySQL 2005 (HY000): Unknown MySQL server host 'banks_portal' (8)
----------------------------------------
Exception occurred during processing of request from ('127.0.0.1', 61124)
Traceback (most recent call last):
  File "/Library/Frameworks/Python.framework/Versions/3.11/lib/python3.11/socketserver.py", line 317, in _handle_request_noblock
    self.process_request(request, client_address)
  File "/Library/Frameworks/Python.framework/Versions/3.11/lib/python3.11/socketserver.py", line 348, in process_request
    self.finish_request(request, client_address)
  File "/Library/Frameworks/Python.framework/Versions/3.11/lib/python3.11/socketserver.py", line 361, in finish_request
    self.RequestHandlerClass(request, client_address, self)
  File "/Users/melaniemunoz/Downloads/portalServer.py", line 10, in __init__
    BaseHTTPRequestHandler.__init__(self, *args)
  File "/Library/Frameworks/Python.framework/Versions/3.11/lib/python3.11/socketserver.py", line 755, in __init__
    self.handle()
  File "/Library/Frameworks/Python.framework/Versions/3.11/lib/python3.11/http/server.py", line 432, in handle
    self.handle_one_request()
  File "/Library/Frameworks/Python.framework/Versions/3.11/lib/python3.11/http/server.py", line 420, in handle_one_request
    method()
  File "/Users/melaniemunoz/Downloads/portalServer.py", line 63, in do_GET
    records = self.database.getAllAccounts()
              ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/Users/melaniemunoz/Downloads/portalDatabase.py", line 38, in getAllAccounts
    if self.connection.is_connected():
       ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
AttributeError: 'NoneType' object has no attribute 'is_connected'
----------------------------------------
Error while connecting to MySQL 2005 (HY000): Unknown MySQL server host 'banks_portal' (8)
----------------------------------------
Exception occurred during processing of request from ('127.0.0.1', 61126)
Traceback (most recent call last):
  File "/Library/Frameworks/Python.framework/Versions/3.11/lib/python3.11/socketserver.py", line 317, in _handle_request_noblock
    self.process_request(request, client_address)
  File "/Library/Frameworks/Python.framework/Versions/3.11/lib/python3.11/socketserver.py", line 348, in process_request
    self.finish_request(request, client_address)
  File "/Library/Frameworks/Python.framework/Versions/3.11/lib/python3.11/socketserver.py", line 361, in finish_request
    self.RequestHandlerClass(request, client_address, self)
  File "/Users/melaniemunoz/Downloads/portalServer.py", line 10, in __init__
    BaseHTTPRequestHandler.__init__(self, *args)
  File "/Library/Frameworks/Python.framework/Versions/3.11/lib/python3.11/socketserver.py", line 755, in __init__
    self.handle()
  File "/Library/Frameworks/Python.framework/Versions/3.11/lib/python3.11/http/server.py", line 432, in handle
    self.handle_one_request()
  File "/Library/Frameworks/Python.framework/Versions/3.11/lib/python3.11/http/server.py", line 420, in handle_one_request
    method()
  File "/Users/melaniemunoz/Downloads/portalServer.py", line 63, in do_GET
    records = self.database.getAllAccounts()
              ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/Users/melaniemunoz/Downloads/portalDatabase.py", line 38, in getAllAccounts
    if self.connection.is_connected():
       ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
AttributeError: 'NoneType' object has no attribute 'is_connected'
----------------------------------------
Error while connecting to MySQL 2005 (HY000): Unknown MySQL server host 'banks_portal' (8)
----------------------------------------
Exception occurred during processing of request from ('127.0.0.1', 61128)
Traceback (most recent call last):
  File "/Library/Frameworks/Python.framework/Versions/3.11/lib/python3.11/socketserver.py", line 317, in _handle_request_noblock
    self.process_request(request, client_address)
  File "/Library/Frameworks/Python.framework/Versions/3.11/lib/python3.11/socketserver.py", line 348, in process_request
    self.finish_request(request, client_address)
  File "/Library/Frameworks/Python.framework/Versions/3.11/lib/python3.11/socketserver.py", line 361, in finish_request
    self.RequestHandlerClass(request, client_address, self)
  File "/Users/melaniemunoz/Downloads/portalServer.py", line 10, in __init__
    BaseHTTPRequestHandler.__init__(self, *args)
  File "/Library/Frameworks/Python.framework/Versions/3.11/lib/python3.11/socketserver.py", line 755, in __init__
    self.handle()
  File "/Library/Frameworks/Python.framework/Versions/3.11/lib/python3.11/http/server.py", line 432, in handle
    self.handle_one_request()
  File "/Library/Frameworks/Python.framework/Versions/3.11/lib/python3.11/http/server.py", line 420, in handle_one_request
    method()
  File "/Users/melaniemunoz/Downloads/portalServer.py", line 63, in do_GET
    records = self.database.getAllAccounts()
              ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/Users/melaniemunoz/Downloads/portalDatabase.py", line 38, in getAllAccounts
    if self.connection.is_connected():
       ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
AttributeError: 'NoneType' object has no attribute 'is_connected'
----------------------------------------
Error while connecting to MySQL 2005 (HY000): Unknown MySQL server host 'banks_portal' (8)

============ RESTART: /Users/melaniemunoz/Downloads/portalServer.py ============
Starting httpd on port 8000
[(1, 'Maria', 123456789, Decimal('10000.00'), 'active'), (2, 'Linda', 987654321, Decimal('2600.00'), 'inactive'), (3, 'John', 222222222, Decimal('100.50'), 'active'), (4, 'Patty', 111111111, Decimal('509.75'), 'inactive'), (5, 'Maria Jozef', 123456789, Decimal('10000.00'), 'active'), (6, 'Linda Jones ', 987654321, Decimal('2600.00'), 'inactive'), (7, 'John McGrail', 222222222, Decimal('100.50'), 'active'), (8, 'Patty Luna', 111111111, Decimal('509.75'), 'inactive'), (9, 'Maria Jozef', 123456789, Decimal('10000.00'), 'active'), (10, 'Linda Jones ', 987654321, Decimal('2600.00'), 'inactive'), (11, 'John McGrail', 222222222, Decimal('100.50'), 'active'), (12, 'Patty Luna', 111111111, Decimal('509.75'), 'inactive'), (13, 'Maria Jozef', 123456789, Decimal('10000.00'), 'active'), (14, 'Linda Jones ', 987654321, Decimal('2600.00'), 'inactive'), (15, 'John McGrail', 222222222, Decimal('100.50'), 'active'), (16, 'Patty Luna', 111111111, Decimal('509.75'), 'inactive')]
127.0.0.1 - - [27/May/2023 00:42:00] "GET / HTTP/1.1" 200 -
127.0.0.1 - - [27/May/2023 00:42:47] "GET /addAccount HTTP/1.1" 200 -
127.0.0.1 - - [27/May/2023 00:42:48] "GET /addAccount HTTP/1.1" 200 -
[(1, 'Maria', 123456789, Decimal('10000.00'), 'active'), (2, 'Linda', 987654321, Decimal('2600.00'), 'inactive'), (3, 'John', 222222222, Decimal('100.50'), 'active'), (4, 'Patty', 111111111, Decimal('509.75'), 'inactive'), (5, 'Maria Jozef', 123456789, Decimal('10000.00'), 'active'), (6, 'Linda Jones ', 987654321, Decimal('2600.00'), 'inactive'), (7, 'John McGrail', 222222222, Decimal('100.50'), 'active'), (8, 'Patty Luna', 111111111, Decimal('509.75'), 'inactive'), (9, 'Maria Jozef', 123456789, Decimal('10000.00'), 'active'), (10, 'Linda Jones ', 987654321, Decimal('2600.00'), 'inactive'), (11, 'John McGrail', 222222222, Decimal('100.50'), 'active'), (12, 'Patty Luna', 111111111, Decimal('509.75'), 'inactive'), (13, 'Maria Jozef', 123456789, Decimal('10000.00'), 'active'), (14, 'Linda Jones ', 987654321, Decimal('2600.00'), 'inactive'), (15, 'John McGrail', 222222222, Decimal('100.50'), 'active'), (16, 'Patty Luna', 111111111, Decimal('509.75'), 'inactive')]
127.0.0.1 - - [27/May/2023 00:42:49] "GET / HTTP/1.1" 200 -
127.0.0.1 - - [27/May/2023 00:42:50] "GET /withdraw HTTP/1.1" 200 -
127.0.0.1 - - [27/May/2023 00:42:51] "GET /deposit HTTP/1.1" 200 -
[(1, 'Maria', 123456789, Decimal('10000.00'), 'active'), (2, 'Linda', 987654321, Decimal('2600.00'), 'inactive'), (3, 'John', 222222222, Decimal('100.50'), 'active'), (4, 'Patty', 111111111, Decimal('509.75'), 'inactive'), (5, 'Maria Jozef', 123456789, Decimal('10000.00'), 'active'), (6, 'Linda Jones ', 987654321, Decimal('2600.00'), 'inactive'), (7, 'John McGrail', 222222222, Decimal('100.50'), 'active'), (8, 'Patty Luna', 111111111, Decimal('509.75'), 'inactive'), (9, 'Maria Jozef', 123456789, Decimal('10000.00'), 'active'), (10, 'Linda Jones ', 987654321, Decimal('2600.00'), 'inactive'), (11, 'John McGrail', 222222222, Decimal('100.50'), 'active'), (12, 'Patty Luna', 111111111, Decimal('509.75'), 'inactive'), (13, 'Maria Jozef', 123456789, Decimal('10000.00'), 'active'), (14, 'Linda Jones ', 987654321, Decimal('2600.00'), 'inactive'), (15, 'John McGrail', 222222222, Decimal('100.50'), 'active'), (16, 'Patty Luna', 111111111, Decimal('509.75'), 'inactive')]
127.0.0.1 - - [27/May/2023 00:42:56] "GET / HTTP/1.1" 200 -
[(1, 'Maria', 123456789, Decimal('10000.00'), 'active'), (2, 'Linda', 987654321, Decimal('2600.00'), 'inactive'), (3, 'John', 222222222, Decimal('100.50'), 'active'), (4, 'Patty', 111111111, Decimal('509.75'), 'inactive'), (5, 'Maria Jozef', 123456789, Decimal('10000.00'), 'active'), (6, 'Linda Jones ', 987654321, Decimal('2600.00'), 'inactive'), (7, 'John McGrail', 222222222, Decimal('100.50'), 'active'), (8, 'Patty Luna', 111111111, Decimal('509.75'), 'inactive'), (9, 'Maria Jozef', 123456789, Decimal('10000.00'), 'active'), (10, 'Linda Jones ', 987654321, Decimal('2600.00'), 'inactive'), (11, 'John McGrail', 222222222, Decimal('100.50'), 'active'), (12, 'Patty Luna', 111111111, Decimal('509.75'), 'inactive'), (13, 'Maria Jozef', 123456789, Decimal('10000.00'), 'active'), (14, 'Linda Jones ', 987654321, Decimal('2600.00'), 'inactive'), (15, 'John McGrail', 222222222, Decimal('100.50'), 'active'), (16, 'Patty Luna', 111111111, Decimal('509.75'), 'inactive'), (17, 'Maria Jozef', 123456789, Decimal('10000.00'), 'active'), (18, 'Linda Jones ', 987654321, Decimal('2600.00'), 'inactive'), (19, 'John McGrail', 222222222, Decimal('100.50'), 'active'), (20, 'Patty Luna', 111111111, Decimal('509.75'), 'inactive')]
127.0.0.1 - - [27/May/2023 00:43:50] "GET / HTTP/1.1" 200 -
[(1, 'Maria', 123456789, Decimal('10000.00'), 'active'), (2, 'Linda', 987654321, Decimal('2600.00'), 'inactive'), (3, 'John', 222222222, Decimal('100.50'), 'active'), (4, 'Patty', 111111111, Decimal('509.75'), 'inactive'), (5, 'Maria Jozef', 123456789, Decimal('10000.00'), 'active'), (6, 'Linda Jones ', 987654321, Decimal('2600.00'), 'inactive'), (7, 'John McGrail', 222222222, Decimal('100.50'), 'active'), (8, 'Patty Luna', 111111111, Decimal('509.75'), 'inactive'), (9, 'Maria Jozef', 123456789, Decimal('10000.00'), 'active'), (10, 'Linda Jones ', 987654321, Decimal('2600.00'), 'inactive'), (11, 'John McGrail', 222222222, Decimal('100.50'), 'active'), (12, 'Patty Luna', 111111111, Decimal('509.75'), 'inactive'), (13, 'Maria Jozef', 123456789, Decimal('10000.00'), 'active'), (14, 'Linda Jones ', 987654321, Decimal('2600.00'), 'inactive'), (15, 'John McGrail', 222222222, Decimal('100.50'), 'active'), (16, 'Patty Luna', 111111111, Decimal('509.75'), 'inactive'), (17, 'Maria Jozef', 123456789, Decimal('10000.00'), 'active'), (18, 'Linda Jones ', 987654321, Decimal('2600.00'), 'inactive'), (19, 'John McGrail', 222222222, Decimal('100.50'), 'active'), (20, 'Patty Luna', 111111111, Decimal('509.75'), 'inactive')]
127.0.0.1 - - [27/May/2023 00:43:51] "GET / HTTP/1.1" 200 -
[(1, 'Maria', 123456789, Decimal('10000.00'), 'active'), (2, 'Linda', 987654321, Decimal('2600.00'), 'inactive'), (3, 'John', 222222222, Decimal('100.50'), 'active'), (4, 'Patty', 111111111, Decimal('509.75'), 'inactive'), (5, 'Maria Jozef', 123456789, Decimal('10000.00'), 'active'), (6, 'Linda Jones ', 987654321, Decimal('2600.00'), 'inactive'), (7, 'John McGrail', 222222222, Decimal('100.50'), 'active'), (8, 'Patty Luna', 111111111, Decimal('509.75'), 'inactive'), (9, 'Maria Jozef', 123456789, Decimal('10000.00'), 'active'), (10, 'Linda Jones ', 987654321, Decimal('2600.00'), 'inactive'), (11, 'John McGrail', 222222222, Decimal('100.50'), 'active'), (12, 'Patty Luna', 111111111, Decimal('509.75'), 'inactive'), (13, 'Maria Jozef', 123456789, Decimal('10000.00'), 'active'), (14, 'Linda Jones ', 987654321, Decimal('2600.00'), 'inactive'), (15, 'John McGrail', 222222222, Decimal('100.50'), 'active'), (16, 'Patty Luna', 111111111, Decimal('509.75'), 'inactive'), (17, 'Maria Jozef', 123456789, Decimal('10000.00'), 'active'), (18, 'Linda Jones ', 987654321, Decimal('2600.00'), 'inactive'), (19, 'John McGrail', 222222222, Decimal('100.50'), 'active'), (20, 'Patty Luna', 111111111, Decimal('509.75'), 'inactive')]
127.0.0.1 - - [27/May/2023 00:43:51] "GET / HTTP/1.1" 200 -
[(1, 'Maria', 123456789, Decimal('10000.00'), 'active'), (2, 'Linda', 987654321, Decimal('2600.00'), 'inactive'), (3, 'John', 222222222, Decimal('100.50'), 'active'), (4, 'Patty', 111111111, Decimal('509.75'), 'inactive'), (5, 'Maria Jozef', 123456789, Decimal('10000.00'), 'active'), (6, 'Linda Jones ', 987654321, Decimal('2600.00'), 'inactive'), (7, 'John McGrail', 222222222, Decimal('100.50'), 'active'), (8, 'Patty Luna', 111111111, Decimal('509.75'), 'inactive'), (9, 'Maria Jozef', 123456789, Decimal('10000.00'), 'active'), (10, 'Linda Jones ', 987654321, Decimal('2600.00'), 'inactive'), (11, 'John McGrail', 222222222, Decimal('100.50'), 'active'), (12, 'Patty Luna', 111111111, Decimal('509.75'), 'inactive'), (13, 'Maria Jozef', 123456789, Decimal('10000.00'), 'active'), (14, 'Linda Jones ', 987654321, Decimal('2600.00'), 'inactive'), (15, 'John McGrail', 222222222, Decimal('100.50'), 'active'), (16, 'Patty Luna', 111111111, Decimal('509.75'), 'inactive'), (17, 'Maria Jozef', 123456789, Decimal('10000.00'), 'active'), (18, 'Linda Jones ', 987654321, Decimal('2600.00'), 'inactive'), (19, 'John McGrail', 222222222, Decimal('100.50'), 'active'), (20, 'Patty Luna', 111111111, Decimal('509.75'), 'inactive')]
127.0.0.1 - - [27/May/2023 00:43:52] "GET / HTTP/1.1" 200 -
127.0.0.1 - - [27/May/2023 00:44:08] "GET /addAccount HTTP/1.1" 200 -
[(1, 'Maria', 123456789, Decimal('10000.00'), 'active'), (2, 'Linda', 987654321, Decimal('2600.00'), 'inactive'), (3, 'John', 222222222, Decimal('100.50'), 'active'), (4, 'Patty', 111111111, Decimal('509.75'), 'inactive'), (5, 'Maria Jozef', 123456789, Decimal('10000.00'), 'active'), (6, 'Linda Jones ', 987654321, Decimal('2600.00'), 'inactive'), (7, 'John McGrail', 222222222, Decimal('100.50'), 'active'), (8, 'Patty Luna', 111111111, Decimal('509.75'), 'inactive'), (9, 'Maria Jozef', 123456789, Decimal('10000.00'), 'active'), (10, 'Linda Jones ', 987654321, Decimal('2600.00'), 'inactive'), (11, 'John McGrail', 222222222, Decimal('100.50'), 'active'), (12, 'Patty Luna', 111111111, Decimal('509.75'), 'inactive'), (13, 'Maria Jozef', 123456789, Decimal('10000.00'), 'active'), (14, 'Linda Jones ', 987654321, Decimal('2600.00'), 'inactive'), (15, 'John McGrail', 222222222, Decimal('100.50'), 'active'), (16, 'Patty Luna', 111111111, Decimal('509.75'), 'inactive'), (17, 'Maria Jozef', 123456789, Decimal('10000.00'), 'active'), (18, 'Linda Jones ', 987654321, Decimal('2600.00'), 'inactive'), (19, 'John McGrail', 222222222, Decimal('100.50'), 'active'), (20, 'Patty Luna', 111111111, Decimal('509.75'), 'inactive')]
127.0.0.1 - - [27/May/2023 00:44:09] "GET / HTTP/1.1" 200 -
[(1, 'Maria', 123456789, Decimal('10000.00'), 'active'), (2, 'Linda', 987654321, Decimal('2600.00'), 'inactive'), (3, 'John', 222222222, Decimal('100.50'), 'active'), (4, 'Patty', 111111111, Decimal('509.75'), 'inactive'), (5, 'Maria Jozef', 123456789, Decimal('10000.00'), 'active'), (6, 'Linda Jones ', 987654321, Decimal('2600.00'), 'inactive'), (7, 'John McGrail', 222222222, Decimal('100.50'), 'active'), (8, 'Patty Luna', 111111111, Decimal('509.75'), 'inactive'), (9, 'Maria Jozef', 123456789, Decimal('10000.00'), 'active'), (10, 'Linda Jones ', 987654321, Decimal('2600.00'), 'inactive'), (11, 'John McGrail', 222222222, Decimal('100.50'), 'active'), (12, 'Patty Luna', 111111111, Decimal('509.75'), 'inactive'), (13, 'Maria Jozef', 123456789, Decimal('10000.00'), 'active'), (14, 'Linda Jones ', 987654321, Decimal('2600.00'), 'inactive'), (15, 'John McGrail', 222222222, Decimal('100.50'), 'active'), (16, 'Patty Luna', 111111111, Decimal('509.75'), 'inactive'), (17, 'Maria Jozef', 123456789, Decimal('10000.00'), 'active'), (18, 'Linda Jones ', 987654321, Decimal('2600.00'), 'inactive'), (19, 'John McGrail', 222222222, Decimal('100.50'), 'active'), (20, 'Patty Luna', 111111111, Decimal('509.75'), 'inactive')]
127.0.0.1 - - [27/May/2023 00:44:10] "GET / HTTP/1.1" 200 -
[(1, 'Maria', 123456789, Decimal('10000.00'), 'active'), (2, 'Linda', 987654321, Decimal('2600.00'), 'inactive'), (3, 'John', 222222222, Decimal('100.50'), 'active'), (4, 'Patty', 111111111, Decimal('509.75'), 'inactive'), (5, 'Maria Jozef', 123456789, Decimal('10000.00'), 'active'), (6, 'Linda Jones ', 987654321, Decimal('2600.00'), 'inactive'), (7, 'John McGrail', 222222222, Decimal('100.50'), 'active'), (8, 'Patty Luna', 111111111, Decimal('509.75'), 'inactive'), (9, 'Maria Jozef', 123456789, Decimal('10000.00'), 'active'), (10, 'Linda Jones ', 987654321, Decimal('2600.00'), 'inactive'), (11, 'John McGrail', 222222222, Decimal('100.50'), 'active'), (12, 'Patty Luna', 111111111, Decimal('509.75'), 'inactive'), (13, 'Maria Jozef', 123456789, Decimal('10000.00'), 'active'), (14, 'Linda Jones ', 987654321, Decimal('2600.00'), 'inactive'), (15, 'John McGrail', 222222222, Decimal('100.50'), 'active'), (16, 'Patty Luna', 111111111, Decimal('509.75'), 'inactive'), (17, 'Maria Jozef', 123456789, Decimal('10000.00'), 'active'), (18, 'Linda Jones ', 987654321, Decimal('2600.00'), 'inactive'), (19, 'John McGrail', 222222222, Decimal('100.50'), 'active'), (20, 'Patty Luna', 111111111, Decimal('509.75'), 'inactive')]
127.0.0.1 - - [27/May/2023 00:44:10] "GET / HTTP/1.1" 200 -
[(1, 'Maria', 123456789, Decimal('10000.00'), 'active'), (2, 'Linda', 987654321, Decimal('2600.00'), 'inactive'), (3, 'John', 222222222, Decimal('100.50'), 'active'), (4, 'Patty', 111111111, Decimal('509.75'), 'inactive'), (5, 'Maria Jozef', 123456789, Decimal('10000.00'), 'active'), (6, 'Linda Jones ', 987654321, Decimal('2600.00'), 'inactive'), (7, 'John McGrail', 222222222, Decimal('100.50'), 'active'), (8, 'Patty Luna', 111111111, Decimal('509.75'), 'inactive'), (9, 'Maria Jozef', 123456789, Decimal('10000.00'), 'active'), (10, 'Linda Jones ', 987654321, Decimal('2600.00'), 'inactive'), (11, 'John McGrail', 222222222, Decimal('100.50'), 'active'), (12, 'Patty Luna', 111111111, Decimal('509.75'), 'inactive'), (13, 'Maria Jozef', 123456789, Decimal('10000.00'), 'active'), (14, 'Linda Jones ', 987654321, Decimal('2600.00'), 'inactive'), (15, 'John McGrail', 222222222, Decimal('100.50'), 'active'), (16, 'Patty Luna', 111111111, Decimal('509.75'), 'inactive'), (17, 'Maria Jozef', 123456789, Decimal('10000.00'), 'active'), (18, 'Linda Jones ', 987654321, Decimal('2600.00'), 'inactive'), (19, 'John McGrail', 222222222, Decimal('100.50'), 'active'), (20, 'Patty Luna', 111111111, Decimal('509.75'), 'inactive')]
127.0.0.1 - - [27/May/2023 00:44:10] "GET / HTTP/1.1" 200 -
[(1, 'Maria', 123456789, Decimal('10000.00'), 'active'), (2, 'Linda', 987654321, Decimal('2600.00'), 'inactive'), (3, 'John', 222222222, Decimal('100.50'), 'active'), (4, 'Patty', 111111111, Decimal('509.75'), 'inactive'), (5, 'Maria Jozef', 123456789, Decimal('10000.00'), 'active'), (6, 'Linda Jones ', 987654321, Decimal('2600.00'), 'inactive'), (7, 'John McGrail', 222222222, Decimal('100.50'), 'active'), (8, 'Patty Luna', 111111111, Decimal('509.75'), 'inactive'), (9, 'Maria Jozef', 123456789, Decimal('10000.00'), 'active'), (10, 'Linda Jones ', 987654321, Decimal('2600.00'), 'inactive'), (11, 'John McGrail', 222222222, Decimal('100.50'), 'active'), (12, 'Patty Luna', 111111111, Decimal('509.75'), 'inactive'), (13, 'Maria Jozef', 123456789, Decimal('10000.00'), 'active'), (14, 'Linda Jones ', 987654321, Decimal('2600.00'), 'inactive'), (15, 'John McGrail', 222222222, Decimal('100.50'), 'active'), (16, 'Patty Luna', 111111111, Decimal('509.75'), 'inactive'), (17, 'Maria Jozef', 123456789, Decimal('10000.00'), 'active'), (18, 'Linda Jones ', 987654321, Decimal('2600.00'), 'inactive'), (19, 'John McGrail', 222222222, Decimal('100.50'), 'active'), (20, 'Patty Luna', 111111111, Decimal('509.75'), 'inactive')]
127.0.0.1 - - [27/May/2023 00:45:46] "GET / HTTP/1.1" 200 -
[(1, 'Maria', 123456789, Decimal('10000.00'), 'active'), (2, 'Linda', 987654321, Decimal('2600.00'), 'inactive'), (3, 'John', 222222222, Decimal('100.50'), 'active'), (4, 'Patty', 111111111, Decimal('509.75'), 'inactive'), (5, 'Maria Jozef', 123456789, Decimal('10000.00'), 'active'), (6, 'Linda Jones ', 987654321, Decimal('2600.00'), 'inactive'), (7, 'John McGrail', 222222222, Decimal('100.50'), 'active'), (8, 'Patty Luna', 111111111, Decimal('509.75'), 'inactive'), (9, 'Maria Jozef', 123456789, Decimal('10000.00'), 'active'), (10, 'Linda Jones ', 987654321, Decimal('2600.00'), 'inactive'), (11, 'John McGrail', 222222222, Decimal('100.50'), 'active'), (12, 'Patty Luna', 111111111, Decimal('509.75'), 'inactive'), (13, 'Maria Jozef', 123456789, Decimal('10000.00'), 'active'), (14, 'Linda Jones ', 987654321, Decimal('2600.00'), 'inactive'), (15, 'John McGrail', 222222222, Decimal('100.50'), 'active'), (16, 'Patty Luna', 111111111, Decimal('509.75'), 'inactive'), (17, 'Maria Jozef', 123456789, Decimal('10000.00'), 'active'), (18, 'Linda Jones ', 987654321, Decimal('2600.00'), 'inactive'), (19, 'John McGrail', 222222222, Decimal('100.50'), 'active'), (20, 'Patty Luna', 111111111, Decimal('509.75'), 'inactive')]
127.0.0.1 - - [27/May/2023 00:45:47] "GET / HTTP/1.1" 200 -

=========== RESTART: /Users/melaniemunoz/Downloads/portalDatabase.py ===========
>>> 
=========== RESTART: /Users/melaniemunoz/Downloads/portalDatabase.py ===========
>>> 
============ RESTART: /Users/melaniemunoz/Downloads/portalServer.py ============
Starting httpd on port 8000
[(1, 'Maria', 123456789, Decimal('10000.00'), 'active'), (2, 'Linda', 987654321, Decimal('2600.00'), 'inactive'), (3, 'John', 222222222, Decimal('100.50'), 'active'), (4, 'Patty', 111111111, Decimal('509.75'), 'inactive'), (5, 'Maria Jozef', 123456789, Decimal('10000.00'), 'active'), (6, 'Linda Jones ', 987654321, Decimal('2600.00'), 'inactive'), (7, 'John McGrail', 222222222, Decimal('100.50'), 'active'), (8, 'Patty Luna', 111111111, Decimal('509.75'), 'inactive'), (9, 'Maria Jozef', 123456789, Decimal('10000.00'), 'active'), (10, 'Linda Jones ', 987654321, Decimal('2600.00'), 'inactive'), (11, 'John McGrail', 222222222, Decimal('100.50'), 'active'), (12, 'Patty Luna', 111111111, Decimal('509.75'), 'inactive'), (13, 'Maria Jozef', 123456789, Decimal('10000.00'), 'active'), (14, 'Linda Jones ', 987654321, Decimal('2600.00'), 'inactive'), (15, 'John McGrail', 222222222, Decimal('100.50'), 'active'), (16, 'Patty Luna', 111111111, Decimal('509.75'), 'inactive'), (17, 'Maria Jozef', 123456789, Decimal('10000.00'), 'active'), (18, 'Linda Jones ', 987654321, Decimal('2600.00'), 'inactive'), (19, 'John McGrail', 222222222, Decimal('100.50'), 'active'), (20, 'Patty Luna', 111111111, Decimal('509.75'), 'inactive')]
127.0.0.1 - - [27/May/2023 00:50:17] "GET / HTTP/1.1" 200 -
