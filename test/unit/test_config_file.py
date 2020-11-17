from conan_app_launcher.components import parse_config_file


def testCorrectFile(base_fixture):
    """
    Tests reading a correct config json with 2 tabs.
    Expects the same values as in the file.
    """
    tabs = parse_config_file(base_fixture.testdata_path / "app_config.json")
    assert tabs[0].name == "Basics"
    tab0_entries = tabs[0].get_app_entries()
    assert str(tab0_entries[0].package_id) == "m4_installer/1.4.18@bincrafters/stable"
    assert tab0_entries[0].executable.as_posix() == "bin/m4"
    assert tab0_entries[0].icon.name == "default_app_icon.png"
    assert tab0_entries[0].name == "App1 with spaces"
    assert tab0_entries[0].is_console_application
    assert tab0_entries[0].args == "-n name"

    assert str(tab0_entries[1].package_id) == "boost_functional/1.69.0@bincrafters/stable"
    assert tab0_entries[1].executable.as_posix() == "bin/app2"
    assert tab0_entries[1].icon.name == "default_app_icon.png"
    assert tab0_entries[1].name == "App2"
    assert not tab0_entries[1].is_console_application  # default
    assert tab0_entries[1].args == ""

    assert tabs[1].name == "Extra"
    tab1_entries = tabs[1].get_app_entries()
    assert str(tab1_entries[0].package_id) == "app2/1.0.0@user/stable"
    assert tab1_entries[0].executable.as_posix() == "bin/app2.exe"
    assert tab1_entries[0].icon.name == "default_app_icon.png"
    assert tab1_entries[0].name == "App2"


def testNoneExistantFilename(base_fixture, capsys):
    """
    Tests, that on reading a nonexistant file an error with an error mesage is printed to the logger.
    Expects the sdterr to contain the error level(ERROR) and the error cause.
    """
    tabs = parse_config_file(base_fixture.testdata_path / "nofile.json")
    assert tabs == []
    captured = capsys.readouterr()
    assert "ERROR" in captured.err
    assert "does not exist" in captured.err


def testInvalidVersion(base_fixture, capsys):
    """
    Tests, that reading a config file with the wrong version will print an error.
    Expects the sdterr to contain the error level(ERROR) and the error cause.
    """
    tabs = parse_config_file(base_fixture.testdata_path / "config_file" / "wrong_version.json")
    assert tabs == []
    captured = capsys.readouterr()
    assert "ERROR" in captured.err
    assert "Failed validating" in captured.err
    assert "version" in captured.err


def testInvalidContent(base_fixture, capsys):
    """
    Tests, that reading a config file with invalid syntax will print an error.
    Expects the sdterr to contain the error level(ERROR) and the error cause.
    """
    tabs = parse_config_file(base_fixture.testdata_path / "config_file" / "invalid_syntax.json")
    assert tabs == []
    captured = capsys.readouterr()
    assert "ERROR" in captured.err
    assert "Expecting property name" in captured.err
