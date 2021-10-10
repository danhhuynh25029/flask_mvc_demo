from flask import Flask
app = Flask("project")

import project.models
import project.controllers