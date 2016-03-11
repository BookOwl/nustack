from nustack.interpreter import Scope, ScopeLookupError, ScopeUnderflowError
import pytest

def test_init():
    s = Scope()
    assert s._scopes == [ {}, ]

def test_pushScope():
    s = Scope()
    s.pushScope()
    assert s._scopes == [ {}, {}, ]
    s.pushScope({"one": 1, 1:"one"})
    assert s._scopes == [ {}, {}, {"one": 1, 1:"one"}]

def test_popScope():
    s = Scope()
    with pytest.raises(ScopeUnderflowError):
        s.popScope()
    s.pushScope()
    s.pushScope()
    s.popScope()
    assert len(s._scopes) == 2
    s.popScope()
    assert len(s._scopes) == 1
    with pytest.raises(ScopeUnderflowError):
        s.popScope()

def test_assign():
    s = Scope()
    s.assign("a", 1)
    assert s._scopes == [ {"a": 1, }, ]
    s.assign("b", 2)
    assert s._scopes == [ {"a": 1, "b": 2, }, ]
    s.assign("a", "spam")
    assert s._scopes == [ {"a": "spam", "b": 2, }, ]
    s.pushScope()
    s.assign("a", 1)
    s.assign("c", "foo")
    assert s._scopes == [ {"a": "spam", "b": 2, }, {"a": 1, "c": "foo", }, ]

def test_lookup():
    s = Scope()
    s.assign("a", "spam")
    s.assign("b", 2)
    s.pushScope()
    s.assign("a", 1)
    s.assign("c", "foo")
    assert s._scopes == [ {"a": "spam", "b": 2, }, {"a": 1, "c": "foo", }, ]
    assert s.lookup("a") == 1
    assert s.lookup("b") == 2
    assert s.lookup("c") == "foo"
    with pytest.raises(ScopeLookupError):
        s.lookup("spam")

def test_getGlobal():
    s = Scope()
    s.assign("a", "spam")
    s.assign("b", 2)
    s.pushScope()
    s.assign("a", 1)
    s.assign("c", "foo")
    assert s._scopes == [ {"a": "spam", "b": 2, }, {"a": 1, "c": "foo", }, ]
    assert s.getGlobal("a") == "spam"
    assert s.getGlobal("b") == 2
    with pytest.raises(ScopeLookupError):
        s.getGlobal("c")
    with pytest.raises(ScopeLookupError):
        s.getGlobal("spam")
