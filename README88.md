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

## Dados Diários - Página 88

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 7e8da0a3-22b7-3bd9-bf95-6a93f15e7c6b | -9.6519 | -48.30058 | 2025-08-28 06:16:00 | AQUA_M-M | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 13.8 |
| e5b36eb3-6dd5-3789-ac9f-57d93e72d6d5 | -11.22613 | -55.05737 | 2025-08-28 06:16:00 | AQUA_M-M | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 14.4 |
| 09f7dfd8-e477-3851-a7e0-3b7304682af4 | -12.80582 | -48.13895 | 2025-08-28 06:16:00 | AQUA_M-M | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 22.6 |
| c63cfca7-fcd0-397d-9a4c-b64ef14fe38a | -12.95837 | -44.56092 | 2025-08-28 06:16:00 | AQUA_M-M | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 62.6 |
| da99f463-2ba9-3234-9df5-7402c39c070b | -9.66085 | -48.31658 | 2025-08-28 06:16:00 | AQUA_M-M | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 20.6 |
| c4281e4e-b877-380a-856a-256e0b58041d | -10.33082 | -46.77732 | 2025-08-28 06:16:00 | AQUA_M-M | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 39.2 |
| 618ad1bf-88b7-377c-aecf-8e0b5948bec9 | -12.81606 | -48.12829 | 2025-08-28 06:16:00 | AQUA_M-M | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 14.3 |
| 396b1322-0af7-3491-9420-210723e4d5d8 | -13.42724 | -46.97184 | 2025-08-28 06:16:00 | AQUA_M-M | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 36.6 |
| cb5dc169-3b38-3dea-ac4d-f97a50930dda | -9.05356 | -54.94016 | 2025-08-28 06:16:00 | AQUA_M-M | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 10.1 |
| 1bea5f46-0980-3c3d-ab43-7e5bba75e911 | -13.42497 | -46.97732 | 2025-08-28 06:16:00 | AQUA_M-M | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 24.3 |
| 6c5f0898-8e0b-378a-8e37-f0f4bf5d18f3 | -10.79709 | -60.75603 | 2025-08-28 06:16:00 | AQUA_M-M | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 46.8 |
| 209324e0-7460-3834-92c4-ae004b949b7c | -13.73131 | -51.90965 | 2025-08-28 06:16:00 | AQUA_M-M | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 9.0 |
| 31b91156-96ab-3f25-81a6-8ce2de517d89 | -12.85528 | -48.10095 | 2025-08-28 06:16:00 | AQUA_M-M | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 22.3 |
| 0b9b05ef-8107-318c-a214-9dddacdf5071 | -12.96031 | -44.58522 | 2025-08-28 06:16:00 | AQUA_M-M | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 48.6 |
| fc68a148-aa62-30ac-af28-12296c98cbec | -13.42722 | -46.95847 | 2025-08-28 06:16:00 | AQUA_M-M | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 38.0 |
| 5b7a964e-4bac-32ce-a9de-193f678e9f43 | -13.97513 | -46.34578 | 2025-08-28 06:16:00 | AQUA_M-M | GUARANI DE GOIÁS | GOIÁS | Brasil | 5209408 | 52 | 33 | nan | nan | nan | Cerrado | 23.0 |
| 77d790db-bd62-3dd9-bc79-98533cbd117a | -10.5237 | -46.69639 | 2025-08-28 06:16:00 | AQUA_M-M | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 16.3 |
| c6d55f0f-d509-3890-9f6c-d37902217b4a | -13.98485 | -46.32884 | 2025-08-28 06:16:00 | AQUA_M-M | GUARANI DE GOIÁS | GOIÁS | Brasil | 5209408 | 52 | 33 | nan | nan | nan | Cerrado | 31.1 |
| 255c1cc6-b441-33de-8c53-367e8d6f4b84 | -10.8003 | -60.76439 | 2025-08-28 06:16:00 | AQUA_M-M | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 40.6 |
| aa7ef3b2-e483-3d65-97c1-262a3785fe72 | -12.81403 | -48.1446 | 2025-08-28 06:16:00 | AQUA_M-M | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 13.1 |
| db9debe5-d01c-39a2-9246-0abd11961701 | -7.73196 | -50.28022 | 2025-08-28 06:16:00 | AQUA_M-M | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 7.0 |
| c4a3ecbc-d5dd-370c-b8e0-6f1d32ef9c64 | -9.45417 | -51.94512 | 2025-08-28 06:16:00 | AQUA_M-M | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 29ae0e89-ff7f-3c4c-b7fb-a545dae1a066 | -11.56793 | -46.39518 | 2025-08-28 06:16:00 | AQUA_M-M | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 16.1 |
| a2035a2b-681b-3d7a-9ba1-6315774f91cc | -11.22765 | -55.04769 | 2025-08-28 06:16:00 | AQUA_M-M | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 11.8 |
| ccc006a8-28ac-35ec-9c4b-686c534691a2 | -11.21849 | -55.04621 | 2025-08-28 06:16:00 | AQUA_M-M | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 0272a6c5-bf54-3ab0-abbf-35a6c57b37bc | -13.08801 | -46.32516 | 2025-08-28 06:16:00 | AQUA_M-M | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 18.2 |
| 40b51f16-8beb-3e89-ae1d-fc7f83f87a1c | -10.33007 | -46.77048 | 2025-08-28 06:16:00 | AQUA_M-M | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 56.4 |
| a6074215-ebaf-300f-925e-0c6b64d2d10c | -14.28952 | -53.02921 | 2025-08-28 06:16:00 | AQUA_M-M | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 8.9 |
| 207f5251-37cf-31ce-bbdc-54b542416b0e | -12.67381 | -48.18026 | 2025-08-28 06:16:00 | AQUA_M-M | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 17.1 |
| 185b790e-ce01-3fa3-9335-224f621b510c | -10.32753 | -46.78959 | 2025-08-28 06:16:00 | AQUA_M-M | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 22.0 |
| dac4a6a5-cc80-38ae-99e4-0ecf7ed5a9c5 | -8.2773 | -45.16943 | 2025-08-28 06:16:00 | AQUA_M-M | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 18.8 |
| 62bfa2d0-13f5-3b81-995f-5e4cbefa740e | -14.32774 | -53.33974 | 2025-08-28 06:18:00 | AQUA_M-M | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 20.9 |
| 08513981-c469-3f9e-868b-2e73ae50d338 | -14.32908 | -53.33065 | 2025-08-28 06:18:00 | AQUA_M-M | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 17.9 |
| b5739834-198e-30f8-bf11-a3a7d5acaa8f | -15.66897 | -52.73959 | 2025-08-28 06:18:00 | AQUA_M-M | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 25e826d3-3e9e-3fba-b01b-01fdf415944d | -14.35422 | -53.34382 | 2025-08-28 06:18:00 | AQUA_M-M | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 9ce87b5c-79ff-3bab-bcd1-72f3c2dc881f | -14.59398 | -54.50727 | 2025-08-28 06:18:00 | AQUA_M-M | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | 5.4 |
| cc83c950-fc34-3d03-a938-dc94804869af | -16.15274 | -49.64194 | 2025-08-28 06:18:00 | AQUA_M-M | ITAUÇU | GOIÁS | Brasil | 5211404 | 52 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 83d39e95-9aec-3e2b-8c83-7821f9fa4986 | -14.33657 | -53.3411 | 2025-08-28 06:18:00 | AQUA_M-M | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 91.0 |
| 8ff8418b-2e9d-3e45-b05b-892d37f10be4 | -14.33791 | -53.33201 | 2025-08-28 06:18:00 | AQUA_M-M | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 28.5 |
| dd8af9e0-316e-3624-a0a7-5c97ed320df1 | -14.77814 | -59.71769 | 2025-08-28 06:18:00 | AQUA_M-M | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 12.8 |
| e7fced95-4264-308c-9e67-e14bc08e2120 | -14.34405 | -53.35154 | 2025-08-28 06:18:00 | AQUA_M-M | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 8.9 |
| c8929cd7-ee7a-3e28-b067-47e85f4bf300 | -15.6301 | -52.75327 | 2025-08-28 06:18:00 | AQUA_M-M | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 5.8 |
| d9eeafa3-78b8-35ad-9551-3eb75c769935 | -15.17425 | -52.33205 | 2025-08-28 06:18:00 | AQUA_M-M | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 8ba1ae1a-708b-3e11-a6c9-15dacc744ae4 | -14.3454 | -53.34246 | 2025-08-28 06:18:00 | AQUA_M-M | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 116.0 |
| 21175482-1428-370d-ac7e-3d87cb208b22 | -14.3485 | -53.3504 | 2025-08-28 06:20:00 | GOES-19 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 94.4 |
| 22bf2ab8-1800-3318-ada3-c9c85f734d1b | -8.2893 | -45.1586 | 2025-08-28 06:20:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 123.7 |
| f15cbf3c-149a-38e3-8934-001cb699be22 | -14.3292 | -53.3528 | 2025-08-28 06:20:00 | GOES-19 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 95.0 |
| bca35442-ae8e-31c3-aef0-d3f3d7508783 | -9.1339 | -65.788 | 2025-08-28 06:20:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 175.2 |
| 74d8aa05-364e-39a6-b992-d2ff3703f91b | -9.134 | -65.7694 | 2025-08-28 06:20:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 90.4 |
| 82792160-1a90-3809-a811-4f04a6abd508 | -9.1155 | -65.7699 | 2025-08-28 06:20:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 105.8 |
| 1b479c48-52e7-3fe6-9caf-8670c4d3937c | -9.1154 | -65.7886 | 2025-08-28 06:20:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 216.8 |
| 99e9352d-9ccd-31cc-adb2-5c3834317874 | -14.3296 | -53.3318 | 2025-08-28 06:20:00 | GOES-19 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 118.2 |
| 414b12fb-699a-39a8-9f9c-5b011840c777 | -8.3085 | -45.1338 | 2025-08-28 06:20:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 74.7 |
| 1a5eafdb-2126-3fd6-904d-6fb9e738a28a | -14.3489 | -53.3294 | 2025-08-28 06:20:00 | GOES-19 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 83.9 |
| fcf96ebe-cf7a-3b55-98ca-be9c03cf3de7 | -6.8772 | -43.6152 | 2025-08-28 06:20:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 121.3 |
| 582725d2-22d7-3da3-8b10-7c2e6919f2d1 | -8.3079 | -45.1794 | 2025-08-28 06:20:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 47.6 |
| 22e316d0-8da1-3c65-a1a0-2b74bddf03c5 | -8.289 | -45.1814 | 2025-08-28 06:20:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 46.0 |
| 6c8a90ca-fbdc-3a7b-bd3b-9cd921938f87 | -6.896 | -43.6135 | 2025-08-28 06:20:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 65.5 |
| 1eb60f0b-4baf-31b8-8196-217aea90c5d9 | -9.1338 | -65.8067 | 2025-08-28 06:20:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 36.4 |
| 301ed52c-fb8b-31c7-954b-7532a7b90e60 | -9.1153 | -65.8073 | 2025-08-28 06:20:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 42.6 |
| 340e823e-69a5-3218-9b84-fdd9700ba37b | -10.4738 | -57.9366 | 2025-08-28 06:20:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 65.8 |
| dbceacf3-6d0c-31cc-baa0-62604fbefa2c | -8.3082 | -45.1566 | 2025-08-28 06:20:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 174.8 |
| 73d76804-bb3c-30c2-986d-c2da5dc0af43 | -6.8772 | -43.6152 | 2025-08-28 06:30:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 113.0 |
| 4046f95d-eb38-3e62-8d6c-e07bcd771f94 | -8.3082 | -45.1566 | 2025-08-28 06:30:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 233.7 |
| afbe8004-6cec-3c90-8d6b-0a99a0fd1308 | -8.2896 | -45.1357 | 2025-08-28 06:30:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 56.0 |
| d298dda7-f731-3c0e-991f-dd841af440ba | -6.896 | -43.6135 | 2025-08-28 06:30:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 62.3 |
| 0c47dedb-00b5-3488-adf2-3e517d8d1645 | -8.289 | -45.1814 | 2025-08-28 06:30:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 48.3 |
| 0e6060dc-965e-3886-89d5-d65336f5a2ca | -9.0969 | -65.7892 | 2025-08-28 06:30:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 44.3 |
| ec589ae8-56fc-3c5b-bdf0-63bbf258efa3 | -10.4738 | -57.9366 | 2025-08-28 06:30:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 65.4 |
| c4506c7b-87e8-3c60-8a0d-19d76960dffa | -8.2893 | -45.1586 | 2025-08-28 06:30:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 141.0 |
| b2158c36-076e-329e-bc4d-28d28a6580bd | -9.1154 | -65.7886 | 2025-08-28 06:30:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 222.0 |
| 2d9eb7f4-d576-37c4-9c28-544c56bf1147 | -8.3079 | -45.1794 | 2025-08-28 06:30:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 62.9 |
| 6cf3eecd-f568-38fd-8cfc-ebce5f4cf972 | -8.3085 | -45.1338 | 2025-08-28 06:30:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 87.2 |
| 9575e7de-757e-3cf9-9d15-1cbe4029e1fb | -9.1155 | -65.7699 | 2025-08-28 06:30:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 129.3 |
| decad48b-121e-315e-862d-80df378f4273 | -9.1339 | -65.788 | 2025-08-28 06:30:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 155.5 |
| 9f2d9111-d5e7-354a-8f3f-fb7da98b5f17 | -9.134 | -65.7694 | 2025-08-28 06:30:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 97.4 |
| 37d537af-4faa-3267-a129-304e6da8802a | -6.896 | -43.6135 | 2025-08-28 06:40:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 60.1 |
| 30165d25-5556-380d-acad-a5539a8fdf48 | -6.8772 | -43.6152 | 2025-08-28 06:40:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 100.2 |
| 6931897d-bee7-3855-b812-daee480cdd36 | -9.134 | -65.7694 | 2025-08-28 06:40:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 81.5 |
| fda482f7-7e41-370d-b16d-e476be4ba227 | -6.178 | -44.0688 | 2025-08-28 06:40:00 | GOES-19 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 58.5 |
| ac28c491-e8a3-34d8-b7ee-4418a7027a6b | -8.3082 | -45.1566 | 2025-08-28 06:40:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 109.8 |
| be2b43be-8712-36bb-a0e7-033ba2b8f036 | -9.1154 | -65.7886 | 2025-08-28 06:40:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 245.9 |
| af78c360-daa7-38e7-97ad-bf1e0dc05cb8 | -9.1155 | -65.7699 | 2025-08-28 06:40:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 147.3 |
| 4139c252-1250-3680-a671-afd602dea55a | -9.1339 | -65.788 | 2025-08-28 06:40:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 125.4 |
| 9ee45fa3-c70c-3460-8e1b-eb594bb84528 | -10.4738 | -57.9366 | 2025-08-28 06:40:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 58.2 |
| 60764099-f7b7-3424-aa8e-310c8ca5ea55 | -8.2893 | -45.1586 | 2025-08-28 06:40:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 68.9 |
| d2357cd3-e636-3b86-8e1e-36a5774e341f | -10.56338 | -69.81165 | 2025-08-28 06:40:00 | NOAA-21 | ASSIS BRASIL | ACRE | Brasil | 1200054 | 12 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 12124178-7729-35e6-8d0e-f740351f0ca7 | -8.58461 | -70.11874 | 2025-08-28 06:40:00 | NOAA-21 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 857c5a06-0220-3f8d-9629-fb44b14f2388 | -8.10043 | -71.24175 | 2025-08-28 06:40:00 | NOAA-21 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d194b868-4974-3fa2-9f9e-7571b76908d8 | -8.44556 | -70.1454 | 2025-08-28 06:40:00 | NOAA-21 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 75a17941-af22-3f3a-93be-77688ca11456 | -8.74121 | -71.00029 | 2025-08-28 06:40:00 | NOAA-21 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 5.3 |
| be3eaf07-5655-33ed-92c3-9ece130f9776 | -8.51339 | -69.79738 | 2025-08-28 06:40:00 | NOAA-21 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.1 |
| cd5e3f9e-7dab-3d12-9775-9a27ee1b1011 | -8.1048 | -71.24905 | 2025-08-28 06:40:00 | NOAA-21 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 354766aa-4b95-3c12-8d6c-dcb436ecd7e6 | -10.56391 | -69.80736 | 2025-08-28 06:40:00 | NOAA-21 | ASSIS BRASIL | ACRE | Brasil | 1200054 | 12 | 33 | nan | nan | nan | Amazônia | 2.8 |
| decef3b4-57a8-36bd-bbec-21772603a9d2 | -8.73813 | -71.00095 | 2025-08-28 06:40:00 | NOAA-21 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 1decad18-3efe-358a-86e2-944acde53685 | -8.09916 | -71.2514 | 2025-08-28 06:40:00 | NOAA-21 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 1197c035-5cef-37c1-92bf-7e771a001487 | -9.11901 | -67.70834 | 2025-08-28 06:40:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 8aea10a1-c6a2-3016-85e2-109eb5191a7d | -9.11237 | -67.70739 | 2025-08-28 06:40:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| da046729-63ef-3d2a-a99e-d34a594cfb3a | -8.7173 | -68.68761 | 2025-08-28 06:40:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 092665b5-d4bd-3d4a-993c-756b889f4cbe | -8.51919 | -69.79822 | 2025-08-28 06:40:00 | NOAA-21 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.3 |


[Clique aqui para ver as próximas entradas](README89.md)
