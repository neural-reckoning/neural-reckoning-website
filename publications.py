# coding=utf-8
class Publication(object):
    peer_reviewed = True # by default
    def __init__(self, **args):
        for k, v in list(args.items()):
            setattr(self, k, v)
    @property
    def is_preprint(self):
        return isinstance(self.year, str) and self.year=="Preprints"

category_inclusions = {
    'Brian': ['Neural simulation', 'Spiking'],
    'Neural simulation': ['Neuroinformatics', 'Spiking'],
    'Spike sorting': ['Neuroinformatics', 'Spiking', 'Neural data analysis'],
    'Neural data analysis': ['Neuroinformatics'],
    'Neuroinformatics': ['Neuroscience', 'Software'],
    'Sound localisation': ['Auditory', 'Neuroscience'],
    'Auditory': ['Sensory'],
    'Spiking': ['Neuroscience'],
    'Plasticity': ['Neuroscience'],
    'Learning': ['Neuroscience'],
    'Modelling': ['Neuroscience'],
    'Visual': ['Sensory'],
    'Virtual reality': ['Sensory']
    }

category_detail_links = {
    'Brian': 'software.html',
    'Neural simulation': 'neuroinformatics.html',
    'Spike sorting': 'software.html',
    'Neuroinformatics': 'neuroinformatics.html',
    'Sensory': 'sensory.html',
    'Software': 'software.html',
    }

