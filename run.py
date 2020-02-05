
#!/usr/bin/env python
# -*- coding: utf-8 -*-

from hashcodebase.datastream import StreamHandler
from hashcodebase.solver import Solver


streamHandler = StreamHandler()
solver = Solver()

loaded_data = streamHandler.open("data/b_small.in")
result = solver.solve(loaded_data)
streamHandler.write("data/b_small_result.in", result)
