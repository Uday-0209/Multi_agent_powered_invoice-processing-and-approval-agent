import dspy 

from dspy.teleprompt import BootstrapFewShot
from dspy_programs.decision_reasoning import DecisionReasoning
from dspy_programs.decision_examples import trainset

def optimize_decision_model():
    
    program = dspy.Predict(DecisionReasoning)
    
    optimizer = BootstrapFewShot()
    
    compiled_prompt = optimizer.compile(
        program,
        trainset = trainset)
    
    return compiled_prompt