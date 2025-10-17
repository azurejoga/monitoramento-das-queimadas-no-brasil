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

## Dados Diários - Página 11

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 215f6f91-8d4e-37e8-a2b1-71f3c743fcfb | -7.28325 | -42.30915 | 2025-10-17 00:13:00 | TERRA_M-M | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 8.6 |
| bfb8c307-ff50-3642-900d-9a68a151e679 | -8.3741 | -46.25532 | 2025-10-17 00:13:00 | TERRA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 9.0 |
| 36d4b200-0a72-3aab-86c0-1d31250c0a48 | -8.56705 | -45.43792 | 2025-10-17 00:13:00 | TERRA_M-M | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 10.9 |
| d2b74d15-633d-3211-a8cd-52941a7a99d7 | -8.29663 | -43.40762 | 2025-10-17 00:13:00 | TERRA_M-M | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 7.6 |
| ceb6f61a-3d5e-3cac-a6b3-0a3f7cedc8d9 | -5.64791 | -46.58777 | 2025-10-17 00:13:00 | TERRA_M-M | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 10.6 |
| 60469216-2e49-3325-a086-c905f689bdfa | -6.13443 | -44.22858 | 2025-10-17 00:13:00 | TERRA_M-M | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 6a90490c-050c-3ed6-ba0a-c660108548cd | -7.62352 | -47.82881 | 2025-10-17 00:13:00 | TERRA_M-M | FILADÉLFIA | TOCANTINS | Brasil | 1707702 | 17 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 4f41f807-2b28-3500-bf98-e77794065318 | -4.41833 | -43.42743 | 2025-10-17 00:13:00 | TERRA_M-M | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 5e8a4975-0937-3bce-b80b-f03020e82e0b | -6.58137 | -47.07907 | 2025-10-17 00:13:00 | TERRA_M-M | SÃO JOÃO DO PARAÍSO | MARANHÃO | Brasil | 2111052 | 21 | 33 | nan | nan | nan | Cerrado | 19.2 |
| 2c17abb0-12d3-3d3a-978e-5fe6720e5c2c | -6.53748 | -44.34561 | 2025-10-17 00:13:00 | TERRA_M-M | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 7842a73c-fc96-3ebc-b556-ef21e30df028 | -4.11427 | -42.1945 | 2025-10-17 00:13:00 | TERRA_M-M | BATALHA | PIAUÍ | Brasil | 2201507 | 22 | 33 | nan | nan | nan | Caatinga | 8.2 |
| 767b2644-df78-37bc-9d80-f2571e0b3143 | -9.70961 | -44.56296 | 2025-10-17 00:13:00 | TERRA_M-M | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 6.3 |
| e39a6bbc-a38b-3d45-812b-60e0c4098aa3 | -9.88758 | -47.66887 | 2025-10-17 00:13:00 | TERRA_M-M | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 23.6 |
| 20dd21ed-7df6-3547-8d80-5e74331d3cd7 | -7.28469 | -42.31923 | 2025-10-17 00:13:00 | TERRA_M-M | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 15.7 |
| 04e1d7b6-818d-31e0-8110-9a5ea96adec0 | -8.22104 | -43.9884 | 2025-10-17 00:13:00 | TERRA_M-M | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 9.6 |
| 0e611d60-2767-341e-99a7-519c40089551 | -7.08849 | -44.26638 | 2025-10-17 00:13:00 | TERRA_M-M | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 032f4afe-17b8-34de-b532-271fc5e99b8b | -5.50679 | -47.2994 | 2025-10-17 00:13:00 | TERRA_M-M | SENADOR LA ROCQUE | MARANHÃO | Brasil | 2111763 | 21 | 33 | nan | nan | nan | Cerrado | 57.3 |
| 2cb4817b-f704-3423-8f2e-06c50adaa2ee | -5.94909 | -43.17073 | 2025-10-17 00:13:00 | TERRA_M-M | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 6.9 |
| afce00b5-5f86-345b-b537-9454145efc10 | -4.40784 | -43.41922 | 2025-10-17 00:13:00 | TERRA_M-M | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 25.6 |
| 629f9e6c-3e1c-317a-9e85-c06b745732e3 | -6.19457 | -43.28053 | 2025-10-17 00:13:00 | TERRA_M-M | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 90eccf11-1ea4-367e-9792-2fd4dd1d3e61 | -6.17132 | -43.44231 | 2025-10-17 00:13:00 | TERRA_M-M | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 927fb747-4c1f-3357-b23e-9a71c68b100c | -4.71631 | -46.4428 | 2025-10-17 00:13:00 | TERRA_M-M | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 12.3 |
| ba60d8a5-524a-3f63-842c-737c89140172 | -5.71154 | -46.44753 | 2025-10-17 00:13:00 | TERRA_M-M | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 6.4 |
| cacf4521-abfa-3887-90c5-98d63d03fa28 | -9.19315 | -46.87784 | 2025-10-17 00:13:00 | TERRA_M-M | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 7.4 |
| b960bb09-3213-3a26-baa5-2961953a2ad3 | -7.17348 | -42.18625 | 2025-10-17 00:13:00 | TERRA_M-M | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 6.0 |
| a8e208b4-4a28-3c26-a55e-ed8d726a10e3 | -6.1374 | -41.7356 | 2025-10-17 00:13:00 | TERRA_M-M | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 14.7 |
| ab5c6bd0-538d-37cd-8603-fe1b1e84660e | -8.38333 | -46.25384 | 2025-10-17 00:13:00 | TERRA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 13.0 |
| 99ab8bcf-029e-36db-adfa-d04bd69a8080 | -5.85527 | -43.885 | 2025-10-17 00:13:00 | TERRA_M-M | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 7f393981-4a85-3e96-a3a3-2b7de0471d20 | -8.25862 | -44.06445 | 2025-10-17 00:13:00 | TERRA_M-M | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 12.7 |
| dad54f06-7dca-3c04-a631-d5e05f732663 | -8.11535 | -45.56909 | 2025-10-17 00:13:00 | TERRA_M-M | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 19.9 |
| a91347c8-87f3-36b8-8898-d7f5dc66379f | -6.54333 | -43.92123 | 2025-10-17 00:13:00 | TERRA_M-M | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 11.0 |
| 6512e8e3-67eb-34db-a23d-ff77e2e531ab | -6.25301 | -44.61137 | 2025-10-17 00:13:00 | TERRA_M-M | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 1cda8c23-8157-37bb-b843-849ab9078a8c | -11.12449 | -47.43799 | 2025-10-17 00:13:00 | TERRA_M-M | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 6.9 |
| f2b870b9-e27c-3e3a-ad12-e4f08e205d60 | -5.35761 | -47.30457 | 2025-10-17 00:13:00 | TERRA_M-M | JOÃO LISBOA | MARANHÃO | Brasil | 2105500 | 21 | 33 | nan | nan | nan | Amazônia | 9.1 |
| 543dd09e-615a-34c9-8d2b-c1e29ec92f95 | -8.27844 | -48.00466 | 2025-10-17 00:13:00 | TERRA_M-M | ITAPIRATINS | TOCANTINS | Brasil | 1710904 | 17 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 87636394-d75c-31b9-935a-e5e58d87edb7 | -5.25595 | -44.21502 | 2025-10-17 00:13:00 | TERRA_M-M | GONÇALVES DIAS | MARANHÃO | Brasil | 2104404 | 21 | 33 | nan | nan | nan | Cerrado | 34.4 |
| dd5072a5-1356-3a68-9ce3-4a663151ad68 | -10.51671 | -43.39647 | 2025-10-17 00:13:00 | TERRA_M-M | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 19.4 |
| f01e962c-9039-3e0f-93bc-5751aa959862 | -5.2007 | -43.75227 | 2025-10-17 00:13:00 | TERRA_M-M | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 874bc228-a49a-318f-8e1d-cd0bac8316b2 | -8.40412 | -46.21474 | 2025-10-17 00:13:00 | TERRA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 38.3 |
| dd2cf48f-8ce1-3e4c-91ff-a43ae24679cd | -7.85589 | -49.65166 | 2025-10-17 00:13:00 | TERRA_M-M | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 16.7 |
| 3e4a5854-67e7-3c95-a01d-72ad6c90fc41 | -10.53015 | -44.50073 | 2025-10-17 00:13:00 | TERRA_M-M | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 7.7 |
| f76358b9-a5c9-3d5a-aa7c-8ff66ce6f571 | -7.2041 | -45.50036 | 2025-10-17 00:13:00 | TERRA_M-M | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 45.0 |
| fc703b07-d974-364e-a44e-5142b45b4fe1 | -5.1742 | -42.65532 | 2025-10-17 00:13:00 | TERRA_M-M | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 0b451211-32f5-3bce-899d-5fe7dd5546fc | -10.15825 | -44.54147 | 2025-10-17 00:13:00 | TERRA_M-M | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 36.2 |
| 300e4fc8-d405-3e32-8e93-108eec3a48fa | -6.17456 | -44.32243 | 2025-10-17 00:13:00 | TERRA_M-M | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 40a1f203-d4c2-3864-88af-3344163f8f0d | -7.75647 | -42.46299 | 2025-10-17 00:13:00 | TERRA_M-M | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 9.2 |
| 65f3183b-9572-3942-84f5-531790e51f6b | -5.89398 | -44.82768 | 2025-10-17 00:13:00 | TERRA_M-M | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 5.8 |
| b66468c6-703a-3a34-a97a-e2136742b1d0 | -10.13275 | -48.90385 | 2025-10-17 00:13:00 | TERRA_M-M | PARAÍSO DO TOCANTINS | TOCANTINS | Brasil | 1716109 | 17 | 33 | nan | nan | nan | Cerrado | 10.5 |
| fec7b0e5-e7eb-3536-ad40-7ffbd3cb8fb2 | -7.35394 | -43.85013 | 2025-10-17 00:13:00 | TERRA_M-M | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 13.1 |
| 6ac59fb6-8552-3c56-a601-a78e5eb6f64f | -4.46646 | -42.93037 | 2025-10-17 00:13:00 | TERRA_M-M | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 14.0 |
| f35ec7eb-8580-3cbe-a530-bbe735dcfeb9 | -6.83756 | -42.41581 | 2025-10-17 00:13:00 | TERRA_M-M | CAJAZEIRAS DO PIAUÍ | PIAUÍ | Brasil | 2202075 | 22 | 33 | nan | nan | nan | Caatinga | 10.7 |
| afe956e0-3c09-3035-8e8c-9ae3fd039870 | -4.64032 | -42.5168 | 2025-10-17 00:13:00 | TERRA_M-M | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Caatinga | 15.5 |
| 7c966c1b-cdba-39b9-9348-97158f5642ab | -6.19803 | -41.73772 | 2025-10-17 00:13:00 | TERRA_M-M | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 11.3 |
| 6784de82-6f9a-3241-9382-7980eb4b1a04 | -8.44979 | -44.17844 | 2025-10-17 00:13:00 | TERRA_M-M | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 40.1 |
| 7304c3e0-86f5-3c10-83e2-20fc4fc85554 | -4.47727 | -42.93908 | 2025-10-17 00:13:00 | TERRA_M-M | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 66.5 |
| 69560ae0-ef26-35c0-a041-21e9c6fff5db | -6.35774 | -41.49465 | 2025-10-17 00:13:00 | TERRA_M-M | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 8.3 |
| 0a477490-90c7-333c-bfcb-73e1225534bc | -5.74246 | -49.01959 | 2025-10-17 00:13:00 | TERRA_M-M | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 32.4 |
| e3abd436-bc8e-3bb7-96de-50e53a38c0a0 | -6.74903 | -42.37354 | 2025-10-17 00:13:00 | TERRA_M-M | CAJAZEIRAS DO PIAUÍ | PIAUÍ | Brasil | 2202075 | 22 | 33 | nan | nan | nan | Caatinga | 38.9 |
| a2d7134e-661b-3ec3-9d4c-771df854c273 | -6.15157 | -40.91794 | 2025-10-17 00:13:00 | TERRA_M-M | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 15.7 |
| adb2ba06-ec14-3a39-b23a-565bb0f2f5be | -5.59635 | -50.05633 | 2025-10-17 00:13:00 | TERRA_M-M | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 12.3 |
| bf186bb4-e44a-3fd2-8368-77e164e1f40c | -9.15276 | -41.06196 | 2025-10-17 00:13:00 | TERRA_M-M | CASA NOVA | BAHIA | Brasil | 2907202 | 29 | 33 | nan | nan | nan | Caatinga | 68.4 |
| 36a92577-a6fb-3886-b3c9-6625a62ba9c9 | -6.01193 | -41.93455 | 2025-10-17 00:13:00 | TERRA_M-M | SANTA CRUZ DOS MILAGRES | PIAUÍ | Brasil | 2209153 | 22 | 33 | nan | nan | nan | Caatinga | 21.4 |
| 5b888917-0b63-3173-a3f8-ce5814e7bef0 | -5.72396 | -44.52523 | 2025-10-17 00:13:00 | TERRA_M-M | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 8.3 |
| f852c0c1-ffcb-3dff-9d72-239fa123556c | -7.3321 | -44.15891 | 2025-10-17 00:13:00 | TERRA_M-M | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 9.2 |
| 8662868f-2c7b-35ca-991d-281923220e1f | -8.40542 | -46.22459 | 2025-10-17 00:13:00 | TERRA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 41.1 |
| 606a7b2b-126b-34c2-9bf6-2363f8a5e0d8 | -6.29647 | -45.53211 | 2025-10-17 00:13:00 | TERRA_M-M | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 33.6 |
| c0ba4fc5-013a-3488-8309-f3ae4a2c75d0 | -10.49786 | -43.40551 | 2025-10-17 00:13:00 | TERRA_M-M | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 15.6 |
| 01989c72-ba59-3202-aa2b-f34964030014 | -9.34207 | -46.91229 | 2025-10-17 00:13:00 | TERRA_M-M | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 17.2 |
| e2d73c4e-c009-3c56-852a-9ffd8677950e | -8.44508 | -46.23954 | 2025-10-17 00:13:00 | TERRA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 18.1 |
| 86bd812d-c5b8-31a0-8f1a-aaf72a399cb7 | -7.1245 | -44.7208 | 2025-10-17 00:13:00 | TERRA_M-M | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 9.4 |
| 7c2dc5e7-427c-3e89-ab6b-6ad873bc0c18 | -6.05672 | -44.52549 | 2025-10-17 00:13:00 | TERRA_M-M | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 6.2 |
| b68aafd2-71e2-3f7f-abb4-2e4a2f389ba7 | -9.89785 | -47.66729 | 2025-10-17 00:13:00 | TERRA_M-M | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 23.8 |
| 9235ebc6-7bb5-3b4d-b7c6-c15cc0659b67 | -4.52411 | -45.5853 | 2025-10-17 00:13:00 | TERRA_M-M | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Cerrado | 5.6 |
| f13092c8-e8f9-3b7b-8599-4962ebd55646 | -5.58229 | -47.4623 | 2025-10-17 00:13:00 | TERRA_M-M | IMPERATRIZ | MARANHÃO | Brasil | 2105302 | 21 | 33 | nan | nan | nan | Cerrado | 6.5 |
| d29a0a71-f79d-3ad4-8fa6-0d6bd401003d | -6.39728 | -41.48253 | 2025-10-17 00:13:00 | TERRA_M-M | LAGOA DO SÍTIO | PIAUÍ | Brasil | 2205599 | 22 | 33 | nan | nan | nan | Caatinga | 7.7 |
| 0ee94810-3eb6-3692-a5a8-58d2b3b599d4 | -7.74356 | -42.50481 | 2025-10-17 00:13:00 | TERRA_M-M | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 30.3 |
| 529a1604-8810-3ce2-b7fc-979dd889b2df | -8.3424 | -46.2296 | 2025-10-17 00:13:00 | TERRA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 8.4 |
| 0b6fc13b-4a3f-325b-a2f4-3c0a18a05084 | -7.22007 | -47.8662 | 2025-10-17 00:13:00 | TERRA_M-M | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 22.8 |
| f9fac5a5-2999-3245-9512-01c78863213f | -9.24158 | -44.37804 | 2025-10-17 00:13:00 | TERRA_M-M | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 10.7 |
| 5afbcbb8-75b8-36f7-abe3-0a87e093b197 | -6.30536 | -44.72971 | 2025-10-17 00:13:00 | TERRA_M-M | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 121ad6b1-0c6f-3dbc-893c-194c62cdfb99 | -6.07053 | -41.90855 | 2025-10-17 00:13:00 | TERRA_M-M | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 12.0 |
| 091a0a5b-008d-3bb0-a50b-6ce331e886d2 | -5.94496 | -42.24558 | 2025-10-17 00:13:00 | TERRA_M-M | SÃO FÉLIX DO PIAUÍ | PIAUÍ | Brasil | 2209609 | 22 | 33 | nan | nan | nan | Caatinga | 10.4 |
| 7beec129-8cae-3d71-8b46-208079fbf7d5 | -5.92054 | -45.34586 | 2025-10-17 00:13:00 | TERRA_M-M | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 9a1c8ab3-5172-3989-b802-f21c28b1b62a | -10.11407 | -44.62779 | 2025-10-17 00:13:00 | TERRA_M-M | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 5.8 |
| ad87312d-8e2a-3dc8-b3c2-cf8853bb6908 | -2.70962 | -49.4188 | 2025-10-17 00:16:00 | TERRA_M-M | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 10.7 |
| 543d2277-c441-3a96-a64f-b7182ce512f1 | -3.23147 | -45.95987 | 2025-10-17 00:16:00 | TERRA_M-M | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 10.3 |
| 653cc4d4-615c-35b5-8fd2-6bb01c137719 | -4.00844 | -44.18758 | 2025-10-17 00:16:00 | TERRA_M-M | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 3dfbdba9-bb47-3ead-a4bd-319a19fb3538 | -3.98077 | -42.48207 | 2025-10-17 00:16:00 | TERRA_M-M | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 5.1 |
| 32c7d1d0-0375-3ecb-8d0e-cb93e84b17e9 | -3.15865 | -46.30898 | 2025-10-17 00:16:00 | TERRA_M-M | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | 23.4 |
| ae50c941-af2b-384f-aa59-684b13339c18 | -4.49906 | -47.29242 | 2025-10-17 00:16:00 | TERRA_M-M | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 439238b4-eb84-375f-b6e0-5b22af576aec | -3.51628 | -52.48206 | 2025-10-17 00:16:00 | TERRA_M-M | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 146.3 |
| 65390e20-8ff9-373c-a5e8-d6fefaef2eef | -4.42526 | -47.75299 | 2025-10-17 00:16:00 | TERRA_M-M | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 26.2 |
| dd965d7b-acb0-3429-a988-7adf4b4982a2 | -2.65031 | -48.38077 | 2025-10-17 00:16:00 | TERRA_M-M | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 9.2 |
| d9b8fe6d-4718-33e8-8195-f5b632b29362 | -4.2728 | -45.70173 | 2025-10-17 00:16:00 | TERRA_M-M | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 11.2 |
| a88ac790-76c2-302d-b9bd-87115ca2ce69 | -4.24892 | -48.56353 | 2025-10-17 00:16:00 | TERRA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 8da7fedc-f239-33d4-809a-fbb52e1fea8f | -3.66267 | -50.26877 | 2025-10-17 00:16:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 51.4 |
| ee0c28ac-275a-35ec-b6da-fee5b921e89c | -4.04107 | -47.49442 | 2025-10-17 00:16:00 | TERRA_M-M | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 98cf598d-c817-380d-9ba5-6c1aed44988c | -4.41462 | -48.9551 | 2025-10-17 00:16:00 | TERRA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 18.6 |
| 7ff5c801-744b-3ab6-8759-467b93e3d7dc | -4.05661 | -43.22176 | 2025-10-17 00:16:00 | TERRA_M-M | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 3689ac91-77a9-3797-b7c7-a565e95edc40 | -0.90566 | -47.53998 | 2025-10-17 00:16:00 | TERRA_M-M | MARACANÃ | PARÁ | Brasil | 1504307 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |


[Clique aqui para ver as próximas entradas](README12.md)
