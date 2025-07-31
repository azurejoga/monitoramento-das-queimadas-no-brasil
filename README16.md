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

## Dados Diários - Página 16

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 4e9d731b-3891-34db-bc20-40cf26cdac78 | -6.66148 | -56.4007 | 2025-07-31 05:25:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| da6c6476-5faa-39cd-af98-ff283b7ae3cf | -6.6692 | -56.40196 | 2025-07-31 05:25:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 7.8 |
| a769a137-584e-3656-84f6-198d2b2ce1b6 | -12.63548 | -48.09045 | 2025-07-31 05:25:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.8 |
| fba53f5e-b5e6-3ab1-8719-ffbafa20b295 | -6.50923 | -56.21124 | 2025-07-31 05:25:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c915cd3b-c7ef-33c8-b48e-d19ec3ea9a22 | -6.68031 | -58.86528 | 2025-07-31 05:25:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 5f4017c2-c8b4-329b-85dc-de5aa722daaa | -6.39522 | -53.31867 | 2025-07-31 05:25:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| cd857ef7-dff3-3e0d-a28d-082adbd3960b | -12.6349 | -48.09595 | 2025-07-31 05:25:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 0eb66c56-ab70-30c3-8065-54117b0c8d6f | -6.5604 | -56.18849 | 2025-07-31 05:25:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| d179502f-6ba5-31ee-8de1-d2e4b95d554a | -6.37885 | -53.3317 | 2025-07-31 05:25:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 78fb0725-a2d0-30c8-b56e-568a6dff3d28 | -6.51526 | -56.19693 | 2025-07-31 05:25:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 83902e6d-a92a-3342-9a13-d8b16e270338 | -7.7432 | -51.09212 | 2025-07-31 05:25:00 | NOAA-21 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 754725f0-f6a4-3ae5-93bc-6947eaacac72 | -6.52093 | -56.21304 | 2025-07-31 05:25:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 96f4997a-bc80-3af2-84b0-2769a7210659 | -6.37486 | -53.32587 | 2025-07-31 05:25:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 64d643cb-575f-3e6b-b70c-ef5ef8a851b2 | -6.50852 | -56.21621 | 2025-07-31 05:25:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 3d682361-fc2d-3f36-9ddf-d329a1b6433b | -6.38976 | -53.323 | 2025-07-31 05:25:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 2d7cca44-6b21-38e8-99e6-9f6e0dbd6341 | -6.52874 | -56.21417 | 2025-07-31 05:25:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c96cacf3-381a-3dc2-ac6c-cb2e5bc26f11 | -6.50894 | -56.20951 | 2025-07-31 05:25:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| b3c598a9-a799-376a-a27f-75c927b3bab8 | -6.39725 | -53.31447 | 2025-07-31 05:25:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 49eb7b90-dd05-3b05-aeb8-06854446c858 | -6.38431 | -53.3273 | 2025-07-31 05:25:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| a5177ba8-273d-373e-9a78-67ae5a5e0071 | -6.66777 | -56.41161 | 2025-07-31 05:25:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 986f47a6-bd1e-38be-b23d-df4337d089ec | -6.54508 | -56.21149 | 2025-07-31 05:25:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 9cca3dd6-158e-3d77-90cc-f4cd8c359654 | -6.4987 | -56.19793 | 2025-07-31 05:25:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 057a3c08-600a-336e-9dcc-38d8dee7b3a0 | -6.6576 | -56.40024 | 2025-07-31 05:25:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 49f6d926-c3f6-35d4-b231-fff30229bcfb | -5.87727 | -57.75074 | 2025-07-31 05:25:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 042843ef-f489-348e-a62c-70a37064d46f | -6.51135 | -56.19634 | 2025-07-31 05:25:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 472f6d70-7774-3628-8a2d-0d37eae6ccd6 | -6.54331 | -56.19616 | 2025-07-31 05:25:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 3bf33e01-1c33-3277-b601-926fe87d8118 | -6.55577 | -56.19288 | 2025-07-31 05:25:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| bd245196-6fc3-3c92-84b8-b5552f20f547 | -6.40917 | -53.36777 | 2025-07-31 05:25:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 9f765e09-128b-3982-afae-ca17844e408f | -6.52454 | -56.21186 | 2025-07-31 05:25:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| c59977a2-431a-34da-b9a6-563a76405005 | -21.97538 | -57.59256 | 2025-07-31 05:27:00 | NOAA-21 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 3.1 |
| a1abec74-cb6e-3f10-b120-509db0fbd3f7 | -22.21781 | -56.19611 | 2025-07-31 05:27:00 | NOAA-21 | ANTÔNIO JOÃO | MATO GROSSO DO SUL | Brasil | 5000906 | 50 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 5951d7f6-1f7b-38be-acd2-689a317eef7e | -21.61114 | -57.5774 | 2025-07-31 05:27:00 | NOAA-21 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 0.8 |
| b3d9e6ee-f69c-33a8-a5d4-a635b925c77d | -20.19664 | -50.51096 | 2025-07-31 05:27:00 | NOAA-21 | VITÓRIA BRASIL | SÃO PAULO | Brasil | 3556958 | 35 | 33 | nan | nan | nan | Mata Atlântica | 19.0 |
| aeea4e5d-7213-3578-93e0-17d4e6f89d1f | -21.86881 | -56.73624 | 2025-07-31 05:27:00 | NOAA-21 | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 3ce95fcb-cc48-337c-82fe-952a76406570 | -21.97979 | -57.59327 | 2025-07-31 05:27:00 | NOAA-21 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a5eb047c-3ad2-3298-a7ed-dc2d95e49aa9 | -21.86825 | -56.7415 | 2025-07-31 05:27:00 | NOAA-21 | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 79d2c1e9-f125-3536-aa93-896bbb0eeb1f | -20.19399 | -50.51209 | 2025-07-31 05:27:00 | NOAA-21 | VITÓRIA BRASIL | SÃO PAULO | Brasil | 3556958 | 35 | 33 | nan | nan | nan | Mata Atlântica | 21.6 |
| 97beb70f-a906-31ce-8778-9884511de3d9 | -20.19711 | -50.5047 | 2025-07-31 05:27:00 | NOAA-21 | VITÓRIA BRASIL | SÃO PAULO | Brasil | 3556958 | 35 | 33 | nan | nan | nan | Mata Atlântica | 19.0 |
| c10c81c0-a957-34d5-8047-7cee65e78010 | -20.1945 | -50.50591 | 2025-07-31 05:27:00 | NOAA-21 | VITÓRIA BRASIL | SÃO PAULO | Brasil | 3556958 | 35 | 33 | nan | nan | nan | Mata Atlântica | 28.0 |
| 373f73c2-b1f3-30b2-b4e9-71af2b2a65c0 | -21.61661 | -57.56882 | 2025-07-31 05:27:00 | NOAA-21 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c2447e47-6baf-36d1-abe1-eac9ad110f5f | -21.32866 | -55.63654 | 2025-07-31 05:27:00 | NOAA-21 | MARACAJU | MATO GROSSO DO SUL | Brasil | 5005400 | 50 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 1b232034-730e-3bf2-8c22-16a640fac5e5 | -10.0843 | -53.8712 | 2025-07-31 05:30:00 | GOES-19 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 56.3 |
| e4ee5a0d-bbf5-3499-a4e0-e2cda6b69a0b | -6.6725 | -56.4029 | 2025-07-31 05:30:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 51.2 |
| 54a2083d-49bb-3a23-a4f8-aac7294e3ffb | -6.6725 | -56.4029 | 2025-07-31 05:40:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 49.3 |
| 0a503d26-d30d-340e-bf9c-8a2c6a2fd38c | 4.30912 | -60.79771 | 2025-07-31 05:48:00 | NPP-375D | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 923aef55-e27f-3971-8f35-874fcfb31a76 | -8.07 | -43.1216 | 2025-07-31 05:50:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 68.3 |
| 1cb85032-c14b-398f-9a58-805e37d4861e | -20.2068 | -50.5059 | 2025-07-31 05:50:00 | GOES-19 | VITÓRIA BRASIL | SÃO PAULO | Brasil | 3556958 | 35 | 33 | nan | nan | nan | Mata Atlântica | 44.0 |
| 0a0153cc-a334-39b5-85b6-434feb8055d2 | -6.6725 | -56.4029 | 2025-07-31 05:50:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 46.0 |
| 47e91ca2-07b6-3c88-b560-4e28de9da80f | -8.0513 | -43.1001 | 2025-07-31 05:50:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 113.0 |
| b37d06b3-d8dc-3dcc-96cb-665c016fc70b | -8.0703 | -43.0981 | 2025-07-31 05:50:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 77.7 |
| dfa2c67b-f9c9-33b8-87a1-34197cdc136a | -8.051 | -43.1237 | 2025-07-31 05:50:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 99.7 |
| f430b7b0-0d9c-3540-9659-a49df62caca7 | -6.6276 | -59.98318 | 2025-07-31 05:50:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 75562cad-d1b8-341b-8b10-5869ae7c3e80 | -6.55755 | -56.1919 | 2025-07-31 05:50:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 8ce8a93e-d045-3fc8-9127-4fb1ab25d7d5 | -6.66048 | -56.39479 | 2025-07-31 05:50:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 16060df1-015b-378e-a615-a59f57ef34ad | -6.61839 | -59.982 | 2025-07-31 05:50:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 60ef0446-1b51-33ac-b607-1507eaa9e5b8 | -6.6527 | -58.82576 | 2025-07-31 05:50:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| dcac228f-bae9-3561-b6b3-cd885eceda5d | -6.54508 | -56.19475 | 2025-07-31 05:50:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 7004bf94-7df1-313c-a4f8-c46fddbe4888 | -7.89799 | -61.521 | 2025-07-31 05:50:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 0.3 |
| 07d2b851-68d8-302b-91b7-1b0f1a27ebf1 | -6.6716 | -56.40079 | 2025-07-31 05:50:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 5902850c-67e7-30b1-a44d-3507121cfb2a | -6.61907 | -59.97737 | 2025-07-31 05:50:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 125127d8-e4fd-38bb-a4b1-d499752aa8ed | -6.56291 | -56.19696 | 2025-07-31 05:50:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 1da41871-73a1-359e-9b08-16270f4161d6 | -6.53441 | -56.20694 | 2025-07-31 05:50:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 096bef81-6f81-3b6f-bf12-5cd5f54e3f4f | -6.50597 | -56.19439 | 2025-07-31 05:50:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 77e0646e-2b4d-3128-b82b-e3e0ccf96183 | -6.39244 | -53.3222 | 2025-07-31 05:50:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 788fa6f6-07b9-3e53-a944-3b2c4b357112 | -6.66102 | -56.39085 | 2025-07-31 05:50:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 25ddd7dd-61ee-3498-a45c-67db1abcbb2a | -6.52082 | -56.19555 | 2025-07-31 05:50:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| a9c470d2-2ecd-3309-82f8-d8bdd882b044 | -6.6768 | -56.40645 | 2025-07-31 05:50:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| f4b2d75d-73bb-3567-809a-fdb4cf7a3646 | -6.6675 | -56.38713 | 2025-07-31 05:50:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a2ff3c1d-f0fb-3b0b-a55b-2c08da21945a | -6.81277 | -59.27501 | 2025-07-31 05:50:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c67efb86-5a89-3d26-86b6-7337fe1125bc | -6.50478 | -56.20292 | 2025-07-31 05:50:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| db75ddb9-0074-3b5a-91ce-01fc5a9863a6 | -6.52502 | -56.20938 | 2025-07-31 05:50:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 59ec44b8-9f57-3171-be38-9a00fd6dba0b | -6.65992 | -56.39891 | 2025-07-31 05:50:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 25eb302b-5720-3ae1-9f46-3c51c57bc842 | -6.52254 | -56.20544 | 2025-07-31 05:50:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 3f5d0679-0ef5-332e-8aad-2b41b588eefa | -6.54396 | -56.20309 | 2025-07-31 05:50:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0fdc80eb-2976-37ae-8a0c-82104f6c74f2 | -6.62299 | -59.98264 | 2025-07-31 05:50:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 08fb276d-3a80-36bc-8b7f-9976a0df9f2f | -9.45742 | -57.84382 | 2025-07-31 05:50:00 | NPP-375D | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 117804af-555d-307f-b658-7515140d8cac | -6.52315 | -56.20114 | 2025-07-31 05:50:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| e49d9771-8d31-3e45-a1ca-7c84e30433aa | -6.37463 | -53.33155 | 2025-07-31 05:50:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| e1e9ec88-35eb-344f-9539-070a2827ba65 | -6.53209 | -56.2016 | 2025-07-31 05:50:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 47f77907-8568-37e0-9f37-eb7ea38e36bf | -6.51844 | -56.19159 | 2025-07-31 05:50:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 20eebb4b-33e4-3994-ad72-dbe311b8623c | -6.65455 | -56.39445 | 2025-07-31 05:50:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| abcf9be4-a19e-328c-85e4-cd7a268d22e9 | -6.50004 | -56.19361 | 2025-07-31 05:50:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 92c474a0-d933-326e-9692-21ecd83c5ffa | -6.52375 | -56.19682 | 2025-07-31 05:50:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 49ec1c6b-e868-3889-8dab-af53f0ce844a | -6.66465 | -56.40796 | 2025-07-31 05:50:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 682817fc-9baa-3771-9c02-6b8a71fa5425 | -6.678 | -56.39772 | 2025-07-31 05:50:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| c587fa18-b8b8-3218-8571-671279fffab1 | -6.52139 | -56.1912 | 2025-07-31 05:50:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| ea83bad6-e1f7-3b65-9bbf-5158642ebf2c | -6.5191 | -56.20852 | 2025-07-31 05:50:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 06fe70ea-ef33-396c-8bc2-b629e1391589 | -6.51603 | -56.20882 | 2025-07-31 05:50:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 74917d5f-09d4-37e4-8c7c-d33272f12c9a | -6.51132 | -56.19934 | 2025-07-31 05:50:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 2db39921-b49b-3432-a8a4-0b1575772194 | -6.66156 | -56.38684 | 2025-07-31 05:50:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 693099a8-7f59-38e8-9e4a-7e10c6d325d3 | -6.52907 | -56.202 | 2025-07-31 05:50:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 3d9a54ce-b5f5-3b14-9b31-c724418b74bc | -6.57002 | -56.18911 | 2025-07-31 05:50:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d91f6434-ef1b-370b-aa11-a9b1d81b9da7 | -6.51967 | -56.20421 | 2025-07-31 05:50:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 7c2509a1-7f62-3d0c-b3be-c75b21ac1bfa | -6.51543 | -56.21313 | 2025-07-31 05:50:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4bdfcab0-fc96-3809-ace8-db8090bcbed5 | -6.50419 | -56.20722 | 2025-07-31 05:50:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 28bb6d04-a1ef-35ea-9904-8322cde7f120 | -6.52787 | -56.1879 | 2025-07-31 05:50:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 2eafabc6-d497-3585-8e56-b8bc934b4f20 | -6.38449 | -53.32779 | 2025-07-31 05:50:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| ae9d98b9-8d7e-3a89-9193-344895845937 | -6.38254 | -53.3258 | 2025-07-31 05:50:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b6ac2b2f-579c-3b7c-b792-b0b16c30b453 | -6.55814 | -56.18756 | 2025-07-31 05:50:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 45657ea1-65e4-31a1-85ad-5fce2dade8e3 | -6.54035 | -56.20765 | 2025-07-31 05:50:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |


[Clique aqui para ver as próximas entradas](README17.md)
