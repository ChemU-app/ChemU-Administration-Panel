class GlobalState:
    containerIDs=[]
    names=[]
    images=[]
    created=[]
    status=[]
    ports=[]
    
    def updateDockerInformation(self, client):
        stdin, stdout, stderr = client.exec_command("docker ps --format \"{{.Names}}'{{.ID}}'{{.CreatedAt}}'{{.Status}}'{{.Ports}}'{{.Image}}\"")
        for line in stdout.readlines():
            if "'" in stdout.readlines():
                variables = line.split("'")
                names.append(variables[0])
                containerIDs.append(variables[1])
                created.append(variables[2])
                status.append(variables[3])
                ports.append(variables[4])
                image = variables[5]
                images.append(image[:-2])

    def getTeachers(self, client):
        stdin, stdout, stderr = client.exec_command("docker exec chemu_mongo mongosh chemu --quiet --eval \"print(EJSON.stringify(db.Teacher.find({}).toArray()))\"")
        text = stdout.readlines()[0].strip()
        if text.endswith(r"\n"):
            text = text[:-2]
        return json.loads(text)

    def getStudents(self, client):
        stdin, stdout, stderr = client.exec_command("docker exec -it chemu_mongo mongosh chemu --eval 'db.Student.find({}).toArray()'")
        return json.loads(stdout.readlines())
