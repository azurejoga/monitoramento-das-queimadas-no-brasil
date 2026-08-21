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

## Dados Diários - Página 89

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| f85276a8-6ee5-3c8f-a96d-2da02bf4de0d | -9.42261 | -60.41857 | 2026-08-21 12:14:00 | TERRA_M-T | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 18.7 |
| 934761b8-d82c-32d9-a3ca-cd19f5b0190e | -13.67132 | -51.79539 | 2026-08-21 12:14:00 | TERRA_M-T | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 21.1 |
| d5e5953a-b01c-3d13-99ac-379b6facc903 | -8.58212 | -54.78583 | 2026-08-21 12:14:00 | TERRA_M-T | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 2c8c092c-a03b-3899-9bec-2d0ceb833fb7 | -13.43733 | -51.78924 | 2026-08-21 12:14:00 | TERRA_M-T | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 26.5 |
| 74205f96-69e7-3f5a-b937-14f82516154b | -6.87645 | -43.7425 | 2026-08-21 12:14:00 | TERRA_M-T | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 77.4 |
| ae2db21f-99e9-3feb-8cff-d594286b1937 | -13.93043 | -53.8547 | 2026-08-21 12:14:00 | TERRA_M-T | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 17.4 |
| 715ff1b5-8ab2-32ef-b436-a219ae6de8ff | -14.34252 | -51.88356 | 2026-08-21 12:14:00 | TERRA_M-T | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 38.2 |
| 7120f130-ba5d-39a8-a6ba-1594c2611c49 | -11.2094 | -55.0514 | 2026-08-21 12:14:00 | TERRA_M-T | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 7.4 |
| 68c89787-8d82-3cc2-859c-0afd07ebb703 | -9.32885 | -56.9105 | 2026-08-21 12:14:00 | TERRA_M-T | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 44.3 |
| c26fae68-e525-36c1-accf-298f64557cae | -13.38007 | -54.37484 | 2026-08-21 12:14:00 | TERRA_M-T | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 19.0 |
| 3bc6910a-7f55-3239-b38d-9002ac7d3de7 | -11.17225 | -54.01809 | 2026-08-21 12:14:00 | TERRA_M-T | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 30.0 |
| 976e9c87-4a1b-39a6-bef3-ea94115884bf | -10.00972 | -53.95741 | 2026-08-21 12:14:00 | TERRA_M-T | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 6d68f7b8-3e3b-33ff-989c-c6f995d2366c | -8.09282 | -51.65722 | 2026-08-21 12:14:00 | TERRA_M-T | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| f03f4a18-aea4-3ece-b02c-41725fa5b620 | -6.89215 | -59.42754 | 2026-08-21 12:14:00 | TERRA_M-T | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 31.8 |
| c06d7a5a-1efe-31bf-85e6-a158e5868717 | -14.03137 | -58.86267 | 2026-08-21 12:14:00 | TERRA_M-T | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 6.5 |
| b5d1bb0f-2923-3cf9-a3d4-30dbf8fae908 | -8.18383 | -54.98889 | 2026-08-21 12:14:00 | TERRA_M-T | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 0f7a93cf-d0a5-34e2-9dc8-0055f00b1784 | -6.69759 | -58.94655 | 2026-08-21 12:14:00 | TERRA_M-T | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 14.6 |
| a74c5887-dfb2-3359-95f3-93bd573c469e | -14.32235 | -51.88754 | 2026-08-21 12:14:00 | TERRA_M-T | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 19.1 |
| 625b5d77-a9fd-3cd7-9dc3-7ca7bcb47c11 | -13.23319 | -51.6343 | 2026-08-21 12:14:00 | TERRA_M-T | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 16.1 |
| 1377917b-f226-3158-90ff-740b75a14d7f | -6.86815 | -59.42377 | 2026-08-21 12:14:00 | TERRA_M-T | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 43.8 |
| 9de8bd8b-1830-3809-8fd0-49069219fc03 | -11.62733 | -46.55344 | 2026-08-21 12:14:00 | TERRA_M-T | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 32.0 |
| 8d668464-b3de-32be-832d-d25076f48e4b | -6.94111 | -52.7806 | 2026-08-21 12:14:00 | TERRA_M-T | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 98d0e9b6-d353-33ee-ab70-ccd134f71f35 | -6.23032 | -55.60807 | 2026-08-21 12:14:00 | TERRA_M-T | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| b2e1079e-4cff-344b-a571-8def34142562 | -12.74821 | -48.4697 | 2026-08-21 12:14:00 | TERRA_M-T | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 21.3 |
| 94081fee-2714-3bf5-b8d4-3f9052ac6488 | -9.43509 | -48.25894 | 2026-08-21 12:14:00 | TERRA_M-T | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 32.1 |
| ad5f2368-670d-3e97-99fb-10ddc2b3aafd | -6.88014 | -59.42571 | 2026-08-21 12:14:00 | TERRA_M-T | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 50.8 |
| 36f7c615-f270-33e9-8b56-222d02842d52 | -7.36682 | -45.8109 | 2026-08-21 12:14:00 | TERRA_M-T | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 69.9 |
| af81552a-506f-3181-a136-b25e3f15eb52 | -6.25933 | -48.65817 | 2026-08-21 12:14:00 | TERRA_M-T | SÃO GERALDO DO ARAGUAIA | PARÁ | Brasil | 1507458 | 15 | 33 | nan | nan | nan | Amazônia | 100.8 |
| 141cd42e-efe3-343d-ac99-0a5728828d1e | -13.26683 | -51.61409 | 2026-08-21 12:14:00 | TERRA_M-T | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 11.0 |
| 4e0a30ad-d732-37bc-9c69-7ac2d97d8bab | -13.62533 | -51.75919 | 2026-08-21 12:14:00 | TERRA_M-T | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 9.3 |
| 556a65ff-f9e8-3e78-b429-0766fd1696b5 | -10.25758 | -54.36364 | 2026-08-21 12:14:00 | TERRA_M-T | MATUPÁ | MATO GROSSO | Brasil | 5105606 | 51 | 33 | nan | nan | nan | Amazônia | 5.0 |
| ec31a881-c47f-3041-9c81-b2bf0538a3f2 | -8.45165 | -46.95289 | 2026-08-21 12:14:00 | TERRA_M-T | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 109.7 |
| f953941e-c069-36f7-9532-3603bc268436 | -8.52118 | -55.33337 | 2026-08-21 12:14:00 | TERRA_M-T | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 14.5 |
| b6cf1490-0347-347c-a500-97177910263f | -4.9561 | -56.25815 | 2026-08-21 12:14:00 | TERRA_M-T | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 8.7 |
| 4d3540f4-4664-3352-bb90-56be1516bf14 | -11.37689 | -46.35945 | 2026-08-21 12:14:00 | TERRA_M-T | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 31.5 |
| 339d1f60-cad4-391d-b190-9d31062e46f3 | -9.45127 | -51.60052 | 2026-08-21 12:14:00 | TERRA_M-T | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 15.9 |
| 12de30e9-de37-35f2-88cc-eab7afce639b | -15.00704 | -52.66992 | 2026-08-21 12:14:00 | TERRA_M-T | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 14.2 |
| dd5aa2cf-d47c-3347-a576-c59f6fc4d54b | -12.00964 | -53.43103 | 2026-08-21 12:14:00 | TERRA_M-T | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 16.2 |
| 7bdc5245-aca5-382e-9686-3037a8de91b5 | -14.33091 | -51.90095 | 2026-08-21 12:14:00 | TERRA_M-T | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 35.6 |
| a142f631-940c-32e5-950d-f634581859ae | -6.22889 | -55.61785 | 2026-08-21 12:14:00 | TERRA_M-T | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 101.4 |
| aad3ac36-9d2a-3f9f-b693-ae946453fff4 | -13.73591 | -51.84668 | 2026-08-21 12:14:00 | TERRA_M-T | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 39.5 |
| c86e1895-4a9a-3326-9890-8562780a50ed | -8.02864 | -54.01964 | 2026-08-21 12:14:00 | TERRA_M-T | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| d649ec2b-4022-30a7-9964-eda67e90fe42 | -7.4599 | -46.14678 | 2026-08-21 12:14:00 | TERRA_M-T | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 41.0 |
| 2ae57f8b-0ee7-3521-9b59-0696ec5777dc | -9.4011 | -60.55042 | 2026-08-21 12:14:00 | TERRA_M-T | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 24.4 |
| 933c20ff-5d1e-3177-a0d3-251d1bbc8762 | -6.17152 | -55.44419 | 2026-08-21 12:14:00 | TERRA_M-T | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 11.6 |
| b1dd30eb-d549-38b7-a855-223ffcd08deb | -22.85584 | -49.32965 | 2026-08-21 12:17:00 | TERRA_M-T | ÁGUAS DE SANTA BÁRBARA | SÃO PAULO | Brasil | 3500550 | 35 | 33 | nan | nan | nan | Cerrado | 61.3 |
| a10023e7-41d4-3081-a1d0-7e4e1470a01f | -19.66237 | -46.02684 | 2026-08-21 12:17:00 | TERRA_M-T | CÓRREGO DANTA | MINAS GERAIS | Brasil | 3119807 | 31 | 33 | nan | nan | nan | Cerrado | 71.9 |
| 8c2d6c57-3fb9-3ae6-bda8-cc93e0d9292c | -20.82919 | -54.94542 | 2026-08-21 12:17:00 | TERRA_M-T | SIDROLÂNDIA | MATO GROSSO DO SUL | Brasil | 5007901 | 50 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 27f8771d-6a85-3b88-ba46-0a0428da91dc | -17.7782 | -54.24693 | 2026-08-21 12:17:00 | TERRA_M-T | SONORA | MATO GROSSO DO SUL | Brasil | 5007935 | 50 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 65852bd8-449d-374d-b06c-79bc58a34c51 | -16.72161 | -47.69217 | 2026-08-21 12:17:00 | TERRA_M-T | CRISTALINA | GOIÁS | Brasil | 5206206 | 52 | 33 | nan | nan | nan | Cerrado | 58.2 |
| 0ab1040e-0b3a-3bda-ab45-28a965845d0e | -16.72014 | -47.68552 | 2026-08-21 12:17:00 | TERRA_M-T | CRISTALINA | GOIÁS | Brasil | 5206206 | 52 | 33 | nan | nan | nan | Cerrado | 56.4 |
| 90170138-52cd-3411-9f28-8e9a643ba7c9 | -23.06974 | -50.36792 | 2026-08-21 12:17:00 | TERRA_M-T | BANDEIRANTES | PARANÁ | Brasil | 4102406 | 41 | 33 | nan | nan | nan | Mata Atlântica | 11.8 |
| 6649a7ae-4d71-353d-adb5-73a6c3c71038 | -22.62144 | -54.99954 | 2026-08-21 12:17:00 | TERRA_M-T | CAARAPÓ | MATO GROSSO DO SUL | Brasil | 5002407 | 50 | 33 | nan | nan | nan | Mata Atlântica | 12.0 |
| 9b2ca5ee-d0c7-326b-b1c1-5a013e89ad48 | -22.85352 | -49.35529 | 2026-08-21 12:17:00 | TERRA_M-T | ÁGUAS DE SANTA BÁRBARA | SÃO PAULO | Brasil | 3500550 | 35 | 33 | nan | nan | nan | Cerrado | 164.3 |
| 899123ee-6747-3ac3-982a-2c7acd54314d | -23.06759 | -50.38948 | 2026-08-21 12:17:00 | TERRA_M-T | BANDEIRANTES | PARANÁ | Brasil | 4102406 | 41 | 33 | nan | nan | nan | Mata Atlântica | 10.7 |
| e4dee3ee-fd43-3d2c-9772-6d7ec0c3b8ea | -17.19808 | -53.14787 | 2026-08-21 12:17:00 | TERRA_M-T | SANTA RITA DO ARAGUAIA | GOIÁS | Brasil | 5219407 | 52 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 7e142a64-d818-3af1-876b-6af26a929070 | -22.8479 | -49.34941 | 2026-08-21 12:17:00 | TERRA_M-T | ÁGUAS DE SANTA BÁRBARA | SÃO PAULO | Brasil | 3500550 | 35 | 33 | nan | nan | nan | Cerrado | 206.5 |
| f0c1df9e-fcf9-3ae7-983c-a0daefb6b02f | -19.65912 | -46.02093 | 2026-08-21 12:17:00 | TERRA_M-T | CÓRREGO DANTA | MINAS GERAIS | Brasil | 3119807 | 31 | 33 | nan | nan | nan | Cerrado | 62.1 |
| 44f35e53-028a-3146-86ef-100e1b2857ef | -14.3343 | -51.8944 | 2026-08-21 12:20:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 116.2 |
| 93ce0567-8574-3e43-8355-f2f6ba37fa86 | -13.2431 | -51.6295 | 2026-08-21 12:20:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 96.4 |
| ac753a51-727c-3f9e-a3c4-49680dd9d56a | -6.8755 | -59.4364 | 2026-08-21 12:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 69.4 |
| 1e6b06b7-5d36-37a0-ba1c-831ce6e3be5e | -14.715 | -47.1387 | 2026-08-21 12:20:00 | GOES-19 | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 70.0 |
| 027af81b-205d-3f49-883f-bdd86d552ca4 | -22.8482 | -49.3487 | 2026-08-21 12:20:00 | GOES-19 | ÁGUAS DE SANTA BÁRBARA | SÃO PAULO | Brasil | 3500550 | 35 | 33 | nan | nan | nan | Cerrado | 174.8 |
| b61b48e6-79c5-35b6-8096-e8b50865e05c | -5.5978 | -44.0209 | 2026-08-21 12:20:00 | GOES-19 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 91.4 |
| e987ce5e-71a6-396b-9b60-6ce72229f53b | -9.4071 | -60.417 | 2026-08-21 12:20:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 74.4 |
| a47cac86-e93e-3f88-ab2b-8069f483ce59 | -11.1747 | -54.0216 | 2026-08-21 12:20:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 79.4 |
| 200c61f2-fa1d-36da-bdfd-c16b4e789c78 | -5.6168 | -43.9965 | 2026-08-21 12:20:00 | GOES-19 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 76.7 |
| 02302b75-7346-3542-91dd-9c4a34e558d6 | -8.3717 | -62.716 | 2026-08-21 12:20:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 64.7 |
| 5f0ca748-b88a-3560-8ce5-a6522515a5c7 | -5.598 | -43.9978 | 2026-08-21 12:20:00 | GOES-19 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 93.4 |
| 191ed659-d23a-38b3-a5d1-7a6f26e4ceef | -5.6166 | -44.0196 | 2026-08-21 12:20:00 | GOES-19 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 75.6 |
| 49f0ce59-b53b-3833-bea5-7e9dd47a6f28 | -6.2341 | -55.6109 | 2026-08-21 12:30:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 67.2 |
| f9f46b5a-2e0b-36a1-9d06-b329fd793a9a | -5.6168 | -43.9965 | 2026-08-21 12:30:00 | GOES-19 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 78.0 |
| 0b0978b8-1e55-3da9-b07e-bd4a7c7cd8f9 | -11.1747 | -54.0216 | 2026-08-21 12:30:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 98.3 |
| e93957be-70a5-32e5-adcf-33b7a3b0c06f | -9.4071 | -60.417 | 2026-08-21 12:30:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 83.7 |
| 79e874b6-887e-3f21-88be-4bbea3a53525 | -9.3238 | -56.9064 | 2026-08-21 12:30:00 | GOES-19 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 85.3 |
| 1350e3f2-3e5b-3f72-b0e6-2022012e0fbe | -14.3343 | -51.8944 | 2026-08-21 12:30:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 75.9 |
| 68ed9eb8-e8bf-3d59-95e1-ec595bbf6813 | -16.7194 | -47.6887 | 2026-08-21 12:30:00 | GOES-19 | CRISTALINA | GOIÁS | Brasil | 5206206 | 52 | 33 | nan | nan | nan | Cerrado | 90.8 |
| 316d0ee5-edea-3106-96b8-7bce9c828131 | -13.6624 | -51.7897 | 2026-08-21 12:30:00 | GOES-19 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 127.1 |
| 22b909cd-b4de-3a88-9f4f-0969c84eaa3d | -17.9546 | -44.3882 | 2026-08-21 12:30:00 | GOES-19 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 134.9 |
| b8295250-8146-3116-bd3f-7dc27bdd4630 | -22.8482 | -49.3487 | 2026-08-21 12:30:00 | GOES-19 | ÁGUAS DE SANTA BÁRBARA | SÃO PAULO | Brasil | 3500550 | 35 | 33 | nan | nan | nan | Cerrado | 115.4 |
| ff309912-ec33-3be9-a9da-cd73d3805b9a | -6.1177 | -59.9069 | 2026-08-21 12:30:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 65.4 |
| 30b5ac92-3c95-316b-ad29-7b029f2b533b | -14.7346 | -47.1354 | 2026-08-21 12:30:00 | GOES-19 | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 108.7 |
| 75cf8506-b8c2-338a-bf6a-368d71bb9686 | -5.5978 | -44.0209 | 2026-08-21 12:30:00 | GOES-19 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 103.4 |
| b567b7c4-8d7d-3cc6-aca7-515659c28603 | -5.598 | -43.9978 | 2026-08-21 12:30:00 | GOES-19 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 82.1 |
| faccb39e-05fc-397e-b1bf-55de696d0138 | -6.8755 | -59.4364 | 2026-08-21 12:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 73.3 |
| 37a6aa46-563d-3116-a3d5-1721bcaba586 | -6.1361 | -59.9063 | 2026-08-21 12:30:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 66.7 |
| 03f8644e-b2d7-3b84-95f3-9e668a7d3cf2 | -5.6166 | -44.0196 | 2026-08-21 12:30:00 | GOES-19 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 101.4 |
| 08ecdc89-b3ea-3aad-a550-373c804af2af | -8.9042 | -60.5385 | 2026-08-21 12:40:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 65.1 |
| 940eafa9-f8cd-3154-ac57-b4731de44a0c | -9.4071 | -60.417 | 2026-08-21 12:40:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 74.0 |
| 90bf5e72-5195-39c8-b79b-4ff777b948d1 | -11.1747 | -54.0216 | 2026-08-21 12:40:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 88.9 |
| 5e0386d1-f135-3dbb-8671-6be3285c43cb | -6.2673 | -48.6494 | 2026-08-21 12:40:00 | GOES-19 | SÃO GERALDO DO ARAGUAIA | PARÁ | Brasil | 1507458 | 15 | 33 | nan | nan | nan | Amazônia | 82.8 |
| 0d7ca890-23e2-31c1-8113-7eaf4b937096 | -19.6591 | -46.0388 | 2026-08-21 12:40:00 | GOES-19 | CÓRREGO DANTA | MINAS GERAIS | Brasil | 3119807 | 31 | 33 | nan | nan | nan | Cerrado | 115.6 |
| 88d38822-94ab-3219-a0ab-9285d0803068 | -8.4554 | -46.9628 | 2026-08-21 12:40:00 | GOES-19 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 80.5 |
| 8ad2d8ac-59cb-3760-9a68-f64917c0b105 | -21.5784 | -41.1856 | 2026-08-21 12:40:00 | GOES-19 | SÃO FRANCISCO DE ITABAPOANA | RIO DE JANEIRO | Brasil | 3304755 | 33 | 33 | nan | nan | nan | Mata Atlântica | 191.6 |
| becb7843-62b6-3c99-be37-dc79a47dbc6a | -5.5978 | -44.0209 | 2026-08-21 12:40:00 | GOES-19 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 318.1 |
| 3238ac60-e092-359d-9bfa-4feb5fcd6cb6 | -6.8756 | -59.4171 | 2026-08-21 12:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 62.1 |
| 05bdc9c4-fcb6-3cc9-97f6-59dbc9229f37 | -13.6624 | -51.7897 | 2026-08-21 12:40:00 | GOES-19 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 125.1 |
| aa7b635e-333d-3de5-a633-8918b7a6dfe9 | -17.9345 | -44.3929 | 2026-08-21 12:40:00 | GOES-19 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 148.5 |
| 19257ef4-db82-3da9-a062-87e01f873d7f | -14.3343 | -51.8944 | 2026-08-21 12:40:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 79.8 |
| bc54512a-4c87-3f71-8fd9-73057b9a6637 | -5.6166 | -44.0196 | 2026-08-21 12:40:00 | GOES-19 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 113.3 |


[Clique aqui para ver as próximas entradas](README90.md)
