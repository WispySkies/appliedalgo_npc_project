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
        echo "PASSED"
    else
        echo "FAILED"
        echo "${test_case}/${input_file}"
    fi
}

run_test_cases() {
    test_case_dir="$1"
    pass_count=0
    fail_count=0
    for input_file in "${test_case_dir}"/*; do
        test_case=$(basename "${test_case_dir}")
        input_file=$(basename "${input_file}")
        result=$(compare_results "${test_case}" "${input_file}")
        if [ "$result" == "PASSED" ]; then
            pass_count=$((pass_count + 1))
        else
            fail_count=$((fail_count + 1))
        fi
    done
    echo ">${test_case_dir}"
    echo "Passed: ${pass_count}"
    echo "Failed: ${fail_count}"
    return $pass_count
}

# Iterate test case sub directories
main() {
    total_pass=0
    total_fail=0
    echo "Approximate Min Graph Coloring Tests"
    for test_case_dir in "${TEST_CASES_DIR}"/*; do
        if [ -d "${test_case_dir}" ]; then
            run_test_cases "${test_case_dir}"
            pass_count=$?
            total_pass=$((total_pass + pass_count))
            total_fail=$((total_fail + fail_count))
        fi
    done
    echo "Total Passed: ${total_pass}"
    echo "Total Failed: ${total_fail}"
}

main