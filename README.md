# elasticsearch-open5e
Messing around with creative commons open5e json files

Setup python environment
```
python3 -m venv env
source env/bin/activate
pip install -r requirements.txt
```

* Create your elasticsearch cluster
* add a role (see devtool command below)
* create a user / passowrd 
* set that user in the run.sh environment variables



Credential for elasticsearch indexing role

```json
POST /_security/role/open5e_role
{
  "cluster": [
    "manage_index_templates",
    "manage_ilm",
    "monitor"
  ],
  "indices": [
    {
      "names": [
        "open5e-*"
      ],
      "privileges": [
        "manage",
        "index",
        "create_index",
        "create"
      ]
    }
  ]
}
```