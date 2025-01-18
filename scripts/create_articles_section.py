
import json

article_html = '''
<article class="style1">
	<span class="image">
		<img src="__image__" alt="" />
	</span>
	<a href="__link__" target="_blank">
		<h2>__title__</h2>
		<div class="content">
			<p>__description__</p>
		</div>
	</a>
</article>
'''

# load json
with open('scripts/articles.json') as f:
    data = json.load(f)

output = ''
for article in data:
    article_string = article_html.replace('__image__', article['image'])
    article_string = article_string.replace('__link__', article['link'])
    article_string = article_string.replace('__title__', article['title'].capitalize())
    article_string = article_string.replace('__description__', article['description'].capitalize())
    output += article_string

with open('articles_section.txt', 'w+') as f:
    f.write(output)