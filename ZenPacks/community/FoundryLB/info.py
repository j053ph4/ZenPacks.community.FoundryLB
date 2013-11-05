from ZenPacks.community.ConstructionKit.ClassHelper import *

def snL4RealServergetEventClassesVocabulary(context):
    return SimpleVocabulary.fromValues(context.listgetEventClasses())

class snL4RealServerInfo(ClassHelper.snL4RealServerInfo):
    ''''''

def snL4BindgetEventClassesVocabulary(context):
    return SimpleVocabulary.fromValues(context.listgetEventClasses())

class snL4BindInfo(ClassHelper.snL4BindInfo):
    ''''''

def snL4VirtualServergetEventClassesVocabulary(context):
    return SimpleVocabulary.fromValues(context.listgetEventClasses())

class snL4VirtualServerInfo(ClassHelper.snL4VirtualServerInfo):
    ''''''


