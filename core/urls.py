from .settings import core_app

import article_app


article_app.article_app.add_url_rule(
    rule="/", 
    view_func= article_app.view_all_articles
    )

core_app.register_blueprint(blueprint = article_app.article_app )