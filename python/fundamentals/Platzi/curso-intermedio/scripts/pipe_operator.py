test_list = [{
	'numero': 1,
},
{
	'numero': 2,
},
{
	'numero': 3
}]

test_dict = list(map(lambda pair: pair | {'mayor': pair['numero'] > 1}, test_list))
print(test_dict)