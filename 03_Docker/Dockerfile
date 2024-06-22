FROM python:3.10-slim

WORKDIR /app
COPY api_holidays/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY api_holidays/ .

#Execute Python script
CMD ["python3", "./api_holidays/api_holidays.py"]