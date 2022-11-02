FROM public.ecr.aws/lambda/python:3.9

COPY . ${LAMBDA_TASK_ROOT}

RUN {{cookiecutter.runtime}} -m pip install -r requirements.txt -t .

# Command can be overwritten by providing a different command in the template directly.
CMD ["main.main"]
