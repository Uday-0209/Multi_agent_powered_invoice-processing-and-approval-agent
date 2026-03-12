import dspy 
from dspy_programs.fraud_detection import FraudDetection
from dspy.teleprompt import BootstrapFewShot
from dspy_programs.fraud_examples import trainset

def optimize_fraud_detector():
    
    fraud_program = dspy.Predict(FraudDetection)
    optimizer = BootstrapFewShot()
    
    compiled_prompt =optimizer.compile(
        fraud_program,
        trainset = trainset
    )
    return compiled_prompt