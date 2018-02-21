# SampleStream

Sample server of http streaming.

## How to use.
```
docker build -t stream .
docker run -it -p 8888:8000 stream

# Open http://localhost:8888/stream/json?interval=1&limit=5
```

## Parameter

* interval
    * stream output interval [sec]. default=5
* count
    * How many times dose server sent requests.
* template
    * Output template. `$count`, `$ts` is available.
