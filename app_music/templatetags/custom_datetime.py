from django import template
from datetime import datetime
register = template.Library()


@register.filter
def date_spiliter(date):
	pass
	# return date.strftime('%Y-%m-%d') 
@register.filter
def rating (rate):
	html = ''
	for i in range (5):
		active = None
		if rate > i:
			acitve = style = 'color:#ffd700'
		html +=f'''
			 <input type="radio" id="star{i}" name="rating" value="1" /><label class = "full" {active}for="star1" title="Sucks big time - 1 star"></label>
    <input type="radio" id="starhalf" name="rating" value="half" /><label class="half" {active}for="starhalf" title="Sucks big time - 0.5 stars"></label>
			'''
	return html 