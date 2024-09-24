import flask

forum_app = flask.Blueprint(
    name='forum',
    import_name='forum_app',
    template_folder='templates'
)