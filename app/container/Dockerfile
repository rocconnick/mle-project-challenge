FROM continuumio/miniconda3:latest

ADD app/container/conda_environment.yml .
RUN conda update -n base -c defaults conda && \
    conda env create -f ./conda_environment.yml

ADD app/peer_loan_app.py .

# Default port for Flask applications
EXPOSE 5000

CMD ["conda", "run", "-n", "loanApp", "python", "peer_loan_app.py"]
