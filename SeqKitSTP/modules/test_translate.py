from SeqKitSTP.modules.translate import codons, translate

def test_codons_chunkby3():
    assert codons("acggtgcag") == ["acg", "gtg", "cag"]

def test_translate_aa():
    assert translate("aaaaaaaaa") == "KKK"

def test_translate_stop():
    assert translate("gaagaaugauga") == "EE"