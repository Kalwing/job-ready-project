# Notes

* **Binary classification** problem -> *Dense* with 1 output and a *sigmoid* activation (Theoutput being between 0 and 1 represent the probability of the choice)
* Loss for sigmoid on a binary classification problem : **binary_crossentropy**
* **rmsprop** optimizer is good enough for everything
* If you try to classify among **N classes** the last layer should be a *Dense* one of size *N*
* **Multiclass classification** problem should end  with a **softmax** activation
* Loss for Multiclass classification should be **categorical crossentropy**
* Avoid bottleneck in your models (too small intermediate layers)
* Loss for regression is often **Mean Squared Error**
* We don't use accuracy to evaluate regression, prefer **Mean Absolute Error**
* Reduce Overfitting :
    * Get more training data
    * Reduce the capacity of the Network (less layer/parameter)
    * Add weight regularization
    * Add dropout


# Experiments

## 3.4.6

It seems that using a single layers is slightly better than using 2, and using three slightly worse.
It seems that with layers containing many units, the performance goes down at each epoch and faster.
