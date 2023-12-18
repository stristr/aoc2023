package main

import (
	"fmt"
	"io"
	"os"
	"strconv"
	"strings"
	"time"
)

type Direction int64
type Int int64

const (
	Right Direction = iota
	Down
	Left
	Up
)

var directions = map[byte]Direction{
	'R': Right,
	'D': Down,
	'L': Left,
	'U': Up,
}

const ZERO Int = 0

type step struct {
	dir  Direction
	dist Int
}

type steps []*step

type vector []Int

type puzzle struct {
	input []string
	a     steps
	b     steps
}

func (i Int) Abs() Int {
	if i < ZERO {
		return -i
	}

	return i
}

func (v vector) decompose(u vector) Int {
	s := ZERO
	for i, n := range v[:len(v)-1] {
		s += n * u[i+1]
	}
	return s
}

func (s steps) dig() Int {
	x, y, p, vx, vy := ZERO, ZERO, ZERO, make(vector, len(s)), make(vector, len(s))
	for i, st := range s {
		switch st.dir {
		case Right:
			x += st.dist
		case Down:
			y += st.dist
		case Left:
			x -= st.dist
		case Up:
			y -= st.dist
		}
		p += st.dist
		vx[i] = x
		vy[i] = y
	}

	return (p+(vy.decompose(vx)-vx.decompose(vy)).Abs())/2 + 1
}

func toInt(s string) Int {
	n, _ := strconv.Atoi(s)
	return Int(n)
}

func toIntFromHex(s string) Int {
	n, _ := strconv.ParseInt(s, 16, 64)
	return Int(n)
}

func (p *puzzle) readData() {
	p.a, p.b = make(steps, len(p.input)), make(steps, len(p.input))
	for i, line := range p.input {
		parts := strings.Fields(line)
		p.a[i] = &step{
			dir:  directions[parts[0][0]],
			dist: toInt(parts[1]),
		}
		p.b[i] = &step{
			dir:  Direction(parts[2][7] - '0'),
			dist: toIntFromHex(parts[2][2:7]),
		}
	}
}

func main() {
	start := time.Now().UnixNano()
	buf, _ := io.ReadAll(os.Stdin)
	p := puzzle{input: strings.Split(strings.TrimSpace(string(buf)), "\n")}
	p.readData()
	println("a", p.a.dig())
	println("b", p.b.dig())
	// Print time in microseconds
	fmt.Printf("time: %dµs\n", (time.Now().UnixNano()-start)/1000)
}
