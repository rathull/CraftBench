<template>
    <section class="page">
        <div class="hero hero1">
            <!-- <div class="video">
                <iframe src="https://www.youtube.com/embed/tgbNymZ7vqY?autoplay=1&mute=1&loop=1">
                </iframe>
            </div> -->

            <div class="hero-body top-header columns">
                <div
                    class="column has-text-right"
                    style="display: flex; flex-direction: column; justify-content: center;"
                >
                    <h1 class="title is-1">
                        Craftbench
                    </h1>
                    <div class="subtitle">
                        Motivation, Teamwork, Management, Projects Made Simple
                    </div>
                </div>
                <div class="left-image column">
                    <img src="@/assets/images/add-files.svg">
                </div>

            </div>
        </div>

        <div class="hero hero2">
            <div class="hero-body">
                <h1 class="title is-2"> Gamified Experience</h1>
                <div class="paragraph2">
                    <p class="feature-1"> Craftbench turns working on projects into a fun motivating game. <br>Users can team up and work to defeat an enemy, by submitting projects!</p>
                </div>
            </div>
        </div>

        <div class="hero hero3">
            <div class="hero-body">
                <h1 class="title is-2">Manage Projects</h1>
                <div class="paragraph3">
                    <p class="feature-2"> Easy, intuitive, clear, efficient workspace. <br> Manage your upcoming submissions with a very fun UI experience. </p>
                </div>
            </div>
        </div>

        <div class="has-text-centered cards">
            <div class="columns benefit-cards">
                <div class="column">
                    <div>
                        <h2 class="subtitle">Private</h2>
                        <h1 class="title">Workspaces</h1>
                        <br />
                        <p>Private workspaces based on region and code.</p>
                        <img class="cover-image" />
                    </div>
                </div>

                <div class="column">
                    <div>
                        <h2 class="subtitle">Projects</h2>
                        <h1 class="title">Gamified</h1>
                        <br />
                        <p>Submit different leveled projects to defeat an evil opponent.</p>
                        <img class="cover-image" />
                    </div>
                </div>

                <div class="column">
                    <div>
                        <h2 class="subtitle">Store</h2>
                        <h1 class="title">Notes</h1>
                        <br />
                        <p>Take notes for different topics and projects, and then view them later.</p>
                        <img class="cover-image" />
                    </div>
                </div>
            </div>

            <div class="columns benefit-cards">
                <div class="column">
                    <div>
                        <h2 class="subtitle">Set up a</h2>
                        <h1 class="title">Timeline</h1>
                        <br />
                        <p>Plan out a detailed timeline for your project.</p>
                        <img class="cover-image" />
                    </div>
                </div>

                <div class="column">
                    <div>
                        <h2 class="subtitle">Gain</h2>
                        <h1 class="title">Rewards</h1>
                        <br />
                        <p>
                            Gain different rewards, powerups, and cool perks when submitting projects.
                        </p>
                        <img class="cover-image" />
                    </div>
                </div>

                <div class="column">
                    <div>
                        <h2 class="subtitle">Easy to</h2>
                        <h1 class="title">Submit</h1>
                        <br />
                        <p class>Submit notes, projects, and other tasks to your teacher, boss, etc., all with ease.</p>
                        <img class="cover-image" />
                    </div>
                </div>
            </div>
        </div>

    </section>
</template>

<style scoped>
.top-header {
    text-align: center;
}

.hero1 {
    background-color: var(--primary);
    height: 30rem;
    text-align: left;
}

.hero2 {
    background-color: var(--light);
    height: 20rem;
    text-align: left;
}

.hero3 {
    background-color: var(--primary);
    height: 20rem;
    text-align: right;
}

.paragraph2 {
    text-align: left;
}

.paragraph3 {
    text-align: right;
}

.top-header {
    text-align: center;
}

.cards {
    background-color: var(--dark);
    color: white;
    padding: 2rem;
}

.benefit-cards * {
    color: var(--light) !important;
}

.left-image img {
    animation: image-in 1s linear;
    height: 20rem;
}

@keyframes image-in {
    from {
        opacity: 0;
        transform: translateX(200%);
    }

    to {
        opacity: 1;
        transform: none;
    }
}

.video {
    background-size: cover;
}

.feature-1 {
    font-size: 25px;
}

.feature-2 {
    font-size: 25px;
}
</style>