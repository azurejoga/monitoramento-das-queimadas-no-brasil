# Monitoramento de Queimadas na Amazônia

Este projeto tem como objetivo monitorar as queimadas na Amazônia e apresentar informações diárias atualizadas sobre os focos de incêndio detectados. Abaixo, você pode visualizar as queimadas mais recentes, com detalhes sobre localização, satélite que realizou a detecção, e outros fatores relevantes.

## Estrutura dos Dados

Cada entrada na tabela representa um foco de incêndio com as seguintes informações:

- **ID:** Identificador único do foco de incêndio.
- **Latitude/Longitude:** Coordenadas geográficas do foco detectado. Para visualizar o local exato, insira estas coordenadas no Google Maps ou outro aplicativo de mapas.
- **Data/Hora GMT:** Data e hora da detecção em formato GMT (Greenwich Mean Time).
- **Satélite:** Satélite responsável pela detecção do foco de incêndio.
- **Município, Estado e País:** Localização administrativa do foco detectado.
- **Dias sem Chuva:** Número de dias consecutivos sem precipitação na região, o que pode indicar um aumento no risco de incêndio.
- **Precipitação:** Quantidade de chuva (em milímetros) registrada no local.
- **Risco de Fogo:** Índice que indica a probabilidade de ocorrência de incêndio, baseado em fatores como condições climáticas e quantidade de combustível disponível.
- **Bioma:** Bioma onde o foco foi identificado, como Amazônia, Cerrado, ou Mata Atlântica.
- **FRP (Fire Radiative Power):** Potência radiativa do fogo, que mede a intensidade do incêndio. Focos com FRP mais alto indicam incêndios mais intensos.

## Visualização Gráfica

Se você deseja visualizar de forma gráfica onde as queimadas estão ocorrendo, copie as coordenadas de latitude e longitude mais recentes e cole no Google Maps. Isso permite uma compreensão espacial mais clara da distribuição dos focos de incêndio. Alternativamente, você também pode usar a descrição de localização (Município, Estado e País) para identificar a região afetada.

## Informação Adicional

As queimadas na Amazônia não apenas afetam a biodiversidade local, mas também têm implicações globais, contribuindo para o aquecimento global e a emissão de gases de efeito estufa. O monitoramento contínuo é essencial para entender e mitigar os impactos desses incêndios, além de auxiliar na gestão de políticas ambientais e ações de preservação.

