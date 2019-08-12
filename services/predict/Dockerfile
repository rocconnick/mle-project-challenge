FROM continuumio/miniconda3:latest

ADD conda_environment.yml .
RUN conda update -n base -c defaults conda && \
    conda env create -f ./conda_environment.yml

ADD predict.py .

# Default port for Flask applications
EXPOSE 5000

CMD ["conda", "run", "-n", "loanApp", "python", "predict.py"]
