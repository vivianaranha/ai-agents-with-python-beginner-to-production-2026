def run_scenarios(agent, scenarios):
    results=[]
    for s in scenarios:
        out=agent.run(s["request"])
        ok=s.get("contains","") in str(out)
        results.append({"name":s.get("name","scenario"),"passed":ok,"output":out})
    return results
