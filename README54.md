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

## Dados Diários - Página 54

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| c67a01e2-49f4-3776-b10d-5d2ab7579991 | -7.05306 | -59.84493 | 2026-08-20 05:06:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d204e7e4-ee0b-35b4-a0d4-549a5cbc95ad | -11.18236 | -54.80292 | 2026-08-20 05:06:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4a2789fd-05aa-3145-8047-aeb0a48e76f4 | -9.51069 | -51.63651 | 2026-08-20 05:06:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 329bfaf6-53e4-36d6-9f9c-b1edb831a0bf | -7.37742 | -55.53938 | 2026-08-20 05:06:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e0304b8c-4a10-3f42-adcd-0a848ed6f2c0 | -11.18538 | -54.01542 | 2026-08-20 05:06:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| a5e21ed9-c837-30b9-a19f-88c6445197c7 | -9.5147 | -51.63706 | 2026-08-20 05:06:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| c160c785-20f2-38a4-be6b-21d0c21cc7e4 | -11.46223 | -46.56734 | 2026-08-20 05:06:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 17.1 |
| 91bb8bb0-3d89-3662-8258-4a565929b1b8 | -7.60186 | -60.95221 | 2026-08-20 05:06:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| f7a2dc12-21b0-330e-8293-2d1763619a95 | -9.39055 | -60.55806 | 2026-08-20 05:06:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 7fbec6b6-dcfd-3abb-ad04-bd088318186b | -11.42375 | -54.33444 | 2026-08-20 05:06:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| dc24e710-7e5a-31a3-96ad-a2d92a0b1223 | -9.21021 | -59.78404 | 2026-08-20 05:06:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 8d8f4334-e906-3242-97c6-ddfd7d8a0e4f | -10.33786 | -57.56936 | 2026-08-20 05:06:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 9f6d8074-26d7-35e4-88e8-bfa5a76376c9 | -8.57429 | -54.67289 | 2026-08-20 05:06:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ae3d8901-2f30-387e-a6cf-069c3f0b4889 | -10.11104 | -54.28487 | 2026-08-20 05:06:00 | NOAA-21 | MATUPÁ | MATO GROSSO | Brasil | 5105606 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| bedddbe7-3921-3635-8f11-7f73d8876634 | -10.38696 | -61.2157 | 2026-08-20 05:06:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 079bd621-06ce-3403-a31c-f1ccd84998c9 | -10.38863 | -61.20598 | 2026-08-20 05:06:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 50174346-ed3a-35d8-8a1f-fb01a089798f | -6.88476 | -59.03749 | 2026-08-20 05:06:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 2525d67b-45ed-3135-8789-b3a39ed97b11 | -10.919 | -57.18386 | 2026-08-20 05:06:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 9c8630fb-83eb-3aac-b267-8c6853b34ae1 | -8.57032 | -54.67606 | 2026-08-20 05:06:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 33123b0a-a238-3e7a-bb54-84fdad321046 | -9.25783 | -56.91289 | 2026-08-20 05:06:00 | NOAA-21 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a83b823c-1672-3754-83de-d23d22ea88e5 | -11.43069 | -47.24978 | 2026-08-20 05:06:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 0fb483c7-65e7-3264-93d3-ac8ccf5a8668 | -6.87177 | -59.02689 | 2026-08-20 05:06:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 17169740-0df9-370e-ae5e-87ca25e4ebb6 | -7.76946 | -61.13735 | 2026-08-20 05:06:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| ae3c018f-5a75-3a29-8dac-f6e17cd2caae | -6.79311 | -59.57963 | 2026-08-20 05:06:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8f662ddc-5a95-3240-9463-c7cceaee3d24 | -10.83174 | -50.29626 | 2026-08-20 05:06:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 6747db62-ef69-347f-9985-0194e177818b | -10.75656 | -50.34901 | 2026-08-20 05:06:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 92f17040-bbe3-3608-bc4b-977e5ad47a22 | -7.86892 | -63.76045 | 2026-08-20 05:06:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 946297d5-370b-317a-b9f1-5fccb8d10a74 | -13.54463 | -52.22839 | 2026-08-20 05:06:00 | NOAA-21 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 8f711794-d26d-37cf-b902-75a6cc1e2ee6 | -6.84738 | -59.01866 | 2026-08-20 05:06:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 06246287-48e0-373d-9d80-c7a9cdd4b9eb | -8.58075 | -54.77534 | 2026-08-20 05:06:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 8dd7a3d0-372f-33b5-9114-68f68446bb0a | -8.54072 | -54.86982 | 2026-08-20 05:06:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| df1f88b9-9c97-37f5-bfba-e73bf2abf600 | -8.09733 | -51.66192 | 2026-08-20 05:06:00 | NOAA-21 | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 9f119eaf-ca3d-3470-b6bf-d9371283e0e2 | -8.59302 | -54.73977 | 2026-08-20 05:06:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| ccd801ed-9010-3e05-9b93-3dc58fa1ddc4 | -10.8344 | -50.29853 | 2026-08-20 05:06:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| a8e249a1-b75c-39e5-a89c-45ca1d528509 | -10.38394 | -61.21016 | 2026-08-20 05:06:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 10.0 |
| 7fc2195a-d2e4-3b4a-85c1-21094712cf28 | -8.22004 | -55.0277 | 2026-08-20 05:06:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 4e95deb8-1fa4-337d-8caa-fe7652d4aab2 | -9.17444 | -57.01053 | 2026-08-20 05:06:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 258d8e87-d1de-3c5a-8d62-639b125b480d | -10.91955 | -57.18036 | 2026-08-20 05:06:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 75220663-94dc-3c26-8b95-166b41c3c02a | -14.44682 | -45.61897 | 2026-08-20 05:06:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 4b4a2d52-0070-379e-951a-23fb80e589e2 | -8.5567 | -54.65135 | 2026-08-20 05:06:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| aa9ca203-a3f1-3967-8d99-f07a96725204 | -11.8192 | -56.59897 | 2026-08-20 05:06:00 | NOAA-21 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 785ba58a-b662-309b-ae31-83aacaccfe39 | -12.49624 | -54.74251 | 2026-08-20 05:06:00 | NOAA-21 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 6.4 |
| ca3cb79f-8c8f-32cf-b513-d6d4b7997a17 | -8.55466 | -54.77868 | 2026-08-20 05:06:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 97d361dc-949b-302d-ab98-f49d28f6e487 | -7.5542 | -55.56036 | 2026-08-20 05:06:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 45c41b50-57f2-3d2e-9666-eb2f6cb2ef2d | -12.75885 | -48.46058 | 2026-08-20 05:06:00 | NOAA-21 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 00fcca7a-d66d-3562-96ea-26b0a9e23c31 | -7.48166 | -55.32657 | 2026-08-20 05:06:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| aeaf199f-1126-32f3-b040-94609a228c34 | -9.21957 | -59.77256 | 2026-08-20 05:06:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 1e9f72d0-d7c4-3db1-9813-1ec6eda68897 | -11.835 | -58.84845 | 2026-08-20 05:06:00 | NOAA-21 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 069d48f7-7796-362c-a377-13b6bc41dc0b | -11.4627 | -46.56346 | 2026-08-20 05:06:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 17.1 |
| 76f3ccab-f164-318f-93b5-c05d150daf39 | -6.92095 | -59.34702 | 2026-08-20 05:06:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 6e1a8dd5-373a-3429-ba12-b6e10e009b57 | -11.99908 | -53.436 | 2026-08-20 05:06:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 4.6 |
| deb6ed41-8b21-3332-b4d6-de86a1fcfac3 | -7.40556 | -55.53305 | 2026-08-20 05:06:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 54657363-864b-36a1-a586-ee34c3d99b4b | -9.45562 | -51.60797 | 2026-08-20 05:06:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| e3e33537-1934-3f0c-8973-eee7c67d7a3f | -12.38513 | -46.45509 | 2026-08-20 05:06:00 | NOAA-21 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 98a2777a-a161-39cd-9081-10155ac16a62 | -11.21843 | -55.05713 | 2026-08-20 05:06:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 60278fc9-372f-307f-84ac-6cec6e9e6a49 | -10.38478 | -61.20529 | 2026-08-20 05:06:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 10.0 |
| eb7f1ca9-48d1-36e1-807d-b6cb0e96364c | -14.11833 | -44.38474 | 2026-08-20 05:06:00 | NOAA-21 | FEIRA DA MATA | BAHIA | Brasil | 2910776 | 29 | 33 | nan | nan | nan | Cerrado | 3.5 |
| d3bb54c9-4e6f-3339-adea-dafdfe34cb53 | -10.83383 | -50.30299 | 2026-08-20 05:06:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 27703921-cd68-31ec-99ee-aedf16266fae | -7.61113 | -60.96953 | 2026-08-20 05:06:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| d1c8a185-7451-3727-9dd1-484f6c850d31 | -8.5631 | -54.7688 | 2026-08-20 05:06:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2c9de90b-a54b-32df-a97e-a2cd9863c480 | -6.85386 | -59.02396 | 2026-08-20 05:06:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 89d621fe-4ecb-3abb-bae4-71de52b3c7fd | -9.10607 | -60.92628 | 2026-08-20 05:06:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 7.5 |
| f018ffd1-1468-3dde-866b-9f77c4fef34d | -13.40537 | -54.38054 | 2026-08-20 05:06:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 9.1 |
| aec72b30-bf53-37ed-80c3-68ceb54e8c00 | -11.19107 | -54.01891 | 2026-08-20 05:06:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 51a91ec0-cc4b-3951-8139-16b46c3171c7 | -9.10406 | -60.92868 | 2026-08-20 05:06:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 11.6 |
| 23d49f54-bac9-3548-b47d-f3bcb96f7cb5 | -10.78413 | -50.31222 | 2026-08-20 05:06:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 12.0 |
| c12186bc-416b-30b5-b13d-8339f7a7db65 | -13.44525 | -51.81295 | 2026-08-20 05:06:00 | NOAA-21 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| bcedfff7-1bed-37b0-b9f5-9f0ea65e8cd5 | -10.34119 | -57.56988 | 2026-08-20 05:06:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d5b403d7-5230-3e45-a556-d9d6cdced8e6 | -10.84172 | -57.5243 | 2026-08-20 05:06:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7fb3517e-d614-3609-988c-aa7f67347338 | -14.45374 | -45.61446 | 2026-08-20 05:06:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 11.5 |
| e354f24f-7d04-388a-b9f3-847dea4b4fe1 | -8.03538 | -54.02344 | 2026-08-20 05:06:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 997c76a0-64be-33cc-a2c8-36c6db1946f6 | -9.46011 | -51.60518 | 2026-08-20 05:06:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 01261d8e-4c91-33ef-a7e2-bc57c296b38e | -12.00586 | -53.44161 | 2026-08-20 05:06:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 45339aea-2bb0-3c6d-8206-e6c574467f20 | -12.1609 | -57.22318 | 2026-08-20 05:06:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e0282533-f3e6-3bfc-9b3e-b3770ed60913 | -9.38979 | -60.56268 | 2026-08-20 05:06:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 2766771f-daec-3f17-bae0-df607e565c99 | -8.49292 | -54.86605 | 2026-08-20 05:06:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 05b4040a-f534-3afa-90b1-4fe4741a6952 | -8.55646 | -55.32037 | 2026-08-20 05:06:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ecf26bbf-cc4c-3f73-beec-d41c71459833 | -12.82628 | -48.43565 | 2026-08-20 05:06:00 | NOAA-21 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 7723cf3d-64b5-3416-b8e4-421816ee4549 | -8.49629 | -54.86658 | 2026-08-20 05:06:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 5942bfbe-affa-34ca-9204-88a0fcc71601 | -12.16421 | -57.22371 | 2026-08-20 05:06:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7b7b2aee-1720-3cf7-b500-403617bc4ebc | -6.81175 | -58.99747 | 2026-08-20 05:06:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 67ce3f7a-0ca0-3328-90b1-d187edd93312 | -8.53945 | -54.78751 | 2026-08-20 05:06:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| a5e89d73-c03a-3373-8a0d-58e6434ce60d | -7.87454 | -61.58723 | 2026-08-20 05:06:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e6f6c69a-93ce-3df0-9d11-089b4d37b562 | -6.96144 | -59.05367 | 2026-08-20 05:06:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.2 |
| e2dcf55a-67c2-37e3-bb8e-22eb4d7628c5 | -11.23875 | -54.82735 | 2026-08-20 05:06:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| c671c37d-bb0b-3a40-92be-f98395234383 | -10.14886 | -54.27054 | 2026-08-20 05:06:00 | NOAA-21 | MATUPÁ | MATO GROSSO | Brasil | 5105606 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| af70effb-4b2a-36b8-8bbe-9fca11424791 | -8.72087 | -49.61612 | 2026-08-20 05:06:00 | NOAA-21 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 9840db12-ea43-33eb-97ac-b9f42867871e | -13.45299 | -51.78613 | 2026-08-20 05:06:00 | NOAA-21 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 1b6f6d6a-f8fb-382c-8244-e81b75257b03 | -8.56634 | -54.65659 | 2026-08-20 05:06:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 7c3b946a-6ac9-3e36-a894-086f33154845 | -13.6569 | -51.77541 | 2026-08-20 05:06:00 | NOAA-21 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 460c739a-07f8-382b-a112-e5fc76a23636 | -11.37873 | -46.37471 | 2026-08-20 05:06:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 2569548c-37dd-305e-ae85-9a5e29e06b67 | -12.93897 | -56.63146 | 2026-08-20 05:06:00 | NOAA-21 | NOVA MUTUM | MATO GROSSO | Brasil | 5106224 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7bc934cf-4e2a-389f-8ade-aad06a4f2a93 | -7.38073 | -55.53989 | 2026-08-20 05:06:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| df7f458e-811d-3543-a856-1850c1f1bcd7 | -13.40876 | -54.37059 | 2026-08-20 05:06:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d9d9a5f4-a9d9-3387-ad81-c624ad7879f7 | -7.01246 | -59.54526 | 2026-08-20 05:06:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| cdafee61-9869-3fc8-b7f4-fa14b2ac862e | -8.49575 | -54.87019 | 2026-08-20 05:06:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 12efe2b9-9284-3fb1-9f4a-4121a6e49b89 | -13.48014 | -51.43961 | 2026-08-20 05:06:00 | NOAA-21 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f9c44eca-701b-3cbf-a3a7-1215aa040825 | -8.58304 | -54.78316 | 2026-08-20 05:06:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 60da2dc7-2bd6-353d-a097-5ff3f71f3a24 | -7.83253 | -61.61068 | 2026-08-20 05:06:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ffb3927f-f297-30ad-956e-f75c8c37d0aa | -7.55474 | -55.55688 | 2026-08-20 05:06:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |


[Clique aqui para ver as próximas entradas](README55.md)