publications = [
#    Publication(
#        name='', #selected=True,
#        year=2021, # set year to 'Preprints' if not published yet
#        authors='',
#        title='',
#        journal='', # for an article
#        publisher='', # for a book
#        conference='', # for a conference paper (use short name here, and long name under additional_detail)
#        phd_thesis=True, publisher='Imperial College London',
#        additional='', # goes after Journal (Year)
#        doi='', # linked to on detail page only
#        book='', book_editors='', # if it's a book chapter, fill this in
#        additional_detail='', # only shown on detail page
#        categories=[],
#        urls=[('Journal', ''),
#              ('Conference', ''),
#              ('PDF', ''),
#              ],
#        abstract="",
#        video_embed='',
#        ),
    ############################### 2021 ###########################################################
      Publication(
            name='humanlikehearing', #selected=True,
            year='Preprints', # set year to 'Preprints' if not published yet
            authors='Weerts L, Rosen S, Clopath C, Goodman DFM',
            title='The Psychometrics of Automatic Speech Recognition',
            # journal='', # for an article
            # additional='', # goes after Journal (Year)
            # doi='', # linked to on detail page only
            # additional_detail='', # only shown on detail page
            categories=['Neuroscience', 'Auditory', 'Machine learning', 'Modelling', 'Software', 'Neuroinformatics'],
            urls=[('Preprint', 'https://www.biorxiv.org/content/10.1101/2021.04.19.440438v2'),
                  ('Preprint (PDF)', 'https://www.biorxiv.org/content/10.1101/2021.04.19.440438v2.full.pdf'),
                  ('Code', 'https://github.com/neural-reckoning/HumanlikeHearing'),
                  ('Twitter', 'https://twitter.com/neuralreckoning/status/1395704493753479168'),
                  ],
            abstract='''
             Automatic speech recognition (ASR) software has been suggested as a candidate model of the human auditory system thanks to dramatic improvements in performance in recent years. To test this hypothesis, we compared several state-of-the-art ASR systems to results from humans on a barrage of standard psychoacoustic experiments. While some systems showed qualitative agreement with humans in some tests, in others all tested systems diverged markedly from humans. In particular, none of the models used spectral invariance, temporal fine structure or speech periodicity in a similar way to humans. We conclude that none of the tested ASR systems are yet ready to act as a strong proxy for human speech recognition. However, we note that the more recent systems with better performance also tend to better match human results, suggesting that continued cross-fertilisation of ideas between human and automatic speech recognition may be fruitful. Our software is released as an open-source toolbox to allow researchers to assess future ASR systems or add additional psychoacoustic measures.
            ''',
            last_tweet_in_thread='1395704552519839746',
            ),
      Publication(
            name='sparse_spiking_gradient_descent', #selected=True,
            year='Preprints', # set year to 'Preprints' if not published yet
            authors='Perez-Nieves N, Goodman DFM',
            title='Sparse Spiking Gradient Descent',
            # journal='', # for an article
            # conference='', # for a conference paper (use short name here, and long name under additional_detail)
            # additional='', # goes after Journal (Year)
            # doi='', # linked to on detail page only
            # additional_detail='', # only shown on detail page
            categories=['Neuroscience', 'Learning', 'Spiking', 'Modelling', 'Machine learning', 'Neural simulation'],
            urls=[('Preprint', 'https://arxiv.org/abs/2105.08810'),
                  ('Preprint (PDF)', 'https://arxiv.org/pdf/2105.08810'),
                  ],
            abstract="There is an increasing interest in emulating Spiking Neural Networks (SNNs) on neuromorphic computing devices due to their low energy consumption. Recent advances have allowed training SNNs to a point where they start to compete with traditional Artificial Neural Networks (ANNs) in terms of accuracy, while at the same time being energy efficient when run on neuromorphic hardware. However, the process of training SNNs is still based on dense tensor operations originally developed for ANNs which do not leverage the spatiotemporally sparse nature of SNNs. We present here the first sparse SNN backpropagation algorithm which achieves the same or better accuracy as current state of the art methods while being significantly faster and more memory efficient. We show the effectiveness of our method on real datasets of varying complexity (Fashion-MNIST, Neuromophic-MNIST and Spiking Heidelberg Digits) achieving a speedup in the backward pass of up to 70x, and 40% more memory efficient, without losing accuracy.",
            ),
      Publication(
            name='jitter', #selected=True,
            year=2021, # set year to 'Preprints' if not published yet
            authors='Su Y, Chung Y, Goodman DFM, Hancock KE, Delgutte B',
            title='Rate and Temporal Coding of Regular and Irregular Pulse Trains in Auditory Midbrain of Normal‑Hearing and Cochlear‑Implanted Rabbits',
            journal='Journal of the Association for Research in Otolaryngology', # for an article
            doi='10.1007/s10162-021-00792-5', # linked to on detail page only
            categories=['Auditory', 'Neuroscience'],
            urls=[('Journal', 'https://link.springer.com/article/10.1007/s10162-021-00792-5'),
                  ('Preprint (PDF)', 'https://www.dropbox.com/s/jy45giagrffkm9j/jitter-preprint.pdf?dl=1'),
                  ],
            abstract="Although pitch is closely related to temporal periodicity, stimuli with a degree of temporal irregularity can evoke a pitch sensation in human listeners. However, the neural mechanisms underlying pitch perception for irregular sounds are poorly understood. Here, we recorded responses of single units in the inferior colliculus (IC) of normal hearing (NH) rabbits to acoustic pulse trains with different amounts of random jitter in the inter-pulse intervals and compared with responses to electric pulse trains delivered through a cochlear implant (CI) in a different group of rabbits. In both NH and CI animals, many IC neurons demonstrated tuning of firing rate to the average pulse rate (APR) that was robust against temporal jitter, although jitter tended to increase the firing rates for APRs ≥ 1280 Hz. Strength and limiting frequency of spike synchronization to stimulus pulses were also comparable between periodic and irregular pulse trains, although there was a slight increase in synchronization at high APRs with CI stimulation. There were clear differences between CI and NH animals in both the range of APRs over which firing rate tuning was observed and the prevalence of synchronized responses. These results suggest that the pitches of regular and irregular pulse trains are coded differently by IC neurons depending on the APR, the degree of irregularity, and the mode of stimulation. In particular, the temporal pitch produced by periodic pulse trains lacking spectral cues may be based on a rate code rather than a temporal code at higher APRs.",
            ),
      Publication(
            name='heterogeneity', selected=True,
            year='Preprints', # set year to 'Preprints' if not published yet
            authors='Perez-Nieves N, Leung VCH, Dragotti PL, Goodman DFM',
            title='Neural heterogeneity promotes robust learning',
            # journal='', # for an article
            # additional='', # goes after Journal (Year)
            # doi='', # linked to on detail page only
            # additional_detail='', # only shown on detail page
            categories=['Neuroscience', 'Learning', 'Visual', 'Auditory', 'Spiking', 'Machine learning', 'Modelling'],
            urls=[('Preprint', 'https://www.biorxiv.org/content/10.1101/2020.12.18.423468v3'),
                  ('Preprint (PDF)', 'https://www.biorxiv.org/content/10.1101/2020.12.18.423468v3.full.pdf'),
                  ('Neurotheory talk (video)', 'https://www.youtube.com/watch?v=V2HFqVfeTPg&feature=youtu.be'),
                  ('Twitter', 'https://twitter.com/neuralreckoning/status/1341011316975218695'),
                  ],
            abstract='''
            The brain has a hugely diverse, heterogeneous structure. Whether or not heterogeneity at the neural level
            plays a functional role remains unclear, and has been relatively little explored in models which are often
            highly homogeneous. We compared the performance of spiking neural networks trained to carry out tasks of
            real-world difficulty, with varying degrees of heterogeneity, and found that it substantially improved task
            performance. Learning was more stable and robust, particularly for tasks with a rich temporal structure. In
            addition, the distribution of neuronal parameters in the trained networks closely matches those observed
            experimentally. We suggest that the heterogeneity observed in the brain may be more than just the byproduct
            of noisy processes, but rather may serve an active and important role in allowing animals to learn in
            changing environments.
            ''',
            video_embed='''
            <iframe class="embed-responsive-item" src="https://www.youtube-nocookie.com/embed/V2HFqVfeTPg"
             frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media;
             gyroscope; picture-in-picture" allowfullscreen></iframe>
            ''',
            last_tweet_in_thread='1341011376299511809',
            ),
      Publication(
            name='snufa_review', selected=True,
            year=2021, # set year to 'Preprints' if not published yet
            authors='Zenke F, Bohté SM, Clopath C, Comşa IM, Göltz J, Maass W, Masquelier T, Naud R, Neftci EO, Petrovici MA, Scherr F, Goodman DFM',
            title='Visualizing a joint future of neuroscience and neuromorphic engineering',
            journal='Neuron', # for an article
            #additional='', # goes after Journal (Year)
            doi='10.1016/j.neuron.2021.01.009', # linked to on detail page only
            categories=['Neuroscience', 'Spiking', 'Machine learning', 'Plasticity', 'Learning', 'Neuroinformatics'],
            urls=[('Journal', 'https://www.sciencedirect.com/science/article/pii/S089662732100009X?dgcid=author'),
                  ('Preprint (PDF)', 'https://www.dropbox.com/s/942rf97l80wyya5/snufa-meeting-report.pdf?dl=1'),
                  ('Workshop', 'https://neural-reckoning.github.io/snn_workshop_2020/'),
                  ('Workshop talk recordings', 'https://www.youtube.com/playlist?list=PL09WqqDbQWHFvM9DFYkM_GfnrVnIdLRhy'),
                  ('Twitter', 'https://twitter.com/neuralreckoning/status/1362107086017036289'),
                  ],
            abstract='''
                  Recent research resolves the challenging problem of building biophysically plausible spiking neural models that
                  are also capable of complex information processing. This advance creates new opportunities in neuroscience and
                  neuromorphic engineering, which we discussed at an online focus meeting.
                  ''',
            last_tweet_in_thread='1362107103998062594',
            ),
      Publication(
            name='nmc3', selected=True,
            year=2021, # set year to 'Preprints' if not published yet
            authors='Achakulvisut T, Ruangrong T, Mineault P, Vogels TP, Peters MAK, Poirazi P, Rozell C, Wyble B, Goodman DFM, Kording KP',
            title='Towards democratizing and automating online conferences: lessons from the Neuromatch conferences',
            journal='Trends in Cognitive Sciences', # for an article
            doi='10.1016/j.tics.2021.01.007', # linked to on detail page only
            categories=['Neuroscience', 'Machine learning'],
            urls=[('Journal', 'https://www.cell.com/trends/cognitive-sciences/fulltext/S1364-6613(21)00009-7'),
                  ('Preprint (PDF)', 'https://www.dropbox.com/s/snqgeuyt38vekfx/nmc3.pdf?dl=1'),
                  ('Neuromatch', 'https://www.neuromatch.io/'),
                  ],
            abstract="""
                  Legacy conferences are costly, time-consuming, and exclude scientists lacking various resources
                  or abilities. During the 2020 pandemic, we created an online conference platform, Neuromatch
                  Conferences, aimed at developing technological and cultural changes to make conferences more
                  democratic, scalable, and accessible. We discuss the lessons we learned.
                  """,
            peer_reviewed=False,
            ),
    Publication(
        name='comments_on_edge_bundling',  # selected=True,
        year=2021,
        authors='Zheng JX, Pawar S, Goodman DFM',
        title='Further Towards Unambiguous Edge Bundling: Investigating Power-Confluent Drawings for Network Visualization',
        journal='IEEE Transactions on Visualization and Computer Graphics',
        doi='10.1109/TVCG.2019.2944619',
        categories=['Visualisation', 'Software'],
        urls=[('Journal', 'https://ieeexplore.ieee.org/document/8852738'),
              ('Preprint', 'https://arxiv.org/abs/1810.09948'),
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
            name='zheng_thesis',
            year=2021, # set year to 'Preprints' if not published yet
            authors='Zheng JX',
            title='Advances in network visualisation with an application to serious games',
            phd_thesis=True, publisher='Imperial College London',
            # doi='', # linked to on detail page only
            # additional_detail='', # only shown on detail page
            categories=['Machine learning', 'Visualisation', 'Software', 'Ecology'],
            urls=[('Thesis (PDF)', 'https://imperialcollegelondon.box.com/s/n2osvtt8exnturc5mzemzuou27vrb5i9')],
            abstract='''
            This thesis concerns the visualisation of networks, through an in-depth study into
            the node-link diagram representation. Three subtopics are explored within this
            space. The first is the problem of node layout, where the optimisation of a popular
            energy function, known as stress, is improved through an algorithm known
            as stochastic gradient descent. The second is the method of edge bundling, where
            the idea of hierarchical edge bundling is explored in the absence of a known ground
            truth hierarchy. Its similarity to a topologically lossless bundling method known
            as power-confluent drawing is then leveraged, in order to improve technical problems
            with the underlying algorithms. The final topic is an engineering application
            in the form of a serious game called EcoBuilder, which utilises the node-link diagram
            to visualise the dynamical behaviour of food webs. Its purpose is to crowdsource
            research through a citizen science approach, with outcomes in both visualisation
            and mathematical ecology.
            ''',
            ),
    ############################### 2020 ###########################################################
      Publication(
            name='hathway_thesis',
            year=2020, # set year to 'Preprints' if not published yet
            authors='Hathway P',
            title='Biologically-inspired machine learning approaches to large-scale neural data analysis',
            phd_thesis=True, publisher='Imperial College London',
            # doi='', # linked to on detail page only
            # additional_detail='', # only shown on detail page
            categories=['Machine learning', 'Visualisation', 'Software', 'Neuroscience', 'Neuroinformatics', 'Neural data analysis', 'Learning', 'Spiking', 'Plasticity'],
            urls=[('Thesis (PDF)', 'https://imperialcollegelondon.box.com/s/2n8psmtrlxs5ymmus6vailh7i5x2wqmn')],
            abstract='''
            <p>Recent progress in recording techniques now allows researchers to record
            from hundreds and even thousands of neurons simultaneously. New, scalable
            methods need to be developed to handle such large data sets. Ideally
            these methods should not only analyse the multi-dimensional data, but also
            provide results which could be interpreted by the brain.</p>

            <p>One key problem in neuronal data analysis is to identify neuronal assemblies
            i.e. groups of neurons displaying coordinated neuronal activity. Currently
            available methods either search for assemblies whose neurons participate
            in repeated spike sequences or search for assemblies whose neurons display
            similar firing rate modulations. In this thesis, I present two approaches
            to the search for neuronal assemblies.</p>

            <p>I investigate whether a spiking neural network equipped with biologically
            plausible synaptic learning rules can provide a biologically interpretable way
            of finding repeating spike patterns in neuronal data. Due to the similarities
            between spiking neural networks to how brains function, this might be very
            close to how the brain itself detects such repeated activity.</p>

            <p>Furthermore, I present neural topic modelling – a new data analysis method
            for large neuronal data sets. Based on a machine learning method from text
            mining, neural topic modelling is scalable and produces interpretable results.
            By including multiple features of neuronal spike trains and even other
            data types such as local field potentials into the analysis, I can expand the
            definition of neuronal assemblies to any type of neuronal activity features
            which are co-modulated. The application of neural topic modelling to neuronal
            recordings reveals interactions between features of neuronal activity
            which have previously not been identified.</p>

            <p>Since both approaches are biologically plausible, the results from both
            methods can be used to generate hypotheses about how the brain processes
            information and may reveal hitherto unknown information processing pathways.</p>
            ''',
            ),
    Publication(
       name='elife_labs_matching', #selected=True,
       year=2020, # set year to 'Preprints' if not published yet
       authors='Achakulvisut T, Ruangrong T, Acuna DE, Wyble B, Goodman D, Kording K',
       title='neuromatch: Algorithms to match scientists',
       journal='eLife Labs', # for an article
       categories=['Neuroscience', 'Machine learning'],
       urls=[('Journal', 'https://elifesciences.org/labs/5ed408f4/neuromatch-algorithms-to-match-scientists'),
             ('Neuromatch', 'https://www.neuromatch.io/'),
             ],
       abstract="""We developed machine-learning algorithms to help connect scientists during online
                   research conferences. """,
       peer_reviewed=False,
       ),
    Publication(
       name='elife_neuromatch', #selected=True,
       year=2020, # set year to 'Preprints' if not published yet
       authors='Achakulvisut T, Ruangrong T, Bilgin I, Van Den Bossche S, Wyble B, Goodman DFM, Kording KP',
       title='Point of View: Improving on legacy conferences by moving online',
       journal='eLife', # for an article
       additional='9:e57892', # goes after Journal (Year)
       doi='10.7554/eLife.57892', # linked to on detail page only
       categories=['Neuroscience', 'Machine learning'],
       urls=[('Journal', 'https://elifesciences.org/articles/57892'),
             ('Neuromatch', 'https://www.neuromatch.io/'),
             ],
       abstract="""Scientific conferences and meetings have an important role in research, but they
            also suffer from a number of disadvantages: in particular, they can have a massive
            carbon footprint, they are time-consuming, and the high costs involved in attending can
            exclude many potential participants. The COVID-19 pandemic has led to the cancellation
            of many conferences, forcing the scientific community to explore online alternatives.
            Here, we report on our experiences of organizing an online neuroscience conference,
            neuromatch, that attracted some 3000 participants and featured two days of talks,
            debates, panel discussions, and one-on-one meetings facilitated by a matching algorithm.
            By offering most of the benefits of traditional conferences, several clear advantages,
            and with fewer of the downsides, we feel that online conferences have the potential to
            replace many legacy conferences.""",
       peer_reviewed=False,
       ),
    Publication(
       name='learning_sound_loc_limited_sup', #selected=True,
       year='Preprints', # set year to 'Preprints' if not published yet
       authors='Chu Y, Luk W, Goodman D',
       title='Learning Absolute Sound Source Localisation With Limited Supervisions',
       #journal='', # for an article
       #conference='', # for a conference paper (use short name here, and long name under additional_detail)
       #additional='', # goes after Journal (Year)
       #doi='', # linked to on detail page only
       #additional_detail='', # only shown on detail page
       categories=['Machine learning', 'Auditory', 'Sound localisation', 'Modelling', 'Neuroscience', 'Learning'],
       urls=[('Preprint', 'https://arxiv.org/abs/2001.10605'),
             ('Preprint (PDF)', 'https://arxiv.org/pdf/2001.10605'),
             ],
       abstract="An accurate auditory space map can be learned from auditory experience, for example during "
                "development or in response to altered auditory cues such as a modified pinna. We studied neural "
                "network models that learn to localise a single sound source in the horizontal plane using binaural "
                "cues based on limited supervisions. These supervisions can be unreliable or sparse in real life. "
                "First, a simple model that has unreliable estimation of the sound source location is built, "
                "in order to simulate the unreliable auditory orienting response of newborns. It is used as a Teacher "
                "that acts as a source of unreliable supervisions. Then we show that it is possible to learn a "
                "continuous auditory space map based only on noisy left or right feedbacks from the Teacher. "
                "Furthermore, reinforcement rewards from the environment are used as a source of sparse supervision. "
                "By combining the unreliable innate response and the sparse reinforcement rewards, an accurate "
                "auditory space map, which is hard to be achieved by either one of these two kind of supervisions, "
                "can eventually be learned. Our results show that the auditory space mapping can be calibrated even "
                "without explicit supervision. Moreover, this study implies a possibly more general neural mechanism "
                "where multiple sub-modules can be coordinated to facilitate each other's learning process under "
                "limited supervisions. ",
       ),
    Publication(
        name='brian2genn',  # selected=True,
        year=2020,  # set year to 'Preprints' if not published yet
        authors='Stimberg M, Goodman DFM, Nowotny T',
        title='Brian2GeNN: a system for accelerating a large variety of spiking neural networks with graphics hardware',
        journal='Scientific Reports',
        additional='10, 410',
        doi='10.1038/s41598-019-54957-7',
        categories=['Brian', 'Neuroinformatics', 'Neural simulation'],
        urls=[('Journal', 'https://www.nature.com/articles/s41598-019-54957-7'),
              ('Journal (PDF)', 'https://www.nature.com/articles/s41598-019-54957-7.pdf'),
              ('Code (GitHub)', 'https://github.com/brian-team/brian2genn'),
              ('Documentation', 'https://brian2genn.readthedocs.io/en/stable/'),
              ('Preprint', 'https://www.biorxiv.org/content/early/2018/10/20/448050'),
              ('Preprint (PDF)', 'https://www.biorxiv.org/content/early/2018/10/20/448050.full.pdf'),
              ],
        abstract='"Brian" is a popular Python-based simulator for spiking neural networks, commonly used in '
                 'computational neuroscience. GeNN is a C++-based meta-compiler for accelerating spiking neural '
                 'network simulations using consumer or high performance grade graphics processing units (GPUs). Here '
                 'we introduce a new software package, Brian2GeNN, that connects the two systems so that users can '
                 'make use of GeNN GPU acceleration when developing their models in Brian, without requiring any '
                 'technical knowledge about GPUs, C++ or GeNN. The new Brian2GeNN software uses a pipeline of code '
                 'generation to translate Brian scripts into C++ code that can be used as input to GeNN, '
                 "and subsequently can be run on suitable NVIDIA GPU accelerators. From the user's perspective, "
                 'the entire pipeline is invoked by adding two simple lines to their Brian scripts. We have shown '
                 'that using Brian2GeNN, two non-trivial models from the literature can run tens to hundreds of times '
                 'faster than on CPU.',
        ),
    ############################### 2019 ###########################################################
      Publication(
            name='lestang_thesis',
            year=2019, # set year to 'Preprints' if not published yet
            authors='Lestang J-H',
            title='The role of canonical neural computations in sound localization',
            phd_thesis=True, publisher='Imperial College London',
            # doi='', # linked to on detail page only
            # additional_detail='', # only shown on detail page
            categories=['Neuroscience', 'Modelling', 'Auditory', 'Sound localisation'],
            urls=[('Thesis', 'https://spiral.imperial.ac.uk/handle/10044/1/76509'),
                  ('Thesis (PDF)', 'https://spiral.imperial.ac.uk/bitstream/10044/1/76509/1/Lestang-J-2019-PhD-Thesis.pdf')],
            abstract='''
            Localizing sounds is an important ability for many species. However, reverberative sounds
            present a signicant challenge to the auditory system as later arriving reverberations may carry
            confounding localization cues. The 'precedence eect' refers to a set of perceptual behaviours
            related to this situation. Studies investigating the precedence eect observed that the auditory
            system tends to focus the core of the localization process on the computation of localization
            cues carried by the rst arriving sound. Doing so relieves the auditory system from dealing
            with contradictory localization cues in later arriving sounds. A recent study by Dietz et al.
            (2013) conrmed that human listeners use this approach to deal with dynamic localization
            cues. In order to provide an explanation for this nding, we rst tested several auditory models
            on the specic task described in Dietz et al. (2013) in order to shortlist possible mechanisms
            capable of accounting for the early extraction of temporal binaural cues. We found that the
            best candidates to account for this data are single cell mechanisms, such as adaptation and
            onset ring, as well as inhibitory population mechanisms. To further understand how each
            mechanism contributes to the suppression of lagging sounds, we designed more general models
            capable of demonstrating the principal features of each mechanism. We tested these models
            thoroughly and found that all mechanisms were able to reproduce the results over a wide range
            of parameters. This nding suggests that mechanisms responsible for the precedence eect
            may not be specialized to perform this specic task but instead may be the results of more
            commonly found neural circuits in the brain. Finally, to facilitate comparing the performance
            of auditory models on psychoacoustical data, we also designed and implemented an auditory
            modelling framework capable of addressing many challenges existing in the eld of auditory
            modelling.
            ''',
            ),
    Publication(
       name='gamification_sound_localisation', #selected=True,
       year=2019, # set year to 'Preprints' if not published yet
       authors='Steadman MA, Kim C, Lestang JH, Goodman DFM, Picinali L',
       title='Short-term effects of sound localization training in virtual reality',
       journal='Scientific Reports',
       doi='10.1038/s41598-019-54811-w',
       additional='9, 18284',
       categories=['Auditory', 'Sound localisation', 'Learning', 'Virtual reality'],
       urls=[('Journal', 'https://www.nature.com/articles/s41598-019-54811-w'),
             ('PDF (journal)', 'https://www.nature.com/articles/s41598-019-54811-w.pdf'),
             ('Data and code (Zenodo)', 'https://zenodo.org/record/2594832'),
             ('Preprint', 'https://www.biorxiv.org/content/10.1101/207753v3'),
             ('PDF (preprint)', 'https://www.biorxiv.org/content/biorxiv/early/2019/07/10/207753.full-text.pdf'),
             ],
       abstract='Head-related transfer functions (HRTFs) capture the direction-dependant way that sound interacts '
                'with the head and torso. In virtual audio systems, which aim to emulate these effects, '
                'non-individualized, generic HRTFs are typically used leading to an inaccurate perception of virtual '
                "sound location. Training has the potential to exploit the brain's ability to adapt to these "
                'unfamiliar cues. In this study, three virtual sound localization training paradigms were evaluated; '
                'one provided simple visual positional confirmation of sound source location, a second introduced '
                'game design elements ("gamification") and a final version additionally utilized head-tracking to '
                'provide listeners with experience of relative sound source motion ("active listening"). The results '
                'demonstrate a significant effect of training after a small number of short (12-minute) training '
                'sessions, which is retained across multiple days. Gamification alone had no significant effect on '
                'the efficacy of the training, but active listening resulted in a significantly greater improvements '
                'in localization accuracy. In general, improvements in virtual sound localization following training '
                'generalized to a second set of non-individualized HRTFs, although some HRTF-specific changes were '
                'observed in polar angle judgement for the active listening group. The implications of this on the '
                'putative mechanisms of the adaptation process are discussed.',
       ),
    Publication(
       name='attention_ccn2019', #selected=True,
       year=2019, # set year to 'Preprints' if not published yet
       authors='Chu Y, Goodman DFM',
       title='An Inference Network Model for Goal-directed Attentional Selection',
       conference='Cognitive Computational Neuroscience',
       additional='', # goes after Journal (Year)
       additional_detail='2019 Conference on Cognitive Computational Neuroscience, 13-16 September 2019, Berlin, Germany',
       doi='10.32470/CCN.2019.1431-0', # linked to on detail page only
       categories=['Machine learning', 'Modelling', 'Visual'],
       urls=[('Abstract', 'https://ccneuro.org/2019/Papers/ViewPapers.asp?PaperNum=1431'),
             ('PDF', 'https://ccneuro.org/2019/showDoc.php?s=W&pn=1431'),
             ],
       abstract='''
       "Listen to the cello in this symphony!" How can we direct selective attention according to different goals, even
       in distracting environments which we haven't experienced before? It is an essential cognitive ability of the
       brain, but remains challenging for machines. We developed a computational model that can identify individual
       digits in images containing multiple overlapping digits, without ever having seen overlapping digits during
       training. The goal-driven attentional selection is modelled as inferring the posterior distribution of latent
       variables (the attended target) in a generative model, conditioned on both sensory input and different semantic
       goals. A neural network model has been build to efficiently carry out the the inference process by predicting the
       most likely results, instead of using classic per-sample based iterative optimization methods which may not
       naturally map onto neural structures. Our model also help to understand how top-down and bottom-up attention are
       combined during perception in the brain.
       ''',
       ),
    Publication(
       name='heterogeneity_ccn2019', #selected=True,
       year=2019, # set year to 'Preprints' if not published yet
       authors='Perez-Nieves N, Leung VCH, Dragotti PL, Goodman DFM',
       title='Advantages of heterogeneity of parameters in spiking neural network training',
       conference='Cognitive Computational Neuroscience',
       additional='', # goes after Journal (Year)
       additional_detail='2019 Conference on Cognitive Computational Neuroscience, 13-16 September 2019, Berlin, Germany',
       doi='10.32470/CCN.2019.1173-0', # linked to on detail page only
       categories=['Machine learning', 'Spiking', 'Modelling'],
       urls=[('Abstract', 'https://ccneuro.org/2019/Papers/ViewPapers.asp?PaperNum=1173'),
             ('PDF', 'https://ccneuro.org/2019/showDoc.php?s=W&pn=1173'),
             ],
       abstract='It is very common in studies of the learning capabilities of spiking neural networks (SNNs) to use '
                'homogeneous neural and synaptic parameters (time constants, thresholds, etc.). Even in studies in '
                'which these parameters are distributed heterogeneously, the advantages or disadvantages of the '
                'heterogeneity have rarely been studied in depth. By contrast, in the brain, neurons and synapses are '
                'highly diverse, leading naturally to the hypothesis that this heterogeneity may be advantageous for '
                'learning. Starting from two state-of-the-art methods for training spiking neural networks (Nicola & '
                'Clopath, 2017, Shrestha & Orchard 2018), we found that adding parameter heterogeneity reduced errors '
                'when the network had to learn more complex patterns, increased robustness to hyperparameter '
                'mistuning, and reduced the number of training iterations required. We propose that neural '
                'heterogeneity may be an important principle for brains to learn robustly in real world environments '
                'with highly complex structure, and where task-specific hyperparameter tuning may be impossible. '
                'Consequently, heterogeneity may also be a good candidate design principle for artificial neural '
                'networks, to reduce the need for expensive hyperparameter tuning as well as for reducing training '
                'time. '
       ),
    Publication(
       name='neural_topic_modelling_ccn2019', #selected=True,
       year=2019, # set year to 'Preprints' if not published yet
       authors='Hathway P, Goodman DFM',
       title=' Neural Topic Modelling',
       conference='Cognitive Computational Neuroscience',
       additional='', # goes after Journal (Year)
       additional_detail='2019 Conference on Cognitive Computational Neuroscience, 13-16 September 2019, Berlin, Germany',
       doi='10.32470/CCN.2019.1382-0', # linked to on detail page only
       categories=['Machine learning', 'Neuroinformatics', 'Neural data analysis'],
       urls=[('Abstract', 'https://ccneuro.org/2019/Papers/ViewPapers.asp?PaperNum=1382'),
             ('PDF', 'https://ccneuro.org/2019/showDoc.php?s=W&pn=1382'),
             ],
       abstract='We introduce neural topic modelling - an unsupervised, scalable and interpretable neural data '
                'analysis tool which can be applied across different spatial and temporal scales. The aim is an '
                'approach that can handle the ever-increasing number of neurons recorded by high channel count '
                'multi-electrode arrays. Neural topic modelling is based on latent Dirichlet allocation, '
                'a method routinely used in text mining to find latent topics in texts. The spike trains are '
                'converted into "neural words" - the presence or absence of discrete events (e.g. neuron 1 has a '
                'higher firing rate than usual). Neural topic modelling results in a number of topics (probability '
                'distributions over words) which best explain the given co-occurrences of neural words over time. '
                'Applied to an electrophysiological dataset of mouse visual cortex, hippocampus and thalamus neurons, '
                'neural topic modelling groups neural words into topics which exhibit common attributes such as '
                'overlapping receptive fields or proximity on the recording electrode. It recovers these '
                'relationships despite receiving no knowledge about the cortex topography or about the spatial '
                'structure of the stimuli. Choosing neural activity patterns as neural words that are relevant to the '
                'brain makes the topics interpretable by both the brain and researchers, setting neural topic '
                'modelling apart from other machine learning approaches.'
       ),
    Publication(
       name='data_driven_auditory_ccn2019', #selected=True,
       year=2019, # set year to 'Preprints' if not published yet
       authors='Weerts L, Clopath C, Goodman DFM',
       title=' A Unifying Framework for Neuro-Inspired, Data-Driven Detection of Low-Level Auditory Features',
       conference='Cognitive Computational Neuroscience',
       additional='', # goes after Journal (Year)
       additional_detail='2019 Conference on Cognitive Computational Neuroscience, 13-16 September 2019, Berlin, Germany',
       doi='10.32470/CCN.2019.1245-0', # linked to on detail page only
       categories=['Machine learning', 'Auditory', 'Modelling'],
       urls=[('Abstract', 'https://ccneuro.org/2019/Papers/ViewPapers.asp?PaperNum=1245'),
             ('PDF', 'https://ccneuro.org/2019/showDoc.php?s=W&pn=1245'),
             ],
       abstract='Our understanding of hearing and speech recognition rests on controlled experiments requiring simple '
                'stimuli. However, these stimuli often lack the characteristics of complex sounds such as speech. We '
                'propose an approach that combines neural modelling with machine learning to determine relevant '
                'low-level auditory features. Our approach bridges the gap between detailed neuronal models that '
                'capture specific auditory responses, and research on the statistics of real-world speech data and '
                'speech recognition. First, we introduce a feature detection model with a modest number of parameters '
                'that is compatible with auditory physiology. In order to objectively determine relevant feature '
                'detectors within the model parameter space, the model is tested in a speech classification task, '
                'using a simple classifier that approximates the information bottleneck. This framework allows us to '
                'determine the best model parameters and their neurophysiological and psychoacoustic implications. We '
                'show that our model can capture a variety of well-studied features (such as amplitude modulations '
                'and onsets) and allows us to unify concepts from different areas of hearing research. Our approach '
                'has various potential applications. Firstly, it could lead to new, testable experimental hypotheses '
                'for understanding hearing. Moreover, promising features could be directly applied as a new acoustic '
                'front-end for speech recognition systems.'
       ),
    Publication(
       name='brian2', selected=True,
       year=2019, # set year to 'Preprints' if not published yet
       authors='Stimberg M, Brette R, Goodman DFM',
       title='Brian 2, an intuitive and efficient neural simulator',
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
       title='General neural mechanisms can account for rising slope preference in localization of ambiguous sounds',
       #journal='', # for an article
       #additional='', # goes after Journal (Year)
       #doi='', # linked to on detail page only
       #additional_detail='', # only shown on detail page
       categories=['Auditory', 'Sound localisation', 'Modelling'],
       urls=[('Preprint', 'https://www.biorxiv.org/content/10.1101/687178v2'),
             ('Preprint (PDF)', 'https://www.biorxiv.org/content/10.1101/687178v2.full.pdf'),
             ('Code (GitHub)', 'https://github.com/neural-reckoning/simple_ambb_modelling'),
             ('Live code (Binder)', 'https://mybinder.org/v2/gh/neural-reckoning/simple_ambb_modelling/master?filepath=index.ipynb'),
             ],
       abstract='''
       Sound localization in reverberant environments is a difficult task that human listeners perform effortlessly.
       Many neural mechanisms have been proposed to account for this behavior. Generally they rely on emphasizing localization
       information at the onset of the incoming sound while discarding localization cues that arrive later. We modelled several
       of these mechanisms using neural circuits commonly found in the brain and tested their performance in the context of
       experiments showing that, in the dominant frequency region for sound localisation, we have a preference for auditory cues
       arriving during the rising slope of the sound energy (Dietz et al., 2013). We found that both single cell mechanisms (onset
       and adaptation) and population mechanisms (lateral inhibition) were easily able to reproduce the results across a very wide
       range of parameter settings. This suggests that sound localization in reverberant environments may not require specialised
       mechanisms specific to perform that task, but could instead rely on common neural circuits in the brain. This would allow
       for the possibility of individual differences in learnt strategies or neuronal parameters. This research is fully
       reproducible, and we made our code available to edit and run online via interactive live notebooks.
       ''',
       ),
    Publication(
       name='auditory_anchors', #selected=True,
       year=2019, # set year to 'Preprints' if not published yet
       authors='Engel I, Goodman DFM, Picinali L',
       title='The Effect of Auditory Anchors on Sound Localization: A Preliminary Study',
       conference='Immersive and Interactive Audio ', # for a conference paper (use short name here, and long name under additional_detail)
       additional='', # goes after Journal (Year)
       doi='', # linked to on detail page only
       additional_detail='2019 AES International Conference on Immersive and Interactive Audio (March 2019)', # only shown on detail page
       categories=['Sound localisation', 'Virtual reality'],
       urls=[('Conference', 'http://www.aes.org/e-lib/browse.cfm?elib=20388'),
             ],
       abstract='Traditional sound localization studies are often performed in anechoic chambers and in complete '
                'darkness. In our daily life, however, we are exposed to rich auditory scenes with multiple sound '
                'sources and complementary visual information. Although it is understood that the presence of maskers '
                'hinders auditory spatial awareness, it is not known whether competing sound sources can provide '
                'spatial information that helps in localizing a target stimulus. In this study, we explore the effect '
                'of presenting controlled auditory scenes with different amounts of visual and spatial cues during a '
                'sound localization task. A novel, gamified localization task is also presented. Preliminary results '
                'suggest that subjects who are exposed to audio-visual anchors show faster improvements than those '
                'who are not.',
       ),
    Publication(
       name='astrocytes', #selected=True,
       year=2019,
       authors='Stimberg M, Goodman DFM, Brette R, De Pittà M',
       title='Modeling neuron-glia interactions with the Brian 2 simulator',
       publisher='Springer',
       book_chapter=True,
       book='Computational Glioscience',
       book_editors='De Pittà M, Berry H',
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
############################### 2018 ###########################################################
    Publication(
       name='vr_mobile_binaural', #selected=True,
       year=2018, # set year to 'Preprints' if not published yet
       authors='Chungeun K, Steadman M, Lestang JH, Goodman DFM, Picinali L',
       title='A VR-Based Mobile Platform for Training to Non-Individualized Binaural 3D Audio',
       conference='Audio Engineering Society ', # for a conference paper (use short name here, and long name under additional_detail)
       additional='', # goes after Journal (Year)
       doi='', # linked to on detail page only
       additional_detail='AES Convention: 144 (May 2018)', # only shown on detail page
       categories=['Sound localisation', 'Virtual reality'],
       urls=[('Conference', 'http://www.aes.org/e-lib/browse.cfm?elib=19406'),
             ],
       abstract="Delivery of immersive 3D audio with arbitrarily-positioned sound sources over headphones often "
                "requires processing of individual source signals through a set of Head-Related Transfer Functions ("
                "HRTFs), the direction-dependent filters that describe the propagation of sound in an anechoic "
                "environment from the source to the listener's ears. The individual morphological differences and the "
                "impracticality of HRTF measurement make it difficult to deliver completely individualized 3D audio "
                "in this manner, and instead lead to the use of previously-measured non-individual sets of HRTFs. In "
                "this study a VR-based mobile sound localization training prototype system is introduced that uses "
                "HRTF sets for audio. It consists of a mobile phone as a head-mounted device, a hand-held Bluetooth "
                "controller, and a network-enabled PC with a USB audio interface and a pair of headphones. The "
                "virtual environment was developed on the mobile phone such that the user can listen-to/navigate-in "
                "an acoustically neutral scene and locate invisible target sound sources presented at random "
                "directions using non-individualized HRTFs in repetitive sessions. Various training paradigms can be "
                "designed with this system, with performance-related feedback provided according to the user's "
                "localization accuracy, including visual indication of the target location, and some aspects of a "
                "typical first-person shooting game, such as enemies, scoring, and level advancement. An experiment "
                "was conducted using this system in which 11 subjects went through multiple training sessions, "
                "using non-individualized HRTF sets. The localization performance evaluations showed reduction of "
                "overall localization angle error over repeated training sessions, reflecting lower front-back "
                "confusion rates.",
       ),
    Publication(
       name='confluent_hierarchical_gd2018', #selected=True,
       year=2018, # set year to 'Preprints' if not published yet
       authors='Zheng JX, Pawar S, Goodman DFM',
       title='Confluent* Drawings by Hierarchical Clustering',
       conference='Graph Drawing and Network Visualization', # for a conference paper (use short name here, and long name under additional_detail)
       additional='', # goes after Journal (Year)
       doi='10.1007/978-3-030-04414-5', # linked to on detail page only
       additional_detail='26th International Symposium, GD 2018, Barcelona, Spain, September 26-28, 2018, Proceedings', # only shown on detail page
       categories=['Visualisation', 'Machine learning'],
       urls=[('Proceedings', 'https://link.springer.com/book/10.1007/978-3-030-04414-5'),
             ('Proceedings PDF (see p. 640)', 'https://link.springer.com/content/pdf/10.1007%2F978-3-030-04414-5.pdf'),
             ],
       abstract='Recently an edge bundling technique known as confluent* drawing was applied to general graphs by Bach '
                'et al. (2017) by leveraging power graph decomposition (a form of edge compression that groups similar '
                'vertices together, merging edges shared among group members). We explore the technique further by '
                'demonstrating the equivalence between confluent drawing and the hierarchical edge bundling of Holten '
                '(2006), thereby opening the door for existing hierarchical clustering algorithms to be used instead of '
                'power graphs to produce confluent drawings for general graphs. We investigate various popular '
                'hierarchical clustering methods, and present a qualitative experimental comparison between them. We '
                'also introduce a new distance measure for agglomerative clustering that outperforms previous measures, '
                'and make recommendations for using the method in practice.',
       ),
    Publication(
       name='codegen_review', #selected=True,
       year=2018,
       authors=('Blundell I, Brette R, Cleland TA, Close TG, Coca D, Davison AP, Diaz-Pier S, Musoles CF, '
                'Gleeson P, Goodman DFM, Hines M, Hopkins MW, Kumbhar P, Lester DR, Marin B, Morrison A, '
                'Müller E, Nowotny T, Peyser A, Plotnikov D, Richmond P, Rowley A, Rumpe B, Stimberg M, '
                'Stokes AB, Tomkins A, Trensch G, Woodman M, Eppler JM'),
       title='Code Generation in Computational Neuroscience: A Review of Tools and Techniques',
       journal='Frontiers in Neuroinformatics',
       doi='10.3389/fninf.2018.00068',
       categories=['Neuroinformatics', 'Neural simulation', 'Brian'],
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
       categories=['Visualisation', 'Machine learning', 'Software'],
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
       name='vcn_regularity', #selected=True,
       year=2018,
       authors='Goodman DFM, Winter IM, Léger AC, de Cheveigné A, Lorenzi C',
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
############################### 2017 ###########################################################
    Publication(
       name='roles_inhibition_adaptation_spatial_hearing', #selected=True,
       year=2017, # set year to 'Preprints' if not published yet
       authors='Lestang JH, Goodman DF',
       title='The roles of inhibition and adaptation for spatial hearing in difficult listening conditions',
       conference='Acoustical Society of America', # for a conference paper (use short name here, and long name under additional_detail)
       additional='', # goes after Journal (Year)
       doi='10.1121/1.4987838 ', # linked to on detail page only
       additional_detail='Acoustical Society of America meeting 2017', # only shown on detail page
       categories=['Auditory', 'Modelling'],
       urls=[('Conference', 'https://asa.scitation.org/doi/abs/10.1121/1.4987838'),
             ],
       abstract="The computation of binaural cues such as the Interaural Time Difference (ITD) and Interaural Level "
                "Difference (ILD) by the auditory system is known to play an important role in spatial hearing. It is "
                "not yet understood how such computations are performed in realistic acoustic environments where "
                "noise and reverberations are present. It has been hypothesized that robust sound localization is "
                "achieved through the extraction of the ITD information in the rising part of amplitude modulated ("
                "AM) sounds. Dietz et al. (2013) tested this hypothesis using psychoacoustics and MEG experiments. "
                "They presented AM sounds with ITDs varying during the course of one AM cycle. Their results showed "
                "that participants preferentially extracted the ITD information in the rising portion of the AM "
                "cycle. We designed a computational model of the auditory pathway to investigate the neural "
                "mechanisms involved in this process. Two mechanisms were tested. The first one corresponds to the "
                "adaptation in the auditory nerve fibers. The second mechanism occurs after coincidence detection and "
                "involves a winner-take-all network of ITD sensitive neurons. Both mechanisms qualitatively accounted "
                "for the data, consequently we suggest further experiments based on similar stimuli to distinguish "
                "between the two mechanisms. Dietz et al. (2013), “Emphasis of spatial cues in the temporal fine "
                "structure during the rising segments of amplitude-modulated sounds,” Proc. Natl. Acad. Sci. 110(37), "
                "15151-15156.",
       ),
    Publication(
        name='model_initiative_asa2017',  # selected=True,
        year=2017,  # set year to 'Preprints' if not published yet
        authors='Dietz M, Marquardt T, Majdak P, Stern RM, Hartmann WM, Goodman DF, Ewert SD',
        title='An initiative for testability and comparability of binaural models',
        conference='Acoustical Society of America',
        # for a conference paper (use short name here, and long name under additional_detail)
        additional='',  # goes after Journal (Year)
        doi='10.1121/1.4987810',  # linked to on detail page only
        additional_detail='Acoustical Society of America meeting 2017',  # only shown on detail page
        categories=['Auditory', 'Neuroinformatics'],
        urls=[('Conference', 'https://asa.scitation.org/doi/abs/10.1121/1.4987810'),
              ],
        abstract="A framework aimed at improving the testability and comparability of binaural models will be "
                 "presented. The framework consists of two key elements: (1) a repository of testing software that "
                 "evaluates the models against published data and (2) a model repository. While the framework is "
                 "also intended for physiological data, the planned initial contribution will be psychoacoustical "
                 "data together with their psychoacoustical testing protocols, as well as existing binaural models "
                 "from available auditory toolboxes. Researchers will be invited to provide their established as "
                 "well as newly developed models in whatever programming language they prefer, given the models are "
                 "compatibility with the proposed interface to the testing software. This entails that the models "
                 "act as artificial observers, testable with exactly the same procedure as the human subjects. A "
                 "simple communication protocol based on wav and txt-files is proposed because these are supported "
                 "by every programming environment, and are able connect models and testing software of any "
                 "programming language. Examples will illustrate the principle of testing models with unaltered "
                 "signal processing stages on various seminal data sets such as tone detection in so-called "
                 "double-delayed masking noise, or lateralization of ¾-period delayed noise and sounds with "
                 "temporally asymmetric envelopes.",
    ),
    Publication(
        name='hypothesis_driven_asa2017',  # selected=True,
        year=2017,  # set year to 'Preprints' if not published yet
        authors='Goodman DF',
        title='On the use of hypothesis-driven reduced models in auditory neuroscience',
        conference='Acoustical Society of America',
        # for a conference paper (use short name here, and long name under additional_detail)
        additional='',  # goes after Journal (Year)
        doi='10.1121/1.4987594',  # linked to on detail page only
        additional_detail='Acoustical Society of America meeting 2017',  # only shown on detail page
        categories=['Auditory', 'Modelling'],
        urls=[('Conference', 'https://asa.scitation.org/doi/abs/10.1121/1.4987594'),
              ],
        abstract="There are a number of detailed models of auditory neurons that are able to reproduce a wide range "
                 "of phenomena. However, using these models to test hypotheses can be challenging, as they have many "
                 "parameters and complex interacting subsystems. This makes it difficult to investigate the function "
                 "of a mechanism by varying just one parameter in isolation, or to assess the robustness of a model "
                 "by systematically varying many parameters. In some cases, by limiting the scope of a model to "
                 "testing a specific hypothesis using a particular set of stimuli, it is possible to create a "
                 "reduced mathematical model with relatively few, independent parameters. This has considerable "
                 "advantages with respect to the problems above. In particular, if a certain behavior is robust and "
                 "does not depend on finely tuned parameters, then different implementations are more likely to "
                 "produce the same results—a key property for reproducible research. In addition, the code for these "
                 "models is typically simpler and therefore more readable, and can often run faster, enabling us to "
                 "carry out systematic parameter exploration. I will illustrate these points with a reduced model of "
                 "chopper cells in the ventral cochlear nucleus.",
    ),
    ############################### 2016 ###########################################################
   Publication(
       name='spikesorting', selected=True,
       year=2016,
       authors=('Rossant C, Kadir SN, Goodman DFM, Schulman J, Hunter MLD, Saleem AB, Grosmark A, Belluscio M, '
                'Denfield GH, Ecker AS, Tolias AS, Solomon S, Buzsáki G, Carandini M, Harris KD'),
       title='Spike sorting for large, dense electrode arrays',
       journal='Nature Neuroscience',
       doi='10.1038/nn.4268',
       categories=['Spike sorting', 'Machine learning'],
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
        name='model_initiative_asa2016',  # selected=True,
        year=2016,  # set year to 'Preprints' if not published yet
        authors='Dietz M, Marquardt T, Majdak P, Stern RM, Hartmann WM, Goodman DF, Ewert SD',
        title='A framework for auditory model comparability and applicability',
        conference='Acoustical Society of America',
        # for a conference paper (use short name here, and long name under additional_detail)
        additional='',  # goes after Journal (Year)
        doi='10.1121/1.4970386',  # linked to on detail page only
        additional_detail='Acoustical Society of America meeting 2016',  # only shown on detail page
        categories=['Auditory', 'Modelling', 'Neuroinformatics'],
        urls=[('Conference', 'https://asa.scitation.org/doi/abs/10.1121/1.4970386'),
              ],
        abstract="Many computational models of the auditory system exist, most of which can predict a variety of "
                 "psychoacoustical, physiological, or other experimental data. However, it is often challenging to "
                 "apply existing third party models to own experimental paradigms, even if the model code is "
                 "available. It will be demonstrated that model applicability is increased by providing a framework "
                 "where the model acts as artificial observer performing exactly the same task as the subject (e.g., "
                 "adaptive staircase procedure). A possible separation of the actual auditory processing of the "
                 "model from the decision making stage will be discussed, which allows for testing the auditory "
                 "processing of one model in a variety of experimental paradigms. The framework will consist of a "
                 "citable data repository providing the required data for the models as well as toolboxes "
                 "implementing both the auditory models and a variety of experimental paradigms. The model framework "
                 "will be demonstrated with exemplary binaural models applied to the three most common binaural "
                 "psychoacoustic paradigms: just noticeable difference (e.g., interaural time difference), "
                 "tone in noise detection (e.g., binaural masking level difference), and absolute judgment (e.g., "
                 "sound source localization). Further development of the framework will be discussed.",
    ),
############################### 2015 ###########################################################
    Publication(
        name='downstream_cns2015',  # selected=True,
        year=2015,  # set year to 'Preprints' if not published yet
        authors='Goodman DFM, de Cheveigné A, Winter IM, Lorenzi C',
        title='Downstream changes in firing regularity following damage to the early auditory system',
        conference='Computational Neuroscience',
        # for a conference paper (use short name here, and long name under additional_detail)
        additional='',  # goes after Journal (Year)
        doi='10.1186/1471-2202-16-S1-O11',  # linked to on detail page only
        additional_detail='24th Annual Computational Neuroscience Meeting: CNS*2015',  # only shown on detail page
        categories=['Auditory', 'Modelling'],
        urls=[('Conference', 'https://bmcneurosci.biomedcentral.com/articles/10.1186/1471-2202-16-S1-O11'),
              ],
        abstract='''<p>We demonstrate how an abstract mathematical model that approximates a wide range of more 
        detailed models can be used to make predictions about hearing loss-related changes in neural behaviour.</p> 

        <p>One consequence of neurosensory hearing loss (noise-induced and aging-related) is a reduced ability to 
        understand speech, particularly in noisy environments, and sometimes beyond what would be predicted from 
        reduced audibility. Indeed, this type of speech deficit can occur in listeners with near-normal hearing 
        thresholds [1]. A promising avenue of investigation to explain this comes from experimental results in mice 
        showing that there can be a permanent loss of auditory nerve fibres (ANFs) following "temporary" 
        noise-induced hearing loss (i.e. when thresholds return to normal after a few weeks) [2]. The downstream 
        consequences of this loss of fibres has not yet been systematically investigated (although see [3]). We 
        predict, using a theoretical analysis that applies to a wide range of neural models, that the regularity of 
        the spike trains of many neurons in the cochlear nucleus (the next structure after the auditory nerve) will 
        decrease following a reduction in the number of input cells. </p>

        <p>We present a mathematical analysis of the stationary behaviour of "chopper" cells in the ventral cochlear 
        nucleus, approximating them by a stochastic process that is entirely characterised by its mean, 
        standard deviation and time constants. Furthermore, these constants can be straightforwardly related to 
        physiologically significant parameters including the number of inputs and their average firing rates. From 
        this approximation, we can compute the regularity of the chopper cell spike trains measured as the 
        coefficient of variation of their interspike intervals (CV). </p>

        <p>One simple prediction of this model is that when the intensity of a stimulus changes, leading to a change in 
        the average firing rate of the ANF inputs, there will be a corresponding change in the regularity of the 
        chopper cell spike train. This prediction poses problems for the widely used scheme for classifying chopper 
        cells as sustained or transient based on their ongoing CVs as it implies that the classification could be 
        level-dependent. We present a re-analysis of an existing experimental data set that demonstrates that ongoing 
        CV is indeed level-dependent in the majority of chopper cells, and that in some cells (>7%) this leads to a 
        level-dependence in their classification. </p>

        <p>Assuming a homeostatic regulation of long term firing rates, a loss of ANFs will lead to an increase in the 
        standard deviation of the stochastic process and a consequent increase in the CV of the chopper cell. Some 
        choppers that were previously classified as sustained will become transient, a substantial change in their 
        behaviour that is highly likely to disrupt auditory processing. While the function of chopper cells is still 
        debated, one suggested role is in the coding of temporal envelope [4], which is widely agreed to be essential 
        for understanding speech. Loss of ANFs could therefore lead to a disruption of the processing of temporal 
        envelope, and consequently degrade speech intelligibility. We briefly conclude by discussing the challenges 
        of testing this hypothesis experimentally.</p>''',
    ),
############################### 2014 ###########################################################
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
        categories=['Spike sorting', 'Machine learning'],
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
############################### 2013 ###########################################################
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
        categories=['Sound localisation', 'Modelling', 'Machine learning'],
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
############################### 2012 ###########################################################
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
############################### 2011 ###########################################################
    Publication(
        name='rat_barrel_cortex',
        year=2011,
        authors='Kremer Y, Léger J-F, Goodman D, Brette R, Bourdieu L',
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
############################### 2010 ###########################################################
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
        name='spike_timing_sound_loc',# selected=True,
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
        urls=[('Journal', 'https://link.springer.com/article/10.1007/s12021-010-9082-x'),
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
############################### 2009 ###########################################################
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
        peer_reviewed=False,
        ),
############################### 2008 ###########################################################
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
############################### 2007 ###########################################################
############################### 2006 ###########################################################
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

