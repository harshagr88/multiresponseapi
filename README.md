Note: Below installation instructions is to run the application in a POSIX type environment. To run the application on a Windows OS, source path has to be changed.

Software Requirments

* python 3.9

**Setting up Environment**

1. First unzip the project and move to project directory
2. Then you can create a new virtual environment with the command:

   ```
   $ python3 -m venv venv
   ```
3. Activate the virual environment:

   ```
   $ source venv/bin/activate
   ```
4. Install dependencies

```
$ pip install -r dependency.txt
```

**Start the application and check response**

1. Run below command to start the application

   ```
   $ python3 app.py
   ```
2. Curl command without header

   ```
   $ curl  http://localhost:8000/hello
   ```

   output:

   ```
   <p>Hello, World</p>
   ```
3. Curl command with header:

   ```
   $ curl -H "accept:application/json" http://localhost:8000/hello
   ```

output:

```
{ 
  "message": "Hello, World"
}
```

**Enable logging**

* start application with debug option

```
$ python3 app.py debug
```

* Logging sample:

2022-03-06 12:21:32,614 DEBUG app Thread-3 : [2022-Mar-06 12:21] /hello?

**Run test cases**

```
$ py.test
```

To show results press Ctrl+C
