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

## Dados Diários - Página 13

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 80711edb-5eef-316b-8aca-5a7bf5eb7be5 | -4.08464 | -46.60585 | 2024-12-17 04:21:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| b1431ada-9ae6-3e2f-b25c-2c2d6ca8f630 | -3.8737 | -47.03387 | 2024-12-17 04:21:00 | NOAA-21 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 2b1b508e-49af-31d8-ab4e-9dc032d64fdb | -3.95725 | -47.03395 | 2024-12-17 04:21:00 | NOAA-21 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 78d50e91-b91c-3947-afaa-57722e2e3968 | -2.7805 | -48.57859 | 2024-12-17 04:21:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 68300c1b-c129-3b43-b2b9-8fd422df75b0 | -5.08254 | -43.9057 | 2024-12-17 04:21:00 | NOAA-21 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 50576304-2091-37cd-a014-d3cd1089406f | -3.77026 | -47.16151 | 2024-12-17 04:21:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 0d163161-92bc-3be4-983a-b2a50aeb7465 | -5.08918 | -43.90672 | 2024-12-17 04:21:00 | NOAA-21 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 9.9 |
| ea4922d9-6d3d-3723-b220-130e21ebb9e7 | -4.383 | -46.54351 | 2024-12-17 04:21:00 | NOAA-21 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ca502e66-f7a5-3c58-bfea-291cab565770 | -4.96514 | -43.71999 | 2024-12-17 04:21:00 | NOAA-21 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 0125362f-3d13-36ab-a095-e6d5e64c70c0 | -4.24848 | -45.99492 | 2024-12-17 04:21:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| d02c6442-128f-3b84-9d42-0883f23e83dc | -3.29909 | -53.36701 | 2024-12-17 04:21:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 14.4 |
| 2e6ed7e8-a031-3888-b878-1a062b931156 | -3.76838 | -47.17353 | 2024-12-17 04:21:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| fcf8d8c0-c4b6-347c-8c12-3c55abc13980 | -5.80683 | -43.04595 | 2024-12-17 04:21:00 | NOAA-21 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 573cbfd4-8117-3213-8244-abe7a3a927e9 | -4.10258 | -46.67088 | 2024-12-17 04:21:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| bc451e83-e3c7-3e60-9f43-967140932177 | -5.59197 | -43.28783 | 2024-12-17 04:21:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 73d658ed-5810-3a43-b45e-e870ee090755 | -4.36889 | -44.57819 | 2024-12-17 04:21:00 | NOAA-21 | SÃO LUÍS GONZAGA DO MARANHÃO | MARANHÃO | Brasil | 2111409 | 21 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 8bc959bf-f2fc-30ae-b1ca-b30b95bd1cc9 | -4.62232 | -46.31827 | 2024-12-17 04:21:00 | NOAA-21 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 734db37e-b41a-3029-967a-31087022296d | -4.02737 | -46.86378 | 2024-12-17 04:21:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| df066aef-492f-3947-b58b-7039c36ca735 | -3.50257 | -53.9579 | 2024-12-17 04:21:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 10372928-6da3-3617-971b-4bcf647c253e | -3.4361 | -53.98085 | 2024-12-17 04:21:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 3c2b36dc-d489-3000-82d7-a04790d0a4ea | -3.18814 | -46.68977 | 2024-12-17 04:21:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 91282dc2-1808-3512-908d-5a7a4249591d | -2.77537 | -48.57974 | 2024-12-17 04:21:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 24db61ff-14f2-3bc1-89fe-08525bb3177c | -4.96181 | -43.71948 | 2024-12-17 04:21:00 | NOAA-21 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 0db4f9c6-009a-3da3-9535-ad47fb53bfa0 | -4.12111 | -43.57102 | 2024-12-17 04:21:00 | NOAA-21 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f2f5f76f-a782-338f-9091-6811bda73f86 | -5.53109 | -39.18145 | 2024-12-17 04:21:00 | NOAA-21 | MILHÃ | CEARÁ | Brasil | 2308351 | 23 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 0b260f5d-178c-3628-934e-f0a3b7d89426 | -0.79853 | -52.34306 | 2024-12-17 04:21:00 | NOAA-21 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7b2751a3-738c-351d-98d0-f610567fe7c9 | -5.0925 | -43.90723 | 2024-12-17 04:21:00 | NOAA-21 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 32.1 |
| 17f843a4-fdfe-302b-98dd-c655b72e0243 | -5.36626 | -44.04959 | 2024-12-17 04:21:00 | NOAA-21 | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| ec0f9c90-f658-3665-85e0-7842f7c5904c | -4.28438 | -46.89511 | 2024-12-17 04:21:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 6476089b-b0fd-316b-bd32-ebc41cd13a56 | -5.03667 | -46.47301 | 2024-12-17 04:21:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b50be50c-d653-31b0-acb9-8fdd1417e07a | -5.08757 | -43.91714 | 2024-12-17 04:21:00 | NOAA-21 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 1f44c2ed-59e5-3ac1-8072-bdedb395da80 | -3.79834 | -46.84549 | 2024-12-17 04:21:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2d79c61a-41e9-397a-a239-4fdd47c63a88 | -3.87432 | -47.02994 | 2024-12-17 04:21:00 | NOAA-21 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 99c18337-14f1-34aa-a4be-144a579643c4 | -3.96493 | -47.03109 | 2024-12-17 04:21:00 | NOAA-21 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 3.8 |
| da359588-3537-338a-b333-54c926789e77 | -4.47847 | -39.34436 | 2024-12-17 04:21:00 | NOAA-21 | CANINDÉ | CEARÁ | Brasil | 2302800 | 23 | 33 | nan | nan | nan | Caatinga | 1.3 |
| f5d7c62c-afe2-3bd6-bb1a-1cc21e9a6743 | -4.03781 | -47.02991 | 2024-12-17 04:21:00 | NOAA-21 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 9b369155-2bb3-3f42-8538-0ceb6a57054f | -4.03366 | -47.03332 | 2024-12-17 04:21:00 | NOAA-21 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 15f13421-b87d-361d-a4ee-77f4c7a09557 | -3.98064 | -48.39023 | 2024-12-17 04:21:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 264ac08f-de0a-38d4-929a-5c153d00319e | -2.49297 | -49.04839 | 2024-12-17 04:21:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a8bd19d5-c42c-3564-b066-97fa89309904 | -4.39855 | -41.43097 | 2024-12-17 04:21:00 | NOAA-21 | PEDRO II | PIAUÍ | Brasil | 2207900 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| f3d5f3b9-a36d-3dad-bd91-f2d147181ebf | -0.75554 | -47.75585 | 2024-12-17 04:21:00 | NOAA-21 | MARAPANIM | PARÁ | Brasil | 1504406 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 369f2f71-9941-35b3-b390-db9d50c1c551 | -3.05006 | -47.97066 | 2024-12-17 04:21:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 6a7dbb7a-2b6c-39fc-9c24-ebdc2eb44f49 | -2.65966 | -45.5633 | 2024-12-17 04:21:00 | NOAA-21 | SANTA HELENA | MARANHÃO | Brasil | 2109809 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7f26b618-8500-3756-b48b-d0eed8de51dc | -3.9245 | -46.92373 | 2024-12-17 04:21:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c9c3f079-04ae-30ab-8541-62b44ae88f8c | -1.27557 | -53.0293 | 2024-12-17 04:21:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c5482d85-c962-3dde-a6b0-c6fe4f267e67 | -1.64193 | -45.91688 | 2024-12-17 04:21:00 | NOAA-21 | AMAPÁ DO MARANHÃO | MARANHÃO | Brasil | 2100550 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| bb2155b2-a40b-3ee8-8b73-c2c5a0c75f0a | -4.04863 | -47.00748 | 2024-12-17 04:21:00 | NOAA-21 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 2.5 |
| b789790f-e6ef-38f4-b0be-99d50f99967b | -3.97638 | -44.36864 | 2024-12-17 04:21:00 | NOAA-21 | SÃO MATEUS DO MARANHÃO | MARANHÃO | Brasil | 2111508 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| a7966deb-1f42-3ec8-8672-8f0034ebb216 | -5.96579 | -41.5917 | 2024-12-17 04:21:00 | NOAA-21 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 16d42255-aadb-3419-bda8-5947e7fdbeca | -1.60222 | -45.41027 | 2024-12-17 04:21:00 | NOAA-21 | TURIAÇU | MARANHÃO | Brasil | 2112407 | 21 | 33 | nan | nan | nan | Amazônia | 2.5 |
| b69d907c-9fa9-3427-b240-64fed83980c4 | -3.99374 | -44.17069 | 2024-12-17 04:21:00 | NOAA-21 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 223a490d-c34a-3a2e-8e05-a42d51052548 | -1.51971 | -46.04819 | 2024-12-17 04:21:00 | NOAA-21 | CARUTAPERA | MARANHÃO | Brasil | 2102903 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2346bfa5-cd10-3400-9328-dc49f9c97ece | -4.96568 | -43.7165 | 2024-12-17 04:21:00 | NOAA-21 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 2d368d13-0ecb-31e1-a02d-c505e48ebc9b | -4.08059 | -46.60903 | 2024-12-17 04:21:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| fc84817a-14fb-34a9-a341-92d3e8893ccf | -4.62507 | -45.3314 | 2024-12-17 04:21:00 | NOAA-21 | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 20d2f82a-b98d-329e-b598-5b895582f344 | -2.60005 | -45.74291 | 2024-12-17 04:21:00 | NOAA-21 | SANTA LUZIA DO PARUÁ | MARANHÃO | Brasil | 2110039 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d5f4b99d-fb30-3366-9749-e51ed616ffa8 | -2.01516 | -46.61304 | 2024-12-17 04:21:00 | NOAA-21 | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 979360c5-22c5-3b70-834f-dc9e88fe27b8 | -4.0789 | -46.72984 | 2024-12-17 04:21:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4eda0a02-e307-375c-8e6d-e2d00b249381 | -3.855 | -46.50877 | 2024-12-17 04:21:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3ea4958d-644d-3288-8735-d83069233262 | -5.17503 | -39.44695 | 2024-12-17 04:21:00 | NOAA-21 | QUIXERAMOBIM | CEARÁ | Brasil | 2311405 | 23 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 4dc89493-b86a-390a-9d61-96fa4f5895b7 | -3.99507 | -46.95471 | 2024-12-17 04:21:00 | NOAA-21 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 35710b85-1ae0-3ade-bf68-9d669a6e6f52 | -4.07939 | -46.61648 | 2024-12-17 04:21:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 7d2ccddf-8eec-3d39-b6c2-49a67ad2af7a | -4.67433 | -44.03728 | 2024-12-17 04:21:00 | NOAA-21 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| cdfc01df-a62d-3d5a-b37d-cab2b5c9f01e | -5.24904 | -40.87949 | 2024-12-17 04:21:00 | NOAA-21 | CRATEÚS | CEARÁ | Brasil | 2304103 | 23 | 33 | nan | nan | nan | Caatinga | 1.2 |
| d79dda2e-26ac-35ae-8331-93fd02fed0dd | -3.2976 | -53.36535 | 2024-12-17 04:21:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 9.8 |
| 24b99e76-e007-3efa-ac7b-d6fdb615cfb1 | -3.92386 | -46.92765 | 2024-12-17 04:21:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c9e266ee-d468-364d-9c49-5c086c82cd62 | -5.22774 | -46.06349 | 2024-12-17 04:21:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 0199180a-2cbb-3a46-9c58-2f47d3e5e499 | -1.65232 | -45.89552 | 2024-12-17 04:21:00 | NOAA-21 | AMAPÁ DO MARANHÃO | MARANHÃO | Brasil | 2100550 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 89d33fab-6273-324d-850b-8ae6f990a5f3 | -3.29392 | -43.11686 | 2024-12-17 04:21:00 | NOAA-21 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 72c061df-cddb-3a89-a6a9-21d8edb08fd7 | -4.01546 | -46.89384 | 2024-12-17 04:21:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| fb0c758d-900a-3432-9614-45c375cbf704 | -1.30086 | -52.83685 | 2024-12-17 04:21:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 58fd96b4-d1a0-3780-9360-b1241ba3fe87 | -4.58297 | -47.09198 | 2024-12-17 04:21:00 | NOAA-21 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 44dc18fe-e1cf-37c8-ad64-3745013ca12c | -5.98696 | -41.5737 | 2024-12-17 04:21:00 | NOAA-21 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 6f82ac75-6822-3c13-bc1a-6f1128f3e727 | -5.31121 | -46.4931 | 2024-12-17 04:21:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f395cad3-0f15-308e-a9b2-d5b0904f8455 | -3.32606 | -46.18946 | 2024-12-17 04:21:00 | NOAA-21 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d69ee9a0-8236-3710-9bb7-dc036c7ed988 | -4.12037 | -46.18354 | 2024-12-17 04:21:00 | NOAA-21 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 58638f7e-2f70-32c1-9b2e-9c4631cc791a | -3.49889 | -53.9459 | 2024-12-17 04:21:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a31e3c44-a749-36c0-91f7-5190cb1a46ee | -4.02676 | -46.86766 | 2024-12-17 04:21:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d615398a-9ac9-3b16-9d9a-f8b25e5b744d | -3.12376 | -52.69997 | 2024-12-17 04:21:00 | NOAA-21 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 56340efa-ac64-3149-99cc-cdff6d72d578 | -4.90553 | -42.0779 | 2024-12-17 04:21:00 | NOAA-21 | CAMPO MAIOR | PIAUÍ | Brasil | 2202208 | 22 | 33 | nan | nan | nan | Caatinga | 4.5 |
| 7e8966da-9a9a-3347-b8cf-7d44d39c5d40 | -4.12165 | -43.56753 | 2024-12-17 04:21:00 | NOAA-21 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e4fb017f-f888-3705-9f49-f52932a7520c | -4.03014 | -47.03275 | 2024-12-17 04:21:00 | NOAA-21 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 138aefcc-d1da-33e8-8680-208ef9834cc0 | -3.18403 | -46.69312 | 2024-12-17 04:21:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b90a124d-f72e-3f83-94eb-8c2f63c46a7b | -4.05702 | -46.67533 | 2024-12-17 04:21:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9611f7ec-46d6-37d1-bc8d-a9f2f292c992 | -2.87648 | -45.24696 | 2024-12-17 04:21:00 | NOAA-21 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a04c9695-042f-36c4-90f5-f6168db066c9 | -5.09196 | -43.9107 | 2024-12-17 04:21:00 | NOAA-21 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 18.2 |
| 725c75c5-1056-34a2-862d-f9bf7840a57f | -4.40053 | -44.87663 | 2024-12-17 04:21:00 | NOAA-21 | LAGO DO JUNCO | MARANHÃO | Brasil | 2105807 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 9c8df61b-33d0-3a29-805d-c3abb97cb526 | -4.97099 | -44.96959 | 2024-12-17 04:21:00 | NOAA-21 | ESPERANTINÓPOLIS | MARANHÃO | Brasil | 2104008 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 57f87385-6853-36e7-82c4-8ef00fa580f4 | -3.84503 | -45.85798 | 2024-12-17 04:21:00 | NOAA-21 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| e6d58145-781b-3861-97c9-315bfae2410a | -5.13632 | -46.18205 | 2024-12-17 04:21:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 3.8 |
| f226f4da-e138-319e-bf50-178aa1d010ba | -5.10138 | -43.9157 | 2024-12-17 04:21:00 | NOAA-21 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| df4d6952-7349-3223-9d51-742865920f4d | -3.77079 | -43.24107 | 2024-12-17 04:21:00 | NOAA-21 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| c1f1ed36-be67-312d-8531-4e7de925ef64 | -3.26421 | -45.37613 | 2024-12-17 04:21:00 | NOAA-21 | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| fd94eeb1-498b-3368-a4b7-289fa847fd63 | -4.40194 | -40.88996 | 2024-12-17 04:21:00 | NOAA-21 | CROATÁ | CEARÁ | Brasil | 2304236 | 23 | 33 | nan | nan | nan | Caatinga | 1.0 |
| f3523928-3865-3c0c-ade1-4905a7456e96 | -4.02299 | -46.82341 | 2024-12-17 04:21:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 63a6af58-8056-3456-8682-4af62bfb112a | -5.09967 | -43.90476 | 2024-12-17 04:21:00 | NOAA-21 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 23.1 |
| 98fe113f-45e3-3300-bad6-4978cf7287b0 | -4.22291 | -43.98814 | 2024-12-17 04:21:00 | NOAA-21 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 5.0 |
| cd51ea5a-f7c9-37a1-99d5-cfc26cf9ee28 | -5.08478 | -43.91316 | 2024-12-17 04:21:00 | NOAA-21 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 686d7d8c-94cd-3afe-8544-e665c5cfb2ae | -1.46327 | -53.48336 | 2024-12-17 04:21:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6d21a5f8-5282-3957-9d19-651d0c8383ed | -4.68095 | -44.0383 | 2024-12-17 04:21:00 | NOAA-21 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |


[Clique aqui para ver as próximas entradas](README14.md)
