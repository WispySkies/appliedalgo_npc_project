TEST_CASES_DIR="test_cases"
EXPECTED_RESULTS_DIR="expected_results"

run_min_graph_coloring() {
    test_case="$1"
    input_file="$2"
    output=$(python cs412_mingraphcolor_exact.py <"${TEST_CASES_DIR}/${test_case}/${input_file}")
    echo "${output}" > "${EXPECTED_RESULTS_DIR}/${test_case}/${input_file}"
}

run_test_cases() {
    test_case_dir="$1"
    echo ">${test_case_dir}"
    for input_file in "${test_case_dir}"/*; do
        test_case=$(basename "${test_case_dir}")
        input_file=$(basename "${input_file}")
        run_min_graph_coloring "${test_case}" "${input_file}"
    done
}

# Create expected results directory
mkdir -p "${EXPECTED_RESULTS_DIR}"

# iterate test case sub directories
main() {
    echo "Min Graph Coloring Tests"
    for test_case_dir in "${TEST_CASES_DIR}"/*; do
        if [ -d "${test_case_dir}" ]; then
            mkdir -p "${EXPECTED_RESULTS_DIR}/$(basename "${test_case_dir}")"
            run_test_cases "${test_case_dir}"
        fi
    done
}

main