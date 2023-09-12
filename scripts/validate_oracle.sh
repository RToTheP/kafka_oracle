curl -i -X PUT -H "Accept:application/json" \
  -H "Content-Type:application/json" \
  localhost:8083/connector-plugins/io.debezium.connector.oracle.OracleConnector/config/validate \
  -d @scripts/register_oracle.json