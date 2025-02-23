import argparse
from azureml.core import Run

# Parse arguments
parser = argparse.ArgumentParser()
parser.add_argument("--preprocessing_order", type=str, required=True)
args = parser.parse_args()

# Azure ML Run context
run = Run.get_context()

# Simulate training with the given preprocessing order
print(f"Running preprocessing with order: {args.preprocessing_order}")

# Log the result (simulated accuracy)
import random
accuracy = random.uniform(0.7, 0.99)
run.log("accuracy", accuracy)

run.complete()
