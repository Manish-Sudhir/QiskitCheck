from math import degrees, pi
from dataclasses import dataclass
# from .ExtraFunctions import cordsComplexToThetaPhi

@dataclass()
class Precondition():
    def __init__(self,
                 minTheta,
                 maxTheta = None,
                 minPhi = None,
                 maxPhi = None,
                 isRadian = None):
        if isRadian == None: isRadian = False
        if (isinstance(minTheta, int) or isinstance(minTheta, float)) \
            and (isinstance(maxTheta, int) or isinstance(maxTheta, float)) \
            and (isinstance(minPhi, int) or isinstance(minPhi, float)) \
            and (isinstance(maxPhi, int) or isinstance(maxPhi, float)) \
            and (isRadian == False):

            self.setThetaPhiVals(minTheta, maxTheta, minPhi, maxPhi, isRadian)  
        # elif (isinstance(minTheta, list) or isinstance(minTheta, tuple)) \
        #     and (isinstance(maxTheta, int) or isinstance(maxTheta, float) or arg1 == None) \
        #     and (isinstance(minPhi, int) or isinstance(minPhi, float) or arg2 == None) \
        #     and (isinstance(maxPhi, bool) or maxPhi == None):
        #         if maxTheta == None:
        #             maxTheta = 0
        #         if minPhi == None:
        #             minPhi = 0
        #         if maxPhi == None:
        #             maxPhi = False

        #         self.init_coords(minTheta, maxTheta, minPhi, maxPhi)     
        elif (isinstance(minTheta, str)):
            state = minTheta
            if state.lower() == "any":
                self.setThetaPhiVals(0, 360, 0, 360, False)
            elif state == "+":
                self.setThetaPhiVals(90, 90, 0, 0, False)
            elif state == "-":
                self.setThetaPhiVals(90, 90, 180, 180, False)
            elif state == "1":
                self.setThetaPhiVals(180, 180, 0, 0, False)
            elif state == "0":
                self.setThetaPhiVals(0, 0, 0, 0, False)
            else:
                raise Exception(f"Input for Precondition not recognised: {minTheta}")
        else:
            raise Exception(f"Incorrect arguments for Precondition")

    #Can initalise with 2 complex numbers and how much it can vary around
    # def init_coords(self,
    #                 init_vect,
    #                 diff_theta,
    #                 diff_phi,
    #                 radian):

    #     (theta, phi) = cordsComplexToThetaPhi(init_vect)

    #     theta = round(degrees(theta))
    #     phi = round(degrees(phi))
    #     diff_theta = round(diff_theta)
    #     diff_phi = round(diff_phi)

    #     if not radian:
    #         self.minTheta = theta - diff_theta
    #         self.maxTheta = theta + diff_theta
    #         self.minPhi = phi - diff_phi
    #         self.maxPhi = phi + diff_phi
    #     else:
    #         self.minTheta = theta - degrees(diff_theta)
    #         self.maxTheta = theta + degrees(diff_theta)
    #         self.minPhi = phi - degrees(diff_phi)
    #         self.maxPhi = phi + degrees(diff_phi)

    def setThetaPhiVals(self,
                       minTheta,
                       maxTheta,
                       minPhi,
                       maxPhi,
                       isRadian):

        if isRadian==False:
            #Error handling on Precondition values
            if minTheta < 0 or minTheta > 360:
                raise Exception(f"Invalid minTheta supplied, it has to be between 0 and 360 inclusive: {minTheta}")
            if maxTheta < 0 or maxTheta > 360:
                raise Exception(f"Invalid maxTheta supplied, it has to be between 0 and 360 inclusive: {maxTheta}")
            if minPhi < 0 or minPhi > 360:
                raise Exception(f"Invalid minPhi supplied, it has to be between 0 and 360 inclusive: {minPhi}")
            if maxPhi < 0 or maxPhi > 360:
                raise Exception(f"Invalid maxPhi supplied, it has to be between 0 and 360 inclusive: {maxPhi}")

            self.minTheta = minTheta
            self.maxTheta = maxTheta
            self.minPhi = minPhi
            self.maxPhi = maxPhi

        else:
            self.minTheta = degrees(minTheta)
            self.maxTheta = degrees(maxTheta)
            self.minPhi = degrees(minPhi)
            self.maxPhi = degrees(maxPhi)

@dataclass()
class TestProperty:
    def __init__(self,
                 pVal=0.01,
                 noOfTests=10,
                 noOfExperiments=100,
                 noOfMeasurements=500,
                 noOfQubits=1,
                 noOfClassicalBits=0,
                 preConditions={},
                 backend="aer_simulator"): 

        #Error handling on all values for the test property
        if pVal < 0 and pVal > 1:
            raise Exception(f"Invalid pVal supplied: {pVal}")
        elif noOfTests < 1:
            raise Exception(f"Invalid amount of tests supplied: {noOfTests}")
        elif noOfExperiments < 1:
            raise Exception(f"Invalid number of trials supplied: {noOfExperiments}")
        elif noOfMeasurements < 1:
            raise Exception(f"Invalid number of measurements supplied: {noOfMeasurements}")

        elif isinstance(noOfQubits, int) and noOfQubits < 1:
            raise Exception(f"Invalid number of qubits supplied: {noOfQubits}")
        elif ((isinstance(noOfQubits, tuple) or isinstance(noOfQubits, list))) \
                and (noOfQubits[0] < 1 or noOfQubits[1] < noOfQubits[0] or len(noOfQubits) != 2):
            raise Exception(f"Invalid range of qubits supplied: {noOfQubits}")

        elif noOfClassicalBits < 0:
            raise Exception(f"Invalid number of classical bits supplied: {noOfClassicalBits}")


        self.pVal = pVal
        self.noOfTests = noOfTests
        self.noOfExperiments = noOfExperiments
        self.noOfMeasurements = noOfMeasurements
        if isinstance(noOfQubits, int):
            self.minQubits = noOfQubits
            self.maxQubits = noOfQubits
        elif isinstance(noOfQubits, tuple) or isinstance(noOfQubits, list):
            self.minQubits = noOfQubits[0]
            self.maxQubits = noOfQubits[1]
        self.noOfClassicalBits = noOfClassicalBits
        self.preConditions = preConditions
        self.backend = backend