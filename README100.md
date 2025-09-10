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

## Dados Diários - Página 100

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 4919cf20-0c6a-3557-9cdf-e48e508cc4d3 | -11.06896 | -65.18781 | 2025-09-10 05:06:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 6be403cd-bcfb-3d83-8806-4e6038e7f94c | -11.79129 | -60.69075 | 2025-09-10 05:06:00 | NOAA-20 | PIMENTA BUENO | RONDÔNIA | Brasil | 1100189 | 11 | 33 | nan | nan | nan | Amazônia | 2.1 |
| fc13115f-0885-3c75-8328-364757baa15e | -14.85657 | -49.53553 | 2025-09-10 05:06:00 | NOAA-20 | ITAPACI | GOIÁS | Brasil | 5210901 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 17f3ed9e-637a-3be7-bfe3-abcd634806a4 | -14.89744 | -50.12836 | 2025-09-10 05:06:00 | NOAA-20 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 18.5 |
| adaca7f2-1892-30fc-8080-f1683e77c915 | -12.77262 | -61.44804 | 2025-09-10 05:06:00 | NOAA-20 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| b5868efd-30ea-3209-aea9-266e788bae56 | -14.92363 | -50.1177 | 2025-09-10 05:06:00 | NOAA-20 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 15.5 |
| f5366120-25ad-32bb-8ead-2c2bf0bc81c8 | -15.8086 | -52.25903 | 2025-09-10 05:06:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| c00fa076-ee9d-3643-8299-f06acfa1e16d | -17.7365 | -44.49282 | 2025-09-10 05:06:00 | NOAA-20 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 58f69f62-1f35-3c4e-8984-fe4c5e29cd45 | -15.02018 | -50.08219 | 2025-09-10 05:06:00 | NOAA-20 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 17.7 |
| 6ebf9c62-a7a2-35b8-bcd2-b1526ac4b5ee | -19.29737 | -47.98507 | 2025-09-10 05:06:00 | NOAA-20 | UBERLÂNDIA | MINAS GERAIS | Brasil | 3170206 | 31 | 33 | nan | nan | nan | Cerrado | 6.3 |
| c4c2a771-d326-3a4c-8731-691d72505398 | -17.74182 | -44.49012 | 2025-09-10 05:06:00 | NOAA-20 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 09204f48-cfd9-358a-91b6-5d541ecf829e | -13.94351 | -48.26323 | 2025-09-10 05:06:00 | NOAA-20 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 4.6 |
| e20a81ed-c2b6-3643-ba60-7f17aa0102c4 | -14.56178 | -48.7634 | 2025-09-10 05:06:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 4.1 |
| d04a603d-ef85-3f5f-9d67-e4d532d33c6d | -12.93732 | -54.81562 | 2025-09-10 05:06:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| dc513733-b112-341c-8562-71d93996bc17 | -15.08899 | -50.07639 | 2025-09-10 05:06:00 | NOAA-20 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 701f5ebb-45b8-38f1-aa40-5dfa6995a1f2 | -14.8958 | -55.86542 | 2025-09-10 05:06:00 | NOAA-20 | CHAPADA DOS GUIMARÃES | MATO GROSSO | Brasil | 5103007 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 3a11b1c9-c0d4-3ee5-8e98-1223f2f553b4 | -16.4615 | -50.67052 | 2025-09-10 05:06:00 | NOAA-20 | MOIPORÁ | GOIÁS | Brasil | 5213400 | 52 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 7a659e0e-2e91-3147-ae9c-65f0bf4b567d | -15.51996 | -52.7673 | 2025-09-10 05:06:00 | NOAA-20 | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 201550b6-9b0b-3fb5-9974-c70fff1f11a1 | -14.3885 | -47.32685 | 2025-09-10 05:06:00 | NOAA-20 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 8a9c1648-93b4-3e5b-9e45-e727e12522c3 | -15.47591 | -49.37039 | 2025-09-10 05:06:00 | NOAA-20 | RIANÁPOLIS | GOIÁS | Brasil | 5218706 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ed2df115-b525-3606-b774-9a267688920c | -18.13439 | -51.72448 | 2025-09-10 05:06:00 | NOAA-20 | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b9d81f38-3bc5-3c93-b4c4-5651f11beaa3 | -18.46699 | -46.47579 | 2025-09-10 05:06:00 | NOAA-20 | PRESIDENTE OLEGÁRIO | MINAS GERAIS | Brasil | 3153400 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 89a37265-9ff6-38e3-8b13-e9c5321e15c1 | -17.23919 | -46.07773 | 2025-09-10 05:06:00 | NOAA-20 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| e3316be6-7beb-3147-839c-e095a2c8db82 | -14.8985 | -50.12537 | 2025-09-10 05:06:00 | NOAA-20 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 16.4 |
| ba7a162b-22c3-3dfe-ac61-7dd4537465db | -15.51593 | -52.76677 | 2025-09-10 05:06:00 | NOAA-20 | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 3304e7c7-ef25-39e6-aa65-6c5c69c33cf3 | -14.90292 | -50.12334 | 2025-09-10 05:06:00 | NOAA-20 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 18.5 |
| 67d455c4-c686-300b-b137-00c48cfb758b | -18.33978 | -49.33807 | 2025-09-10 05:06:00 | NOAA-20 | ITUMBIARA | GOIÁS | Brasil | 5211503 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| cfcd32b2-b380-34f2-9570-edbacc486eb7 | -15.93978 | -50.23693 | 2025-09-10 05:06:00 | NOAA-20 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 4c4f41ab-f9b4-37d1-abcf-2d6189cfab24 | -15.73141 | -53.51979 | 2025-09-10 05:06:00 | NOAA-20 | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 4ebfc88c-17b5-3ebb-8f5a-70fa1f4f122a | -11.77922 | -64.94603 | 2025-09-10 05:06:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| c92c4693-d235-37cf-bcff-b2c0cb127539 | -15.80668 | -52.24882 | 2025-09-10 05:06:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 073563cb-1232-3c52-805c-8aec2e47f1f4 | -15.80939 | -52.26101 | 2025-09-10 05:06:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 776966a6-08ea-375d-b5f3-3e3529e7e490 | -15.01897 | -50.09233 | 2025-09-10 05:06:00 | NOAA-20 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 9.3 |
| ed84dadd-78b1-3565-8df4-c8dcbf04f21a | -15.84649 | -52.2702 | 2025-09-10 05:06:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| bea5b031-180e-37d2-a20c-3e1544e2594a | -17.3133 | -46.73592 | 2025-09-10 05:06:00 | NOAA-20 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 2.8 |
| cc237dfa-9a3b-33bb-92dd-07db3b37b861 | -14.92433 | -55.93203 | 2025-09-10 05:06:00 | NOAA-20 | CHAPADA DOS GUIMARÃES | MATO GROSSO | Brasil | 5103007 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 35c2b4d8-6b6f-384c-b061-fd9614af3797 | -17.75169 | -44.48161 | 2025-09-10 05:06:00 | NOAA-20 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 6.5 |
| fc384f2f-c2aa-3e5c-8993-ff5954b10a10 | -14.89238 | -55.86486 | 2025-09-10 05:06:00 | NOAA-20 | CHAPADA DOS GUIMARÃES | MATO GROSSO | Brasil | 5103007 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 5ac06003-d110-3734-a0c6-ac6b1f2ee2d8 | -11.07394 | -65.18877 | 2025-09-10 05:06:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| b1193119-feb0-309e-8f1f-136ff6cf6679 | -15.51786 | -48.37996 | 2025-09-10 05:06:00 | NOAA-20 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| fd50a3a6-b9d7-3400-82dd-c7a17bc4456b | -15.10692 | -50.08863 | 2025-09-10 05:06:00 | NOAA-20 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 94d01dc1-6c4e-3ed7-a566-0b5a681e6730 | -13.96654 | -48.22287 | 2025-09-10 05:06:00 | NOAA-20 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 5.1 |
| cfb696aa-f433-317e-84a3-3b621516df56 | -15.95236 | -48.10701 | 2025-09-10 05:06:00 | NOAA-20 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 1.9 |
| c12623b2-c663-3893-b0cf-9c925e21157a | -15.80811 | -52.26271 | 2025-09-10 05:06:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 46988d62-afb6-35bb-b9ac-ad0cbcc06b85 | -12.93791 | -54.81167 | 2025-09-10 05:06:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 927619d4-47f7-3aa5-b689-4e4045a5279d | -13.11906 | -54.93081 | 2025-09-10 05:06:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 35b6ba02-0eea-3ba4-a141-55663a67119a | -14.92659 | -55.91695 | 2025-09-10 05:06:00 | NOAA-20 | CHAPADA DOS GUIMARÃES | MATO GROSSO | Brasil | 5103007 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 6aae4416-d19a-371d-9417-9de85c6bb59c | -14.39122 | -47.32335 | 2025-09-10 05:06:00 | NOAA-20 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 0dedc75d-03c7-351f-916c-151c0801de19 | -15.01664 | -48.02419 | 2025-09-10 05:06:00 | NOAA-20 | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d4c94504-4eef-3c92-8d14-0bbeb528898c | -15.09316 | -50.08191 | 2025-09-10 05:06:00 | NOAA-20 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| ebcfc31c-429e-3093-bf89-5ad860199a81 | -15.81218 | -52.27241 | 2025-09-10 05:06:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d56382c7-1b97-340d-88e4-9d232b0277f0 | -17.20585 | -50.17114 | 2025-09-10 05:06:00 | NOAA-20 | JANDAIA | GOIÁS | Brasil | 5211701 | 52 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 344cdacc-ffa1-367d-92b0-f571077db3c1 | -19.72855 | -47.90289 | 2025-09-10 05:06:00 | NOAA-20 | UBERABA | MINAS GERAIS | Brasil | 3170107 | 31 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 2f90a91b-a7e2-3d03-8668-200f266a2fa4 | -19.64303 | -45.05284 | 2025-09-10 05:06:00 | NOAA-20 | LEANDRO FERREIRA | MINAS GERAIS | Brasil | 3138302 | 31 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 0998c8fa-2492-3350-842c-47364fc7991a | -15.13507 | -52.39943 | 2025-09-10 05:06:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 56609958-e20a-3f61-87b7-8db6e1bf95d4 | -12.41602 | -63.88947 | 2025-09-10 05:06:00 | NOAA-20 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 823eabf5-1d19-386c-8a2e-e40c2da38f4b | -15.52201 | -48.39124 | 2025-09-10 05:06:00 | NOAA-20 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 09e28f03-f57d-3d7b-93f1-d6a002e16c93 | -18.14127 | -51.72827 | 2025-09-10 05:06:00 | NOAA-20 | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| a10c2a6d-a02c-357d-ab9e-50c90efa7d7a | -16.28387 | -45.68434 | 2025-09-10 05:06:00 | NOAA-20 | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | 5.2 |
| a2bfe4a7-3b48-3ee0-ad9c-85a743c941a5 | -14.42775 | -52.95218 | 2025-09-10 05:06:00 | NOAA-20 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| fd55766b-ae51-3a2d-9c9c-36cd609cfad5 | -17.23882 | -46.0817 | 2025-09-10 05:06:00 | NOAA-20 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 94a1469a-d3a6-34c7-9c3d-b5f9ed44f033 | -13.12023 | -54.92297 | 2025-09-10 05:06:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 00ca97f0-a7df-36bb-a316-4d5a8f8f0135 | -19.72725 | -47.90519 | 2025-09-10 05:06:00 | NOAA-20 | UBERABA | MINAS GERAIS | Brasil | 3170107 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f8dd4b6e-ec81-3c86-960d-3836d692c874 | -15.83204 | -48.97129 | 2025-09-10 05:06:00 | NOAA-20 | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 09846305-ed46-35b2-837d-3dbfd317d780 | -16.34138 | -52.94521 | 2025-09-10 05:06:00 | NOAA-20 | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| dbca6772-1a34-3b77-8927-374588d72f55 | -14.89693 | -55.85783 | 2025-09-10 05:06:00 | NOAA-20 | CHAPADA DOS GUIMARÃES | MATO GROSSO | Brasil | 5103007 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 3c99f1c7-3353-3cd0-a6f0-8340975553e4 | -15.48456 | -49.38378 | 2025-09-10 05:06:00 | NOAA-20 | RIANÁPOLIS | GOIÁS | Brasil | 5218706 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 898fe988-4c9d-3410-8d15-045bf674d2e8 | -15.13562 | -52.39539 | 2025-09-10 05:06:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 7c64da4f-38ae-3efa-badf-faeb6eac3887 | -15.27749 | -53.78777 | 2025-09-10 05:06:00 | NOAA-20 | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 47ce52ab-82a4-3f3a-9572-85f921178225 | -15.95199 | -48.1103 | 2025-09-10 05:06:00 | NOAA-20 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 1.9 |
| d5b4149d-f445-3b6d-b02d-58fee9f52d49 | -12.35219 | -63.64079 | 2025-09-10 05:06:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 03ce36eb-3361-3271-ae44-6f232b099067 | -15.10678 | -50.09063 | 2025-09-10 05:06:00 | NOAA-20 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| faf60f45-1e17-3f83-9e58-f4662a60b0cc | -15.80848 | -52.26813 | 2025-09-10 05:06:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 5423bfc6-4b8e-32cb-bddf-db79db089a40 | -15.05741 | -50.13516 | 2025-09-10 05:06:00 | NOAA-20 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 12.4 |
| b34d492a-10fa-35b5-9d7e-e073eff5623c | -12.6126 | -56.96121 | 2025-09-10 05:06:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e20c022e-dd1e-3a6a-b0cd-6ed36a8732c0 | -14.567 | -48.76389 | 2025-09-10 05:06:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| cd6ebc03-9f9b-3c14-adab-1aa47ed0d717 | -13.12836 | -54.91623 | 2025-09-10 05:06:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 60de4b51-81cd-3c1e-aa53-e35db40b1755 | -15.80656 | -52.24252 | 2025-09-10 05:06:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 6cfdcf30-652e-3dab-a153-ae6d6f2df6a7 | -15.04727 | -50.13877 | 2025-09-10 05:06:00 | NOAA-20 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 7d274f1f-40d5-3fa3-b4bf-b6cf32461f0b | -17.4068 | -49.88636 | 2025-09-10 05:06:00 | NOAA-20 | EDÉIA | GOIÁS | Brasil | 5207402 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 5d8ef03e-440d-3fe6-a7cc-98a654538945 | -16.3459 | -52.94212 | 2025-09-10 05:06:00 | NOAA-20 | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 1d343458-7a97-39c5-adbd-348e1a3f8795 | -15.01963 | -50.08715 | 2025-09-10 05:06:00 | NOAA-20 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 19.2 |
| 9fd3c611-dfda-3adc-ab4b-2b413871ec15 | -13.12371 | -54.92353 | 2025-09-10 05:06:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 15352e7c-0b47-3d4c-8700-3e6955050dc1 | -15.11159 | -50.09114 | 2025-09-10 05:06:00 | NOAA-20 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 1b48c821-c0a0-30c4-aa25-8e9d5bd4e8c3 | -15.09853 | -50.07795 | 2025-09-10 05:06:00 | NOAA-20 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 7783be31-6f4e-30ed-ad63-230bc147599c | -18.01159 | -47.12616 | 2025-09-10 05:06:00 | NOAA-20 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 66dd24b5-02cf-32b9-910e-6a6c7e20d32a | -15.5124 | -52.76252 | 2025-09-10 05:06:00 | NOAA-20 | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ae83adf4-5d05-3db1-b883-c561d8d26a46 | -18.69279 | -52.59715 | 2025-09-10 05:06:00 | NOAA-20 | CHAPADÃO DO SUL | MATO GROSSO DO SUL | Brasil | 5002951 | 50 | 33 | nan | nan | nan | Cerrado | 1.4 |
| eda21527-574b-3eec-93fc-4b77480679a8 | -15.47556 | -49.37339 | 2025-09-10 05:06:00 | NOAA-20 | RIANÁPOLIS | GOIÁS | Brasil | 5218706 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| af15a4e3-3ca3-35b7-ab45-690b38814457 | -17.71144 | -44.4301 | 2025-09-10 05:06:00 | NOAA-20 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 08ccfc64-df17-329e-a83a-09e4016c4af2 | -15.66213 | -49.92848 | 2025-09-10 05:06:00 | NOAA-20 | ITAPURANGA | GOIÁS | Brasil | 5211206 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 2ce35845-cd05-3414-95c5-a023bfceaabc | -15.09375 | -50.07724 | 2025-09-10 05:06:00 | NOAA-20 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 8fee3875-a9ad-3cc3-b069-47a7ad75bfa0 | -18.00565 | -47.12472 | 2025-09-10 05:06:00 | NOAA-20 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| b89dcb90-1b0e-36db-8114-bcc16b58912b | -14.92067 | -50.10219 | 2025-09-10 05:06:00 | NOAA-20 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 128bc382-76e8-3d08-9ce9-bb4314912a57 | -14.89973 | -50.11509 | 2025-09-10 05:06:00 | NOAA-20 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 4.6 |
| c9037e9e-58b0-3709-9afa-8e24821716c7 | -14.57483 | -51.40461 | 2025-09-10 05:06:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 0.5 |
| d9379ebd-d318-3602-87c5-c9be601f5e86 | -12.61536 | -56.96528 | 2025-09-10 05:06:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 3ca2032d-0603-3da2-850d-22c06890c686 | -15.60899 | -52.75311 | 2025-09-10 05:06:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f40ae44b-a523-37b6-ba6a-b400593da25c | -18.1368 | -51.72762 | 2025-09-10 05:06:00 | NOAA-20 | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 0be0b662-97fa-3dbc-ba20-1f0314d8f679 | -15.80601 | -52.24664 | 2025-09-10 05:06:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |


[Clique aqui para ver as próximas entradas](README101.md)
