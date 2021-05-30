import React, { useCallback, useState } from "react";
import { useRegister } from "./components";
import { CustomerServiceOutlined } from "@ant-design/icons";
import { Button } from "antd";
import { library, generateRespones, RenderList } from "./components/index";

//text是语句，reg会生成正则匹配，useReg会使用自定义匹配
library.push(
	//语料库，push进去，也可以不用
	{
		text: "我是机器人",
		reg: "你是谁",
	},
	{
		text: "author is yehuozhili",
		useReg: /(.*?)作者是谁(.*?)/,
	},
	{
		text: <CustomerServiceOutlined></CustomerServiceOutlined>,
		useReg: /(.*?)表情(.*?)/,
	},{
		text:'神湾镇公安分局办证大厅\n' +
			'\n' +
			'办理地点：中山市神湾镇神湾大道中52号（神湾镇公安分局办证大厅）公安业务窗口\n' +
			'\n' +
			'办公电话：0760-23186007\n' +
			'\n' +
			'办公时间：星期一至星期五：上午09:00-12:00，下午13:30-17:00（法定节假日除外）\n' +
			'\n' +
			'位置指引：乘坐206、613、935路公共汽车在彩虹路口站下车，往鹿角树村方向步行约100米到达神湾镇公安分局办证大厅',
		useReg: /(.*?)通行证(.*?)/,
	},{
		text:<span>
			你是不是想找？
			<p><a>无线电频率使用许可（注销）(无线电频率使用许可（行政机关注销）)</a></p>
			<p><a>无线电频率使用许可（遗失补办）(无线电频率使用许可（其他组织遗失补办）)</a></p>
			<p><a>无线电频率使用许可（变更）(行政机关变更)</a></p>
		</span>,
		useReg: /(.*?)无线电(.*?)/,
	}
);

function App() {
	const [modalOpen, setModalOpen] = useState(false);
	//使用useCllback避免用户输入时调用匹配！！！！！！！
	const callb = useCallback((v: RenderList) => {
		setTimeout(async () => {
			//使用settimeout 更像机器人回话
			let returnValue = await generateRespones(v);
			if (returnValue) {
				//排除null
				setList((prev) => [
					...prev,
					{ isUser: false, text: returnValue },
				]);
			}
		}, 500);
		// eslint-disable-next-line react-hooks/exhaustive-deps
	}, []);

	// 注册
	const [render, setList] = useRegister(
		modalOpen,
		callb,
		{
			onOk: () => setModalOpen(false),
			onCancel: () => setModalOpen(false),
			title: "政务领域问答机器人",
		},
		{},
		<div>welcome，请问有什么能帮助您的？</div>
	);

	return (
		<div>
			<div
				style={{
					position: "fixed",
					right: "10px",
					top: "40%",
				}}
			>
				<Button type="primary" onClick={() => setModalOpen(!modalOpen)}>
					<CustomerServiceOutlined></CustomerServiceOutlined>
				</Button>
			</div>
			{render}
		</div>
	);
}

export default App;
