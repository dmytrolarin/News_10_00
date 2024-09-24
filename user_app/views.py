import flask

def render_template():
    return flask.render_template(
        template_name_or_list= "user.html"
    )