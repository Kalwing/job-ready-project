# Answers
## 3.1.1
1. I took the liberty of moving some line a cell forward, as after thinking about a LOT, I think it doesn't make sense the way it is presented (Maybe it's because of the conversion to pdf.).
```python
sm1 = Delay(1)
sm2 = Delay(2)
c = sm.Cascade(sm1, sm2)
c.transduce([3,5,7,9])
```

|          |t=0|t=1|t=2|t=3|t=4|
|----------|---|---|---|---|---|
|sm1 input |   |3  |5  |7  |9  |
|sm1 state |1  |3  |5  |7  |9  |
|sm1 output|   |1  |3  |5  |7  |
|sm2 input |   |1  |3  |5  |7  |
|sm2 state |2  |1  |3  |5  |7  |
|sm2 output|   |2  |1  |3  |5  |

2.
```python
sm1 = Delay(1)
sm2 = Increment(3)
c = sm.Cascade(sm1, sm2)
c.transduce([3,5,7,9])
```

|          |t=0|t=1|t=2|t=3|t=4|
|----------|---|---|---|---|---|
|sm1 input |   |3  |5  |7  |9  |
|sm1 state |1  |3  |5  |7  |9  |
|sm1 output|   |1  |3  |5  |7  |
|sm2 input |   |1  |3  |5  |7  |
|sm2 state |0  |3  |6  |9  |12 |
|sm2 output|   |3  |6  |9  |12 |

## 3.1.2
See [3.1.2.py](./3.1.2.py)

## 3.1.3
See [3.1.3.py](./3.1.3.py)
