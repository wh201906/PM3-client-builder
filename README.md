# PM3 Client Builder

Build multiple clients of [Proxmark3 RRG repo](https://github.com/RfidResearchGroup/proxmark3)(for Windows) in parallel by GitHub Action.  

## Usage
1. Fork this repo  
2. Go to `Actions` then enable it.  
(If you don't want to affect your contribution chart, you can create a new branch then do the following steps)  
3. Change the `config.json`  
4. Push a commit to this repo or click `Run workflow` in `Actions`  
5. Check and download the clients in `Actions`->the latest workflow run->`Artifacts`  

## Examples of `config.json`

### Build 3 versions on 4 platforms 

<details>
<summary>config.json</summary>


```
{
    "refs": [
        "master",
        "v4.16191",
        "v4.15864"
    ],
    "platforms": [
        "PM3RDV4",
        "PM3GENERIC",
        "RDV4BTADDON",
        "GENERICWITHFLASH"
    ]
}
```

</details>
