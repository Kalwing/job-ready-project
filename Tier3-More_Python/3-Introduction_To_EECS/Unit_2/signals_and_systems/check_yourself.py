"""
I will not use the library so it might not work exactly as intended
"""
import sys
sys.path.append('../../')
from lib import SM

class Vending(SM):
    """
    Define a state machine for a vending machine.
    * The vending machine has an unlimited number of sodas that it sells for 75 cents apiece.
    * The user can deposit quarters in the machine.
    * If the user presses the cancel button, all the coins she's put in so far are returned.
    * If the user presses the dispense button,
        * If she had not deposited at least 75 cents, she gets no soda and no change.
        * If she had deposited 75 cents or more, she gets a soda and any amount over 75
    cents that she has deposited.

    More concretely,
    * The input for the machine is one of:
        * 'quarter' (25 cents) indicates that a coin has been deposited
        * 'cancel' indicates that the user wants her money back
        * 'dispense' indicates that the user wants a soda
    The output of the machine is:
     (change, soda)
    where:
    * change is an integer that indicates (in cents) the amount of change (possibly 0)
    that is returned
    * soda is a boolean that indicates whether or not the machine will dispense a soda
    For example:
    Vending().transduce(['dispense', 'quarter', 'quarter', 'quarter', 'quarter',
                         'dispense', 'quarter', 'cancel', 'dispense'])
    would return:
    [(0, False), (0, False), (0, False), (0, False), (0, False),
    (25, True), (0, False), (25, False), (0, False)]
    """
    SODA_PRICE = 75
    QUARTER_VALUE = 25

    INPUT_QUARTER = 'quarter'
    INPUT_CANCEL = 'cancel'
    INPUT_DISPENSE = 'dispense'

    start_state = 0 # No money inside the machine at first

    def getNextValues(self, state, input):
        """
        Return a tuple as so (state, output).
        """
        if input == self.INPUT_QUARTER:
            return (self.state + self.QUARTER_VALUE, (0, False))

        elif input == self.INPUT_CANCEL:
            return (0, (self.state, False))

        elif input == self.INPUT_DISPENSE:
            if self.state < self.SODA_PRICE:
                return (self.state, (0, False))
            else:
                return (0, (self.state - self.SODA_PRICE, True))

print(Vending().transduce(['dispense', 'quarter', 'quarter', 'quarter',
                           'quarter', 'dispense', 'quarter', 'cancel',
                           'dispense']))
