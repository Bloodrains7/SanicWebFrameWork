import sanic
from sanic import Blueprint

bp_version1 = Blueprint('version1', url_prefix='/v1')
bp_version2 = Blueprint('version2', url_prefix='/v2')

app = sanic.Sanic(name='SanicBlueprint')
app.blueprint(bp_version1)
app.blueprint(bp_version2)


@bp_version1.route('/generate')
async def generate(request):
    return sanic.response.text('OK from version 1')


@bp_version2.route('/generate')
async def generate(request):
    return sanic.response.text('OK from version 2')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
