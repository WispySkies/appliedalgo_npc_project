TEST_CASES_DIR="test_cases"
EXPECTED_RESULTS_DIR="expected_results"

run_min_graph_coloring() {
    test_case="$1"
    input_file="$2"
    output=$(python cs412_mingraphcolor_approx.py <"${TEST_CASES_DIR}/${test_case}/${input_file}")
    echo "${output}"
}

compare_results() {
    test_case="$1"
    input_file="$2"
    expected_output=$(<"${EXPECTED_RESULTS_DIR}/${test_case}/${input_file}")
    actual_output=$(run_min_graph_coloring "${test_case}" "${input_file}")
    if [ "$expected_output" == "$actual_output" ]; then
        echo "Test case ${test_case}/${input_file}: PASSED"
    else
        echo "Test case ${test_case}/${input_file}: FAILED"
        diff <(echo "$expected_output") <(echo "$actual_output")
    fi
}

run_test_cases() {
    test_case_dir="$1"
    echo ">${test_case_dir}"
    for input_file in "${test_case_dir}"/*; do
        test_case=$(basename "${test_case_dir}")
        input_file=$(basename "${input_file}")
        compare_results "${test_case}" "${input_file}"
    done
}

# Iterate test case sub directories
main() {
    echo "Approximate Min Graph Coloring Tests"
    for test_case_dir in "${TEST_CASES_DIR}"/*; do
        if [ -d "${test_case_dir}" ]; then
            run_test_cases "${test_case_dir}"
        fi
    done
}

main