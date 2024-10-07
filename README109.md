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

## Dados Diários - Página 109

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| b8e04d79-22f3-3feb-9f47-bfb455475212 | -18.70341 | -57.26252 | 2024-10-07 04:55:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.5 |
| c7b31ae6-c567-3c9e-8328-c88ec54f9012 | -23.04784 | -49.8415 | 2024-10-07 04:57:00 | AQUA_M-M | OURINHOS | SÃO PAULO | Brasil | 3534708 | 35 | 33 | nan | nan | nan | Mata Atlântica | 29.4 |
| d74a01c9-33ed-3c12-a637-4a557c3a1692 | -23.04713 | -49.84641 | 2024-10-07 04:57:00 | AQUA_M-M | OURINHOS | SÃO PAULO | Brasil | 3534708 | 35 | 33 | nan | nan | nan | Mata Atlântica | 30.7 |
| e58bd8f3-c51f-371a-9e7a-9e6db114adbf | -25.62133 | -51.42761 | 2024-10-07 04:57:00 | NOAA-21 | GUARAPUAVA | PARANÁ | Brasil | 4109401 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 639edcc6-ed8e-37bd-9983-c64c55966291 | -25.32201 | -54.05496 | 2024-10-07 04:57:00 | NOAA-21 | MEDIANEIRA | PARANÁ | Brasil | 4115804 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| b0f2c5ed-d323-3ca4-a314-afa04cea7478 | -25.01605 | -54.07746 | 2024-10-07 04:57:00 | NOAA-21 | DIAMANTE D'OESTE | PARANÁ | Brasil | 4107157 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 3e66f09a-d8cf-319c-9d74-a21db9effed5 | -25.01546 | -54.08172 | 2024-10-07 04:57:00 | NOAA-21 | DIAMANTE D'OESTE | PARANÁ | Brasil | 4107157 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 1e1b2eb2-475c-347b-a375-9bec64d2d9bc | -23.89543 | -54.21842 | 2024-10-07 04:57:00 | NOAA-21 | ELDORADO | MATO GROSSO DO SUL | Brasil | 5003751 | 50 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| f2c563ba-3f1f-3687-a769-cd2a7389b18b | -23.89484 | -54.2226 | 2024-10-07 04:57:00 | NOAA-21 | ELDORADO | MATO GROSSO DO SUL | Brasil | 5003751 | 50 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 4ed7aa98-5ee5-3178-8342-006e96c54d29 | -23.89136 | -54.22204 | 2024-10-07 04:57:00 | NOAA-21 | ELDORADO | MATO GROSSO DO SUL | Brasil | 5003751 | 50 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| f013c501-11c9-3edb-a2fd-2ea05ebc875b | -23.9159 | -55.4127 | 2024-10-07 04:57:00 | NOAA-21 | PARANHOS | MATO GROSSO DO SUL | Brasil | 5006358 | 50 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 73a4e496-2090-3d83-b05e-7456881b1d0c | -20.44 | -47.71 | 2024-10-07 05:03:26 | MSG-03 | ITUVERAVA | SÃO PAULO | Brasil | 3524105 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 2a928ca9-4071-3e7b-af3d-72028fecc5b3 | -3.9387 | -46.44552 | 2024-10-07 05:14:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 8063659d-6ccc-34cf-ae18-bf39f73b88d9 | -3.93798 | -46.45068 | 2024-10-07 05:14:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 46bdacb8-1982-33d5-b968-3fce83cd3683 | -3.93797 | -46.44478 | 2024-10-07 05:14:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 1b83b37a-3c80-3a40-92b3-626af0ce262e | -3.12403 | -48.60871 | 2024-10-07 05:14:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b1c634b6-9e5a-3287-928b-d64c42da9d46 | -3.93721 | -46.44994 | 2024-10-07 05:14:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 59a10b68-82ad-3b50-a9ae-5bc8c9edf082 | -3.93235 | -46.43853 | 2024-10-07 05:14:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e3071137-3e5b-3dba-89be-71789f47b7f5 | -3.93157 | -46.44381 | 2024-10-07 05:14:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| a2e1238b-ea8e-3fa7-821e-53d0dbd23260 | -3.85048 | -46.46348 | 2024-10-07 05:14:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 1bbc72bf-4c67-30f0-92fe-32fbab685375 | -3.50045 | -48.90272 | 2024-10-07 05:14:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 36610138-34f0-3d3e-ab24-f314c1924182 | -3.49553 | -48.8986 | 2024-10-07 05:14:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f5b30fe9-b98e-392a-a938-5db52b41b098 | -3.46347 | -47.66162 | 2024-10-07 05:14:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 687a13a9-5f08-3566-ad61-4a24a916155f | -3.46283 | -47.66592 | 2024-10-07 05:14:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 5cf1a109-e5de-3b76-b16b-02768f71f331 | -3.22277 | -48.92474 | 2024-10-07 05:14:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 525c1fbc-eccb-3087-89d4-e299c3d4322e | -3.22227 | -48.92812 | 2024-10-07 05:14:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b7ed367b-f176-3c88-966b-317f7dee3ae2 | -3.12456 | -48.604 | 2024-10-07 05:14:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| ffa42b23-84ba-3d3c-96e4-dcb7970ce075 | -3.12455 | -48.60518 | 2024-10-07 05:14:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f060adc7-5dee-3892-a67f-3e51c436b431 | -3.12402 | -48.60752 | 2024-10-07 05:14:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 820a60ec-0924-330f-ab59-823a6cd83f71 | -3.12352 | -48.61225 | 2024-10-07 05:14:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| d57fb635-3f18-33b1-aa89-15e103c0b4d0 | -3.12348 | -48.61105 | 2024-10-07 05:14:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 3831a2ad-d289-307a-be2f-b3702e3fe11b | -3.12294 | -48.61457 | 2024-10-07 05:14:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 4a9fa2ed-44e8-33bf-af93-2c1dd5c12bd5 | -3.11853 | -48.60791 | 2024-10-07 05:14:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 7ded26bd-99de-3a2d-b8a4-b855a89320b6 | -3.11852 | -48.60673 | 2024-10-07 05:14:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| f4d33231-0908-39f9-82dd-8da7122160dd | -3.11798 | -48.61026 | 2024-10-07 05:14:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d34127f8-7bb1-3bdd-9e43-c136d6257042 | -2.93941 | -47.84306 | 2024-10-07 05:14:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| c61bd6c5-b6c3-310d-b657-aeb436fc9aa1 | -2.93363 | -47.84221 | 2024-10-07 05:14:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e1cd8183-1268-3f1e-bbd9-90cf0e62a6bd | -2.74082 | -48.6923 | 2024-10-07 05:14:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 4b33e347-1c07-3f32-81a8-b5d9ccab4657 | -2.44036 | -48.66809 | 2024-10-07 05:14:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0bf0b748-af86-337a-9507-3e25ded7a8f8 | -4.39149 | -48.69197 | 2024-10-07 05:14:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| ce4207c0-9795-3f17-a008-5b6d6e0223b8 | -4.39092 | -48.69584 | 2024-10-07 05:14:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| c872e2e1-45a9-3e20-896a-fb396ba67317 | -4.39052 | -48.6907 | 2024-10-07 05:14:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| ce38927e-03bf-301c-b1f4-99cf2d784fa4 | -4.38996 | -48.6946 | 2024-10-07 05:14:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 94c2c07a-20cb-39d3-9721-14e5812ab7cb | -4.3848 | -48.69872 | 2024-10-07 05:14:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 9e57b72f-0f14-3e01-a3d7-ac10c6019570 | -4.38385 | -48.69757 | 2024-10-07 05:14:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 8b099364-7165-30a7-ac04-ffeaae62052a | -4.38334 | -48.70118 | 2024-10-07 05:14:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 1518273e-4d05-30f3-a290-44a0230cb6b4 | -4.37921 | -48.69802 | 2024-10-07 05:14:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 20a865cd-8d2c-352d-b16b-0c027ceb2a3e | -4.16757 | -48.61095 | 2024-10-07 05:14:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 87b80c7c-ddf4-380f-913b-29f034f68d1f | -4.16617 | -48.60968 | 2024-10-07 05:14:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7b4ebb28-8740-3ef5-98d3-286f7dd0db7c | -4.16565 | -48.6134 | 2024-10-07 05:14:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 38dce4e8-4445-3b29-aca0-c4544708b9ae | -4.16511 | -48.6172 | 2024-10-07 05:14:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 113be0e7-3fad-30f4-a4d0-8a68c413eb44 | -4.162 | -48.61004 | 2024-10-07 05:14:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f8872acf-249e-37fb-8112-d751bffe4e28 | -4.16145 | -48.61374 | 2024-10-07 05:14:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c9e5bbea-cdfc-3f40-b27c-4d24568fd3cf | -4.16089 | -48.61749 | 2024-10-07 05:14:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| af0cf265-bfaf-3a82-81fe-fa58ac954c36 | -4.15696 | -48.60555 | 2024-10-07 05:14:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a962b208-a77d-3b2c-aa3b-bef4d79fe466 | -4.09651 | -48.25724 | 2024-10-07 05:14:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 7de4ef05-7c3a-377a-b994-d70df4c5ba1a | -4.09594 | -48.26108 | 2024-10-07 05:14:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 096d0f7d-c0f1-3e4a-9be5-987f805dccb0 | -4.09537 | -48.26494 | 2024-10-07 05:14:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| bf275cb1-5244-3104-b737-f0d4b5aff70f | -4.0948 | -48.26881 | 2024-10-07 05:14:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 2acfdba0-cb44-3c93-b896-1be6ea9cf47b | -3.91264 | -48.34822 | 2024-10-07 05:14:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6917d7f0-31a8-377d-aa5b-9a9fac58b514 | -3.91096 | -48.34587 | 2024-10-07 05:14:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f8592436-6fd2-3d6a-8020-32817c29a6f5 | -3.9104 | -48.3496 | 2024-10-07 05:14:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f92790a7-c6e6-3c26-afdd-37dd8d11126d | -3.90748 | -48.34389 | 2024-10-07 05:14:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 46e36a61-7ed6-371c-8f67-295c6f1d859f | -3.90694 | -48.34764 | 2024-10-07 05:14:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f8dc34c4-e3d9-33b4-9957-b4506ff292e1 | -3.90642 | -48.3513 | 2024-10-07 05:14:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7c33ace7-e588-3e28-b158-72c87a872d84 | -3.90525 | -48.34533 | 2024-10-07 05:14:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0241b7f5-6193-3c24-9441-0778ceb07b15 | -3.9047 | -48.34901 | 2024-10-07 05:14:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a31ed2a8-e525-39fe-afe3-28bd070cc3ce | -3.90415 | -48.35264 | 2024-10-07 05:14:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 01a55e98-f073-3d4e-a197-7ab3a4aa7b02 | -0.26826 | -48.73933 | 2024-10-07 05:14:00 | NPP-375D | SOURE | PARÁ | Brasil | 1507904 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| ea3b5c69-fb2b-316a-bc62-034d3b6ce9c1 | -3.50717 | -50.27217 | 2024-10-07 05:14:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 43279079-ab1b-3918-b674-4acd30d47dbf | -3.50591 | -50.27092 | 2024-10-07 05:14:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 20a4f863-6a62-3635-9bb2-efd0b71dfffc | -3.50507 | -50.27643 | 2024-10-07 05:14:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 4e0583f0-577e-3264-ae62-eb50478758dc | -3.50223 | -50.27142 | 2024-10-07 05:14:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 12fb59dc-1231-3bed-be12-02a4d9960a3c | -3.50097 | -50.27021 | 2024-10-07 05:14:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| fcbb6df3-0f7e-3eb0-8fcd-7d74e8d3d8e4 | -3.50013 | -50.27572 | 2024-10-07 05:14:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 1454c736-c4e4-3f4a-9c95-559638e5ee0d | -3.35519 | -49.91602 | 2024-10-07 05:14:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| eefc40ff-349b-39a3-8e8c-0ffe2968add3 | -3.32828 | -49.15561 | 2024-10-07 05:14:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c564d229-303f-3e6b-bd9d-19d2a6f4beec | -3.32346 | -49.15151 | 2024-10-07 05:14:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 359ce138-eaf1-3711-9039-d4c8c2230044 | -3.32297 | -49.15477 | 2024-10-07 05:14:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 5b663cb4-1a30-3a21-b8b7-61dcbc6fadef | -3.29205 | -49.14344 | 2024-10-07 05:14:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 3604f20d-5373-301a-8037-c507caae8c6d | -3.29157 | -49.14668 | 2024-10-07 05:14:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7c7cce5a-005e-3e81-8b05-43403004baa0 | -3.26739 | -49.12625 | 2024-10-07 05:14:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 1f22e39c-12c8-3398-ad5a-7b841e88916c | -3.2669 | -49.12961 | 2024-10-07 05:14:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 9d2fbf7e-8df7-325e-a1a9-829a57a2d58e | -3.26641 | -49.13291 | 2024-10-07 05:14:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 065d3f9e-fb01-3e63-b16f-8db3675eacfb | -3.26207 | -49.1254 | 2024-10-07 05:14:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| e3aecde5-863a-3161-8a77-b546e2cecf78 | -2.79167 | -49.52686 | 2024-10-07 05:14:00 | NPP-375D | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 71f4ea71-1658-3794-9e06-c881c960b3af | -2.78653 | -49.52609 | 2024-10-07 05:14:00 | NPP-375D | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 24a57f69-44cd-343a-b856-fb788f352170 | -2.74707 | -49.52898 | 2024-10-07 05:14:00 | NPP-375D | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 6d9d70db-b1a7-3a7a-bbb5-d0516a4056e9 | -2.74661 | -49.53199 | 2024-10-07 05:14:00 | NPP-375D | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 248cf5e7-e735-3a36-a964-7bf3cce73168 | -2.5349 | -49.0218 | 2024-10-07 05:14:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 9825d0f9-8cc5-38ff-81da-2cdcbfceeabe | -2.52959 | -49.02104 | 2024-10-07 05:14:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 01d8a746-9ae9-32f3-a34e-e9985487c413 | -3.68232 | -50.25409 | 2024-10-07 05:14:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c8071f35-c10d-38b9-a27f-6a58b0191b52 | 1.80848 | -50.80837 | 2024-10-07 05:14:00 | NPP-375D | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 3bff7efd-a048-39ae-9074-61d186ad89cf | -2.12098 | -50.8051 | 2024-10-07 05:14:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e5708030-1685-39b2-908d-f9de8cf637e1 | -0.03551 | -51.6627 | 2024-10-07 05:14:00 | NPP-375D | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 7cb16b25-7b92-398b-b884-26a3d5826e61 | -3.32836 | -53.38804 | 2024-10-07 05:14:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| a6eb06fb-ab49-3ce4-95c0-d7a5ea59c992 | -3.32758 | -53.39312 | 2024-10-07 05:14:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 606479a7-002e-3c6c-b92a-50a30f27a885 | -3.32439 | -53.38739 | 2024-10-07 05:14:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| c0d671c9-f482-3174-9f4f-77b82c61548a | -3.32361 | -53.39247 | 2024-10-07 05:14:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 2060400e-3c14-37a6-8d15-57e38aab0464 | -3.25682 | -52.8488 | 2024-10-07 05:14:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |


[Clique aqui para ver as próximas entradas](README110.md)
