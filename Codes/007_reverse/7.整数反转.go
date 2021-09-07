/*
 * @Author: Theo_hui
 * @Date: 2021-09-07 09:44:23
 * @Descripttion:
 */
/*
 * @lc app=leetcode.cn id=7 lang=golang
 *
 * [7] 整数反转
 */

// @lc code=start
func unsignedAdd32(base *int32, add int32) error {

	if *base > math.MaxInt32-add {
		return errors.New("overflow")
	}
	*base = *base + add

	return nil
}

func reverse(x int) int {
	//取符号 屏蔽符号差异
	var symbol int32
	symbol = 1
	if x < 0 {
		symbol = -1
		x = -1 * x
	}

	var rst int32
	for {
		if x <= 0 {
			break
		}
		//rst=rst*10
		rst_copy := rst
		for i := 0; i < 9; i++ {
			err := unsignedAdd32(&rst, rst_copy)
			if err != nil {
				return 0
			}
		}
		fmt.Println(rst, x)

		//rst=rst*10+x%10
		err := unsignedAdd32(&rst, (int32)(x%10))
		if err != nil {
			return 0
		}
		fmt.Println(rst, x)

		x = x / 10
	}

	return (int)(symbol * rst)

}

// @lc code=end

