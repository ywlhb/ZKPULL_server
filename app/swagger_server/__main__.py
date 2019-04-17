#!/usr/bin/env python3

import connexion
from .encoder import JSONEncoder

if __name__ == '__main__':
    app = connexion.App(__name__, specification_dir='./swagger/')
    app.app.json_encoder = JSONEncoder
    app.add_api('swagger.yaml', arguments={'title': '中控门禁控制器通讯服务API说明.'})
    app.run(port=9080)
