from controller import *
from param import PARAM, PARAM_RESERVED

# Trivial "controller" that just turns on motors and sets pwm duty cycle.

P0 = const(2)
assert P0 == PARAM_RESERVED

PARAM_DUTY1  = const(P0+0)   # motor1 duty cycle setpoint
PARAM_DUTY2  = const(P0+1)   # motor2 duty cycle setpoint


class Control(Controller):

    def update(self):
        # set motor duty cycle
        self.state[STATE_DUTY1] = PARAM[PARAM_DUTY1]
        self.state[STATE_DUTY2] = PARAM[PARAM_DUTY2]
