# QiskitCheck

## Table of Contents
- [Introduction](#introduction)
- [Design & Specification](#design--specification)
  - [Language of Test](#language-of-test)
  - [Example Test](#example-test)
- [QiskitCheck Tool Architecture](#qiskitcheck-tool-architecture)
  - [Statistical Hypothesis Testing](#statistical-hypothesis-testing)
- [Assertions](#assertions)
  - [Single Qubit Assertions](#single-qubit-assertions)
  - [Multi Qubit Assertions](#multi-qubit-assertions)
- [Additional Features Implemented](#additional-features-implemented)
  - [Backend Selection](#backend-selection)
  - [Measure qubit values before quantum operations](#measure-qubit-values-before-quantum-operations)
  - [Filter Generated Tests](#filter-generated-tests)


## Introduction
Welcome to **QiskitCheck**, a test specification tool designed to check the correctness of assertions in quantum programs developed using Qiskit. This readme provides an overview of the QiskitCheck tool, its design, and how to use it effectively.

## Design & Specification
The design and implementation of QiskitCheck draw inspiration from various sources, including work by Honarvar et al. [16], quantum predicates, predicate transformers [8], and Quantum Hoare Logic [27]. QiskitCheck leverages Qiskit's syntax to define its test specification language. This section provides an informal discussion and an example of how to use QiskitCheck's semantics to define tests.

### Language of Test
A test in QiskitCheck consists of three main parts:

1. **Test Property and Preconditions**: Here, testers can specify properties and preconditions for test case generation, execution, and statistical analysis. Testers can optionally provide preconditions on input qubits, defining their states or positions on the Bloch sphere. QiskitCheck allows flexibility in parameter definition, with defaults for unspecified values.

2. **Function Call**: Testers define operations to be applied to the quantum circuits generated for tests. This is where quantum algorithms or circuits with simple gates are specified using QiskitCheck's built-in assertions.

3. **Assertions and Analysis**: Testers define post-conditions using built-in assertions. QiskitCheck uses assertions and statistical hypothesis tests to relate pre-conditions and post-conditions to verify correlations between them.

### Example Test
Here's an example test to check the equality of qubits using QiskitCheck:

    ```python
    class exampleTest(QiskitCheck):
        def setProperties(self):
            return TestProperty(noOfQubits=2, noOfTests=10, noOfExperiments=200,
                                noOfMeasurements=2000,
                                preConditions={0: Precondition(90, 90, 0, 0), 1: Precondition("−")})
  
      def operation(self, qc):
          qc.x(0)
          qc.x(1)
  
      def assertions(self):
          self.assertEqual(0, 1, basis='z')
          self.assertEqual(0, 1, basis='x')
  
    exampleTest().run()

This example checks the equality of qubits in the "z" and "x" axes. The test defines properties, operations, and assertions. After running the test, you'll receive a report indicating which tests passed and which failed.

### QiskitCheck Tool Architecture

QiskitCheck consists of four main components:

- **Test Case Generator**: Generates test cases based on specified properties for test quantum circuits.
- **Test Execution Engine**: Collects data for statistical tests.
- **Statistical Analysis Engine**: Performs statistical hypothesis tests on collected data.
- **Property-based Testing Engine (PBT Engine)**: Drives the entire framework and interfaces with users.

### Statistical Hypothesis Testing

QiskitCheck employs statistical hypothesis testing to analyze quantum program properties. This testing distinguishes between two hypotheses: the null hypothesis (H0) and the alternative hypothesis (H1). H0 assumes no significant difference between observed and expected data, while H1 suggests a significant difference. QiskitCheck uses tests like the chi-squared and t-distribution tests via Python's scipy library for hypothesis testing.

### Assertions

QiskitCheck supports various assertions to validate quantum program properties:

### Single Qubit Assertions
- **AssertProbability**: Checks the probability of measuring a qubit in a specific state.
- **AssertTeleported**: Tests if quantum teleportation has occurred between qubits.

### Multi Qubit Assertions
- **AssertEqual**: Compares states of two qubits for equality in a specified basis.
- **AssertEntangled**: Determines if two qubits are entangled.

## Additional Features Implemented

### Backend Selection
The default backend specified in the Test property parameters is the Aer simulator; however, testers have the freedom to choose from any of the Aer backends. Testers can accomplish this by simply passing down the desired backend into the test property parameters, e.g., `backend="qasm_simulator"`. For those with a verified IBMQ account, tests can be run on IBM's quantum computers via their website. To enable this functionality, testers must copy the API key found in the settings panel of the "My Account" section on the IBMQ website and specify the code seen in listing 4.1 in their respective test files:

QiskitCheck provides tools to rigorously test quantum programs, ensuring the correctness of quantum algorithms and circuits. For more details on usage, consult the documentation or examples provided.

    ```python
          from qiskit import IBMQ
          IBMQ.save_account("<replace with api token>")  

All testers have to do afterward is specify backend="ibmq" in the test property parameters in their test files. This feature adds flexibility for testers to switch between backends as needed.

## Measure Qubit Values Before Quantum Operations 

The assertions assertEqual(), assertProbability(), and assertTeleported() support measuring qubits before the application of quantum operations to the test cases. This is possible by setting the boolean pre-values, preMeasQubit0 and preMeasQubit1, to True. This feature has not been added to assertEntangled() as testing for entanglement requires generating a Bell state. This feature provides more flexibility as testers can ensure that a qubit has changed values or that a qubit is in the same state as another, among other use cases.

## Filter Generated Tests

Testers can filter the generated tests by applying any function that takes a Quantum Circuit as input and returns a boolean. This function can be specified as a parameter passed into the assertions, ensuring that all the concrete generated test cases are filtered by the function. This feature has been implemented as a function that checks if the user has specified a filter or not and utilizes Python's built-in filter class. The function returns the filtered list of generated tests and their new test indexes. This feature enables users to provide extremely general properties about the input program and adds a great deal of detail to the generated test cases.

For more details on these additional features and their usage, please refer to the documentation or examples provided.



