import os
os.environ['JAVA_HOME'] = '/usr/lib/jvm/java-1.11.0-openjdk-amd64'
os.environ['CLASSPATH'] = './lib/java/worldwind.jar:./lib/java/worldwindx.jar'
from jnius import autoclass

# Classe d'utilité pour charger les classes java NWW & autre
class NWW:
    ApplicationTemplate = autoclass('gov.nasa.worldwindx.examples.ApplicationTemplate')
    AppFrame = autoclass('gov.nasa.worldwindx.examples.ApplicationTemplate$AppFrame')
    String = autoclass('java.lang.String')
    WorldWindowGLCanvas = autoclass('gov.nasa.worldwind.awt.WorldWindowGLCanvas')
