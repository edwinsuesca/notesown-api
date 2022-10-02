from flask import Blueprint, jsonify, request

# Entities
from models.entities.entiCarpetas import Carpetas
# Models
from models.CarpetasModel import CarpetasModel

main = Blueprint('carpeta_blueprint',  __name__)

#Buscar todos
@main.route('/') 
def get_carpetas():
    try:
        carpetas = CarpetasModel.get_carpetas()
        return jsonify(carpetas)
    except Exception as ex:
        return jsonify({'message': str(ex)}),500

#Buscar uno
@main.route('/<id>')
def get_carpeta(id):
    try:
        carpeta = CarpetasModel.get_carpeta(id)
        if carpeta != None:
            return jsonify(carpeta)
        else:
            return jsonify({}), 404
    except Exception as ex:
        return jsonify({'message': str(ex)}),500
 
# Añadir 
@main.route('/add', methods = ['POST'])
def add_carpeta():
    try:
        name = request.json['name']
        carpeta = Carpetas(name)
        print(carpeta)
        affected_rows = CarpetasModel.add_carpeta(carpeta)

        if affected_rows == 1:
            return jsonify('message' f'Carpeta "{carpeta.name}" creada.')
        else:
            return jsonify({'message': "Error on insert"}), 500
        
    except Exception as ex:
        return jsonify({'mensaje': str(ex)}),500 

# Actualizar
@main.route('/update/<id>', methods = ['PUT'])
def update_carpeta(id):
    try:
        id = request.json['id']
        name = request.json['name']
        creationDate = request.json['creationDate']
        updateDate = request.json['updateDate']
        panel = request.json['panel']
        
        carpeta = Carpetas(id,name,creationDate,updateDate,panel)

        affected_rows = CarpetasModel.update_carpeta(carpeta)

        if affected_rows == 1:
            return jsonify(carpeta.id)
        else:
            return jsonify({'message': "No folder updated"}), 500
        
    except Exception as ex:
        return jsonify({'message': str(ex)}),500 

#Eliminar
@main.route('/delete/<id>', methods = ['DELETE'])
def delete_carpeta(id):
    try:
        carpeta = Carpetas(id)

        affected_rows = CarpetasModel.delete_carpeta(id)

        if affected_rows == 1:
            return jsonify(carpeta.id)
        else:
            return jsonify({'message': "No folder delete"}), 404
        
    except Exception as ex:
        return jsonify({'message': str(ex)}),500 