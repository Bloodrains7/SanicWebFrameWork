import sanic
from sanic.views import HTTPMethodView

app = sanic.Sanic(name="SanicWebFramework")


@app.route("/")
async def index(request):
    return sanic.response.redirect(app.url_for("ViewDemo"))


class ViewDemo(HTTPMethodView):
    async def get(self, request):
        return sanic.response.text("This with get!")

    async def post(self, request):
        return sanic.response.text("This with post!")


app.add_route(ViewDemo.as_view(), "/ViewDemo")

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8000)
