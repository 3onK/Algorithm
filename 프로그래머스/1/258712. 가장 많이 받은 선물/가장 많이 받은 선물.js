

function solution(friends, gifts) {
    const record = new Array(friends.length).fill(0).map(_ => new Array(friends.length).fill(0));
    const point = new Array(friends.length).fill(0);
    const next = new Array(friends.length).fill(0);
    let result = 0;
    
    //내역 정리
    gifts.forEach(e => {
        const [from, to] = e.split(" ");
        record[friends.findIndex(name => name === from)][friends.findIndex(name => name === to)]++;
    })
    
    //지수 계산
    for(let i=0; i<friends.length; i++){
        point[i] = record[i].reduce((acc, cur) => acc += cur, 0);
        
        for(let j=0; j<friends.length; j++){
            point[i] -= record[j][i];
        }
    }
    
    //다음달 선물 계산
    for(let i=0; i<friends.length; i++){
        for(let j=i+1; j<friends.length; j++){
            if(i===j) continue;
            if(record[i][j] > record[j][i]) next[i]++;
            if(record[i][j] < record[j][i]) next[j]++;
            if(record[i][j] == record[j][i]){
                if(point[i] > point[j]) next[i]++;
                if(point[i] < point[j]) next[j]++;
            }
        }
    }

    //최대 선물 수
    result = Math.max(...next);
    return result;
}