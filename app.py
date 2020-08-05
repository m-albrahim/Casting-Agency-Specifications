import os
from flask import Flask, request, abort, jsonify, abort
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from sqlalchemy import exc
import json
import sys

from models import setup_db, Movie, Actor
from auth import AuthError, requires_auth


def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__)
    setup_db(app)

    cors = CORS(app, resources={r'*': {"origins": "*"}})

    @app.after_request
    def after_request(response):
        response.headers.add('Access-Control-Allow-Headers',
                             'Content-Type, Authorization, true')
        response.headers.add('Access-Control-Allow-Methods',
                             'GET, PPOST, PATCH, DELETE, OPTION')
        response.headers.add('Access-Control-Allow-Credentials', 'true')
        return response

    @app.route('/movies', methods=['GET'])
    @requires_auth('get:movies')
    def get_movies(payload):
        movies = Movie.query.all()
        formatted_movies = [movie.format() for movie in movies]

        if (len(movies) == 0):
            abort(404)

        return jsonify({
            'success': True,
            'movies': formatted_movies
        })

    @app.route('/actors', methods=['GET'])
    @requires_auth('get:actors')
    def get_actors(payload):
        actors = Actor.query.all()
        formatted_actors = [actor.format() for actor in actors]

        if (len(actors) == 0):
            abort(404)

        return jsonify({
            'success': True,
            'actors': formatted_actors
        })

    @app.route('/movies/<int:movie_id>', methods=['DELETE'])
    @requires_auth('delete:movies')
    def delete_movie(payload, movie_id):
        try:
            movie = Movie.query.filter(Movie.id == movie_id).one_or_none()

            if movie is None:
                abort(404)

            movie.delete()

            return jsonify({
                'success': True,
                'deleted': movie_id,
                'total_movies': len(Movie.query.all())
            })

        except Exception:
            print(sys.exc_info())
            abort(422)

    @app.route('/actors/<int:actor_id>', methods=['DELETE'])
    @requires_auth('delete:actors')
    def delete_actor(payload, actor_id):
        try:
            actor = Actor.query.filter(Actor.id == actor_id).one_or_none()

            if actor is None:
                abort(404)

            actor.delete()

            return jsonify({
                'success': True,
                'deleted': actor_id,
                'total_actors': len(Actor.query.all())
            })

        except Exception:
            print(sys.exc_info())
            abort(422)

    @app.route('/movies', methods=['POST'])
    @requires_auth('post:movies')
    def create_movies(payload):
        try:
            body = request.get_json()

            if not ('title' in body and
                    'release_date' in body):
                abort(422)

            title = body.get('title', None)
            release_date = body.get('release_date', None)

            movie = Movie(title=title, release_date=release_date)
            movie.insert()

            return jsonify({
                'success': True,
                'created': movie.id,
                'total_movies': len(Movie.query.all())
            })
        except Exception:
            print(sys.exc_info())
            abort(422)

    @app.route('/actors', methods=['POST'])
    @requires_auth('post:actors')
    def create_actors(payload):
        try:
            body = request.get_json()

            if not ('name' in body and
                    'age' in body and
                    'gender' in body):
                abort(422)

            name = body.get('name', None)
            age = body.get('age', None)
            gender = body.get('gender', None)

            actor = Actor(name=name, age=age, gender=gender)
            actor.insert()

            return jsonify({
                'success': True,
                'created': actor.id,
                'total_actors': len(Actor.query.all())
            })
        except Exception:
            print(sys.exc_info())
            abort(422)

    @app.route('/movies/<int:movie_id>', methods=['PATCH'])
    @requires_auth('patch:movies')
    def update_movies(payload, movie_id):
        try:
            movie = Movie.query.filter(Movie.id == movie_id).one_or_none()

            if movie is None:
                abort(404)

            body = request.get_json()

            if not ('title' in body and
                    'release_date' in body):
                abort(422)

            movie.title = body.get('title', None)
            movie.release_date = body.get('release_date', None)

            movie.update()

            return jsonify({
                'success': True,
                'updated': movie.id,
                'total_movies': len(Movie.query.all())
            })
        except Exception:
            print(sys.exc_info())
            abort(422)

    @app.route('/actors/<int:actor_id>', methods=['PATCH'])
    @requires_auth('patch:actors')
    def update_actors(payload, actor_id):
        try:
            actor = Actor.query.filter(Actor.id == actor_id).one_or_none()

            if actor is None:
                abort(404)

            body = request.get_json()

            if not ('name' in body and
                    'age' in body and
                    'gender' in body):
                abort(422)

            actor.name = body.get('name', None)
            actor.age = body.get('age', None)
            actor.gender = body.get('gender', None)

            actor.update()

            return jsonify({
                'success': True,
                'updated': actor.id,
                'total_actors': len(Actor.query.all())
            })
        except Exception:
            print(sys.exc_info())
            abort(422)

    @app.errorhandler(404)
    def not_found(error):
        return jsonify({
            'success': False,
            'error': 404,
            'message': 'Resource not found'
        }), 404

    @app.errorhandler(422)
    def unprocessable(error):
        return jsonify({
            'success': False,
            'error': 422,
            'message': 'unprocessable'
        }), 422

    @app.errorhandler(400)
    def bad_request(error):
        return jsonify({
            'success': False,
            'error': 400,
            'message': 'bad request'
        }), 400

    @app.errorhandler(401)
    def method_not_allowed(error):
        return jsonify({
            'success': False,
            'error': 401,
            'message': 'method not allowed'
        }), 401

    @app.errorhandler(AuthError)
    def auth_error(e):
        return jsonify(e.error), e.status_code

    return app


app = create_app()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)
