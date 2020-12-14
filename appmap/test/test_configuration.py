"""Test Configuration"""
import appmap


def test_can_be_enabled(monkeypatch):
    """Test that recording is enabled when APPMAP=true"""
    monkeypatch.setenv("APPMAP", "true")
    assert appmap.enabled()


def test_is_disabled_when_unset(monkeypatch):
    """Test that recording is disabled when APPMAP is unset"""
    monkeypatch.delenv("APPMAP", raising=False)
    assert not appmap.enabled()

def test_is_disabled_when_false(monkeypatch):
    """Test that recording is disabled when APPMAP=false"""
    monkeypatch.setenv("APPMAP", "false")
    assert not appmap.enabled()
