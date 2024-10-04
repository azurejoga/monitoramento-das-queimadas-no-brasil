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

## Dados Diários - Página 29

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 901d85bb-9daf-382f-9fcc-a74a7b94f5aa | -3.30235 | -50.45178 | 2024-10-04 01:11:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 128.2 |
| a5e0cd41-4553-37e9-85a2-f64e0e347292 | -3.29441 | -50.46296 | 2024-10-04 01:11:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 87.8 |
| f2d49714-c910-3255-8c46-4b0fa454daaf | -3.29303 | -50.45311 | 2024-10-04 01:11:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 240.1 |
| c7327439-f8fb-3abe-ac47-23406b85090a | -3.29165 | -50.44327 | 2024-10-04 01:11:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 16.3 |
| 655ee21b-4e83-3d9a-80f3-e084f3223ff9 | -3.28372 | -50.45449 | 2024-10-04 01:11:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 19.1 |
| b0b1ea10-4715-3cf8-b1d8-7270506966a3 | -3.2445 | -50.37925 | 2024-10-04 01:11:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 15.4 |
| a4dc8cc5-0e6b-388f-973b-711417a8aef0 | -3.24309 | -50.3693 | 2024-10-04 01:11:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 45.1 |
| 044b64cc-33b7-3271-9099-3cfdb90c2458 | -3.11267 | -50.48124 | 2024-10-04 01:11:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 10.6 |
| e08b9d61-ecd6-3e27-b84b-40be9e150c79 | -3.11129 | -50.47139 | 2024-10-04 01:11:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 17.4 |
| 9fb78cfc-b474-3d72-88f2-8eb12230c76d | -3.10196 | -50.47272 | 2024-10-04 01:11:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 9.1 |
| 2ec0f08e-52a9-33c0-b28c-dff28d50dcae | -5.06692 | -49.79128 | 2024-10-04 01:11:00 | TERRA_M-M | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 911cd529-aca7-3866-b669-865e119e5750 | -5.02041 | -49.77261 | 2024-10-04 01:11:00 | TERRA_M-M | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 22.4 |
| 0c8cb8bc-6b4e-3618-8a3c-1ebfff2cd21b | -5.0124 | -49.78421 | 2024-10-04 01:11:00 | TERRA_M-M | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| c25c7ea2-7c1f-307e-820e-2356100551d1 | -4.94549 | -50.73946 | 2024-10-04 01:11:00 | TERRA_M-M | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| a4b69267-adab-36ef-aaa4-9febe8566ece | -4.6618 | -50.88427 | 2024-10-04 01:11:00 | TERRA_M-M | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 10.6 |
| 3e94ec41-6934-3067-ab68-787ce5e426be | -4.66075 | -49.53473 | 2024-10-04 01:11:00 | TERRA_M-M | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 13.4 |
| 010016b6-b786-37c1-89dd-f0917629721e | -4.38614 | -50.43116 | 2024-10-04 01:11:00 | TERRA_M-M | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| d27af299-b40e-3f46-bce3-ae26a72c29e3 | -3.55185 | -50.85985 | 2024-10-04 01:11:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 11.1 |
| 12f7fd87-1472-39c7-80cc-43ec3003d3f5 | -3.54319 | -50.85739 | 2024-10-04 01:11:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 11.2 |
| 95021c43-c83e-34fc-9cf3-b0e8e5c6b69b | -3.5 | -50.81535 | 2024-10-04 01:11:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| c104c013-20f4-3948-ad06-2084fea0cffc | -3.49867 | -50.80591 | 2024-10-04 01:11:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 28.7 |
| ddd0821f-0fff-3fdb-95cd-153766aa6cf7 | -3.49086 | -50.81668 | 2024-10-04 01:11:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| ddb45c4d-616f-3176-949a-983ae5e12df5 | -3.48952 | -50.80723 | 2024-10-04 01:11:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 30.6 |
| 6cd67c1e-b193-3662-a963-e24b54ef2a18 | -3.3208 | -50.78534 | 2024-10-04 01:11:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 6d7159bf-0ef2-3461-8eb8-ecb88001b0b5 | -3.29976 | -50.76894 | 2024-10-04 01:11:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| dfaec12d-b877-3b20-ac16-e583f0623c6d | -3.29841 | -50.75941 | 2024-10-04 01:11:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 18.1 |
| 1133f401-4514-381a-81cf-f38f2a61cfe3 | -3.28922 | -50.76073 | 2024-10-04 01:11:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 12.4 |
| 41078eb1-fd49-360a-8eb4-18c490bdcbac | -4.09613 | -51.12098 | 2024-10-04 01:11:00 | TERRA_M-M | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| a285bc44-f597-385f-8cdb-d8f49cdd8778 | -3.90562 | -51.27225 | 2024-10-04 01:11:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 8943fdca-5723-35f7-84dc-927c8c762635 | -3.83181 | -52.18664 | 2024-10-04 01:11:00 | TERRA_M-M | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 25.1 |
| e83c75df-20e7-37cb-82af-00a773e7c97f | -3.83058 | -52.17783 | 2024-10-04 01:11:00 | TERRA_M-M | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 15.3 |
| 75ec15df-d819-347f-9100-05768557516c | -3.80959 | -51.18064 | 2024-10-04 01:11:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 11.2 |
| 09bb42ed-52f4-3c78-ad78-a3fcc577f0fa | -3.79523 | -51.66803 | 2024-10-04 01:11:00 | TERRA_M-M | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 9.8 |
| ae37c8b5-d018-3e52-910e-b1f6fedadd44 | -3.79398 | -51.6591 | 2024-10-04 01:11:00 | TERRA_M-M | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 366d1a72-7bf5-3509-9d10-bad53579092e | -3.77614 | -51.86754 | 2024-10-04 01:11:00 | TERRA_M-M | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 6810d909-46a3-3857-8868-31f61af50ff2 | -3.70121 | -52.05552 | 2024-10-04 01:11:00 | TERRA_M-M | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 13.2 |
| f96ed1f4-4ab5-3701-ae2b-2a0a3783006e | -3.53833 | -52.14489 | 2024-10-04 01:11:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| a70d11d3-ce10-38e7-b68e-b2485bc33238 | -2.95601 | -52.79029 | 2024-10-04 01:11:00 | TERRA_M-M | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 12.1 |
| 163572c6-5831-3dbd-9a3b-2cadbab416d9 | -2.95478 | -52.78151 | 2024-10-04 01:11:00 | TERRA_M-M | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 27.8 |
| e0200a46-8084-3ef3-a820-6fd82d6d71c1 | -2.94718 | -52.79153 | 2024-10-04 01:11:00 | TERRA_M-M | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 15.4 |
| 563b0fa4-b79e-3405-b0f1-caeb91e6d1cc | -2.94595 | -52.78275 | 2024-10-04 01:11:00 | TERRA_M-M | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 16.2 |
| d883461e-1468-3b64-a0a4-557789137dc6 | -3.82487 | -52.34638 | 2024-10-04 01:11:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 10.2 |
| b75b8d00-e0d3-3e88-9f02-d56df6116937 | -3.76063 | -52.33754 | 2024-10-04 01:11:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 7dd19278-10fb-3535-9d93-6b3c5e0feb33 | -2.05144 | -54.37054 | 2024-10-04 01:11:00 | TERRA_M-M | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| bc827ebb-3b4a-3606-8934-7d98b347e06d | -1.75804 | -54.44878 | 2024-10-04 01:11:00 | TERRA_M-M | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 4b0f4ae0-bd40-3ba0-9b86-a180df3a67fb | -3.4039 | -42.28965 | 2024-10-04 01:11:00 | TERRA_M-M | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Cerrado | 215.0 |
| 0f8ccb87-4b91-327e-87de-ec86d595cc0d | -3.40179 | -42.29509 | 2024-10-04 01:11:00 | TERRA_M-M | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Cerrado | 170.0 |
| 521ce46c-cdd8-3a82-8633-92334bb3f9c9 | -4.46701 | -42.87991 | 2024-10-04 01:11:00 | TERRA_M-M | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 46.1 |
| 4b99af27-40bc-38f9-84a4-330d10b98180 | -5.54698 | -42.77317 | 2024-10-04 01:11:00 | TERRA_M-M | CURRALINHOS | PIAUÍ | Brasil | 2203255 | 22 | 33 | nan | nan | nan | Caatinga | 23.3 |
| a93912c4-bca3-3ec7-a8fc-d891f4438bf0 | -5.53898 | -42.78144 | 2024-10-04 01:11:00 | TERRA_M-M | CURRALINHOS | PIAUÍ | Brasil | 2203255 | 22 | 33 | nan | nan | nan | Caatinga | 31.9 |
| 264c7ce2-1d5f-3074-b606-a8bceae9fc5b | -5.31964 | -42.96342 | 2024-10-04 01:11:00 | TERRA_M-M | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Caatinga | 23.2 |
| 02399efa-6232-3815-92eb-e71daefde03a | -5.31058 | -42.97029 | 2024-10-04 01:11:00 | TERRA_M-M | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 28.3 |
| 52c58a35-f82b-3950-b459-49c3746baf8c | -3.42935 | -43.35595 | 2024-10-04 01:11:00 | TERRA_M-M | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 21.2 |
| 656448be-5695-3891-ab26-9150fa17e0c4 | -3.26869 | -43.1264 | 2024-10-04 01:11:00 | TERRA_M-M | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 24.3 |
| 2e1cab29-ba0f-334d-bbdd-f25ddf0a82f2 | -3.26464 | -43.15518 | 2024-10-04 01:11:00 | TERRA_M-M | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 42.9 |
| 231371a8-d874-3058-82e3-66ae0e6be57a | -3.25933 | -43.12078 | 2024-10-04 01:11:00 | TERRA_M-M | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 25.3 |
| 82b4ca8a-5add-38ff-9184-d75d95aab6a3 | -4.93113 | -43.77731 | 2024-10-04 01:11:00 | TERRA_M-M | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 25.1 |
| 20220944-650a-30ed-a8e5-5001da66f17b | -4.54095 | -43.31225 | 2024-10-04 01:11:00 | TERRA_M-M | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 126.1 |
| 14ac94a1-9e0e-3c60-b32e-1c409fafbb06 | -4.53526 | -43.30635 | 2024-10-04 01:11:00 | TERRA_M-M | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 162.9 |
| 926e2c9c-6c9e-32ec-9f78-98c99aedcf2b | -4.52529 | -43.31469 | 2024-10-04 01:11:00 | TERRA_M-M | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 26.1 |
| 781009c5-d973-3222-aa74-96cf17fff6d6 | -5.89293 | -43.86825 | 2024-10-04 01:11:00 | TERRA_M-M | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 17.6 |
| d0c05d1d-c431-3cc7-8f20-cf9d5bbcc1de | -5.8922 | -43.87523 | 2024-10-04 01:11:00 | TERRA_M-M | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 23.6 |
| 53d3a4e9-5a76-3d2a-9ca4-0fe92776d0e5 | -6.07275 | -44.63241 | 2024-10-04 01:11:00 | TERRA_M-M | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 19.6 |
| feef2ace-0bc4-3df6-ba64-c1c7ad676dad | -6.05901 | -44.63456 | 2024-10-04 01:11:00 | TERRA_M-M | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 46.9 |
| f9d68e3b-20a7-31ae-992a-0a51b6292b34 | -5.82591 | -44.13318 | 2024-10-04 01:11:00 | TERRA_M-M | JATOBÁ | MARANHÃO | Brasil | 2105450 | 21 | 33 | nan | nan | nan | Cerrado | 194.5 |
| f00f0eda-41e8-340f-baa4-fc871318ac8c | -5.82184 | -44.10699 | 2024-10-04 01:11:00 | TERRA_M-M | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 20.0 |
| 77e08cfc-381b-35cb-b0f6-4a3ac5c732f8 | -4.69147 | -45.88779 | 2024-10-04 01:11:00 | TERRA_M-M | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 45.6 |
| defe7306-64a4-3e90-a633-2a2c48ee003f | -4.68847 | -45.86807 | 2024-10-04 01:11:00 | TERRA_M-M | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 25.0 |
| f5e80317-12ad-3572-8417-6fd80d666010 | -4.68171 | -45.90905 | 2024-10-04 01:11:00 | TERRA_M-M | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 15.1 |
| adb6cc69-8c47-3d71-b950-16c3276e0567 | -4.6789 | -45.89498 | 2024-10-04 01:11:00 | TERRA_M-M | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 65.6 |
| e6916eec-17f5-3fee-8b68-b3245b5a0ab0 | -4.6787 | -45.88942 | 2024-10-04 01:11:00 | TERRA_M-M | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 183.4 |
| 04f1339a-45a7-3359-bdc1-86d74ce87463 | -4.67606 | -45.87549 | 2024-10-04 01:11:00 | TERRA_M-M | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 223.8 |
| cb366c4f-6793-3cbe-8e35-168246531756 | -4.67569 | -45.8698 | 2024-10-04 01:11:00 | TERRA_M-M | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 184.9 |
| b2cdb0f1-7583-3f5c-9c49-321273feb2d3 | -4.60437 | -45.74519 | 2024-10-04 01:11:00 | TERRA_M-M | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 25.5 |
| c4068eab-70d1-3776-8c32-0c7a3a848cfe | -4.407 | -45.38081 | 2024-10-04 01:11:00 | TERRA_M-M | VITORINO FREIRE | MARANHÃO | Brasil | 2113009 | 21 | 33 | nan | nan | nan | Amazônia | 12.8 |
| 6901bb34-b212-3ef6-b8d3-b5be35dd902e | -5.96739 | -45.39415 | 2024-10-04 01:11:00 | TERRA_M-M | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 62.1 |
| cf9a7922-a61a-332d-a812-d614471d94dc | -5.96618 | -45.3802 | 2024-10-04 01:11:00 | TERRA_M-M | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 89.7 |
| cdb49376-6cb1-312a-92d7-20c129fb8e00 | -5.9642 | -45.37386 | 2024-10-04 01:11:00 | TERRA_M-M | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 52.3 |
| c6dfc561-784f-3a9e-90b6-b53970314d4e | -5.79046 | -45.09161 | 2024-10-04 01:11:00 | TERRA_M-M | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 53.8 |
| ca5cebb7-1af1-301b-80a9-7f24ec0d6dcb | -3.31927 | -46.99131 | 2024-10-04 01:11:00 | TERRA_M-M | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 23.7 |
| 8c22f84c-a502-303c-ab09-0fc97c190266 | -2.62713 | -46.91095 | 2024-10-04 01:11:00 | TERRA_M-M | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 13.8 |
| 9a4379a1-0956-371b-905b-1063d49e6986 | -2.62308 | -46.91715 | 2024-10-04 01:11:00 | TERRA_M-M | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 15.5 |
| a53f5ad1-bd28-3dce-a264-80bf0414ea42 | -4.17248 | -46.37409 | 2024-10-04 01:11:00 | TERRA_M-M | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 10.6 |
| 0595962a-1352-324d-af7e-e7a957298908 | -5.60018 | -47.96973 | 2024-10-04 01:11:00 | TERRA_M-M | ARAGUATINS | TOCANTINS | Brasil | 1702208 | 17 | 33 | nan | nan | nan | Cerrado | 17.5 |
| 61be40a1-78ce-386d-9104-f0b73383cb7b | -5.59828 | -47.95667 | 2024-10-04 01:11:00 | TERRA_M-M | ARAGUATINS | TOCANTINS | Brasil | 1702208 | 17 | 33 | nan | nan | nan | Cerrado | 27.1 |
| 7ef75b25-6572-320a-a18e-842254580eda | -5.46763 | -47.3721 | 2024-10-04 01:11:00 | TERRA_M-M | SENADOR LA ROCQUE | MARANHÃO | Brasil | 2111763 | 21 | 33 | nan | nan | nan | Cerrado | 9.6 |
| 3ad559ab-eaf9-3b3a-a561-d16d48f35aaf | -5.31481 | -47.27439 | 2024-10-04 01:11:00 | TERRA_M-M | JOÃO LISBOA | MARANHÃO | Brasil | 2105500 | 21 | 33 | nan | nan | nan | Amazônia | 12.4 |
| 56df6d78-2168-341d-877f-14105c684aca | -5.31265 | -47.25964 | 2024-10-04 01:11:00 | TERRA_M-M | JOÃO LISBOA | MARANHÃO | Brasil | 2105500 | 21 | 33 | nan | nan | nan | Amazônia | 14.3 |
| 4b0b1473-d885-310d-84ee-6282adf02cd1 | -5.28763 | -47.3235 | 2024-10-04 01:11:00 | TERRA_M-M | JOÃO LISBOA | MARANHÃO | Brasil | 2105500 | 21 | 33 | nan | nan | nan | Amazônia | 8.0 |
| 5f12a974-d7ad-371b-8209-611cf1f5fecc | 3.2333 | -51.20271 | 2024-10-04 01:13:00 | TERRA_M-M | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 13.5 |
| a8e7a280-39e5-3f6d-b314-57c1a167dd14 | 3.23187 | -51.21332 | 2024-10-04 01:13:00 | TERRA_M-M | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 5.6 |
| e28e888b-14b8-37ec-8c93-3f4e349245f5 | -3.404 | -42.2858 | 2024-10-04 01:15:25 | GOES-16 | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Cerrado | 100.2 |
| 7ac8333e-3db6-39b8-82b2-a1fe07cf2fdc | -3.4227 | -42.2849 | 2024-10-04 01:15:25 | GOES-16 | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Cerrado | 79.1 |
| 94cd0900-80c3-3b79-bd06-dde169033140 | -3.4915 | -50.8004 | 2024-10-04 01:15:26 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 63.4 |
| d775d5d4-655f-3080-9f21-f21a7e068845 | -4.0949 | -48.4894 | 2024-10-04 01:15:29 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 76.0 |
| 60578e35-db19-3204-af71-5c0457dcb9dd | -4.5375 | -43.304 | 2024-10-04 01:15:31 | GOES-16 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 117.5 |
| a653a17f-da9e-3361-b02b-244a2d0006a1 | -5.5033 | -48.8046 | 2024-10-04 01:15:37 | GOES-16 | SÃO DOMINGOS DO ARAGUAIA | PARÁ | Brasil | 1507151 | 15 | 33 | nan | nan | nan | Amazônia | 66.4 |
| f84033a3-c2db-349a-a2ef-309cdda51dae | -5.5218 | -48.8035 | 2024-10-04 01:15:37 | GOES-16 | SÃO DOMINGOS DO ARAGUAIA | PARÁ | Brasil | 1507151 | 15 | 33 | nan | nan | nan | Amazônia | 52.6 |
| f00ba102-5cfe-3833-b983-af45a60ce608 | -5.8214 | -44.1426 | 2024-10-04 01:15:39 | GOES-16 | JATOBÁ | MARANHÃO | Brasil | 2105450 | 21 | 33 | nan | nan | nan | Cerrado | 86.7 |
| d354053b-09b6-35ff-979e-ab65ccacabd4 | -5.8216 | -44.1196 | 2024-10-04 01:15:39 | GOES-16 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 117.3 |


[Clique aqui para ver as próximas entradas](README30.md)
