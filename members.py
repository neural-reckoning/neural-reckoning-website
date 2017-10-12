# -*- coding: utf-8 -*-
class Member(object):
    def __init__(self, **args):
        for k, v in args.items():
            setattr(self, k, v)


# Positions: 1_pi, 2_postdoc, 3_phd, 4_other, 5_former

member_types = {'1_pi': '',
                '2_postdoc': 'Postdocs',
                '3_phd': 'PhD students',
                '4_other': 'Others',
                '5_former': 'Former members',
                }

members = [
    Member(
        id='dan_goodman',
        name='Dan Goodman',
        author_names=['Goodman DFM', 'Goodman D', 'Goodman DF'],
        position='1_pi',
        associate=False,
        show_publications=True,
        address='''
        Room 1001
        Department of Electrical and Electronic Engineering
        Imperial College
        Exhibition Road
        London SW7 2AZ
        ''',
        # generate this by import base64; base64.b64encode('address')
        email='ZC5nb29kbWFuQGltcGVyaWFsLmFjLnVr',
        telephone='+44 (0)20 7594 6264',
        social_media='''<a href="https://twitter.com/thesamovar">@thesamovar</a>
                        <a href="https://twitter.com/neuralreckoning">@neuralreckoning</a>''',
        short='''
        Head of lab.
        ''',
        long='''
        I am a lecturer in the
        <a href="http://www3.imperial.ac.uk/intellisysnetworks">Intelligent
        Systems and Networks group</a> in the
        <a href="http://www3.imperial.ac.uk/electricalengineering">Department
        of Electrical and Electronic Engineering</a> at
        <a href="http://www3.imperial.ac.uk/">Imperial College London</a>.

        <h2>Research interests</h2>

        <p>
        The aim of my research is to uncover the principles underlying neural
        computation with precisely timed spikes. This is a form of computation
        specific to the brain, being radically different to both digital and
        analogue computation. I have developed several
        <a href="software.html">software tools</a> for
        working with spiking neurons, notably the
        <a href="http://briansimulator.org">&quot;Brian&quot; spiking neural
        network simulator</a>. My focus is on sensory processing of complex,
        realistic stimuli, primarily in the auditory system.
        </p>
        ''',
    ),
    ############# PHD STUDENTS ################################
    # Alphabetical order
    Member(
        id='isaac_engel',
        name='Isaac Engel',
        author_names=['Engel I'],
        position='3_phd',
        associate=False,
        show_publications=True,
        # generate this by import base64; base64.b64encode('address')
        email='aXNhYWMuZW5nZWxAaW1wZXJpYWwuYWMudWs=',
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
    ),
    Member(
        id='pamela_hathway',
        name='Pamela Hathway',
        author_names=['Hathway P'],
        position='3_phd',
        associate=False,
        show_publications=True,
        # generate this by import base64; base64.b64encode('address')
        email='cC5oYXRod2F5MTZAaW1wZXJpYWwuYWMudWs=',
        short='''
        Large scale neural data analysis.
        ''',
        long='''
        <p>
        Pamela Hathway is a PhD student working on the problem of large
        scale neural data analysis. With new techniques to record from
        huge numbers of neurons simultaneously, we need new methods to
        make sense of this data.
        </p>
        ''',
    ),
    Member(
        id='jean_hugues_lestang',
        name='Jean-Hugues Lestang',
        author_names=['Lestang JH', 'Lestang J', 'Lestang J-H'],
        position='3_phd',
        associate=False,
        show_publications=True,
        # generate this by import base64; base64.b64encode('address')
        email='ai5sZXN0YW5nMTVAaW1wZXJpYWwuYWMudWs=',
        short='''
        Auditory neuroscience: sound localisation, neural adaptation.
        ''',
        long='''
        <p>
        Jean-Hugues Lestang is a PhD student, looking at the role of neural adaptation
        in sound localisation in realistic acoustic environments.
        </p>
        <p>
        Jean is also the Python developer for the
        <a href="https://github.com/model-initiative/model_initiative">Auditory Model Initiative</a>.
        </p>
        ''',
    ),
    Member(
        id='lotte_weerts',
        name='Lotte Weerts',
        author_names=['Weerts L'],
        position='3_phd',
        associate=False,
        show_publications=True,
        social_media='''<a href="http://lotteweerts.com/">lotteweerts.com</a>''',
        # generate this by import base64; base64.b64encode('address')
        email='bG90dGUud2VlcnRzMTVAaW1wZXJpYWwuYWMudWs=',
        short='''
        Auditory neuroscience: plasticity across multiple timescales
        ''',
        long='''
        <p>
        Lotte Weerts is a PhD student in the
        <a href="http://www.imperial.ac.uk/neurotechnology/cdt/">Neurotechnology CDT</a>,
        working on how the brain learns to cope with different auditory
        environments. She is jointly supervised by
        <a href="http://www.bg.ic.ac.uk/research/c.clopath/members/claudia_clopath/">Claudia Clopath</a>.
        </p>
        ''',
    ),
    Member(
        id='chu_yang',
        name='Yang Chu',
        author_names=['Chu Y'],
        position='3_phd',
        associate=False,
        show_publications=True,
        # generate this by import base64; base64.b64encode('address')
        email='eS5jaHUxNkBpbXBlcmlhbC5hYy51aw==',
        short='''
        Principles of neural computation and simulation techniques
        ''',
        long='''
        <p>
        Yang Chu is a PhD student, working on principles of neural computation,
        and high performance implementations using spiking neural
        network (in particular, using non-standard computational
        hardware such as FPGAs). He is jointly supervised by
        <a href="http://www.imperial.ac.uk/people/w.luk">Wayne Luk</a>.
        </p>
        ''',
    ),
    Member(
        id='jonathan_zheng',
        name='Jonathan Zheng',
        author_names=['Zheng J'],
        position='3_phd',
        associate=False,
        show_publications=True,
        # generate this by import base64; base64.b64encode('address')
        email='am9uYXRoYW4uemhlbmcxMkBpbXBlcmlhbC5hYy51aw==',
        short='''
        Interactive systems for ecosystems and neuroscience
        ''',
        long='''
        <p>
        Jonathan Zheng is a PhD student, working on interactive systems for
        visualising the behaviour of ecosystems and neural networks. He is
        jointly supervised by
        <a href="http://www.imperial.ac.uk/people/s.pawar">Samraat Pawar</a>.
        You can see an early prototype of our work in ecosystems at the
        <a href="http://ecobuildergame.org/">EcoBuilder</a> website.
        </p>
        ''',
    ),

]
