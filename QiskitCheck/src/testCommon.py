from Qiskit_PTesting.Qiskit_PTesting import TestProperty, Qarg, QiskitPropertyTest


# class testing(QiskitPropertyTest):
#     def property(self):
#         return TestProperty(nbQubits=5,
#                             nbClassicalBits=20)

#     def quantumFunction(self, qc):
#         qc.h(0)
#         qc.h(1)


#     def assertions(self):
#         self.assertMostCommon("00000") # should fail
#         self.assertMostCommon(["00000", "01000", "11000", "10000"])

# testing().run()

class testAssertEntangle(QiskitPropertyTest):
    def property(self):
        return TestProperty(nbQubits=7,
                            qargs={0: Qarg("0"),
                                1: Qarg("+"),
                                2: Qarg("+"),
                                3: Qarg("+")
                            })

    def quantumFunction(self, qc):
        qc.h(0)
        qc.cx(0, 1)

    def assertions(self):
        self.assertEntangled(0, 1)
        self.assertNotEntangled(2, 1)
        self.assertNotEntangled(2, 3)

testAssertEntangle().run()