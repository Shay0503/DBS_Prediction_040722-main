#!/usr/bin/env python
# coding: utf-8

# In[1]:


from flask import Flask


# In[2]:


import joblib


# In[3]:


app = Flask(__name__)


# In[4]:


from flask import render_template, request

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        rates = request.form.get("rates")
        rates = float(rates)
        print(rates)
        model1 = joblib.load("regression")
        pred1 = model1.predict([[rates]])
        model2 = joblib.load("decision tree")
        pred2 = model2.predict([[rates]])
        return(render_template("index.html", result1=pred1, result2=pred2))
    else:
        return(render_template("index.html", result1="Waiting", result2="Waiting"))


# In[ ]:


if __name__ == "__main__":
    app.run()


# In[ ]:





# In[ ]:




