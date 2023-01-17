import asyncio
import tornado.web
import datetime

class IndexPage(tornado.web.RequestHandler):
    def get(self):
        e = datetime.datetime.now()
        self.write("Today's date:  = %s/%s/%s<br>" % (e.month, e.day, e.year))
        self.write("The time is now: = %s:%s:%s" % (e.hour, e.minute, e.second))

def makeApp():
    endpoints = [
        ("/", IndexPage)
    ]
    app = tornado.web.Application(endpoints)
    app.listen(8000)
    return app

if __name__ == "__main__":
    app = makeApp()
    asyncio.get_event_loop().run_forever()