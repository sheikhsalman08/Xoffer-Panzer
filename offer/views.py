from django.shortcuts import render,render_to_response
from django.template import RequestContext
from models import Offer

def offer(request):
	if request.method == 'POST':
		name = request.POST['name']
		brand_name = request.POST['brand_name']
		address = request.POST['address']
		created_date = request.POST['created_date']
		last_update_date = request.POST['last_update_date']
		details = request.POST['details']
		starting = {'date':request.POST['starting_date'],'month':request.POST['starting_month'],'year':request.POST['starting_year']}
		ending = {'date':request.POST['ending_date'],'month':request.POST['ending_month'],'year':request.POST['ending_year']}
		img_url = request.POST['img_url']
		keywords = request.POST['keywords']
		shoping_mall = request.POST['shoping_mall']
		category = request.POST['category']
		sub_category = request.POST['sub_category']
		

		print(request.POST['last_update_date'])
		offer = Offer(
					name = name, 
					brand_name = brand_name, 
					address = [address,],
					created_date = created_date,
					last_update_date = last_update_date,
					details = details,
					starting = starting,
					ending = ending,
					img_url = [img_url,],
					keywords = [keywords,],
					shoping_mall = [shoping_mall,],
					category = [category,],
					sub_category = [sub_category,],
					)
		offer.save()

	offers = Offer.objects()
	context = {
		"offers":offers,
	}
	return render(request,"form.html",context)