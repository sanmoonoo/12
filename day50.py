from flask import  Flask
import congfig


app = Flask(__name__)
#加载配置文件
app.config.from_object(congfig)

if __name__ == '__main__':

    app.run()