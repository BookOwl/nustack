from nustack.interpreter import Stack, StackUnderflowError
import pytest

def test_init():
    s = Stack()
    assert s._stack == []
    l = [1,2,3]
    s = Stack(l)
    assert s._stack == l
    assert s._stack is not l

def test_clear():
    s = Stack((1,2,3))
    s.clear()
    assert s._stack == []

def test_push():
    s = Stack()
    s.push(1)
    assert s._stack == [1,]
    s.push(2, 3)
    assert s._stack == [1, 2, 3]
    s.push(*(4, 5, 6))
    assert s._stack == [1, 2, 3, 4, 5, 6]

def test_len():
    s = Stack([1,2,3])
    assert len(s) == 3
    s.push(4)
    assert len(s) == 4

def test_pop():
    s = Stack()
    with pytest.raises(StackUnderflowError):
        s.pop()
    s.push(1, 2, 3)
    assert s.pop() == 3
    assert s.pop() == 2
    assert s.pop() == 1
    with pytest.raises(StackUnderflowError):
        s.pop()

def test_popN():
    s = Stack([1, 2, 3, 4, 5])
    t = s.popN(2)
    assert len(t) == 2
    assert t == (4, 5)
    assert s._stack == [1, 2, 3]
    t = s.popN(1)
    assert len(t) == 1
    assert t == (3, )
    s.clear()
    t = s.popN(0)
    assert t == ()

def test_repr():
    s = Stack([1, 2, 3])
    assert repr(s) == "Stack( [1, 2, 3] )"
    assert str(s) == "Stack( [1, 2, 3] )"
