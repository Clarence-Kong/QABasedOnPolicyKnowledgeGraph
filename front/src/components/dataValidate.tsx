import { ReactNode } from "react";
import { RenderList } from ".";
import ajax  from 'superagent'
//这个文件与index实际分离关系。

export type libraryType = Array<{
	reg?: string;
	text: ReactNode;
	useReg?: RegExp;
}>;

export let library: libraryType = [];

/*export function generateRespones(v: RenderList): ReactNode {
	if (typeof v.text === "string") {
		for (let value of library) {
			if (value.reg) {
				//字符串全字匹配
				let r = new RegExp(value.reg);
				if (r.test(v.text)) {
					return value.text;
				}
			} else if (value.useReg && value.useReg.test(v.text)) {
				//使用自定义匹配
				return value.text;
			}
		}
		return null;
	}
	return null;
}*/


export async function generateRespones(v: RenderList) {
	if (typeof v.text === "string") {
		/*for (let value of library) {
			if (value.reg) {
				//字符串全字匹配
				let r = new RegExp(value.reg);
				if (r.test(v.text)) {
					return value.text;
				}
			} else if (value.useReg && value.useReg.test(v.text)) {
				//使用自定义匹配
				return value.text;
			}
		}*/
		const req =await ajax.get(`http://127.0.0.1:20230/que/${v.text}`)
		console.log(v, 'v')

		return req.body.msg;
	}
	return null;
}

