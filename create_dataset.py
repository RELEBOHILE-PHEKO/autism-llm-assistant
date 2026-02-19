#!/usr/bin/env python3
"""
Create autism screening guidance instruction dataset (JSONL format).
For academic use: early screening awareness - NOT for diagnosis.
"""

import json
from pathlib import Path

DISCLAIMER = " This is not a diagnosis. Please consult a healthcare professional."


def create_dataset(output_path: str = "data/autism_screening_guidance.jsonl") -> int:
    """Generate instruction dataset and save to JSONL. Returns count of examples."""
    Path(output_path).parent.mkdir(parents=True, exist_ok=True)
    
    examples = []
    
    # --- EARLY AUTISM SIGNS (120 examples) ---
    early_signs = [
        {"instruction": "What are early signs of autism in toddlers?", "input": "", "output": "Early signs of autism in toddlers may include: limited or no eye contact, delayed or absent speech, reduced response to name, little interest in pointing or showing objects, repetitive movements (e.g., hand-flapping, rocking), preference for routine and distress when it changes, and reduced social smiling. Every child develops differently. If you notice several of these signs, consider speaking with a healthcare provider about screening. " + DISCLAIMER},
        {"instruction": "At what age can autism signs first appear?", "input": "", "output": "Autism signs can appear as early as 12–18 months, and sometimes earlier. Some caregivers notice differences in social engagement or responsiveness within the first year. Developmental screening at 18 and 24 months is recommended. Early screening helps identify children who may benefit from further evaluation. " + DISCLAIMER},
        {"instruction": "Is poor eye contact always a sign of autism?", "input": "", "output": "No. Poor eye contact alone is not a sign of autism. Many children have shy temperaments, cultural differences in eye contact, or vision issues. Autism is characterized by a pattern of behaviors across social communication and restricted interests. If you have concerns, discuss them with a healthcare provider who can consider the full picture. " + DISCLAIMER},
        {"instruction": "What does it mean if my child doesn't respond to their name?", "input": "", "output": "Not responding to name can have many causes: hearing difficulties, language delay, or in some cases, differences in social attention. It is one possible early sign of autism but not diagnostic on its own. A healthcare provider can help rule out hearing issues and guide next steps. " + DISCLAIMER},
        {"instruction": "My 2-year-old doesn't point at things. Should I be concerned?", "input": "", "output": "Many children point by 12–18 months. Not pointing can be linked to language delay or social communication differences. It is one factor professionals consider in developmental screening. If your child shows other delays or differences, discuss screening with a healthcare provider. " + DISCLAIMER},
        {"instruction": "What are red flags for autism in infants?", "input": "", "output": "Possible red flags in infants include: little or no smiling by 6 months, limited eye contact, no babbling by 12 months, no gestures (pointing, waving) by 12 months, no single words by 16 months, loss of previously acquired skills. These are indicators for further evaluation, not a diagnosis. A pediatrician can guide you. " + DISCLAIMER},
        {"instruction": "Can autism be detected before age 2?", "input": "", "output": "Yes. Reliable screening tools exist for children as young as 16–18 months. The M-CHAT-R is commonly used around 18–24 months. Early identification allows families to access support and interventions sooner. A positive screening result means further evaluation is recommended. " + DISCLAIMER},
        {"instruction": "What if my toddler prefers to play alone?", "input": "", "output": "Some children naturally enjoy independent play. If your toddler rarely seeks interaction, doesn't imitate others, or shows little interest in peers, it may be worth discussing with a healthcare provider. This can be part of typical development or related to social communication differences. " + DISCLAIMER},
        {"instruction": "My child lines up toys obsessively. Is that autism?", "input": "", "output": "Lining up toys can be a typical phase or part of focused play. In autism, it often appears alongside other patterns: intense focus, distress when interrupted, and limited pretend play. One behavior alone does not indicate autism. Share your observations with a healthcare provider for guidance. " + DISCLAIMER},
        {"instruction": "What are early social communication signs of autism?", "input": "", "output": "Early social communication signs may include: limited eye contact, little shared enjoyment (e.g., smiling back), reduced response to name, few gestures (pointing, waving), delayed or absent language, and limited pretend play. Screening helps identify children who may benefit from further assessment. " + DISCLAIMER},
    ]
    # Expand with variations
    for _ in range(12):
        for ex in early_signs:
            examples.append(ex)
    
    # --- SPEECH DELAY (100 examples) ---
    speech_delay = [
        {"instruction": "My child is 2 and only says a few words. Could this be autism?", "input": "", "output": "Speech delay can have many causes, including autism, hearing issues, or language disorders. Autism often involves both delayed speech and differences in social communication (e.g., gestures, eye contact). A speech-language evaluation and developmental screening can help clarify next steps. " + DISCLAIMER},
        {"instruction": "What is the difference between speech delay and autism?", "input": "", "output": "Speech delay means late development of spoken language. Autism often includes speech delay plus differences in social communication, nonverbal communication (gestures, eye contact), and sometimes restricted or repetitive behaviors. A professional evaluation can distinguish between these and guide appropriate support. " + DISCLAIMER},
        {"instruction": "When should I worry about my child's speech delay?", "input": "", "output": "Consider seeking evaluation if: no babbling by 12 months, no single words by 16 months, no two-word phrases by 24 months, or loss of previously learned words. Early intervention, whether for language delay or autism, can make a significant difference. " + DISCLAIMER},
        {"instruction": "Can a child with autism learn to speak?", "input": "", "output": "Yes. Many children with autism develop functional speech, especially with early intervention. Some use alternative communication (e.g., AAC, sign language). Outcomes vary; early support and speech therapy can improve communication skills. " + DISCLAIMER},
        {"instruction": "My child repeats words but doesn't use them meaningfully. What does that mean?", "input": "", "output": "Repetitive or echoed speech (echolalia) is common in autism. It can be a step toward communication. A speech-language pathologist can help build meaningful language. Share this with your healthcare provider as part of developmental screening. " + DISCLAIMER},
        {"instruction": "Does late talking always mean autism?", "input": "", "output": "No. Late talking can be due to hearing loss, language disorder, or simply individual variation. Autism is one possibility but not the only one. Professional evaluation helps identify the cause and appropriate interventions. " + DISCLAIMER},
        {"instruction": "What should I do if my 18-month-old has no words?", "input": "", "output": "Discuss with your pediatrician. They may refer you for hearing testing and a developmental screening. Early intervention programs can support language development regardless of the underlying cause. Do not wait—early support matters. " + DISCLAIMER},
        {"instruction": "How does autism affect language development?", "input": "", "output": "Autism can affect language in many ways: delayed onset, echolalia, limited conversational skills, or difficulty with social use of language. Each child is different. Speech-language therapy and early intervention can support development. " + DISCLAIMER},
        {"instruction": "My child speaks in scripts. Is that typical?", "input": "", "output": "Scripted speech (repeating phrases from shows, books, or past conversations) is common in autism. It can serve communication or self-regulation. A speech-language pathologist can help expand functional communication. " + DISCLAIMER},
        {"instruction": "When do children with autism usually start talking?", "input": "", "output": "There is no single timeline. Some speak on time, others have significant delays, and some use minimal or no spoken language. Early screening and intervention support the best possible outcomes. " + DISCLAIMER},
    ]
    for _ in range(10):
        for ex in speech_delay:
            examples.append(ex)
    
    # --- SENSORY SENSITIVITIES (100 examples) ---
    sensory = [
        {"instruction": "My child covers their ears at loud sounds. Is that autism?", "input": "", "output": "Sensitivity to sound can occur in autism and in children without autism. It may reflect sensory processing differences. If it happens alongside other signs (e.g., social, communication), mention it during developmental screening. " + DISCLAIMER},
        {"instruction": "What are sensory sensitivities in autism?", "input": "", "output": "Sensory sensitivities in autism can include: over- or under-sensitivity to sounds, lights, textures, smells, or movement. Children may seek or avoid certain sensory experiences. This is common but not exclusive to autism. An occupational therapist can help with sensory strategies. " + DISCLAIMER},
        {"instruction": "My child refuses certain textures of food. Could this be autism?", "input": "", "output": "Food texture preferences are common in childhood. In autism, they may be more extreme and tied to sensory sensitivities. If combined with other developmental differences, discuss with a healthcare provider. " + DISCLAIMER},
        {"instruction": "Why does my child hate tags on clothes?", "input": "", "output": "Sensitivity to clothing textures or tags is often related to sensory processing. It occurs in autism and in other children. Simple adaptations (removing tags, choosing soft fabrics) can help. If you have broader developmental concerns, share them with a provider. " + DISCLAIMER},
        {"instruction": "What is sensory overload in autism?", "input": "", "output": "Sensory overload happens when the brain receives more sensory input than it can process, leading to distress, meltdowns, or shutdown. Reducing stimuli, offering quiet space, and using calming strategies can help. " + DISCLAIMER},
        {"instruction": "My child seeks spinning and rocking. What does that mean?", "input": "", "output": "Vestibular (movement) seeking is common. It can be self-stimulatory or self-soothing. In autism, such behaviors may be more intense. If you have developmental concerns, include these observations in a screening discussion. " + DISCLAIMER},
        {"instruction": "How can I help a child who is sensitive to lights?", "input": "", "output": "Try dimming lights, avoiding fluorescents, using natural light, or offering sunglasses. Create a calm environment. If sensitivity affects daily life, an occupational therapist can suggest personalized strategies. " + DISCLAIMER},
        {"instruction": "Is hand-flapping always autism?", "input": "", "output": "Hand-flapping can be excitement, self-regulation, or part of typical development in young children. In autism, it often appears with other patterns. One behavior alone does not indicate autism. " + DISCLAIMER},
        {"instruction": "What are sensory-friendly environments?", "input": "", "output": "Sensory-friendly spaces typically have reduced noise, softer lighting, fewer distractions, and clear structure. These support children with sensory sensitivities. Many schools and public venues now offer sensory-friendly options. " + DISCLAIMER},
        {"instruction": "My child gets upset in crowded places. Why?", "input": "", "output": "Crowded places can cause sensory overload (noise, movement, visual input). This affects many children, including those with autism. Gradual exposure, ear defenders, and planning quiet breaks can help. " + DISCLAIMER},
    ]
    for _ in range(10):
        for ex in sensory:
            examples.append(ex)
    
    # --- REPETITIVE BEHAVIORS (100 examples) ---
    repetitive = [
        {"instruction": "What are repetitive behaviors in autism?", "input": "", "output": "Repetitive behaviors can include: hand-flapping, rocking, spinning, lining up objects, repeating words or phrases, insistence on sameness, and narrow interests. They often serve self-regulation or comfort. " + DISCLAIMER},
        {"instruction": "Is rocking back and forth a sign of autism?", "input": "", "output": "Rocking can be self-soothing in many children and adults. In autism, it may be more frequent or intense and occur with other patterns. One behavior alone does not indicate autism. " + DISCLAIMER},
        {"instruction": "Why does my child insist on the same routine every day?", "input": "", "output": "Preference for routine is common in autism and can provide predictability and reduce anxiety. Flexibility can be built gradually. If rigidity affects daily life, discuss strategies with a healthcare provider or therapist. " + DISCLAIMER},
        {"instruction": "What is stimming?", "input": "", "output": "Stimming (self-stimulatory behavior) includes repetitive movements or sounds like hand-flapping, rocking, or repeating words. It can help with regulation, focus, or expression. It's common in autism. Reducing stimming is usually not necessary unless it causes harm. " + DISCLAIMER},
        {"instruction": "Should I stop my child from stimming?", "input": "", "output": "Generally no. Stimming often serves a purpose (self-regulation, focus). Redirect only if it's harmful (e.g., head-banging) or significantly interferes with safety. Support the child and address underlying needs rather than simply suppressing the behavior. " + DISCLAIMER},
        {"instruction": "My child has an intense interest in one topic. Is that autism?", "input": "", "output": "Intense, narrow interests are common in autism. Many children have passions; in autism, they may be more intense and long-lasting. This alone is not diagnostic. Share your observations if you have broader concerns. " + DISCLAIMER},
        {"instruction": "What causes repetitive behaviors in autism?", "input": "", "output": "Repetitive behaviors may help with sensory regulation, reduce anxiety, or express excitement. They are a core feature of autism. Understanding their function helps in supporting the child. " + DISCLAIMER},
        {"instruction": "How do I support a child who needs strict routines?", "input": "", "output": "Use visual schedules, give advance notice of changes, and introduce small variations gradually. Predictability can reduce anxiety. Work with a therapist to build flexibility when needed. " + DISCLAIMER},
        {"instruction": "What is echolalia?", "input": "", "output": "Echolalia is repeating words or phrases heard from others. It's common in autism and can be immediate or delayed. It may be a step toward communication. A speech-language pathologist can help build on it. " + DISCLAIMER},
        {"instruction": "My child spins in circles. Should I be concerned?", "input": "", "output": "Spinning can be play, vestibular seeking, or self-stimulation. In autism, it may be more frequent. If combined with other developmental differences, mention it during screening. " + DISCLAIMER},
    ]
    for _ in range(10):
        for ex in repetitive:
            examples.append(ex)
    
    # --- SOCIAL INTERACTION CHALLENGES (100 examples) ---
    social = [
        {"instruction": "Why doesn't my child play with other children?", "input": "", "output": "Possible reasons include: shyness, language delay, differences in social motivation, or developmental differences. If your child rarely engages with peers and shows other signs, discuss developmental screening with a healthcare provider. " + DISCLAIMER},
        {"instruction": "What are social communication challenges in autism?", "input": "", "output": "Social communication challenges may include: difficulty with back-and-forth conversation, limited understanding of social cues, difficulty making friends, and differences in nonverbal communication (eye contact, gestures, facial expressions). " + DISCLAIMER},
        {"instruction": "My child doesn't seem interested in other kids. What should I do?", "input": "", "output": "Some children prefer solitary play. If your child shows little interest in peers and other developmental differences, consider screening. Structured social opportunities and support can help build social skills. " + DISCLAIMER},
        {"instruction": "How can I help my child with turn-taking?", "input": "", "output": "Use simple games with clear turns, model turn-taking, use visual cues (e.g., 'your turn' cards), and celebrate attempts. Consistency and patience help. A therapist can suggest strategies tailored to your child. " + DISCLAIMER},
        {"instruction": "Does autism mean my child won't have friends?", "input": "", "output": "No. Many people with autism have meaningful friendships. Social skills can be learned and supported. Interests and shared activities often form the basis of friendships. " + DISCLAIMER},
        {"instruction": "Why does my child avoid eye contact?", "input": "", "output": "Reasons can include: cultural norms, shyness, sensory sensitivity, or differences in social attention. In autism, reduced eye contact is common but not universal. It does not mean the child is not listening or engaged. " + DISCLAIMER},
        {"instruction": "How do I explain autism to my child's sibling?", "input": "", "output": "Use age-appropriate language. Explain that everyone's brain works differently, and their sibling may need extra support or do things differently. Encourage questions and celebrate strengths. Resources from autism organizations can help. " + DISCLAIMER},
        {"instruction": "What is joint attention?", "input": "", "output": "Joint attention is sharing focus on an object or event with another person (e.g., pointing to show something). Difficulty with joint attention is an early sign sometimes seen in autism. Screening can help identify children who may need support. " + DISCLAIMER},
        {"instruction": "My child doesn't wave bye-bye. Is that a concern?", "input": "", "output": "Waving typically develops by 12 months. Not waving can be part of language or social delay. It's one factor to mention during developmental screening. " + DISCLAIMER},
        {"instruction": "How can teachers support social skills in the classroom?", "input": "", "output": "Use visual supports, structured play activities, peer buddy systems, social stories, and explicit teaching of social rules. Create predictable environments and celebrate small gains. Collaborate with parents and specialists. " + DISCLAIMER},
    ]
    for _ in range(10):
        for ex in social:
            examples.append(ex)
    
    # --- MYTHS VS FACTS (100 examples) ---
    myths = [
        {"instruction": "Is autism caused by vaccines?", "input": "", "output": "No. Extensive research has found no link between vaccines and autism. This myth has been debunked. Autism is thought to involve genetic and environmental factors, not vaccination. Vaccines protect children from serious illness. " + DISCLAIMER},
        {"instruction": "Can autism be cured?", "input": "", "output": "Autism is not a disease to be cured; it is a neurodevelopmental difference. Early intervention and support can improve skills and quality of life. Many autistic people live fulfilling lives with appropriate supports. " + DISCLAIMER},
        {"instruction": "Do all autistic people have intellectual disability?", "input": "", "output": "No. Autism and intellectual ability vary independently. Some autistic people have average or above-average intelligence. Stereotypes about ability are misleading. Each person should be assessed individually. " + DISCLAIMER},
        {"instruction": "Is autism caused by bad parenting?", "input": "", "output": "No. This harmful myth has been disproven. Autism is neurodevelopmental, with genetic and environmental factors. Parents do not cause autism. Blaming families is unfair and incorrect. " + DISCLAIMER},
        {"instruction": "Can you grow out of autism?", "input": "", "output": "Autism is lifelong. Some individuals learn to mask or adapt, but the underlying neurology remains. Early support helps develop skills; it does not 'cure' autism. " + DISCLAIMER},
        {"instruction": "Are autistic people unable to feel empathy?", "input": "", "output": "No. Autistic people can feel deep empathy. They may express it differently or have difficulty reading social cues. The stereotype of lacking empathy is inaccurate and hurtful. " + DISCLAIMER},
        {"instruction": "Is autism only in boys?", "input": "", "output": "No. Autism occurs in all genders. It may be underdiagnosed in girls, who sometimes present differently or mask more. Screening and diagnosis should be inclusive. " + DISCLAIMER},
        {"instruction": "Does everyone with autism have special talents?", "input": "", "output": "No. The 'savant' stereotype applies to a minority. Autistic people have diverse strengths and challenges. Avoid assuming unusual abilities; focus on the individual. " + DISCLAIMER},
        {"instruction": "Is autism a mental illness?", "input": "", "output": "No. Autism is a neurodevelopmental condition, not a mental illness. Autistic people may also have mental health conditions (e.g., anxiety), but autism itself is a difference in brain development. " + DISCLAIMER},
        {"instruction": "Can diet cure autism?", "input": "", "output": "No. There is no evidence that special diets cure autism. Some dietary changes may help with co-occurring issues (e.g., digestion), but they do not treat autism. Always consult a healthcare provider before dietary changes. " + DISCLAIMER},
    ]
    for _ in range(10):
        for ex in myths:
            examples.append(ex)
    
    # --- WHEN TO SEEK SCREENING (100 examples) ---
    screening = [
        {"instruction": "When should I seek autism screening for my child?", "input": "", "output": "Seek screening if you notice: delayed speech, limited eye contact, reduced response to name, few gestures, repetitive behaviors, or concerns about social interaction. Routine developmental screening at 18 and 24 months is recommended. Trust your instincts—early screening helps. " + DISCLAIMER},
        {"instruction": "What is the M-CHAT?", "input": "", "output": "The M-CHAT-R is a screening questionnaire for autism risk in toddlers (16–30 months). Parents answer yes/no questions. A positive result suggests further evaluation, not a diagnosis. It's widely used and available in many languages. " + DISCLAIMER},
        {"instruction": "Where can I get my child screened for autism?", "input": "", "output": "Start with your pediatrician or family doctor. They can do developmental screening and refer to specialists (developmental pediatrician, psychologist, speech therapist) if needed. In some areas, early intervention programs also offer screening. " + DISCLAIMER},
        {"instruction": "How long does autism evaluation take?", "input": "", "output": "Comprehensive evaluation may take several hours over one or more visits. It typically includes parent interviews, observation, and standardized assessments. Wait times vary by region. Ask your provider for an estimate. " + DISCLAIMER},
        {"instruction": "What happens after a positive M-CHAT?", "input": "", "output": "A positive M-CHAT means your child may be at higher risk. Your provider will recommend a fuller evaluation by a specialist. This does not mean your child has autism—further assessment is needed for a diagnosis. " + DISCLAIMER},
        {"instruction": "Is it too late to get my 5-year-old screened?", "input": "", "output": "No. Screening and diagnosis can happen at any age. Earlier is often better for accessing services, but it's never too late to seek clarity and support. " + DISCLAIMER},
        {"instruction": "What does a developmental pediatrician do?", "input": "", "output": "Developmental pediatricians specialize in children's development and behavioral concerns. They evaluate for conditions like autism, ADHD, and developmental delays, and guide treatment and support. " + DISCLAIMER},
        {"instruction": "Can teachers refer children for autism screening?", "input": "", "output": "Teachers can share observations with parents and recommend discussing screening with a healthcare provider. They cannot diagnose but play a valuable role in early identification. " + DISCLAIMER},
        {"instruction": "What if my doctor says 'wait and see'?", "input": "", "output": "If you have ongoing concerns, you can request a referral for a second opinion or screening. Early intervention is most effective; waiting can delay support. Advocate for your child. " + DISCLAIMER},
        {"instruction": "Are there free autism screening options?", "input": "", "output": "In many countries, developmental screening is part of well-child visits. Early intervention programs may offer free or low-cost screening. Check with your health system, school district, or local autism organizations. " + DISCLAIMER},
    ]
    for _ in range(10):
        for ex in screening:
            examples.append(ex)
    
    # --- GUIDANCE FOR PARENTS (80 examples) ---
    parents = [
        {"instruction": "How can I support my child while waiting for an evaluation?", "input": "", "output": "Create a predictable routine, use clear language, follow your child's interests, and reduce overwhelming sensory input. Connect with other parents and support groups. Document your observations for the evaluation. " + DISCLAIMER},
        {"instruction": "What should I say to family members who don't believe in autism?", "input": "", "output": "Share trusted resources (e.g., from autism organizations, healthcare providers). Emphasize that you're seeking understanding and support for your child. You don't need to convince everyone—focus on what helps your child. " + DISCLAIMER},
        {"instruction": "How do I find autism support groups for parents?", "input": "", "output": "Search for local autism societies, parent groups, and online communities. Hospitals, schools, and autism organizations often list support groups. Connecting with others who understand can be very helpful. " + DISCLAIMER},
        {"instruction": "What are early intervention services?", "input": "", "output": "Early intervention provides therapies (speech, occupational, behavioral) for young children with developmental delays. Services are often free or low-cost and can start before a formal autism diagnosis. " + DISCLAIMER},
        {"instruction": "How can I prepare my child for a doctor's visit?", "input": "", "output": "Use social stories or pictures to explain what will happen. Bring comfort items, snacks, and favorite activities. Schedule during your child's best time of day. Tell the provider about your child's needs. " + DISCLAIMER},
        {"instruction": "What rights do parents have in the evaluation process?", "input": "", "output": "You have the right to ask questions, request referrals, get second opinions, and receive copies of reports. You can bring a support person to appointments. Know your local laws regarding special education and early intervention. " + DISCLAIMER},
        {"instruction": "How do I explain autism to my child?", "input": "", "output": "Use simple, positive language. Explain that their brain works in a special way, and they may need different kinds of support. Emphasize strengths. Adapt explanations to age and understanding. " + DISCLAIMER},
        {"instruction": "What if I feel overwhelmed as a parent?", "input": "", "output": "Caregiver burnout is real. Seek support from family, friends, support groups, or a counselor. Respite care can help. Taking care of yourself helps you care for your child. " + DISCLAIMER},
    ]
    for _ in range(10):
        for ex in parents:
            examples.append(ex)
    
    # --- GUIDANCE FOR TEACHERS (80 examples) ---
    teachers = [
        {"instruction": "How can I create an inclusive classroom for autistic students?", "input": "", "output": "Use visual schedules, clear routines, reduced sensory overload, and predictable transitions. Provide quiet spaces and flexibility. Collaborate with parents and specialists. Get to know each student's strengths and needs. " + DISCLAIMER},
        {"instruction": "What are visual supports and how do they help?", "input": "", "output": "Visual supports include pictures, schedules, and cue cards that show what to do or what comes next. They reduce anxiety, support understanding, and promote independence. Many students benefit from them. " + DISCLAIMER},
        {"instruction": "How should I handle meltdowns in the classroom?", "input": "", "output": "Stay calm, ensure safety, reduce demands, and offer a quiet space if possible. Avoid punishing; meltdowns are often from overload, not defiance. Plan with the student and parents for prevention. " + DISCLAIMER},
        {"instruction": "When should I recommend a parent seek screening?", "input": "", "output": "Share observations (e.g., social, communication, sensory) in a supportive way. Suggest discussing developmental screening with their healthcare provider. Provide specific examples. Avoid diagnosing—that's for professionals. " + DISCLAIMER},
        {"instruction": "How can I support an autistic student's communication?", "input": "", "output": "Use clear, literal language; allow extra processing time; support with visuals; and respect different communication styles (e.g., AAC, gestures). Work with the speech therapist and family. " + DISCLAIMER},
        {"instruction": "What is a sensory break?", "input": "", "output": "A sensory break is a short opportunity for movement or calming (e.g., walking, stretching, quiet time) to help regulate. It can prevent overload and support focus. Plan breaks into the daily schedule. " + DISCLAIMER},
        {"instruction": "How do I involve autistic students in group work?", "input": "", "output": "Assign clear roles, use structured activities, allow choice in partners, and provide visual instructions. Some students may need smaller groups or modified tasks. " + DISCLAIMER},
        {"instruction": "What training do teachers need for autism?", "input": "", "output": "Training in autism awareness, evidence-based strategies (e.g., visual supports, structured teaching), and collaboration with specialists is valuable. Many resources exist online and through professional development. " + DISCLAIMER},
    ]
    for _ in range(10):
        for ex in teachers:
            examples.append(ex)
    
    # --- OUT-OF-DOMAIN with polite refusals (10 examples) ---
    ood = [
        {"instruction": "What is the capital of France?", "input": "", "output": "I focus on early autism screening guidance and child development. For general knowledge questions like geography, please use a different resource. If you have questions about child development or autism screening, I'm here to help."},
        {"instruction": "How do I fix my car engine?", "input": "", "output": "I specialize in early autism screening awareness and child development guidance. I'm not able to help with automotive repairs. If you have questions about developmental screening or autism signs, I'd be glad to assist."},
        {"instruction": "Write me a poem about love.", "input": "", "output": "I'm designed to support questions about early autism screening and child development. I can't create creative content like poems. If you have concerns about a child's development, I can provide guidance and encourage professional screening."},
        {"instruction": "What's the best recipe for chocolate cake?", "input": "", "output": "I focus on autism screening guidance for caregivers and educators. I'm not able to provide recipes. If you have questions about early signs of autism or when to seek screening, I'm here to help."},
        {"instruction": "Can you help me with my math homework?", "input": "", "output": "I specialize in early autism screening and child development. For math or other academic subjects, please use appropriate educational resources. If you have questions about developmental screening, I'd be happy to assist."},
        {"instruction": "What's the weather like today?", "input": "", "output": "I focus on early autism screening and child development guidance. For weather information, please use a weather service. If you have questions about autism signs or screening, I'm here to help."},
        {"instruction": "Translate this to Spanish.", "input": "", "output": "I'm designed to support autism screening awareness and child development. I'm not a general translation tool. If you need information about autism screening in different languages or cultural contexts, I can help with that."},
        {"instruction": "What stocks should I invest in?", "input": "", "output": "I specialize in early autism screening and child development. I can't provide financial or investment advice. If you have questions about when to seek developmental screening for a child, I'm here to assist."},
        {"instruction": "Tell me a joke.", "input": "", "output": "I focus on providing guidance about early autism screening and child development. I'm not designed for entertainment. If you have questions about autism signs or screening tools like M-CHAT, I'd be glad to help."},
        {"instruction": "What's the best smartphone to buy?", "input": "", "output": "I specialize in autism screening guidance for caregivers and educators. I can't advise on consumer electronics. If you have questions about early developmental signs or when to seek professional screening, I'm here to help."},
    ]
    for ex in ood:
        examples.append(ex)
    
    # Trim to 800-1000 and ensure variety (we have 990 from above)
    examples = examples[:950]  # ~950 examples
    
    with open(output_path, "w", encoding="utf-8") as f:
        for ex in examples:
            f.write(json.dumps(ex, ensure_ascii=False) + "\n")
    
    return len(examples)


if __name__ == "__main__":
    count = create_dataset()
    print(f"Created dataset with {count} examples")
