import gsap from "gsap";
import { ScrollTrigger } from "gsap/ScrollTrigger";

gsap.registerPlugin(ScrollTrigger);

// Reveal animation for sections
export const animateSectionReveal = (element: HTMLElement) => {
    gsap.fromTo(
        element,
        { opacity: 0, y: 50 },
        {
            opacity: 1,
            y: 0,
            duration: 1,
            ease: "power3.out",
            scrollTrigger: {
                trigger: element,
                start: "top 80%",
                toggleActions: "play none none reverse",
            },
        }
    );
};

// Background color transition
export const setupColorTransitions = (
    triggerElement: HTMLElement,
    targetElement: HTMLElement,
    color: string
) => {
    ScrollTrigger.create({
        trigger: triggerElement,
        start: "top center",
        end: "bottom center",
        onEnter: () => gsap.to(targetElement, { backgroundColor: color, duration: 0.5 }),
        onLeaveBack: () =>
            gsap.to(targetElement, { backgroundColor: "var(--color-background)", duration: 0.5 }), // Revert to default
    });
};

// Staggered reveal for children
export const animateStaggeredChildren = (
    parentElement: HTMLElement,
    childSelector: string,
    staggerAmount = 0.1
) => {
    const children = parentElement.querySelectorAll(childSelector);

    gsap.fromTo(
        children,
        { opacity: 0, y: 20 },
        {
            opacity: 1,
            y: 0,
            duration: 0.8,
            stagger: staggerAmount,
            ease: "power2.out",
            scrollTrigger: {
                trigger: parentElement,
                start: "top 85%",
            },
        }
    );
};

// Depth Gauge Animation util
export const updateDepthGauge = (
    indicator: HTMLElement,
    containerHeight: number,
    maxDepth: number = 50
) => {
    ScrollTrigger.create({
        start: 0,
        end: "max",
        onUpdate: (self) => {
            const progress = self.progress;
            const currentDepth = Math.round(progress * maxDepth);
            // Update logic to be handled in the component, usually via a callback or store
        }
    });
};
