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

## Dados Diários - Página 14

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| b5a84a5d-c6f7-39dc-a463-1b15355ce9ce | -9.57165 | -49.11358 | 2025-05-27 04:49:00 | NOAA-20 | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 41659914-6057-343e-aea4-822fe5bdf7b4 | -6.2298 | -43.34611 | 2025-05-27 04:49:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 84c59ac7-4296-3f0e-87e0-c93af36f36ea | -7.97069 | -49.69699 | 2025-05-27 04:49:00 | NOAA-20 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 501f0582-1694-3b59-84e6-227dd6b1f4cc | -6.64463 | -43.20346 | 2025-05-27 04:49:00 | NOAA-20 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Caatinga | 1.4 |
| d49d32ce-3d0c-363d-bd0a-c9481f600dd4 | -6.64366 | -43.21048 | 2025-05-27 04:49:00 | NOAA-20 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 8a66f4b6-bdfd-3743-aa2d-a5ec752738fc | -9.35422 | -57.53391 | 2025-05-27 04:49:00 | NOAA-20 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b834efde-bfa7-3a78-8d2d-48aa5f8d4ab6 | -6.63819 | -43.20982 | 2025-05-27 04:49:00 | NOAA-20 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Caatinga | 1.4 |
| a29ef070-ee38-3f4a-815a-0c19faf35d03 | -7.60199 | -43.39698 | 2025-05-27 04:49:00 | NOAA-20 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 6dc2d070-c0ec-3620-88d1-6598bd7322b9 | -7.47218 | -43.36061 | 2025-05-27 04:49:00 | NOAA-20 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 0d1d9123-fdfc-3402-90fb-c739540e18e0 | -8.78747 | -49.90674 | 2025-05-27 04:49:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| fa5a0350-017d-3c27-982f-7f50a75d5496 | -9.60397 | -49.02591 | 2025-05-27 04:49:00 | NOAA-20 | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 0acbfa70-d2b5-35fa-8420-b60e50682ca9 | -7.55623 | -43.36544 | 2025-05-27 04:49:00 | NOAA-20 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 3be2b063-eda3-3a4c-9509-ae5331bd287f | -7.07568 | -43.55787 | 2025-05-27 04:49:00 | NOAA-20 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e50bbeeb-1944-3ded-b4bc-944df1bb2101 | -8.42916 | -46.65906 | 2025-05-27 04:49:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| a41a73ff-f001-3c8d-a7ff-4544391635ba | -8.4342 | -46.65529 | 2025-05-27 04:49:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| de374e92-7eae-3c12-bd96-0051f482a3a1 | -9.03648 | -47.75029 | 2025-05-27 04:49:00 | NOAA-20 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 93b83fdf-7de9-34a1-aa96-5afa6b3e028a | -7.20226 | -43.11558 | 2025-05-27 04:49:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 8.4 |
| 4694e080-2040-3223-8a84-b905fe315859 | -6.49941 | -47.49018 | 2025-05-27 04:49:00 | NOAA-20 | AGUIARNÓPOLIS | TOCANTINS | Brasil | 1700301 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 3e344862-b92b-3be0-b3f2-fc9799f2ca38 | -7.61976 | -45.76183 | 2025-05-27 04:49:00 | NOAA-20 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| b15ba72c-4c58-3f70-9315-77b66682b575 | -10.64256 | -48.08699 | 2025-05-27 04:49:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| efe8ba75-20a8-3611-a191-454e0612675f | -6.22493 | -43.34185 | 2025-05-27 04:49:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 6845f42e-ca1c-371a-b73d-d76178e4d97c | -7.54668 | -43.18433 | 2025-05-27 04:49:00 | NOAA-20 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| d2fcb971-01e7-3fe5-ac87-c0b221695aa6 | -6.65059 | -43.20055 | 2025-05-27 04:49:00 | NOAA-20 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 7a379a81-3037-3232-a7f1-a69422f3467d | -8.04127 | -49.6499 | 2025-05-27 04:49:00 | NOAA-20 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 00e8c950-1ee7-3916-8d97-725bcc2808d8 | -8.42978 | -46.6547 | 2025-05-27 04:49:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 37e99c6a-3ead-3c0d-a2fa-063585bfed81 | -7.60102 | -43.40403 | 2025-05-27 04:49:00 | NOAA-20 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 6b6e8f00-fc01-371c-a2e0-f847e6832257 | -8.7216 | -49.38414 | 2025-05-27 04:49:00 | NOAA-20 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| eccf2915-88f4-3e7c-8402-f0c47180a04f | -6.49995 | -47.48657 | 2025-05-27 04:49:00 | NOAA-20 | AGUIARNÓPOLIS | TOCANTINS | Brasil | 1700301 | 17 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 9300a375-59a1-3921-bd4d-c7a6347cb8d0 | -6.22443 | -43.34536 | 2025-05-27 04:49:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 59cd849c-11e4-3a00-af9f-22d8e3bf4c75 | -8.77862 | -47.95479 | 2025-05-27 04:49:00 | NOAA-20 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f8ff7b99-0559-37ac-b1bf-c5fa3e629485 | -8.02038 | -49.68732 | 2025-05-27 04:49:00 | NOAA-20 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 471e2e81-07b6-3f34-8e42-f8b1df9a0031 | -6.63228 | -43.21241 | 2025-05-27 04:49:00 | NOAA-20 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Caatinga | 2.8 |
| c40df0a1-eb0d-348c-9156-eb60a048dd4c | -7.22484 | -43.11521 | 2025-05-27 04:49:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| ce5b4a0e-7dbd-376a-a148-e68caac81779 | -7.62506 | -45.76619 | 2025-05-27 04:49:00 | NOAA-20 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| ac578912-315a-316b-98b7-f3e58e9a8c31 | -8.7832 | -47.95181 | 2025-05-27 04:49:00 | NOAA-20 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 7179fb06-ad76-3e7f-9afd-ec893ec98147 | -7.20176 | -43.11928 | 2025-05-27 04:49:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 6.9 |
| 92be6fcc-3d58-3814-abf0-953e9626787f | -7.40665 | -49.37317 | 2025-05-27 04:49:00 | NOAA-20 | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| f9af6d1d-5e78-3dc2-b152-cebda99c118c | -8.59631 | -49.85996 | 2025-05-27 04:49:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 8bd316a6-6682-3df6-af53-90e814af93f8 | -7.62902 | -45.76335 | 2025-05-27 04:49:00 | NOAA-20 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 4be11c48-0d8c-380e-acd1-d1eb9f451b79 | -8.43544 | -46.64654 | 2025-05-27 04:49:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 40e16135-9b2a-37e2-a32b-629f71f586da | -7.2128 | -43.12085 | 2025-05-27 04:49:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 4.3 |
| 9703d882-5e18-35db-8f0d-3dc3221f14b2 | -7.60053 | -43.40754 | 2025-05-27 04:49:00 | NOAA-20 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 5e1b4fad-2a8f-348d-988b-12360d2aeecf | -6.15849 | -48.05385 | 2025-05-27 04:49:00 | NOAA-20 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 2bb52701-8a30-3c3c-aede-05e63523d4d1 | -10.64039 | -48.08733 | 2025-05-27 04:49:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 905b468f-7e30-3478-af19-4c757bd9a9bd | -9.57547 | -49.11416 | 2025-05-27 04:49:00 | NOAA-20 | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 810bec8c-b3c2-3c8d-a46e-e933ade5314b | -6.63277 | -43.20891 | 2025-05-27 04:49:00 | NOAA-20 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 9b1ac5d6-7d35-36da-8645-bc41b1c13238 | -8.4304 | -46.65032 | 2025-05-27 04:49:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 3910201b-61b9-3643-a224-aea40eaf27b1 | -4.17335 | -47.53073 | 2025-05-27 04:49:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 5c987e70-1ce8-352e-800b-eb94d8a3140e | -7.19774 | -43.10747 | 2025-05-27 04:49:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 7.6 |
| 6b498180-5d56-32b1-915c-061d876c67f3 | -9.38818 | -48.41837 | 2025-05-27 04:49:00 | NOAA-20 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 82dd5b00-6ba6-3410-bd28-8d7212e6d60a | -7.62439 | -45.76258 | 2025-05-27 04:49:00 | NOAA-20 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| bbe0effe-6cb7-3416-9545-360898f44419 | -7.62576 | -45.76133 | 2025-05-27 04:49:00 | NOAA-20 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| e10f94ab-9c11-3007-b83e-e3a4502fd157 | -7.59958 | -43.4145 | 2025-05-27 04:49:00 | NOAA-20 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 4ac87ce6-c834-3495-b663-ccf7bacc98e4 | -6.32316 | -43.36638 | 2025-05-27 04:49:00 | NOAA-20 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 46a7eea2-455f-3d3a-ae6c-c0d6772ccf9b | -8.01847 | -43.18425 | 2025-05-27 04:49:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 96e43cf0-1021-395f-ab0b-433984686266 | -6.22879 | -43.35316 | 2025-05-27 04:49:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| afba982f-b5c7-39a1-92d4-ac44a4d02fbb | -9.91392 | -50.63893 | 2025-05-27 04:49:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 768133bf-0ba3-31fc-8ff0-fafad2395c23 | -7.97131 | -49.69279 | 2025-05-27 04:49:00 | NOAA-20 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| bddb486a-b4e6-319e-bcaa-974762610f7f | -6.16555 | -48.05991 | 2025-05-27 04:49:00 | NOAA-20 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 6e824f78-4dcb-3915-813c-4865c056e6a5 | -6.2147 | -43.33681 | 2025-05-27 04:49:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 30f626ce-c563-3fcb-9fb4-abc38c973542 | -8.43358 | -46.65966 | 2025-05-27 04:49:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 93eddb9f-31cb-31dd-bbca-a54b48bc0ea6 | -4.41073 | -47.95343 | 2025-05-27 04:49:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| fd5c96ae-da4a-3860-917d-e39052428c27 | -9.15303 | -49.6539 | 2025-05-27 04:49:00 | NOAA-20 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 78352938-2e31-3c6c-b866-9d6b1015bf72 | -8.78268 | -47.95541 | 2025-05-27 04:49:00 | NOAA-20 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 8a71ebb6-2ff5-304a-95f3-25d5a413a54e | -6.65168 | -41.99623 | 2025-05-27 04:49:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 0.6 |
| a91d556f-635c-3dff-aa0c-947ba8fdb55c | -6.16167 | -48.05926 | 2025-05-27 04:49:00 | NOAA-20 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| a3d02eca-31da-34be-b61f-e8e50ca6aa73 | -9.39462 | -48.42987 | 2025-05-27 04:49:00 | NOAA-20 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 6d99cd44-4d18-368b-9739-ec7ffec358b7 | -6.64414 | -43.20699 | 2025-05-27 04:49:00 | NOAA-20 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 1b91c2a9-b227-3033-a649-9a47e77505fd | -8.43102 | -46.64594 | 2025-05-27 04:49:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 3d88b96e-4749-321f-9834-fa9828c344dc | -7.406 | -49.37749 | 2025-05-27 04:49:00 | NOAA-20 | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c0a651ac-1b12-3a33-b67a-bcc979e24eaa | -7.96706 | -49.69644 | 2025-05-27 04:49:00 | NOAA-20 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| fe5954e4-f800-3e23-aa78-c99dad64fd86 | -6.63182 | -43.21577 | 2025-05-27 04:49:00 | NOAA-20 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Caatinga | 6.2 |
| 600aea91-ec94-3f6d-8ee8-bbefac25e032 | -5.77891 | -43.61773 | 2025-05-27 04:49:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 5b768b65-380b-3004-b8a5-40198c4d687f | -7.3092 | -55.30902 | 2025-05-27 04:49:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 0f996865-49b7-3142-a793-5df951ddfc76 | -8.74997 | -49.75478 | 2025-05-27 04:49:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| e431184a-5c6a-3468-957a-855b366c8c1b | -8.01798 | -43.18795 | 2025-05-27 04:49:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 59627d8b-0843-3a2e-8ef2-b67639fc2beb | -8.3155 | -55.11734 | 2025-05-27 04:49:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 2f680f88-febe-382d-8f7d-7037d1b358a6 | -7.23138 | -43.10874 | 2025-05-27 04:49:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 4.8 |
| 629076cc-8575-3938-8585-1d6bcdfc65bb | -8.75258 | -48.04959 | 2025-05-27 04:49:00 | NOAA-20 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 49556d76-eb25-3b2a-8107-0bb603534976 | -7.23087 | -43.11242 | 2025-05-27 04:49:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 4.8 |
| 389ded32-03c4-3d85-8603-f393ea5dc12f | -7.20778 | -43.11638 | 2025-05-27 04:49:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 5.2 |
| e9042805-11a6-3aa3-906d-b3504623351e | -8.64872 | -49.40336 | 2025-05-27 04:49:00 | NOAA-20 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a0f3a5cf-03e3-3127-8747-a2f5dd880e4e | -9.03343 | -47.74209 | 2025-05-27 04:49:00 | NOAA-20 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a9f55dc3-1bdc-3803-a6ec-d623321922c3 | -5.78415 | -43.61845 | 2025-05-27 04:49:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 8ad4d9f2-6140-300a-b88b-903b1e929676 | -8.29732 | -55.09886 | 2025-05-27 04:49:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4929f82a-b4c9-3987-96f7-7f0f36cc350a | -10.35999 | -47.97649 | 2025-05-27 04:49:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e9025812-f393-3fa8-a664-f4f346d48afa | -7.20624 | -45.35273 | 2025-05-27 04:49:00 | NOAA-20 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| b9e20594-9ad0-3087-af68-7e2b1a34fa5d | -5.42567 | -49.08149 | 2025-05-27 04:49:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| a2528d1b-8f68-33fa-8fb3-c4e357a0614d | -8.75126 | -49.74621 | 2025-05-27 04:49:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 426fa838-67ca-3e18-a088-57887794d8f2 | -7.5746 | -43.35301 | 2025-05-27 04:49:00 | NOAA-20 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 22a43c62-d7de-3c59-b1c9-0c93c5983686 | -6.64578 | -41.99549 | 2025-05-27 04:49:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 0.4 |
| f695d682-2db2-3433-8b6e-6e6158a300cd | -7.20125 | -43.12293 | 2025-05-27 04:49:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 6.9 |
| 01cfa6a2-4da2-32c9-b7a6-cab30f982dbf | -7.6015 | -43.40051 | 2025-05-27 04:49:00 | NOAA-20 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 24dcfc82-a040-3f21-8ba0-1a26a60af3d7 | -9.03702 | -47.7465 | 2025-05-27 04:49:00 | NOAA-20 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| abbd35d5-0968-32f6-a28f-291b861625c8 | -6.6501 | -43.2041 | 2025-05-27 04:49:00 | NOAA-20 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Caatinga | 1.3 |
| d252b366-46f1-3bf1-9e8b-f3cff1dba976 | -10.63626 | -48.08669 | 2025-05-27 04:49:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 627d8249-836d-3f21-978d-7e8847830bd1 | -10.36051 | -47.97276 | 2025-05-27 04:49:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| e4452903-bddf-3725-8659-8af90829d4ca | -8.74395 | -49.74512 | 2025-05-27 04:49:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 2d09a1bb-3b24-38d2-93f4-5bd0ed5001fe | -8.75516 | -47.67668 | 2025-05-27 04:49:00 | NOAA-20 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 70299ca6-c9f8-3d43-96b9-bfce2e8657a6 | -9.15367 | -49.64952 | 2025-05-27 04:49:00 | NOAA-20 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |


[Clique aqui para ver as próximas entradas](README15.md)
