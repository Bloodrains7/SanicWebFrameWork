import sanic

app = sanic.Sanic(name="request_parameters")


@app.route("/forum/<page_id>")
async def forum_page(request, page_id):
    return sanic.response.text("You hit the {} page of the forum!".format(page_id))


@app.route("/forum/<page_id:int>")
async def forum_page_with_int(request, page_id):
    return sanic.response.text("You hit the {} page of the forum with integer!".format(page_id))


@app.route("/forum/<page_id:float>")
async def forum_page_with_float(request, page_id):
    return sanic.response.text("You hit the {} page of the forum with float or int!".format(page_id))


@app.route("/forum/<page_name:[a-z+]>")
async def forum_page_name(request, page_name):
    return sanic.response.text("You hit the {} name of the forum!".format(page_name))


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8000)
