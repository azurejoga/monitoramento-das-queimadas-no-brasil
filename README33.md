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

## Dados Diários - Página 33

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 02c02601-a6b3-3715-8cc7-26e53b50d95e | -7.50674 | -46.64336 | 2025-10-15 04:06:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 23075ce2-aca0-3d6e-9f92-7f97ebeccd92 | -4.64882 | -43.12991 | 2025-10-15 04:06:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 28.7 |
| 4ed32c86-d2d1-3285-a5a6-3c93482d088f | -7.04924 | -43.96896 | 2025-10-15 04:06:00 | NOAA-20 | MARCOS PARENTE | PIAUÍ | Brasil | 2206001 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 61be1290-86be-3f9d-a91c-d598fb7e9be3 | -8.06098 | -45.91702 | 2025-10-15 04:06:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 966d3fed-9ec9-3467-a3df-245a13cb1a7a | -6.1932 | -42.59612 | 2025-10-15 04:06:00 | NOAA-20 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| f300b8b8-2c13-30c2-9c60-7aa23aa0acaf | -3.8365 | -44.54345 | 2025-10-15 04:06:00 | NOAA-20 | MATÕES DO NORTE | MARANHÃO | Brasil | 2106631 | 21 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 23ba1baf-c181-356e-89af-2b4aec3dafc4 | -6.15396 | -41.77485 | 2025-10-15 04:06:00 | NOAA-20 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 4f8dacbe-3d3a-30d7-88aa-c2e7e23c1bfe | -6.01077 | -43.12383 | 2025-10-15 04:06:00 | NOAA-20 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 1.8 |
| e7fbf6c4-a191-3755-b836-f78c815018d7 | -6.71395 | -42.14243 | 2025-10-15 04:06:00 | NOAA-20 | TANQUE DO PIAUÍ | PIAUÍ | Brasil | 2210979 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 9eff1120-a34f-3209-a654-053b1dc9e1e0 | -4.29042 | -41.7396 | 2025-10-15 04:06:00 | NOAA-20 | PIRIPIRI | PIAUÍ | Brasil | 2208403 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| bcd76068-4b5b-318f-b994-2c5997635e7f | -7.03979 | -42.74176 | 2025-10-15 04:06:00 | NOAA-20 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| a743fdab-6f45-3d1c-9dd1-60dd827f4978 | -3.97056 | -43.24654 | 2025-10-15 04:06:00 | NOAA-20 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 59b24ffd-4552-30e3-bae1-6f16debc1969 | -5.94674 | -43.75315 | 2025-10-15 04:06:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| bd854fc1-c32d-3a5e-920b-e47d2d2b1bd9 | -5.18348 | -42.90262 | 2025-10-15 04:06:00 | NOAA-20 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 85b19df9-dfb1-3573-84f3-f1e6b6b62ff8 | -7.49208 | -42.14149 | 2025-10-15 04:06:00 | NOAA-20 | SANTO INÁCIO DO PIAUÍ | PIAUÍ | Brasil | 2209500 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 236fd0ed-1383-3821-94ca-2035e592989f | -6.13631 | -41.75775 | 2025-10-15 04:06:00 | NOAA-20 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 331121f3-2f9b-3054-b170-2904f345d7ae | -6.02621 | -44.31392 | 2025-10-15 04:06:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 605dd4a6-bd5b-3bdc-8361-9d3751887a96 | -3.83348 | -44.54467 | 2025-10-15 04:06:00 | NOAA-20 | MATÕES DO NORTE | MARANHÃO | Brasil | 2106631 | 21 | 33 | nan | nan | nan | Cerrado | 6.1 |
| bbeea395-ba1c-36e6-a19c-f0f6c46f91a1 | -4.12226 | -50.72347 | 2025-10-15 04:06:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 733db8a7-67b8-32c1-8020-88dc1b617da2 | -5.87427 | -43.86353 | 2025-10-15 04:06:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 26.9 |
| 8ab72127-71d7-31a5-b6f1-8862ab94ef41 | -7.28728 | -41.95566 | 2025-10-15 04:06:00 | NOAA-20 | WALL FERRAZ | PIAUÍ | Brasil | 2211704 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 894ad4c2-efbe-359f-ae58-e6d1b422a66d | -3.72442 | -44.13941 | 2025-10-15 04:06:00 | NOAA-20 | PIRAPEMAS | MARANHÃO | Brasil | 2108801 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b05a17d7-7004-3696-bc11-82b76a6d1a8f | -5.42315 | -40.98255 | 2025-10-15 04:06:00 | NOAA-20 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 5.3 |
| 5d255e55-d207-3a71-8e37-3d8ce7c34c88 | -8.21785 | -44.07203 | 2025-10-15 04:06:00 | NOAA-20 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 3d8dac0c-25a2-318d-8e0b-72715ce511cf | -8.21943 | -44.08419 | 2025-10-15 04:06:00 | NOAA-20 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 7288d189-9b81-3750-a47b-ab1d9291ba83 | -5.20294 | -47.68307 | 2025-10-15 04:06:00 | NOAA-20 | IMPERATRIZ | MARANHÃO | Brasil | 2105302 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| e1e8236d-d981-3b91-9f7c-274ffe9478e8 | -7.68218 | -42.37654 | 2025-10-15 04:06:00 | NOAA-20 | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 9992f0cd-86cf-39e9-abc5-a9dd45a64bde | -6.14292 | -41.75885 | 2025-10-15 04:06:00 | NOAA-20 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| c9958c13-022d-3cb5-809b-5d185aa1c9e6 | -6.41926 | -42.43459 | 2025-10-15 04:06:00 | NOAA-20 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 8cd2ddf8-0a37-3b7d-bb12-4527c2e3b12c | -5.00054 | -44.49406 | 2025-10-15 04:06:00 | NOAA-20 | SÃO JOSÉ DOS BASÍLIOS | MARANHÃO | Brasil | 2111250 | 21 | 33 | nan | nan | nan | Cerrado | 0.4 |
| cc3a8bb8-a978-3713-b0f1-7b12f9c011c7 | -5.95363 | -42.86548 | 2025-10-15 04:06:00 | NOAA-20 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 3.5 |
| 86e0cbba-b822-3dcb-a108-0663ae7e642c | -6.38316 | -41.4848 | 2025-10-15 04:06:00 | NOAA-20 | LAGOA DO SÍTIO | PIAUÍ | Brasil | 2205599 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| 70ce0b6a-e9ea-3043-9891-6b291d43e093 | -8.2071 | -44.00703 | 2025-10-15 04:06:00 | NOAA-20 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 0ea34543-e2c5-31ce-a28e-377635dce173 | -6.29342 | -42.54215 | 2025-10-15 04:06:00 | NOAA-20 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| d5fb00d2-3a80-3d58-a0c5-6f5da2198148 | -8.18405 | -44.03901 | 2025-10-15 04:06:00 | NOAA-20 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d8ce9861-5fc3-3054-8cec-ceaeeb60ff43 | -6.02249 | -43.39766 | 2025-10-15 04:06:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 8a13af19-6bc8-3668-b1ff-fbfec72fbb51 | -4.3955 | -43.46353 | 2025-10-15 04:06:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 7769f551-36c5-39b6-863e-f941400c8bba | -4.88602 | -42.76906 | 2025-10-15 04:06:00 | NOAA-20 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 7700b88b-e188-3224-84ba-2a672254203a | -7.01894 | -41.95535 | 2025-10-15 04:06:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| d53e2ba7-44a1-3b69-a5ac-24d5b2d9b4d4 | -7.16892 | -42.18681 | 2025-10-15 04:06:00 | NOAA-20 | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 73895748-806e-3b7c-aff4-ebbf62fe0353 | -5.50002 | -43.78059 | 2025-10-15 04:06:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 424ad89a-310e-370c-965b-874bf6665c8f | -5.3322 | -42.56291 | 2025-10-15 04:06:00 | NOAA-20 | BENEDITINOS | PIAUÍ | Brasil | 2201606 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| daedd204-5282-3bd9-a1c4-d01d9debd70e | -4.88887 | -43.46215 | 2025-10-15 04:06:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 91dc2178-9a98-3c6c-aa57-d385669d4a07 | -3.42439 | -50.2593 | 2025-10-15 04:06:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| fc836df5-f7ff-3a78-97d8-2f50433271e9 | -5.99706 | -42.86118 | 2025-10-15 04:06:00 | NOAA-20 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| e937a90a-3bda-31a2-9307-caa9c20af137 | -4.90286 | -43.4644 | 2025-10-15 04:06:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 56.5 |
| b56dd778-f237-300e-ac4b-dcbb75ce0053 | -4.12076 | -50.71813 | 2025-10-15 04:06:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| ea24a121-ca0f-383d-b5a2-7cfc3f58e26a | -5.58062 | -44.74828 | 2025-10-15 04:06:00 | NOAA-20 | SANTA FILOMENA DO MARANHÃO | MARANHÃO | Brasil | 2109759 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b60cb903-1883-37ce-a296-8f1fc6c50810 | -6.32293 | -44.72444 | 2025-10-15 04:06:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| a8d30bb0-6354-3a29-8684-9bf01ccedf85 | -5.32602 | -42.55826 | 2025-10-15 04:06:00 | NOAA-20 | BENEDITINOS | PIAUÍ | Brasil | 2201606 | 22 | 33 | nan | nan | nan | Caatinga | 0.5 |
| cb5c5953-571f-38e3-822e-7ed3e8fb09c1 | -4.63534 | -42.51606 | 2025-10-15 04:06:00 | NOAA-20 | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 32b11d3c-633b-34ff-b14e-6c7a7fd98f91 | -5.24172 | -45.60509 | 2025-10-15 04:06:00 | NOAA-20 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| dd3c7653-79f6-398f-8532-aadecf310158 | -6.57286 | -42.96369 | 2025-10-15 04:06:00 | NOAA-20 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| c71ca92f-5a5c-348a-bdbb-2edb336c2236 | -5.49938 | -43.78455 | 2025-10-15 04:06:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| bc855b80-8e20-3433-9b9f-a86a8159bf7e | -9.34096 | -35.50766 | 2025-10-15 04:06:00 | NOAA-20 | BARRA DE SANTO ANTÔNIO | ALAGOAS | Brasil | 2700508 | 27 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 99b85b16-bf5b-3130-a4ae-7aeb334eabae | -5.87075 | -43.86294 | 2025-10-15 04:06:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| d73241ac-2f1e-35e4-9665-27b945ead7e9 | -6.89109 | -43.96403 | 2025-10-15 04:06:00 | NOAA-20 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 18bf9fd6-0b0a-3e87-a97e-93c20a6cfa01 | -7.74747 | -42.45899 | 2025-10-15 04:06:00 | NOAA-20 | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 4.9 |
| 8d693c90-9831-39e2-8627-8452ae6b2e2c | -6.33908 | -42.65569 | 2025-10-15 04:06:00 | NOAA-20 | AMARANTE | PIAUÍ | Brasil | 2200509 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 77ed9989-e458-3fe6-bfbb-ef7c7e12bf41 | -7.94897 | -44.14509 | 2025-10-15 04:06:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 1a11fd11-d1d6-38ce-8a84-016b1d1c0ee9 | -4.11181 | -48.02086 | 2025-10-15 04:06:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 1d0e86f1-2ec6-3ae2-83c2-b6ead6460fbc | -6.17237 | -42.61856 | 2025-10-15 04:06:00 | NOAA-20 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| f7a0f1a4-a79e-3570-b76b-a739e568414f | -5.88347 | -42.78296 | 2025-10-15 04:06:00 | NOAA-20 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 3.6 |
| 4075a6a3-bfc8-3a0f-894e-76e29f980d29 | -4.15182 | -43.12782 | 2025-10-15 04:06:00 | NOAA-20 | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 74e016ff-b1a5-3a9b-840b-69c9ab684f30 | -8.21848 | -44.06817 | 2025-10-15 04:06:00 | NOAA-20 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 08187148-6fbe-3196-b8bf-8234ff4c625c | -5.44402 | -44.30172 | 2025-10-15 04:06:00 | NOAA-20 | GRAÇA ARANHA | MARANHÃO | Brasil | 2104701 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| b65facfe-37aa-3214-9e3b-98bbda85f88d | -7.93978 | -44.13557 | 2025-10-15 04:06:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 537a110a-1dd8-3a4b-b959-512aeb92de96 | -5.31645 | -42.9271 | 2025-10-15 04:06:00 | NOAA-20 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 2b589710-bee8-30fe-a0b4-ee1c959d4612 | -5.3968 | -44.03786 | 2025-10-15 04:06:00 | NOAA-20 | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 3801766a-5475-38cf-a6d1-73131bd6fd39 | -6.32501 | -42.76428 | 2025-10-15 04:06:00 | NOAA-20 | AMARANTE | PIAUÍ | Brasil | 2200509 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| fd02842d-648c-3fa2-acdc-c5ab31cd7133 | -4.86881 | -45.67147 | 2025-10-15 04:06:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 70e45a2a-2f0a-32d8-b952-38ece8b8733f | -10.15887 | -36.17347 | 2025-10-15 04:06:00 | NOAA-20 | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| b6e6a6df-f46b-3cb2-9faa-32c040592c0b | -6.73917 | -42.15392 | 2025-10-15 04:06:00 | NOAA-20 | TANQUE DO PIAUÍ | PIAUÍ | Brasil | 2210979 | 22 | 33 | nan | nan | nan | Caatinga | 4.9 |
| 1ba7a49b-2339-3172-a1f4-309a4beff918 | -3.16285 | -48.6106 | 2025-10-15 04:06:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| be0315d3-51fa-3840-812d-213b466b8eb5 | -5.6821 | -46.4263 | 2025-10-15 04:06:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| b34b9e3b-b7a1-3d47-8c93-9f38ade90167 | -6.45829 | -41.84791 | 2025-10-15 04:06:00 | NOAA-20 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 4e291f95-6885-3315-a3d3-35f5c16dbd2e | -3.52845 | -50.31448 | 2025-10-15 04:06:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 0a002797-243d-3ee2-a870-d62c8ca57a50 | -3.16183 | -48.61062 | 2025-10-15 04:06:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 346ed51b-9cd4-3353-a0b7-1e9328c26c4d | -6.14568 | -41.76286 | 2025-10-15 04:06:00 | NOAA-20 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 16ed11d2-c32a-3c4b-84b1-c2f56f03e9a6 | -5.25397 | -44.89285 | 2025-10-15 04:06:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 24e92dd6-f191-31be-94fb-45932bf363ea | -4.75855 | -40.8675 | 2025-10-15 04:06:00 | NOAA-20 | ARARENDÁ | CEARÁ | Brasil | 2301257 | 23 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 44e20899-3dd1-3664-b70b-e7782715a944 | -5.87474 | -44.21414 | 2025-10-15 04:06:00 | NOAA-20 | JATOBÁ | MARANHÃO | Brasil | 2105450 | 21 | 33 | nan | nan | nan | Cerrado | 6.0 |
| e5fe1823-3526-3355-836b-a34f2b687767 | -3.6195 | -48.91888 | 2025-10-15 04:06:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 6cab1160-43f1-34fe-a785-e1830ba0ce47 | -5.4015 | -41.16267 | 2025-10-15 04:06:00 | NOAA-20 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 71c4403f-00e7-3483-a52f-f355a47c9c1b | -4.55179 | -43.91026 | 2025-10-15 04:06:00 | NOAA-20 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d3c2552b-45c6-352e-a369-8506af159054 | -4.88951 | -43.45825 | 2025-10-15 04:06:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 344c6e39-6430-3342-94cd-2d964bca50fc | -5.57197 | -41.33133 | 2025-10-15 04:06:00 | NOAA-20 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 821d6c33-d28c-3bae-b81e-ead2f279c52b | -4.89714 | -43.45545 | 2025-10-15 04:06:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 43.4 |
| 891db983-c63b-3796-950c-92343fc8f027 | -5.00859 | -44.49089 | 2025-10-15 04:06:00 | NOAA-20 | SÃO JOSÉ DOS BASÍLIOS | MARANHÃO | Brasil | 2111250 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 2ca91b5c-2895-32e2-88ae-7c79c533e484 | -7.45785 | -43.93246 | 2025-10-15 04:06:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 28451b68-b565-3e7b-873b-10ca019cee29 | -4.63698 | -42.52749 | 2025-10-15 04:06:00 | NOAA-20 | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 5356517d-62a8-3789-8c9b-6ad10732389d | -7.50747 | -46.6438 | 2025-10-15 04:06:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 6fffb35d-877a-39c6-9c89-86194496b2f5 | -6.82698 | -42.77747 | 2025-10-15 04:06:00 | NOAA-20 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| c205b7c2-4437-3d2b-9385-581a1f02bd8a | -7.08294 | -41.95838 | 2025-10-15 04:06:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 30be6f8a-d01e-3c72-972f-eeee178072a9 | -5.09377 | -44.94793 | 2025-10-15 04:06:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 2537968e-74f5-3b7d-b790-24bc4757a1b4 | -2.94697 | -49.33867 | 2025-10-15 04:06:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 9b14064f-82ab-3221-aecb-d119b0b9399a | -5.90912 | -42.83939 | 2025-10-15 04:06:00 | NOAA-20 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 4.5 |
| 7c4599c5-be51-39cd-b29f-5482802a949e | -5.90866 | -42.8206 | 2025-10-15 04:06:00 | NOAA-20 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 1a62ef34-6b8d-3e1b-8387-3bb80f05e2ff | -8.18248 | -44.0269 | 2025-10-15 04:06:00 | NOAA-20 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 74321b5a-5e43-383e-a65d-13fd2fb11943 | -4.6476 | -43.1375 | 2025-10-15 04:06:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |


[Clique aqui para ver as próximas entradas](README34.md)
