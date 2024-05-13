FROM public.ecr.aws/lambda/python:3.11

COPY . ./
RUN {{cookiecutter.runtime}} -m pip install -r requirements.txt -t .
RUN chmod -R 755 .

# Command can be overwritten by providing a different command in the template directly.
CMD ["app.lambda_handler"]
