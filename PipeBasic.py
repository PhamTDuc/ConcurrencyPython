import multiprocessing as mp


def send_message(sender):
    sender.send([2, None, "Hello the world"])
    sender.close()


if __name__ == '__main__':
    context = mp.get_context("spawn")
    manager = context.Manager()

    recv, sender = context.Pipe(duplex=False)
    proc = context.Process(target=send_message, args=(sender,))
    proc.start()
    proc.join()

    print(recv.recv())
