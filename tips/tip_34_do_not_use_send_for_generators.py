# Tip 34 do not use send() to inject data do generators
import math


# do not recommend to use it
def example_with_send():
    def my_generator():
        received = yield 1
        print(f'received = {received}')

    it = iter(my_generator())
    output = it.send(None)
    print(f'output = {output}')

    try:
        it.send('Hellow')
    except StopIteration:
        pass


def wave_cascading(amplitude_it, steps):
    step_size = 2 * math.pi / steps
    for step in range(steps):
        radians = step * step_size
        fraction = math.sin(radians)
        amplitude = next(amplitude_it)
        output = amplitude * fraction
        yield output


def complex_wave_cascading(amplitude_it):
    yield from wave_cascading(amplitude_it, 3)
    yield from wave_cascading(amplitude_it, 4)
    yield from wave_cascading(amplitude_it, 5)


def transmit(output):
    if output is None:
        print(f'Output data to None')
    else:
        print(f'Output data to: {output:>5.1f}')


def run_cascading():
    amplitudes = [7, 7, 7, 2, 2, 2, 2, 10, 10, 10, 10, 10]
    it = complex_wave_cascading(iter(amplitudes))
    for amplitude in amplitudes:
        output = next(it)
        transmit(output)


# recommend to use it
def example_without_send():
    run_cascading()


example_without_send()
example_with_send()
