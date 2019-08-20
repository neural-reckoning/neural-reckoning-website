# coding=utf-8
class Publication(object):
    def __init__(self, **args):
        for k, v in args.items():
            setattr(self, k, v)
    @property
    def is_preprint(self):
        return isinstance(self.year, basestring) and self.year=="Preprints"

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
#        year=2014, # set year to 'Preprints' if not published yet
#        authors='',
#        title='',
#        journal='', # for an article
#        publisher='', # for a book
#        additional='', # goes after Journal (Year)
#        doi='', # linked to on detail page only
#        book='', book_editors='', # if it's a book chapter, fill this in
#        additional_detail='', # only shown on detail page
#        categories=[],
#        urls=[('Journal', ''),
#              ('PDF', ''),
#              ],
#        abstract='''
#        ''',
#        ),
    Publication(
       name='brian2', selected=True,
       year=2019, # set year to 'Preprints' if not published yet
       authors='Stimberg M, Brette R, Goodman DFM',
       title='Brian 2: an intuitive and efficient neural simulator',
       journal='eLife', # for an article
       # publisher='', # for a book
       additional='8:e47314', # goes after Journal (Year)
       doi='10.7554/eLife.47314', # linked to on detail page only
       # book='', book_editors='', # if it's a book chapter, fill this in
       # additional_detail='', # only shown on detail page
       categories=['Brian'],
       urls=[('Journal', 'https://elifesciences.org/articles/47314'),
             ('Code', 'https://github.com/brian-team/brian2'),
             ('Documentation', 'https://brian2.readthedocs.io/en/stable/'),
             ('Examples code', 'https://github.com/brian-team/brian2_paper_examples'),
             ('Interactive examples', 'https://mybinder.org/v2/gh/brian-team/brian2_paper_examples/master?filepath=index.ipynb'),
             ('Website', 'http://briansimulator.org/'),
             ],
       abstract='''
       Brian 2 allows scientists to simply and efficiently simulate spiking neural network models. These models can
       feature novel dynamical equations, their interactions with the environment, and experimental protocols. To
       preserve high performance when defining new models, most simulators offer two options: low-level programming or
       description languages. The first option requires expertise, is prone to errors, and is problematic for
       reproducibility. The second option cannot describe all aspects of a computational experiment, such as the
       potentially complex logic of a stimulation protocol. Brian addresses these issues using runtime code generation.
       Scientists write code with simple and concise high-level descriptions, and Brian transforms them into efficient
       low-level code that can run interleaved with their code. We illustrate this with several challenging examples: a
       plastic model of the pyloric network, a closed-loop sensorimotor model, a programmatic exploration of a neuron
       model, and an auditory model with real-time input.
       ''',
       ),
    Publication(
       name='canonical_ambb', #selected=True,
       year='Preprints', # set year to 'Preprints' if not published yet
       authors='Lestang J-H, Goodman DFM',
       title='Canonical brain computations account for perceived sound source location',
       #journal='', # for an article
       #additional='', # goes after Journal (Year)
       #doi='', # linked to on detail page only
       #additional_detail='', # only shown on detail page
       categories=['Auditory', 'Sound localisation', 'Modelling'],
       urls=[('Preprint', 'https://www.biorxiv.org/content/10.1101/687178v1'),
             ('Preprint (PDF)', 'https://www.biorxiv.org/content/biorxiv/early/2019/06/29/687178.full-text.pdf'),
             ('Code (GitHub)', 'https://github.com/neural-reckoning/simple_ambb_modelling'),
             ('Live code (Binder)', 'https://mybinder.org/v2/gh/neural-reckoning/simple_ambb_modelling/master?filepath=index.ipynb'),
             ],
       abstract='''
       Sound localization in reverberant environments is a difficult task that human listeners perform effortlessly.
       Many neural mechanisms have been proposed to account for this behavior. Generally they rely on emphasizing
       localization information at the onset of the incoming sound while discarding localization cues that arrive later.
       We modelled several of these mechanisms using neural circuits commonly found in the brain and tested their
       performance in the context of experiments showing that, in the dominant frequency region for sound localisation,
       we have a preference for auditory cues arriving during the rising slope of the sound energy (Dietz et al. 2013).
       We found that both single cell mechanisms (onset and adaptation) and population mechanisms (lateral inhibition)
       were easily able to reproduce the results across a very wide range of parameter settings. This suggests that
       sound localization in reverberant environments may not require specialised mechanisms specific to that task, but
       may instead rely on common neural circuits in the brain. This is in line with the theory that the brain consists
       of functionally overlapping general purpose mechanisms rather than a collection of mechanisms each highly
       specialised to specific tasks. This research is fully reproducible, and we made our code available to edit and
       run online via interactive live notebooks.
       ''',
       ),
    Publication(
        name='comments_on_edge_bundling',  # selected=True,
        year='Preprints',  # set year to 'Preprints' if not published yet
        authors='Zheng JX, Pawar S, Goodman DFM',
        title='Further Towards Unambiguous Edge Bundling: Investigating Power-Confluent Drawings for Network Visualization',
        # journal='',
        # additional='',
        categories=['Visualisation'],
        urls=[('Preprint', 'https://arxiv.org/abs/1810.09948'),
              ('Preprint (PDF)', 'https://arxiv.org/pdf/1810.09948'),
              ('Code (GitHub)', 'https://github.com/jxz12/pconfluent'),
              ],
        abstract='''
           Bach et al. [1] recently presented an algorithm for constructing confluent drawings, by leveraging power graph
           decomposition to generate an auxiliary routing graph. We identify two problems with their method and offer a
           single solution to solve both. We also classify the exact type of confluent drawings that the algorithm can
           produce as 'power-confluent', and prove that it is a subclass of the previously studied 'strict confluent'
           drawing. A description and source code of our implementation is also provided, which additionally includes an
           improved method for power graph construction.
           ''',
            ),
    Publication(
       name='gamification_sound_localisation', #selected=True,
       year='Preprints', # set year to 'Preprints' if not published yet
       authors='Steadman MA, Kim C, Lestang JH, Goodman DFM, Picinali L',
       title='Short-term effects of sound localization training in virtual reality',
       #journal='',
       #additional='',
       categories=['Auditory', 'Sound localisation', 'Learning'],
       urls=[('Preprint', 'https://www.biorxiv.org/content/10.1101/207753v3'),
             ('PDF (preprint)', 'https://www.biorxiv.org/content/biorxiv/early/2019/07/10/207753.full-text.pdf'),
             ],
       abstract='''
       Head-related transfer functions (HRTFs) capture the direction-dependant way that sound interacts with the head
       and torso. In virtual audio systems, which aim to emulate these effects, non-individualized, generic HRTFs are
       typically used leading to an inaccurate perception of virtual sound location. Training has the potential to
       exploit the brain's ability to adapt to these unfamiliar cues. In this study, three virtual sound localization
       training paradigms were evaluated; one provided simple visual positional confirmation of sound source location, a
       second introduced game design elements ("gamification") and a final version additionally utilized head-tracking
       to provide listeners with experience of relative sound source motion ("active listening"). The results
       demonstrate a significant effect of training after a small number of short (12-minute) training sessions, which
       is retained across multiple days. Gamification alone had no significant effect on the efficacy of the training,
       but active listening resulted in a significantly greater improvements in localization accuracy. In general,
       improvements in virtual sound localization following training generalized to a second set of non-individualized
       HRTFs, although some HRTF-specific changes were observed in polar angle judgement for the active listening group.
       The implications of this on the putative mechanisms of the adaptation process are discussed.
       ''',
       ),
    Publication(
       name='astrocytes', #selected=True,
       year=2019,
       authors=u'Stimberg M, Goodman DFM, Brette R, De Pittà M',
       title='Modeling neuron-glia interactions with the Brian 2 simulator',
       publisher='Springer',
       book_chapter=True,
       book=u'Computational Glioscience',
       book_editors=u'De Pittà M, Berry H',
       categories=['Brian', 'Modelling'],
       urls=[('Book', 'https://link.springer.com/book/10.1007/978-3-030-00817-8'),
             ('Chapter', 'https://link.springer.com/chapter/10.1007/978-3-030-00817-8_18'),
             ('Preprint', 'https://www.biorxiv.org/content/early/2017/10/05/198366'),
             ('PDF (preprint)', 'https://www.biorxiv.org/content/early/2017/10/05/198366.full.pdf'),
             ],
       abstract='''
       Despite compelling evidence that glial cells could crucially regulate neural network activity, the vast majority
       of available neural simulators ignores the possible contribution of glia to neuronal physiology. Here, we show
       how to model glial physiology and neuron-glia interactions in the Brian 2 simulator. Brian 2 offers facilities to
       explicitly describe any model in mathematical terms with limited and simple simulator-specific syntax,
       automatically generating high-performance code from the user-provided descriptions. The flexibility of this
       approach allows us to model not only networks of neurons, but also individual glial cells, electrical coupling of
       glial cells, and the interaction between glial cells and synapses. We therefore conclude that Brian 2 provides an
       ideal platform to efficiently simulate glial physiology, and specifically, the influence of astrocytes on neural
       activity.
       ''',
       ),
    Publication(
       name='codegen_review', #selected=True,
       year=2018,
       authors=(u'Blundell I, Brette R, Cleland TA, Close TG, Coca D, Davison AP, Diaz-Pier S, Musoles CF, '
                u'Gleeson P, Goodman DFM, Hines M, Hopkins MW, Kumbhar P, Lester DR, Marin B, Morrison A, '
                u'Müller E, Nowotny T, Peyser A, Plotnikov D, Richmond P, Rowley A, Rumpe B, Stimberg M, '
                u'Stokes AB, Tomkins A, Trensch G, Woodman M, Eppler JM'),
       title='Code Generation in Computational Neuroscience: A Review of Tools and Techniques',
       journal='Frontiers in Neuroinformatics',
       doi='10.3389/fninf.2018.00068',
       categories=['Neuroinformatics', 'Neural simulation'],
       urls=[('Journal', 'https://www.frontiersin.org/articles/10.3389/fninf.2018.00068/full'),
             ('PDF', 'https://www.frontiersin.org/articles/10.3389/fninf.2018.00068/pdf'),
             ],
       abstract='''
       Advances in experimental techniques and computational power allowing researchers to gather anatomical and
       electrophysiological data at unprecedented levels of detail have fostered the development of increasingly complex
       models in computational neuroscience. Large-scale, biophysically detailed cell models pose a particular set of
       computational challenges, and this has led to the development of a number of domain-specific simulators. At the
       other level of detail, the ever growing variety of point neuron models increases the implementation barrier even
       for those based on the relatively simple integrate-and-fire neuron model. Independently of the model complexity,
       all modeling methods crucially depend on an efficient and accurate transformation of mathematical model
       descriptions into efficiently executable code. Neuroscientists usually publish model descriptions in terms of the
       mathematical equations underlying them. However, actually simulating them requires they be translated into code.
       This can cause problems because errors may be introduced if this process is carried out by hand, and code written
       by neuroscientists may not be very computationally efficient. Furthermore, the translated code might be generated
       for different hardware platforms, operating system variants or even written in different languages and thus
       cannot easily be combined or even compared. Two main approaches to addressing this issues have been followed. The
       first is to limit users to a fixed set of optimized models, which limits flexibility. The second is to allow
       model definitions in a high level interpreted language, although this may limit performance. Recently, a third
       approach has become increasingly popular: using code generation to automatically translate high level
       descriptions into efficient low level code to combine the best of previous approaches. This approach also greatly
       enriches efforts to standardize simulator-independent model description languages. In the past few years, a
       number of code generation pipelines have been developed in the computational neuroscience community, which differ
       considerably in aim, scope and functionality. This article provides an overview of existing pipelines currently
       used within the community and contrasts their capabilities and the technologies and concepts behind them.
       ''',
       ),
    Publication(
       name='graph_drawing_wcr', #selected=True,
       year=2018, # set year to 'Preprints' if not published yet
       authors='Zheng JX, Pawar S, Goodman DFM',
       title='Graph Drawing by Stochastic Gradient Descent',
       journal=' IEEE Transactions on Visualization and Computer Graphics',
       doi='10.1109/TVCG.2018.2859997',
       categories=['Visualisation'],
       urls=[('Journal', 'https://ieeexplore.ieee.org/document/8419285'),
             ('Preprint', 'https://arxiv.org/abs/1710.04626'),
             ('PDF (preprint)', 'https://arxiv.org/pdf/1710.04626'),
             ('Code (GitHub)', 'https://github.com/jxz12/s_gd2'),
             ],
       abstract='''
       A popular method of force-directed graph drawing is multidimensional scaling using graph-theoretic
       distances as input. We present an algorithm to minimize its energy function, known as stress, by
       using stochastic gradient descent (SGD) to move a single pair of vertices at a time. Our results
       show that SGD can reach lower stress levels faster and more consistently than majorization, without
       needing help from a good initialization. We then present various real-world applications to show
       how the unique properties of SGD make it easier to produce constrained layouts than previous
       approaches. We also show how SGD can be directly applied within the sparse stress approximation of
       Ortmann et al. [1], making the algorithm scalable up to large graphs.
       ''',
       ),
    Publication(
       name='brian2genn', #selected=True,
       year='Preprints', # set year to 'Preprints' if not published yet
       authors='Stimberg M, Goodman DFM, Nowotny T',
       title='Brian2GeNN: a system for accelerating a large variety of spiking neural networks with graphics hardware',
       #journal='',
       #additional='',
       categories=['Brian', 'Neuroinformatics', 'Neural simulation'],
       urls=[('Preprint', 'https://www.biorxiv.org/content/early/2018/10/20/448050'),
             ('Preprint (PDF)', 'https://www.biorxiv.org/content/early/2018/10/20/448050.full.pdf'),
             ],
       abstract='''
       "Brian" is a popular Python-based simulator for spiking neural networks, commonly used in computational
       neuroscience. GeNN is a C++-based meta-compiler for accelerating spiking neural network simulations using
       consumer or high performance grade graphics processing units (GPUs). Here we introduce a new software package,
       Brian2GeNN, that connects the two systems so that users can make use of GeNN GPU acceleration when developing
       their models in Brian, without requiring any technical knowledge about GPUs, C++ or GeNN. The new Brian2GeNN
       software uses a pipeline of code generation to translate Brian scripts into C++ code that can be used as input to
       GeNN, and subsequently can be run on suitable NVIDIA GPU accelerators. From the user's perspective, the entire
       pipeline is invoked by adding two simple lines to their Brian scripts. We have shown that using Brian2GeNN,
       typical models can run tens to hundreds of times faster than on CPU.
       ''',
       ),
    Publication(
       name='re_stdp_repeating_patterns', #selected=True,
       year=2018, # set year to 'Preprints' if not published yet
       authors='Hathway P, Goodman DFM',
       title='[Re] Spike Timing Dependent Plasticity Finds the Start of Repeating Patterns in Continuous Spike Trains',
       journal='ReScience',
       doi='10.5281/zenodo.1327348',
       categories=['Modelling', 'Learning', 'Plasticity', 'Spiking'],
       urls=[('PDF', 'https://github.com/ReScience-Archives/Hathway-Goodman-2018/raw/master/article/Hathway-Goodman-2018.pdf'),
             ('Code (GitHub)', 'https://github.com/pamelahathway/ReScience-submission/tree/Hathway-Goodman/code'),
             ('Code (Zenodo)', 'https://doi.org/10.5281/zenodo.1327348'),
             ('Review', 'https://github.com/ReScience/ReScience-submission/pull/51'),
             ],
       abstract='''
       This article is a replication of
       <a href="http://journals.plos.org/plosone/article?id=10.1371/journal.pone.0001377">Masquelier et al. (2008)
       "Spike Timing Dependent Plasticity Finds the Start of Repeating Patterns in Continuous Spike Trains"</a>.
       ''',
       ),
    Publication(
       name='framework_comparing_binaural_models', #selected=True,
       year=2018, # set year to 'Preprints' if not published yet
       authors='Dietz M, Lestang J-H, Majdak P, Stern RM, Marquardt T, Ewert SD, Hartmann WH, Goodman DFM',
       title='A framework for testing and comparing binaural models',
       journal='Hearing Research',
       doi='10.1016/j.heares.2017.11.010',
       categories=['Auditory', 'Neuroinformatics', 'Sound localisation'],
       urls=[('Journal', 'https://doi.org/10.1016/j.heares.2017.11.010'),
             ('PDF (preprint)', 'https://www.dropbox.com/s/v64783umlei7448/framework-for-testing-and-comparing-binaural-models.pdf?dl=1'),
             ('Code (GitHub)', 'https://github.com/model-initiative/model_initiative'),
             ],
       abstract='''
       Auditory research has a rich history of combining experimental evidence with computational simulations of
       auditory processing in order to deepen our theoretical understanding of how sound is processed in the ears and in
       the brain. Despite significant progress in the amount of detail and breadth covered by auditory models, for many
       components of the auditory pathway there are still different model approaches that are often not equivalent but
       rather in conflict with each other. Similarly, some experimental studies yield conflicting results which has led
       to controversies. This can be best resolved by a systematic comparison of multiple experimental data sets and
       model approaches. Binaural processing is a prominent example of how the development of quantitative theories can
       advance our understanding of the phenomena, but there remain several unresolved questions for which competing
       model approaches exist. This article discusses a number of current unresolved or disputed issues in binaural
       modeling, as well as some of the significant challenges in comparing binaural models with each other and with the
       experimental data. We introduce an auditory model framework, which we believe can become a useful infrastructure
       for resolving some of the current controversies. It operates models over the same paradigms that are used
       experimentally. The core of the proposed framework is an interface that connects three components irrespective of
       their underlying programming language: The experiment software, an auditory pathway model, and task-dependent
       decision stages called artificial observers that provide the same output format as the test subject.
       ''',
       ),
    Publication(
       name='vcn_regularity', selected=True,
       year=2018,
       authors=u'Goodman DFM, Winter IM, Léger AC, de Cheveigné A, Lorenzi C',
       title='Modelling firing regularity in the ventral cochlear nucleus: mechanisms, and effects of stimulus level and synaptopathy',
       journal='Hearing Research',
       doi='10.1016/j.heares.2017.09.010',
       categories=['Auditory', 'Spiking', 'Modelling'],
       urls=[('Journal', 'https://doi.org/10.1016/j.heares.2017.09.010'),
             ('Preprint', 'https://www.biorxiv.org/content/early/2017/09/19/121707'),
             ('PDF (preprint)', 'https://www.biorxiv.org/content/early/2017/09/19/121707.full.pdf'),
             ('Code (GitHub)', 'https://github.com/neural-reckoning/vcn_regularity'),
             ('Code (Binder, interactive)', 'http://mybinder.org/repo/neural-reckoning/vcn_regularity'),
             ],
       abstract='''
       The auditory system processes temporal information at multiple scales, and disruptions to this temporal
       processing may lead to deficits in auditory tasks such as detecting and discriminating sounds in a noisy
       environment. Here, a modelling approach is used to study the temporal regularity of firing by chopper cells in
       the ventral cochlear nucleus, in both the normal and impaired auditory system. Chopper cells, which have a
       strikingly regular firing response, divide into two classes, sustained and transient, based on the time course of
       this regularity. Several hypotheses have been proposed to explain the behaviour of chopper cells, and the
       difference between sustained and transient cells in particular. However, there is no conclusive evidence so far.
       Here, a reduced mathematical model is developed and used to compare and test a wide range of hypotheses with a
       limited number of parameters. Simulation results show a continuum of cell types and behaviours: chopper-like
       behaviour arises for a wide range of parameters, suggesting that multiple mechanisms may underlie this behaviour.
       The model accounts for systematic trends in regularity as a function of stimulus level that have previously only
       been reported anecdotally. Finally, the model is used to predict the effects of a reduction in the number of
       auditory nerve fibres (deafferentation due to, for example, cochlear synaptopathy). An interactive
       version of this paper in which all the model parameters can be changed is available online.
       ''',
       ),
   Publication(
       name='spikesorting', selected=True,
       year=2016,
       authors=(u'Rossant C, Kadir SN, Goodman DFM, Schulman J, Hunter MLD, Saleem AB, Grosmark A, Belluscio M, '
                u'Denfield GH, Ecker AS, Tolias AS, Solomon S, Buzsáki G, Carandini M, Harris KD'),
       title='Spike sorting for large, dense electrode arrays',
       journal='Nature Neuroscience',
       doi='10.1038/nn.4268',
       categories=['Spike sorting'],
       urls=[('Journal', 'http://dx.doi.org/10.1038/nn.4268'),
             ('PDF', 'http://www.nature.com/neuro/journal/vaop/ncurrent/pdf/nn.4268.pdf'),
             ('PDF (preprint)', 'https://www.dropbox.com/s/emnup6d0aoyjccs/spikesorting-preprint.pdf?dl=1'),
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
        additional='8:6',
        doi='10.3389/fninf.2014.00006',
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
        additional='26:11',
        doi='10.1162/NECO_a_00661',
        urls=[('Journal', 'http://www.mitpressjournals.org/doi/abs/10.1162/NECO_a_00661'),
              ('PDF', 'http://www.mitpressjournals.org/doi/pdf/10.1162/NECO_a_00661'),
              ('Preprint', 'http://arxiv.org/abs/1309.2848'),
              ('PDF (preprint)', 'https://arxiv.org/pdf/1309.2848'),
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
        book='Encyclopedia of Computational Neuroscience',
        book_editors='Jaeger D, Jung R',
        publisher='SpringerReference',
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
        doi='10.1016/j.jocs.2011.06.002',
        urls=[('Journal', 'http://www.sciencedirect.com/science/article/pii/S1877750311000561'),
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
        authors=u'Kremer Y, Léger J-F, Goodman D, Brette R, Bourdieu L',
        title='Late emergence of the vibrissa direction selectivity map in the rat barrel cortex',
        journal='Journal of Neuroscience',
        additional='31(29)',
        doi='10.1523/JNEUROSCI.6541-10.2011',
        urls=[('Journal', 'http://www.jneurosci.org/content/31/29/10689.abstract'),
              ('PDF (preprint)', 'https://www.dropbox.com/s/ypos545ptv0blf4/barrelcortex-preprint.pdf?dl=1'),
              ],
        categories=['Sensory', 'Modelling', 'Spiking', 'Plasticity'],
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
        name='brian_hears',
        year=2011,
        authors='Fontaine B, Goodman DFM, Benichoux V, Brette R',
        title='Brian Hears: online auditory processing using vectorisation over channels',
        journal='Frontiers in Neuroinformatics',
        additional='5:9',
        doi='10.3389/fninf.2011.00009',
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
        name='modelfitting_focussed_review',
        year=2011,
        authors='Rossant C, Goodman DFM, Fontaine B, Platkiewicz J, Magnusson AK, Brette R',
        title='Fitting neuron models to spike trains',
        journal='Frontiers in Neuroscience',
        additional='5:9',
        doi='10.3389/fnins.2011.00009',
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
        categories=['Sound localisation', 'Modelling', 'Spiking', 'Learning', 'Plasticity'],
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
        additional='6(11): e1000993',
        doi='10.1371/journal.pcbi.1000993',
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
        additional='8, no. 3 (9).',
        doi='10.1007/s12021-010-9082-x',
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
        doi='10.3389/neuro.11.002.2010',
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
        name='brian_focussed_review', selected=False,
        year=2009,
        authors='Goodman DFM, Brette R',
        title='The Brian simulator',
        journal='Frontiers in Neuroscience',
        additional='3(2)',
        doi='10.3389/neuro.01.026.2009',
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
        additional_detail='''
            Note: The Neuromorphic Engineer journal appears to have closed down, so only a direct link to a
            PDF of the original article is included below.
            ''',
        urls=[('PDF', 'https://www.dropbox.com/s/ri7yhwzqk318ff4/brian-neuromorphic-engineer.pdf?dl=0')
              ],
        categories=['Brian'],
        ),
                
    Publication(
        name='brian',
        year=2008,
        authors='Goodman D, Brette R',
        title='Brian: a simulator for spiking neural networks in Python',
        journal='Frontiers in Neuroinformatics',
        additional='2(5)',
        doi='10.3389/neuro.11.005.2008',
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

