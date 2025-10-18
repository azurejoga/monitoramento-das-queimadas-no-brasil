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

## Dados Diários - Página 15

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 21a3638f-2f07-364d-8f49-cea64eaccbc7 | -0.90386 | -47.54983 | 2025-10-18 04:00:00 | NOAA-21 | MARACANÃ | PARÁ | Brasil | 1504307 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 553bbab1-3f29-3550-86a0-18ece381dc2f | -2.80664 | -48.66488 | 2025-10-18 04:00:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 22c009f3-cb82-33a9-aa8c-882ca45ffcc5 | -3.14174 | -50.24556 | 2025-10-18 04:00:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 12.7 |
| 6cd64899-c76a-3ad0-97a4-08a6ec349e8d | -3.4953 | -42.72335 | 2025-10-18 04:00:00 | NOAA-21 | MILAGRES DO MARANHÃO | MARANHÃO | Brasil | 2106672 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e6d6c413-c366-33c9-a08e-d6ab2214f488 | -6.522 | -44.90419 | 2025-10-18 04:00:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 92a32653-3fd8-369f-8141-629a27ecb64e | -6.13328 | -44.21791 | 2025-10-18 04:00:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 82819531-6e5c-3a2d-bf68-fd7f13c4e96b | -6.30701 | -45.54449 | 2025-10-18 04:00:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 348f8772-0850-3478-9dea-1096f16c8168 | -7.54911 | -37.79005 | 2025-10-18 04:00:00 | NOAA-21 | JURU | PARAÍBA | Brasil | 2508000 | 25 | 33 | nan | nan | nan | Caatinga | 1.3 |
| c3ec04a9-3daa-3915-bc88-ad037c21f0bb | -5.70622 | -44.19269 | 2025-10-18 04:00:00 | NOAA-21 | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| a2329bc5-97a0-37d7-b814-90b469f87c79 | -6.14601 | -44.45624 | 2025-10-18 04:00:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 44914eb2-a0f2-382e-a2e5-5bce94e09030 | -3.2386 | -42.07244 | 2025-10-18 04:00:00 | NOAA-21 | MAGALHÃES DE ALMEIDA | MARANHÃO | Brasil | 2106300 | 21 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 07a921fa-a71e-32c3-b382-feebad3fdc07 | -5.84713 | -44.33815 | 2025-10-18 04:00:00 | NOAA-21 | JATOBÁ | MARANHÃO | Brasil | 2105450 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| ee283feb-5b7a-36d9-8737-dc68cedc3c13 | -5.16338 | -45.21776 | 2025-10-18 04:00:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 0ea5c532-ba50-362f-8720-bd48b40b88d8 | -5.20797 | -45.75109 | 2025-10-18 04:00:00 | NOAA-21 | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 16708ed7-391b-3807-bcc8-2aad67aada58 | -3.24214 | -45.96479 | 2025-10-18 04:00:00 | NOAA-21 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 21659d35-c083-3af1-ad40-8a6f1d2f8230 | -5.87863 | -44.84018 | 2025-10-18 04:00:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| aa3804a5-d95c-318c-81e6-4c292c8b5f90 | -6.8437 | -41.71706 | 2025-10-18 04:00:00 | NOAA-21 | IPIRANGA DO PIAUÍ | PIAUÍ | Brasil | 2204808 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 745e0630-1fea-3a6d-8e0c-4b8017195fdb | -5.92053 | -45.44263 | 2025-10-18 04:00:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| efe533f8-01fc-373d-b065-02002b9abf5b | -2.86303 | -50.74039 | 2025-10-18 04:00:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 0c8c9fc9-11e5-3feb-af21-ae90b3b29825 | -5.7606 | -46.69024 | 2025-10-18 04:00:00 | NOAA-21 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| e5597f82-78fd-302a-a305-303da51de9df | -6.84532 | -42.42219 | 2025-10-18 04:00:00 | NOAA-21 | CAJAZEIRAS DO PIAUÍ | PIAUÍ | Brasil | 2202075 | 22 | 33 | nan | nan | nan | Caatinga | 3.7 |
| 0d5076ce-92a6-3302-938f-8ce894629d94 | -6.45444 | -44.20303 | 2025-10-18 04:00:00 | NOAA-21 | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 44109890-0032-37ac-8b39-1e55d65cab63 | -6.10854 | -45.85126 | 2025-10-18 04:00:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| eece98ba-709b-310e-b665-7d47e3e4580d | -6.9888 | -38.4312 | 2025-10-18 04:00:00 | NOAA-21 | SÃO JOSÉ DE PIRANHAS | PARAÍBA | Brasil | 2514503 | 25 | 33 | nan | nan | nan | Caatinga | 1.9 |
| ee5d4782-f55c-3e26-932f-dc0c71cda6e4 | -7.04376 | -41.82782 | 2025-10-18 04:00:00 | NOAA-21 | SÃO JOÃO DA VARJOTA | PIAUÍ | Brasil | 2209955 | 22 | 33 | nan | nan | nan | Caatinga | 3.8 |
| df1aa403-3872-3327-983f-b41e1cf64946 | -3.1425 | -50.24098 | 2025-10-18 04:00:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 8.9 |
| 2eda4349-0940-337e-9549-189046990c49 | -5.91462 | -43.94398 | 2025-10-18 04:00:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 6d77325b-79f2-3826-8e16-f5494fb69c85 | -6.96371 | -39.67068 | 2025-10-18 04:00:00 | NOAA-21 | ALTANEIRA | CEARÁ | Brasil | 2300606 | 23 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 1d70f185-ae9a-3725-b7ec-3add151955d0 | -5.71423 | -46.51351 | 2025-10-18 04:00:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 8d64ae26-5fa2-3857-8bb9-09039c9dcc02 | -6.31464 | -44.31713 | 2025-10-18 04:00:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 93eb152a-c152-3831-997c-fc4d0545df65 | -6.70014 | -40.8699 | 2025-10-18 04:00:00 | NOAA-21 | PIO IX | PIAUÍ | Brasil | 2208205 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 96872e4a-17b9-38c8-8026-05b108e00f6f | -5.21073 | -46.19523 | 2025-10-18 04:00:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| da54b548-73f0-3ab9-ac05-3c8c4e5b05e7 | -2.87182 | -50.7266 | 2025-10-18 04:00:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| a9fb915f-bc5d-32b3-9a6f-7ad053066170 | -4.00376 | -45.50685 | 2025-10-18 04:00:00 | NOAA-21 | ALTAMIRA DO MARANHÃO | MARANHÃO | Brasil | 2100402 | 21 | 33 | nan | nan | nan | Amazônia | 9.4 |
| bd61ee19-9847-36aa-9c65-003d3a8074f4 | -2.86845 | -50.74637 | 2025-10-18 04:00:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 0620b10f-804f-3e3a-b906-09dbd865bd93 | -6.96822 | -42.20651 | 2025-10-18 04:00:00 | NOAA-21 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 945d86aa-7de2-3886-a342-b66398ab2643 | -4.44269 | -43.22304 | 2025-10-18 04:00:00 | NOAA-21 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| dd204d5d-f79c-31a8-94e1-534811c65a3f | -3.8516 | -41.5737 | 2025-10-18 04:00:00 | NOAA-21 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 8.6 |
| 0d5dc4fe-6893-3e67-b352-02fbbe41943e | -4.82365 | -47.08386 | 2025-10-18 04:00:00 | NOAA-21 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 50cd81c1-b6bf-3d69-a0fa-feb84e485ead | -2.3676 | -48.29654 | 2025-10-18 04:00:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f0dd4826-706d-35b8-ba79-6ac965efb7a7 | -6.37967 | -43.56865 | 2025-10-18 04:00:00 | NOAA-21 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 94b669aa-d907-33f3-8466-a2314dec2ec2 | -4.46431 | -43.231 | 2025-10-18 04:00:00 | NOAA-21 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| bd9284d3-8203-34d3-b37d-b63f6ad95ca8 | -7.10329 | -41.45818 | 2025-10-18 04:00:00 | NOAA-21 | PICOS | PIAUÍ | Brasil | 2208007 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| d7025895-d4d3-30f8-8bcf-abacb6e9f6e8 | -5.33906 | -44.99613 | 2025-10-18 04:00:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 7b2c0362-7305-3453-ba26-248c86b25b10 | -2.87723 | -50.73255 | 2025-10-18 04:00:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| ade50605-3a85-3cdc-ba6f-3e677389cf0c | -4.97234 | -44.61128 | 2025-10-18 04:00:00 | NOAA-21 | SÃO JOSÉ DOS BASÍLIOS | MARANHÃO | Brasil | 2111250 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 5d649caa-e9a6-3ff1-bbb5-866bf162ad80 | -4.44642 | -43.22361 | 2025-10-18 04:00:00 | NOAA-21 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| a8aed7a2-2f0f-3d94-a335-b5f5cec35046 | -4.82316 | -44.42103 | 2025-10-18 04:00:00 | NOAA-21 | SANTO ANTÔNIO DOS LOPES | MARANHÃO | Brasil | 2110302 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 9b022994-18d1-3786-8064-4fba67fd6432 | -5.16859 | -48.60155 | 2025-10-18 04:00:00 | NOAA-21 | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 37c7a614-54e1-3bfd-9ba6-9c28a5eda6c2 | -3.99943 | -45.50613 | 2025-10-18 04:00:00 | NOAA-21 | ALTAMIRA DO MARANHÃO | MARANHÃO | Brasil | 2100402 | 21 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 332b26d1-976f-38fd-984a-4ef08e75b5f4 | -2.91173 | -52.72644 | 2025-10-18 04:00:00 | NOAA-21 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 1b743a99-7976-3c68-9cc9-6cd9e3eecc6a | -5.25528 | -47.23916 | 2025-10-18 04:00:00 | NOAA-21 | SÃO FRANCISCO DO BREJÃO | MARANHÃO | Brasil | 2110856 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 4080a56d-2a39-3eaf-9dde-85fa0f8b8d19 | -4.93981 | -41.55734 | 2025-10-18 04:00:00 | NOAA-21 | JUAZEIRO DO PIAUÍ | PIAUÍ | Brasil | 2205516 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 36a2d6c4-93d7-34b7-9d5c-8199898762e5 | -5.56003 | -46.3719 | 2025-10-18 04:00:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| eb751055-ecf3-3af3-a33f-74776db001db | -0.90543 | -47.54015 | 2025-10-18 04:00:00 | NOAA-21 | MARACANÃ | PARÁ | Brasil | 1504307 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| e657fdf3-efaa-3d7e-bcf4-fd1c6c7b20b0 | -6.13411 | -44.2129 | 2025-10-18 04:00:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| c5f5fa3f-e19f-352b-9f76-f7b019b7d68c | -2.42458 | -47.14594 | 2025-10-18 04:00:00 | NOAA-21 | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 22a7c4b6-cab1-3b82-894f-d9e55a6ce9e5 | -6.5186 | -44.90004 | 2025-10-18 04:00:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 9947ed57-576e-3dad-9ea0-abe1b3795495 | -5.8933 | -43.90698 | 2025-10-18 04:00:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| c857bc85-fc12-3674-a007-08e83c696c17 | -6.73787 | -44.36632 | 2025-10-18 04:00:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 06749014-cb17-34c7-8fc4-bce88bed5ac7 | -6.4841 | -44.55691 | 2025-10-18 04:00:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| c7336257-ef3a-3a18-85ea-780508806790 | -6.31771 | -44.32252 | 2025-10-18 04:00:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| cec2ae8d-6586-33e8-8f20-64cb168fa609 | -5.79873 | -41.89933 | 2025-10-18 04:00:00 | NOAA-21 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 823f741b-3749-3960-96d5-50357018e16a | -6.14796 | -40.9182 | 2025-10-18 04:00:00 | NOAA-21 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 331a75c1-c303-39a9-a228-fbb60c1a288f | -6.98541 | -39.24418 | 2025-10-18 04:00:00 | NOAA-21 | CARIRIAÇU | CEARÁ | Brasil | 2303204 | 23 | 33 | nan | nan | nan | Caatinga | 8.7 |
| 32c64cb3-6790-31dd-941f-ac5a850a6090 | -7.00286 | -42.01542 | 2025-10-18 04:00:00 | NOAA-21 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 3b55bd39-d004-37b0-b4c0-ed275f9e186e | -3.68472 | -45.63627 | 2025-10-18 04:00:00 | NOAA-21 | TUFILÂNDIA | MARANHÃO | Brasil | 2112274 | 21 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 0796d2c8-e73d-30f2-8314-01b3b3b30c16 | -2.74646 | -49.38994 | 2025-10-18 04:00:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 09395b13-569b-3b93-9c3c-caa979f5e487 | -3.49896 | -42.72392 | 2025-10-18 04:00:00 | NOAA-21 | MILAGRES DO MARANHÃO | MARANHÃO | Brasil | 2106672 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 1024c086-c64c-344e-8260-4bfcde5cef8f | -3.14199 | -50.25349 | 2025-10-18 04:00:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| e230c192-92fb-3fc5-b262-7dd42b52ff8c | -6.48449 | -39.59877 | 2025-10-18 04:00:00 | NOAA-21 | JUCÁS | CEARÁ | Brasil | 2307403 | 23 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 7f861c67-ec0f-3418-a7e4-8565ac3e1b80 | -5.74588 | -43.83349 | 2025-10-18 04:00:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| f78bf678-033d-3098-a0e6-7cf1002b1cca | -3.90163 | -43.03998 | 2025-10-18 04:00:00 | NOAA-21 | BURITI | MARANHÃO | Brasil | 2102200 | 21 | 33 | nan | nan | nan | Cerrado | 6.2 |
| ab20b31d-9a1c-3380-bcd8-57409ae2aaff | -6.51683 | -44.89884 | 2025-10-18 04:00:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 37310c01-81fb-3fc5-9b6b-f217b06e81e3 | -5.89226 | -44.70542 | 2025-10-18 04:00:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| cc49412b-6ad4-3e32-9e95-d08a0865db13 | -6.5226 | -44.90069 | 2025-10-18 04:00:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 26057794-14f8-34dc-8230-00d22d1a8e71 | -5.70973 | -46.45646 | 2025-10-18 04:00:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| f58627f5-fb02-31cd-8e6e-e7b56441d030 | -5.45705 | -45.40832 | 2025-10-18 04:00:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 59ebbd2f-37aa-3326-860e-04d1c094c615 | -5.6004 | -46.37843 | 2025-10-18 04:00:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 00ddc1e7-bb23-3f99-a091-f1882cfcc844 | -3.60022 | -42.83941 | 2025-10-18 04:00:00 | NOAA-21 | BREJO | MARANHÃO | Brasil | 2102101 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| a2b43bb4-4779-39bd-823c-f2c9dcf9560b | -6.526 | -44.90484 | 2025-10-18 04:00:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ff13fd43-cdb8-3b21-bafe-160d36e9d770 | -5.21656 | -45.51862 | 2025-10-18 04:00:00 | NOAA-21 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 467fcb1d-1fdb-3b17-bebf-5684b720296d | -6.18084 | -46.74259 | 2025-10-18 04:00:00 | NOAA-21 | LAJEADO NOVO | MARANHÃO | Brasil | 2105989 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 9a98b5a8-f5f0-329c-9ac7-77be760bc65d | -5.01328 | -46.0212 | 2025-10-18 04:00:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 21.0 |
| 0ddafbd5-fb91-38cd-9bd0-bb4dbbdeeaa2 | -5.99792 | -44.15078 | 2025-10-18 04:00:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 5fbfa2b0-6878-3430-82f4-96da76343298 | -2.73975 | -49.3877 | 2025-10-18 04:00:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| af309dbd-9242-341a-a93d-535a9c48b5ab | -2.74614 | -49.38474 | 2025-10-18 04:00:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 4abe6262-fa67-33a5-ba71-cfe387179684 | -6.78158 | -40.8935 | 2025-10-18 04:00:00 | NOAA-21 | ALAGOINHA DO PIAUÍ | PIAUÍ | Brasil | 2200251 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 8389e1d9-faf1-359c-a68e-e1f26728dedc | -5.99183 | -44.15294 | 2025-10-18 04:00:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 50ccd60d-e324-3b51-a313-1cf65a30311c | -4.14569 | -44.0564 | 2025-10-18 04:00:00 | NOAA-21 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 9598e2a5-95b4-3cb8-9473-089d2d455e77 | -3.99844 | -43.27857 | 2025-10-18 04:00:00 | NOAA-21 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| d5040622-3948-3b5a-9af2-dafb6a6f64cd | -2.8693 | -50.74139 | 2025-10-18 04:00:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 8c126ac2-f5dc-3e5f-8338-9087d9e96f83 | -3.06401 | -43.21789 | 2025-10-18 04:00:00 | NOAA-21 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 60ae38da-96db-3a80-8b1a-64e7c9719db9 | -3.85263 | -41.58947 | 2025-10-18 04:00:00 | NOAA-21 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| a17b1aff-e8f0-39fd-a036-9e710d5cff9f | -6.91555 | -37.85553 | 2025-10-18 04:00:00 | NOAA-21 | CAJAZEIRINHAS | PARAÍBA | Brasil | 2503753 | 25 | 33 | nan | nan | nan | Caatinga | 0.8 |
| f5d3ad9b-bc25-3ba2-9fa6-2227e2fca2f2 | -5.65466 | -46.81343 | 2025-10-18 04:00:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 85828f06-9c63-3b7d-bcf5-5f2c508a1bd6 | -3.83821 | -47.40255 | 2025-10-18 04:00:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 7942a0fd-f227-30d6-93cd-8b1a3bc640aa | -6.29588 | -44.72091 | 2025-10-18 04:00:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 78fdd984-05ca-363b-8402-865facfd1476 | -6.33855 | -46.34162 | 2025-10-18 04:00:00 | NOAA-21 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 293b0480-5f89-31ed-b09a-d69ca556df2e | -6.53248 | -42.18373 | 2025-10-18 04:00:00 | NOAA-21 | VÁRZEA GRANDE | PIAUÍ | Brasil | 2211407 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |


[Clique aqui para ver as próximas entradas](README16.md)
