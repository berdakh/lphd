def signalProxy(fSample = 100, nChans = 10, blocksize = 2):
    
    import bufhelp
    from time import sleep, time
    import numpy
    
    ftc = bufhelp.connect(header=False)
    print(ftc)
    print("Putting header.")
    print("channels",nChans)
    print("fSample",fSample)
    ftc.putHeader(nChans, fSample, 10)
    
    print("Starting singal proxy")  
    
    delta = 1.0/(fSample/blocksize)
    sample = numpy.random.rand(blocksize, nChans)    
    n = 0;    
    
    while True:
        sendtime = time()
        ftc.putData(sample)
        n = n + 1
        if n % 100 == 0:
           print(str(n) + " data packages sent.")
        sample = numpy.random.rand(blocksize, nChans)
        wait = delta - (time() - sendtime)
        if wait > 0:
            sleep(wait)
        