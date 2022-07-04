


const getBlog = async () => {


        const requestData = {
            name:'Dmytro',
            surname:'Shevchenko',
            languages:{
                'Ukrainian':{
                    level:'Good'
                },
                'English':{
                    level:'Very good'
                },
            }
        }

        const token = 'ssssssss'

        // fetch('http://localhost:8000/students/api',{
        //     method:"GET",
        //     headers:{
        //         "Content-Type":"application/json",
        //         "Authentication":token
        //     },
        //     // body:JSON.stringify(requestData)
        // }
        // ).then((data) => {
        //     console.log(data.json())
        //     return data.json()
        // })

        // await/async

        const students = await fetch('http://localhost:8000/students/api')

        console.log( students )

        return fetch('http://localhost:8000/students/api').then((data) => {
            return data.json()
        }).catch((error) => {
            console.log(error)
            return error;
        })

}

export default getBlog