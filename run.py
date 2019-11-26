from rlbot.utils import public_utils, logging_utils

import sys


def load_all_the_bots():
    rlbots = [module for module in sys.modules if module.startswith('rlbot')]
    for rlbot_module in rlbots:
        sys.modules.pop(rlbot_module)


if __name__ == '__main__':

    # TODO It looks like this isnt hooked up!
    # DEFAULT_LOGGER = 'rlbot'
    # logger = logging_utils.get_logger(DEFAULT_LOGGER)
    # https://stackoverflow.com/a/44401013

    load_all_the_bots()

    try:
        if len(sys.argv) > 1 and sys.argv[1] == 'gui':
            from rlbot.gui.qt_root import RLBotQTGui
            RLBotQTGui.main()
        else:
            from rlbot import runner
            runner.main()
    except Exception as e:
        print("Encountered exception: ", e)
        print("Press enter to close.")
        input()


