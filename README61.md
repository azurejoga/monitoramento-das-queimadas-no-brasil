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

## Dados Diários - Página 61

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 6b7718b3-faa7-304d-95ac-2863533cf64c | -2.42095 | -53.89797 | 2024-10-23 05:40:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| c73afbe3-ea8a-35fc-b47c-16403695fb90 | -2.42032 | -53.89729 | 2024-10-23 05:40:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 4046e76b-1014-39df-a885-94dc495659a4 | -3.89061 | -54.14366 | 2024-10-23 05:40:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 259a6fa6-c942-39b1-ae95-866811f65d71 | -3.89001 | -54.14784 | 2024-10-23 05:40:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1c57c5dd-c7d3-3d05-8fb3-8f7523d29dc9 | -3.88473 | -54.14276 | 2024-10-23 05:40:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 11c10542-47a4-3143-8d94-96937ed5299c | -3.88413 | -54.14695 | 2024-10-23 05:40:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e5878a0e-0035-301f-ba27-8a9a0d58b615 | -3.6651 | -54.43134 | 2024-10-23 05:40:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7ea55700-9964-39bb-b534-96c19adab771 | -3.65995 | -54.4263 | 2024-10-23 05:40:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b3f1dceb-1337-3d14-af6c-7b531bebd250 | -3.65124 | -54.79924 | 2024-10-23 05:40:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ce5e5a49-fc91-3b33-9d4d-c00af5bae862 | -3.64611 | -54.79515 | 2024-10-23 05:40:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 5652d76d-2acf-3720-ac2f-01838cc332a4 | -3.64558 | -54.79869 | 2024-10-23 05:40:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c2d4f266-ed87-3a60-a54a-bd7aa5ef8323 | -2.21329 | -55.05494 | 2024-10-23 05:40:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| ac626da0-e41a-3a14-89d6-e449369dcf89 | -2.20841 | -55.0507 | 2024-10-23 05:40:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 8.2 |
| 78ce33d1-2742-316e-aa85-19c9fb66463f | -2.20788 | -55.05414 | 2024-10-23 05:40:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 8.2 |
| 8c67c2c1-a61a-33cb-9563-c522c93c4bc3 | -1.99544 | -56.51686 | 2024-10-23 05:40:00 | NOAA-20 | TERRA SANTA | PARÁ | Brasil | 1507979 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 74e0e03e-3a2e-3fc6-89fe-5afc0152f780 | -1.91917 | -55.67052 | 2024-10-23 05:40:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 2259cac2-c145-3860-9116-560aef39e9ac | -1.91616 | -55.66839 | 2024-10-23 05:40:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| a558f1f3-eb06-3a7e-a655-abaaaff56631 | -1.9157 | -55.67149 | 2024-10-23 05:40:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| c327726b-06d8-351f-aad9-c66487211723 | -1.914 | -55.66978 | 2024-10-23 05:40:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 95909871-da8c-3970-a9bf-a3d550886c8d | -2.10208 | -56.58961 | 2024-10-23 05:40:00 | NOAA-20 | TERRA SANTA | PARÁ | Brasil | 1507979 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 573891d4-edd0-3806-ad28-8786da3d7757 | -6.50069 | -60.02115 | 2024-10-23 05:40:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 829e86b7-e637-3dc4-809d-161e2d60c7a9 | -6.50015 | -60.0248 | 2024-10-23 05:40:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 284c2bb9-c888-39d3-8601-03ab447cafda | -1.80026 | -59.93063 | 2024-10-23 05:40:00 | NOAA-20 | PRESIDENTE FIGUEIREDO | AMAZONAS | Brasil | 1303536 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a7d312c9-0d0e-32f0-aa39-d4b0af6d3604 | -2.98146 | -60.9819 | 2024-10-23 05:40:00 | NOAA-20 | IRANDUBA | AMAZONAS | Brasil | 1301852 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 4dbcc281-b53b-36f3-ad44-7f0f7f945777 | -7.82386 | -61.69105 | 2024-10-23 05:40:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3f2a132c-cb7a-32b3-bba8-bfac7a7147f3 | -7.82321 | -61.69559 | 2024-10-23 05:40:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ebab0530-b035-3499-ba36-b28bb2620b3d | -7.82309 | -61.6932 | 2024-10-23 05:40:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| eb808f4a-8dcd-3f8d-8b1d-b86cf551fd72 | -7.12284 | -63.02065 | 2024-10-23 05:40:00 | NOAA-20 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f377000c-159a-3edb-b585-3cf8c7054386 | -7.11935 | -63.02012 | 2024-10-23 05:40:00 | NOAA-20 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4a4c5a72-a2a2-351a-adf5-3f773897f674 | -6.83487 | -63.07722 | 2024-10-23 05:40:00 | NOAA-20 | TAPAUÁ | AMAZONAS | Brasil | 1304104 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| fab29423-ee32-3927-b917-1b4f14a88947 | -6.8314 | -63.07669 | 2024-10-23 05:40:00 | NOAA-20 | TAPAUÁ | AMAZONAS | Brasil | 1304104 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| a1cf060b-af45-3c07-807a-6bcdc7a2efe5 | -6.80583 | -63.15107 | 2024-10-23 05:40:00 | NOAA-20 | TAPAUÁ | AMAZONAS | Brasil | 1304104 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 450f1e3d-1ee4-3f4b-91b4-5c562f3f0097 | -7.88299 | -63.7793 | 2024-10-23 05:40:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 35f898f8-45b6-3877-b1d6-bcd47237a277 | -7.87958 | -63.77876 | 2024-10-23 05:40:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 37856a19-7f2a-3052-9a9e-71a606e34e7d | -2.79298 | -51.36504 | 2024-10-23 05:42:00 | AQUA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 3491ef2e-128a-3ca8-9933-caba354601b8 | -2.79159 | -49.57625 | 2024-10-23 05:42:00 | AQUA_M-M | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 2eae7f8c-81b8-37c4-9212-df4fca953c33 | -2.79023 | -49.58543 | 2024-10-23 05:42:00 | AQUA_M-M | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 26.5 |
| 6521965f-07bb-3e18-b06a-86d959f28eb1 | -2.74769 | -54.02576 | 2024-10-23 05:42:00 | AQUA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 9.5 |
| d0d20e46-60ca-338a-b14b-168b151e34ec | -2.74594 | -54.03708 | 2024-10-23 05:42:00 | AQUA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 42574c63-66a9-3f9f-9108-a758d74fbaa9 | -2.6834 | -49.31158 | 2024-10-23 05:42:00 | AQUA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 11.7 |
| 0d918ab8-6a10-36bf-ab6d-a5a39a115e01 | -2.68201 | -49.32092 | 2024-10-23 05:42:00 | AQUA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 13.0 |
| 8f897f2b-871a-3521-8b80-c3120f8d42a1 | -2.65391 | -49.25946 | 2024-10-23 05:42:00 | AQUA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| f73d765a-216d-31fa-9414-16570a445432 | -2.62155 | -49.98041 | 2024-10-23 05:42:00 | AQUA_M-M | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 899e38f1-4dd6-3d4f-8852-3d39cd289b37 | -2.60193 | -51.77186 | 2024-10-23 05:42:00 | AQUA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 34f510b5-dfc7-3ef5-9603-157893759b8e | -2.58862 | -49.82288 | 2024-10-23 05:42:00 | AQUA_M-M | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 34b28e51-0022-3d45-bfdc-2bf1b724598b | -2.57566 | -54.01096 | 2024-10-23 05:42:00 | AQUA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 15.5 |
| 322e2cbe-4524-325f-80f1-876a18ee168a | -2.57419 | -49.24133 | 2024-10-23 05:42:00 | AQUA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 7.3 |
| 9bcac139-d5af-3292-9fb0-9f61472d20a2 | -2.50984 | -54.10211 | 2024-10-23 05:42:00 | AQUA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 8.6 |
| 3f9ab314-4d04-31e0-ac93-cc4085d901a8 | -2.46124 | -51.96829 | 2024-10-23 05:42:00 | AQUA_M-M | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 8.9 |
| 06041cb5-2ac9-33b3-b8ec-ad6d378ed0d9 | -2.40768 | -50.48042 | 2024-10-23 05:42:00 | AQUA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| dec528cf-d61b-3079-92ca-648eeccdbb55 | -2.40052 | -50.4074 | 2024-10-23 05:42:00 | AQUA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| de778042-b5ea-3fc4-997f-b22630132fe9 | -2.2113 | -55.03755 | 2024-10-23 05:42:00 | AQUA_M-M | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 39f1901c-8c63-326b-88a5-7e9b15590683 | -2.20597 | -55.0449 | 2024-10-23 05:42:00 | AQUA_M-M | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 24.7 |
| 898a828f-8cbd-3883-8b13-70d7fef29473 | -2.13495 | -47.91048 | 2024-10-23 05:42:00 | AQUA_M-M | SÃO DOMINGOS DO CAPIM | PARÁ | Brasil | 1507201 | 15 | 33 | nan | nan | nan | Amazônia | 24.2 |
| 9ba940a0-fba6-332e-9618-5e80b12ad052 | -5.57499 | -43.23629 | 2024-10-23 05:42:00 | AQUA_M-M | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 29.9 |
| be9d83d4-d506-369c-bb49-9ae7e2e4428b | -5.57476 | -43.23071 | 2024-10-23 05:42:00 | AQUA_M-M | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 18.9 |
| d6427008-90ca-3bae-bb3b-7630b81ef7c7 | -5.57137 | -43.26403 | 2024-10-23 05:42:00 | AQUA_M-M | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 30.2 |
| 9d7a333a-79d1-3ac5-8dc8-00f1aa2e275a | -5.57095 | -43.25829 | 2024-10-23 05:42:00 | AQUA_M-M | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 41.2 |
| e92096bb-0435-36cb-b2c8-4c261cc5e4c5 | -2.13336 | -47.92124 | 2024-10-23 05:42:00 | AQUA_M-M | SÃO DOMINGOS DO CAPIM | PARÁ | Brasil | 1507201 | 15 | 33 | nan | nan | nan | Amazônia | 14.7 |
| 2c57c22d-0629-3af7-a743-c7df535eda9a | 0.97883 | -51.1468 | 2024-10-23 05:42:00 | AQUA_M-M | FERREIRA GOMES | AMAPÁ | Brasil | 1600238 | 16 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 1cce8bbb-5515-3dd7-82fd-fb01b902c2a7 | 0.47725 | -50.75001 | 2024-10-23 05:42:00 | AQUA_M-M | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 0b7fc533-ed1f-38c9-8d28-42eb404d24ef | -7.41434 | -46.61177 | 2024-10-23 05:42:00 | AQUA_M-M | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 12.7 |
| ef9883f6-e356-39ce-a0d9-79ab46a6c637 | -6.24371 | -44.13488 | 2024-10-23 05:42:00 | AQUA_M-M | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 23.6 |
| 2da70396-860a-32a8-9bef-ac85f2599915 | -6.05918 | -44.61538 | 2024-10-23 05:42:00 | AQUA_M-M | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 15.1 |
| 00d0f0bd-8158-3af9-8b6b-e9230b3335e8 | -5.75146 | -50.21684 | 2024-10-23 05:42:00 | AQUA_M-M | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 7.4 |
| 187d73dc-3bb1-3b97-821d-a5bf490e032d | -5.7501 | -50.22607 | 2024-10-23 05:42:00 | AQUA_M-M | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 203ffa24-1d3f-3ea7-b8e8-fe6a9f365e47 | -5.57952 | -44.88385 | 2024-10-23 05:42:00 | AQUA_M-M | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 21.4 |
| 2922db78-0190-3455-933d-2c2823c474cc | -4.75484 | -46.11192 | 2024-10-23 05:42:00 | AQUA_M-M | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 10.3 |
| 32df5b41-73b0-39e5-8093-ab1681e49376 | -4.75471 | -46.60924 | 2024-10-23 05:42:00 | AQUA_M-M | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 13.0 |
| 262765e6-1bda-3de0-8aa9-888d7b17e59a | -4.75274 | -46.62345 | 2024-10-23 05:42:00 | AQUA_M-M | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 16.1 |
| 6c528cbc-b6ad-3011-8d2c-762b8988e31d | -4.75191 | -46.61798 | 2024-10-23 05:42:00 | AQUA_M-M | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 32.6 |
| f550f7d2-2d2a-3f19-83c7-d67ecdeef02e | -4.73561 | -46.66543 | 2024-10-23 05:42:00 | AQUA_M-M | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 8.7 |
| 3554abf5-c727-3ff3-8c66-73af05b09c58 | -4.71874 | -45.71687 | 2024-10-23 05:42:00 | AQUA_M-M | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 17.7 |
| 0666f5cb-78b2-3c3a-a8e2-c6126e84ec47 | -4.71637 | -45.73388 | 2024-10-23 05:42:00 | AQUA_M-M | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 38.5 |
| b62748d9-9d2d-348c-a48d-2a87557730b5 | -4.60441 | -50.91936 | 2024-10-23 05:42:00 | AQUA_M-M | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 1c93596c-9031-3f45-a415-f26912e2ebb9 | -4.59851 | -47.51848 | 2024-10-23 05:42:00 | AQUA_M-M | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 8.0 |
| 1ddbdd6b-8c95-37b6-8a47-25cc8b22a607 | -4.5967 | -47.53091 | 2024-10-23 05:42:00 | AQUA_M-M | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 7.9 |
| 1964f766-ad97-3fbb-b715-20752e93bd29 | -4.38139 | -49.74976 | 2024-10-23 05:42:00 | AQUA_M-M | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 9.5 |
| e427aea4-6e28-3de0-be71-de3214a6446c | -4.36738 | -48.47115 | 2024-10-23 05:42:00 | AQUA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 13.0 |
| b56a46d7-2e8a-3a9d-aa46-db567f8e7b0e | -4.34031 | -47.59468 | 2024-10-23 05:42:00 | AQUA_M-M | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 9.2 |
| d388bc44-3ef3-3dd0-8439-26f61b512f73 | -4.33363 | -47.58723 | 2024-10-23 05:42:00 | AQUA_M-M | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 1ce7e6eb-7f89-34cc-8221-f38ca2df99c2 | -4.33184 | -47.59936 | 2024-10-23 05:42:00 | AQUA_M-M | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 9.0 |
| 058a8dd3-5093-30d5-a4e1-5c436c2f17a0 | -4.30611 | -46.68977 | 2024-10-23 05:42:00 | AQUA_M-M | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 11.9 |
| edb8f006-b69e-3a4d-ae49-215ef8fa6844 | -4.17315 | -47.97687 | 2024-10-23 05:42:00 | AQUA_M-M | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 51.6 |
| 845be1e3-032e-3521-8234-cc7ddf24f9f8 | -4.17148 | -47.98819 | 2024-10-23 05:42:00 | AQUA_M-M | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 75.9 |
| 75921865-d9e7-33f4-8cc9-f57dd0f098be | -4.13252 | -45.57498 | 2024-10-23 05:42:00 | AQUA_M-M | ALTAMIRA DO MARANHÃO | MARANHÃO | Brasil | 2100402 | 21 | 33 | nan | nan | nan | Amazônia | 23.0 |
| 369f3aec-ff2e-3fe8-803e-a8cc7ee6b1fa | -4.1301 | -45.59185 | 2024-10-23 05:42:00 | AQUA_M-M | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 39.5 |
| ee040136-1a48-3bc5-93e6-1f33cfbbc4b3 | -4.11813 | -45.59021 | 2024-10-23 05:42:00 | AQUA_M-M | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 32.8 |
| 7d32785a-a85b-3af2-b3d9-b234ff1d7402 | -4.04313 | -48.10043 | 2024-10-23 05:42:00 | AQUA_M-M | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 15.4 |
| 202375ca-0272-30be-822b-13d649c20c80 | -4.04149 | -48.1116 | 2024-10-23 05:42:00 | AQUA_M-M | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 9.0 |
| 369af9a7-b553-3f27-8944-01d974c2d774 | -4.0346 | -47.95011 | 2024-10-23 05:42:00 | AQUA_M-M | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| f1b77ab7-6c83-3054-8f9f-81fbb25f12fa | -3.97181 | -49.01445 | 2024-10-23 05:42:00 | AQUA_M-M | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 908a4a6b-ddbe-39ee-a4c8-9c7011e7b07d | -3.97037 | -49.02438 | 2024-10-23 05:42:00 | AQUA_M-M | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 443a4e7a-4882-3b96-9162-533931296df7 | -3.87592 | -52.32244 | 2024-10-23 05:42:00 | AQUA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 9.9 |
| b4b8e584-7cef-370b-962f-1c155069eb8b | -3.81841 | -48.86814 | 2024-10-23 05:42:00 | AQUA_M-M | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 8.6 |
| 6d2a7d01-c864-34d2-881f-a727121ebc2c | -3.79522 | -50.02878 | 2024-10-23 05:42:00 | AQUA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| c0e9a2cb-8fb3-3785-a68d-0f61036cbf34 | -3.78374 | -52.38698 | 2024-10-23 05:42:00 | AQUA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 9.7 |
| 72675b1b-2801-31a0-b0b0-a5b2460d61a2 | -3.64369 | -54.78809 | 2024-10-23 05:42:00 | AQUA_M-M | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 11.3 |
| 905b0138-b193-3980-848d-51872f0bd5fd | -3.62768 | -53.96169 | 2024-10-23 05:42:00 | AQUA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 760a9ac6-abf7-3895-b342-60cd5a4306c7 | -3.58334 | -53.78179 | 2024-10-23 05:42:00 | AQUA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |


[Clique aqui para ver as próximas entradas](README62.md)
