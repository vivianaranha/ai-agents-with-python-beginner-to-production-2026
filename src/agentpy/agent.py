import json
from .security import requires_approval

class Agent:
    def __init__(self, provider, tools=None, max_steps=5, approver=None):
        self.provider=provider; self.tools=tools; self.max_steps=max_steps; self.approver=approver

    def run(self, request: str):
        messages=[{"role":"user","content":request}]
        for _ in range(self.max_steps):
            raw=self.provider.generate(messages)
            try: action=json.loads(raw)
            except json.JSONDecodeError: return {"status":"error","error":"invalid model output"}
            if action.get("type")=="final": return {"status":"done","answer":action.get("answer","")}
            if action.get("type")=="tool":
                tool=self.tools.get(action["name"])
                if requires_approval(tool.permission):
                    if not self.approver or not self.approver(tool.name, action.get("args",{})):
                        return {"status":"denied","tool":tool.name}
                result=tool.call(**action.get("args",{}))
                messages.append({"role":"tool","content":str(result)})
        return {"status":"stopped","reason":"max_steps"}
