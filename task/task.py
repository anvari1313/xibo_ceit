from background_task import background


@background(schedule=60)
def task1(param):
    print('this is notifier' + param)