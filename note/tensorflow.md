# install tensorflow on python3.8 on ubuntu18.04

```bash
    python3.8 -m venv ai
    source ai/bin/activate
    pip install numpy scipy --only-binary=:all:
    (download tensorflow whl from official website)
    mv tensorflow*.whl tensorflow-2.8.0-py3-none-any.whl
    pip install tensorflow*.whl
```
DONE
