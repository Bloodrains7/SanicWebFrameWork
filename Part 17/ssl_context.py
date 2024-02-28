import ssl
import sanic

app = sanic.Sanic(name="SanicWebFramework")

context = ssl.create_default_context(purpose=ssl.Purpose.SERVER_AUTH)
context.load_cert_chain(r'', keyfile=r'')


@app.route("/")
async def index(request):
    return sanic.response.text("OK!")


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=443, ssl=context)
