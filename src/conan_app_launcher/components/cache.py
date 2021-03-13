import json
import os
from pathlib import Path
from typing import Dict, List, Optional

from conan_app_launcher.base import Logger
from conans.model.ref import ConanFileReference

try:
    from typing import TypedDict
except ImportError:
    from typing_extensions import TypedDict


class ConanInfoCache():
    """
    This is a cache to accelerate calls which need Remote access.
    It also has an option to store the local package path.
    """

    def __init__(self, cache_file: Path):
        self._cache_file = cache_file
        self._local_packages: Dict[str, str] = {}
        self._remote_packages: Dict[str, List[str]] = {}
        self._read_only = False  # for testing purposes

        # create cache file, if it does not exist
        if not self._cache_file.exists():
            self._cache_file.open('a').close()
            return

        # read cached info
        self._read()

    def get_local_package_path(self, conan_ref: ConanFileReference) -> Path:
        """ Return cached package path of a locally installed package. """
        conan_ref_str = str(conan_ref)
        pkg_path_str = self._local_packages.get(conan_ref_str, "")
        if not pkg_path_str:
            pkg_path = Path("NULL")
        else:
            pkg_path = Path(pkg_path_str)

        # validate own cache - remove element if path does not exist
        if not pkg_path.exists() and conan_ref_str in self._local_packages.keys():
            self._local_packages.pop(conan_ref_str)
        return pkg_path

    def get_remote_pkg_refs(self, name: str, user: str) -> List[ConanFileReference]:
        """ Return cached info on available conan refs from  the same ref name and user. """
        refs: List[ConanFileReference] = []
        version_channels = self._remote_packages.get(f"{name}@{user}", [])
        for version_channel in version_channels:
            version, channel = version_channel.split("/")
            refs.append(ConanFileReference(name, version, user, channel))
        return refs

    def search_in_remote_refs(self, query: str) -> List[ConanFileReference]:
        """ Return cached info on available conan refs from a query """
        refs: List[ConanFileReference] = []
        for key in self._remote_packages.keys():
            if query in key:
                name, user = key.split("@")
                refs += self.get_remote_pkg_refs(name, user)
        return list(set(refs))

    def update_local_package_path(self, conan_ref: ConanFileReference, folder: Path):
        """ Update the cache with the path of a local package path. """
        self._local_packages.update({str(conan_ref): str(folder)})
        self._write()

    def update_remote_package_list(self, remote_packages=List[ConanFileReference], invalidate=False):
        """ 
        Update the cache with the info of several remote packages. 
        Invalidate option clears the cache.
        """
        if invalidate:  # clear cache
            self._remote_packages.clear()
            self._write()
        for ref in remote_packages:
            current_name_user = f"{ref.name}@{ref.user}"
            current_version_channel = f"{ref.version}/{ref.channel}"
            version_channels = set(self._remote_packages.get(current_name_user, []))
            if not current_version_channel in version_channels:
                version_channels.add(current_version_channel)
                version_channels_list = list(version_channels)
                self._remote_packages.update({current_name_user: version_channels_list})

        self._write()

    def _read(self):
        """ Laod the cache. """
        json_data = {}
        try:
            with open(self._cache_file, "r") as json_file:
                content = json_file.read()
                if len(content) > 0:
                    json_data = json.loads(content)
        except:  # possibly corrupt, delete cache file
            Logger().debug("Can't read speedup-cache file, deleting it.")
            os.remove(self._cache_file)
            # create file anew
            self._cache_file.open('a').close()
            return
        self._local_packages = json_data.get("local_packages", {})
        self._remote_packages = json_data.get("remote_packages", {})
        self._read_only = json_data.get("read_only", False)

    def _write(self):
        """ Write the cache to file. """
        if self._read_only:
            return
        json_data = {}
        json_data["read_only"] = self._read_only
        json_data["remote_packages"] = self._remote_packages
        json_data["local_packages"] = self._local_packages
        with open(self._cache_file, "w") as json_file:
            json.dump(json_data, json_file)