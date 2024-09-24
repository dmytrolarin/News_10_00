from .settings import core_app

import article_app
import user_app

article_app.article_app.add_url_rule(
    rule="/", 
    view_func= article_app.view_all_articles
    )
user_app.user_app.add_url_rule(
    rule="/User/",
    view_func= user_app.render_template
)

core_app.register_blueprint(blueprint = article_app.article_app )
core_app.register_blueprint(blueprint= user_app.user_app)