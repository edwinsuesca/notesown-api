from flask import Blueprint, jsonify, request

# Entities
from models.entities.entiNotas import Notas
# Models
from models.NotasModel import NotasModel

main = Blueprint('nota_blueprint',  __name__)

#Buscar todos
@main.route('/') 
def get_notas():
    try:
        notas = NotasModel.get_notas()
        return jsonify(notas)
    except Exception as ex:
        return jsonify({'message': str(ex)}),500

#Buscar uno
@main.route('/<id>')
def get_nota(id):
    try:
        nota = NotasModel.get_nota(id)
        if nota != None:
            return jsonify(nota)
        else:
            return jsonify({}), 404
    except Exception as ex:
        return jsonify({'message': str(ex)}),500

# Añadir 
@main.route('/add', methods = ['POST'])
def add_nota():
    try:
        description = request.json['description']
        name = request.json['name']
        parentFolder = request.json['parentFolder']

        nota = Notas(description,name,parentFolder)

        affected_rows = NotasModel.add_nota(nota)

        if affected_rows == 1:
            return jsonify('message' f'Nota "{nota.name}" creada.')
        else:
            return jsonify({'message': "Error on insert"}), 500
        
    except Exception as ex:
        return jsonify({'mensaje': str(ex)}),500 

# Actualizar
@main.route('/update/<id>', methods = ['PUT'])
def update_nota(id):
    try:
        id = request.json['id']
        name = request.json['name']
        creationDate = request.json['creationDate']
        updateDate = request.json['updateDate']
        description = request.json['description']
        lastEditor = request.json['lastEditor']
        parentFolder = request.json['parentFolder']
        panel = request.json['panel']


        nota = Notas(id,name,creationDate,updateDate,panel,description,lastEditor,parentFolder)

        affected_rows = NotasModel.update_nota(nota)

        if affected_rows == 1:
            return jsonify(nota.id)
        else:
            return jsonify({'message': "No note updated"}), 500
        
    except Exception as ex:
        return jsonify({'message': str(ex)}),500 