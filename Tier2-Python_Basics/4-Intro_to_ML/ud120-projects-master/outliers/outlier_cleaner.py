#!/usr/bin/python
from operator import itemgetter
import math


def outlierCleaner(predictions, ages, net_worths):
    """
        Clean away the 10% of points that have the largest
        residual errors (difference between the prediction
        and the actual net worth).

        Return a list of tuples named cleaned_data where
        each tuple is of the form (age, net_worth, error).
    """

    cleaned_data = []

    # Make a list of the form (age, net_worth, error).
    for i, age in enumerate(ages):
        error = abs(predictions[i] - net_worths[i])
        cleaned_data.append((age, net_worths[i], error))

    # Only keep the 90% values with the lowest errors.
    cleaned_data.sort(key=itemgetter(2))
    nb_final_datum = math.ceil(0.9 * len(cleaned_data))
    cleaned_data = cleaned_data[:nb_final_datum]

    return cleaned_data