## Dados Diários - Página 63

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| fcbd0ee5-f0c9-3eec-baae-e54d361f520a | -16.08162 | -50.0014 | 2025-09-13 04:10:00 | NOAA-20 | ITABERAÍ | GOIÁS | Brasil | 5210406 | 52 | 33 | nan | nan | nan | Cerrado | 7.4 |
| ab857568-f01c-3632-8c3b-d31485842fbe | -15.20982 | -56.687 | 2025-09-13 04:10:00 | NOAA-20 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 9a5f12f4-7a89-3658-b73c-9f5f5d4b2663 | -15.14482 | -52.48909 | 2025-09-13 04:10:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c7051b19-2667-3179-9043-e7910de373d6 | -21.86977 | -46.49758 | 2025-09-13 04:10:00 | NOAA-20 | CALDAS | MINAS GERAIS | Brasil | 3110301 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| baaef0c8-f91c-318e-b6e1-19ad815b7fda | -15.1598 | -50.15621 | 2025-09-13 04:10:00 | NOAA-20 | ARAGUAPAZ | GOIÁS | Brasil | 5202155 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| b49f50cc-038b-3835-b75d-202f6d55d5d8 | -15.85673 | -47.23232 | 2025-09-13 04:10:00 | NOAA-20 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| e7048d14-0895-3195-9246-859f8d6eda2b | -17.83814 | -44.21909 | 2025-09-13 04:10:00 | NOAA-20 | BUENÓPOLIS | MINAS GERAIS | Brasil | 3109204 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 58d4d849-a711-3936-88ea-61b65c853006 | -16.35926 | -51.51226 | 2025-09-13 04:10:00 | NOAA-20 | ARENÓPOLIS | GOIÁS | Brasil | 5202353 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 7c0b0377-631f-3ed7-a8a1-abd5bb763fd0 | -19.99195 | -46.90535 | 2025-09-13 04:10:00 | NOAA-20 | TAPIRA | MINAS GERAIS | Brasil | 3168101 | 31 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 1836d31d-f824-36fe-8f8d-fcba33475e76 | -18.50557 | -43.96769 | 2025-09-13 04:10:00 | NOAA-20 | MONJOLOS | MINAS GERAIS | Brasil | 3142502 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 300875bd-aea6-3708-893e-888cb4283a27 | -17.41457 | -49.24432 | 2025-09-13 04:10:00 | NOAA-20 | PROFESSOR JAMIL | GOIÁS | Brasil | 5218391 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 25c8a454-4806-30e6-a033-1a6fdab3fb1d | -21.55784 | -45.43325 | 2025-09-13 04:10:00 | NOAA-20 | VARGINHA | MINAS GERAIS | Brasil | 3170701 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| 6be87fbf-1c21-3cf7-9f9e-b256c6f5d51e | -16.07456 | -49.9916 | 2025-09-13 04:10:00 | NOAA-20 | ITABERAÍ | GOIÁS | Brasil | 5210406 | 52 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 40da04ab-5a7a-3526-8339-62c9cb0c9177 | -20.41557 | -46.51707 | 2025-09-13 04:10:00 | NOAA-20 | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 805a25f8-9a5a-3797-ba4a-a8039d1d9c79 | -21.97524 | -44.61043 | 2025-09-13 04:10:00 | NOAA-20 | AIURUOCA | MINAS GERAIS | Brasil | 3101201 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| 0f7897b9-4ad8-3508-80b3-8c3016f3df12 | -17.39866 | -48.2313 | 2025-09-13 04:10:00 | NOAA-20 | URUTAÍ | GOIÁS | Brasil | 5221809 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 16743f01-3ee4-31d9-b2a9-3f7406e97df3 | -15.54533 | -54.80298 | 2025-09-13 04:10:00 | NOAA-20 | DOM AQUINO | MATO GROSSO | Brasil | 5103601 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 4f6f8eda-a126-3253-959d-10c9ae7eb49f | -15.15047 | -52.48753 | 2025-09-13 04:10:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 2d55c00d-3968-3a17-b996-814c71b845eb | -19.06411 | -43.86611 | 2025-09-13 04:10:00 | NOAA-20 | SANTANA DE PIRAPAMA | MINAS GERAIS | Brasil | 3158508 | 31 | 33 | nan | nan | nan | Cerrado | 0.3 |
| b617c156-57d3-3a2a-a079-586f405ecc7c | -17.95741 | -46.93441 | 2025-09-13 04:10:00 | NOAA-20 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 6d99802d-6787-3dcf-8313-4e48cea0a313 | -18.04079 | -45.42844 | 2025-09-13 04:10:00 | NOAA-20 | SÃO GONÇALO DO ABAETÉ | MINAS GERAIS | Brasil | 3161700 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| cddf9285-5a42-30af-af31-8820aa5b6159 | -15.69424 | -50.58667 | 2025-09-13 04:10:00 | NOAA-20 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 39520813-cf0a-375b-97f6-e1e54d76c89a | -16.39565 | -49.06794 | 2025-09-13 04:10:00 | NOAA-20 | TEREZÓPOLIS DE GOIÁS | GOIÁS | Brasil | 5221197 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 3d734a3d-71a2-3d72-9b1a-0879ce85a852 | -18.60351 | -47.18839 | 2025-09-13 04:10:00 | NOAA-20 | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 5d6671dd-0385-387b-8bf9-8b69724e3e05 | -16.06674 | -49.98587 | 2025-09-13 04:10:00 | NOAA-20 | ITABERAÍ | GOIÁS | Brasil | 5210406 | 52 | 33 | nan | nan | nan | Cerrado | 4.6 |
| aa6753c8-5107-376b-a2c8-3e00296329f6 | -15.58398 | -54.75615 | 2025-09-13 04:10:00 | NOAA-20 | DOM AQUINO | MATO GROSSO | Brasil | 5103601 | 51 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 3a99a86b-78d1-3bf1-b13c-8bdd4ad32c68 | -16.25968 | -50.07082 | 2025-09-13 04:10:00 | NOAA-20 | AMERICANO DO BRASIL | GOIÁS | Brasil | 5200852 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 8816a8fb-3d48-3d66-83a8-714b47943270 | -16.5558 | -49.22169 | 2025-09-13 04:10:00 | NOAA-20 | GOIÂNIA | GOIÁS | Brasil | 5208707 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 4f403a1e-888c-3076-933c-0a1b25da6d12 | -18.27989 | -42.59808 | 2025-09-13 04:10:00 | NOAA-20 | SÃO JOSÉ DO JACURI | MINAS GERAIS | Brasil | 3163508 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| fe0b48e7-69d2-3b87-9ab1-012ce4c80cd3 | -20.72753 | -56.7393 | 2025-09-13 04:10:00 | NOAA-20 | BODOQUENA | MATO GROSSO DO SUL | Brasil | 5002159 | 50 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 4403f773-4ef7-3124-a5f0-7354c105e7f8 | -17.94465 | -45.26668 | 2025-09-13 04:10:00 | NOAA-20 | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 0270ac06-5f67-3ae7-8151-378f3dceefca | -20.44928 | -46.44024 | 2025-09-13 04:10:00 | NOAA-20 | SÃO JOÃO BATISTA DO GLÓRIA | MINAS GERAIS | Brasil | 3162203 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 004364b8-2f09-366a-abda-5602065466fe | -17.55131 | -44.54931 | 2025-09-13 04:10:00 | NOAA-20 | VÁRZEA DA PALMA | MINAS GERAIS | Brasil | 3170800 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 14d2b241-b0f3-3e96-a664-29d1d5f63ee0 | -21.62244 | -46.81907 | 2025-09-13 04:10:00 | NOAA-20 | SÃO JOSÉ DO RIO PARDO | SÃO PAULO | Brasil | 3549706 | 35 | 33 | nan | nan | nan | Mata Atlântica | 18.1 |
| db4bd042-37c3-3655-9858-cccc8acffac6 | -16.78105 | -41.71737 | 2025-09-13 04:10:00 | NOAA-20 | ITINGA | MINAS GERAIS | Brasil | 3134004 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.9 |
| f79eac34-a3bb-311e-97be-5ea40bcbc7aa | -16.64576 | -49.75394 | 2025-09-13 04:10:00 | NOAA-20 | NAZÁRIO | GOIÁS | Brasil | 5214408 | 52 | 33 | nan | nan | nan | Cerrado | 14.6 |
| 47c151ae-8c47-3694-b9b2-aa66245bd924 | -19.98095 | -46.9282 | 2025-09-13 04:10:00 | NOAA-20 | TAPIRA | MINAS GERAIS | Brasil | 3168101 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e2f02955-7893-3fce-ac16-11e31eca3d29 | -17.32206 | -46.65899 | 2025-09-13 04:10:00 | NOAA-20 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 4ede930a-5b29-3f55-9c73-6f61db74fbd3 | -16.35878 | -51.54034 | 2025-09-13 04:10:00 | NOAA-20 | ARENÓPOLIS | GOIÁS | Brasil | 5202353 | 52 | 33 | nan | nan | nan | Cerrado | 4.2 |
| d9b9fb76-e5b7-3adf-8df6-4bff682f6367 | -15.84797 | -49.94404 | 2025-09-13 04:10:00 | NOAA-20 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 55eb8d5b-86dc-35cf-9c47-103bd6185b91 | -20.01905 | -47.63508 | 2025-09-13 04:10:00 | NOAA-20 | CONQUISTA | MINAS GERAIS | Brasil | 3118205 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 6570daa2-7961-37de-962f-fd37c0ecc70d | -16.09286 | -49.96473 | 2025-09-13 04:10:00 | NOAA-20 | ITABERAÍ | GOIÁS | Brasil | 5210406 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f27f0ded-932f-3399-bc05-94eb65c3ef6c | -17.14053 | -53.89284 | 2025-09-13 04:10:00 | NOAA-20 | ITIQUIRA | MATO GROSSO | Brasil | 5104609 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 5dc357c6-fab9-3515-94f4-a7651fefb6ee | -18.67655 | -48.22283 | 2025-09-13 04:10:00 | NOAA-20 | ARAGUARI | MINAS GERAIS | Brasil | 3103504 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| b6824e66-7df3-3287-a80c-39b1ce5d8219 | -17.14086 | -48.5103 | 2025-09-13 04:10:00 | NOAA-20 | PIRES DO RIO | GOIÁS | Brasil | 5217401 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 971503d7-f0c3-3a11-8d17-01076865d4d6 | -17.42393 | -49.26118 | 2025-09-13 04:10:00 | NOAA-20 | PROFESSOR JAMIL | GOIÁS | Brasil | 5218391 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 056f50cc-16bf-3300-8a0a-0b195269c86b | -15.6856 | -50.57448 | 2025-09-13 04:10:00 | NOAA-20 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| bfcbbd04-b877-363f-8244-13806e17b15c | -17.43442 | -49.22627 | 2025-09-13 04:10:00 | NOAA-20 | PIRACANJUBA | GOIÁS | Brasil | 5217104 | 52 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 7b158676-0927-34a9-9756-d50d6823f750 | -15.06915 | -52.48544 | 2025-09-13 04:10:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 23165835-032a-3e3e-af07-d62094966ddd | -21.23549 | -44.93943 | 2025-09-13 04:10:00 | NOAA-20 | IJACI | MINAS GERAIS | Brasil | 3130408 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 5a613c60-011e-323c-ba9e-c39571e0db34 | -20.41283 | -46.5125 | 2025-09-13 04:10:00 | NOAA-20 | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| ba6c6696-3d3e-3d96-83bb-8b197968ac18 | -17.46724 | -43.72696 | 2025-09-13 04:10:00 | NOAA-20 | OLHOS-D'ÁGUA | MINAS GERAIS | Brasil | 3145455 | 31 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 632eb359-be57-3bc7-a0ea-a91a954d3579 | -16.88706 | -45.78078 | 2025-09-13 04:10:00 | NOAA-20 | BRASILÂNDIA DE MINAS | MINAS GERAIS | Brasil | 3108552 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e2cfd98d-6c56-3a71-a54b-58ca4a6c25a8 | -19.99917 | -47.64427 | 2025-09-13 04:10:00 | NOAA-20 | CONQUISTA | MINAS GERAIS | Brasil | 3118205 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 13a61d28-1ad7-3524-a940-4bfee60a0a98 | -20.45082 | -46.4362 | 2025-09-13 04:10:00 | NOAA-20 | SÃO JOÃO BATISTA DO GLÓRIA | MINAS GERAIS | Brasil | 3162203 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 3c9fb598-5638-3e21-86a0-704d7adef7c7 | -19.50904 | -46.14084 | 2025-09-13 04:10:00 | NOAA-20 | CAMPOS ALTOS | MINAS GERAIS | Brasil | 3111507 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 4ea35280-3ad1-3672-8c19-a23ceb43b81a | -19.64063 | -45.07956 | 2025-09-13 04:10:00 | NOAA-20 | LEANDRO FERREIRA | MINAS GERAIS | Brasil | 3138302 | 31 | 33 | nan | nan | nan | Cerrado | 4.6 |
| a43b3679-11f0-3933-b277-65153dd60657 | -16.40851 | -49.04357 | 2025-09-13 04:10:00 | NOAA-20 | TEREZÓPOLIS DE GOIÁS | GOIÁS | Brasil | 5221197 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| f02a3b3b-7e19-3638-b03b-0a14ffb3a16f | -15.17363 | -52.31695 | 2025-09-13 04:10:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 1fa7c63b-f483-34b2-b682-e210fd6b6cd4 | -17.42051 | -49.23449 | 2025-09-13 04:10:00 | NOAA-20 | PROFESSOR JAMIL | GOIÁS | Brasil | 5218391 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 659753c5-9d30-3294-966b-151c2f73603b | -16.28519 | -45.68493 | 2025-09-13 04:10:00 | NOAA-20 | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 71d85f1c-f21c-3ac1-9dce-e388d811cfb0 | -17.99856 | -46.9283 | 2025-09-13 04:10:00 | NOAA-20 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 5bcefda3-bef4-3efb-b408-b169daedcd01 | -17.40873 | -48.21837 | 2025-09-13 04:10:00 | NOAA-20 | URUTAÍ | GOIÁS | Brasil | 5221809 | 52 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 2eb6fa8e-b985-3437-8b65-3a455c78a552 | -17.41319 | -49.22927 | 2025-09-13 04:10:00 | NOAA-20 | PROFESSOR JAMIL | GOIÁS | Brasil | 5218391 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| cfa21b55-d7f5-3651-b042-0c466eb201b6 | -17.9478 | -42.52723 | 2025-09-13 04:10:00 | NOAA-20 | ARICANDUVA | MINAS GERAIS | Brasil | 3104452 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 7bbc9327-1ada-32e4-ae01-be598019d331 | -17.13597 | -48.50724 | 2025-09-13 04:10:00 | NOAA-20 | PIRES DO RIO | GOIÁS | Brasil | 5217401 | 52 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 4a17f325-c757-3e11-a91b-79b32df56a56 | -17.41717 | -49.23011 | 2025-09-13 04:10:00 | NOAA-20 | PROFESSOR JAMIL | GOIÁS | Brasil | 5218391 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| e6b0131f-d260-3161-b57d-92da561b541c | -20.02259 | -47.63578 | 2025-09-13 04:10:00 | NOAA-20 | CONQUISTA | MINAS GERAIS | Brasil | 3118205 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| eb9bba8a-3d68-316d-aeeb-6be10c46956b | -20.34525 | -46.66478 | 2025-09-13 04:10:00 | NOAA-20 | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| cfcc18e8-a88a-30d3-a451-1558e5c3e85b | -17.95119 | -42.52781 | 2025-09-13 04:10:00 | NOAA-20 | ARICANDUVA | MINAS GERAIS | Brasil | 3104452 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 51c08195-e2f3-33f6-a1c0-c09b552c60cb | -16.53101 | -51.74781 | 2025-09-13 04:10:00 | NOAA-20 | PIRANHAS | GOIÁS | Brasil | 5217203 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 16d88973-8aed-320b-a92b-7afe1077ffe0 | -16.40508 | -44.047 | 2025-09-13 04:10:00 | NOAA-20 | MONTES CLAROS | MINAS GERAIS | Brasil | 3143302 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| c86dbb52-7969-3cb6-8335-e67f903263e0 | -18.85551 | -46.83741 | 2025-09-13 04:10:00 | NOAA-20 | PATROCÍNIO | MINAS GERAIS | Brasil | 3148103 | 31 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 1cb3829e-44a2-3eee-b1c7-25263386c88c | -21.1599 | -47.75755 | 2025-09-13 04:10:00 | NOAA-20 | RIBEIRÃO PRETO | SÃO PAULO | Brasil | 3543402 | 35 | 33 | nan | nan | nan | Cerrado | 0.9 |
| f647bb78-8f47-36d0-b4fd-f51991f5852b | -16.36793 | -41.38459 | 2025-09-13 04:10:00 | NOAA-20 | JEQUITINHONHA | MINAS GERAIS | Brasil | 3135803 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| 389a1591-b80a-3d04-8023-8a3b1bf8d26a | -16.25193 | -50.06466 | 2025-09-13 04:10:00 | NOAA-20 | AMERICANO DO BRASIL | GOIÁS | Brasil | 5200852 | 52 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 3b644349-6ee7-34c7-9d26-0ae27bb9e742 | -15.13406 | -52.48948 | 2025-09-13 04:10:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 1f3ef10b-b2c4-3058-9192-af476dcd4ec2 | -15.24087 | -51.39373 | 2025-09-13 04:10:00 | NOAA-20 | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 9.3 |
| 8e694fe9-3d06-35e4-91b7-27917f62e20f | -15.69064 | -50.58116 | 2025-09-13 04:10:00 | NOAA-20 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| b883169a-9db1-357b-8663-2be19cfcb70d | -19.16553 | -46.66221 | 2025-09-13 04:10:00 | NOAA-20 | SERRA DO SALITRE | MINAS GERAIS | Brasil | 3166808 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 0ff078d7-d5e6-346b-8519-a0efb3e679a3 | -20.41711 | -50.74688 | 2025-09-13 04:10:00 | NOAA-20 | PALMEIRA D'OESTE | SÃO PAULO | Brasil | 3535200 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| b812c855-13e2-37e7-aa91-c19b36649bc5 | -16.32521 | -43.75767 | 2025-09-13 04:10:00 | NOAA-20 | CAPITÃO ENÉAS | MINAS GERAIS | Brasil | 3112703 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| dd726318-82b7-3efb-a6df-0626c023d56c | -15.76929 | -52.23609 | 2025-09-13 04:10:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| ddcb818d-e476-3a3d-8766-07df3a8d857c | -17.23699 | -46.83756 | 2025-09-13 04:10:00 | NOAA-20 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| fe59cd49-b9a3-3d0e-ade7-46956345b702 | -20.02564 | -47.6353 | 2025-09-13 04:10:00 | NOAA-20 | CONQUISTA | MINAS GERAIS | Brasil | 3118205 | 31 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 08349c39-d90b-30ae-98da-2b0fdcb10346 | -15.17292 | -52.32055 | 2025-09-13 04:10:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f183568e-3afd-324a-b51b-c39983430d57 | -19.94162 | -42.31979 | 2025-09-13 04:10:00 | NOAA-20 | RAUL SOARES | MINAS GERAIS | Brasil | 3154002 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 47cd7b76-5bd5-381a-b5dc-11775c376abf | -16.49647 | -55.13625 | 2025-09-13 04:10:00 | NOAA-20 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 3.4 |
| 4b4e6606-c830-3fb6-bbc7-2c33fcf3129c | -15.59705 | -54.76103 | 2025-09-13 04:10:00 | NOAA-20 | DOM AQUINO | MATO GROSSO | Brasil | 5103601 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d50d3010-a1ff-3051-b81e-6659efc6c3d9 | -17.28539 | -47.24838 | 2025-09-13 04:10:00 | NOAA-20 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| f615d1cc-1a06-3f5f-a693-3454db796fc2 | -21.23884 | -47.76282 | 2025-09-13 04:10:00 | NOAA-20 | RIBEIRÃO PRETO | SÃO PAULO | Brasil | 3543402 | 35 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 818d4c80-9ce4-3ac5-8ec0-2f47bc13bbd2 | -15.138 | -52.49652 | 2025-09-13 04:10:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c8db2f86-da08-3a47-a004-4c6121352386 | -18.0566 | -45.45826 | 2025-09-13 04:10:00 | NOAA-20 | SÃO GONÇALO DO ABAETÉ | MINAS GERAIS | Brasil | 3161700 | 31 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 98e7e65e-b2b6-33e4-bb7a-ac6e8248704f | -17.91556 | -44.45878 | 2025-09-13 04:10:00 | NOAA-20 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 1f2715ff-727a-3170-8958-bacb934b836f | -20.06691 | -43.69633 | 2025-09-13 04:10:00 | NOAA-20 | CAETÉ | MINAS GERAIS | Brasil | 3110004 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| d79c83ea-430b-3e4c-8df9-d31b4dcc4e1a | -22.15738 | -47.37096 | 2025-09-13 04:10:00 | NOAA-20 | LEME | SÃO PAULO | Brasil | 3526704 | 35 | 33 | nan | nan | nan | Mata Atlântica | 4.2 |
| a5dab5bc-953e-3b7f-be00-c844986197ed | -20.09688 | -46.90746 | 2025-09-13 04:10:00 | NOAA-20 | SACRAMENTO | MINAS GERAIS | Brasil | 3156908 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 9c84a3bc-cbce-3020-a4b4-ed400aa9b655 | -17.30146 | -48.7331 | 2025-09-13 04:10:00 | NOAA-20 | SANTA CRUZ DE GOIÁS | GOIÁS | Brasil | 5219209 | 52 | 33 | nan | nan | nan | Cerrado | 4.3 |
| e7407ea1-a454-3703-b050-3253ac5d3c2e | -20.0783 | -46.91233 | 2025-09-13 04:10:00 | NOAA-20 | SACRAMENTO | MINAS GERAIS | Brasil | 3156908 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c8edb1cf-dd26-3ba7-9d40-34532486b6f2 | -19.69522 | -47.96711 | 2025-09-13 04:10:00 | NOAA-20 | UBERABA | MINAS GERAIS | Brasil | 3170107 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |


[Clique aqui para ver as próximas entradas](README64.md)
