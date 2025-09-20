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

## Dados Diários - Página 27

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 16ed0761-e1f4-32d8-bf23-9f04b268c88a | -8.17512 | -55.17437 | 2025-09-20 05:16:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 8af57433-3563-3f09-abf4-d6526f4fe22a | -9.71373 | -55.61418 | 2025-09-20 05:16:00 | NOAA-20 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ed69983c-aa57-300c-b4e0-108295101738 | -9.67851 | -63.17506 | 2025-09-20 05:16:00 | NOAA-20 | ALTO PARAÍSO | RONDÔNIA | Brasil | 1100403 | 11 | 33 | nan | nan | nan | Amazônia | 0.6 |
| dd491da1-55df-354a-a5dc-18d69adebd9c | -5.69401 | -51.74216 | 2025-09-20 05:16:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 64517ce4-9b2c-3e88-9e91-672f79af3602 | -3.73907 | -53.80649 | 2025-09-20 05:16:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 83703e1f-064d-373b-8f5a-14df2c00cf5e | -11.28659 | -47.41986 | 2025-09-20 05:16:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| cbb5182b-fe2f-394a-b12e-2d55aee77bcb | -9.6596 | -62.27263 | 2025-09-20 05:16:00 | NOAA-20 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 63a4a99b-134c-37df-9aa0-0d03290ca39b | -9.34554 | -57.43785 | 2025-09-20 05:16:00 | NOAA-20 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| d9788b2d-5840-369e-92d9-f26e698dcfe0 | -9.5273 | -63.5766 | 2025-09-20 05:16:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 4ccb4eaa-f700-324e-9257-48d182401960 | -5.76237 | -53.41755 | 2025-09-20 05:16:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 5093c237-cd36-394d-a14a-9b510751ce7a | -9.39468 | -54.68728 | 2025-09-20 05:16:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 8fce1632-0f43-32bb-be83-e8006000959b | -9.39268 | -54.70137 | 2025-09-20 05:16:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| cc25d967-0343-3eb6-8276-3a7c215b1d4c | -11.16877 | -49.93605 | 2025-09-20 05:16:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| f5233852-6ac9-3e14-bf72-fe11269e8cff | -9.41434 | -63.69226 | 2025-09-20 05:16:00 | NOAA-20 | ALTO PARAÍSO | RONDÔNIA | Brasil | 1100403 | 11 | 33 | nan | nan | nan | Amazônia | 3.6 |
| b4b66872-d57a-3211-b329-74e5882c34a6 | -9.96533 | -57.758 | 2025-09-20 05:16:00 | NOAA-20 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 70df6e3c-c6f5-3428-936b-b5f9f95075c8 | -9.84591 | -59.88145 | 2025-09-20 05:16:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 2a07f6e4-0cc9-36a8-93bc-941ec5ce242c | -9.40766 | -54.68208 | 2025-09-20 05:16:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 238bf876-917a-3bc5-9592-7f631c023433 | -3.90917 | -59.59615 | 2025-09-20 05:16:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ade202c4-d63a-3409-befa-82e7217d9050 | -9.50988 | -54.66399 | 2025-09-20 05:16:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 6ee07cb0-d678-3765-97e0-8044bc7bce8b | -3.20328 | -58.00143 | 2025-09-20 05:16:00 | NOAA-20 | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| aa6d11f0-6227-3006-9a14-492a9bdc6eda | -3.44249 | -56.93187 | 2025-09-20 05:16:00 | NOAA-20 | BARREIRINHA | AMAZONAS | Brasil | 1300508 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 03c6cd92-cda6-3406-a58a-af0177d8f032 | -9.67026 | -62.93053 | 2025-09-20 05:16:00 | NOAA-20 | RIO CRESPO | RONDÔNIA | Brasil | 1100262 | 11 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 00c03c7a-9957-3ffa-b151-d9456b267b2a | -3.74454 | -57.01788 | 2025-09-20 05:16:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a8c47d0c-2c9c-3f7b-ab6a-7f2db11fdeee | -4.4773 | -54.85215 | 2025-09-20 05:16:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 8e225f48-f992-3dda-a6c3-6b69970c204c | -8.66555 | -63.8562 | 2025-09-20 05:16:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e62a836e-9ad6-342d-9d5d-5e3b48066187 | -9.7667 | -62.32688 | 2025-09-20 05:16:00 | NOAA-20 | VALE DO ANARI | RONDÔNIA | Brasil | 1101757 | 11 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 49d11e03-3856-32eb-a9c7-1acfde861e50 | -9.68185 | -63.17301 | 2025-09-20 05:16:00 | NOAA-20 | ALTO PARAÍSO | RONDÔNIA | Brasil | 1100403 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 9de1da8e-67af-3a8b-846e-cbb3758bd678 | -6.10725 | -47.85103 | 2025-09-20 05:16:00 | NOAA-20 | CACHOEIRINHA | TOCANTINS | Brasil | 1703826 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 25f45d6a-d5da-3c2d-b748-b0679de1477c | -9.40995 | -57.0353 | 2025-09-20 05:16:00 | NOAA-20 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b208c87e-00f0-3651-9260-8616cd87f6a9 | -9.52807 | -63.57204 | 2025-09-20 05:16:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a89bfeeb-c2a4-3c94-89f0-b722f6dc0357 | -5.7665 | -53.41811 | 2025-09-20 05:16:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| aeeb54f6-61b9-3a84-9be2-2c3bb707b4f1 | -5.80819 | -53.43876 | 2025-09-20 05:16:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 4239cf7c-8efd-31c4-8d87-e600e7b4f387 | -4.92439 | -47.54265 | 2025-09-20 05:16:00 | NOAA-20 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 489784df-0f2f-390d-9eaa-85f7b6fd1b95 | -9.40977 | -63.69622 | 2025-09-20 05:16:00 | NOAA-20 | ALTO PARAÍSO | RONDÔNIA | Brasil | 1100403 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 45d146b9-af6d-32cc-8546-61cc4ff8021c | -6.34744 | -49.85904 | 2025-09-20 05:16:00 | NOAA-20 | CANAÃ DOS CARAJÁS | PARÁ | Brasil | 1502152 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 718a0e48-136e-31db-b883-1abe81e37786 | -7.83024 | -45.64152 | 2025-09-20 05:16:00 | NOAA-20 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 3e646581-9dbc-3313-8f44-13a51591de16 | -9.39867 | -54.68787 | 2025-09-20 05:16:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 92b04e0b-2405-3b02-b08f-d51658f8b009 | -9.45818 | -54.67159 | 2025-09-20 05:16:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 92ca4a57-216c-3c4f-a5f3-05c55eff4f67 | -5.04717 | -47.90257 | 2025-09-20 05:16:00 | NOAA-20 | CIDELÂNDIA | MARANHÃO | Brasil | 2103257 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4571a464-1546-3f9b-b635-11e6bef97678 | -10.21499 | -59.52242 | 2025-09-20 05:16:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| cdebc949-6045-31b3-b794-69f132ea6a71 | -8.19582 | -49.67432 | 2025-09-20 05:16:00 | NOAA-20 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 98ee40d9-3d95-3ad1-aa4d-72571ec41535 | -3.982 | -51.06219 | 2025-09-20 05:16:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 6824d0a7-ef15-36f4-8368-03718221c935 | -5.1419 | -60.37718 | 2025-09-20 05:16:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 02aea889-e3ae-37a3-9f61-8544ea37da43 | -3.98276 | -51.057 | 2025-09-20 05:16:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 45a0bc1c-0114-3c16-9d44-e2a348003052 | -5.69796 | -51.74759 | 2025-09-20 05:16:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| fc573782-6caa-314c-8aa9-4015be696c37 | -9.40616 | -54.69258 | 2025-09-20 05:16:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 951c5ad2-a0d1-3354-adb7-a9f56a039871 | -8.92168 | -54.44868 | 2025-09-20 05:16:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 9715834a-3fd4-353d-aedd-7192adaf4fd7 | -9.84923 | -59.88198 | 2025-09-20 05:16:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a97d11a5-c420-3c20-b4ed-1c0da03442fe | -4.66691 | -49.32619 | 2025-09-20 05:16:00 | NOAA-20 | JACUNDÁ | PARÁ | Brasil | 1503804 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| b3b2bb0a-d40a-3ece-ba16-6038883615b0 | -6.91289 | -59.91293 | 2025-09-20 05:16:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 99c57010-0668-36f0-8201-14240a729afd | -11.28486 | -47.41484 | 2025-09-20 05:16:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| afd36954-3a4d-3953-b8f4-e91eeebcbacf | -9.67818 | -63.1724 | 2025-09-20 05:16:00 | NOAA-20 | ALTO PARAÍSO | RONDÔNIA | Brasil | 1100403 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 71ddc52b-e3a1-3006-a8c0-1aa882fc2bc1 | -8.76792 | -61.44205 | 2025-09-20 05:16:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 36e0fde7-5f09-3b8d-a671-032045782ce2 | -9.41115 | -54.6862 | 2025-09-20 05:16:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 245620bc-0bc1-3976-a5f0-7ee01c8e556e | -7.83119 | -45.63428 | 2025-09-20 05:16:00 | NOAA-20 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 2971b202-5565-383d-a8ec-93df03a51a55 | -10.24709 | -58.48229 | 2025-09-20 05:16:00 | NOAA-20 | JURUENA | MATO GROSSO | Brasil | 5105176 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| b3054396-d062-3c06-9a24-bf2799c4d40e | -7.83575 | -45.63723 | 2025-09-20 05:16:00 | NOAA-20 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| f4d5d5f8-a8dc-3279-a521-a1b5efd5e7cb | -6.34787 | -49.85601 | 2025-09-20 05:16:00 | NOAA-20 | CANAÃ DOS CARAJÁS | PARÁ | Brasil | 1502152 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 343e94de-1cc0-3dfa-ba51-a1f926630dd9 | -5.23404 | -56.01683 | 2025-09-20 05:16:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 1f409161-10dd-3d10-9d81-119415201115 | -9.35881 | -54.52655 | 2025-09-20 05:16:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f651c0dc-fa4b-359a-9103-ead59d672c50 | -4.47859 | -54.85427 | 2025-09-20 05:16:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| b201f062-d75c-31ad-bf80-2a86dc012d10 | -9.39318 | -54.69788 | 2025-09-20 05:16:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 27829c90-d6a9-3ed8-bb9e-b5e883d06332 | -15.3425 | -59.40376 | 2025-09-20 05:18:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 36848dcf-5e6f-37ed-aab8-f33cedc159a3 | -15.30442 | -56.81431 | 2025-09-20 05:18:00 | NOAA-20 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| f9f2e157-c0ab-37b5-a3b4-5f0655982b73 | -15.27884 | -56.85886 | 2025-09-20 05:18:00 | NOAA-20 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 288124a7-65ef-33eb-90d2-3e6e55c8f9e5 | -11.64139 | -52.86527 | 2025-09-20 05:18:00 | NOAA-20 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 0290f69e-b042-3396-afcd-63c904097e8a | -11.64207 | -52.86028 | 2025-09-20 05:18:00 | NOAA-20 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 773a3a5f-3807-355f-9add-e27a3c540de1 | -15.31897 | -56.82112 | 2025-09-20 05:18:00 | NOAA-20 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 61c92ebc-d84d-32f1-b086-289345dc6e4f | -12.00837 | -64.83669 | 2025-09-20 05:18:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.9 |
| e4234292-1b93-3142-aa12-ae1683c80563 | -15.28574 | -56.86477 | 2025-09-20 05:18:00 | NOAA-20 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 159281ac-f034-385a-b4d6-49f3480f7904 | -15.90795 | -59.41156 | 2025-09-20 05:18:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 5f5b825b-82a2-3380-90b6-e4d77b910a35 | -14.83306 | -60.25047 | 2025-09-20 05:18:00 | NOAA-20 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| b2aab2fa-aad8-3806-ae7b-8d7d1e6e1b52 | -15.92548 | -59.43372 | 2025-09-20 05:18:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1d5818bf-7108-3621-ae7d-3cfb7779a746 | -12.89051 | -62.1274 | 2025-09-20 05:18:00 | NOAA-20 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2c3b8234-7f7e-3dd7-b61d-4b57d9f3ffce | -9.74322 | -64.43076 | 2025-09-20 05:18:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ec13a443-7e34-3de4-879f-58710be49e36 | -12.00004 | -63.52762 | 2025-09-20 05:18:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 5c1705cd-1812-3ef9-8898-4a8a522f07ce | -15.9249 | -59.43753 | 2025-09-20 05:18:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 09835551-2213-3c6b-b48b-694f8fc407d2 | -15.91579 | -59.45171 | 2025-09-20 05:18:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 0b8cdb90-5778-39d3-a216-be75c99b8f91 | -10.29862 | -67.36597 | 2025-09-20 05:18:00 | NOAA-20 | PLÁCIDO DE CASTRO | ACRE | Brasil | 1200385 | 12 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7933f0bd-6afb-3ab4-a1af-208001609bde | -14.83914 | -60.25517 | 2025-09-20 05:18:00 | NOAA-20 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3f1e0358-1d58-3141-b521-52765d48dd65 | -15.31515 | -56.82074 | 2025-09-20 05:18:00 | NOAA-20 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 7ce76f4f-ba92-3d82-bc5a-dfc0229a2220 | -15.27637 | -56.84879 | 2025-09-20 05:18:00 | NOAA-20 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 5.9 |
| dff35900-e644-3d30-8e5f-d203b1f7baa9 | -13.23133 | -57.13005 | 2025-09-20 05:18:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 2c4b88f0-fcfc-3bca-9445-0231310783e1 | -15.27968 | -56.82507 | 2025-09-20 05:18:00 | NOAA-20 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| bca8ec7f-9800-312e-b6d4-10b3e79b78ab | -12.85281 | -53.00542 | 2025-09-20 05:18:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 613f4173-0772-3b08-8a00-fa8ac53c7399 | -15.82104 | -59.50483 | 2025-09-20 05:18:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 03a24b4d-e3c3-3c6d-ab1b-72a10d2253f8 | -11.63672 | -52.86466 | 2025-09-20 05:18:00 | NOAA-20 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 0d28bd4e-f47e-37b8-841e-f818c0aa3f08 | -15.27819 | -56.86349 | 2025-09-20 05:18:00 | NOAA-20 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 7e75e1b3-675c-369b-83a7-eca031fabe80 | -15.77198 | -59.38593 | 2025-09-20 05:18:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 63cd3bfb-bc17-3a05-8532-36b0d092cbc9 | -9.47074 | -67.89105 | 2025-09-20 05:18:00 | NOAA-20 | PORTO ACRE | ACRE | Brasil | 1200807 | 12 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4556fbae-c61f-3394-97ee-2957b4f093b8 | -15.91919 | -59.45222 | 2025-09-20 05:18:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 0ef94f75-02a3-3cfc-96d0-21e5499ebfc0 | -15.34645 | -59.40053 | 2025-09-20 05:18:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 3.9 |
| d9e4349e-f47f-3423-9a6a-7e7a41924472 | -15.76859 | -59.38535 | 2025-09-20 05:18:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 0.1 |
| 891fe96c-cf86-3028-9a7d-69b8dfa608a2 | -15.92605 | -59.42991 | 2025-09-20 05:18:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 638fef8a-263c-38cc-b2c8-43391cf7b3f7 | -15.91184 | -59.45488 | 2025-09-20 05:18:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1e21001d-2e66-3d57-b531-57bc7b68ef8d | -16.11082 | -53.80776 | 2025-09-20 05:18:00 | NOAA-20 | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| e4414596-ed92-36dd-9f44-d487df97dd58 | -15.28479 | -56.8162 | 2025-09-20 05:18:00 | NOAA-20 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 4e59cf4f-1f23-3056-afa3-cf952f528bce | -15.77772 | -52.18409 | 2025-09-20 05:18:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b50f81e1-fec2-3c41-9aad-6c369b372906 | -12.85344 | -53.00041 | 2025-09-20 05:18:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 4.5 |
| f3a23b23-92d8-3334-9c6e-1d2d5b66ddf5 | -15.90902 | -59.45059 | 2025-09-20 05:18:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |


[Clique aqui para ver as próximas entradas](README28.md)
