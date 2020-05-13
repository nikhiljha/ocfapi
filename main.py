from fastapi import FastAPI, HTTPException
from fastapi.responses import RedirectResponse

from ocflib.misc.shorturls import get_shorturl
from ocflib.misc.shorturls import get_connection

app = FastAPI()

@app.get("/shorturl/{slug}")
def short_url(slug: str):
    if slug:
        with get_connection() as ctx:
            target = get_shorturl(ctx, slug)
            if target:
                return RedirectResponse(target, status_code=302)
    raise HTTPException(status_code=404, detail="short url not found")

