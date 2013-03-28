import sys
import os
import nose

sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)), "autoload"))

nose.main(argv=sys.argv + ["-w", "./test"])
