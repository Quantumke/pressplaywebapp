from django.shortcuts import get_object_or_404, render_to_response,render
from blog.models import Entry, Link, Category,fakeusers
from django.template import RequestContext
from datetime import datetime, timedelta
from django.contrib.comments.models import Comment
from django.db.models import F
from django.contrib.auth.models import User
import random
# Create your views here.

def entries_index(request):
	marque=Entry.objects.all().order_by('-pub_date')[:3]
	newest=Entry.objects.filter(pub_date=datetime.today())[:4]
	new_stories=Entry.objects.filter(pub_date=datetime.today())
	last_story=Entry.objects.filter(pub_date=datetime.today())[:1]
	lastest_story=Entry.objects.filter(pub_date=datetime.today())[:5]
	categories=Category.objects.all()
#	new_stories=new_stories.count()
	featured=Entry.objects.filter(featured=True).order_by('-pub_date')[:4]
	exclusive=Entry.objects.filter(tags='exclusive')[:3]
	exclusives=Entry.objects.filter(tags='exclusive').order_by('-pub_date')[:1]
	event=Entry.objects.filter(tags='events').order_by('-pub_date')[:1]
	events=Entry.objects.filter(tags='events').order_by('-pub_date')
	grapevine=Entry.objects.filter(tags='grapevine').order_by('-pub_date')[:1]
	grapevines=Entry.objects.filter(tags='grapevine').order_by('-pub_date')
	politic=Entry.objects.filter(tags='politics').order_by('-pub_date')[:1]
	politics=Entry.objects.filter(tags='politics').order_by('-pub_date')
	lifestyle=Entry.objects.filter(tags='lifestyle').order_by('-pub_date')[:1]
	lifestyles=Entry.objects.filter(tags='lifestyle').order_by('-pub_date')
	item_small=Entry.objects.all().order_by('-pub_date')[:4]
	xtrending=Entry.objects.order_by('-count')[:6]
	popular=Entry.objects.order_by('-count')[:5]
	trending=Entry.objects.filter(count__gte=9)[:5]
	hot=Entry.objects.filter(tags='hot').order_by('-pub_date')[:5]

	#trending = Entry.objects.filter(pub_date__lt=F('pub_date') - timedelta(days=1)).order_by('-count')[:5]
	last_month= datetime.today() - timedelta(days=30)
	featured_last_month = Entry.objects.filter(pub_date__lt=F('pub_date') - timedelta(days=30))
	all_stories=Entry.objects.all().order_by('-pub_date')[:15]
	sponserd=Entry.objects.filter(tags='sponsored').order_by('-pub_date')[:5]
	campus=Entry.objects.filter(tags='campus').filter(featured=True).order_by('-pub_date')[:1]
	politics=Entry.objects.filter(tags='politics').filter(featured=True).order_by('-pub_date')[:1]
	f_campus=Entry.objects.filter(tags='campus').order_by('-pub_date')[:5]
	f_politics=Entry.objects.filter(tags='politics').order_by('-pub_date')[:5]
	#popular=Entry.objects.filter(tags='popular').order_by('-pub_date')[:5]
	recent=Entry.objects.all().order_by('-pub_date')[:5]
	comments=Comment.objects.all().order_by('-submit_date')[:5]
	#trending=Entry.objects.all().order_by('-pub_date')[:5]
	most_recent=Entry.objects.all().order_by('-pub_date')[:1]
	#print most_recent
	other_recent=Entry.objects.all().order_by('-pub_date')[:3]
	news=Entry.objects.filter(tags='news').order_by('-pub_date')[:4]
	count_more_stories=Entry.objects.filter(tags='news')
	count_more_stories=count_more_stories.count()
	count_more_stories=	count_more_stories-4
	count_today_unread=newest.count()
	count_today_unread=count_today_unread-4
	sel_random=[27,35,15,32,31,12,10,19,5,6,34,28,23]
	ran=random.choice(sel_random)

	return render_to_response('index.html',
							  {'entries': Entry.objects.all(),
							   'marque':marque,
							   'new_stories':new_stories,
							   'featured':featured,
							   'last_story':last_story,
							   'exclusives':exclusives,
							   'exclusive':exclusive,
							   'event':event,
							   'events':events,
							   'grapevine':grapevine,
							   'grapevines':grapevines,
							   'all_stories':all_stories,
							   'politics':politics,
							   'sponserd':sponserd,
							   'hot':hot,
							   'popular':popular,
							   'recent':recent,
							   'comments':comments,
							   'trending':trending,
							   'lastest_story':lastest_story,
							   'other_recent':other_recent,
							   'news':news,
							   'count_more_stories':count_more_stories,
							   'categories':categories,
							   'ran':ran,

							   })



