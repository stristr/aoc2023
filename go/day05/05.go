package main

import (
	"fmt"
	"io"
	"math"
	"os"
	"regexp"
	"strconv"
	"strings"
)

type interval struct {
	l, r uint64
}

type rule struct {
	dst, src, d uint64
}

type rules []*rule

type puzzle struct {
	input  []string
	data   []rules
	a      []uint64
	b      []*interval
	ranges []*interval
}

func toInt(s string) uint64 {
	n, _ := strconv.Atoi(s)
	return uint64(n)
}

func max(ns ...uint64) uint64 {
	nMax := uint64(0)
	for _, n := range ns {
		if n > nMax {
			nMax = n
		}
	}
	return nMax
}

func min(ns ...uint64) uint64 {
	nMin := uint64(math.MaxUint64)
	for _, n := range ns {
		if n < nMin {
			nMin = n
		}
	}
	return nMin
}

func (i interval) String() string {
	return fmt.Sprintf("[%d, %d)", i.l, i.r)
}

func (r rules) applyRules(a uint64) uint64 {
	for _, rule := range r {
		if rule.src <= a && a < rule.src+rule.d {
			return rule.dst + a - rule.src
		}
	}

	return a
}

func (r rules) applyRanges(ranges []*interval) ([]*interval, []*interval) {
	var nextRanges, b []*interval
	for _, nextRule := range r {
		nextRanges = nil
		L, R := nextRule.src, nextRule.src+nextRule.d
		for _, rng := range ranges {
			if rng.l < R && L < rng.r {
				b = append(b, &interval{
					l: nextRule.dst + max(rng.l, L) - nextRule.src,
					r: nextRule.dst + min(rng.r, R) - nextRule.src,
				})
			}
			if rng.l > R || rng.r < L {
				nextRanges = append(nextRanges, rng)
			}
			if rng.l < L && L < rng.r {
				nextRanges = append(nextRanges, &interval{
					l: rng.l,
					r: L,
				})
			}
			if rng.l < R && R < rng.r {
				nextRanges = append(nextRanges, &interval{
					l: R,
					r: rng.r,
				})
			}
		}
		ranges = nextRanges
	}

	return append(nextRanges, b...), b
}

func (p *puzzle) readSeeds() {
	seedsMatches := regexp.MustCompile("\\d+").FindAllString(p.input[0], -1)
	p.a = make([]uint64, len(seedsMatches))
	for i, n := range seedsMatches {
		p.a[i] = toInt(n)
	}
}

func (p *puzzle) readData() {
	p.data = make([]rules, len(p.input)-1)
	for i, chunk := range p.input[1:] {
		lines := strings.Split(chunk, "\n")
		p.data[i] = make(rules, len(lines)-1)
		for j, line := range lines[1:] {
			parts := strings.Split(line, " ")
			p.data[i][j] = &rule{
				dst: toInt(parts[0]),
				src: toInt(parts[1]),
				d:   toInt(parts[2]),
			}
		}
	}
}

func (p *puzzle) readRanges() {
	p.ranges = make([]*interval, len(p.a)/2)
	for i := 0; i < len(p.a)/2; i++ {
		p.ranges[i] = &interval{
			l: p.a[i*2],
			r: p.a[i*2] + p.a[i*2+1],
		}
	}
}

func (p *puzzle) solve() {
	for _, r := range p.data {
		for i, a := range p.a {
			p.a[i] = r.applyRules(a)
		}
		p.ranges, p.b = r.applyRanges(p.ranges)
	}

	bs := make([]uint64, len(p.b))
	for i, b := range p.b {
		bs[i] = b.l
	}

	println("a", min(p.a...))
	println("b", min(bs...))
}

func main() {
	b, _ := io.ReadAll(os.Stdin)
	p := puzzle{input: strings.Split(strings.TrimSpace(string(b)), "\n\n")}
	p.readSeeds()
	p.readData()
	p.readRanges()
	p.solve()
}
