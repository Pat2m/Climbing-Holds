# -*- coding: utf-8 -*-
"""
Created on Thu Jan 20 19:37:52 2022

@author: Pat
"""

import numpy as np
#import math

X = [[1,2,3,2.5,2.0,5.0,-1,2],
     [2.0,5.0,-1,2,2.0,5.0,-1,2],
     [-1.5,2.7,3.3,-.8,2.0,5.0,-1,2]]

#x = [batchsize, data points] ^ is batch = 3 with 4 data points
 

class LayerDense:
    def __init__(self, n_inputs, n_neurons):
       self.weights = .1 * np.random.randn(n_inputs, n_neurons)
       self.biases = np.zeros((1, n_neurons))
       self.inputs = n_inputs
       self.neurons = n_neurons
    
    def forwardPass(self, inputs):
        self.output = np.dot(inputs, self.weights) + self.biases
        
    def exportW(self):
        return self.weights
    
    def exportB(self):
        return self.biases
    
    def importWB(self, newWB):
        self.weights = newWB[0]
        self.biases = newWB[1]
    
    def exportWB(self):
        return [self.weights, self.biases]
        
    def exportLayer(self):
        return [self.inputs, self.neurons, [self.exportWB()]]
    
    # Backward pass
    def backward(self, dvalues):
         # Gradients on parameters
         self.dweights = np.dot(self.inputs.T, dvalues)
         self.dbiases = np.sum(dvalues, axis=0, keepdims=True)
         # Gradient on values
         self.dinputs = np.dot(dvalues, self.weights.T)
    

class Memory():
    def backward(self,inputs):
        self.output = inputs


class ActivationReLu:
    def forward(self,inputs):
        self.output = np.maximum(0,inputs)
        
        # Backward pass
    def backward(self, dvalues):
         # Since we need to modify original variable,
         # let’s make a copy of values first
         self.dinputs = dvalues.copy()
         # Zero gradient where input values were negative
         self.dinputs[self.inputs <= 0] = 0
        
class SoftMax:
        def forward(self,inputs):
            exponentiatedValues = np.exp(inputs - np.max(inputs))
            prob = exponentiatedValues / np.sum(exponentiatedValues, axis=1, keepdims=True)
            self.output = prob #probabilities
        def backward(self, dvalues):
         # Create uninitialized array
         self.dinputs = np.empty_like(dvalues)
         # Enumerate outputs and gradients
         for index, (single_output, single_dvalues) in enumerate(zip(self.output, dvalues)):
         # Flatten output array
             single_output = single_output.reshape(-1, 1)
         # Calculate Jacobian matrix of the output
         jacobian_matrix = np.diagflat(single_output) - np.dot(single_output, single_output.T)
         # Calculate sample-wise gradient
         # and add it to the array of sample gradients
         self.dinputs[index] = np.dot(jacobian_matrix,
         single_dvalues)
                
class Loss:
        def calculateLoss(self, output, y):
            sampleLoss = self.forward(output, y)
            dataLoss = np.mean(sampleLoss)
            return dataLoss
        
        
class LossCategoricalEntropy(Loss)            :
    def forward(self, yPred, yTrue):
        sample = len(yPred)
        yPredClipped = np.clip(yPred, 1e-7, 1-1e-7)
        if len(yTrue.shape) == 1:
            correctConf = yPredClipped[range(sample), yTrue]
        elif len(yTrue.shape)==2:
            correctConf = np.sum(yPredClipped*yTrue, axis=1)
    
        negativeLogProb = -np.log(correctConf)
        return negativeLogProb

        # Backward pass
    def backward(self, dvalues, y_true):
         # Number of samples
         samples = len(dvalues)
         # Number of labels in every sample
         # We'll use the first sample to count them
         labels = len(dvalues[0])
         # If labels are sparse, turn them into one-hot vector
         if len(y_true.shape) == 1:
             y_true = np.eye(labels)[y_true]
         # Calculate gradient
         self.dinputs = -y_true / dvalues
         # Normalize gradient
         self.dinputs = self.dinputs / samples


class Activation_Softmax_Loss_CategoricalCrossentropy():
     # Creates activation and loss function objects
     def __init__(self):
         self.activation = SoftMax()
         self.loss = LossCategoricalEntropy()
     # Forward pass
     def forward(self, inputs, y_true):
         # Output layer's activation function
         self.activation.forward(inputs)
         # Set the output
         self.output = self.activation.output
         # Calculate and return loss value
         return self.loss.calculate(self.output, y_true)
     # Backward pass
     def backward(self, dvalues, y_true):
         # Number of samples
         samples = len(dvalues)
         # If labels are one-hot encoded,
         # turn them into discrete values
         if len(y_true.shape) == 2:
             y_true = np.argmax(y_true, axis=1)
         # Copy so we can safely modify
         self.dinputs = dvalues.copy()
         # Calculate gradient
         self.dinputs[range(samples), y_true] -= 1
         # Normalize gradient
         self.dinputs = self.dinputs / samples



#working on bias tweak functions
class TweakWB():
        def __init__(self):
            self.bestLoss = 1000000000000000
            
        def forward(self, LayerDense, Loss):
            if Loss < self.bestLoss:
                self.bestLoss = Loss
            else:
                self.output


trueVal = np.array(
           [[1, 0, 3, 4, 5, 6],
           [1, 2, 3, 4, 0, 6],
           [1, 2, 0, 4, 5, 6]]
           )

        #test functions
layer1 = LayerDense(8,5)
layer2 = LayerDense(5,6)
layer3 = LayerDense(6,6)
activation1 = SoftMax()
layer1.forwardPass(X)
activation1.forward(layer1.output)
activation2 = SoftMax()

print(activation1.output)
lossFunction = LossCategoricalEntropy()
layer2.forwardPass(activation1.output)
#out1=activation2.forward(layer2.output)
 
print(layer2.output)
layer3.forwardPass(layer2.output)
print(layer3.output)
loss = lossFunction.calculateLoss(layer3.output, trueVal)
print(loss)
optimizer = TweakWB()
tweaks = optimizer.forward(layer2,loss)
#layer1.forwardPass(X)
#activation1.forward(layer1.output)
#layer2.forwardPass(activation1.output)
#activation2.forward(layer2.output)


#tweaks = TweakWB.forward(layer2,loss)



#print(np.clip(activation2.output, 1e-7, 1-1e-7))
#print("Loss: " + str(loss))
#print(len(trueVal.shape))