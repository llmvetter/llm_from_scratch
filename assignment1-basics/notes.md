(a) What Unicode character does chr(0) return?

chr(0) returns '\x00'.

How does this character’s string representation (__repr__()) differ from its printed
representation?

The __repr__() method return the actual string representation including backlashes and quotation marks
whereas the print statement will return only a whitespace.

(c) What happens when this character occurs in text?

The character adds a whitespace.

(e) What are some reasons to prefer training our tokenizer on UTF-8 encoded bytes, rather than UTF-16 or UTF-32?

UTF16 and UTF32 return increasingly sparser arrays taking up more memory.
For most ASCII characters, we only need one byte, using a larger byte encoding will produce sparser arrays of data.

(f) Consider the following (incorrect) function, which is intended to decode a UTF-8 byte string
into a Unicode string. Why is this function incorrect? Provide an example of an input byte
string that yields incorrect results.

The character string こんにちは will break the function. The function is incorrect as it assumes that each byte represents a single character (might be correct for ASCII) but for characters that have a large unicode point number it will break.

(g) Give a two-byte sequence that does not decode to any Unicode character(s).

0b11100000, 101 will break as the first byte indicates that it will be a three byte array but then only one follow up byte is given resulting in a UnicodeDecodError.