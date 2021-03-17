from extras.plugins import PluginConfig

class Crossconnect(PluginConfig):
    name="plugin_crossconnect"
    verbose_name="cross connect"
    description="Manage Cross Connect Circuit"
    version="0.1"
    author="authakarn"
    base_url="crossconnect"
    required_settings = []
    default_settings = {}

config = Crossconnect
