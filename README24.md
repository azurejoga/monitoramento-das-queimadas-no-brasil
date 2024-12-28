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

## Dados Diários - Página 24

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 723492a8-9ddc-3fbc-abd2-bb26399db69c | -11.97915 | -63.50877 | 2024-12-28 05:59:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a8647e9d-9695-35e4-8b0d-e55cde831b50 | -12.35124 | -64.17357 | 2024-12-28 05:59:00 | NOAA-21 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 2.8 |
| af832d82-fdfc-38e2-a968-7b17db1a88d9 | -16.10384 | -60.0723 | 2024-12-28 05:59:00 | NOAA-21 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 805757fa-a9bd-3e20-b3db-f9474a19b194 | -12.45363 | -64.14982 | 2024-12-28 05:59:00 | NOAA-21 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| fd739f6d-18c1-32f3-99aa-344e70f5c920 | -11.9102 | -64.05441 | 2024-12-28 05:59:00 | NOAA-21 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 04f5b364-ea69-384f-b96a-bb1568f4b8b6 | -10.49289 | -67.82199 | 2024-12-28 05:59:00 | NOAA-21 | CAPIXABA | ACRE | Brasil | 1200179 | 12 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ffaa691c-891a-325e-9a70-7af6326bfe26 | -15.27597 | -59.88113 | 2024-12-28 05:59:00 | NOAA-21 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| a2bf0b39-d834-3b9c-b353-768b64b44964 | 3.9598 | -60.55483 | 2024-12-28 06:18:00 | NPP-375D | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 3b35e754-e124-36fb-9bfb-24bea7e1945c | 3.96161 | -60.56547 | 2024-12-28 06:18:00 | NPP-375D | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 7.3 |
| bcfbf44e-5aa5-3d76-87eb-504cd4b03923 | 3.96087 | -60.56236 | 2024-12-28 06:18:00 | NPP-375D | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 13.1 |
| 5b737b81-a8c7-3315-a4c2-43d63e3f7808 | 3.95993 | -60.55705 | 2024-12-28 06:18:00 | NPP-375D | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 8.4 |
| 3fa28fe7-5186-3bc6-8a47-de8b3ce5aa24 | 3.96071 | -60.56017 | 2024-12-28 06:18:00 | NPP-375D | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 7.3 |
| ffbc5460-fc86-33c8-9001-71e864c470c5 | -12.34584 | -64.17379 | 2024-12-28 06:22:00 | NPP-375D | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 37eb136d-40ef-378d-b9c4-840e1ff884ff | -12.35229 | -64.17453 | 2024-12-28 06:22:00 | NPP-375D | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b2845614-c5d2-3b07-b783-fb0d39b3a1d0 | -5.47 | -42.93 | 2024-12-28 11:00:00 | MSG-03 | NAZÁRIA | PIAUÍ | Brasil | 2206720 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 415b08de-0f3b-3a33-961d-379bb50f1901 | -15.83 | -43.46 | 2024-12-28 12:00:00 | MSG-03 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| cf609f10-4c78-3db3-b3a1-13929132e154 | -2.92136 | -41.92857 | 2024-12-28 12:48:00 | TERRA_M-T | ARAIOSES | MARANHÃO | Brasil | 2100907 | 21 | 33 | nan | nan | nan | Caatinga | 84.3 |
| c41cb1c6-f1d4-3dee-82df-0677b34db167 | -1.81777 | -46.07456 | 2024-12-28 12:48:00 | TERRA_M-T | JUNCO DO MARANHÃO | MARANHÃO | Brasil | 2105658 | 21 | 33 | nan | nan | nan | Amazônia | 17.4 |
| 3471add6-ecf4-3803-a023-1d41297590f3 | -1.81618 | -46.08557 | 2024-12-28 12:48:00 | TERRA_M-T | JUNCO DO MARANHÃO | MARANHÃO | Brasil | 2105658 | 21 | 33 | nan | nan | nan | Amazônia | 14.1 |
| 20bab833-4805-30f6-a57b-297371e3e5f0 | -3.47893 | -40.84712 | 2024-12-28 12:48:00 | TERRA_M-T | TIANGUÁ | CEARÁ | Brasil | 2313401 | 23 | 33 | nan | nan | nan | Caatinga | 47.8 |
| 0da9c254-2f28-3e75-aed2-31da1a84e835 | -1.80765 | -45.21355 | 2024-12-28 12:48:00 | TERRA_M-T | BACURI | MARANHÃO | Brasil | 2101301 | 21 | 33 | nan | nan | nan | Amazônia | 11.0 |
| decda3f0-3634-3182-9909-d08aea9d818a | -1.82602 | -46.08692 | 2024-12-28 12:48:00 | TERRA_M-T | JUNCO DO MARANHÃO | MARANHÃO | Brasil | 2105658 | 21 | 33 | nan | nan | nan | Amazônia | 17.6 |
| 830f67ef-4408-30da-9a1d-4d0608be94ce | -1.82861 | -46.08194 | 2024-12-28 12:48:00 | TERRA_M-T | JUNCO DO MARANHÃO | MARANHÃO | Brasil | 2105658 | 21 | 33 | nan | nan | nan | Amazônia | 14.4 |
| 8fb91177-3975-3db1-b2f6-7bc34e22c617 | -1.34512 | -46.59059 | 2024-12-28 12:48:00 | TERRA_M-T | BRAGANÇA | PARÁ | Brasil | 1501709 | 15 | 33 | nan | nan | nan | Amazônia | 16.2 |
| e0402060-ca68-38fd-adde-b7c1d7ce7786 | -3.48193 | -40.84225 | 2024-12-28 12:48:00 | TERRA_M-T | TIANGUÁ | CEARÁ | Brasil | 2313401 | 23 | 33 | nan | nan | nan | Caatinga | 41.2 |
| 31d91876-eb08-3c36-9cc0-f02537d52e1c | -3.03411 | -44.75163 | 2024-12-28 12:48:00 | TERRA_M-T | SÃO JOÃO BATISTA | MARANHÃO | Brasil | 2111003 | 21 | 33 | nan | nan | nan | Amazônia | 11.8 |
| 6b400c3e-f1d1-31a3-b123-e81efb881e2d | -0.32425 | -48.42789 | 2024-12-28 12:48:00 | TERRA_M-T | SOURE | PARÁ | Brasil | 1507904 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| a2c8dadd-1234-3d7c-ba88-c597f7e5e797 | -2.43448 | -47.4837 | 2024-12-28 12:48:00 | TERRA_M-T | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 11.7 |
| 8ea316f5-1469-368b-a648-a0743d1b1bfb | -1.82762 | -46.07589 | 2024-12-28 12:48:00 | TERRA_M-T | JUNCO DO MARANHÃO | MARANHÃO | Brasil | 2105658 | 21 | 33 | nan | nan | nan | Amazônia | 23.4 |
| 416b66cd-18ab-360f-ab2c-27156894c1d1 | -1.65317 | -45.86827 | 2024-12-28 12:48:00 | TERRA_M-T | AMAPÁ DO MARANHÃO | MARANHÃO | Brasil | 2100550 | 21 | 33 | nan | nan | nan | Amazônia | 17.0 |
| 3b931bb4-bea3-333c-81ec-9f8aa601c269 | -2.43585 | -47.47422 | 2024-12-28 12:48:00 | TERRA_M-T | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 18.3 |
| e4383ad5-67b5-3dc2-a234-9be206cf4466 | -2.44502 | -47.47548 | 2024-12-28 12:48:00 | TERRA_M-T | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 64.9 |
| 7b12d40f-7aab-32bd-a64d-896c9c360322 | -2.47474 | -45.70433 | 2024-12-28 12:48:00 | TERRA_M-T | SANTA LUZIA DO PARUÁ | MARANHÃO | Brasil | 2110039 | 21 | 33 | nan | nan | nan | Amazônia | 12.7 |
| 3a693108-28bd-3354-9fe0-362257f108b3 | -2.44365 | -47.48497 | 2024-12-28 12:48:00 | TERRA_M-T | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 38.5 |
| 22af5b5e-b4d3-3432-a561-3681bff824e4 | -1.34366 | -46.6008 | 2024-12-28 12:48:00 | TERRA_M-T | BRAGANÇA | PARÁ | Brasil | 1501709 | 15 | 33 | nan | nan | nan | Amazônia | 29.2 |
| f71a3a81-e5a5-3ea0-b448-81389d559102 | -6.17866 | -45.7561 | 2024-12-28 12:50:00 | TERRA_M-T | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 33.2 |
| cf845dc2-25bb-3ea5-b160-9c3c4d5cb752 | -5.59872 | -45.88285 | 2024-12-28 12:50:00 | TERRA_M-T | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 13.6 |
| f85fddad-de91-345d-a86d-6b394ead3af4 | -5.65895 | -45.28235 | 2024-12-28 12:50:00 | TERRA_M-T | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 16.5 |
| 0e361906-89ee-388d-8db7-a93ec8b28d34 | -5.57578 | -46.12453 | 2024-12-28 12:50:00 | TERRA_M-T | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 9.7 |
| 5a5a969f-5e80-3bb6-a205-9049694724b4 | -4.71381 | -43.44978 | 2024-12-28 12:50:00 | TERRA_M-T | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 29.7 |
| 4d2f4dd5-5576-3b91-9483-16891d74b208 | -5.21792 | -41.25193 | 2024-12-28 12:50:00 | TERRA_M-T | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 59.3 |
| 3675f42d-2a4a-386b-8d13-58c8aabbf338 | -3.8283 | -43.03257 | 2024-12-28 12:50:00 | TERRA_M-T | BURITI | MARANHÃO | Brasil | 2102200 | 21 | 33 | nan | nan | nan | Cerrado | 25.0 |
| d2cccd3a-dd4c-399a-9649-5e50363035ac | -3.41681 | -46.34849 | 2024-12-28 12:50:00 | TERRA_M-T | SÃO JOÃO DO CARÚ | MARANHÃO | Brasil | 2111029 | 21 | 33 | nan | nan | nan | Amazônia | 18.9 |
| 0386daf8-3928-3736-9835-a744786b1621 | -4.5702 | -46.79938 | 2024-12-28 12:50:00 | TERRA_M-T | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 10.9 |
| 89e6f7c1-b40e-3606-bb0b-f88b380e2ba8 | -5.96197 | -41.82806 | 2024-12-28 12:50:00 | TERRA_M-T | SANTA CRUZ DOS MILAGRES | PIAUÍ | Brasil | 2209153 | 22 | 33 | nan | nan | nan | Caatinga | 43.7 |
| ac0a222e-7b52-3cc6-bddc-2cea99cc9d01 | -5.62492 | -45.27198 | 2024-12-28 12:50:00 | TERRA_M-T | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 14.1 |
| f9ef49d7-1af4-3b3a-aa46-ab6b5f99c071 | -5.17502 | -43.23372 | 2024-12-28 12:50:00 | TERRA_M-T | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 25.2 |
| 83db68ca-277e-348d-aa60-9beba08e2e4c | -4.52216 | -45.61228 | 2024-12-28 12:50:00 | TERRA_M-T | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Cerrado | 15.5 |
| 15d8045b-4405-38c3-bba5-43fcec2fa917 | -5.96237 | -41.83502 | 2024-12-28 12:50:00 | TERRA_M-T | SANTA CRUZ DOS MILAGRES | PIAUÍ | Brasil | 2209153 | 22 | 33 | nan | nan | nan | Caatinga | 62.4 |
| 54f88c54-588a-323f-9efb-a50d1daeb72e | -6.8544 | -41.98044 | 2024-12-28 12:50:00 | TERRA_M-T | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 27.9 |
| c63aadc5-2b18-3fa1-8f70-abe75255caac | -4.3457 | -47.08148 | 2024-12-28 12:50:00 | TERRA_M-T | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 7.3 |
| cb6e00f1-8063-325f-a439-0d7818a1034a | -4.65162 | -43.81896 | 2024-12-28 12:50:00 | TERRA_M-T | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 35.0 |
| 1116a372-18e8-3d37-8728-1512c2aa6f4a | -3.49143 | -44.93039 | 2024-12-28 12:50:00 | TERRA_M-T | VITÓRIA DO MEARIM | MARANHÃO | Brasil | 2112902 | 21 | 33 | nan | nan | nan | Amazônia | 16.1 |
| c7740de6-cff3-34a0-8ab5-fe26a28096e1 | -4.21837 | -43.9965 | 2024-12-28 12:50:00 | TERRA_M-T | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 17.0 |
| 6182689b-b541-3c54-9c47-b57f2473fa5f | -5.9145 | -43.46702 | 2024-12-28 12:50:00 | TERRA_M-T | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 31.9 |
| 35d22916-1d4e-3a05-b0ee-67492b22effa | -5.22178 | -41.22274 | 2024-12-28 12:50:00 | TERRA_M-T | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 34.3 |
| d989e7f4-5189-39e0-8328-9e15fe16e314 | -6.40891 | -44.74608 | 2024-12-28 12:50:00 | TERRA_M-T | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 20.4 |
| dff67cd2-11e3-3075-9a89-d23e1eb581f0 | -5.21533 | -41.257 | 2024-12-28 12:50:00 | TERRA_M-T | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 46.9 |
| a11b9b97-240b-3c9e-92a0-db7347c1acc2 | -5.87202 | -44.97803 | 2024-12-28 12:50:00 | TERRA_M-T | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 23.6 |
| d8a1eec9-ae0d-35c5-a5cc-e8ac47beeb32 | -3.82969 | -43.02604 | 2024-12-28 12:50:00 | TERRA_M-T | BURITI | MARANHÃO | Brasil | 2102200 | 21 | 33 | nan | nan | nan | Cerrado | 50.4 |
| b7e78582-3e42-3503-8752-4bb2873c59ed | -5.657 | -45.29671 | 2024-12-28 12:50:00 | TERRA_M-T | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 18.5 |
| 4cfa6c13-5558-3c83-91bb-31af17b2726c | -4.0777 | -47.08982 | 2024-12-28 12:50:00 | TERRA_M-T | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 29.1 |
| f34aa7e3-b70f-3faa-9a7c-bce3c6e4d308 | -4.34721 | -47.07095 | 2024-12-28 12:50:00 | TERRA_M-T | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 68.2 |
| daa97dd2-3c98-3775-92d7-f2a66e23682e | -4.50477 | -44.23075 | 2024-12-28 12:50:00 | TERRA_M-T | PERITORÓ | MARANHÃO | Brasil | 2108454 | 21 | 33 | nan | nan | nan | Cerrado | 17.3 |
| cb65c973-26a7-35a5-b446-2a0070973f11 | -5.47365 | -42.93288 | 2024-12-28 12:50:00 | TERRA_M-T | NAZÁRIA | PIAUÍ | Brasil | 2206720 | 22 | 33 | nan | nan | nan | Caatinga | 31.1 |
| 2ad3899f-f0cf-37f4-a81f-b7b1f2b960e4 | -3.18254 | -46.12469 | 2024-12-28 12:50:00 | TERRA_M-T | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 11.2 |
| 8931ff69-7ddd-367a-82a1-f194694bd849 | -5.17331 | -43.23899 | 2024-12-28 12:50:00 | TERRA_M-T | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 26.1 |
| a20a7932-38a6-302f-a0e1-85e65b2e67ad | -5.91186 | -43.48688 | 2024-12-28 12:50:00 | TERRA_M-T | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 20.7 |
| 766c4692-2990-32f6-bcd4-b8678a37253b | -5.62572 | -45.27787 | 2024-12-28 12:50:00 | TERRA_M-T | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 14.6 |
| 416980a6-52b5-3e70-aadf-ac6fe4af6e6f | -6.20728 | -42.63177 | 2024-12-28 12:50:00 | TERRA_M-T | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 42.9 |
| 74c76941-0f22-32d8-bbf0-df6c038bc9ad | -6.22114 | -42.63374 | 2024-12-28 12:50:00 | TERRA_M-T | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 28.2 |
| a444335e-1778-30a5-9a9b-c3e2610249e1 | -5.64576 | -43.71121 | 2024-12-28 12:50:00 | TERRA_M-T | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 20.2 |
| 9f9d4752-3061-34a3-815c-5f39585268a7 | -3.72906 | -47.1896 | 2024-12-28 12:50:00 | TERRA_M-T | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 7.3 |
| 6a2f9caf-b906-3b11-bd67-7c0b75df2a7a | -3.83097 | -43.01255 | 2024-12-28 12:50:00 | TERRA_M-T | BURITI | MARANHÃO | Brasil | 2102200 | 21 | 33 | nan | nan | nan | Cerrado | 38.6 |
| e837596b-e645-3673-854a-6a16e060dc6a | -5.21899 | -41.22763 | 2024-12-28 12:50:00 | TERRA_M-T | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 51.7 |
| cbc4a4d6-3e3b-3018-9dbe-230387d47bba | -4.07919 | -47.07946 | 2024-12-28 12:50:00 | TERRA_M-T | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 11.0 |
| bdf516ee-8ea8-3854-af10-14e043b63502 | -12.85131 | -42.35933 | 2024-12-28 12:53:00 | TERRA_M-T | IBIPITANGA | BAHIA | Brasil | 2912509 | 29 | 33 | nan | nan | nan | Caatinga | 57.4 |
| 2666c59c-1a8c-30a2-a584-914067307c45 | -10.2787 | -42.36003 | 2024-12-28 12:53:00 | TERRA_M-T | ITAGUAÇU DA BAHIA | BAHIA | Brasil | 2915353 | 29 | 33 | nan | nan | nan | Caatinga | 37.0 |
| 372bb021-e42d-3496-b187-13baba08c647 | -10.60874 | -44.97463 | 2024-12-28 12:53:00 | TERRA_M-T | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 32.2 |
| d4a24a62-a6ac-3ef6-955c-df945835849f | -8.99644 | -41.01697 | 2024-12-28 12:53:00 | TERRA_M-T | CASA NOVA | BAHIA | Brasil | 2907202 | 29 | 33 | nan | nan | nan | Caatinga | 220.7 |
| e78689fe-8abc-342e-9ed5-5c5fab7da7c7 | -8.32424 | -43.49277 | 2024-12-28 12:53:00 | TERRA_M-T | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Cerrado | 23.7 |
| 2ee681a3-5255-36c9-b409-368a65d8d536 | -8.99011 | -41.00936 | 2024-12-28 12:53:00 | TERRA_M-T | CASA NOVA | BAHIA | Brasil | 2907202 | 29 | 33 | nan | nan | nan | Caatinga | 149.2 |
| a83dc8ca-f613-392a-a6fd-9eb76ead791d | -10.27662 | -42.3667 | 2024-12-28 12:53:00 | TERRA_M-T | ITAGUAÇU DA BAHIA | BAHIA | Brasil | 2915353 | 29 | 33 | nan | nan | nan | Caatinga | 46.4 |
| e5849cf3-50a3-37f4-b57b-bce0f8f28bda | -10.60652 | -44.99294 | 2024-12-28 12:53:00 | TERRA_M-T | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 45.7 |
| 2c7be807-8083-35ac-8498-de3ac955bbc2 | -8.07352 | -44.34986 | 2024-12-28 12:53:00 | TERRA_M-T | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 27.4 |
| 6d638bb0-2f1f-382f-ac83-92f42cd29a8f | -10.2752 | -42.38899 | 2024-12-28 12:53:00 | TERRA_M-T | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 31.5 |
| 137b3ef2-6c6b-3a48-8427-62b05b85adac | -10.60327 | -44.98675 | 2024-12-28 12:53:00 | TERRA_M-T | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 78.3 |
| 46f0b54b-a685-3be1-a781-2be5aa97af6e | -8.98581 | -41.0447 | 2024-12-28 12:53:00 | TERRA_M-T | CASA NOVA | BAHIA | Brasil | 2907202 | 29 | 33 | nan | nan | nan | Caatinga | 47.9 |
| edffc401-d601-3dd6-bad9-7b9024d6c5a3 | -23.22053 | -51.05185 | 2024-12-28 12:55:00 | TERRA_M-T | IBIPORÃ | PARANÁ | Brasil | 4109807 | 41 | 33 | nan | nan | nan | Mata Atlântica | 8.0 |
| fad5872b-176c-3c3c-b7af-367f7efa2e1b | -21.62604 | -51.77903 | 2024-12-28 12:55:00 | TERRA_M-T | PRESIDENTE VENCESLAU | SÃO PAULO | Brasil | 3541505 | 35 | 33 | nan | nan | nan | Mata Atlântica | 9.3 |
| aeccc44e-51f8-339e-98cf-3152b60c385c | -20.03269 | -52.58378 | 2024-12-28 12:55:00 | TERRA_M-T | TRÊS LAGOAS | MATO GROSSO DO SUL | Brasil | 5008305 | 50 | 33 | nan | nan | nan | Cerrado | 8.7 |
| 2f6684d7-eec5-3677-9bbe-b6581279e526 | -23.60223 | -51.64429 | 2024-12-28 12:55:00 | TERRA_M-T | JANDAIA DO SUL | PARANÁ | Brasil | 4112108 | 41 | 33 | nan | nan | nan | Mata Atlântica | 8.0 |
| 321031bc-9c5c-3990-a076-5b75dddb7391 | -23.28921 | -51.07946 | 2024-12-28 12:55:00 | TERRA_M-T | IBIPORÃ | PARANÁ | Brasil | 4109807 | 41 | 33 | nan | nan | nan | Mata Atlântica | 9.1 |
| 36b21fd3-a58c-3ec2-b4b3-a0215326d709 | -23.53397 | -51.31658 | 2024-12-28 12:55:00 | TERRA_M-T | ARAPONGAS | PARANÁ | Brasil | 4101507 | 41 | 33 | nan | nan | nan | Mata Atlântica | 9.0 |
| d3a799a5-832b-3744-811b-27d9c691ddaa | -23.55239 | -51.73413 | 2024-12-28 12:55:00 | TERRA_M-T | MANDAGUARI | PARANÁ | Brasil | 4114203 | 41 | 33 | nan | nan | nan | Mata Atlântica | 6.7 |
| f536523b-965c-31d1-ace4-c08334840d6a | -21.48529 | -51.52823 | 2024-12-28 12:55:00 | TERRA_M-T | DRACENA | SÃO PAULO | Brasil | 3514403 | 35 | 33 | nan | nan | nan | Mata Atlântica | 7.6 |
| b3fb2798-9cc1-3788-a835-33c019235ae4 | -27.17754 | -51.50569 | 2024-12-28 12:57:00 | TERRA_M-T | JOAÇABA | SANTA CATARINA | Brasil | 4209003 | 42 | 33 | nan | nan | nan | Mata Atlântica | 8.1 |
| 11bca04b-847e-3ad9-a5e9-81ddae962d7a | -27.00686 | -51.15202 | 2024-12-28 12:57:00 | TERRA_M-T | VIDEIRA | SANTA CATARINA | Brasil | 4219309 | 42 | 33 | nan | nan | nan | Mata Atlântica | 9.9 |
| f7717b8a-1ee2-3514-97c1-04400b62dc0e | -28.60945 | -49.56028 | 2024-12-28 12:57:00 | TERRA_M-T | SIDERÓPOLIS | SANTA CATARINA | Brasil | 4217600 | 42 | 33 | nan | nan | nan | Mata Atlântica | 9.1 |
| faa9206d-ff92-31cf-813d-9e1cd962a644 | -29.5732 | -50.79392 | 2024-12-28 12:57:00 | TERRA_M-T | IGREJINHA | RIO GRANDE DO SUL | Brasil | 4310108 | 43 | 33 | nan | nan | nan | Mata Atlântica | 10.4 |


[Clique aqui para ver as próximas entradas](README25.md)
