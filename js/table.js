//https://www.convertcsv.com/csv-to-json.htm to convert csv-to-json

$.ajax(
{type: 'GET',
datatype: 'JSON',
async: false,
url:"src/Employee%20Location.json",
success: function(data){
	data.forEach(function(item){
		const id = item["Sit ID"].toString();
	    	const Pid = "Pin "+id;
	    	const Cid = "Content "+id;
	    	const Piid = "Pic "+id;
	    	const CTid = "ConTittle "+id;
	    	const Stid = "Status "+id;
	    	const Eid = "Email "+id;
	    	const Phid = "Phone "+id;
			const LLid = "LL "+id;
			const LLcid = "LLc "+id;
			let url = "";
			if(item["Image"].includes("https://drive.google.com/file/d/")){
				url=item["Image"].replace("https://drive.google.com/file/d/","").split("/")[0];
				url="https://drive.google.com/uc?export=view&id="+url;
			}
		if(document.getElementById(Pid)){
			let dc = "0";
			let exten ="";
			if(item["Status"].includes("Intern")){
				dc = "1";
			}
			else if(item["Status"].includes("Perm")){
				dc = "2";
			}
			if(item["Extension"]!=undefined){
				exten=item["Extension"]+": ";
			}
			document.getElementById(Pid).setAttribute("data-category",dc);
			document.getElementById(Cid).setAttribute("data-category",dc);
			document.getElementById(CTid).innerHTML=exten+item["Name"]+"("+item["Sit ID"]+")";
			document.getElementById(Piid).src=url;
			document.getElementById(Stid).innerHTML+=item["Status"];
			document.getElementById(Eid).innerHTML+=item["Email"];
			document.getElementById(Phid).innerHTML+=item["Phone"];
			document.getElementById(LLid).setAttribute("data-category",dc);
			document.getElementById(LLid).setAttribute("class","list__item");
			document.getElementById(LLcid).setAttribute("class","list__link");
			document.getElementById(LLcid).innerHTML=item["Name"];
		}
	});
}});
