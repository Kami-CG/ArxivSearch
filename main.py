from fastapi.staticfiles import StaticFiles
import extracting_bio_api.extract_bioapi as extract_article
from server_model.sql_folder.sql_table import adding_entries
from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse, JSONResponse
from pydantic import BaseModel
from fastapi.templating import Jinja2Templates
import uvicorn

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")

templates = Jinja2Templates(directory="templates")


class HelloWorldRequest(BaseModel):
    message: str


@app.get("/", response_class=HTMLResponse)
async def read_hello(request: Request):
    data = "Hello from FastAPI!"

    return templates.TemplateResponse("search.html", {"request": request, "data": data})


@app.post("/search")
async def search(request: Request, search: str = Form(...)):
    if search:

        url_api = f"http://export.arxiv.org/api/query?search_query=all:{search}"

        retrieved_output = extract_process(url_api)
        tranferred_articles = transfer_process(retrieved_output)
        # adding_entries(tranferred_articles)

        return HTMLResponse(content=tranferred_articles.to_html())
    else:
        return JSONResponse(status_code=400, content={"error": "No search text provided"})


def extract_process(article_api):
    api_output = extract_article.extract_data(article_api)
    return api_output


def transfer_process(extracted_articles):
    return extract_article.transfer_process(extracted_articles)


if __name__ == '__main__':
    uvicorn.run(app, host='0.0.0.0', port=8000)