def view_more(request, slug):
	#count=Entry.objects.get(slug=slug)
	#print count
	next_issue = Entry.objects.get(slug=slug)
	current_id= next_issue.pk
	next_iem_id= current_id+1
	previous_id=current_id-1
	last_id=Entry.objects.latest('id')
	last_id= last_id.pk
	if next_iem_id > last_id:
		next_item = Entry.objects.get(id=current_id - 1)
	else:
		next_item = Entry.objects.get(id=next_iem_id)
	if previous_id == 0:
		previous_item=Entry.objects.get(id=current_id+1)
	else:
		previous_item=Entry.objects.get(id=current_id-1)
	next_item_slug= next_item.slug
	next_item_title=next_item.title
	next_item_pic=next_item.image1
	next_item_pic2=next_item.image2
	previous_item_slug=previous_item.slug
	previous_item_title=previous_item.title
	previous_item_pic=previous_item.image1
	previous_item_pic2=previous_item.image2
	marque = Entry.objects.all().order_by('-pub_date')[:3]
	trending = Entry.objects.all().order_by('-pub_date')[:5]
	recent = Entry.objects.all().order_by('-pub_date')[:5]
	comments = Comment.objects.all().order_by('-submit_date')[:5]
	cats = Category.objects.all()
	# user = User.objects.get(username=request.user.username)
	# bio=fakeusers.objects.filter(user=user)
	o=Entry.objects.get(slug=slug)
	author_id= o.author_id
	count=o.count
	new_count=count +1
	c=Entry.objects.filter(slug=slug).update(count=new_count)
	bio=User.objects.get(id=author_id)
	id= bio.id
	bio=fakeusers.objects.filter(user_id=id)
	return render_to_response('entry_detail.html',{
	'object':get_object_or_404(Entry, slug=slug),
		'marque':marque,
		'bio':bio,
		'trending':trending,
		'recent':recent,
		'comments':comments,
		'cats':cats,
		'next_item_slug':next_item_slug,
		'next_item_title':next_item_title,
		'previous_item_slug':previous_item_slug,
		'previous_item_title':previous_item_title,
		'next_item_pic':next_item_pic,
		'next_item_pic2':next_item_pic2,
		'previous_item_pic':previous_item_pic,
		'previous_item_pic2':previous_item_pic2,


	},RequestContext(request))

def search(request):
	query=request.GET.get('q', '')
	results=[]
	marque = Entry.objects.all().order_by('-pub_date')[:3]
	recent = Entry.objects.all().order_by('-pub_date')[:5]
	comments = Comment.objects.all().order_by('-submit_date')[:5]
	trending = Entry.objects.all().order_by('-pub_date')[:5]
	if query:
		results=Entry.objects.filter(title__contains=query)
		count=results.count()
	return render_to_response('search.html', {'query':query, 'results':results,
											  'marque':marque, 'count':count,
											  'recent':recent,'comments':comments,
											  'trending':trending})
def category_list(request):
	return render_to_response('category_list.html',
                                  { 'object_list': Category.objects.all() })

def category_detail(request, slug):
	return render_to_response('entry_detail.html', {
		'object': get_object_or_404(Entry, category=slug)
	}, RequestContext(request))
