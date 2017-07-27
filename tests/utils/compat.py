try:
    from unittest2 import TestCase
    from unittest2 import skipIf
except ImportError:
    from unittest import TestCase  # noqa
    from unittest import skipIf  # noqa
