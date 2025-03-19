FROM leonhrt/dev-images-hub:nutria-testagent-base
WORKDIR /app
COPY ./app/ /app/app/
WORKDIR /app/app/
EXPOSE 8000
ENTRYPOINT ["uvicorn", "app.main:app"]
CMD ["--host", "0.0.0.0", "--port", "8000"]
