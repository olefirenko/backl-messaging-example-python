from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def home():
    return """<h4>Your backl.io messaging API is running! 🥳</h4>
    <p>Use {yourdomain}/message in the backlink builder to start using it.</p>
    <p>To adapt it, edit ✍️ <code>api/index.py</code></p>
    """

@app.route('/message')
def message():
    from pprint import pprint
    p = request.get_json()
    pprint(p)
    subject = 'Enhance Your "{prospect_title}" Site with {my_domain}'.format(**p)
    email = p["email_address"]
    if '.' in email.split('@')[0]:
        name = email.split('@')[0].split('.')[0].capitalize()
    else:
        name = 'there'

    if p['prospect_title_above_link']:
        extra_section = ' under the section "{prospect_title_above_link}"'.format(**p)
    else:
        extra_section = ''
    body = """Hi {name},

I hope this message finds you well.

I'm Dmytro, the founder of {my_domain}, a platform dedicated to helping content creators craft compelling content 10 times faster with our sophisticated AI tools.

In my research, I came across your impressive site "{prospect_title}" and noticed that you often link out to tools that empower people in the same way we do.

I wanted to bring your attention to {my_domain} and consider its potential value for your audience. Would you mind featuring a link to our site{extra_section}?

Moreover, to add icing on the cake, we have an affiliate program that generously rewards our partners with a 30% commission from all referred users' payments! You can get the nitty-gritty of this program here https://easy-peasy-ai.getrewardful.com/signup.

Thank you for considering this opportunity, {name}. I genuinely believe that {my_domain} can be a useful resource for your audience and a profitable addition for you.

Looking forward to hearing from you soon.

Best regards,
Dmytro
""".format(name=name, extra_section=extra_section, **p)
    return dict(subject=subject, body=body)
