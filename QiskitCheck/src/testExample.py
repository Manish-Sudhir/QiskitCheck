from PBTEngine import QiskitPropertyTest, TestProperty, Precondition
import numpy as np




# class testExample(QiskitPropertyTest):
#     def property(self):
#         return TestProperty(nbQubits=2,
#                             qargs={0: Qarg([1,0]),
#                                    1: Qarg([0,1])})

#     def quantumFunction(self, qc):
#         qc.x(0)
#         qc.x(1)

#     def assertions(self):
#         self.assertNotEqual(0, 1)
#         self.assertProbability(0, 0)
#         self.assertProbability(1, 1)

# testExample().run()


# def lamb(qc, inputIndex):
#     foundInit = False
#     for gate in qc.data:
#         if (gate[0].name == "initialize" and gate[1][0].index == inputIndex):
#             foundInit = True
#             break
#     return foundInit

# min = 1
# max = 20
# class testFurtherExample(QiskitPropertyTest):
#     def property(self):
#         return TestProperty(nbQubits=[min, max])

#     def quantumFunction(self, qc):
#         for qubitIndex in range(len(qc.qubits)):
#             if np.random.randint(2) == 0:
#                 #randomly initialises to |1>, else it's already initialised to |0>
#                 qc.initialize([0, 1], qubitIndex)
#             qc.x(qubitIndex)

#     def assertions(self):
#         for qubitIndex in range(max):
#             self.assertProbability(qubitIndex, 0, filter_qc=lambda qc: len(qc.qubits) > qubitIndex and not lamb(qc, qubitIndex))
#             self.assertProbability(qubitIndex, 1, filter_qc=lambda qc: len(qc.qubits) > qubitIndex and lamb(qc, qubitIndex))

# testFurtherExample().run()


class testPlusMinusEquality(QiskitPropertyTest):
   def property(self):
      return TestProperty(noOfQubits=2,
                          preConditions={0: Precondition("+"),
                                 1: Precondition("-")})

   def assertions(self):
      self.assertEqual(0, 1, basis="z")
      self.assertEqual(0, 1, basis="y")
      self.assertNotEqual(0, 1, basis="x")

testPlusMinusEquality().run()
