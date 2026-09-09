# Agent Security Checklist

- Treat prompts, retrieved documents and tool output as untrusted data.
- Separate instructions from data.
- Validate structured actions.
- Enforce permissions outside the model.
- Require approval for high-impact side effects.
- Prevent secret exposure in logs and prompts.
- Apply least privilege to tools and identities.
- Bound loops, retries, spend and concurrency.
- Test prompt injection, memory poisoning and tool misuse.
- Trace who requested, approved and executed an action.
