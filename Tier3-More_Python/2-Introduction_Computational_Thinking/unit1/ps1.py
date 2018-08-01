###########################
# 6.00.2x Problem Set 1: Space Cows

from ps1_partition import get_partitions
import time

#================================
# Part A: Transporting Space Cows
#================================

def load_cows(filename):
    """
    Read the contents of the given file.  Assumes the file contents contain
    data in the form of comma-separated cow name, weight pairs, and return a
    dictionary containing cow names as keys and corresponding weights as values.

    Parameters:
    filename - the name of the data file as a string

    Returns:
    a dictionary of cow name (string), weight (int) pairs
    """

    cow_dict = dict()

    f = open(filename, 'r')

    for line in f:
        line_data = line.split(',')
        cow_dict[line_data[0]] = int(line_data[1])
    return cow_dict


# Problem 1
def greedy_cow_transport(cows, limit=10, verbose=False):
    """
    Uses a greedy heuristic to determine an allocation of cows that attempts to
    minimize the number of spaceship trips needed to transport all the cows. The
    returned allocation of cows may or may not be optimal.
    The greedy heuristic should follow the following method:

    1. As long as the current trip can fit another cow, add the largest cow that will fit
        to the trip
    2. Once the trip is full, begin a new trip to transport the remaining cows

    Does not mutate the given dictionary of cows.

    Parameters:
    cows - a dictionary of name (string), weight (int) pairs
    limit - weight limit of the spaceship (an int)
    verbose - show the process

    Returns:
    A list of lists, with each inner list containing the names of cows
    transported on a particular trip and the overall list containing all the
    trips
    """
    # TODO: Your code here
    cows_aboard = sorted(cows, key=cows.get)
    trips = []
    while len(cows_aboard) > 0:
        trip = []
        trip_weight = 0
        id = len(cows_aboard) - 1
        while trip_weight < limit and id >= 0:
            if verbose:
                print("{}: {} + {} < {}".format(cows_aboard[id], trip_weight,
                                                cows[cows_aboard[id]], limit))
            if trip_weight + cows[cows_aboard[id]] <= limit:
                trip.append(cows_aboard[id])
                trip_weight += cows[cows_aboard[id]]
                del cows_aboard[id]
            id -= 1
        if verbose:
            print(trip)
        trips.append(trip)
    return trips


# Problem 2
def brute_force_cow_transport(cows, limit=10, verbose=False):
    """
    Finds the allocation of cows that minimizes the number of spaceship trips
    via brute force.  The brute force algorithm should follow the following method:

    1. Enumerate all possible ways that the cows can be divided into separate trips
    2. Select the allocation that minimizes the number of trips without making any trip
        that does not obey the weight limitation

    Does not mutate the given dictionary of cows.

    Parameters:
    cows - a dictionary of name (string), weight (int) pairs
    limit - weight limit of the spaceship (an int)

    Returns:
    A list of lists, with each inner list containing the names of cows
    transported on a particular trip and the overall list containing all the
    trips
    """
    best_trips = None
    for trips in get_partitions(cows):
        isValid = True
        for trip in trips:
            trip_weight = 0
            if verbose:
                print(trip, end="")
            for cow in trip:
                trip_weight += cows[cow]
            if trip_weight > limit:
                isValid = False
                if verbose:
                    print("->INVALID. next.")
                break
            elif verbose:
                print("->VALID, continuing...", end="\n")
        if isValid and (best_trips is None or len(trips) < len(best_trips)):
            best_trips = trips
        if verbose:
            print("BEST: {}".format(best_trips))
    return best_trips


# Problem 3
def compare_cow_transport_algorithms():
    """
    Using the data from ps1_cow_data.txt and the specified weight limit, run your
    greedy_cow_transport and brute_force_cow_transport functions here. Use the
    default weight limits of 10 for both greedy_cow_transport and
    brute_force_cow_transport.

    Print out the number of trips returned by each method, and how long each
    method takes to run in seconds.

    Returns:
    Does not return anything.
    """
    # TODO: Your code here
    cows = load_cows("ps1_cow_data.txt")
    limit = 10
    print(cows)

    start = time.time()
    greedy = greedy_cow_transport(cows, limit)
    end = time.time()
    print("Greedy:\n---\n\tNb of trips: {}\n\tDuration: {}"
          .format(len(greedy), end - start))

    start = time.time()
    brute = brute_force_cow_transport(cows, limit)
    end = time.time()
    print("Brute Force:\n---\n\tNb of trips: {}\n\tDuration: {}"
          .format(len(brute), end - start))


"""
Here is some test data for you to see the results of your algorithms with.
Do not submit this along with any of your answers. Uncomment the last two
lines to print the result of your problem.
"""

cows = load_cows("ps1_cow_data.txt")
limit = 10
print(cows)

print(greedy_cow_transport(cows, limit))
print(brute_force_cow_transport(cows, limit))
compare_cow_transport_algorithms()
