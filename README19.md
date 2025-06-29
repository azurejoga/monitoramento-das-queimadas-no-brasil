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

## Dados Diários - Página 19

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| bb94f2c1-9770-34af-ae20-67e6eb96e586 | -9.15179 | -46.35308 | 2025-06-29 04:32:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 582c9fc4-ab01-392e-b26d-e0eb9fd41781 | -9.42139 | -47.95097 | 2025-06-29 04:32:00 | NOAA-20 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 13.4 |
| 6c35b9a2-0e59-3cb8-a498-e000222898d6 | -4.54306 | -48.01656 | 2025-06-29 04:32:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3d03a6ab-ec47-33e2-bebe-bad27915df4d | -9.08403 | -59.48764 | 2025-06-29 04:32:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 7b891512-3772-3666-81e5-f4b30699d6ce | -9.71153 | -56.18333 | 2025-06-29 04:32:00 | NOAA-20 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 42d94762-c1e7-3724-825f-a00aef2b25bf | -5.57157 | -45.21566 | 2025-06-29 04:32:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 88fd930d-6bd9-3b6d-81ef-a52e0d4cd082 | -6.80183 | -47.97832 | 2025-06-29 04:32:00 | NOAA-20 | WANDERLÂNDIA | TOCANTINS | Brasil | 1722081 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| bf98dcc0-8e38-3a10-bf58-9192531edd76 | -7.19 | -43.70113 | 2025-06-29 04:32:00 | NOAA-20 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 494ea908-33df-356f-ae18-619a0545d352 | -10.83684 | -53.76774 | 2025-06-29 04:32:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 71c3e3cf-f488-3909-8830-4b245049d3e3 | -10.30303 | -57.13794 | 2025-06-29 04:32:00 | NOAA-20 | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1a5f20e5-b824-3bce-828b-c5029d816fec | -4.42169 | -47.66551 | 2025-06-29 04:32:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8e775875-70bc-3574-afc1-5cfc7480749c | -7.12584 | -45.52481 | 2025-06-29 04:32:00 | NOAA-20 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 6f5aef41-b0ad-3b50-98ca-470cabc6b818 | -5.42684 | -49.08136 | 2025-06-29 04:32:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 34c4c6e7-cf6f-3ebd-aaf4-8155a294eb37 | -10.55832 | -52.047 | 2025-06-29 04:32:00 | NOAA-20 | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 86cda1ca-df5d-3729-aeb8-6118bec70ece | -5.18935 | -47.73377 | 2025-06-29 04:32:00 | NOAA-20 | CIDELÂNDIA | MARANHÃO | Brasil | 2103257 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ab0c205b-f0ac-377a-ab0f-4aa9221aad1e | -10.56981 | -52.04467 | 2025-06-29 04:32:00 | NOAA-20 | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 9cd770d1-dcee-3522-a879-cf8c6c1721af | -5.19211 | -47.73773 | 2025-06-29 04:32:00 | NOAA-20 | CIDELÂNDIA | MARANHÃO | Brasil | 2103257 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 3bb4b02f-38ed-38fc-8b17-020e97b690df | -10.29963 | -57.1283 | 2025-06-29 04:32:00 | NOAA-20 | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 7181e1c3-24a4-3040-9cea-8f3ab163f46d | -4.69847 | -48.58073 | 2025-06-29 04:32:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 0d300495-14b7-3197-ab61-63b5f595c65d | -7.55534 | -45.84439 | 2025-06-29 04:32:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| fd0c0d9a-b767-3efa-be18-a913961ec4e3 | -9.47163 | -57.83995 | 2025-06-29 04:32:00 | NOAA-20 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 9caee7f9-e1fe-36a0-b40d-d15808f48fa9 | -7.39962 | -44.56377 | 2025-06-29 04:32:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| f4100f39-3e1e-364c-91c9-8e926d5dc962 | -10.93189 | -49.42585 | 2025-06-29 04:32:00 | NOAA-20 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| b8737fd9-3dbf-30d0-9a58-d015f115d20d | -10.564 | -52.03502 | 2025-06-29 04:32:00 | NOAA-20 | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| cbc00612-eb88-32ea-8682-66b5e3a3791d | -8.85212 | -50.16211 | 2025-06-29 04:32:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9070cf01-6b24-387e-af74-349f381242aa | -7.18679 | -43.42781 | 2025-06-29 04:32:00 | NOAA-20 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 015e0796-77b9-372d-9b12-669e701b5397 | -9.97783 | -47.80008 | 2025-06-29 04:32:00 | NOAA-20 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a991349a-ea22-3a13-aa23-465dc52cd2ce | -4.55463 | -48.00774 | 2025-06-29 04:32:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 6c4648af-93c8-3d91-a61e-7d265f09f7a0 | -11.82476 | -47.51203 | 2025-06-29 04:32:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| cd1b190a-7c46-3c32-b16f-1df0f1400f09 | -10.97375 | -45.11097 | 2025-06-29 04:32:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 3310cd08-0bf5-36ed-9a9c-c6f3ece87705 | -10.56109 | -52.0302 | 2025-06-29 04:32:00 | NOAA-20 | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| a9d77289-6e1d-3437-9ef4-b447769ca244 | -5.08405 | -48.35491 | 2025-06-29 04:32:00 | NOAA-20 | SÃO PEDRO DA ÁGUA BRANCA | MARANHÃO | Brasil | 2111532 | 21 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 510b76d9-c5b9-33ba-bf2c-5b1686520c60 | -8.37616 | -51.07633 | 2025-06-29 04:32:00 | NOAA-20 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| bfd63624-7718-3272-8fb4-2301321e27e3 | -10.86894 | -53.74705 | 2025-06-29 04:32:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 8bbb536e-a05f-3379-a0be-27eacb864ea1 | -10.56621 | -52.04404 | 2025-06-29 04:32:00 | NOAA-20 | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 5d772e41-6bbe-3253-a587-d3bfcf2e6a7f | -7.55939 | -45.84111 | 2025-06-29 04:32:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a9ab7d1d-dc1d-301b-9a7c-444a92c0fafb | -10.97001 | -45.11039 | 2025-06-29 04:32:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 6fb23062-5785-388e-a10a-51f194056e90 | -8.84694 | -50.17257 | 2025-06-29 04:32:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 57c79bfd-dcb9-3b0f-ab0d-697f1c5839d9 | -9.11196 | -59.05341 | 2025-06-29 04:32:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d92d5d31-9229-3310-bfc9-12e1aa0b7e09 | -7.40133 | -44.5773 | 2025-06-29 04:32:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 4a36bd8e-0160-32ff-abe1-65a6d591452d | -7.40199 | -44.57294 | 2025-06-29 04:32:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 04b1e5a8-f224-33e6-a65b-a8046113085f | -10.54113 | -42.53865 | 2025-06-29 04:32:00 | NOAA-20 | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 2.3 |
| aaa4d69c-1f2d-3443-a62f-6c3e7d9066f4 | -10.16002 | -53.92906 | 2025-06-29 04:32:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 4c393f2e-f7f7-337d-97ad-5a9e05bef130 | -10.23002 | -54.29466 | 2025-06-29 04:32:00 | NOAA-20 | MATUPÁ | MATO GROSSO | Brasil | 5105606 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 00ff7237-23c7-3230-83b8-4938bf9a7170 | -7.18854 | -43.71088 | 2025-06-29 04:32:00 | NOAA-20 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 0735482c-3fb0-3e6f-837b-37de8ead320f | -6.3316 | -43.75208 | 2025-06-29 04:32:00 | NOAA-20 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 228f746b-313a-30a6-a609-a23cfc5a9adf | -9.08831 | -59.49752 | 2025-06-29 04:32:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 43c8c0f6-c861-3bbd-a589-34347fa78a1d | -9.27505 | -40.4433 | 2025-06-29 04:32:00 | NOAA-20 | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 1.1 |
| d856fcf0-2059-3d89-b921-96ec4b7eff3f | -7.18039 | -43.65961 | 2025-06-29 04:32:00 | NOAA-20 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 60e2df92-fbb5-3820-b95d-c47ab9b11b58 | -4.66234 | -55.96734 | 2025-06-29 04:32:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| bc1fa0a5-3dc3-30da-876d-24d9f97027aa | -9.14715 | -46.38359 | 2025-06-29 04:32:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| c59c2763-8d32-3bfe-a7b7-0229488bf6ff | -10.865 | -53.74633 | 2025-06-29 04:32:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| a99f5df5-af45-37f8-b820-b8234fb03ab8 | -9.10574 | -59.05257 | 2025-06-29 04:32:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 2be6df2a-57e4-39e4-bc25-e10d22a18a34 | -9.79452 | -48.56139 | 2025-06-29 04:32:00 | NOAA-20 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 75ff2548-a315-38b1-a7ca-bd8523efd074 | -10.30251 | -57.1408 | 2025-06-29 04:32:00 | NOAA-20 | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d8f00fc9-6ed5-3e52-880d-be4c9cba5886 | -9.43798 | -47.95361 | 2025-06-29 04:32:00 | NOAA-20 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| c4970d06-c69b-3c92-9cf9-f35e271c3249 | -8.08993 | -46.8607 | 2025-06-29 04:32:00 | NOAA-20 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a3541fa0-32f1-3e88-ae90-f27b569df901 | -11.68266 | -48.27888 | 2025-06-29 04:32:00 | NOAA-20 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f2ce7552-3d73-3c58-a0de-c700f7bb110c | -7.0925 | -43.65526 | 2025-06-29 04:32:00 | NOAA-20 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 43743364-e6e2-30f6-bffe-3ef4fd10bd94 | -10.56857 | -52.03903 | 2025-06-29 04:32:00 | NOAA-20 | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ab04d4b9-ab3b-3757-bb71-28d1b80a3c27 | -10.85139 | -53.75438 | 2025-06-29 04:32:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| d679b49a-5969-3d7a-b450-e1cf068db3ca | -7.1878 | -43.71574 | 2025-06-29 04:32:00 | NOAA-20 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 27999db6-04b0-3224-9670-cce0ba02e452 | -10.28822 | -57.02223 | 2025-06-29 04:32:00 | NOAA-20 | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| eb5674d4-92ed-3a77-890d-d91bcf13aa68 | -10.62284 | -48.69453 | 2025-06-29 04:32:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| e8b4104b-73ce-3e19-855a-c7ac862fa9d8 | -4.31937 | -48.07736 | 2025-06-29 04:32:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| ddf2dfb8-8cf7-3100-a8fa-e706e3873da9 | -10.87326 | -53.76912 | 2025-06-29 04:32:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 570025e6-f134-332d-bff0-a21d56313a37 | -7.19413 | -43.70885 | 2025-06-29 04:32:00 | NOAA-20 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 32ba276d-18b2-38d9-b575-b68eac800aee | -11.58101 | -44.83223 | 2025-06-29 04:32:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 55ac491d-bc26-31f8-a7b8-09c4cf63e717 | -10.85444 | -53.76023 | 2025-06-29 04:32:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ef18735a-5139-3d02-8d9b-40d520d73425 | -10.52777 | -53.62313 | 2025-06-29 04:32:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 8684f1e7-161b-3ef8-ae0f-0ed22ce77518 | -10.29911 | -57.13116 | 2025-06-29 04:32:00 | NOAA-20 | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| b0fbb7c9-b14a-35dc-b9ef-42317ebacc61 | -9.7068 | -56.1825 | 2025-06-29 04:32:00 | NOAA-20 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 4.8 |
| f26e3c6a-b7f8-38fe-a686-d86388d414b9 | -5.08792 | -48.35196 | 2025-06-29 04:32:00 | NOAA-20 | SÃO PEDRO DA ÁGUA BRANCA | MARANHÃO | Brasil | 2111532 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 15a2d9bc-1644-3bdf-9a67-95279b1c239b | -14.22226 | -45.50649 | 2025-06-29 04:34:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 3bc99f41-950d-38f1-8901-aea2233b3453 | -17.39993 | -42.61717 | 2025-06-29 04:34:00 | NOAA-20 | TURMALINA | MINAS GERAIS | Brasil | 3169703 | 31 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 72f4a127-8f7c-3bb3-956d-6b844015379a | -11.02796 | -56.27302 | 2025-06-29 04:34:00 | NOAA-20 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 927a6c4f-ff95-33e3-bbad-f250012791d7 | -12.48548 | -58.47387 | 2025-06-29 04:34:00 | NOAA-20 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 6e334f63-734d-398a-949d-b513db53e976 | -17.76186 | -52.44168 | 2025-06-29 04:34:00 | NOAA-20 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 07ffcdd4-c80a-35e1-a526-b62d1c5556b0 | -13.10184 | -52.29647 | 2025-06-29 04:34:00 | NOAA-20 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 6a5bd17e-a2d7-33c0-a92b-d802b7fc710f | -12.62101 | -54.2101 | 2025-06-29 04:34:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 8.5 |
| c64a02e6-5349-30cc-a150-49bdb85707e8 | -14.53043 | -53.77019 | 2025-06-29 04:34:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 0.5 |
| c2ec7a12-b4ed-37f9-a090-257a840f8b47 | -9.92429 | -59.90246 | 2025-06-29 04:34:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 49512738-d2cb-38b0-af13-6bde8cdcf5ec | -12.60089 | -57.87661 | 2025-06-29 04:34:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 76125837-97aa-3815-8337-91414f10715d | -11.01917 | -56.27981 | 2025-06-29 04:34:00 | NOAA-20 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 5d6ec856-40f0-3ba6-bdf5-a37f64e807be | -11.56165 | -52.79505 | 2025-06-29 04:34:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 3.9 |
| f0cd3320-6a09-3bf3-a6a4-07af0b62f102 | -13.13956 | -56.80708 | 2025-06-29 04:34:00 | NOAA-20 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 556b2bb0-7fc5-3f2b-9b4b-a394878a3bdf | -12.4861 | -58.47067 | 2025-06-29 04:34:00 | NOAA-20 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| b877dde5-04cc-32fa-aa10-99eb7aedd420 | -12.50299 | -58.35593 | 2025-06-29 04:34:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 583d938b-da82-3d30-94af-827bc5ca38fe | -12.49845 | -58.35155 | 2025-06-29 04:34:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 1664d3e6-5dd8-3e04-a4b9-a58d9258d129 | -18.3773 | -44.4995 | 2025-06-29 04:34:00 | NOAA-20 | CORINTO | MINAS GERAIS | Brasil | 3119104 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 01203284-ee11-30bf-8137-f4e5e4a257ba | -15.72807 | -49.55346 | 2025-06-29 04:34:00 | NOAA-20 | ITAGUARU | GOIÁS | Brasil | 5210604 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 39e7d212-753d-34a5-9a9f-3188600575d8 | -11.0307 | -56.25827 | 2025-06-29 04:34:00 | NOAA-20 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 82ab59d2-fe92-3bad-a8a6-f91bfca5f48f | -12.99394 | -59.05473 | 2025-06-29 04:34:00 | NOAA-20 | CAMPOS DE JÚLIO | MATO GROSSO | Brasil | 5102686 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| b201a492-4fa7-3018-ac3e-16817cf2fb56 | -14.52963 | -48.2566 | 2025-06-29 04:34:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 225c9f94-99a2-325b-a8e0-2cf05068d5c4 | -11.03351 | -56.26897 | 2025-06-29 04:34:00 | NOAA-20 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 4.8 |
| e4a95d8c-d765-3c01-b7e2-781d85da78f3 | -14.89233 | -48.40816 | 2025-06-29 04:34:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 9181a2c7-b521-3b1d-ab6b-80f2c6ce4933 | -12.10763 | -54.57813 | 2025-06-29 04:34:00 | NOAA-20 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 34a795b4-6d8f-34fc-83a5-c8ca9e5fab04 | -11.02979 | -56.26318 | 2025-06-29 04:34:00 | NOAA-20 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 3e76394e-ca92-3e43-a4a9-233e48bd6650 | -11.25844 | -52.7475 | 2025-06-29 04:34:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 5354bf34-e646-3971-b8cb-13b1acfb0ac7 | -18.78849 | -52.58328 | 2025-06-29 04:34:00 | NOAA-20 | CHAPADÃO DO SUL | MATO GROSSO DO SUL | Brasil | 5002951 | 50 | 33 | nan | nan | nan | Cerrado | 23.8 |


[Clique aqui para ver as próximas entradas](README20.md)
