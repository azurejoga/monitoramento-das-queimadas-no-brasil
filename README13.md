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

## Dados Diários - Página 13

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 3bd378aa-b708-3f36-9b16-dab947332a22 | -11.0218 | -45.23456 | 2025-06-07 04:21:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| d56114bd-0869-3394-8993-0299269b6ef3 | -7.8615 | -47.90359 | 2025-06-07 04:21:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f5e3db36-0f37-3211-8fed-435f83bd1052 | -9.40108 | -48.43864 | 2025-06-07 04:21:00 | NPP-375D | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 6a728ae1-8881-36a4-bba8-a67ace16728c | -10.4332 | -48.81092 | 2025-06-07 04:21:00 | NPP-375D | PUGMIL | TOCANTINS | Brasil | 1718451 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 9fb1ec60-3376-3b8c-bc7f-b11a3ef16c89 | -9.50397 | -47.39255 | 2025-06-07 04:21:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 7ecb2f9e-e9a4-34ca-89cf-4caebee04d9c | -12.37804 | -47.31573 | 2025-06-07 04:21:00 | NPP-375D | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 83901d86-cd4b-350c-8d4e-d7f56218c868 | -5.64774 | -43.71006 | 2025-06-07 04:21:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 10.0 |
| 094c612e-07f7-3e13-a6d8-54e0ed506879 | -8.45899 | -46.48769 | 2025-06-07 04:21:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 12542a76-30d4-3638-ae83-24751d6b59b8 | -7.72316 | -44.16655 | 2025-06-07 04:21:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 16.4 |
| c95950fe-0e5d-3525-9476-0319b2688cbe | -5.64274 | -43.72008 | 2025-06-07 04:21:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 11.3 |
| 54545a5a-4b7f-35cd-95f9-1770cbf15497 | -9.40039 | -48.44279 | 2025-06-07 04:21:00 | NPP-375D | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 2b609806-d62a-39e7-9144-84eb47d768cb | -11.81597 | -44.26858 | 2025-06-07 04:21:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 2f5e20e3-1d88-3e07-81c1-5a27efe35f98 | -7.71816 | -44.17663 | 2025-06-07 04:21:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 940cab79-e613-3a65-9c40-f756d097fbfb | -9.12483 | -46.88526 | 2025-06-07 04:21:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 536c23f3-6837-3560-9544-c95d30faf702 | -8.59359 | -45.87106 | 2025-06-07 04:21:00 | NPP-375D | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 9e57c198-92cf-3c05-adc1-708ea4585010 | -6.29309 | -48.50521 | 2025-06-07 04:21:00 | NPP-375D | SÃO GERALDO DO ARAGUAIA | PARÁ | Brasil | 1507458 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| fd021d0c-b998-3e80-ac75-11cc135df694 | -7.01058 | -44.61475 | 2025-06-07 04:21:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 6066f2c5-c609-37f7-ad93-117ab8c82ba5 | -6.23621 | -48.54623 | 2025-06-07 04:21:00 | NPP-375D | SÃO GERALDO DO ARAGUAIA | PARÁ | Brasil | 1507458 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 84e13a44-ff30-300b-8e11-9e963014ecdf | -6.81747 | -45.00034 | 2025-06-07 04:21:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 860899e1-33ce-30f8-a41c-d3143583a4ae | -11.81312 | -44.26432 | 2025-06-07 04:21:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 85a74376-5545-3333-bcd3-519179bcf543 | -12.38141 | -47.31629 | 2025-06-07 04:21:00 | NPP-375D | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 4bdfc703-8315-3fcb-bdd8-4d216c454aac | -10.49493 | -53.67146 | 2025-06-07 04:21:00 | NPP-375D | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 226b1a94-4850-3ba2-b64d-6fba5fd4e811 | -11.7714 | -47.39165 | 2025-06-07 04:21:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 29e7b884-7560-31c7-8ab7-e2d22bbaef93 | -7.73266 | -44.17166 | 2025-06-07 04:21:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 3.3 |
| e1156046-7bb6-3e19-a213-ded422facf4a | -6.20702 | -43.32635 | 2025-06-07 04:21:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 5a71d952-60e9-30eb-a819-66f0f7e4bd2c | -11.81939 | -44.26912 | 2025-06-07 04:21:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 4.0 |
| d428eeea-0b63-3f40-a20d-4278b49c7a3b | -5.6394 | -43.71955 | 2025-06-07 04:21:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 12.5 |
| b908038c-3c8a-38b6-95d0-72f0cc8a7920 | -10.46381 | -47.95036 | 2025-06-07 04:21:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| ac4469e7-7278-3a91-9705-3b4fd1a73f0c | -11.77081 | -47.39532 | 2025-06-07 04:21:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 1b64e17b-6c24-3264-9299-9a7ddde9a3d3 | -9.126 | -46.87804 | 2025-06-07 04:21:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b611421e-bb16-347c-8ffb-289c26c3b032 | -8.79425 | -45.10008 | 2025-06-07 04:21:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| aa82d79f-a70e-3849-ac78-ec007b840702 | -6.30724 | -48.48917 | 2025-06-07 04:21:00 | NPP-375D | SÃO GERALDO DO ARAGUAIA | PARÁ | Brasil | 1507458 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 9b24fc60-e38c-30d3-b16a-1713894ff435 | -8.20893 | -48.97883 | 2025-06-07 04:21:00 | NPP-375D | COUTO MAGALHÃES | TOCANTINS | Brasil | 1706001 | 17 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 677cd309-84d2-3ddc-b0f4-71d458c12195 | -7.18457 | -42.82452 | 2025-06-07 04:21:00 | NPP-375D | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 857728ab-75ac-3742-b340-2ad20c94629f | -8.17032 | -46.50467 | 2025-06-07 04:21:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 2537cf08-89c1-3510-baaa-0c20e1a1a03e | -6.2145 | -44.51045 | 2025-06-07 04:21:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| adeba67a-ed46-30fb-b535-0d37aa5466a0 | -6.28864 | -48.50889 | 2025-06-07 04:21:00 | NPP-375D | SÃO GERALDO DO ARAGUAIA | PARÁ | Brasil | 1507458 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 2bcdb332-e5ce-33a0-8897-9b8a2802a436 | -9.84333 | -48.60681 | 2025-06-07 04:21:00 | NPP-375D | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 19e0d70d-95c4-37e5-aef8-835acce8079c | -9.54723 | -47.77185 | 2025-06-07 04:21:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 8706b894-ca92-370d-80b5-761b6703ffde | -11.78495 | -47.39395 | 2025-06-07 04:21:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 7eb3efdf-4cc4-305a-a9dc-6a31948521b7 | -6.94594 | -42.90123 | 2025-06-07 04:21:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| a78a30d7-58dd-31dc-bebd-076493430b1b | -8.70413 | -46.67918 | 2025-06-07 04:21:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f97095ed-49e1-31d8-a0b4-964e82b295eb | -5.65091 | -43.60225 | 2025-06-07 04:21:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| cbb991e1-d7e6-3579-b155-63d46fb8f9fd | -8.20818 | -48.98334 | 2025-06-07 04:21:00 | NPP-375D | COUTO MAGALHÃES | TOCANTINS | Brasil | 1706001 | 17 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 964106cf-c989-307a-b45e-deba7246af66 | -7.8586 | -47.89894 | 2025-06-07 04:21:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| fcfdb111-6705-33d6-be4c-e170a77bd5d8 | -9.49991 | -47.39574 | 2025-06-07 04:21:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 3dccf69c-c695-3c90-91fc-b52401f8af1b | -6.20308 | -43.32941 | 2025-06-07 04:21:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 15.2 |
| 3fe44999-d75d-3167-910f-3125d7d86555 | -8.87301 | -50.18767 | 2025-06-07 04:21:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| c0834c23-74e8-3a96-bc92-233d015f0de7 | -9.55072 | -47.77242 | 2025-06-07 04:21:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 4b52fdd6-e44f-3b40-9aa1-258f6c28be83 | -10.89723 | -42.24459 | 2025-06-07 04:21:00 | NPP-375D | ITAGUAÇU DA BAHIA | BAHIA | Brasil | 2915353 | 29 | 33 | nan | nan | nan | Caatinga | 0.6 |
| f0878729-5975-3e3b-a2f6-3e2d8e10152a | -11.90526 | -44.87208 | 2025-06-07 04:21:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e0f36903-9555-3b94-888e-5c98184d5fec | -6.96199 | -42.91143 | 2025-06-07 04:21:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 14.7 |
| 6d884371-dc0d-3461-ad22-a3aaf78efe97 | -9.2609 | -48.2436 | 2025-06-07 04:21:00 | NPP-375D | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| f8680111-2429-3f07-930a-31c79525a94b | -5.65146 | -43.59872 | 2025-06-07 04:21:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 96510423-7bb6-3567-81b0-7aee80abaf8c | -10.49312 | -53.66058 | 2025-06-07 04:21:00 | NPP-375D | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 883c2dc6-25cc-3a71-83ee-c607d8f6dd7b | -11.33181 | -44.8533 | 2025-06-07 04:21:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| f9080195-712c-31b4-9fca-1ba9444c9b21 | -11.77639 | -47.40381 | 2025-06-07 04:21:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 10ec2c3d-9802-373a-a6dc-7c3727ca6087 | -10.64289 | -44.48769 | 2025-06-07 04:21:00 | NPP-375D | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| a1ebdbec-ed78-3024-a1c6-e9cabcc9dbb5 | -8.16973 | -46.5083 | 2025-06-07 04:21:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 136fb4e0-31c4-3759-ac2e-fcd46ae4160b | -11.78715 | -47.40186 | 2025-06-07 04:21:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 5.9 |
| aace91b2-3327-3c64-9bad-77eb7df77c56 | -9.07263 | -47.14231 | 2025-06-07 04:21:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 71100d25-e7a0-37c3-8ee5-254c7804f1c4 | -6.2156 | -44.50351 | 2025-06-07 04:21:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| ee6473b7-ba01-344f-a390-ef9a97454310 | -11.90807 | -44.87624 | 2025-06-07 04:21:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 1643f2c2-ba9b-3e7f-8687-c06202bd5cca | -10.49692 | -53.66038 | 2025-06-07 04:21:00 | NPP-375D | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 80f797d6-a9c9-3176-b7d4-11818fcfdb8c | -10.8805 | -54.31478 | 2025-06-07 04:21:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4d2388f1-c391-3cfb-9f8d-56378b7c7f49 | -8.45503 | -46.49076 | 2025-06-07 04:21:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 83671339-b86b-3fd8-879a-eccff4a0e45d | -6.66532 | -47.73545 | 2025-06-07 04:21:00 | NPP-375D | PALMEIRAS DO TOCANTINS | TOCANTINS | Brasil | 1713809 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 8eaf50ca-6b26-31c3-ae3e-1552d8393bea | -7.21327 | -43.11277 | 2025-06-07 04:21:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 15d8dabc-3147-3ccf-84a2-d8fc8898072a | -12.27701 | -44.60518 | 2025-06-07 04:21:00 | NPP-375D | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| b6eeaf1c-042f-3d03-8117-e13ad0334f7a | -7.7349 | -44.17926 | 2025-06-07 04:21:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 5eeae161-ec3d-3802-bc61-3f13f88b0fe9 | -6.95453 | -42.91408 | 2025-06-07 04:21:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 4.8 |
| 0e8f3e98-93cd-37f6-bd05-7417120d9fe5 | -7.7321 | -44.1752 | 2025-06-07 04:21:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 3.3 |
| b00d6375-7e81-3393-b7ac-99be62c3ff5e | -7.736 | -44.17218 | 2025-06-07 04:21:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 16.8 |
| ca2e0e35-a807-35f9-a3f3-a08b078f0c1f | -9.55009 | -47.7763 | 2025-06-07 04:21:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 811c23ee-f6d0-3c45-8c47-663978a8362e | -12.27246 | -44.58938 | 2025-06-07 04:21:00 | NPP-375D | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 4721f8ee-a10f-3ace-be64-b1677adc947b | -11.13832 | -53.9197 | 2025-06-07 04:21:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f7fb0e45-d3f4-3620-9d54-2cd97780c182 | -10.30161 | -57.13659 | 2025-06-07 04:21:00 | NPP-375D | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c411a809-3c97-32c4-8d9f-8039888d01ce | -9.40537 | -48.43509 | 2025-06-07 04:21:00 | NPP-375D | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |
| de5302cb-99a4-3736-ae2e-a97264bf5baf | -10.87765 | -54.3018 | 2025-06-07 04:21:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| bb27d1d3-cbc5-3506-92a1-5412216f4f7a | -7.73435 | -44.18279 | 2025-06-07 04:21:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 9a792008-797c-353c-90c8-dbe3aa889dfc | -11.81711 | -44.26112 | 2025-06-07 04:21:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| b94d9f98-9e04-3476-ac83-c281afb1256c | -7.72096 | -44.18069 | 2025-06-07 04:21:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c5b92710-3692-3af6-8535-72484fd7c7eb | -12.27585 | -44.5899 | 2025-06-07 04:21:00 | NPP-375D | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| df5c4ea9-c53d-3be1-becf-2b6197ec2d01 | -9.05598 | -40.07627 | 2025-06-07 04:21:00 | NPP-375D | LAGOA GRANDE | PERNAMBUCO | Brasil | 2608750 | 26 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 59204d74-f69c-316b-8d1a-241d14acc470 | -7.86217 | -47.89952 | 2025-06-07 04:21:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 3197bd54-b8c4-3bcb-a983-04943fa315fc | -5.64329 | -43.71656 | 2025-06-07 04:21:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 11.3 |
| 536a302d-f3a4-3336-a02d-058a7b9142a2 | -5.6366 | -43.71551 | 2025-06-07 04:21:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 12.5 |
| fe3c7e6a-8091-3cab-b667-bbf85177d55c | -8.44944 | -46.48244 | 2025-06-07 04:21:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| d365e9c1-596f-312e-af5a-cb87b6162d0c | -5.45914 | -44.82078 | 2025-06-07 04:21:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| cf3cd932-2dd9-381a-8450-86d2bc4f99c0 | -6.83326 | -44.32235 | 2025-06-07 04:21:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 5e97269c-09d9-3eac-8c83-edcfdde0bad0 | -7.19018 | -46.23277 | 2025-06-07 04:21:00 | NPP-375D | NOVA COLINAS | MARANHÃO | Brasil | 2107258 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 642cc879-c185-3ebb-a486-eecf91fa0735 | -7.71982 | -44.16603 | 2025-06-07 04:21:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 485a5b0a-7460-3345-8476-cbc8e96d9ab7 | -9.55769 | -47.77364 | 2025-06-07 04:21:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| d6590f91-5a0e-31e7-beaa-61126968c310 | -7.73825 | -44.17978 | 2025-06-07 04:21:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 6d0f2644-a0ac-3a1c-b267-4516bbae8184 | -9.0686 | -47.14546 | 2025-06-07 04:21:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| ba0bfa9c-5642-3951-be8e-1c150da8602a | -5.64554 | -43.72411 | 2025-06-07 04:21:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 14.5 |
| 38533e52-653a-37c2-8c64-10984e347ebd | -6.95167 | -42.90979 | 2025-06-07 04:21:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 4.8 |
| 4b82ea1e-1c17-3bf5-b67a-e3e4bfdd6153 | -6.20646 | -43.32995 | 2025-06-07 04:21:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 15.2 |
| fa7c4cfd-1f29-3659-8cea-f0d171b4d497 | -6.95971 | -42.90339 | 2025-06-07 04:21:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 24.9 |
| 6e951e0c-df79-30ef-a933-f7e169b3ec12 | -6.20253 | -43.333 | 2025-06-07 04:21:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 15.2 |


[Clique aqui para ver as próximas entradas](README14.md)
