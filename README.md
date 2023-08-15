[![Deploy with Vercel](https://vercel.com/button)](https://vercel.com/new/clone?repository-url=https%3A%2F%2Fgithub.com%2Fvercel%2Fexamples%2Ftree%2Fmain%2Fpython%2Fflask&demo-title=Flask%20%2B%20Vercel&demo-description=Use%20Flask%202%20on%20Vercel%20with%20Serverless%20Functions%20using%20the%20Python%20Runtime.&demo-url=https%3A%2F%2Fflask-python-template.vercel.app%2F&demo-image=https://assets.vercel.com/image/upload/v1669994156/random/flask.png)

# backl.io

This is a minimal example for backl.io's messaging api. It creates a email message containing several information of the page (owner) you want to reach out to:

- name of the recipient
- title of the page
- sub-title under which the link of your competitor was found


## Running Locally

```bash
npm i -g vercel
vercel dev
```

Your Flask application is now available at `http://localhost:3000`.

### Expose it to the internet

Serveo offers a great free way to expose your local server to the internet:

`ssh -R {identifier}:80:localhost:3000 serveo.net`

Your server is now available at `http://{identifier}.serveo.net`.

