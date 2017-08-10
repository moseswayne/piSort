import BigNumber from 'bignumber.js'

class BigNum extends BigNumber {
  combinations (spaces) {
    let s = this.toString().replace(/[.,]/, '')

    let indexCombs = [];
    let getIndexCombs = (startInd, spacesLeft, comb) => {
      if (spacesLeft === 0) {
        indexCombs.push(comb)
        return
      }
      for (let i = startInd + 1; i <= s.length - spacesLeft; i++) {
        let tmp = comb.slice()
        tmp.push(i)
        getIndexCombs(i, spacesLeft - 1, tmp)
      }
    }
    getIndexCombs(0, spaces, [])
    return indexCombs.map(splitSpots => {
      let strComb = new Array(spaces + 1)
      strComb[0] = s.slice(0, splitSpots[0])
      for (let i = 0; i < splitSpots.length - 1; i++) {
        strComb[i + 1] = s.slice(splitSpots[i], splitSpots[i + 1])
      }
      strComb[spaces] = s.slice(splitSpots[spaces - 1])
      return strComb
    })
  }
}

export default BigNum;
