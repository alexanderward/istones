# istones

## Monitor
`python monitor.py -n demo -t 1`
- Flags
    * n = name of process.  will match anything starting with this value
    * t = polling every x seconds
    
## Forever
`python forever.py -name demo2`
- Flags
    * name = name of process spun off.
    
Limitations: Didnt' get around to realtime input.  Just spin off another script to add a new name/number. 
