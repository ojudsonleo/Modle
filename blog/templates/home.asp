<h1>Post</h1>

<ul>
{% for post in object_list %}
    <li><a href="{% url 'article-detail' post.pk %}">{{ post.title }}</a> - {{ post.author.first_name }} {{ post.author.last_name }}<br/>
    {{ post.body }}</li><br/>

{% endfor %}
</ul>