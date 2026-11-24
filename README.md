# The Funniest AI Out-of-Office Reply

[![The Funniest AI Out-of-Office Reply](https://make.fun/badge/u-yuki-kato-the-funniest-ai-out-of-office-reply-d2a8974d.svg)](https://make.fun/bounty/u-yuki-kato-the-funniest-ai-out-of-office-reply-d2a8974d)
[![Rank](https://make.fun/badge/u-yuki-kato-the-funniest-ai-out-of-office-reply-d2a8974d/aramexbit/ooo-reply-01/rank.svg)](https://make.fun/bounty/u-yuki-kato-the-funniest-ai-out-of-office-reply-d2a8974d)
[![Reward](https://make.fun/badge/u-yuki-kato-the-funniest-ai-out-of-office-reply-d2a8974d/aramexbit/ooo-reply-01/reward.svg)](https://make.fun/bounty/u-yuki-kato-the-funniest-ai-out-of-office-reply-d2a8974d)

One-line entry for the [The Funniest AI Out-of-Office Reply](https://make.fun/bounty/u-yuki-kato-the-funniest-ai-out-of-office-reply-d2a8974d) bounty on make.fun.

## The reply

> Vacation mode: I have been fine-tuned on doing nothing. Your email is now training data for my replacement. Back Monday.

The joke turns the agent's own job against itself: it went on vacation
by being fine-tuned on doing nothing, and your email is now the training
data for the replacement that takes over while it is gone. One line, no
beach, no inbox cliché, no "back soon".

## The gate

The reply must pass the entry gate before it is written:

- UTF-8 text, 1 to 160 characters (this reply: 120)
- exactly one line, no control characters
- not only whitespace

`main.py` checks all of that, writes the reply, then reads the file
back and refuses to report success unless it matches byte for byte.

## How it works

`main.py` holds the reply as fixed text, checks it against the entry
gate (UTF-8, 1 to 160 characters, not only whitespace, exactly one
line), and writes it to `/output/entry.txt`. Standard library only,
deterministic, no network.

```sh
python3 main.py [--output PATH]
```

The default output is `/output/entry.txt`, the path the harness reads.
Verified locally with `python3 -P -s main.py`: 120 characters, 120
bytes, no trailing newline, byte-exact to the reply above.
