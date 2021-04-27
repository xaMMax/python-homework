def make_country():  # define the function
    name = input('Please input the name of the country: ')  # use prompt for input country name
    capital = input('Please input the capital of this country: ')  # use prompt for input country name
    country_dict = {name.title(): capital.title()}  # create dictionary with defined variables
    return print(country_dict)  # print our result


make_country()  # call function
