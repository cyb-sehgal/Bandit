import os

def insecure_function(password):
    os.system("echo 'Password received: {}'".format(password))

def password_in_source_code(password):
    print("Your password is: {}".format(password))

def sql_injection(username):
    query = "SELECT * FROM users WHERE username='%s'" % username
    # This is vulnerable to SQL Injection

def weak_hash(password):
    import hashlib
    hashed = hashlib.md5(password.encode()).hexdigest()
    return hashed

def insecure_random():
    import random
    return random.random()

def pickling_unsafe(obj):
    import pickle
    return pickle.dumps(obj)

def unsafe_eval(user_input):
    result = eval(user_input)
    return result

def insecure_deserialization(serialized_obj):
    import pickle
    return pickle.loads(serialized_obj)

def insecure_permissions(path):
    import os
    os.chmod(path, 777)

def hardcoded_credentials(username, password):
    if username == 'admin' and password == 'password123':
        print("Login successful!")
    else:
        print("Login failed")

def insecure_ssl():
    import requests
    requests.get('https://insecure-website.com', verify=False)

def unsafe_redirect(redirect_url):
    import webbrowser
    webbrowser.open(redirect_url)

def unsafe_modules(module_name):
    import importlib
    module = importlib.import_module(module_name)
    module.sensitive_function()

if __name__ == "__main__":
    password = "supersecret"
    insecure_function(password)
    password_in_source_code(password)
    sql_injection("admin")
    hashed_password = weak_hash(password)
    print("Weak hashed password:", hashed_password)
    print("Random number:", insecure_random())
    pickled_data = pickling_unsafe({"key": "value"})
    print("Pickled data:", pickled_data)
    print("Eval result:", unsafe_eval("__import__('os').system('echo Hello, World!')"))
    insecure_permissions("/path/to/file.txt")
    hardcoded_credentials("admin", "password123")
    insecure_ssl()
    unsafe_redirect("https://google.com")
    unsafe_modules("sensitive_module")
