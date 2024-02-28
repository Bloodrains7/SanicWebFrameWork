import sanic

app = sanic.Sanic(name="logginispain")


@app.route("/")
async def index(request):
    return sanic.response.text("OK!")


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8000, access_log=True, debug=True)
