import Oslo_model as om
import numpy as np
from matplotlib import pyplot as plt

Obj = om.Oslo(256)
Obj.add_grain(60000)
A = Obj.avalanches[Obj.t_c + 1000:]
