import math

# Activation functions
def relu(x):
    return max(0, x)

def sigmoid(x):
    return 1 / (1 + math.exp(-x))

# Input values
inputs = [1.0, 2.0]   # Example input

# Weights and bias for hidden layer
weights_hidden = [
    [0.5, -0.3],   # weights for hidden neuron 1
    [0.8, 0.2]     # weights for hidden neuron 2
]
bias_hidden = [0.1, -0.1]

# Weights and bias for output layer
weights_output = [1.2, -0.7]
bias_output = 0.05

# ---- Forward Pass ----

# Hidden layer computation
hidden_outputs = []
for i in range(2):
    net_input = (
        inputs[0] * weights_hidden[i][0] +
        inputs[1] * weights_hidden[i][1] +
        bias_hidden[i]
    )
    activated_output = relu(net_input)
    hidden_outputs.append(activated_output)

# Output layer computation
net_output = (
    hidden_outputs[0] * weights_output[0] +
    hidden_outputs[1] * weights_output[1] +
    bias_output
)

final_output = sigmoid(net_output)

# Output
print("Input:", inputs)
print("Hidden Layer Output:", hidden_outputs)
print("Final Output:", final_output)