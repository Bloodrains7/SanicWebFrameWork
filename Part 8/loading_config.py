import sanic

app = sanic.Sanic(name="SanicWebFramework")

app.config.from_envvar("MY_CONFIG")


@app.route("/<parameter>")
async def index(request, parameter):
    return sanic.response.text("The value of parameter: {}, is {}!".format(parameter, app.config.get(parameter)))


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8000)
