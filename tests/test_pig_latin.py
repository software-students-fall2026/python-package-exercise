"""Tests for the english to pig latin."""


from pyjokelang.pig_latin import (english_word_to_pig_latin, english_sentence_to_pig_latin)

class TestPigLatin:
    """Unit tests for English to Pig Latin functions."""

    def test_word_consonants(self):
        """Test words beginning with consonants."""
        assert english_word_to_pig_latin("hello") == "elloh-ay"
        assert english_word_to_pig_latin("goodbye") == "oodbyeg-ay"
        assert english_word_to_pig_latin("software") == "oftwares-ay"

    def test_word_vowels(self):
        """Test words beginning with vowels."""
        assert english_word_to_pig_latin("apple") == "apple-way"
        assert english_word_to_pig_latin("orange") == "orange-way"
        assert english_word_to_pig_latin("ocean") == "ocean-way"

    def test_single_letter(self):
        """Test words containing one letter."""
        assert english_word_to_pig_latin("m") == "m-ay"
        assert english_word_to_pig_latin("b") == "b-ay"
        assert english_word_to_pig_latin("i") == "i-way"

    def test_sentence_known_output(self):
        """Test translating full sentences."""
        assert english_sentence_to_pig_latin("hello world") == "ELLOH-AY ORLDW-AY"
        assert english_sentence_to_pig_latin("i love software") == "I-WAY OVEL-AY OFTWARES-AY"
        assert english_sentence_to_pig_latin("we are the best") == "EW-AY ARE-WAY HET-AY ESTB-AY"

    def test_sentence_capitalization(self):
        """Test lowercase, uppercase, and mixed-case sentences."""
        assert english_sentence_to_pig_latin("hello world") == "ELLOH-AY ORLDW-AY"
        assert english_sentence_to_pig_latin("I LOVE SOFTWARE") == "i-WAY ovel-AY oftwares-AY"
        assert english_sentence_to_pig_latin("We Are The Best") == "Ew-AY aRE-WAY HEt-AY ESTb-AY"

    def test_sentence_whitespace(self):
        """Test empty sentences and extra spaces."""
        assert english_sentence_to_pig_latin("") == ""
        assert english_sentence_to_pig_latin("   ") == ""
        assert english_sentence_to_pig_latin("hello   world") == "ELLOH-AY ORLDW-AY"

    def test_word_invalid_input(self):
        """Placeholder for invalid word input tests."""

    def test_sentence_invalid_input(self):
        """Placeholder for invalid sentence input tests."""
