# coding: utf-8

from datetime import datetime
import json
import asyncio

import sanic

app = sanic.Sanic()

@app.route("/stream/json")
async def json_stream(request):
    async def content(response):
        limit = request.args.get('limit', None)
        if limit:
            limit = int(limit)
        interval = int(request.args.get('interval', '5'))
        count = 0
        while True:
            count += 1
            response.write(json.dumps({'id': count, 'ts': int(datetime.now().timestamp())}))
            response.write('\n')
            if limit and limit <= count:
                break
            await asyncio.sleep(interval)
    return sanic.response.stream(content, content_type='text/plain')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)

