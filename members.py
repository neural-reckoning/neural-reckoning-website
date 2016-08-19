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
        show_publications=False,
        address='''
        Room 1001
        Electrical Engineering
        South Kensington Campus 
        ''',
        # generate this by import base64; base64.b64encode('address')
        email='ZC5nb29kbWFuQGltcGVyaWFsLmFjLnVr',
        telephone='+44 (0)20 7594 6264',
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
        <p>His Imperial webpage is <a href="http://www.ee.ic.ac.uk/electricalengineering/eepeople/person.asp?f=rg&c=ISN&s=NIL&id=30033">here</a>.
        ''',
        ),

    ]
