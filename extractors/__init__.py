from .extractors import *

allClasses = [
        klass
        for name, klass in globals().items()
        if name.endswith('IE')
        ]

def genExtractorClasses():
    return allClasses

def genExtractors():
    print("Generating extractors!")
    return [klass() for klass in genExtractorClasses()]
