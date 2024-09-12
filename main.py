from website import create_app

app = create_app()

# Run the app only if this file is called
if __name__ == "__main__":
    app.run(debug=True)