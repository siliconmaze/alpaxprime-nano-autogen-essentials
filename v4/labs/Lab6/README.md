# Lab 6: Human-in-the-Loop

## Objectives

- Add human approval to workflows
- Configure intervention modes
- Build approval pipelines
- Handle human feedback

---

## Key Concepts

### Human Input Modes

| Mode | Behavior |
|------|----------|
| NEVER | Fully automated |
| ALWAYS | Always ask human |
| TERMINATE | Ask at end |

---

## Examples

### Example 1: Approval Workflow

```python
approver = UserProxyAgent(name="approver", human_input_mode="TERMINATE")

# Agent suggests action
suggestion = agent.generate_reply(messages=[...])

# Human reviews and approves
# Then execute...
```

---

## Exercises

1. Build email approval system
2. Create code deployment approval
3. Implement content moderation

---

## Next Lab

[Lab 7: Production Patterns](../Lab7/README.md)
