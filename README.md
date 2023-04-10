# elasticsearch-open5e
Messing around with creative commons open5e json files
Learn more about Open5e here [link](https://open5e.com/)

Setup python environment
```
python3 -m venv env
source env/bin/activate
pip install -r requirements.txt
```

get the data in a sister project
``` sh
cd ..
git clone https://github.com/open5e/open5e-api
cd elasticsearch-open5e
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