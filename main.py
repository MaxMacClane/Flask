# This is a sample Python script.
# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
from flask import Flask, request
from jinja2 import Template

w = Flask(__name__)

# @w.route("/")
# def index():
#     # Use a breakpoint in the code line below to debug your script.
#     w = f'index'
#     r = f"look at me"
#     return w + ' ' + r  # Press ⌘F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.

@w.route("/")
def der():
    a = ' 10'
    name = "Tyler"
    tm = Template("Hallo {{name}}")
    msf = tm.render(name=name)
    return f"<h1> {msf}  {a} </h1>", f're'


if __name__ == '__main__':
    w.run(debug=True)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
