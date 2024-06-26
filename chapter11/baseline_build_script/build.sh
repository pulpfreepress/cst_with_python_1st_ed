#!/bin/bash

# Global Constants
declare -r SRC_DIR="src"
declare -r TESTS_DIR="tests"
declare -r DOCS_DIR="docs"

# TOOLS: A list of required tools. Edit as required. 
declare -r TOOLS="git python3 pipenv"

# Global Variables 
declare _confirm=1

check_tools() { 	
	echo "Checking for required tools..."
	for tool in $TOOLS
	do
		command -v $tool &> /dev/null && \
		([ $_confirm -eq 1 ] && echo "$tool: OK" || true) || \
		(echo "$tool: MISSING"; exit 1);
	done
}

display_usage() {
	echo
	echo " Usage: "
	echo "   ./`basename $0` [ no argument | --checktools | --help | "
	echo "                --install | --runmain | --runtests | "
	echo "                --docstrings ] "
	echo 
	echo " Examples: "
	echo "   $0                # Default: --checktools and --help"
	echo "   $0 --checktools   # Check for required tools"
	echo "   $0 --help         # Show this message"
	echo "   $0 --install      # pipenv install && install --dev"
	echo "   $0 --runmain      # pipenv run python3 $SRC_DIR/main.py"
	echo "   $0 --runtests     # pipenv run pytest $TESTS_DIR/"
	echo "   $0 --docstrings   # pipenv run pydocstyle $SRC_DIR/"
	echo 
}

default_action() {
 	check_tools
 	display_usage	
}

runtests() {
	pipenv run pytest $TESTS_DIR/
}

runmain() {
	if [[ "$OSTYPE" == "linux-gnu"*  ]]; then
	    pipenv run python3 $SRC_DIR/main.py
    elif [[ "$OSTYPE" == "darwin"*  ]]; then
        pipenv run python3 $SRC_DIR/main.py
    elif [[ "$OSTYPE" == "msys"* ]]; then
        pipenv run python $SRC_DIR/main.py
    else
        echo "Unknown execution environment. "
		echo "Edit build.sh and add your os type to the runmain() method"
    fi
}

install() {
	pipenv install --dev
	pipenv install
}

check_doc_strings() {
	pipenv run pydocstyle -v $SRC_DIR/
}

process_arguments() {
	case $1 in
		--help) # Display usage and help screen
			display_usage 
			help
			;;
		--checktools) # Verfy required tools are installed
			check_tools
			;;
		--runtests)  # Run all tests
			runtests
			;;
		--runmain) # Run application
			runmain
			;;
		--install) # install all packages listed in Pipfile
			install
			;; 
		--docstrings) # Check source files for valid docstrings
			check_doc_strings
			;;	
		*) 	
			default_action
	esac
}

main(){
	process_arguments "$1"
	exit 1
}

# Call main() with all command-line arguments
main "$@"
