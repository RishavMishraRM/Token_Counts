import tiktoken

enc = tiktoken.encoding_for_model("gpt-4")
tokens = enc.encode("I can't believe it's already 2025!") # example sentence → I can't believe it's already 2025!
print(tokens)  # tokens → [40, 1443, 1722, 373, 337, 11802, 20352, 0]
print(len(tokens))  # Number of tokens → 9 tokens
