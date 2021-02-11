from app import app

if __name__ == "__main__":
    HOST = '0.0.0.0'
    PORT = 8080
    app.run(host=HOST, port=PORT)