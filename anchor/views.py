from pyramid.view import view_config


def calc(coins, weight, num, memo):
    if weight >= len(coins):
        return 1 if num == 0 else 0
    if (weight, num) not in memo:
        count = calc(coins, weight+1, num, memo)
        count += calc(coins, weight+1, num - coins[weight], memo)
        memo[(weight, num)] = count
    return memo[(weight, num)] # return memoized value

def coin_determine(coins, num, memo):
    subset = []
    if num != None:
        num = int(num)
    else:
        num = 0
    for i, x in enumerate(coins):
        # check if there is still a solution if we include coins[i]
        if calc(coins, i+1, num - x, memo) > 0:
            subset.append(x)
            num -= x
    return subset


@view_config(route_name='home', renderer='templates/mytemplate.pt')
def my_view(request):

    coins = [1,5,7,9,11]
    memo = dict()

    project = 'Anchor'
    post_data = request.POST #request.params['result'].decode('utf-8')
    result = post_data.get('result')
    result = {'first': len(coin_determine(coins, result, memo)),
                'second': coin_determine(coins, result, memo)}

    return {'project': 'Anchor', 'result': result}