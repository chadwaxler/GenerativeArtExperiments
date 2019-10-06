
REM Execute art!
REM -Xms256m  : Starting heap size of 256Mb
REM -Xmx1024m : Max heap size of 1024Mb

ECHO Start of Loop

FOR /L %%i IN (1,1,50) DO (
	java -Xms256m -Xmx1024m-jar processing-py.jar sketchName.py
  ECHO %%i
)

