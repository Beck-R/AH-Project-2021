pip3 install -r requirements.txt && yarn global add pm2 && pm2 start run_flask_app.sh --app flask && pm2 start run_web.sh --app web