# Big Data Processing Platform
## Running
> flask run

You may need to modify some configurations to allow cross-domain access:

Generate config file
> jupyter notebook --generate-config

Then add config in ~/.jupyter/jupyter_notebook_config.py:
```
c.NotebookApp.allow_origin = '*'  
c.NotebookApp.tornado_settings = {  
    "headers": {  
        "Content-Security-Policy": "frame-ancestors   self http://localhost:5000; report-uri   /api/security/csp-report"  
    }  
}
``` 