# ─────────────────────────────────────────────────────────────
# Dockerfile for PySpark Sales Analysis Application
# Installs: Java 17, Python 3.11, Apache Spark 3.5.1
# ─────────────────────────────────────────────────────────────

FROM python:3.11-slim

# ── System-level dependencies ──────────────────────────────────
RUN apt-get update && apt-get install -y --no-install-recommends \
    openjdk-17-jre-headless \
    wget \
    curl \
    procps \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# ── Java environment variable ──────────────────────────────────
ENV JAVA_HOME=/usr/lib/jvm/java-17-openjdk-amd64
ENV PATH="$JAVA_HOME/bin:$PATH"

# ── Download and install Apache Spark ─────────────────────────
ENV SPARK_VERSION=3.5.1
ENV HADOOP_VERSION=3
ENV SPARK_HOME=/opt/spark

RUN wget -q https://archive.apache.org/dist/spark/spark-${SPARK_VERSION}/spark-${SPARK_VERSION}-bin-hadoop${HADOOP_VERSION}.tgz \
    && tar -xzf spark-${SPARK_VERSION}-bin-hadoop${HADOOP_VERSION}.tgz -C /opt/ \
    && mv /opt/spark-${SPARK_VERSION}-bin-hadoop${HADOOP_VERSION} ${SPARK_HOME} \
    && rm spark-${SPARK_VERSION}-bin-hadoop${HADOOP_VERSION}.tgz

# ── Spark environment variables ────────────────────────────────
ENV PATH="$SPARK_HOME/bin:$SPARK_HOME/sbin:$PATH"
ENV PYSPARK_PYTHON=python3
ENV PYSPARK_DRIVER_PYTHON=python3

# ── Install Python dependencies ────────────────────────────────
RUN pip install --no-cache-dir pyspark==3.5.1

# ── Set working directory and copy project files ───────────────
WORKDIR /app
COPY sales.csv .
COPY sales_analysis.py .

# ── Run the PySpark application on container start ─────────────
CMD ["python", "sales_analysis.py"]
