from flask import Flask
app = Flask("project")

import project.models.databaseConnect
# import project.models.employee
import project.controllers.views