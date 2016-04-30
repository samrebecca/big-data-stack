export HADOOP_CLASSPATH=${JAVA_HOME}/lib/tools.jar
hadoop com.sun.tools.javac.Main HealthCare.java
jar cf healthcare.jar HealthCare*.class
hadoop fs -mkdir /user/hadoop/input
hadoop fs -copyFromLocal /home/hadoop/Medicare_Provider_Util_Payment_PUF_CY2012.txt /user/hadoop/input
hadoop jar healthcare.jar HealthCare /user/hadoop/input /user/hadoop/output
hadoop fs -cat /user/hadoop/output/part-r-00000 > results.txt

echo "Results stored in results.txt"

python convert.py
python viznew.py
echo "visualization image fraud.png created"
