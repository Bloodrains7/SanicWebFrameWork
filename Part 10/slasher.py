import sanic

app = sanic.Sanic(name="slasher")


@app.route("/", strict_slashes=False)
async def index(request):
    return sanic.response.text("Without strict slashes!")


@app.route("/strct", strict_slashes=True)
async def strct(request):
    return sanic.response.text("WITH strict slashes!")


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8000)
