import ckan.plugins as plugins
import ckan.plugins.toolkit as toolkit


class SvvLayoutPlugin(plugins.SingletonPlugin):
    plugins.implements(plugins.IConfigurer)

    def update_config(self, config_):
        toolkit.add_template_directory(config_, 'templates')
        toolkit.add_public_directory(config_, 'public')
