# coding: utf-8

from datetime import datetime
import json
import asyncio

import sanic
app = sanic.Sanic()

@app.route("/stream/json")
async def index(request):
    async def content(response):
        for i in range(10):
            response.write(json.dumps({'id': datetime.now().timestamp()}))
            await asyncio.sleep(5)
    return sanic.response.stream(content, content_type='application/octet-stream')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)

