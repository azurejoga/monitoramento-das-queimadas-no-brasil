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

## Dados Diários - Página 373

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 0fd474d5-5d80-3bc4-846f-91c0f7c64741 | -4.70472 | -40.07879 | 2026-10-08 16:39:00 | NOAA-20 | CATUNDA | CEARÁ | Brasil | 2303659 | 23 | 33 | nan | nan | nan | Caatinga | 5.4 |
| 96f835df-073e-3509-a187-4d2e2223561b | -3.74426 | -58.49236 | 2026-10-08 16:39:00 | NOAA-20 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 9806b35d-c599-362f-8ff8-963844e4a469 | -5.41112 | -45.64442 | 2026-10-08 16:39:00 | NOAA-20 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| da548cb9-d5bb-3cc0-8c03-0752362dde27 | -4.51754 | -54.89553 | 2026-10-08 16:39:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| d4c88c85-84d4-35a1-8542-f2db0ae0dbef | -5.3494 | -45.72834 | 2026-10-08 16:39:00 | NOAA-20 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 39.6 |
| 02da07de-ed96-3c74-8b87-3d2ffd0e9b03 | -1.71352 | -47.85784 | 2026-10-08 16:39:00 | NOAA-20 | SÃO DOMINGOS DO CAPIM | PARÁ | Brasil | 1507201 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 7b19932a-64a3-3af3-86d5-e4cb5f81f5c8 | -3.27595 | -44.20728 | 2026-10-08 16:39:00 | NOAA-20 | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| f291453a-47b4-3a47-9b0d-d4bc56150a1d | -5.39541 | -42.9567 | 2026-10-08 16:39:00 | NOAA-20 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Caatinga | 5.7 |
| 15d972c8-ae68-3d26-aa51-4ac8b6b62a73 | -3.18286 | -58.65417 | 2026-10-08 16:39:00 | NOAA-20 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 29.4 |
| a9f28fc8-0e9f-37a4-8de2-be828065bf72 | -6.74501 | -50.96105 | 2026-10-08 16:39:00 | NOAA-20 | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 7.3 |
| ee737479-d1bb-3fea-bb71-18071790259c | -6.58203 | -53.01907 | 2026-10-08 16:39:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 26.0 |
| da591ed7-32cb-3d80-9211-9decb1ea3e90 | -6.12967 | -51.95529 | 2026-10-08 16:39:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 79b40175-4943-3873-bd75-8aae989d1c6d | -5.70949 | -53.45213 | 2026-10-08 16:39:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 22.5 |
| a42f47b6-80c8-3aac-a306-cbc18aafd48f | -5.705 | -53.48783 | 2026-10-08 16:39:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 31.9 |
| 6c2c3c70-38ed-3b09-9cf6-eea5183299e2 | -1.29014 | -54.56646 | 2026-10-08 16:39:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 8.3 |
| f2a6dcdb-6ee8-3c62-ba23-7d8719c07918 | -5.50905 | -42.84846 | 2026-10-08 16:39:00 | NOAA-20 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Caatinga | 9.3 |
| da6a9998-9417-3f4f-9f58-d220a47fb01c | -3.99381 | -39.31005 | 2026-10-08 16:39:00 | NOAA-20 | APUIARÉS | CEARÁ | Brasil | 2300903 | 23 | 33 | nan | nan | nan | Caatinga | 5.9 |
| ead97ed2-fb4b-35e9-a67e-2bf001649f6a | -0.84921 | -48.59854 | 2026-10-08 16:39:00 | NOAA-20 | SALVATERRA | PARÁ | Brasil | 1506302 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 3e2a3863-8585-3b78-9037-ed3f2b23aa95 | -3.04948 | -57.47901 | 2026-10-08 16:39:00 | NOAA-20 | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 6aaf0a5e-d99c-3dce-81a8-e70b4d5a334c | -3.01995 | -54.736 | 2026-10-08 16:39:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 21.2 |
| b4613b9d-f7b4-33d1-9faf-36b02d63dd49 | -3.08955 | -58.00759 | 2026-10-08 16:39:00 | NOAA-20 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 3.8 |
| a30e0a6c-bfca-3b5c-8e50-8b00351a32d7 | -2.07969 | -45.85349 | 2026-10-08 16:39:00 | NOAA-20 | GOVERNADOR NUNES FREIRE | MARANHÃO | Brasil | 2104677 | 21 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 0fa14064-4475-3a18-a5f3-dec4a286f36c | -6.74232 | -55.1403 | 2026-10-08 16:39:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 44.7 |
| 7120a734-3f07-36ac-a812-009cf016a682 | -3.89415 | -38.66043 | 2026-10-08 16:39:00 | NOAA-20 | MARANGUAPE | CEARÁ | Brasil | 2307700 | 23 | 33 | nan | nan | nan | Caatinga | 4.0 |
| a2060fbf-67c3-33f5-a2c3-675668de1937 | -3.28261 | -44.24965 | 2026-10-08 16:39:00 | NOAA-20 | SANTA RITA | MARANHÃO | Brasil | 2110203 | 21 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 5eb90a7d-bca6-3f7c-b791-69a55d3e811a | -6.84317 | -59.29465 | 2026-10-08 16:39:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 31.6 |
| 4c99df72-9c92-3ea4-912e-fcb4ca188ccf | -2.69404 | -49.05207 | 2026-10-08 16:39:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 5b840e1d-ba29-341f-9ab7-c94fe00f84ff | -4.37024 | -55.31956 | 2026-10-08 16:39:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 12.3 |
| 398f1ab9-6a47-3695-812b-c81dbe68ec96 | -2.74421 | -54.11091 | 2026-10-08 16:39:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 182.3 |
| fe4c7e47-faea-351c-9233-5dd6dc7e591e | -3.11921 | -54.16735 | 2026-10-08 16:39:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 52.5 |
| b021889c-9b78-3ed8-9329-3af9c5be21fd | -2.69772 | -49.03928 | 2026-10-08 16:39:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 13.0 |
| 685eda4b-edd9-317e-998d-e13436ba347e | -4.77751 | -55.744 | 2026-10-08 16:39:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 10.7 |
| 332f9d28-b3b6-3594-b090-865997fcc1c3 | -6.85737 | -59.39072 | 2026-10-08 16:39:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 9.7 |
| 1ce2f840-bd79-358a-8e61-5bb19e60a001 | -3.28847 | -53.70961 | 2026-10-08 16:39:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 66.5 |
| d19ace86-501d-3550-b449-22069a328cc5 | -3.06138 | -57.47718 | 2026-10-08 16:39:00 | NOAA-20 | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | 6.9 |
| aae975e9-3d54-382f-8869-2fdbcf2240d4 | -6.19856 | -53.14762 | 2026-10-08 16:39:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 11.1 |
| 2c7c69b4-2036-35d5-a17b-65f6d183ed77 | -2.84008 | -54.13033 | 2026-10-08 16:39:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 48.4 |
| 5742e183-ab88-38b8-ac29-f69247551c8a | -2.69482 | -49.0436 | 2026-10-08 16:39:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 7f06ccbe-f80e-3435-b730-09f62b222b36 | -2.43939 | -58.01593 | 2026-10-08 16:39:00 | NOAA-20 | SÃO SEBASTIÃO DO UATUMÃ | AMAZONAS | Brasil | 1303957 | 13 | 33 | nan | nan | nan | Amazônia | 3.6 |
| cdac01c1-bfc6-3595-9f5c-6269b14b430a | -2.88212 | -40.40689 | 2026-10-08 16:39:00 | NOAA-20 | CRUZ | CEARÁ | Brasil | 2304251 | 23 | 33 | nan | nan | nan | Caatinga | 3.1 |
| 5e9c47c9-aa51-31d5-972a-a795dc612e1f | -3.98388 | -56.21526 | 2026-10-08 16:39:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 9.6 |
| b2d97c29-bafb-3dcd-8904-e863eabbedc3 | -3.876 | -42.83835 | 2026-10-08 16:39:00 | NOAA-20 | BURITI | MARANHÃO | Brasil | 2102200 | 21 | 33 | nan | nan | nan | Caatinga | 3.3 |
| 0891a1f7-5382-3093-bdfa-dfff6950e596 | -3.10222 | -57.65838 | 2026-10-08 16:39:00 | NOAA-20 | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 1347a62a-24cb-307d-aae5-1d6924553308 | -6.72872 | -55.12079 | 2026-10-08 16:39:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 02a74c8e-ac24-3031-8a35-38a19fb131a2 | -3.91613 | -55.74371 | 2026-10-08 16:39:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 8.8 |
| 030f3326-6c58-33f2-943f-a520f962d9b9 | -3.06024 | -57.32016 | 2026-10-08 16:39:00 | NOAA-20 | BARREIRINHA | AMAZONAS | Brasil | 1300508 | 13 | 33 | nan | nan | nan | Amazônia | 21.5 |
| 47067cac-daa1-364e-9ee2-13c72a97f4ec | -6.44349 | -52.66843 | 2026-10-08 16:39:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 8.0 |
| d82b5b05-4da1-3669-aab2-e497611c7af9 | -3.17123 | -58.62978 | 2026-10-08 16:39:00 | NOAA-20 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 11.9 |
| 6d517c22-1487-30f5-9ed9-2b01a1ff9c4d | -5.69527 | -53.45385 | 2026-10-08 16:39:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 63.1 |
| 7833b898-3d2e-3c36-a796-d3e9668ad911 | -0.8555 | -47.54912 | 2026-10-08 16:39:00 | NOAA-20 | MARACANÃ | PARÁ | Brasil | 1504307 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 0d92d5ce-2aab-32ce-bd56-69a6eba116dd | -6.25864 | -52.67765 | 2026-10-08 16:39:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 52a595dd-3c83-3872-b665-4bb036354f03 | -3.20416 | -57.89209 | 2026-10-08 16:39:00 | NOAA-20 | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | 7.3 |
| 791dc6ab-a53e-36a2-881b-e6d901cb70f6 | -5.47901 | -42.87034 | 2026-10-08 16:39:00 | NOAA-20 | NAZÁRIA | PIAUÍ | Brasil | 2206720 | 22 | 33 | nan | nan | nan | Caatinga | 11.9 |
| 1967c6a7-9cd3-342a-bb34-2f1cc85b8259 | -3.00692 | -54.07176 | 2026-10-08 16:39:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 17.8 |
| 870d2018-693e-313a-a32b-39e636b36b47 | -3.93824 | -56.0216 | 2026-10-08 16:39:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 15.1 |
| 2abc85a3-201e-3397-8f46-3333c1c5a53c | -3.09594 | -53.94893 | 2026-10-08 16:39:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 59.5 |
| adde514f-dc94-32bd-b86d-b000a9aa37ec | -2.66436 | -43.95302 | 2026-10-08 16:39:00 | NOAA-20 | ICATU | MARANHÃO | Brasil | 2105104 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 754942a7-d733-3978-b869-38553aea66b8 | -3.30675 | -54.69882 | 2026-10-08 16:39:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 11.1 |
| d61d579e-3b9a-3776-b4e1-069936ee3518 | -5.46851 | -45.79729 | 2026-10-08 16:39:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 59ab61b7-85df-3b36-9286-91a924c9fa71 | -4.33366 | -43.79824 | 2026-10-08 16:39:00 | NOAA-20 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 67.7 |
| ed6f8ea8-25ce-3724-a0bc-809021788517 | -3.40231 | -58.0419 | 2026-10-08 16:39:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 9f0d5a4a-853d-3d7c-96dd-10d09a300d78 | -2.78657 | -57.64122 | 2026-10-08 16:39:00 | NOAA-20 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 18.7 |
| d3986f98-225e-399c-8ea3-7026aa291fbc | -4.59406 | -42.79136 | 2026-10-08 16:39:00 | NOAA-20 | UNIÃO | PIAUÍ | Brasil | 2211100 | 22 | 33 | nan | nan | nan | Cerrado | 6.1 |
| c04f9573-fbda-36eb-8eff-221b3755369c | -5.878 | -45.94529 | 2026-10-08 16:39:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 9.0 |
| 587a44e1-882c-3143-97ac-f468b09f32a7 | -6.13303 | -53.5072 | 2026-10-08 16:39:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 38.6 |
| 6f67b451-60b9-371f-8d11-f2f164e83008 | -5.24323 | -50.90182 | 2026-10-08 16:39:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 10.2 |
| c993a57b-7607-325e-ae9f-f74fbb3907b8 | -3.73814 | -51.20872 | 2026-10-08 16:39:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 14.9 |
| 4479846d-168c-3da1-84af-8f79de905bb7 | -5.39774 | -45.66776 | 2026-10-08 16:39:00 | NOAA-20 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 24.9 |
| b52c6ab4-4afd-3303-8c45-11086afedd48 | -4.84863 | -43.3639 | 2026-10-08 16:39:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 394125c2-9e02-351c-aad7-d3f92129418b | -5.2851 | -42.73357 | 2026-10-08 16:39:00 | NOAA-20 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Caatinga | 12.4 |
| 2b646aae-4f46-38e8-ae14-fb0189b71759 | -6.22675 | -52.7882 | 2026-10-08 16:39:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 19.4 |
| d0a33e6d-4e78-3f50-b915-88161209a521 | -3.06405 | -44.34258 | 2026-10-08 16:39:00 | NOAA-20 | BACABEIRA | MARANHÃO | Brasil | 2101251 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| e5f07c72-ef9f-3122-ba60-ab0442cb38d7 | -6.36008 | -55.15216 | 2026-10-08 16:39:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| b5f72f15-cf99-371a-9319-56d847d05b9f | -3.85411 | -58.89868 | 2026-10-08 16:39:00 | NOAA-20 | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 41.9 |
| 185cc9a2-9d79-3af8-8f6e-da5b55895877 | -3.13113 | -42.93139 | 2026-10-08 16:39:00 | NOAA-20 | BARREIRINHAS | MARANHÃO | Brasil | 2101707 | 21 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 15b95e1d-e167-3683-9f70-f14881ba17f4 | -0.09538 | -49.48759 | 2026-10-08 16:39:00 | NOAA-20 | CHAVES | PARÁ | Brasil | 1502509 | 15 | 33 | nan | nan | nan | Amazônia | 23.6 |
| 1b5ab0d4-e42e-3ffd-a904-c650b391231f | -7.20425 | -55.19189 | 2026-10-08 16:39:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 8.6 |
| 1c276751-7edc-38c3-b66d-de9852099875 | -5.3833 | -45.68416 | 2026-10-08 16:39:00 | NOAA-20 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| c23936b1-d8e2-3863-b3dc-e9199db04713 | -1.4286 | -54.6092 | 2026-10-08 16:39:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 14.8 |
| e6bc2d7c-4f36-3751-82fc-a3732a1de79f | -5.06595 | -46.18367 | 2026-10-08 16:39:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 11.3 |
| 0e7b4edc-cb8f-3c56-b40b-28e4dfb3a544 | -3.08974 | -53.93968 | 2026-10-08 16:39:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 35.5 |
| a11e8d97-ab63-3823-bf3a-1eb96582af63 | -6.24518 | -52.88505 | 2026-10-08 16:39:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 14.4 |
| 776dd80f-c7e1-3dfc-9437-e00c27bb88f5 | -3.02586 | -54.06126 | 2026-10-08 16:39:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 25.4 |
| 7bf91b2a-4a84-33c8-8f50-5cdd8cda016d | -6.18567 | -53.42956 | 2026-10-08 16:39:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 9.3 |
| 4bf290e2-4d25-35a9-a517-d6785f18c0ea | -6.13504 | -51.75587 | 2026-10-08 16:39:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 8.3 |
| 23407cd6-5106-3dbf-95c7-c4bacfa87c4d | -6.75354 | -55.14202 | 2026-10-08 16:39:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 0c619110-99d4-3b8e-9fcb-55d17e58a879 | -0.43714 | -51.73014 | 2026-10-08 16:39:00 | NOAA-20 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 4bb1b91a-3e64-3d38-9ac3-e22c0912a4b3 | -3.10467 | -53.96107 | 2026-10-08 16:39:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 17.8 |
| e4c2fb58-8f58-3bbb-8acd-d45c6e2c1f06 | -3.01616 | -43.34454 | 2026-10-08 16:39:00 | NOAA-20 | BELÁGUA | MARANHÃO | Brasil | 2101731 | 21 | 33 | nan | nan | nan | Cerrado | 8.0 |
| d622e44d-dce1-349c-b89c-0282c05d8791 | -2.44864 | -57.46126 | 2026-10-08 16:39:00 | NOAA-20 | URUCARÁ | AMAZONAS | Brasil | 1304302 | 13 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 746f23b5-76bd-3361-87b4-f4caf37c83a9 | -1.37029 | -55.92371 | 2026-10-08 16:39:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 27e27e9b-750e-38a9-a63e-6875191500b2 | -0.93487 | -48.00418 | 2026-10-08 16:39:00 | NOAA-20 | SÃO CAETANO DE ODIVELAS | PARÁ | Brasil | 1507102 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| f1f0f0b2-3afc-31e0-8e74-2a0cf390b9a2 | -1.3327 | -56.40509 | 2026-10-08 16:39:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 9.8 |
| 6ce65609-3df1-3895-a031-0ef80cc94cab | -3.33429 | -42.91634 | 2026-10-08 16:39:00 | NOAA-20 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 10.4 |
| 32d43835-d98c-3f3c-8463-4fdcab622381 | -2.09355 | -46.56643 | 2026-10-08 16:39:00 | NOAA-20 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| ce831043-e7c2-35d6-a39d-46b934a9805c | -3.06257 | -53.91832 | 2026-10-08 16:39:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 30.0 |
| 494672ae-9ed0-37d6-97b0-7e31d4b2eee9 | -4.90008 | -43.37303 | 2026-10-08 16:39:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 25.8 |
| bc1710f5-66c0-37aa-9c75-8b40647b434a | -2.16692 | -53.6658 | 2026-10-08 16:39:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 87f5e23e-8d93-34c5-907d-724456051df3 | -4.37625 | -55.32236 | 2026-10-08 16:39:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 16.8 |
| c5469eb6-c386-336d-adfc-9671ee0ae164 | -3.09168 | -53.93744 | 2026-10-08 16:39:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 62.8 |


[Clique aqui para ver as próximas entradas](README374.md)
