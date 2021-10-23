# -*- coding: utf-8 -*-
"""
Created on Fri Oct 22 12:18:41 2021

@author: inesd
"""

#Se importa render_template, flash,redirect, session,url_for, request y g

from flask import render_template, flash, redirect, session, url_for, request, g

#Se importa login_user,logout_user,current_user y login_required

from flask.ext.login import login_user, logout_user, current_user, login_required


#Se importa la aplicacion app, db, lm y oid
from app import app, db, lm, oid

#De forms.py se importa LoginForm
from .forms import LoginForm

#Se importa User de models
from .models import User





#Se retorna  el usuario a partir el id de la base de datos


#la funcion se usara por parte de flask-login


@lm.user_loader


def load_user(id):


    return User.query.get(int(id))





#Se define g.user a partir del usuario actual.


#Esta funcion corre cada vez que una solicitud se realiza a


#fin de saber si el usuario hizo login y es el usuario actual


@app.before_request


def before_request():


    g.user = current_user








#Se define la pagina index por defecto y se requiere que haga login el usuario


@app.route('/')


@app.route('/index')


@login_required


def index():


    #Ahora no se usa un usuario por defecto, se comenta esa linea


    #Ahora se toma el usuario g.user el cual es el usuario actual


    user = g.user


    #user = {'usuario': 'Ernesto'}


    posts = [


      {


          'autor': {'usuario': 'John'},


          'asunto': 'Un gran dia en Edimburgo!'


      },


      {


          'autor': {'usuario': 'Jane'},


          'asunto': 'Civil War, una gran pelicula!'


      }


   ]


   return render_template('index.html',


                         title='Inicio',


                         user=user,


                         posts=posts)








#Se define login con url /login con metodos GET y POST


#Se define el manejador de login.


@app.route('/login', methods=['GET', 'POST'])


@oid.loginhandler


def login():


    #Se consulta si el usuario existe, y si esta autenticado


    #Se redrcciona a la pagina index


    if g.user is not None and g.user.is_authenticated:


        return redirect(url_for('index'))


    #Se crea una instancia de LoginForm


    form = LoginForm()


    #Se consulta si validate existe


    if form.validate_on_submit():


        #Se maneja la sesion a partir del formulario con la variable recuerdame


        session['recuerdame'] = form.recuerdame.data


        #Se returna el inicio de login y correo.


        return oid.try_login(form.openid.data, ask_for=['usuario', 'correo'])


    #Se renderiza la plantilla de login.


    return render_template('login.html',


                         title='Inicio sesion',


                         form=form,


                         providers=app.config['PROVEEDORES_OPENID'])





#Se define after_login para la llamada de flask-login


@oid.after_login


def after_login(resp):


    #Si no existe el campo correo o esta vacio


    #Se devuelve un mensaje de login invalido y se redirecciona


    #a la pagina de login


    if resp.correo is None or resp.correo == "":


        flash('Login invalido, intente de nuevo.')


        return redirect(url_for('login'))


    #Se trae los datos del usuario de la base de datos


    user = User.query.filter_by(email=resp.correo).first()


    #SI el usuario no existe


    if user is None:


        #Se trae el usuario de la resp


        usuario = resp.usuario


        #si usuario no existe o esta en blanco


        #Se toma el nombre del usuario del correo


        if usuario is None or usuario == "":


            usuario = resp.correo.split('@')[0]


        #Se agrega el usuario y correo a la base de datos.


        user = User(usuario=usuario, correo=resp.correo)


        db.session.add(user)


        db.session.commit()


    #Se define la variable recuerdame como falsa


    recuerdame = False


    #Si la variable recuerdame esta en el manejo de session


    if 'recuerdame' in session:


        #Se asigna el valor que maneja recuerdame en la sesion


        recuerdame = session['recuerdame']


        session.pop('recuerdame', None)


    #Se inicia login, pasando el usuario y la variable recuerdame


    #Se redirecciona de pagina


    login_user(user, remember=recuerdame)


    return redirect(request.args.get('next') or url_for('index'))





#Se define el fin de la sesion cuando se ve la pagina logout


#Se redirecciona a la pagina index pero primero se finaliza la session


@app.route('/logout')


def logout():


    logout_user()


    return redirect(url_for('index'))