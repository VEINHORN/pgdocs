"""
Generate docs 
"""

from jinja2 import Template
import subprocess


def generate(host, port, database):
    # read config template
    with open("bin/schemaspy-template.properties", "r") as inpfile:
        template = Template(inpfile.read())
        rendered_config = template.render(
            host=host, port=port, database=database)

        # write to file rendered config file
        with open("bin/schemaspy.properties", "w") as outfile:
            outfile.write(rendered_config)

    with open("schemaspy.log", "w") as outfile:
        subprocess.call(["java", "-jar", "bin/schemaspy-6.0.0.jar",
                         "-configFile", "bin/schemaspy.properties"], stdout=outfile)
