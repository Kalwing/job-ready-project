#!/usr/bin/python

"""
    Starter code for exploring the Enron dataset (emails + finances);
    loads up the dataset (pickled dict of dicts).

    The dataset has the form:
    enron_data["LASTNAME FIRSTNAME MIDDLEINITIAL"] = { features_dict }

    {features_dict} is a dictionary of features associated with that person.
    You should explore features_dict as part of the mini-project,
    but here's an example to get you started:

    enron_data["SKILLING JEFFREY K"]["bonus"] = 5600000

"""
"""
{'salary': 274975, 'to_messages': 873, 'deferral_payments': 'NaN',
'total_payments': 1272284, 'loan_advances': 'NaN', 'bonus': 600000,
'email_address': 'ben.glisan@enron.com', 'restricted_stock_deferred': 'NaN',
'deferred_income': 'NaN', 'total_stock_value': 778546, 'expenses': 125978,
'from_poi_to_this_person': 52, 'exercised_stock_options': 384728,
'from_messages': 16, 'other': 200308, 'from_this_person_to_poi': 6,
'poi': True, 'long_term_incentive': 71023, 'shared_receipt_with_poi': 874,
'restricted_stock': 393818, 'director_fees': 'NaN'}
"""
import pickle
import random

with open("../final_project/final_project_dataset.pkl", "rb") as fin:
    enron_data = pickle.load(fin)
    poi = [person for person, features in enron_data.items()
           if features['poi'] == 1]
    print("PoI in dataset: {}".format(len(poi)))
    with open("../final_project/poi_names.txt", "r") as poi_names_in:
        LEN_BEGINNING = 2
        nb_poi = len(poi_names_in.readlines()) - LEN_BEGINNING
        print("Total Number of PoI: {}".format(nb_poi))

    print("Total Value of the stocks of James Prentice: {}"
          .format(enron_data['PRENTICE JAMES']['total_stock_value']))
    print("Message from Wesley Colwell to a POI: {}"
          .format(enron_data['COLWELL WESLEY']['from_this_person_to_poi']))
    print("Value of stock options exercised by Jeffrey K Skilling: {}"
          .format(enron_data['SKILLING JEFFREY K']['exercised_stock_options']))

    importants = [('SKILLING JEFFREY K', enron_data['SKILLING JEFFREY K']),
                  ('LAY KENNETH L', enron_data['LAY KENNETH L']),
                  ('FASTOW ANDREW S', enron_data['FASTOW ANDREW S'])]
    importants.sort(key=lambda p: p[1]["total_payments"], reverse=True)
    print("Took home the most money: {} took {}"
          .format(importants[0][0], importants[0][1]["total_payments"]))

    print("People with a quantified salary: {}"
          .format(len([person for person, features in enron_data.items()
                       if features['salary'] != 'NaN'])))
    print("People with an email: {}"
          .format(len([person for person, features in enron_data.items()
                       if features['email_address'] != 'NaN'])))

    no_total_payments = len([person for person, features in enron_data.items()
                             if features['total_payments'] == 'NaN'])
    print("People with NaN total_payments: {}"
          .format(no_total_payments / len(enron_data) * 100))

    poi_no_total_payments = len(
                                [person for person, features
                                 in enron_data.items()
                                 if features['total_payments'] == 'NaN'
                                    and features['poi'] is True])
    print("POI with NaN total_payments: {}"
          .format(poi_no_total_payments / len(enron_data) * 100))

    print("If we add 10 PoI: \n\tNb of people: {}\n\t...With NaN payments: {}"
          .format(len(enron_data)+10, no_total_payments+10))
    print("\tNb of Poi: {}\n\t...With NaN payments: {}"
          .format(len(poi)+10, poi_no_total_payments+10))
