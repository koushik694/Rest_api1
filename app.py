from tkinter.filedialog import SaveAs

from flask import Flask,jsonify
todo=Flask('__name__')
students=[
    {
        'id':1,
        'name':'Arun',
        'age':24,
     },
    {
        'id':2,
        'name':'Bean',
        'age':25,
    }
]


@todo.route('/students-list')
def get_students_list():
    return jsonify (students)
@todo.route('/students/get/<int:id>')
def get_students_by_id(id):
    print(id)
    for std in students:
        if std['id'] == id:
            return jsonify(std)
    print(std)
    return jsonify('not found')

if __name__ == '__main__':
    todo.run(
        debug=True
    )
