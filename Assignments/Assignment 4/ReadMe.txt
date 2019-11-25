Currently no ui implemented, and it does not print the order results, but otherwise the rest
of the features should work if you hardcode in a path.


Question 1:
	You would add a Goosie factory extending BrandFactories with the same methods as the others. Add one more
	if statement in order_processor to check for goosie in the brand column.
Question 2:
	You would have to add a create_women_pants method to the factories, add another if statement to determine_garment
	to check for pants.