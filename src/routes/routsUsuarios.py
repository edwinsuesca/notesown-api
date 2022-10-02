from flask import Blueprint, jsonify, request

# Entities
from models.entities.entiUsuarios import Usuarios
# Models
from models.UsuariosModel import UsuariosModel

main = Blueprint('usuario_blueprint',  __name__)

#Buscar todos
@main.route('/') 
def get_usuarios():
    try:
        usuarios = UsuariosModel.get_usuarios()
        return jsonify(usuarios)
    except Exception as ex:
        return jsonify({'message': str(ex)}),500

#Buscar uno
@main.route('/<id>')
def get_usuario(id):
    try:
        usuario = UsuariosModel.get_usuario(id)
        if usuario != None:
            return jsonify(usuario)
        else:
            return jsonify({}), 404
    except Exception as ex:
        return jsonify({'message': str(ex)}),500
 
# Añadir 
@main.route('/add', methods = ['POST'])
def add_usuario():
    try:
        name = request.json['name']
        lastname = request.json['lastname']
        email = request.json['email']
        passw = request.json['passw']
        img = request.json['img']
        
        usuario = Usuarios(name,lastname,email,passw,img)

        affected_rows = UsuariosModel.add_usuario(usuario)

        if affected_rows == 1:
            return jsonify(usuario.id)
        else:
            return jsonify({'message': "Error on insert"}), 500
        
    except Exception as ex:
        return jsonify({'message': str(ex)}),500 

# Actualizar
@main.route('/update/<id>', methods = ['PUT'])
def update_usuario(id):
    try:
        name = request.json['name']
        lastname = request.json['lastname']
        email = request.json['email']
        passw = request.json['passw']
        img = request.json['img']
        
        usuario = Usuarios(id,name,lastname,email,passw,img)

        affected_rows = UsuariosModel.update_usuario(usuario)

        if affected_rows == 1:
            return jsonify(usuario.id)
        else:
            return jsonify({'message': "No user updated"}), 500
        
    except Exception as ex:
        return jsonify({'message': str(ex)}),500 

#Eliminar
@main.route('/delete/<id>', methods = ['DELETE'])
def delete_usuario(id):
    try:
        usuario = Usuarios(id)

        affected_rows = UsuariosModel.delete_usuario(id)

        if affected_rows == 1:
            return jsonify(usuario.id)
        else:
            return jsonify({'message': "No user delete"}), 404
        
    except Exception as ex:
        return jsonify({'message': str(ex)}),500 