# -*- coding: utf-8 -*-
class Member(object):
    def __init__(self, **args):
        for k, v in list(args.items()):
            setattr(self, k, v)
    @property
    def dates_string(self):
        if len(self.dates)==1:
            return str(self.dates[0])+'-'
        else:
            return '-'.join(map(str, self.dates))


# Positions: 1_pi, 2_postdoc, 3_phd, 4_other, 5_former

member_types = {'1_pi': '',
                '2_postdoc': 'Postdocs and Fellows',
                '3_phd': 'PhD students',
                '4_other': 'Others',
                '5_former': 'Former members',
                }

def sk_address(room):
    return '''
    Room {room}
    Department of Electrical and Electronic Engineering
    Imperial College
    Exhibition Road
    London SW7 2AZ
    '''.format(room=room)

members = [
    Member(
        id='dan_goodman',
        name='Dan Goodman',
        author_names=['Goodman DFM', 'Goodman DF', 'Goodman D'],
        position='1_pi',
        associate=False,
        show_publications=True,
        address=sk_address(1001),
        # generate this by import base64; base64.b64encode('address')
        email='ZC5nb29kbWFuQGltcGVyaWFsLmFjLnVr',
        telephone='+44 (0)20 7594 6264',
        social_media='''
            <p>
                <a href="https://twitter.com/neuralreckoning">@neuralreckoning</a><br/>
                <a href="https://scholar.google.com/citations?user=2HiNqI4AAAAJ">Google Scholar</a>
            </p>
            ''',
        twitter='neuralreckoning',
        short='''
        Head of lab.
        ''',
        long='''
        <p>
        I am a (senior) lecturer (US equivalent: associate professor) in the
        <a href="http://www3.imperial.ac.uk/intellisysnetworks">Intelligent
        Systems and Networks group</a> in the
        <a href="http://www3.imperial.ac.uk/electricalengineering">Department
        of Electrical and Electronic Engineering</a> at
        <a href="http://www3.imperial.ac.uk/">Imperial College London</a>.</p>

        <p>
            The aim of my research is to uncover the principles underlying
            neural computation. My approach is to look at tasks that are
            complex and difficult enough to require a brain to solve them,
            but simple enough to be tractable. This includes things like
            understanding how we
            <a href="publication_category_soundlocalisation.html">localise
            sounds</a>, make sense of speech in noisy backgrounds, etc. I am
            particularly interested in neural computations with precisely
            timed spiking neural networks. This is a form of computation
            specific to the brain, being radically different to both digital and
            analogue computation.
        </p>
        
        <p>
            I have developed several
            <a href="software.html">software tools</a> for
            working with spiking neurons, notably the
            <a href="http://briansimulator.org">&quot;Brian&quot; spiking neural
            network simulator</a>.
        </p>

        <p>
            I am also interested in open science and making science better.
            I host a list of <a href="comp-neuro-resources.html">freely
            available computational neuroscience resources</a>. I co-founded
            <a href="https://neuromatch.io">Neuromatch</a> with
            <a href="http://kordinglab.com/">Konrad Kording</a>. I'm an editor
            for the open access journals
            <a href="https://elifesciences.org">eLife</a>, 
            <a href="https://nbdt.scholasticahq.com/">Neurons, Behavior, Data analysis, and Theory</a>, and
            <a href="https://cneuro.peercommunityin.org/">PCI Circuit Neuroscience</a>.
        </p>

        <p>
            A few people may also be interested in my
            <a href="mathematics.html">former career as a mathematician</a>.
        </p>
        ''',
    ),
    ############# POSTDOCS AND FELLOWS ################################
    # Alphabetical order
    Member(
        id='marcus_ghosh',
        name='Marcus Ghosh',
        author_names=['Ghosh M'],
        position='2_postdoc',
        dates=[2021],
        associate=False,
        show_publications=True,
        address=sk_address(1008),
        # generate this by import base64; base64.b64encode('address')
        #email='',
        short='''
        Multisensory integration in biological and simulated neural networks
        ''',
        long='''
        <p>
            Marcus Ghosh is a Research Fellow funded by the <a href="https://parisregion.eu/parisregionfp.html">Paris Region Fellowship Programme</a>. He works on spiking neural network models of multisensory integration in larval zebrafish. He carries out corresponding experimental work in the group of <a href="http://www.paris-neuroscience.fr/en/volker-bormuth">Volker Bormuth</a>.
        </p>
        ''',
        social_media='''
            <p>
                <a href="https://twitter.com/marcusghosh">@MarcusGhosh</a><br/>
                <a href="https://scholar.google.com/citations?user=__03svoAAAAJ&hl=en">Google Scholar</a><br/>
                <a href="https://orcid.org/0000-0002-2428-4605">ORCID</a>
            </p>
            ''',
        twitter='MarcusGhosh',
        orcid='0000-0002-2428-4605',
    ),
    ############# PHD STUDENTS ################################
    # Alphabetical order
    Member(
        id='gabriel_bena',
        name='Gabriel Béna',
        author_names=['Béna G'],
        position='3_phd',
        dates=[2021],
        associate=False,
        show_publications=True,
        address=sk_address(1008),
        # generate this by import base64; base64.b64encode('address')
        #email='',
        semantic_scholar=2107033449,
        short='''
        Machine learning and neuroscience
        ''',
        long='''
        <p>
        Gabriel Béna will work on machine learning and neuroscience, with a particular interest
        in spiking neural networks.
        </p>
        ''',
    ),
    Member(
        id='isaac_engel',
        name='Isaac Engel',
        author_names=['Engel I'],
        position='3_phd',
        dates=[2016],
        associate=False,
        show_publications=True,
        # generate this by import base64; base64.b64encode('address')
        email='aXNhYWMuZW5nZWxAaW1wZXJpYWwuYWMudWs=',
        semantic_scholar=2051731561,
        short='''
        Auditory augmented reality
        ''',
        long='''
        <p>
        Isaac Engel is a PhD student working on Auditory Augmented Reality
        (AAR) and spatial hearing. He is supervised by
        <a href="http://www.imperial.ac.uk/people/l.picinali">Lorenzo Picinali</a>
        and <a href="dan_goodman.html">Dan Goodman</a>.
        </p>
        ''',
        social_media='''
            <ul class="list-unstyled">
                <li><a href="https://www.imperial.ac.uk/people/isaac.engel">Imperial College website</a></li>
            </ul>
        '''
    ),
    Member(
        id='pamela_hathway',
        name='Pamela Hathway',
        author_names=['Hathway P'],
        position='5_former',
        former_position='PhD',
        dates=[2016, 2020],
        associate=False,
        show_publications=True,
        #address=sk_address(1008),
        # generate this by import base64; base64.b64encode('address')
        #email='cC5oYXRod2F5MTZAaW1wZXJpYWwuYWMudWs=',
        semantic_scholar=8781017,
        short='''
        Large scale neural data analysis.
        ''',
        long='''
        <p>
        Pamela Hathway was a PhD student working on the problem of large
        scale neural data analysis, primarily on Neuropixels data. She
        developed a new technique called "neural topic modelling",
        adapting topic modelling methods from machine learning originally
        designed for finding topics in sets of text documents automatically.
        </p>
        ''',
    ),
    Member(
        id='jean_hugues_lestang',
        name='Jean-Hugues Lestang',
        author_names=['Lestang JH', 'Lestang J-H', 'Lestang J'],
        position='5_former',
        former_position='PhD',
        dates=[2015, 2019],
        associate=False,
        show_publications=True,
        #address=sk_address(1008),
        # generate this by import base64; base64.b64encode('address')
        #email='ai5sZXN0YW5nMTVAaW1wZXJpYWwuYWMudWs=',
        semantic_scholar=30444266,
        social_media='''
            <ul class="list-unstyled">
                <li><a href="https://scholar.google.com/citations?user=j9wUAigAAAAJ&hl=en">Google Scholar</a></li>
                <li><a href="https://uk.linkedin.com/in/jean-hugues-lestang-90b70073">LinkedIn</a></li>
                <li><a href="https://github.com/jylls">GitHub</a></li>
            </ul>
            ''',
        short='''
        Auditory neuroscience: sound localisation, neural adaptation.
        ''',
        long='''
        <p>
            Jean-Hugues Lestang was a PhD student, looking at the role of neural adaptation
            in sound localisation in realistic acoustic environments.
        </p>
        <p>
            Jean is also the Python developer for the
            <a href="https://github.com/model-initiative/model_initiative">Auditory Model Initiative</a>.
        </p>
        ''',
    ),
    Member(
        id='nicolas_perez',
        name='Nicolas Perez',
        author_names=['Perez N', 'Perez-Nieves N'],
        position='3_phd',
        dates=[2018],
        associate=False,
        show_publications=True,
        address=sk_address(1008),
        # generate this by import base64; base64.b64encode('address')
        email='bmljb2xhcy5wZXJlejE0QGltcGVyaWFsLmFjLnVr',
        semantic_scholar=1999879303,
        short='''
        Multiresolution processing with heterogeneous spiking neural networks
        ''',
        long='''
        <p>
        Nicolas Perez is a PhD student working on understanding how
        spiking neural networks can use heterogeneous neuron properties
        to carry out multiresolution processing of sensory data.
        </p>
        ''',
    ),
    Member(
        id='lotte_weerts',
        name='Lotte Weerts',
        author_names=['Weerts L'],
        position='3_phd',
        dates=[2016],
        associate=False,
        show_publications=True,
        address=sk_address(1008),
        social_media='''<a href="http://lotteweerts.com/">lotteweerts.com</a>''',
        # generate this by import base64; base64.b64encode('address')
        email='bG90dGUud2VlcnRzMTVAaW1wZXJpYWwuYWMudWs=',
        short='''
        Auditory neuroscience, information theory and machine learning
        ''',
        long='''
        <p>
        Lotte Weerts is a PhD student in the
        <a href="http://www.imperial.ac.uk/neurotechnology/cdt/">Neurotechnology CDT</a>,
        working on a combined information theory and machine learning approach to
        understanding the auditory system. She is jointly supervised by
        <a href="http://www.bg.ic.ac.uk/research/c.clopath/members/claudia_clopath/">Claudia Clopath</a>.
        </p>
        ''',
    ),
    Member(
        id='chu_yang',
        name='Yang Chu',
        author_names=['Chu Y'],
        position='3_phd',
        dates=[2016],
        associate=False,
        show_publications=True,
        address=sk_address(1008),
        # generate this by import base64; base64.b64encode('address')
        email='eS5jaHUxNkBpbXBlcmlhbC5hYy51aw==',
        semantic_scholar=2070014411,
        short='''
        Principles of neural computation and simulation techniques
        ''',
        long='''
        <p>
        Yang Chu is a PhD student, working on principles of neural computation,
        and high performance implementations using spiking neural
        network (in particular, using non-standard computational
        hardware such as FPGAs). He is jointly supervised by
        <a href="http://www.imperial.ac.uk/people/w.luk">Wayne Luk</a> and
        <a href="https://tbrx.github.io/">Brooks Paige</a>.
        </p>
        ''',
    ),
    Member(
        id='jonathan_zheng',
        name='Jonathan Zheng',
        author_names=['Zheng JX', 'Zheng J'],
        position='5_former',
        former_position='PhD',
        dates=[2016, 2020],
        associate=False,
        show_publications=True,
        #address=sk_address(1008),
        # generate this by import base64; base64.b64encode('address')
        #email='am9uYXRoYW4uemhlbmcxMkBpbXBlcmlhbC5hYy51aw==',
        semantic_scholar=27620389,
        short='''
        Interactive systems for ecosystems and neuroscience.
        ''',
        social_media='''
            <ul class="list-unstyled">
                <li><a href="https://scholar.google.co.uk/citations?user=rwiyjioAAAAJ&hl=en&oi=sra">Google Scholar</a></li>
                <li><a href="https://github.com/jxz12">GitHub</a></li>
                <li><a href="https://twitter.com/terracotta_jz">Twitter</a></li>
            </ul>
            ''',
        long='''
        <p>
        Jonathan Zheng was a PhD student, working on interactive systems for
        visualising the behaviour of ecosystems and neural networks. He was
        jointly supervised by
        <a href="http://www.imperial.ac.uk/people/s.pawar">Samraat Pawar</a>.
        You can download the ecosystems game he designed at the
        <a href="http://ecobuildergame.org/">EcoBuilder</a> website.
        </p>
        ''',
    ),
    Member(
        id='tom_clegg',
        name='Tom Clegg',
        author_names=['Clegg T'],
        position='3_phd',
        dates=[2017],
        associate=False,
        show_publications=True,
        # generate this by import base64; base64.b64encode('address')
        #email='dC5jbGVnZzE3QGltcGVyaWFsLmFjLnVr',
        semantic_scholar=48055309,
        short='''
        Effects of temperature on the structure and dynamics of ecological networks
        ''',
        long='''
        <p>
        Tom Clegg is a PhD student, supervised by
        <a href="http://www.imperial.ac.uk/people/s.pawar">Samraat Pawar</a>,
        <a href="https://www.imperial.ac.uk/people/guy.woodward">Guy Woodward</a> and
        <a href="dan_goodman.html">Dan Goodman</a>.
        He studies the effects of temperature on the structure and dynamics of ecological networks and how this affects
        their function (i.e. their ability to convert nutrients to biomass). He uses a combination of theoretical models
        and empirical data collected from stream ecosystems across the globe.
        </p>
        ''',
    ),

]
