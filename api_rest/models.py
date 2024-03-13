from django.db import models


class Game(models.Model):
    class Meta:
        app_label = 'api_rest'

    def __str__(self):
        pass

    def dataFormat(data):
        lines = data.split("\n")
        result = {
            'status': 'success',
            'n': None,
            'k': None,
            'rq': None,
            'cq': None,
            'obstacles': []
        }

        try:
            result['n'] = int(lines[0].split(" ")[0])
            result['k'] = int(lines[0].split(" ")[1])
        except (IndexError, ValueError):
            result['status'] = 'error'
            result['message'] = 'The first line should contain two integers space-separated.'
            return result

        try:
            result['rq'] = int(lines[1].split(" ")[0])
            result['cq'] = int(lines[1].split(" ")[1])
        except (IndexError, ValueError):
            result['status'] = 'error'
            result['message'] = "The second line should contain two integers space-separated."
            return result

        for i in range(2, len(lines)):
            try:
                obstacles = [int(lines[i].split(" ")[1]),
                             int(lines[i].split(" ")[0])]
                result['obstacles'].append(obstacles)
            except (IndexError, ValueError):
                result['status'] = 'error'
                result['message'] = "The line " + \
                    (i+1) + "should contain two integers space-separated."
                return result

        return result

    def queensAttack(n, k, rq, cq, obstacles):

        if n < 1 or n > 10**5 or k < 0 or k > 10**5:
            return {'status': 'Error, n or k out of allowed range (1 to 10000)'}

        conjunto = []

        for x in range(cq, 0, -1):
            data = [x, rq]
            if data in obstacles:
                break
            if data == [cq, rq]:
                continue
            conjunto.append(data)

        aux = 0
        for x in range(cq-1, 0, -1):
            aux += 1
            y = rq - aux
            if y < 1 or x < 1:
                break

            data = [x, y]
            if data in obstacles:
                break
            if data == [cq, rq]:
                continue
            conjunto.append(data)

        for x in range(cq, n + 1):
            data = [x, rq]
            if data in obstacles:
                break
            if data == [cq, rq]:
                continue
            conjunto.append(data)

        aux = 0
        for x in range(cq + 1, n + 1):
            aux += 1
            y = rq + aux
            if y > n or x > n:
                break

            data = [x, y]
            if data in obstacles:
                break
            if data == [cq, rq]:
                continue
            conjunto.append(data)

        for y in range(rq, 0, -1):
            data = [cq, y]
            if data in obstacles:
                break
            if data == [cq, rq]:
                continue
            conjunto.append(data)

        aux = 0
        for y in range(rq-1, 0, -1):
            aux += 1
            x = cq + aux
            if y < 1 or x < 1 or x > n:
                break
            data = [x, y]
            if data in obstacles:
                break
            if data == [cq, rq]:
                continue
            conjunto.append(data)

        for y in range(rq, n + 1):
            data = [cq, y]
            if data in obstacles:
                break
            if data == [cq, rq]:
                continue
            conjunto.append(data)

        aux = 0
        for y in range(rq + 1, n + 1):
            aux += 1
            x = cq - aux
            if x < 1 or y < 1:
                break
            data = [x, y]
            if data in obstacles:
                break
            if data == [cq, rq]:
                continue
            conjunto.append(data)

        return {'status': 'success',
                'options': conjunto,
                'n': n,
                'k': k,
                'rq': rq,
                'cq': cq,
                'obstacles': obstacles,
                'options_number': len(conjunto)
                }
