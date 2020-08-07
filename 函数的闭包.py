def test(name):
    def test_in():
        print(name)
    return test_in

func = test('whyz')
func()
