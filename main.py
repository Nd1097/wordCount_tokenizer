from functions import num_tokens_from_string





if __name__ == "__main__":
    prompt = """So, this was a bit hawkward.  When we first started this, I thought GPT might be able to access URLs.  I swear it did when I first used it.
        I digress.  So, we were going to pass it a secure link.  That's why we're generating an auth.  I figured it may come in handy to have the
        ability in the future, so it hasn't been completely removed when I realized the err of my ways, but we really aren't using it."""
    token = num_tokens_from_string(prompt, "cl100k_base")
    print(token)