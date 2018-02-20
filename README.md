# SampleStream

Sample server of http streaming.

## How to use.
```
docker build -t stream .
docker run -it -p 8888:8000 stream

# Open http://localhost:8888/stream/json?interval=1&limit=5
```
