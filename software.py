class Software(object):
    def __init__(self, **args):
        for k, v in list(args.items()):
            setattr(self, k, v)

software = [
    # Software(
    #     name="",
    #     title="",
    #     url="",
    #     logo="",
    #     short="",
    #     long="""
    #     """,
    #     team=["Goodman DFM"],
    # ),
    Software(
        name="brian",
        title="Brian",
        url="http://briansimulator.org",
        logo="brian.png",
        short="A Python simulator for spiking neural networks.",
        long="""
        <p>
            A simulator for spiking neural networks. It is written in Python for rapid
            development and ease-of-use, and generates code in several different
            languages for a variety of computational devices for efficient
            execution (for example on GPU via the
            <a href="https://genn-team.github.io/genn/">GeNN</a> simulator using the
            <a href="http://brian2genn.readthedocs.io/en/latest/">Brian2GeNN</a> package).
            It includes packages for
            <a href="pub_modelfitting_focussed_review.html">automatically
            fitting neuron models to experimental data</a> and for
            <a href="pub_brian_hears.html">modelling the auditory system</a>.
        </p>
        <p>
            The core Brian team consists of
            <a href="dan_goodman.html">Dan Goodman</a> at Imperial, and
            <a href="http://romainbrette.fr/">Romain Brette</a> and
            <a href="http://scholar.google.co.uk/citations?user=KJs3XswAAAAJ&hl=en">Marcel Stimberg</a>
            at l'Institut de la Vision in Paris.
        </p>
        """,
        team=["Goodman DFM"],
    ),
    Software(
        name="klusta",
        title="KlustaSuite",
        url="http://klusta-team.github.io/",
        logo="spikedetekt.png",
        short="Spike sorting.",
        long="""
        <p>
            A collection of programs for "spike sorting". That is, for
            extracting spike trains from a set of simultaneously recorded
            extracellular traces. This problem involves preprocessing data to
            remove noise, clustering to identify patterns across channels
            that correspond to spikes, and finally manually inspecting and
            refining the output. This software is currently undergoing a
            massive redesign to make it possible to sort spikes using
            enormous electrode arrays with hundreds to thousands of channels.
        </p>
        <p>
            The KlustaSuite team is led by
            <a href="http://iris.ucl.ac.uk/iris/browse/profile?upi=KDHAR02">Kenneth Harris</a>
            at UCL.
        </p>
        """,
        team=["Goodman DFM"],
    ),
    Software(
        name="sgd2",
        title="s(gd)<sup>2</sup>",
        url="https://github.com/jxz12/s_gd2",
        logo="https://media.giphy.com/media/JoaboGdTq1sXNnnIND/giphy.gif",
        short="Graph layout using stochastic gradient descent.",
        long="""
        <p>
            A package for graph layout based on a stochastic gradient descent algorithm (available for C++ and Python).
            The package is described in the paper
            <a href="pub_graph_drawing_wcr.html">Graph Drawing by Stochastic Gradient Descent (Zheng et al. 2018)</a>
            and was written by <a href="jonathan_zheng.html">Jonny Zheng</a>.
        </p>
        """,
        team=["Goodman DFM", "Zheng J"],
    ),
    Software(
        name="ecobuilder",
        title="EcoBuilder",
        url="http://ecobuildergame.org",
        logo="ecobuilder.jpg",
        short="Educational game about building ecosystems.",
        long="""
        <p>
            A game for exploring the development and maintenance of ecosystems
            for both education and research purposes. The game was written by
            Jonathan Zheng, with ecosystems modelling by Orestes Gutierrez
            and <a href="http://www.imperial.ac.uk/people/s.pawar">Samraat Pawar</a>.
        </p>
        """,
        team=["Goodman DFM", "Zheng J"],
    ),
    Software(
        name="humanlike_hearing",
        title="HumanlikeHearing",
        url="https://github.com/neural-reckoning/HumanlikeHearing",
        logo="humanlike-hearing.png",
        short="Python package for psychophysical tests of automatic speech recognition systems.",
        long="""
            <p>
                A Python package for applying a range of psychometric tests on automatic speech recognition (ASR) systems.
                Accompanying <a href="pub_humanlikehearing.html">paper</a>.
                Developed by <a href="lotte_weerts.html">Lotte Weerts</a>.
            </p>
        """,
        team=["Goodman DFM", "Weerts L"],
    ),
    Software(
        name="auditory_model_initiative",
        title="Auditory Model Initiative",
        url="https://github.com/model-initiative/model_initiative",
        logo="model-initiative.png",
        short="Python/Matlab package for comparing binaural auditory models.",
        long="""
        <p>
            A set of Python and Matlab software packages for comparing
            auditory models. The package is still in an early stage of development.
            The initiative is led by
            <a href="http://www.uwo.ca/fhs/csd/people/faculty/dietz_m.html">Mathias Dietz</a>,
            with Python contributions from
            <a href="jean_hugues_lestang.html">Jean-Hugues Lestang</a>.
        </p>
        """,
        team=["Goodman DFM", "Lestang J-H"],
    ),
    Software(
        name="pconfluent",
        title="<tt>pconfluent</tt>: power confluent drawings",
        url="https://github.com/jxz12/pconfluent",
        logo="power-confluent.png",
        short="Package for power confluent graph drawings.",
        long="""
        <p>
            Software for power-confluent drawings, accompanying the paper
            <a href="pub_comments_on_edge_bundling.html">Further Towards Unambiguous Edge Bundling: Investigating
                Power-Confluent Drawings for Network Visualization (Zheng et al. 2019)</a>
            written by <a href="jonathan_zheng.html">Jonny Zheng</a>.
        </p>
        """,
        team=["Goodman DFM", "Zheng J"],
    ),
    Software(
        name="conference_timer",
        title="Conference Timer",
        url="conference-timer.html",
        logo="conference-timer-screenshot.png",
        short="HTML/JavaScript conference timer.",
        long="""
        <p>
            A handy little HTML/Javascript page that can be used as a timer at conferences or workshops.
            It gives you the option to set a length of time for the talk and for questions, and shows a visual
            display of the remaining time. Works with Firefox and some versions of Internet Explorer.
        </p>
        """,
        team=["Goodman DFM"],
    ),
]