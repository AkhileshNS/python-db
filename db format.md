Departments = 

{

​	(did) : {

​						'did' : autonum() + year + sem,

​						'name' : '',

​						'long name' : '',

​						'hod' : (fid ''),

​						...

​				}

}

Faculty = 

{

​	(fid) : {

​						'fid' : autonum() + year + sem,

​						'name' : '',

​						'dept aff.' : (did ''),

​						('ufn' (univarsal faculty number) : '',)

​						...

​				}

}

Courses = 

{

​	(cid) : {

​						'cid' : autonum() + year + sem,

​						'name' : '',

​						'ucid' (universal course id) : '',

​						sheets : [],

​						'dept' : (did ''),

​						...

​				}

}