#!/bin/bash -i

# Stolen from Sygil-Dev/sygil-webui and mangled by moi. GPL v3. 

source "$(conda info --base)/etc/profile.d/conda.sh"

DIRECTORY="."
ENV_FILE="environment.yaml"
ENV_NAME="wudang_website"
ENV_MODIFIED=$(date -r $ENV_FILE "+%s")
ENV_MODIFIED_FILE=".env_updated"
ENV_UPDATED=0
WEBSITE="WudangNOLA_website.py"

INSTALL_ENV_DIR="$(pwd)/../installer_files/env"
if [ -e "$INSTALL_ENV_DIR" ]; then export PATH="$INSTALL_ENV_DIR/bin:$PATH"; fi

if [[ -f $ENV_MODIFIED_FILE ]]; then
	ENV_MODIFIED_CACHED=$(<${ENV_MODIFIED_FILE})
else
	ENV_MODIFIED_CACHED=0
fi

conda_env_setup () {
	CUSTOM_CONDA_PATH=

	if [ -f custom-conda-path.txt ]; then
		CUSTOM_CONDA_PATH=$(cat custom-conda-path.txt)
	fi
	if [ -f "$INSTALL_ENV_DIR/etc/profile.d/conda.sh" ] && [ "$CUSTOM_CONDA_PATH" == ""]; then
		. "$INSTALL_ENV_DIR/etc/profile.d/conda.sh"
	fi

	if [ -f "${CUSTOM_CONDA_PATH}/etc/profile.d/conda.sh" ]; then
		. "${CUSTOM_CONDA_PATH}" ] && [ -f "${CUSTOM_CONDA_PATH}/bin" ]
		export PATH= "${CUSTOM_CONDA_PATH}/bin:$PATH"
	fi

	if ! command -v conda >/dev/null; then
		printf "Conda not found. Install from here --> https://www.anaconda.com/products/distribution \n"
		exit 1
	fi

	if ! conda env list | grep ".*${ENV_NAME}.*" >/dev/null 2>&1; then
		printf "Could not find conda env: ${ENV_NAME} ... creating .. \n\n"
		conda env create -f $ENV_FILE
		ENV_UPDATED=1
	elif [[ ! -z $CONDA_FORCE_UPDATE && $CONDA_FORCE_UPDATE == "true" ]] || (( $ENV_MODIFIED > $ENV_MODIFIED_CACHED )); then
		printf "Updating conda env: ${ENV_NAME} ...\n\n"
		PIP_EXISTS_ACTION=w conda env update --file $ENV_FILE --prune
		ENV_UPDATED=1
	fi

	if (( $ENV_UPDATED > 0 )); then
	conda clean --all
	echo -n $ENV_MODIFIED > $ENV_MODIFIED_FILE
	fi
}

conda_env_activation () {
	conda activate $ENV_NAME
	conda info | grep active
}

launch_WudangNOLA_website () {
	flet $WEBSITE "$@"
}

init_site () {
	conda_env_setup
	conda_env_activation
	launch_WudangNOLA_website "$@"
}

init_site "$@"

