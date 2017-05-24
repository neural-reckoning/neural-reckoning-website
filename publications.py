class Publication(object):
    def __init__(self, **args):
        for k, v in args.items():
            setattr(self, k, v)

category_inclusions = {
    'Brian': ['Neural simulation', 'Spiking'],
    'Neural simulation': ['Neuroinformatics', 'Spiking'],
    'Spike sorting': ['Neuroinformatics', 'Spiking'],
    'Sound localisation': ['Auditory'],
    'Auditory': ['Sensory'],
    }

category_detail_links = {
    'Brian': 'software.html',
    'Neural simulation': 'neuroinformatics.html',
    'Spike sorting': 'software.html',
    'Neuroinformatics': 'neuroinformatics.html',
    'Sensory': 'sensory.html',
    }

publications = [
#    Publication(
#        name='', #selected=True,
#        year=2014,
#        authors='',
#        title='',
#        journal='',
#        additional='',
#        categories=[],
#        urls=[('Journal', ''),
#              ('PDF', ''),
#              ],
#        abstract='''
#        ''',
#        ),

   Publication(
       name='spikesorting', selected=True,
       year=2016,
       authors='Rossant C, Kadir SN, Goodman DFM, et al.',
       title='Spike sorting for large, dense electrode arrays',
       journal='Nature Neuroscience',
       additional='doi: 10.1038/nn.4268',
       categories=['Spike sorting'],
       urls=[('Journal', 'http://dx.doi.org/10.1038/nn.4268'),
             ('PDF', 'http://www.nature.com/neuro/journal/vaop/ncurrent/pdf/nn.4268.pdf'),
             ('Preprint', 'https://www.dropbox.com/s/emnup6d0aoyjccs/spikesorting-preprint.pdf?dl=1'),
             ],
       abstract='''
       Developments in microfabrication technology have enabled the production of
       neural electrode arrays with hundreds of closely spaced recording sites, and
       electrodes with thousands of sites are under development. These probes in
       principle allow the simultaneous recording of very large numbers of neurons.
       However, use of this technology requires the development of techniques for
       decoding the spike times of the recorded neurons from the raw data captured
       from the probes. Here we present a set of tools to solve this problem,
       implemented in a suite of practical, user-friendly, open-source software.
       We validate these methods on data from the cortex, hippocampus and thalamus
       of rat, mouse, macaque and marmoset, demonstrating error rates as low as 5%.
       ''',
       ),
    Publication(
        name='equations',
        year=2014,
        authors='Stimberg M, Goodman DFM, Benichoux V, Brette R',
        title='Equation-oriented specification of neural models for simulations',
        journal='Frontiers in Neuroinformatics',
        additional='8:6. doi: 10.3389/fninf.2014.00006',
        urls=[('Journal', 'http://www.frontiersin.org/Journal/abstract/69453'),
              ],
        categories=['Brian'],
        abstract='''
        Simulating biological neuronal networks is a core method of research in
        computational neuroscience. A full specification of such a network model
        includes a description of the dynamics and state changes of neurons and
        synapses, as well as the synaptic connectivity patterns and the initial
        values of all parameters. A standard approach in neuronal modeling
        software is to build network models based on a library of pre-defined
        components and mechanisms; if a model component does not yet exist, it
        has to be defined in a special-purpose or general low-level language and
        potentially be compiled and linked with the simulator. Here we propose
        an alternative approach that allows flexible definition of models by
        writing textual descriptions based on mathematical notation. We
        demonstrate that this approach allows the definition of a wide range of
        models with minimal syntax. Furthermore, such explicit model
        descriptions allow the generation of executable code for various target
        languages and devices, since the description is not tied to an
        implementation. Finally, this approach also has advantages for
        readability and reproducibility, because the model description is fully
        explicit, and because it can be automatically parsed and transformed
        into formatted descriptions. The presented approach has been implemented
        in the Brian2 simulator.        
        ''',
        ),
                
    Publication(
        name='mkk', selected=False,
        year=2014,
        authors='Kadir SN, Goodman DFM, Harris KD',
        title='High-dimensional cluster analysis with the masked EM algorithm',
        journal='Neural Computation',
        additional='26:11. doi:10.1162/NECO_a_00661',
        urls=[('Journal', 'http://www.mitpressjournals.org/doi/abs/10.1162/NECO_a_00661'),
              ('PDF', 'http://www.mitpressjournals.org/doi/pdf/10.1162/NECO_a_00661'),
              ('Preprint', 'http://arxiv.org/abs/1309.2848'),
              ],
        categories=['Spike sorting'],
        abstract='''
        Cluster analysis faces two problems in high dimensions: the "curse of
        dimensionality" that can lead to overfitting and poor generalization
        performance and the sheer time taken for conventional algorithms to
        process large amounts of high-dimensional data. We describe a solution
        to these problems, designed for the application of spike sorting for
        next-generation, high-channel-count neural probes. In this problem, only
        a small subset of features provides information about the cluster
        membership of any one data vector, but this informative feature subset
        is not the same for all data points, rendering classical feature
        selection ineffective. We introduce a "masked EM" algorithm that allows
        accurate and time-efficient clustering of up to millions of points in
        thousands of dimensions. We demonstrate its applicability to synthetic
        data and to real-world high-channel-count spike sorting data.        
        ''',
        ),
                
    Publication(
        name='decoding_soundloc', selected=True,
        year=2013,
        authors='Goodman DFM, Benichoux V, Brette R',
        title='Decoding neural responses to temporal cues for sound localization',
        journal='eLife',
        additional='2013;2:e01312',
        urls=[('Journal', 'http://elifesciences.org/content/2/e01312'),
              ('PDF', 'http://elifesciences.org/content/2/e01312.full.pdf'),
              ('Code on GitHub', 'https://github.com/neural-reckoning/decoding_sound_location'),
              ],
        categories=['Sound localisation', 'Modelling'],
        abstract='''
        The activity of sensory neural populations carries information about the
        environment. This may be extracted from neural activity using different
        strategies. In the auditory brainstem, a recent theory proposes that
        sound location in the horizontal plane is decoded from the relative
        summed activity of two populations in each hemisphere, whereas earlier
        theories hypothesized that the location was decoded from the identity of
        the most active cells. We tested the performance of various decoders of
        neural responses in increasingly complex acoustical situations, including
        spectrum variations, noise, and sound diffraction. We demonstrate that
        there is insufficient information in the pooled activity of each
        hemisphere to estimate sound direction in a reliable way consistent with
        behavior, whereas robust estimates can be obtained from neural activity
        by taking into account the heterogeneous tuning of cells. These
        estimates can still be obtained when only contralateral neural responses
        are used, consistently with unilateral lesion studies.        
        ''',
        ),
                
    Publication(
        name='brian_scholarpedia',
        year=2013,
        authors='Goodman DFM, Brette R',
        title='Brian simulator',
        journal='Scholarpedia',
        additional='8(1):10883',
        urls=[('Full text', 'http://www.scholarpedia.org/article/Brian_simulator'),
              ],
        categories=['Brian'],
        abstract='''
        Brian is an open source Python package for developing simulations of
        networks of spiking neurons. The design is aimed at minimizing users'
        development time, with execution speed a secondary goal. Users specify
        neuron and synapse models by giving their equations in standard
        mathematical form, create groups of neurons and connect them via
        synapses. The intent is to make the process as flexible as possible, so
        that researchers are not restricted to using neuron and synapse models
        already built in to the simulator. The entire simulator is written in
        Python, using the NumPy and SciPy numerical and scientific computing
        packages. Parts of the simulator can optionally be run using C++ code
        generated on the fly (Goodman 2010). Computationally, Brian uses
        vectorization techniques (Brette and Goodman 2011), so that for large
        numbers of neurons, execution speed is of the same order of magnitude
        as C++ code (Goodman and Brette 2008, 2009).         
        ''',
        ),
                
    Publication(
        name='brian_encyclopedia',
        year=2013,
        authors='Goodman DFM, Brette R',
        title='Brian Spiking Neural Network Simulator',
        journal='Encyclopedia of Computational Neuroscience',
        additional='SpringerReference',
        urls=[('Full text (paywall)', 'http://www.springerreference.com/docs/html/chapterdbid/348318.html'),
              ],
        categories=['Brian'],
        abstract='''
        Brian (http://briansimulator.org) is an open source Python package for
        developing simulations of networks of spiking neurons (Goodman and
        Brette 2008, 2009). The design is aimed at minimizing users' development
        time, with execution speed as secondary goal. Users specify neuron and
        synapse models by giving their equations in standard mathematical form,
        create groups of neurons, and connect them via synapses. The intent is
        to make the process as flexible as possible so that researchers are not
        restricted to using neuron and synapse models already built into the
        simulator. The entire simulator is written in Python, using the NumPy
        and SciPy numerical and scientific computing packages. Parts of the
        simulator can optionally be run using C++ code generated on the fly
        (Goodman 2010). Computationally, Brian uses vectorization techniques
        (Brette and Goodman 2011) so that for large numbers of neurons,
        execution speed is of the same order of magnitude ... 
        ''',
        ),
                
    Publication(
        name='playdoh',
        year=2013,
        authors='Rossant C, Fontaine B, Goodman DFM',
        title='Playdoh: a lightweight Python package for distributed computing and optimisation',
        journal='Journal of Computational Science',
        additional='4(5):352-259',
        urls=[('Journal', 'http://www.sciencedirect.com/science/article/pii/S1877750311000561'),
              ('DOI', 'http://dx.doi.org/10.1016/j.jocs.2011.06.002'),
              ('PDF (preprint)', 'https://www.dropbox.com/s/d2v1dvfu5xv1i9q/playdoh-preprint.pdf?dl=1'),
              ],
        categories=['Neuroinformatics'],
        abstract='''
        Parallel computing is now an essential paradigm for high performance
        scientific computing. Most existing hardware and software solutions are
        expensive or difficult to use. We developed Playdoh, a Python library
        for distributing computations across the free computing units available
        in a small network of multicore computers. Playdoh supports independent
        and loosely coupled parallel problems such as global optimisations,
        Monte Carlo simulations and numerical integration of partial
        differential equations. It is designed to be lightweight and easy to use
        and should be of interest to scientists wanting to turn their lab
        computers into a small cluster at no cost.
        ''',
        ),
                
    Publication(
        name='snn_gpu',
        year=2012,
        authors='Brette R, Goodman DFM',
        title='Simulating spiking neural networks on GPU',
        journal='Network: Computation in Neural Systems',
        additional='23(4)',
        urls=[('Journal', 'http://informahealthcare.com/doi/abs/10.3109/0954898X.2012.730170'),
              ('PDF (preprint)', 'https://www.dropbox.com/s/2rxybu315p0tclq/gpureview-preprint.pdf?dl=1'),
              ],
        categories=['Neural simulation'],
        abstract='''
        Modern graphics cards contain hundreds of cores that can be programmed
        for intensive calculations. They are beginning to be used for spiking
        neural network simulations. The goal is to make parallel simulation of
        spiking neural networks available to a large audience, without the
        requirements of a cluster. We review the ongoing efforts towards this
        goal, and we outline the main difficulties.
        ''',
        ),
                
    Publication(
        name='rat_barrel_cortex',
        year=2011,
        authors='Kremer Y, L&eacute;ger J-F, Goodman D, Brette R, Bourdieu L',
        title='Late emergence of the vibrissa direction selectivity map in the rat barrel cortex',
        journal='Journal of Neuroscience',
        additional='31(29). doi:10.1523/?JNEUROSCI.6541-10.2011 ',
        urls=[('Journal', 'http://www.jneurosci.org/content/31/29/10689.abstract'),
              ('PDF (preprint)', 'https://www.dropbox.com/s/ypos545ptv0blf4/barrelcortex-preprint.pdf?dl=1'),
              ],
        categories=['Sensory', 'Modelling', 'Spiking'],
        abstract='''
        In the neocortex, neuronal selectivities for multiple sensorimotor
        modalities are often distributed in topographical maps thought to emerge
        during a restricted period in early postnatal development. Rodent barrel
        cortex contains a somatotopic map for vibrissa identity, but the
        existence of maps representing other tactile features has not been
        clearly demonstrated. We addressed the issue of the existence in the rat
        cortex of an intrabarrel map for vibrissa movement direction using in
        vivo two-photon imaging. We discovered that the emergence of a direction
        map in rat barrel cortex occurs long after all known critical periods
        in the somatosensory system. This map is remarkably specific, taking a
        pinwheel-like form centered near the barrel center and aligned to the
        barrel cortex somatotopy. We suggest that this map may arise from
        intracortical mechanisms and demonstrate by simulation that the
        combination of spike-timing-dependent plasticity at synapses between
        layer 4 and layer 2/3 and realistic pad stimulation is sufficient to
        produce such a map. Its late emergence long after other classical maps
        suggests that experience-dependent map formation and refinement continue
        throughout adult life. 
        ''',
        ),
                
    Publication(
        name='brian_hears', selected=True,
        year=2011,
        authors='Fontaine B, Goodman DFM (joint first authors), Benichoux V, Brette R',
        title='Brian Hears: online auditory processing using vectorisation over channels',
        journal='Frontiers in Neuroinformatics',
        additional='5:9. doi: 10.3389/fninf.2011.00009',
        urls=[('Journal', 'http://journal.frontiersin.org/Journal/10.3389/fninf.2011.00009/abstract'),
              ],
        categories=['Brian', 'Auditory'],
        abstract='''
        The human cochlea includes about 3000 inner hair cells which filter
        sounds at frequencies between 20 Hz and 20 kHz. This massively parallel
        frequency analysis is reflected in models of auditory processing, which
        are often based on banks of filters. However, existing implementations
        do not exploit this parallelism. Here we propose algorithms to simulate
        these models by vectorizing computation over frequency channels, which
        are implemented in "Brian Hears," a library for the spiking neural
        network simulator package "Brian." This approach allows us to use
        high-level programming languages such as Python, because with vectorized
        operations, the computational cost of interpretation represents a small
        fraction of the total cost. This makes it possible to define and
        simulate complex models in a simple way, while all previous
        implementations were model-specific. In addition, we show that these
        algorithms can be naturally parallelized using graphics processing
        units, yielding substantial speed improvements. We demonstrate these
        algorithms with several state-of-the-art cochlear models, and show that
        they compare favorably with existing, less flexible, implementations.
        ''',
        ),
                
    Publication(
        name='vectorised_algorithms',
        year=2011,
        authors='Brette R, Goodman DFM',
        title='Vectorised algorithms for spiking neural network simulation',
        journal='Neural Computation',
        additional='23:6',
        urls=[('Journal', 'http://www.mitpressjournals.org/doi/abs/10.1162/NECO_a_00123?journalCode=neco'),
              ('PDF (preprint)', 'https://www.dropbox.com/s/okq0bywihietbgr/algorithms-preprint.pdf?dl=1'),
              ],
        categories=['Brian'],
        abstract='''
        High-level languages (Matlab, Python) are popular in neuroscience
        because they are flexible and accelerate development. However, for
        simulating spiking neural networks, the cost of interpretation is a
        bottleneck. We describe a set of algorithms to simulate large spiking
        neural networks efficiently with high-level languages using vector-based
        operations. These algorithms constitute the core of Brian, a spiking
        neural network simulator written in the Python language. Vectorized
        simulation makes it possible to combine the flexibility of high-level
        languages with the computational efficiency usually associated with
        compiled languages.
        ''',
        ),
                
    Publication(
        name='modelfitting_focussed_review', selected=True,
        year=2011,
        authors='Rossant C, Goodman DFM, Fontaine B, Platkiewicz J, Magnusson AK, Brette R',
        title='Fitting neuron models to spike trains',
        journal='Frontiers in Neuroscience',
        additional='5:9. doi: 10.3389/fnins.2011.00009',
        urls=[('Journal', 'http://www.frontiersin.org/Neuroscience/10.3389/fnins.2011.00009/abstract'),
              ],
        categories=['Brian'],
        abstract='''
        Computational modeling is increasingly used to understand the function
        of neural circuits in systems neuroscience. These studies require
        models of individual neurons with realistic input-output properties.
        Recently, it was found that spiking models can accurately predict the
        precisely timed spike trains produced by cortical neurons in response to
        somatically injected currents, if properly fitted. This requires fitting
        techniques that are efficient and flexible enough to easily test
        different candidate models. We present a generic solution, based on the
        Brian simulator (a neural network simulator in Python), which allows the
        user to define and fit arbitrary neuron models to electrophysiological
        recordings. It relies on vectorization and parallel computing techniques
        to achieve efficiency. We demonstrate its use on neural recordings in
        the barrel cortex and in the auditory brainstem, and confirm that simple
        adaptive spiking models can accurately predict the response of cortical
        neurons. Finally, we show how a complex multicompartmental model can be
        reduced to a simple effective spiking model.
        ''',
        ),
                
    Publication(
        name='learning_localisation',
        year=2010,
        authors='Goodman DFM, Brette R',
        title='Learning to localise sounds with spiking neural networks',
        journal='Advances in Neural Information Processing Systems',
        additional='23',
        urls=[('Journal', 'http://papers.nips.cc/paper/4127-learning-to-localise-sounds-with-spiking-neural-networks'),
              ('PDF', 'http://papers.nips.cc/paper/4127-learning-to-localise-sounds-with-spiking-neural-networks.pdf'),
              ('BibTeX', 'http://papers.nips.cc/paper/4127-learning-to-localise-sounds-with-spiking-neural-networks/bibtex'),
              ],
        categories=['Sound localisation', 'Modelling', 'Spiking'],
        abstract='''
        To localise the source of a sound, we use location-specific properties
        of the signals received at the two ears caused by the asymmetric
        filtering of the original sound by our head and pinnae, the head-related
        transfer functions (HRTFs). These HRTFs change throughout an organism's
        lifetime, during development for example, and so the required neural
        circuitry cannot be entirely hardwired. Since HRTFs are not directly
        accessible from perceptual experience, they can only be inferred from
        filtered sounds. We present a spiking neural network model of sound
        localisation based on extracting location-specific synchrony patterns,
        and a simple supervised algorithm to learn the mapping between synchrony
        patterns and locations from a set of example sounds, with no previous
        knowledge of HRTFs. After learning, our model was able to accurately
        localise new sounds in both azimuth and elevation, including the
        difficult task of distinguishing sounds coming from the front and back.
        ''',
        ),
                
    Publication(
        name='qr',
        year=2010,
        authors='Fletcher A, Goodman DFM',
        title='Quasiregular mappings of polynomial type in R<sup>2</sup>',
        journal='Conformal Geometry and Dynamics',
        additional='14',
        urls=[('Journal', 'http://www.ams.org/journals/ecgd/2010-14-17/S1088-4173-2010-00219-5/home.html'),
              ('PDF (preprint)', 'https://www.dropbox.com/s/v6h2bex5y09uqej/quadqr.pdf?dl=1'),
              ],
        categories=['Mathematics'],
        abstract='''
        Complex dynamics deals with the iteration of holomorphic functions. As
        is well known, the first functions to be studied which gave non-trivial
        dynamics were quadratic polynomials, which produced beautiful computer
        generated pictures of Julia sets and the Mandelbrot set. In the same
        spirit, this article aims to study the dynamics of the simplest
        non-trivial quasiregular mappings. These are mappings in R<sup>2</sup>
        which are a composition of a quadratic polynomial and an affine stretch. 
        ''',
        ),
                
    Publication(
        name='spike_timing_sound_loc', selected=True,
        year=2010,
        authors='Goodman DFM, Brette R',
        title='Spike-timing-based computation in sound localization',
        journal='PLoS Computational Biology',
        additional='6(11): e1000993. doi:10.1371/journal.pcbi.1000993',
        urls=[('Journal', 'http://www.ploscompbiol.org/article/info:doi/10.1371/journal.pcbi.1000993'),
              ('PDF', 'http://www.ploscompbiol.org/article/fetchObject.action?uri=info%3Adoi%2F10.1371%2Fjournal.pcbi.1000993&representation=PDF'),
              ('Code on ModelDB', 'http://senselab.med.yale.edu/ModelDB/ShowModel.asp?model=126465'),
              ],
        categories=['Sound localisation', 'Modelling', 'Spiking'],
        abstract='''
        Spike timing is precise in the auditory system and it has been argued
        that it conveys information about auditory stimuli, in particular about
        the location of a sound source. However, beyond simple time differences,
        the way in which neurons might extract this information is unclear and
        the potential computational advantages are unknown. The computational
        difficulty of this task for an animal is to locate the source of an
        unexpected sound from two monaural signals that are highly dependent on
        the unknown source signal. In neuron models consisting of
        spectro-temporal filtering and spiking nonlinearity, we found that the
        binaural structure induced by spatialized sounds is mapped to synchrony
        patterns that depend on source location rather than on source signal.
        Location-specific synchrony patterns would then result in the activation
        of location-specific assemblies of postsynaptic neurons. We designed a
        spiking neuron model which exploited this principle to locate a variety
        of sound sources in a virtual acoustic environment using measured human
        head-related transfer functions. The model was able to accurately
        estimate the location of previously unknown sounds in both azimuth and
        elevation (including front/back discrimination) in a known acoustic
        environment. We found that multiple representations of different
        acoustic environments could coexist as sets of overlapping neural
        assemblies which could be associated with spatial locations by Hebbian
        learning. The model demonstrates the computational relevance of relative
        spike timing to extract spatial information about sources independently
        of the source signal.
        ''',
        ),
                
    Publication(
        name='codegen',
        year=2010,
        authors='Goodman DFM',
        title='Code Generation: A Strategy for Neural Network Simulators',
        journal='Neuroinformatics',
        additional='8, no. 3 (9). doi:10.1007/s12021-010-9082-x',
        urls=[('Journal', 'http://www.springerlink.com/content/12614h7817602680/'),
              ('PDF (preprint)', 'https://www.dropbox.com/s/si4uaau33csqejk/codegen.pdf?dl=1'),
              ],
        categories=['Brian'],
        abstract='''
        We demonstrate a technique for the design of neural network simulation
        software, runtime code generation. This technique can be used to give
        the user complete flexibility in specifying the mathematical model for
        their simulation in a high level way, along with the speed of code
        written in a low level language such as C++. It can also be used to
        write code only once but target different hardware platforms, including
        inexpensive high performance graphics processing units (GPUs). Code
        generation can be naturally combined with computer algebra systems to
        provide further simplification and optimisation of the generated code.
        The technique is quite general and could be applied to any simulation
        package. We demonstrate it with the "Brian" simulator
        (http://www.briansimulator.org).
        ''',
        ),
                
    Publication(
        name='modelfitting',
        year=2010,
        authors='Rossant C, Goodman DFM, Platkiewicz J, Brette R',
        title='Automatic fitting of spiking neuron models to electrophysiological recordings',
        journal='Frontiers in Neuroinformatics',
        additional='doi:10.3389/neuro.11.002.2010',
        urls=[('Journal', 'http://journal.frontiersin.org/Journal/10.3389/neuro.11.002.2010/abstract'),
              ],
        categories=['Brian'],
        abstract='''
        Spiking models can accurately predict the spike trains produced by
        cortical neurons in response to somatically injected currents. Since the
        specific characteristics of the model depend on the neuron, a
        computational method is required to fit models to electrophysiological
        recordings. The fitting procedure can be very time consuming both in
        terms of computer simulations and in terms of code writing. We present
        algorithms to fit spiking models to electrophysiological data
        (time-varying input and spike trains) that can run in parallel on
        graphics processing units (GPUs). The model fitting library is
        interfaced with Brian, a neural network simulator in Python. If a GPU is
        present it uses just-in-time compilation to translate model equations
        into optimized code. Arbitrary models can then be defined at script
        level and run on the graphics card. This tool can be used to obtain
        empirically validated spiking models of neurons in various systems. We
        demonstrate its use on public data from the INCF Quantitative
        Single-Neuron Modeling 2009 competition by comparing the performance of
        a number of neuron spiking models. 
        ''',
        ),
                
    Publication(
        name='brian_focussed_review', selected=True,
        year=2009,
        authors='Goodman DFM, Brette R',
        title='The Brian simulator',
        journal='Frontiers in Neuroscience',
        additional='3(2), doi:10.3389/neuro.01.026.2009',
        urls=[('Journal', 'http://journal.frontiersin.org/Journal/10.3389/neuro.01.026.2009/abstract'),
              ],
        categories=['Brian'],
        abstract='''
        "Brian" is a simulator for spiking neural networks
        (http://www.briansimulator.org ). The focus is on making the writing of
        simulation code as quick and easy as possible for the user, and on
        flexibility: new and non-standard models are no more difficult to define
        than standard ones. This allows scientists to spend more time on the
        details of their models, and less on their implementation. Neuron models
        are defined by writing differential equations in standard mathematical
        notation, facilitating scientific communication. Brian is written in the
        Python programming language, and uses vector-based computation to allow
        for efficient simulations. It is particularly useful for neuroscientific
        modelling at the systems level, and for teaching computational
        neuroscience. 
        ''',
        ),
                
    Publication(
        name='brian_neuromorphic_engineer',
        year=2009,
        authors='Brette R, Goodman D',
        title='Brian: a simple and flexible simulator for spiking neural networks',
        journal='The Neuromorphic Engineer',
        additional='doi: 10.2417/1200906.1659',
        urls=[('Journal', 'http://www.ine-news.org/view.php?source=1659-2009-07-07'),
              ('PDF', 'http://www.ine-news.org/pdf/1659/1659.pdf'),
              ],
        categories=['Brian'],
        ),
                
    Publication(
        name='brian',
        year=2008,
        authors='Goodman D, Brette R',
        title='Brian: a simulator for spiking neural networks in Python',
        journal='Frontiers in Neuroinformatics',
        additional='2(5), doi:10.3389/neuro.11.005.2008',
        urls=[('Journal', 'http://journal.frontiersin.org/Journal/10.3389/neuro.11.005.2008/abstract'),
              ],
        categories=['Brian'],
        abstract='''
        "Brian" is a new simulator for spiking neural networks, written in
        Python (http://www.briansimulator.org ). It is an intuitive and highly
        flexible tool for rapidly developing new models, especially networks of
        single-compartment neurons. In addition to using standard types of
        neuron models, users can define models by writing arbitrary differential
        equations in ordinary mathematical notation. Python scientific libraries
        can also be used for defining models and analysing data. Vectorisation
        techniques allow efficient simulations despite the overheads of an
        interpreted language. Brian will be especially valuable for working on
        non-standard neuron models not easily covered by existing software, and
        as an alternative to using Matlab or C for simulations. With its easy
        and intuitive syntax, Brian is also very well suited for teaching
        computational neuroscience. 
        ''',
        ),
                
    Publication(
        name='spirals',
        year=2006,
        authors='Goodman D',
        title='Spirals in the boundaries of slices of quasifuchsian space',
        journal='Conformal Geometry and Dynamics',
        additional='10',
        urls=[('Journal', 'http://www.ams.org/journals/ecgd/2006-10-08/S1088-4173-06-00133-0/home.html'),
              ('PDF (preprint)', 'https://www.dropbox.com/s/ygz9demdn5n5l19/spirals-paper.pdf?dl=1'),
              ],
        categories=['Mathematics'],
        abstract='''
        We prove that the Bers and Maskit slices of the quasi-Fuchsian space of
        a once-punctured torus have a dense, uncountable set of points in their
        boundaries about which the boundary spirals infinitely.
        ''',
        ),
    ]

