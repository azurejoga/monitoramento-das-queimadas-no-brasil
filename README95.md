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

## Dados Diários - Página 95

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| a969baf8-b3a3-3c2d-a51b-f8431df04f05 | -3.4195 | -50.3844 | 2024-10-06 04:35:25 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 57.4 |
| db66650c-f3fb-3736-874f-5dbb956a2e93 | -3.3084 | -50.451 | 2024-10-06 04:35:25 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 39.6 |
| 8c3c3808-dfd9-3ff7-8f2c-8726804acf23 | -6.9514 | -59.0666 | 2024-10-06 04:35:46 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 58.6 |
| e56102fd-f652-3339-bd8e-9b9e0aa36c96 | -9.3278 | -46.5385 | 2024-10-06 04:35:59 | GOES-16 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 61.6 |
| d7491b56-00b2-3cbd-8800-fdcf95e9162a | -9.8552 | -60.2966 | 2024-10-06 04:36:02 | GOES-16 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 36.0 |
| 2a2fb1a2-6b0b-3952-a5b9-e55b722b88a1 | -9.6965 | -64.6262 | 2024-10-06 04:36:02 | GOES-16 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 61.1 |
| be6e5fc7-2281-3f0d-bc85-f50bbe403473 | -9.6779 | -64.6269 | 2024-10-06 04:36:02 | GOES-16 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 97.0 |
| d989d368-32a9-3ff3-98cf-85884f5baf4a | -12.6092 | -53.1129 | 2024-10-06 04:36:17 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 85.7 |
| 135af515-608d-3ba3-81ac-53837518ba70 | -12.6089 | -53.1338 | 2024-10-06 04:36:17 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 92.4 |
| 3c859ed2-5209-3635-a32e-1d10a2b904e3 | -12.7634 | -50.5136 | 2024-10-06 04:36:18 | GOES-16 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 163.0 |
| 1d2b5f00-a476-3123-9333-2bc133176275 | -12.763 | -50.5352 | 2024-10-06 04:36:18 | GOES-16 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 195.9 |
| d62f9949-3b34-3b62-9a37-fc1623c7a6b9 | -12.6283 | -53.1108 | 2024-10-06 04:36:18 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 111.3 |
| c8fcaa35-4c42-324d-98ca-41569cd4791f | -12.628 | -53.1317 | 2024-10-06 04:36:18 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 78.6 |
| b7dc6fd5-95a1-3356-a5e4-1758acd4f4ac | -13.3976 | -61.957 | 2024-10-06 04:36:22 | GOES-16 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 72.2 |
| 727874c1-edb3-3b5e-8cf6-2b654a5dc9af | -13.3786 | -61.9582 | 2024-10-06 04:36:22 | GOES-16 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 63.0 |
| a3f79744-59ed-3fe6-992a-b8bbfc3c353e | -13.6728 | -51.1696 | 2024-10-06 04:36:23 | GOES-16 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 79.9 |
| 60d2d7b3-cbe9-3a3a-a50c-1d458675ad86 | -13.6724 | -51.1911 | 2024-10-06 04:36:23 | GOES-16 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 106.6 |
| db6200c1-c2bd-3fc3-bc31-a8c3e029a118 | -15.0565 | -49.474 | 2024-10-06 04:36:30 | GOES-16 | NOVA GLÓRIA | GOIÁS | Brasil | 5214861 | 52 | 33 | nan | nan | nan | Cerrado | 56.6 |
| bcebb144-4863-32a1-94d0-36e6b1a984d1 | -16.3764 | -57.3663 | 2024-10-06 04:36:38 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 80.9 |
| edc26504-02db-3348-ad83-c59159273a62 | -16.5544 | -57.2032 | 2024-10-06 04:36:39 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 83.9 |
| 081bf87a-5fb3-3277-99a9-d43fd1975796 | -16.8238 | -57.4584 | 2024-10-06 04:36:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 88.1 |
| 93573a96-3187-3031-b441-538eb71c9459 | -17.1185 | -57.3834 | 2024-10-06 04:36:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 103.1 |
| f70a56b5-193b-33f5-9bf9-d3997e8a1333 | -17.1182 | -57.4039 | 2024-10-06 04:36:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 127.3 |
| d936e3d1-5e26-33d0-ba5b-f30b58d3b34a | -17.0905 | -56.6884 | 2024-10-06 04:36:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 103.5 |
| b46f2fc9-595b-3f40-bf48-fa24a7ec0d46 | -16.9717 | -56.7646 | 2024-10-06 04:36:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 104.4 |
| 4f68c959-3ca0-366a-9317-b073d4fb9f3f | -17.1375 | -57.4221 | 2024-10-06 04:36:43 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 96.5 |
| c09935f0-5f97-3c20-95f5-363deb809795 | -17.8319 | -53.7829 | 2024-10-06 04:36:46 | GOES-16 | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | 92.2 |
| 24c7fa1b-90e1-3665-86c1-34bca6e09048 | -17.812 | -53.7859 | 2024-10-06 04:36:46 | GOES-16 | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | 117.8 |
| aec3e9e8-010d-3154-a78a-99067ed13457 | -18.659 | -57.2552 | 2024-10-06 04:36:51 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 85.4 |
| fef13f5c-4717-3fbc-8552-7a8d50076350 | -18.6586 | -57.2759 | 2024-10-06 04:36:51 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 78.8 |
| e6580082-ffe6-3c6d-a64c-93ada4c1de3f | -18.6391 | -57.2578 | 2024-10-06 04:36:51 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 82.0 |
| e0e94f0d-a69d-38b6-bcbc-72c2deb95536 | -18.6387 | -57.2785 | 2024-10-06 04:36:51 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 137.1 |
| 766130f7-2965-3d4f-ba2f-065b7fa0d6f9 | -6.9514 | -59.0666 | 2024-10-06 04:45:46 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 56.3 |
| a9a4dae9-1173-31bc-ad00-7dbce64a513a | -7.1532 | -59.2898 | 2024-10-06 04:45:47 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 33.8 |
| 993f995b-c98a-302d-8e5a-6a555f4519d6 | -9.6779 | -64.6269 | 2024-10-06 04:46:02 | GOES-16 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 73.6 |
| 2720e699-b914-3049-8360-8e24627efb40 | -9.6965 | -64.6262 | 2024-10-06 04:46:02 | GOES-16 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 86.0 |
| ded5202a-a06f-31a6-868c-34bc44951c1a | -13.3786 | -61.9582 | 2024-10-06 04:46:22 | GOES-16 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 69.0 |
| f7b7099f-6232-3e87-b509-91012ccbbd7f | -13.3976 | -61.957 | 2024-10-06 04:46:22 | GOES-16 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 68.1 |
| 5bd24c4d-9b2e-3220-93aa-955a8c957470 | -6.9514 | -59.0666 | 2024-10-06 04:55:46 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 54.8 |
| bff093a1-6a1a-3265-bc03-f15ad8bb3d86 | -20.46 | -51.29 | 2024-10-06 05:03:29 | MSG-03 | ILHA SOLTEIRA | SÃO PAULO | Brasil | 3520442 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 0f039bd8-e5ea-3875-8386-a5f8de5ed7cd | -20.43 | -51.27 | 2024-10-06 05:03:29 | MSG-03 | ILHA SOLTEIRA | SÃO PAULO | Brasil | 3520442 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 6a768753-fae5-3f99-8054-f2a1ebc70ada | -20.46 | -51.35 | 2024-10-06 05:03:29 | MSG-03 | ILHA SOLTEIRA | SÃO PAULO | Brasil | 3520442 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 03a556b7-3a70-38a6-af9f-95397d9664ba | -10.45 | -50.64 | 2024-10-06 05:04:27 | MSG-03 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| b6fe106e-f7b7-3f79-a85b-a0a834ca5308 | -10.45 | -50.7 | 2024-10-06 05:04:27 | MSG-03 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 0d28d5ab-6338-3319-ac26-367bb8fb1a28 | -10.45 | -50.76 | 2024-10-06 05:04:27 | MSG-03 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 890963f6-6273-3309-bb71-d6169ea8d01d | -10.42 | -50.69 | 2024-10-06 05:04:27 | MSG-03 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 8e38368e-77be-3609-9d92-203771a88211 | -10.42 | -50.75 | 2024-10-06 05:04:27 | MSG-03 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 88f96eb2-da8e-392a-bf45-5fbee23d6e69 | 2.17707 | -50.68862 | 2024-10-06 05:08:00 | NOAA-21 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 3cc93751-d00a-3c88-ab70-45fb94b1d846 | 2.17699 | -50.69224 | 2024-10-06 05:08:00 | NOAA-21 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 37faa506-108e-3040-941a-9876a8ddeec1 | 2.16918 | -50.6899 | 2024-10-06 05:08:00 | NOAA-21 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 4.9 |
| c2c6a268-2c0a-378f-a3f0-7f36819c81e3 | 2.16828 | -50.68845 | 2024-10-06 05:08:00 | NOAA-21 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 6.0 |
| de9134e0-5a65-30a3-9745-6008aab6fbbd | 0.98901 | -51.29075 | 2024-10-06 05:08:00 | NOAA-21 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 1.8 |
| f7140805-386a-385a-a7a1-0e56bd109b50 | -5.57475 | -44.87819 | 2024-10-06 05:10:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 18.1 |
| fb8142c4-ff0f-3eba-bd58-7a65b56216e8 | -5.72428 | -43.79375 | 2024-10-06 05:10:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| fd05f907-3f9e-3b3a-8b90-2e6412ff53e1 | -4.01901 | -43.24397 | 2024-10-06 05:10:00 | NOAA-21 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 0e1773f5-36e6-3a45-9196-a2b2667a5b2b | -4.01687 | -43.24426 | 2024-10-06 05:10:00 | NOAA-21 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 7b1b27ba-897f-39dc-8401-ad7c07edd8b5 | -4.01198 | -43.24287 | 2024-10-06 05:10:00 | NOAA-21 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 4ab5b67e-5b9e-318d-9dec-1e9d5b083f5a | -4.00984 | -43.24312 | 2024-10-06 05:10:00 | NOAA-21 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 73fc0bc1-1c82-3723-9b60-af8710c31467 | -5.8257 | -44.13043 | 2024-10-06 05:10:00 | NOAA-21 | JATOBÁ | MARANHÃO | Brasil | 2105450 | 21 | 33 | nan | nan | nan | Cerrado | 6.0 |
| b4d835d8-badc-3b98-9d87-2b554fe1d59c | -5.82481 | -44.13676 | 2024-10-06 05:10:00 | NOAA-21 | JATOBÁ | MARANHÃO | Brasil | 2105450 | 21 | 33 | nan | nan | nan | Cerrado | 6.0 |
| a6df5d1b-8f4c-3a1e-85e7-4d5d6a90d337 | -5.81984 | -44.13075 | 2024-10-06 05:10:00 | NOAA-21 | JATOBÁ | MARANHÃO | Brasil | 2105450 | 21 | 33 | nan | nan | nan | Cerrado | 15.0 |
| f37479e1-3b17-30e7-8c22-70e9f424e924 | -5.819 | -44.13707 | 2024-10-06 05:10:00 | NOAA-21 | JATOBÁ | MARANHÃO | Brasil | 2105450 | 21 | 33 | nan | nan | nan | Cerrado | 14.9 |
| bf51ae63-e243-3ad5-a607-7704982d049e | -5.81885 | -44.12946 | 2024-10-06 05:10:00 | NOAA-21 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 9eaefba8-f6f2-3780-b03f-341af26bfd87 | -5.81797 | -44.13577 | 2024-10-06 05:10:00 | NOAA-21 | JATOBÁ | MARANHÃO | Brasil | 2105450 | 21 | 33 | nan | nan | nan | Cerrado | 6.0 |
| bede7f85-8be7-3b5c-948a-243473021ecd | -5.58128 | -44.87916 | 2024-10-06 05:10:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 13.3 |
| d97a6da4-80d4-3737-9eb6-e46f8dcc4706 | -5.58082 | -44.87848 | 2024-10-06 05:10:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 11.3 |
| 99d84382-3295-3a1b-869e-0ac22302de98 | -5.58053 | -44.88452 | 2024-10-06 05:10:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 9.7 |
| 8a581577-89b2-3a05-8005-bb7bcd1f929e | -5.58011 | -44.88386 | 2024-10-06 05:10:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 11.3 |
| c252ea27-593c-31c8-99ef-06a0700d4eab | -5.57552 | -44.87269 | 2024-10-06 05:10:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 18.1 |
| 861d8b55-1486-3a7c-b7e2-a61e77ae6045 | -5.57503 | -44.87192 | 2024-10-06 05:10:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 10.8 |
| eaf1e310-83c8-3481-9efe-0cdffafb328e | -5.5743 | -44.87745 | 2024-10-06 05:10:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 15.8 |
| 1ebe1888-8b38-39d7-8804-0ca998b61882 | -5.574 | -44.88361 | 2024-10-06 05:10:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 15.1 |
| 24cab787-c166-3881-bed0-42f2bd02bd2f | -5.57358 | -44.8829 | 2024-10-06 05:10:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 15.8 |
| c891ef22-2e2b-3d7e-9018-b08d3cb7f3a4 | -7.2423 | -44.93938 | 2024-10-06 05:10:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 990ea60e-02cc-3384-88d8-ca0af3c0bc35 | -6.73459 | -44.5667 | 2024-10-06 05:10:00 | NOAA-21 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 862b760d-19ea-3681-87ce-61a3f4e8b26c | -4.83524 | -45.81714 | 2024-10-06 05:10:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 200e7d32-66b7-3158-8812-faa5c3bc9a66 | -4.8296 | -45.81704 | 2024-10-06 05:10:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 70102fa5-31cc-37ea-ac5e-060f7e97d087 | -4.82914 | -45.81626 | 2024-10-06 05:10:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| cc229f9f-121f-312b-a3ef-1fc555e0f566 | -4.57899 | -46.06873 | 2024-10-06 05:10:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| d8734671-9ad1-36c6-b1d0-ba727d990559 | -6.35321 | -45.70284 | 2024-10-06 05:10:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 28.7 |
| 305311f4-d256-3f9e-bdd3-d4bf6037ee56 | -6.3526 | -45.70746 | 2024-10-06 05:10:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 28.7 |
| d916e785-0a35-3d5b-b85a-c809237eba2d | -6.352 | -45.71198 | 2024-10-06 05:10:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 18.4 |
| c5f6f7ec-dd62-30a3-9125-b83d0df30902 | -6.35136 | -45.71679 | 2024-10-06 05:10:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 18.4 |
| f61a3b94-4fea-3fce-8c07-cc4946c5459f | -6.3489 | -45.70582 | 2024-10-06 05:10:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 28.6 |
| e9e98759-3bbd-35c1-b339-4908bec63e21 | -6.3483 | -45.71013 | 2024-10-06 05:10:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 28.6 |
| b104c471-65ae-3168-bf04-2956483bdb99 | -6.34767 | -45.71464 | 2024-10-06 05:10:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 13.0 |
| 2c953d50-b437-3410-9d8b-306666204be7 | -6.34644 | -45.70574 | 2024-10-06 05:10:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 28.7 |
| f9359948-b44e-3cf2-b5ec-02e96752aad0 | -6.34587 | -45.70996 | 2024-10-06 05:10:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 18.4 |
| 55de0834-fb09-3f03-aaf4-6dd0aa0397ca | -6.34528 | -45.71445 | 2024-10-06 05:10:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 18.4 |
| 2334a8e8-e39e-3849-9c82-ffc607193639 | -6.34152 | -45.71291 | 2024-10-06 05:10:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 13.0 |
| 34b91b8a-04a6-38da-88be-fbedfd4cb783 | -6.33969 | -45.70839 | 2024-10-06 05:10:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| cb5718bd-f823-34ca-83e7-294d4d3e209c | -7.7594 | -46.14094 | 2024-10-06 05:10:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 14a1ffb4-3a2a-3aec-8105-a3ec272b709e | -7.75815 | -46.13875 | 2024-10-06 05:10:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 9be0995c-3d46-3de9-bc25-4a0f0de56e38 | -7.75749 | -46.14402 | 2024-10-06 05:10:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 009114bd-9b98-3d63-b74b-e526171a6c1c | -7.07729 | -46.59681 | 2024-10-06 05:10:00 | NOAA-21 | FEIRA NOVA DO MARANHÃO | MARANHÃO | Brasil | 2104073 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c99310b4-d650-3819-b925-6f0b40858930 | -6.75651 | -45.64824 | 2024-10-06 05:10:00 | NOAA-21 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 07b533c9-64f3-323c-a984-8d7a4a3784c7 | -7.07131 | -46.5959 | 2024-10-06 05:10:00 | NOAA-21 | FEIRA NOVA DO MARANHÃO | MARANHÃO | Brasil | 2104073 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ede4d545-5482-357c-8e5f-156044a4450a | -1.76572 | -47.19268 | 2024-10-06 05:10:00 | NOAA-21 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 8.3 |
| 278eb63b-86fa-3177-b97a-000ce7f0735f | -1.76521 | -47.19602 | 2024-10-06 05:10:00 | NOAA-21 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| bba7bbd8-4454-35de-b064-697f796aee18 | -4.82445 | -46.79754 | 2024-10-06 05:10:00 | NOAA-21 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 2.6 |


[Clique aqui para ver as próximas entradas](README96.md)
