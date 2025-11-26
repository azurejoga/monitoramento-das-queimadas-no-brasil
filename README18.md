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

## Dados Diários - Página 18

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| f345f4e1-3407-34c6-ae01-fe6aad56336a | -3.98017 | -46.02311 | 2025-11-26 04:21:00 | NOAA-20 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 3725caf4-a41e-37e1-980f-5b3c81472d07 | -6.30675 | -43.78186 | 2025-11-26 04:21:00 | NOAA-20 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 2a03a699-0f0b-3168-b435-6760bc43c44b | -2.50235 | -47.83383 | 2025-11-26 04:21:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 8a0927c4-0f4b-36d8-aac3-96e418333728 | -4.7421 | -46.50061 | 2025-11-26 04:21:00 | NOAA-20 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a24454fc-c19e-3a81-9487-88b144602f32 | -3.31074 | -44.38419 | 2025-11-26 04:21:00 | NOAA-20 | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| ab585f75-554a-3e44-939e-e4d80a3f7862 | -2.47445 | -47.83879 | 2025-11-26 04:21:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 91bb8522-f07e-39bd-bcb8-3a55f37c337f | -4.70093 | -43.99366 | 2025-11-26 04:21:00 | NOAA-20 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 392a42d0-db02-3a5f-98b4-2e7cac131222 | -6.41914 | -49.92953 | 2025-11-26 04:21:00 | NOAA-20 | CANAÃ DOS CARAJÁS | PARÁ | Brasil | 1502152 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| f622712f-5019-343b-b2b9-2ac69feb2b87 | -3.13486 | -49.40551 | 2025-11-26 04:21:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| ccfca5ce-2f1b-313f-82ab-0670a26671da | -8.0507 | -43.10384 | 2025-11-26 04:21:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 95b4d47e-6e60-305c-a72b-40261ec010a5 | -3.90101 | -47.75373 | 2025-11-26 04:21:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 3946015d-1ed7-30f9-b6a8-2702f8f0fd4d | -4.37138 | -49.7724 | 2025-11-26 04:21:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| e50d96ce-3703-3e2d-91b1-d25481d6bb56 | -3.51479 | -43.69405 | 2025-11-26 04:21:00 | NOAA-20 | NINA RODRIGUES | MARANHÃO | Brasil | 2107209 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 24215d7a-7fcf-359c-9ba4-bc09e8fd53d9 | -4.08616 | -43.92867 | 2025-11-26 04:21:00 | NOAA-20 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c8540f5e-e90d-3d05-8ee8-da707f818fda | -4.53438 | -45.55991 | 2025-11-26 04:21:00 | NOAA-20 | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 1c42181c-4deb-3b6a-9312-2eeeedaa9681 | -4.1678 | -43.73287 | 2025-11-26 04:21:00 | NOAA-20 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 16.0 |
| f66f3836-0e5c-3102-8fd2-eedee6021759 | -3.39347 | -49.2263 | 2025-11-26 04:21:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| d5cf80fd-ad08-33e3-b84d-1ae126367219 | -6.59889 | -44.47675 | 2025-11-26 04:21:00 | NOAA-20 | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| b8fec8a6-aa96-39fa-a091-90cc56b1bfc2 | -5.2549 | -44.14473 | 2025-11-26 04:21:00 | NOAA-20 | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 35556671-6019-3b59-ae54-f7169c214b93 | -8.061 | -43.10543 | 2025-11-26 04:21:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| c2252bc7-ce1a-31b0-b803-a4234ba646ed | -8.06385 | -43.10971 | 2025-11-26 04:21:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| d824ce0c-926c-37f4-a61b-5fb962170df2 | -2.48801 | -47.82683 | 2025-11-26 04:21:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 2cdb59dd-3b5a-36bd-91f1-e2b74cf8d335 | -3.2327 | -51.18347 | 2025-11-26 04:21:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 67ac3348-c578-3473-ae4d-a7630a1c8802 | -4.94076 | -41.14874 | 2025-11-26 04:21:00 | NOAA-20 | PORANGA | CEARÁ | Brasil | 2311009 | 23 | 33 | nan | nan | nan | Caatinga | 1.1 |
| e08b7cf2-e46b-3058-8860-6be9bd713296 | -3.18351 | -46.59946 | 2025-11-26 04:21:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| be595aa3-30d6-36d6-9363-ac7440a55d02 | -8.05527 | -43.11991 | 2025-11-26 04:21:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 19.6 |
| c5b8dcde-53ac-3f99-8912-7bb93f30d6fe | -2.96291 | -49.53196 | 2025-11-26 04:21:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 15152313-4e28-3971-bcf6-90e99a8f0633 | -3.91135 | -47.75988 | 2025-11-26 04:21:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 6d8bb187-8fc8-3ee1-ad62-2247580c9632 | -2.93322 | -48.21824 | 2025-11-26 04:21:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4c9f0fab-e6d8-396f-8971-58542cc57726 | -4.6452 | -47.94744 | 2025-11-26 04:21:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c3bfadcd-3e52-3877-8649-fbff9594ca72 | -5.27967 | -43.63977 | 2025-11-26 04:21:00 | NOAA-20 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 6eb0c9aa-0ab4-340f-94bc-fc4938893a1a | -7.18142 | -44.98384 | 2025-11-26 04:21:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| c7510848-c645-3f3d-b4c0-a18ec8c1058a | -5.62145 | -43.88589 | 2025-11-26 04:21:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 2feba7af-364a-38ce-8ea1-7ca88e3d0f5a | -4.58879 | -45.70675 | 2025-11-26 04:21:00 | NOAA-20 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 8ebdedf2-26fd-3412-aefb-908ea2547430 | -3.32803 | -50.26426 | 2025-11-26 04:21:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 6dbdadb7-4bc6-357d-9278-96262b9b58b5 | -3.25837 | -51.17282 | 2025-11-26 04:21:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 59d9b237-0712-3752-838e-041500ed0002 | -2.8788 | -51.80513 | 2025-11-26 04:21:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 850978ef-f5e6-30f5-8fe8-5461480c8767 | -3.68076 | -43.56818 | 2025-11-26 04:21:00 | NOAA-20 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| e57fb078-a7d6-317e-a274-286a3e60221c | -4.82366 | -43.8181 | 2025-11-26 04:21:00 | NOAA-20 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d30df4a2-8a75-39d7-9c1e-df1663edc633 | -8.08222 | -41.08517 | 2025-11-26 04:21:00 | NOAA-20 | PAULISTANA | PIAUÍ | Brasil | 2207801 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| d6a8aed7-a134-3712-bd7d-7b5fb55774b6 | -4.14272 | -42.54996 | 2025-11-26 04:21:00 | NOAA-20 | BARRAS | PIAUÍ | Brasil | 2201200 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 207dcdc0-f943-3fd3-a815-1b3eb3fcfa68 | -5.34753 | -46.59476 | 2025-11-26 04:21:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 78b42c4a-3814-3964-9f76-2a788429a909 | -8.05642 | -43.11241 | 2025-11-26 04:21:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 36.8 |
| 03f7f751-44b1-3026-b8f2-91bd2f77175a | -5.49485 | -44.69092 | 2025-11-26 04:21:00 | NOAA-20 | SANTA FILOMENA DO MARANHÃO | MARANHÃO | Brasil | 2109759 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 1d667f09-c5ae-3b9e-a45c-9c63dd17c68e | -5.71589 | -39.49936 | 2025-11-26 04:21:00 | NOAA-20 | MOMBAÇA | CEARÁ | Brasil | 2308500 | 23 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 51881986-b494-3764-8640-3d58f747e259 | -6.30953 | -43.78589 | 2025-11-26 04:21:00 | NOAA-20 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 10.3 |
| 3bdf7096-c645-3f0f-92a0-1d6c1d11e6a7 | -5.49858 | -45.2879 | 2025-11-26 04:21:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b7c3a8d6-8454-3385-abac-0d62827c29f4 | -4.66814 | -48.87477 | 2025-11-26 04:21:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 23d180f9-afce-3836-b419-5871b16bf932 | -3.6769 | -43.57111 | 2025-11-26 04:21:00 | NOAA-20 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 6c5f20cd-8cd0-394f-ba59-c8f770e6507a | -8.05241 | -43.13861 | 2025-11-26 04:21:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 10.3 |
| 01aeca11-e305-3546-aef1-faa14fdfd769 | -6.60645 | -35.2279 | 2025-11-26 04:21:00 | NOAA-20 | JACARAÚ | PARAÍBA | Brasil | 2507309 | 25 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| c1770d2f-f966-3ee9-9a77-9147ad143242 | -4.71654 | -46.46185 | 2025-11-26 04:21:00 | NOAA-20 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b78c2056-ba58-3d56-8a21-3d9edf3ff27c | -3.02817 | -51.0339 | 2025-11-26 04:21:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ce54fdf2-67fb-3d70-ad36-bd23975c07e8 | -4.08456 | -48.73382 | 2025-11-26 04:21:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 475b8a2d-d72c-3ddf-b6f8-2591224ec9c4 | -4.1022 | -49.07121 | 2025-11-26 04:21:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 4be85e18-846f-3c73-b6cc-8798951e14e5 | -8.05471 | -43.10061 | 2025-11-26 04:21:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| fd6056c8-7530-3478-a79b-ffb6423a129c | -4.37447 | -47.26051 | 2025-11-26 04:21:00 | NOAA-20 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 1802b945-a489-3dbf-9887-33969cb3ec3b | -4.9683 | -50.8768 | 2025-11-26 04:21:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| c56d8bbe-a3aa-33b1-bec9-bbf3cc3adfc9 | -5.33181 | -43.56567 | 2025-11-26 04:21:00 | NOAA-20 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 8.9 |
| 28b0efa5-d327-3c4e-9519-671cf750f6fa | -2.92787 | -48.22713 | 2025-11-26 04:21:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 7295a44e-359e-37b9-8aad-36b270cca84a | -4.15233 | -43.72337 | 2025-11-26 04:21:00 | NOAA-20 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 7.0 |
| a07eec29-e124-3c6c-a01a-db6af006677e | -4.71997 | -46.46241 | 2025-11-26 04:21:00 | NOAA-20 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 5.3 |
| ccdf674a-5142-34a8-bc74-a29610f5bb8d | -8.04727 | -43.12634 | 2025-11-26 04:21:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 5.7 |
| 0bb91745-c1aa-3e9e-9140-f0552b4e6ff4 | -2.5487 | -45.39102 | 2025-11-26 04:21:00 | NOAA-20 | PRESIDENTE SARNEY | MARANHÃO | Brasil | 2109270 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 69766d5f-94c8-366a-b008-11e7ffcbe1f2 | -8.05756 | -43.1049 | 2025-11-26 04:21:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 38b13411-6eb6-3db9-b27a-235ead84c1eb | -2.62971 | -46.93323 | 2025-11-26 04:21:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| a6677142-6aa1-3e5a-9213-0d4a658fee5e | -3.94229 | -46.74603 | 2025-11-26 04:21:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| b9655bcc-b7db-36b0-8692-064615815659 | -2.88279 | -51.81143 | 2025-11-26 04:21:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 7d718ecc-f722-36e1-bd2a-3996e661ebe0 | -7.48097 | -42.75592 | 2025-11-26 04:21:00 | NOAA-20 | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 3d244c80-2961-34ea-b530-4497c597b574 | -6.6842 | -42.47534 | 2025-11-26 04:21:00 | NOAA-20 | ARRAIAL | PIAUÍ | Brasil | 2201002 | 22 | 33 | nan | nan | nan | Caatinga | 3.1 |
| 31bd348d-7089-3e4c-87ed-b3c9dcc216fc | -3.46342 | -49.91303 | 2025-11-26 04:21:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 7e8a7ea7-4157-3680-a8d5-fbd8589fa17d | -4.99671 | -40.78482 | 2025-11-26 04:21:00 | NOAA-20 | CRATEÚS | CEARÁ | Brasil | 2304103 | 23 | 33 | nan | nan | nan | Caatinga | 1.2 |
| deb1b2d3-2be8-3f9a-bc5f-3f1ddb7f871a | -2.81764 | -46.75836 | 2025-11-26 04:21:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0b0edc21-d33f-3095-8dca-57efa53ee6d1 | -2.70055 | -49.51561 | 2025-11-26 04:21:00 | NOAA-20 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 1dffda32-341e-3ac7-a1e7-9afe83dfbdcb | -3.24846 | -50.69304 | 2025-11-26 04:21:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 91dd87cb-6dc4-352d-a2a8-e6fbe91eac46 | -3.45279 | -50.54561 | 2025-11-26 04:21:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 4e991c35-7a17-3953-8191-6126940592f8 | -5.35097 | -46.59533 | 2025-11-26 04:21:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 97371c8b-1203-3c52-8537-cb6d440c24dc | -6.75615 | -44.21021 | 2025-11-26 04:21:00 | NOAA-20 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 7a396949-fe35-3f9e-8cd4-1d13201ff320 | -4.16503 | -43.72889 | 2025-11-26 04:21:00 | NOAA-20 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 18.0 |
| ff31bdc1-981f-3c6e-b143-95298113444f | -4.44593 | -48.75925 | 2025-11-26 04:21:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| fac42097-ad41-334d-988b-7b69cf88df35 | -6.79966 | -44.62572 | 2025-11-26 04:21:00 | NOAA-20 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| c9102561-2402-3336-9cf9-64a541e5dd22 | -8.0467 | -43.10707 | 2025-11-26 04:21:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| d508f7b6-2728-32bd-817a-90366732eb45 | -4.30854 | -45.37564 | 2025-11-26 04:21:00 | NOAA-20 | VITORINO FREIRE | MARANHÃO | Brasil | 2113009 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 5ca0caab-0d51-33a2-8b7a-2e3565fc3960 | -5.35165 | -44.88749 | 2025-11-26 04:21:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| d2bf08b4-fae4-3057-88c0-8a64091a23df | -4.18979 | -43.70092 | 2025-11-26 04:21:00 | NOAA-20 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 3ae05f0a-6e2a-38e4-a776-4911e3eb5992 | -4.586 | -45.70267 | 2025-11-26 04:21:00 | NOAA-20 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 7b618932-0e1c-33d1-b1d0-c0117a21b40e | -6.59293 | -44.31958 | 2025-11-26 04:21:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| cf9b3444-0191-3727-bc35-af15ab5a780e | -4.5589 | -49.69481 | 2025-11-26 04:21:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 5590584c-b6cb-323f-bfc9-e56d753fa021 | -3.9802 | -49.28781 | 2025-11-26 04:21:00 | NOAA-20 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 91bef72e-eb26-3090-ad81-6a71ca0a4c01 | -3.22496 | -50.56871 | 2025-11-26 04:21:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 4a8d3109-7241-3098-92fc-203305687881 | -4.58542 | -45.70624 | 2025-11-26 04:21:00 | NOAA-20 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 22a713c1-46a8-3316-b705-c4df1c1a72a8 | -3.42145 | -46.96809 | 2025-11-26 04:21:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ff654ea0-4283-36dd-8fcd-0cd1e920a9f4 | -3.75353 | -46.1669 | 2025-11-26 04:21:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 93b7d355-342e-3e87-88b8-b56ee03a99a6 | -3.31569 | -50.4502 | 2025-11-26 04:21:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 055313cc-7a71-3d9d-82b7-5b91862e7672 | -3.14331 | -40.1811 | 2025-11-26 04:21:00 | NOAA-20 | MARCO | CEARÁ | Brasil | 2307809 | 23 | 33 | nan | nan | nan | Caatinga | 1.6 |
| f5b683e7-8721-3d54-9cea-1c687cbd3160 | -6.56792 | -47.89938 | 2025-11-26 04:21:00 | NOAA-20 | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 8279dcb4-7803-311f-bd0c-1333fbb2108d | -4.17274 | -43.72301 | 2025-11-26 04:21:00 | NOAA-20 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| b4454e24-6a8f-3a68-aab3-d211d8fc433f | -4.45511 | -44.3041 | 2025-11-26 04:21:00 | NOAA-20 | PERITORÓ | MARANHÃO | Brasil | 2108454 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| a1db5685-af21-3e95-b342-49dc9b34b752 | -4.14716 | -43.64819 | 2025-11-26 04:21:00 | NOAA-20 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 5.6 |
| d163947e-3252-3f24-8e79-3377aa6182d8 | -6.57445 | -47.90464 | 2025-11-26 04:21:00 | NOAA-20 | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |


[Clique aqui para ver as próximas entradas](README19.md)
