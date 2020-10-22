import os
import time
from conans.model.ref import ConanFileReference

from conan_app_launcher.conan import get_conan_package_folder, ConanWorker

from conan_app_launcher.config_file import parse_config_file
from PyQt5 import QtCore


def testConanApi():
    ref = "m4_installer/1.4.18@bincrafters/stable"
    os.system("conan remove %s -f" % ref)
    # Gets package path / installs the package
    package_folder = get_conan_package_folder(ConanFileReference.loads(ref))
    assert (package_folder / "bin").is_dir()
    # check again for already installed package
    package_folder = get_conan_package_folder(ConanFileReference.loads(ref))
    assert (package_folder / "bin").is_dir()


class DummySignal():

    def emit(self):
        pass


def testConanWorker(base_fixture):
    sig = DummySignal()
    tab_info = parse_config_file(base_fixture.testdata_path / "app_config.json")
    conan_worker = ConanWorker(tab_info, sig)
    elements_before = conan_worker._app_queue.qsize()
    time.sleep(8)

    assert conan_worker._app_queue.qsize() < elements_before
    conan_worker.finish_working()
