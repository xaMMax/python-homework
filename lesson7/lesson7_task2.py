def make_country(name, capital):  # define the function
    country_dict = {name.title(): capital.title()}  # create dictionary with defined variables
    print(country_dict)  # print our result
    return  # return function


name = input('Please input the name of the country: ')  # use prompt for input country name
capital = input('Please input the capital of this country: ')  # use prompt for input country name

make_country(name, capital)  # call function
