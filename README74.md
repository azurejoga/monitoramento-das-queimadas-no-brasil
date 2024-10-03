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

## Dados Diários - Página 74

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| cf6b2118-639f-3c6d-b0e2-57ac7406ad2a | -6.6716 | -45.3308 | 2024-10-03 03:45:44 | GOES-16 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 92.1 |
| 5d8f3b81-4b36-35e9-be86-2ed9c0cfb86f | -8.8506 | -45.5086 | 2024-10-03 03:45:56 | GOES-16 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 55.4 |
| 7efee112-977a-3964-b692-d4b521d10d17 | -8.9791 | -67.4099 | 2024-10-03 03:45:58 | GOES-16 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 49.2 |
| 49feb970-31d5-3bda-aa69-79d1cd67f942 | -9.0515 | -67.871 | 2024-10-03 03:45:58 | GOES-16 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 55.2 |
| eaaab95a-e56e-3999-aefb-b5c7478f8d71 | -9.1566 | -61.6758 | 2024-10-03 03:45:58 | GOES-16 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 59.4 |
| 0cba208f-4b20-3b47-b3ec-f4d8eb30b650 | -10.9381 | -46.5942 | 2024-10-03 03:46:07 | GOES-16 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 39.1 |
| 2567981a-91e0-3174-8b14-21b31fc56002 | -10.8942 | -63.8971 | 2024-10-03 03:46:08 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 67.7 |
| 6e80dbbf-f3ff-3c83-ac6c-f5248b05c6ff | -11.2565 | -60.6019 | 2024-10-03 03:46:10 | GOES-16 | ESPIGÃO D'OESTE | RONDÔNIA | Brasil | 1100098 | 11 | 33 | nan | nan | nan | Amazônia | 54.6 |
| 1f07adc1-de5c-31ad-b5d0-da6a1302d975 | -11.2566 | -60.5825 | 2024-10-03 03:46:10 | GOES-16 | ESPIGÃO D'OESTE | RONDÔNIA | Brasil | 1100098 | 11 | 33 | nan | nan | nan | Amazônia | 51.6 |
| 717f1395-d07b-3dc0-b2d6-dc49208cfbd2 | -11.6931 | -64.9974 | 2024-10-03 03:46:13 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 91.4 |
| 5bebd670-a266-331b-aff2-59c8d13c3183 | -11.6932 | -64.9785 | 2024-10-03 03:46:13 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 64.2 |
| 36dcfe42-bfea-3911-bc64-32ca15b2e392 | -12.4038 | -63.0009 | 2024-10-03 03:46:17 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 187.2 |
| 06d839e9-bb9e-37dc-bdac-277fdd976e58 | -12.404 | -62.9817 | 2024-10-03 03:46:17 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 101.2 |
| 53b2dcb3-cd60-30f2-b16b-c1a1e269c060 | -12.4227 | -62.9999 | 2024-10-03 03:46:17 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 115.6 |
| d8bab125-8d0e-32b0-b14f-381def28068d | -12.6484 | -63.1214 | 2024-10-03 03:46:18 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 77.8 |
| ee0c14ff-2ece-3dd1-ac96-8c6148b9606c | -12.8802 | -62.5503 | 2024-10-03 03:46:19 | GOES-16 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 78.8 |
| 28d2fd6e-36d5-3ab2-b9e5-6479f00632b8 | -12.881 | -62.4538 | 2024-10-03 03:46:19 | GOES-16 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 67.5 |
| 3a39aaac-e761-3859-94a0-d059e3477fb3 | -12.8996 | -62.4913 | 2024-10-03 03:46:19 | GOES-16 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 103.8 |
| c23c1095-c27f-3fbc-93a4-f1c20509ee1d | -12.8998 | -62.472 | 2024-10-03 03:46:19 | GOES-16 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 117.8 |
| b6daea34-63b4-3e02-9783-02b928da205e | -12.8999 | -62.4527 | 2024-10-03 03:46:19 | GOES-16 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 67.3 |
| 1c5d44d1-b404-3109-9dab-de5d3e43ae08 | -13.0402 | -51.1432 | 2024-10-03 03:46:19 | GOES-16 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 96.7 |
| 0b678ebb-54ad-3a7b-92b3-38a6e03ed044 | -13.0594 | -51.1409 | 2024-10-03 03:46:20 | GOES-16 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 61.9 |
| 2213c61c-5755-3fe1-a1c3-d4e307ab2bc4 | -13.5562 | -51.2489 | 2024-10-03 03:46:22 | GOES-16 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 118.1 |
| 08f6c8df-57eb-3bce-a6de-b6c609788d85 | -16.5585 | -58.2204 | 2024-10-03 03:46:39 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 75.0 |
| 7224fa4b-1c7e-3ae3-84d8-07196d170adf | -16.5588 | -58.2001 | 2024-10-03 03:46:39 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 100.5 |
| 96d0fbda-9903-3bbd-ba99-e97aaa70a5cb | -16.578 | -58.2183 | 2024-10-03 03:46:39 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 55.2 |
| b962111e-d546-344f-99a3-c186cd7d412b | -16.5783 | -58.198 | 2024-10-03 03:46:39 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 69.9 |
| 7aae8acb-1d30-36cb-9553-e6b7cc7bb592 | -16.6688 | -57.374 | 2024-10-03 03:46:40 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 97.1 |
| eec71284-2bcf-3b1d-9e53-ef284985ff03 | -16.6492 | -57.3763 | 2024-10-03 03:46:40 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 65.5 |
| 088db971-7daa-3705-a7a8-147566b31227 | -16.6685 | -57.3945 | 2024-10-03 03:46:40 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 69.2 |
| 5a2346b5-49b9-3261-9ea6-7bb92166b780 | -16.779 | -57.8306 | 2024-10-03 03:46:40 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 70.6 |
| e731d197-4cc3-3a0d-bcdf-ef8aae9f4785 | -16.8983 | -57.6949 | 2024-10-03 03:46:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 71.9 |
| 118eba39-1af0-3c80-9730-f1563f0a018b | -16.9176 | -57.7131 | 2024-10-03 03:46:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 61.9 |
| b8c58944-876e-371c-8f27-65e3a8bbf2f0 | -16.9179 | -57.6926 | 2024-10-03 03:46:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 63.0 |
| abd619d3-c6e2-3269-bf38-72d2af78369e | -19.0344 | -43.1944 | 2024-10-03 03:46:51 | GOES-16 | CARMÉSIA | MINAS GERAIS | Brasil | 3113800 | 31 | 33 | nan | nan | nan | Mata Atlântica | 76.6 |
| 0af75db5-ed60-3264-ab8a-4a19d80281d0 | -19.9904 | -43.1359 | 2024-10-03 03:46:56 | GOES-16 | RIO PIRACICABA | MINAS GERAIS | Brasil | 3155702 | 31 | 33 | nan | nan | nan | Mata Atlântica | 62.7 |
| fe5e45f1-ee84-35b7-8a22-0a4fd3f40f5d | -3.4229 | -42.2612 | 2024-10-03 03:55:25 | GOES-16 | MAGALHÃES DE ALMEIDA | MARANHÃO | Brasil | 2106300 | 21 | 33 | nan | nan | nan | Cerrado | 60.8 |
| 79db37cd-040a-3086-8742-6c8e2b9665d1 | -3.4227 | -42.2849 | 2024-10-03 03:55:25 | GOES-16 | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Cerrado | 101.6 |
| 74ed4a4d-233a-3fc3-8d19-3a9eabff0873 | -3.4042 | -42.2621 | 2024-10-03 03:55:25 | GOES-16 | MAGALHÃES DE ALMEIDA | MARANHÃO | Brasil | 2106300 | 21 | 33 | nan | nan | nan | Cerrado | 287.5 |
| 27a98e7a-b7dc-3f7f-8a4f-f2a6456b2f5a | -3.404 | -42.2858 | 2024-10-03 03:55:25 | GOES-16 | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Cerrado | 534.2 |
| b2a8a97c-c0f5-366e-b086-e6cf88278685 | -3.4039 | -42.3094 | 2024-10-03 03:55:25 | GOES-16 | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Caatinga | 69.2 |
| 10b35205-cf1f-3fbd-9af2-d23751ac0138 | -3.3854 | -42.2866 | 2024-10-03 03:55:25 | GOES-16 | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Cerrado | 55.7 |
| 599849ee-fb7a-3bdd-81f0-e7f9280ba29a | -4.1134 | -48.4886 | 2024-10-03 03:55:29 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 48.8 |
| e2fb8ae5-3384-3b2e-aa76-a613732e6168 | -4.095 | -48.4679 | 2024-10-03 03:55:29 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 53.9 |
| 13048ebe-d6ba-3e88-84e3-57ea82694313 | -4.0949 | -48.4894 | 2024-10-03 03:55:29 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 95.4 |
| da4b8369-4f4a-3737-91de-36347a19d066 | -4.5375 | -43.304 | 2024-10-03 03:55:31 | GOES-16 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 97.0 |
| a1353e49-8821-3518-b1ba-2a35c41d47fa | -4.5373 | -43.3273 | 2024-10-03 03:55:31 | GOES-16 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 75.2 |
| 0b47f329-b65a-3d20-8bc8-72ee3afc788d | -4.4845 | -42.8631 | 2024-10-03 03:55:31 | GOES-16 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 34.1 |
| 8778b814-8de7-368e-8b19-8e104eb2c071 | -4.4844 | -42.8866 | 2024-10-03 03:55:31 | GOES-16 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 35.0 |
| ae37b9dc-0b99-3fac-95ef-20ab37ae7efe | -9.0515 | -67.871 | 2024-10-03 03:55:58 | GOES-16 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 49.0 |
| 31454d30-05b2-3ad4-884c-07fea5333f53 | -8.9976 | -67.4094 | 2024-10-03 03:55:58 | GOES-16 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 41.9 |
| b70531ad-52c7-3520-b8c2-8e6711739b9e | -8.9791 | -67.4099 | 2024-10-03 03:55:58 | GOES-16 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 41.5 |
| 2c50fce5-1cfd-3453-94ab-9c99064b5b9a | -10.6505 | -53.6994 | 2024-10-03 03:56:06 | GOES-16 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 53.7 |
| 599239fb-9bc5-3b7c-bc22-e053b301e73c | -10.6319 | -53.6805 | 2024-10-03 03:56:06 | GOES-16 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 52.3 |
| 706e1b96-8475-3488-9019-4002c628b9cd | -10.6317 | -53.7011 | 2024-10-03 03:56:06 | GOES-16 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 71.5 |
| a35cf456-6f2f-31c7-b9e2-f9b77348cdf7 | -10.9384 | -46.5717 | 2024-10-03 03:56:07 | GOES-16 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 65.2 |
| 17c21464-6af2-348a-92ac-6541c425ab95 | -10.9381 | -46.5942 | 2024-10-03 03:56:07 | GOES-16 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 83.5 |
| d1e61ad5-f442-3710-a19f-fdcdfd5022cf | -10.8942 | -63.8971 | 2024-10-03 03:56:08 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 57.8 |
| e26546a9-eda5-3e9e-934b-04649cca80ee | -11.6822 | -47.7045 | 2024-10-03 03:56:12 | GOES-16 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 94.6 |
| bc1bab20-9f4d-3984-b49e-5ad7fe6c8edc | -11.6932 | -64.9785 | 2024-10-03 03:56:13 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 56.2 |
| e9a19dee-1668-391f-b8a0-ab2948c9920c | -11.6931 | -64.9974 | 2024-10-03 03:56:13 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 74.7 |
| 99c8fcbf-283b-3975-bcc6-8669f4796128 | -11.6743 | -64.9983 | 2024-10-03 03:56:13 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 61.5 |
| 3d4e2872-03b6-3bb5-98e5-034ac1120945 | -12.4227 | -62.9999 | 2024-10-03 03:56:17 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 90.0 |
| b027ced7-b413-3c18-b62c-611a5ea7b172 | -12.404 | -62.9817 | 2024-10-03 03:56:17 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 99.6 |
| 6c11d97d-2678-3327-917e-219083f5486e | -12.4038 | -63.0009 | 2024-10-03 03:56:17 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 167.9 |
| 777ccd72-50ec-365d-b71f-00b82c2b018a | -12.6484 | -63.1214 | 2024-10-03 03:56:18 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 83.6 |
| cd22b694-2608-3003-8ccc-d90326a0692c | -13.0402 | -51.1432 | 2024-10-03 03:56:19 | GOES-16 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 77.9 |
| 0d79e9c7-a07a-36de-a910-a8e162df23ac | -12.8998 | -62.472 | 2024-10-03 03:56:19 | GOES-16 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 106.0 |
| 57c85bea-24c6-30b9-a9fc-db7cd28daeac | -12.8996 | -62.4913 | 2024-10-03 03:56:19 | GOES-16 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 88.5 |
| 48c7c9b3-f731-386e-abf7-5b58ac9a06df | -12.8991 | -62.5491 | 2024-10-03 03:56:19 | GOES-16 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 77.0 |
| d6c3391e-9d23-3b7b-92c7-17deabb238a6 | -12.881 | -62.4538 | 2024-10-03 03:56:19 | GOES-16 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 72.7 |
| f4adbb97-49ed-313e-b4ec-5829d7a4f9d7 | -12.8808 | -62.4731 | 2024-10-03 03:56:19 | GOES-16 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 73.6 |
| 60fd074e-fb2e-39f5-be4d-2e7b6197109a | -12.8802 | -62.5503 | 2024-10-03 03:56:19 | GOES-16 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 78.9 |
| 6f51e1fe-d85a-39ee-b302-96489790369c | -13.5754 | -51.2464 | 2024-10-03 03:56:22 | GOES-16 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 64.5 |
| 3cca6054-01f4-3dc8-811d-42d0e89411de | -13.5562 | -51.2489 | 2024-10-03 03:56:22 | GOES-16 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 120.0 |
| 40f42ad3-b3cb-3604-9283-4a02546051ef | -13.5195 | -51.1467 | 2024-10-03 03:56:22 | GOES-16 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 88.7 |
| fadb5c20-3eb3-3964-9115-80cdb1895bac | -16.7477 | -57.3241 | 2024-10-03 03:56:40 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 87.8 |
| a8b908ff-3068-3f28-aa50-caab5705ba93 | -16.7474 | -57.3446 | 2024-10-03 03:56:40 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 133.1 |
| fc62346b-b87a-308e-9181-783734b8feaf | -16.6884 | -57.3718 | 2024-10-03 03:56:40 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 63.6 |
| 7d6a7ffd-01f2-3aaa-a8fe-197bdfa456ae | -16.6688 | -57.374 | 2024-10-03 03:56:40 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 122.0 |
| 149d34b4-8b2d-3783-8f8d-2127c25e77be | -16.6685 | -57.3945 | 2024-10-03 03:56:40 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 74.4 |
| 66d40ecf-9baf-3e90-bbed-1af58009e030 | -16.6492 | -57.3763 | 2024-10-03 03:56:40 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 71.4 |
| b5886b57-bbc2-370e-a0e4-93b3335d31f3 | -16.779 | -57.8306 | 2024-10-03 03:56:40 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 59.8 |
| 58261668-56e4-34f7-8b58-ddc7f8473085 | -16.8983 | -57.6949 | 2024-10-03 03:56:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 56.3 |
| cafac04b-50bb-34cc-8679-c50f4961c75b | -16.9179 | -57.6926 | 2024-10-03 03:56:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 56.6 |
| 78b3c707-d22f-38fb-b80b-93c7e1aadbdd | -16.9176 | -57.7131 | 2024-10-03 03:56:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 57.2 |
| 02f804e7-bf75-3d0c-b230-331f6f32a791 | -19.0344 | -43.1944 | 2024-10-03 03:56:51 | GOES-16 | CARMÉSIA | MINAS GERAIS | Brasil | 3113800 | 31 | 33 | nan | nan | nan | Mata Atlântica | 61.3 |
| 55f42843-34f6-3b4e-bd11-3458673dac4e | -21.346 | -55.6626 | 2024-10-03 03:57:04 | GOES-16 | NIOAQUE | MATO GROSSO DO SUL | Brasil | 5005806 | 50 | 33 | nan | nan | nan | Cerrado | 71.5 |
| 9988e01b-b3b3-3f41-9718-16eedfd3dfdb | -3.43 | -42.27 | 2024-10-03 04:05:07 | MSG-03 | MAGALHÃES DE ALMEIDA | MARANHÃO | Brasil | 2106300 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| d3f14257-8202-39fa-9b81-911c40ebfc21 | -3.4 | -42.27 | 2024-10-03 04:05:07 | MSG-03 | MAGALHÃES DE ALMEIDA | MARANHÃO | Brasil | 2106300 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 520a1ca1-32e2-39d7-8230-497753226755 | -3.4039 | -42.3094 | 2024-10-03 04:05:25 | GOES-16 | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Caatinga | 56.7 |
| c46587cc-90cc-361f-b635-bb2b7d860e66 | -3.404 | -42.2858 | 2024-10-03 04:05:25 | GOES-16 | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Cerrado | 595.8 |
| b627cb03-fc34-377a-9113-eb81a1f774fb | -3.4227 | -42.2849 | 2024-10-03 04:05:25 | GOES-16 | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Cerrado | 115.2 |
| 174970be-8331-3324-895e-560cef521d0f | -3.4229 | -42.2612 | 2024-10-03 04:05:25 | GOES-16 | MAGALHÃES DE ALMEIDA | MARANHÃO | Brasil | 2106300 | 21 | 33 | nan | nan | nan | Cerrado | 69.9 |
| 8e295344-a355-35fd-94bc-ac688fb2149b | -4.0949 | -48.4894 | 2024-10-03 04:05:29 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 87.0 |
| 91636033-9d87-3b66-8da9-1366f37adf5a | -4.095 | -48.4679 | 2024-10-03 04:05:29 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 54.9 |
| 422d9792-64f4-3a84-a908-6e04f08a4f5b | -4.1134 | -48.4886 | 2024-10-03 04:05:29 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 47.5 |
| 7c93d225-729e-3fe2-af2d-0c3925575f77 | -4.4844 | -42.8866 | 2024-10-03 04:05:31 | GOES-16 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 44.7 |
| c22a1a69-519e-394a-acae-053be12ada20 | -4.5373 | -43.3273 | 2024-10-03 04:05:31 | GOES-16 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 70.6 |
| 013d38eb-e69e-3310-bf06-8a82f7d053fa | -4.5375 | -43.304 | 2024-10-03 04:05:31 | GOES-16 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 102.4 |


[Clique aqui para ver as próximas entradas](README75.md)
