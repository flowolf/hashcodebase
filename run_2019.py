
#!/usr/bin/env python
# -*- coding: utf-8 -*-

from hashcodebase.datastream import StreamHandler2019
from hashcodebase.solver import Solver2019


streamHandler = StreamHandler2019()
solver = Solver2019()

loaded_data = streamHandler.open("data/b_small.in")
result = solver.solve(loaded_data)
streamHandler.write("data/b_small_result.in", result)
