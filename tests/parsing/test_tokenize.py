from nustack.tokenize import *
import pytest

def test_addescapes():
    s_raw = r"""\\spam lalala\'\"\b\rspam lalala\n\t\vspam lalala"""
    s_escaped = """\\spam lalala\'\"\b\rspam lalala\n\t\vspam lalala"""
    assert addescapes(s_raw) == s_escaped

class Test_Token():
    def test_init(self):
        t = Token("lit_int", 5)
        assert t.type == "lit_int"
        assert t.val  == 5

    def test_eq(self):
        t1, t2, t3, t4, t5 = (
                              Token("lit_int", 5),
                              Token("lit_int", 5),
                              Token("lit_int", 7),
                              Token("lit_float", 5.0),
                              Token("lit_string", "5")
                             )
        assert t1 == t2
        assert not t1 == t3
        assert t1 == t4
        assert not t1 == t5

    def test_lt(self):
        t1, t2, t3, t4, t5 = (
                              Token("lit_int", 5),
                              Token("lit_int", 5),
                              Token("lit_int", 7),
                              Token("lit_float", 5.0),
                              Token("lit_string", "5")
                             )
        assert not t1 < t2
        assert t1 < t3
        assert not t3 < t1
        assert not t1 < t4
        assert not t1 < t5

    def test_gt(self):
        t1, t2, t3, t4, t5 = (
                              Token("lit_int", 5),
                              Token("lit_int", 5),
                              Token("lit_int", 7),
                              Token("lit_float", 5.0),
                              Token("lit_string", "5")
                             )
        assert not t1 > t2
        assert not t1 > t3
        assert t3 > t1
        assert not t1 > t4
        assert not t1 > t5

    def test_hash(self):
        try:
            h = hash(Token("lit_int", 5))
        except Exception as e:
            print("hash() raised an exception!" + str(e))
            assert False
        else:
            assert type(h) == int

    def test_detailstr(self):
        assert Token("lit_int", 5).detailstr() == "Token(type='lit_int', val=5)"

    def test_repr(self):
        assert repr(Token("lit_int", 5)) == repr(5)
        assert repr(Token("lit_float", 5.0)) == repr(5.0)
        assert repr(Token("lit_string", "spam")) == repr("spam")
        assert repr(Token("lit_list", [Token("lit_int", 5)]*3)) == "[ 5 5 5 ]"
        assert repr(Token("lit_symbol", "spam")) == "`spam"

    def test_iter(self):
        assert list(iter(Token("lit_string", "spam"))) == list(iter("spam"))

    def test_get(self):
        class Fee:
            fii = "foo"
            spam = [1, 2, 3]
        t = Token("obj", Fee())
        assert t.get("fii") == Token("lit_string", "foo")
        assert t.get("spam") == [1, 2, 3]

def test_tokenize():
    expected = [
        Token("lit_string", "spam"),
        Token("lit_string", "spam"),
        Token("lit_string", "spam\nham"),
        Token("lit_int", 1),
        Token("lit_string", "spam"),
        Token("lit_int", 1),
        Token("lit_int", 2),
        Token("lit_float", 3.14159),
        Token("lit_bool", True),
        Token("lit_bool", False),
        Token("lit_bytes", b"spam"),
        Token("lit_symbol", "spam"),
        Token("lit_symbol", LEGAL_IDS),
        Token("call", "a.call"),
        Token("call", LEGAL_IDS),
        Token("lit_liststart","["),
        Token("lit_int", 1),
        Token("lit_int", 2),
        Token("listend", "]"),
        Token("lit_code", [
            Token("lit_string", "spam"),
            Token("call", "show"),
        ]),
    ]
    prog = r"""
    /* A test prog */
    /* Some strings and numbers */
    "spam" 'spam' "spam\nham" 1'spam'1 2 3.14159
    /* Bools */
    #t #f
    b'spam' /* <- Bytes */
    /* A symbol */ `spam
    `%s
    /* A call */
    a.call
    %s
    /* A list */
    [ 1
    2 ]
    /* Code */
    { "spam" show }
    /* The end */""" % (LEGAL_IDS, LEGAL_IDS)
    toks = tokenize(prog)
    assert toks == expected
