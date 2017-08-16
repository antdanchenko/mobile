from tests import tests_data
import time


def pytest_addoption(parser):
    parser.addoption("--build", action="store", default='build_' + time.strftime('%Y_%m_%d_%H_%M'),
                     help="Specify build name")
    parser.addoption('--repeat', action='store', default='1', help='Number of times to repeat each test')
    parser.addoption('--apk', action='store', default=None, help='Please provide url or local path to apk')


def pytest_runtest_setup(item):
    tests_data.name = item.name


def pytest_generate_tests(metafunc):
    if metafunc.config.option.repeat is not None:
        count = int(metafunc.config.option.repeat)
        metafunc.fixturenames.append('tmp_ct')
        metafunc.parametrize('tmp_ct', range(count))
