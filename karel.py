function main() {
    goFindTurn();
    pileColumn();
    move();
    goFindTurn();
    pileColumn();
    goKarel();
    turnAround();
    goFindTurn();
    goKarel();
    turnAround();
    breakColumn();
    turnRight();
    move();
    goFindTurn();
    goKarel();
    turnAround();
    breakColumn();
    turnLeft();
    move();
    turnLeft();
    pileColumn();
    turnAround();
    turnLeft();
    turnLeft();
    move();
    turnLeft();
    pileColumn();
    goKarel();
}

function goKarel() {
    while (frontIsClear()) {
        move();
    }
}

function goFindTurn() {
   while (noBeepersPresent()) {
	    move();
	}
    if (leftIsClear()) {
        turnLeft();
    } else {
        turnRight();
    }
}

function pileColumn() {
    if (noBeepersPresent()) {
        putBeeper();
    }
    while (frontIsClear()) {
        move();
        if (noBeepersPresent()) {
            putBeeper();
        }
    }
    turnAround();
    while (frontIsClear()) {
        move();
    }
    turnLeft();
}

function breakColumn() {
    if (beepersPresent()) {
        pickBeeper();
    }
    while (frontIsClear()) {
        move();
        if (beepersPresent()) {
            pickBeeper();
        }
    }
}

