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

## Dados Diários - Página 57

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 44c7c14a-7392-3675-bc82-bd029becb9e3 | -14.31019 | -44.72781 | 2025-09-30 04:40:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 6fbac92a-424b-3fea-841f-8b407453d06c | -13.58215 | -48.05497 | 2025-09-30 04:40:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 4.1 |
| c09328f9-ec01-34be-bfe2-fb1d184115d6 | -10.11021 | -47.78118 | 2025-09-30 04:40:00 | NOAA-21 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 5dd9670c-0f41-39c8-bb90-73db24890610 | -11.19814 | -47.21583 | 2025-09-30 04:40:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 9.1 |
| 74b9e38b-2f98-33fe-beb3-b79958a38c0a | -9.42642 | -54.71501 | 2025-09-30 04:40:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| a1f5a92c-a33f-3f8a-9c80-346b95d04deb | -13.38988 | -48.06187 | 2025-09-30 04:40:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |
| ee68a79f-2556-318d-8890-af4ae686ffd1 | -10.17385 | -44.88844 | 2025-09-30 04:40:00 | NOAA-21 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| c765e7b4-0554-3a5a-ad9c-aff52d721e22 | -11.8899 | -48.05544 | 2025-09-30 04:40:00 | NOAA-21 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 6c691752-f120-3325-b508-7f9e81eaca15 | -12.84212 | -46.97703 | 2025-09-30 04:40:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| b80e6d6c-d784-3a57-aba0-d4eb802f1489 | -13.3672 | -47.91446 | 2025-09-30 04:40:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 099af6c9-0110-3b92-8209-6cf18c7a00d7 | -9.40391 | -54.69815 | 2025-09-30 04:40:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 5ac5286b-0fb3-36c0-9f0e-9b1d4087b33e | -9.32557 | -45.70134 | 2025-09-30 04:40:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 3.7 |
| caab189d-d772-30d8-a0e5-6c451a1183eb | -9.12782 | -47.63669 | 2025-09-30 04:40:00 | NOAA-21 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 1c4c16d5-06f7-3caa-8a4c-8d1ef06b4c63 | -13.81099 | -47.89408 | 2025-09-30 04:40:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 53c154d3-f866-32e0-85c1-d211e6e1e916 | -9.077 | -45.87268 | 2025-09-30 04:40:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 3a82c098-b7d2-3260-b25e-c6685db5d8f7 | -10.06472 | -50.23408 | 2025-09-30 04:40:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 86466772-1f4d-3aef-9e66-c75d01def933 | -13.01249 | -44.1184 | 2025-09-30 04:40:00 | NOAA-21 | SANTANA | BAHIA | Brasil | 2928208 | 29 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 2366de17-7f67-38d5-b0c6-f930f7f63606 | -7.11586 | -45.54836 | 2025-09-30 04:40:00 | NOAA-21 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| c8d9d3c0-f949-38ac-9418-6745e2d1627e | -10.06689 | -50.22017 | 2025-09-30 04:40:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 9.4 |
| bd2995ed-5425-37b9-828d-b80b2eb5f88e | -10.40449 | -49.04506 | 2025-09-30 04:40:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 2f9ba2fa-5483-394c-906a-8416a1489f40 | -12.89505 | -46.76427 | 2025-09-30 04:40:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 70be6f37-1217-3a5b-82cb-b66dfd441b2e | -9.0527 | -46.69526 | 2025-09-30 04:40:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| b5c52e06-9648-31a3-bb2e-40a218888865 | -10.06719 | -48.19166 | 2025-09-30 04:40:00 | NOAA-21 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| c1a600cd-466b-3fd3-9d4d-141f8172b763 | -13.83909 | -47.50883 | 2025-09-30 04:40:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 73b053a8-9622-3dea-bfd1-35ae2c28eb03 | -10.43068 | -46.14948 | 2025-09-30 04:40:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 6b23427b-645c-3179-b45e-bff7a5c2dddd | -9.57658 | -40.34922 | 2025-09-30 04:40:00 | NOAA-21 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 29.4 |
| a7673a0f-556e-321f-8338-09aa1e66529b | -9.58456 | -54.58964 | 2025-09-30 04:40:00 | NOAA-21 | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 7a24044b-fe03-3f98-92ad-6a5057d1e483 | -12.76845 | -46.83926 | 2025-09-30 04:40:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| ccca4466-3729-3917-a22c-a87400bf7f2c | -11.21094 | -47.20443 | 2025-09-30 04:40:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| aeac77c0-ca08-3c34-916f-f720db74e5c2 | -9.04433 | -46.69939 | 2025-09-30 04:40:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 9782a1d8-8e17-3edc-a385-06927f971720 | -7.82667 | -46.99656 | 2025-09-30 04:40:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 6.9 |
| c2e2a31e-86b7-3e05-bf6d-f7671688b04a | -10.6314 | -48.52153 | 2025-09-30 04:40:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| da4758c8-7311-3894-9a7e-9c41f1301734 | -7.92842 | -44.63208 | 2025-09-30 04:40:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 5.9 |
| d85db759-9b5b-3dd0-96b2-0a6dadb13877 | -11.37098 | -45.06571 | 2025-09-30 04:40:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 7f4bd1d9-6c3b-3cbe-b36f-789275741773 | -8.67086 | -47.71285 | 2025-09-30 04:40:00 | NOAA-21 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 03a86541-2b2e-30f7-8542-6478ce4aa026 | -13.75189 | -47.92018 | 2025-09-30 04:40:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| b1298dbd-8895-3860-923b-e2997fe90d55 | -13.78838 | -47.97535 | 2025-09-30 04:40:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| a240e27a-f42d-3122-9e2c-44a9ef67ed79 | -10.62043 | -54.94924 | 2025-09-30 04:40:00 | NOAA-21 | TERRA NOVA DO NORTE | MATO GROSSO | Brasil | 5108055 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 29e0b0ed-de0f-3b4b-a5cb-00d2140754f5 | -7.53872 | -45.29709 | 2025-09-30 04:40:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 3b8b39ae-5bde-3f7b-a7c7-fbd6facd94cd | -13.77175 | -47.93643 | 2025-09-30 04:40:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 6758308b-0318-38e6-b383-349b87b5ef9d | -10.0437 | -50.19146 | 2025-09-30 04:40:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 7f32ccc6-a730-3ade-a89d-ea1c8490b5a4 | -12.78681 | -47.73393 | 2025-09-30 04:40:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 5d016ef3-1ba3-3087-8ee4-cea50674edb9 | -11.65232 | -47.49353 | 2025-09-30 04:40:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 5.0 |
| f6edc5d7-a1ca-377e-bf83-7fc8af613821 | -10.19091 | -44.88705 | 2025-09-30 04:40:00 | NOAA-21 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 22.0 |
| 9935f544-9e0e-3ad3-9afe-bf961f03fbd5 | -13.20886 | -50.92878 | 2025-09-30 04:40:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 6e714837-8485-3319-a1e2-fb7ffb2ddbee | -12.82261 | -47.00687 | 2025-09-30 04:40:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 0a95d5be-5d00-3834-856c-99c84e04b935 | -10.63425 | -48.52589 | 2025-09-30 04:40:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 7b67fdfe-e0c9-30e2-9371-e210f78459bb | -8.87473 | -46.65818 | 2025-09-30 04:40:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 2e81efcf-f921-3ee5-a409-9c630eab45c4 | -7.16245 | -50.55268 | 2025-09-30 04:40:00 | NOAA-21 | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 7e4099b6-d267-3378-a3db-634bc2e02e92 | -12.95672 | -48.40435 | 2025-09-30 04:40:00 | NOAA-21 | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 4f9b55d8-fdf7-34f0-9c89-ea4595dd9611 | -8.25369 | -45.54311 | 2025-09-30 04:40:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 4.5 |
| e829dc24-6519-3e8d-b860-6428d117e216 | -7.5082 | -44.28533 | 2025-09-30 04:40:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 95e97a59-f670-3fac-b274-68b0e63fe3c3 | -7.33586 | -44.73092 | 2025-09-30 04:40:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| c0a54a88-a554-3b63-901b-3c731129b1ff | -12.29283 | -55.14199 | 2025-09-30 04:40:00 | NOAA-21 | VERA | MATO GROSSO | Brasil | 5108501 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 49545b37-ce3a-3a01-b5e9-89067f09a6c6 | -12.54262 | -48.29171 | 2025-09-30 04:40:00 | NOAA-21 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 4dd06d6d-ceb3-3325-9e2f-5057c774c2a7 | -10.66107 | -48.55691 | 2025-09-30 04:40:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| ef271c41-c361-39a1-bf9c-ac404dcdeace | -8.23413 | -45.50196 | 2025-09-30 04:40:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 2202a56e-01fa-3261-8925-5f8c55f628da | -8.67373 | -47.71724 | 2025-09-30 04:40:00 | NOAA-21 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 7ab6f4b3-0df9-3593-8387-7f683c1809cc | -12.75235 | -46.87158 | 2025-09-30 04:40:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |
| c9f55859-177e-3c70-a214-4584e49537a2 | -10.62749 | -48.54792 | 2025-09-30 04:40:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 9934daa1-916f-3724-b809-8cf2865d96c1 | -14.002 | -49.63113 | 2025-09-30 04:40:00 | NOAA-21 | MARA ROSA | GOIÁS | Brasil | 5212808 | 52 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 4e97284a-4db5-3209-b5c7-2e0070de32ef | -13.27805 | -48.45832 | 2025-09-30 04:40:00 | NOAA-21 | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 2c8f8caf-9336-3dc2-9cac-d457815800fd | -7.04574 | -45.20852 | 2025-09-30 04:40:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 5bc6c958-e7fe-3f32-8a5d-f6fb541c08e2 | -10.14573 | -48.1567 | 2025-09-30 04:40:00 | NOAA-21 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 209135b4-1f86-3140-8496-f5905bfb8071 | -11.20666 | -47.20831 | 2025-09-30 04:40:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| ebca1bfe-3465-3b3e-9f4c-5a9d49c9128f | -12.84427 | -46.87856 | 2025-09-30 04:40:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 7df9f770-8afa-3687-b95d-47a19f42d5ba | -11.05157 | -47.65312 | 2025-09-30 04:40:00 | NOAA-21 | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 927747a6-c14a-34e5-ab67-7131ea33e1e0 | -10.95612 | -46.47588 | 2025-09-30 04:40:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.2 |
| da4f9892-d242-30ea-b5b2-eb6d357d913e | -7.91845 | -44.61484 | 2025-09-30 04:40:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 5.2 |
| bd4807b3-44db-3549-8e7f-232fc04c92fc | -8.87536 | -46.6538 | 2025-09-30 04:40:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 0b14cc37-74f9-3046-8227-e0db8e370f05 | -11.89453 | -48.04509 | 2025-09-30 04:40:00 | NOAA-21 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 9371c05b-fc65-35fd-a51a-39f022f139c5 | -11.80743 | -52.39495 | 2025-09-30 04:40:00 | NOAA-21 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a4725e4b-da38-3693-bd85-56b8a27ec8f0 | -7.4357 | -47.80828 | 2025-09-30 04:40:00 | NOAA-21 | FILADÉLFIA | TOCANTINS | Brasil | 1707702 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 3e15b76f-08db-31ed-ac0a-a3ac7e64a223 | -10.08117 | -50.2153 | 2025-09-30 04:40:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 12.9 |
| 4841a6c5-27af-386b-ac1f-11ad82f0537a | -12.86746 | -46.90597 | 2025-09-30 04:40:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 4f030f0b-85c6-3da4-aa41-23b652e1bf18 | -7.79648 | -42.51384 | 2025-09-30 04:40:00 | NOAA-21 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| d126f944-9d45-31e9-b2d7-a3328d1082a5 | -13.21601 | -50.92633 | 2025-09-30 04:40:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 727c481f-225d-309f-8b7d-99dfa7bcc396 | -13.21681 | -47.31274 | 2025-09-30 04:40:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 6645e1c6-1455-374c-8e24-f476365cfb64 | -8.89426 | -45.03786 | 2025-09-30 04:40:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 597d3cde-1c45-3056-9c61-2289ea32fff9 | -9.32088 | -50.6347 | 2025-09-30 04:40:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d5fb1ce7-a14d-3401-8b89-08148cb990ba | -8.2418 | -45.51554 | 2025-09-30 04:40:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| dcefea3a-5137-3ecf-8894-13b3f587f8b4 | -13.37068 | -47.31156 | 2025-09-30 04:40:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 864b47a4-149b-3233-8193-9904b9aa9482 | -8.14321 | -46.36596 | 2025-09-30 04:40:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 5.8 |
| ded303de-c385-3af4-aa8a-cf7ad3dd24dd | -10.19299 | -52.55023 | 2025-09-30 04:40:00 | NOAA-21 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 6b484201-00de-32e8-8662-5860cc01b9fa | -12.74926 | -46.86609 | 2025-09-30 04:40:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 0.3 |
| d0717f9d-80ff-3827-867a-0f5f4103b791 | -13.7358 | -48.68774 | 2025-09-30 04:40:00 | NOAA-21 | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| f0784529-999a-31d2-9dbf-8cb4130efcf6 | -11.25569 | -47.22898 | 2025-09-30 04:40:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 2270f410-0e32-37d8-9d43-37112c72484c | -11.75504 | -44.74381 | 2025-09-30 04:40:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 25.9 |
| 9e144c24-38e6-3aa2-aef2-38d7edc36de9 | -10.40726 | -48.16695 | 2025-09-30 04:40:00 | NOAA-21 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 6d9ec6aa-ced7-38b5-9054-6e0c419b81f4 | -10.65648 | -48.54086 | 2025-09-30 04:40:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 24e8880a-0e82-3cfc-adc2-145ac22aa8e3 | -13.63812 | -51.83258 | 2025-09-30 04:40:00 | NOAA-21 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 566a8cb4-9649-35be-bea7-831e68ddb259 | -10.08447 | -50.21582 | 2025-09-30 04:40:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 11.2 |
| 181713de-5c8d-3484-9d8d-73533d26de59 | -9.62717 | -50.89548 | 2025-09-30 04:40:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| b09b5264-cee3-312a-ad0e-c1eabd9afe58 | -8.50452 | -47.25689 | 2025-09-30 04:40:00 | NOAA-21 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| e8899678-9a2c-31ad-9449-6d7d020579da | -14.38784 | -47.14506 | 2025-09-30 04:40:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 2aeced2d-b1ee-39b2-822d-96b2b5ee6480 | -9.46749 | -45.48959 | 2025-09-30 04:40:00 | NOAA-21 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 6cc2fd9b-2fae-3c4c-840e-cba79620dc6b | -11.70545 | -47.83199 | 2025-09-30 04:40:00 | NOAA-21 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 91fa37cb-5062-3fbf-a632-5cde8ebecb96 | -13.49655 | -47.40163 | 2025-09-30 04:40:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 63a38cf5-7db9-37f7-9277-908680119f6c | -13.63166 | -48.03048 | 2025-09-30 04:40:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 61564c04-f688-34de-b67a-3028c270521f | -7.05249 | -45.18943 | 2025-09-30 04:40:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 5.6 |


[Clique aqui para ver as próximas entradas](README58.md)
