from rtmbot.core import Plugin


class RepeatPlugin(Plugin):

    def process_message(self, data):
        if data['channel'].startswith("D"):
            self.outputs.append(
                [data['channel'], 'from repeat1 "{}" in channel {}'.format(
                    data['text'], data['channel']
                )]
            )

    def process_desktop_notification(self, data):
        pass

# https://github.com/slackapi/python-rtmbot/issues/83
