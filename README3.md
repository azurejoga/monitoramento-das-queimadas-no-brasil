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

## Dados Diários - Página 3

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 62f207cc-f384-3db3-90f0-1be6a98fa316 | -13.04949 | -53.72562 | 2025-05-02 04:19:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 76a14fc2-87a7-32c8-868a-d1c9210b2fbd | -5.16031 | -45.10579 | 2025-05-02 04:19:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 6c134430-6b4b-3357-b7f9-bc180c5ce1b3 | -17.69403 | -54.34473 | 2025-05-02 04:21:00 | NOAA-20 | SONORA | MATO GROSSO DO SUL | Brasil | 5007935 | 50 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b9d7c1e5-7092-3723-8afb-eb5ef8a96e12 | -21.46755 | -57.15964 | 2025-05-02 04:21:00 | NOAA-20 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 51c67567-8ad6-3714-8e93-f7ba4a41da68 | -23.14517 | -54.89996 | 2025-05-02 04:21:00 | NOAA-20 | AMAMBAI | MATO GROSSO DO SUL | Brasil | 5000609 | 50 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 9563c70a-36b2-3a8f-aee7-4a97b0bdb9da | -23.59211 | -47.4389 | 2025-05-02 04:21:00 | NOAA-20 | VOTORANTIM | SÃO PAULO | Brasil | 3557006 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| b2c11122-634b-3c80-8909-91dee278e256 | -23.6118 | -49.00673 | 2025-05-02 04:21:00 | NOAA-20 | ITAÍ | SÃO PAULO | Brasil | 3521804 | 35 | 33 | nan | nan | nan | Cerrado | 0.7 |
| bc970938-9979-31e6-a4f8-8e7f63a69a26 | -16.3131 | -53.81962 | 2025-05-02 04:21:00 | NOAA-20 | GUIRATINGA | MATO GROSSO | Brasil | 5104203 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 3218a61d-1f90-320d-9264-dc73dd6c40ac | -20.34628 | -45.72244 | 2025-05-02 04:21:00 | NOAA-20 | PAINS | MINAS GERAIS | Brasil | 3146503 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 0ba157c5-69b2-33d4-bf78-fa673a023f7c | -22.24768 | -52.98185 | 2025-05-02 04:21:00 | NOAA-20 | ANAURILÂNDIA | MATO GROSSO DO SUL | Brasil | 5000807 | 50 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 20688bbe-cb70-344c-8a48-59f8e740ac5c | -17.62181 | -50.91662 | 2025-05-02 04:21:00 | NOAA-20 | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 6f6add47-6475-34c9-9e26-3e0af0937775 | -16.31576 | -53.83 | 2025-05-02 04:21:00 | NOAA-20 | GUIRATINGA | MATO GROSSO | Brasil | 5104203 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 80b73ba9-770b-33f8-8d45-5696d2b0fcbb | -23.16729 | -54.65194 | 2025-05-02 04:21:00 | NOAA-20 | AMAMBAI | MATO GROSSO DO SUL | Brasil | 5000609 | 50 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| eba910fd-9e5e-3b1e-bca2-2b5c47839bbf | -23.14458 | -54.8987 | 2025-05-02 04:21:00 | NOAA-20 | AMAMBAI | MATO GROSSO DO SUL | Brasil | 5000609 | 50 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| f8db3ac9-68b5-3fd5-885d-66e5567181a7 | -20.15094 | -46.91238 | 2025-05-02 04:21:00 | NOAA-20 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 24e302f1-48a0-36c0-b5d3-f2ea0da77a71 | -22.53881 | -48.81204 | 2025-05-02 04:21:00 | NOAA-20 | MACATUBA | SÃO PAULO | Brasil | 3528007 | 35 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 71a23cb6-6c4d-3aa3-b721-b9eaf3765162 | -21.12981 | -47.79987 | 2025-05-02 04:21:00 | NOAA-20 | RIBEIRÃO PRETO | SÃO PAULO | Brasil | 3543402 | 35 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 9cf984be-9acd-3bb6-a16d-f251cd2c6d91 | -21.17898 | -43.98163 | 2025-05-02 04:21:00 | NOAA-20 | BARROSO | MINAS GERAIS | Brasil | 3105905 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| e076087a-f804-306c-803e-ba813481e92b | -23.63068 | -46.42565 | 2025-05-02 04:21:00 | NOAA-20 | SÃO PAULO | SÃO PAULO | Brasil | 3550308 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 87997fdf-5c14-317a-9c1b-40a3268efb54 | -21.47253 | -57.16096 | 2025-05-02 04:21:00 | NOAA-20 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 4a6618b8-565e-3f8f-99ee-8a58869ac5e7 | -17.61813 | -50.91595 | 2025-05-02 04:21:00 | NOAA-20 | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f637a967-ca5a-3f51-bcff-e65db51a2ec0 | -16.31221 | -53.82424 | 2025-05-02 04:21:00 | NOAA-20 | GUIRATINGA | MATO GROSSO | Brasil | 5104203 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ec9f6c70-e64a-3cd4-8940-a02c9ccddf5b | -18.14571 | -47.79916 | 2025-05-02 04:21:00 | NOAA-20 | OUVIDOR | GOIÁS | Brasil | 5215504 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| ae1c874f-e3fc-303f-832b-4b41f76a8735 | -19.96865 | -44.21545 | 2025-05-02 04:21:00 | NOAA-20 | BETIM | MINAS GERAIS | Brasil | 3106705 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 61805248-394a-3109-9d64-aef4c963c39d | -20.99513 | -51.79445 | 2025-05-02 04:21:00 | NOAA-20 | TRÊS LAGOAS | MATO GROSSO DO SUL | Brasil | 5008305 | 50 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| ce9e2a50-7c10-34f4-b34a-1d2fde404e86 | -23.98245 | -48.91889 | 2025-05-02 04:21:00 | NOAA-20 | ITAPEVA | SÃO PAULO | Brasil | 3522406 | 35 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 87bd62c6-b974-3ce8-87d4-abf965df91ae | -17.76593 | -52.44502 | 2025-05-02 04:21:00 | NOAA-20 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 3f1cc1f0-2495-3f39-ba0b-cbd779791e2c | -17.60691 | -49.59717 | 2025-05-02 04:21:00 | NOAA-20 | PONTALINA | GOIÁS | Brasil | 5217708 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 0f89ed02-3735-30c8-bf36-341b2c3e4597 | -22.67788 | -49.81114 | 2025-05-02 04:21:00 | NOAA-20 | SÃO PEDRO DO TURVO | SÃO PAULO | Brasil | 3550506 | 35 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 29bc1f50-0eb2-3ae9-a02a-31264b6a15a4 | -23.40615 | -46.55732 | 2025-05-02 04:21:00 | NOAA-20 | SÃO PAULO | SÃO PAULO | Brasil | 3550308 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 13d1652f-cc13-3cf8-8264-70949f741236 | -21.19478 | -44.93566 | 2025-05-02 04:21:00 | NOAA-20 | IJACI | MINAS GERAIS | Brasil | 3130408 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| d934f40c-5e63-304e-95fc-75a4c2de205d | -21.02706 | -55.6492 | 2025-05-02 04:21:00 | NOAA-20 | NIOAQUE | MATO GROSSO DO SUL | Brasil | 5005806 | 50 | 33 | nan | nan | nan | Cerrado | 1.9 |
| f487b588-bce5-3aab-8a52-bd99a36cd179 | -23.60849 | -49.0061 | 2025-05-02 04:21:00 | NOAA-20 | ITAÍ | SÃO PAULO | Brasil | 3521804 | 35 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 3f1c4e2c-b104-34fb-a766-55c37ea49b0c | -21.0289 | -55.64706 | 2025-05-02 04:21:00 | NOAA-20 | NIOAQUE | MATO GROSSO DO SUL | Brasil | 5005806 | 50 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f2889752-92b9-35b6-916d-92b44d8e9684 | -17.69267 | -54.3474 | 2025-05-02 04:21:00 | NOAA-20 | SONORA | MATO GROSSO DO SUL | Brasil | 5007935 | 50 | 33 | nan | nan | nan | Cerrado | 0.9 |
| b313a71d-004d-3514-b2b6-4ee1c53bcf6f | -23.60789 | -49.00988 | 2025-05-02 04:21:00 | NOAA-20 | ITAÍ | SÃO PAULO | Brasil | 3521804 | 35 | 33 | nan | nan | nan | Cerrado | 0.5 |
| e5543e95-53bb-336d-b4f8-8025953541e7 | -19.38014 | -53.20934 | 2025-05-02 04:21:00 | NOAA-20 | PARAÍSO DAS ÁGUAS | MATO GROSSO DO SUL | Brasil | 5006275 | 50 | 33 | nan | nan | nan | Cerrado | 1.0 |
| fcdd8334-1186-3eb6-aa12-7fa5c6da63a3 | -20.41601 | -43.55355 | 2025-05-02 04:21:00 | NOAA-20 | OURO PRETO | MINAS GERAIS | Brasil | 3146107 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| 3c695a1b-d254-3243-98da-7db55df4ef2d | -20.47847 | -53.67622 | 2025-05-02 04:21:00 | NOAA-20 | RIBAS DO RIO PARDO | MATO GROSSO DO SUL | Brasil | 5007109 | 50 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 07d9acd1-dd87-3abf-8d63-2809b0f29abb | -23.33687 | -46.77251 | 2025-05-02 04:21:00 | NOAA-20 | CAIEIRAS | SÃO PAULO | Brasil | 3509007 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 50fa8d8b-5d2a-30c4-9808-0eee0bec4c09 | -24.24294 | -50.73806 | 2025-05-02 04:21:00 | NOAA-20 | ORTIGUEIRA | PARANÁ | Brasil | 4117305 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 21e5b061-f527-3051-aa5c-8fef1d1b5001 | -16.96581 | -51.27967 | 2025-05-02 04:21:00 | NOAA-20 | CAIAPÔNIA | GOIÁS | Brasil | 5204409 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| fb6aab18-641c-3b80-8859-7b3425edb883 | -19.49516 | -44.2751 | 2025-05-02 04:21:00 | NOAA-20 | SETE LAGOAS | MINAS GERAIS | Brasil | 3167202 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 09d6ff6a-bd95-3457-8af3-34ff82878396 | -25.79117 | -50.49123 | 2025-05-02 04:23:00 | NOAA-20 | SÃO MATEUS DO SUL | PARANÁ | Brasil | 4125605 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| d1ff3e9f-e6f9-30d0-a266-850d289e40c9 | -25.19873 | -49.32182 | 2025-05-02 04:23:00 | NOAA-20 | RIO BRANCO DO SUL | PARANÁ | Brasil | 4122206 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 8364d09d-c502-3530-92e7-b1250e52739a | -30.14856 | -52.02464 | 2025-05-02 04:23:00 | NOAA-20 | MINAS DO LEÃO | RIO GRANDE DO SUL | Brasil | 4312252 | 43 | 33 | nan | nan | nan | Pampa | 0.5 |
| 599c8b5b-ef4f-3a89-b5d5-d8cec36d1627 | -29.77692 | -51.17688 | 2025-05-02 04:23:00 | NOAA-20 | SÃO LEOPOLDO | RIO GRANDE DO SUL | Brasil | 4318705 | 43 | 33 | nan | nan | nan | Pampa | 0.9 |
| cc59b1f2-2eb5-34bb-bf3e-7c7fa31101b0 | -25.19089 | -49.32816 | 2025-05-02 04:23:00 | NOAA-20 | RIO BRANCO DO SUL | PARANÁ | Brasil | 4122206 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| d2472238-6d6c-353c-a2aa-a02655d922e9 | 1.11252 | -60.5167 | 2025-05-02 05:08:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 570c4ca5-ce38-3458-bff3-d95ccbdaab7a | 1.10799 | -60.51384 | 2025-05-02 05:08:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 0.6 |
| c199e026-815a-3f78-b794-7730f0e5d68b | 2.61417 | -60.3579 | 2025-05-02 05:08:00 | NOAA-21 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| fb2713c2-20b7-3711-84b1-efc763e8f490 | 1.11305 | -60.52017 | 2025-05-02 05:08:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 0.6 |
| ec23d265-c8f7-351e-b7bd-e295ec703b5a | 1.10852 | -60.51729 | 2025-05-02 05:08:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 32a23198-440f-37b3-b89a-2146d5ccff48 | -2.5993 | -49.06125 | 2025-05-02 05:08:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 78e4b350-07f3-3a08-95f0-36773ca3e745 | -5.16233 | -45.10447 | 2025-05-02 05:10:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 4334caa0-e257-315b-af58-530c2528ee29 | -7.99758 | -44.39442 | 2025-05-02 05:10:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| fe9ed9e1-87b9-38e5-aebd-e1061e397c6c | -9.87658 | -37.07503 | 2025-05-02 05:12:00 | AQUA_M-M | TRAIPU | ALAGOAS | Brasil | 2709202 | 27 | 33 | nan | nan | nan | Mata Atlântica | 8.3 |
| 5a19d715-2799-32a1-8d19-1338502851b6 | -10.50799 | -58.86243 | 2025-05-02 05:12:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 22112125-f746-3a6e-897b-3fc169553d96 | -12.55706 | -57.71362 | 2025-05-02 05:12:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 93afc2cb-a7b3-39e5-88f9-ab502de8adc9 | -12.55372 | -57.71309 | 2025-05-02 05:12:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 81d6c9fc-9d7f-3294-bf9c-b7054bb0bf58 | -13.04993 | -53.71322 | 2025-05-02 05:12:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| e8d8a9c3-a9ce-3acc-811c-cd6368e1775e | -15.58726 | -57.34272 | 2025-05-02 05:12:00 | NOAA-21 | PORTO ESTRELA | MATO GROSSO | Brasil | 5106851 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 95311c89-4904-3a3e-a15d-39f47d28eb0a | -15.71245 | -58.94524 | 2025-05-02 05:12:00 | NOAA-21 | PORTO ESPERIDIÃO | MATO GROSSO | Brasil | 5106828 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 5594d43f-b87f-31fc-b434-35755a331610 | -12.55427 | -57.7095 | 2025-05-02 05:12:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| bffa1759-4568-3d41-a5ed-02c024e04cbf | -12.55094 | -57.70896 | 2025-05-02 05:12:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 3b05def4-3566-336e-ad9a-ea449304c75c | -13.04639 | -53.70903 | 2025-05-02 05:12:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8222ac34-cc6f-35e8-b039-12842f318fc3 | -12.66623 | -58.11022 | 2025-05-02 05:12:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ecc3ac0b-a08e-3c30-aef2-5870cfc3a613 | -12.55651 | -57.71719 | 2025-05-02 05:12:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| abbea369-9065-37ca-a69d-3bb2ec263614 | -11.40447 | -52.95872 | 2025-05-02 05:12:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 48db097e-2a16-32dd-9e9a-dbe4f7729231 | -16.31783 | -53.81911 | 2025-05-02 05:12:00 | NOAA-21 | GUIRATINGA | MATO GROSSO | Brasil | 5104203 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c89d634b-1753-3a10-8f5e-21d309f7fdcd | -11.40498 | -52.95496 | 2025-05-02 05:12:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| a8976c1e-9045-3d30-815c-4982a8ddb603 | -13.05347 | -53.71735 | 2025-05-02 05:12:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| d5127c5d-b0d2-31af-a4e1-a38584f6cf6d | -11.39773 | -52.94626 | 2025-05-02 05:12:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 800d755e-0558-3ef7-8fc9-f20c9dc9ce3c | -13.04944 | -53.71682 | 2025-05-02 05:12:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 58e3e560-60c0-3ad6-96b2-890f98915dbe | -13.05249 | -53.72455 | 2025-05-02 05:12:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0526d7d6-2887-3854-bc59-715255ba596d | -13.05396 | -53.71376 | 2025-05-02 05:12:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| b9c401ea-43d3-3b33-9d15-a33c52c56fb1 | -13.05042 | -53.70959 | 2025-05-02 05:12:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| f481c0f8-8c59-3704-97fc-2778f0d966f0 | -11.88461 | -58.06487 | 2025-05-02 05:12:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 9c19c488-e23c-3b3a-9791-c4b39b741239 | -11.39722 | -52.95004 | 2025-05-02 05:12:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 32fb9edc-6408-336e-8eb1-cabfee767a00 | -12.66292 | -58.10969 | 2025-05-02 05:12:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 36e91535-9829-30ad-a3de-b3ddb7a716c8 | -16.31732 | -53.82299 | 2025-05-02 05:12:00 | NOAA-21 | GUIRATINGA | MATO GROSSO | Brasil | 5104203 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 1a1cfa1d-2462-36e3-9d61-d536769d2bea | -13.04797 | -53.72762 | 2025-05-02 05:12:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7890932c-bd00-3607-956f-d8d07fa5f8f9 | -13.62704 | -54.8773 | 2025-05-02 05:12:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 1da8cfa5-cd3e-350f-a9a5-dd7563c794f9 | -12.68223 | -58.09463 | 2025-05-02 05:12:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 3.0 |
| bb5359f7-3514-3c58-b7d9-3cf7e023a8c6 | -12.5576 | -57.71002 | 2025-05-02 05:12:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a0725000-db40-3892-8d23-11a2fbe946e1 | -13.052 | -53.72815 | 2025-05-02 05:12:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 415f280a-5936-3698-81cd-669f753758af | -12.55482 | -57.7059 | 2025-05-02 05:12:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 37408f15-4516-330b-95df-1ef76912be89 | -11.88516 | -58.06134 | 2025-05-02 05:12:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 29c1ef30-eede-343e-a383-160ce151d367 | -11.88185 | -58.06081 | 2025-05-02 05:12:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 596404d3-c3c2-39e0-92e5-bed7c64a94e2 | -13.04394 | -53.72707 | 2025-05-02 05:12:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f26998b6-aa7c-3138-8d2b-34753b9fcb1e | -21.47129 | -57.15895 | 2025-05-02 05:14:00 | NOAA-21 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e3ce5d75-fb8e-348d-94ec-d7c92a90c66f | -21.03012 | -55.64837 | 2025-05-02 05:14:00 | NOAA-21 | NIOAQUE | MATO GROSSO DO SUL | Brasil | 5005806 | 50 | 33 | nan | nan | nan | Cerrado | 1.8 |
| acb1702a-fd6b-374f-a05f-7c4a3ad1d3b3 | -22.06987 | -55.48493 | 2025-05-02 05:14:00 | NOAA-21 | DOURADOS | MATO GROSSO DO SUL | Brasil | 5003702 | 50 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 3c4208c3-7371-3981-9ee7-f4a1b250e905 | -23.98515 | -48.92084 | 2025-05-02 05:14:00 | NOAA-21 | ITAPEVA | SÃO PAULO | Brasil | 3522406 | 35 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 870c29d6-01cc-3c7e-996d-a614a61a3a81 | -21.46762 | -57.1584 | 2025-05-02 05:14:00 | NOAA-21 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f4411435-49a0-3252-91a7-0c678231cd6a | -24.24255 | -50.73861 | 2025-05-02 05:14:00 | NOAA-21 | ORTIGUEIRA | PARANÁ | Brasil | 4117305 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 6a4102ed-604e-3c38-81dc-8392249ebc73 | -23.17302 | -54.65205 | 2025-05-02 05:14:00 | NOAA-21 | AMAMBAI | MATO GROSSO DO SUL | Brasil | 5000609 | 50 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 4dd81b2c-7d7d-3f77-8d4c-b0f774c52244 | -21.7801 | -55.31624 | 2025-05-02 05:14:00 | NOAA-21 | MARACAJU | MATO GROSSO DO SUL | Brasil | 5005400 | 50 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 8e9ee365-2cfb-3cce-a20d-9c0b1428a07e | -23.1487 | -54.90034 | 2025-05-02 05:14:00 | NOAA-21 | AMAMBAI | MATO GROSSO DO SUL | Brasil | 5000609 | 50 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 2e830f02-7d12-3787-bfd7-e57c48dfcdc5 | -17.69495 | -54.3441 | 2025-05-02 05:14:00 | NOAA-21 | SONORA | MATO GROSSO DO SUL | Brasil | 5007935 | 50 | 33 | nan | nan | nan | Cerrado | 2.2 |


[Clique aqui para ver as próximas entradas](README4.md)
