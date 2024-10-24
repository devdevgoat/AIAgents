#%%
from agent import Agent

# existing persona example
worker = Agent("worker")
worker_response = worker.instruct("Say hello")
print(worker_response)
# new persona example
reviewer = Agent("reviewer")
reviewer_response=reviewer.instruct("Say hello")
print(reviewer_response)

# %%
