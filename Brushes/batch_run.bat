
ECHO Start of Loop

FOR /L %%i IN (1,1,50) DO (
	java -Xms6g -Xmx6g -jar processing-py.jar brushesSketch.py
  ECHO %%i
)

