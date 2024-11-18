from app_site import database, app
from app_site.models import Usuario, Foto

with app.app_context():
    database.create_all()