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

## Dados Diários - Página 90

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 560b4f7f-8ace-3066-990c-b25b8ba07485 | -9.2258 | -48.5782 | 2025-10-16 13:10:00 | GOES-19 | MIRANORTE | TOCANTINS | Brasil | 1713304 | 17 | 33 | nan | nan | nan | Cerrado | 61.6 |
| 6b57a2cf-2e27-3d63-a058-7bd259c49995 | 1.0765 | -51.1026 | 2025-10-16 13:10:00 | GOES-19 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 112.7 |
| f910e0ba-9625-3ce8-8d77-4c6b1373bdae | -13.9127 | -45.5808 | 2025-10-16 13:10:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 219.6 |
| 98608b59-e215-357b-b6e5-af58fac0c523 | -10.6172 | -45.2282 | 2025-10-16 13:10:00 | GOES-19 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 136.2 |
| f3d8f2da-11de-3759-bb06-9f089a8f7de0 | -13.0743 | -46.9717 | 2025-10-16 13:10:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 65.8 |
| dcf9c37b-8871-32e2-a056-8554f92e73a0 | -10.5144 | -43.3579 | 2025-10-16 13:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 72.7 |
| 17fce732-bf34-36dd-900a-fb3c77afb6e6 | -10.6024 | -47.4178 | 2025-10-16 13:10:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 123.3 |
| 46607795-2c64-3493-a239-9b1d31d4362a | -10.6543 | -45.2921 | 2025-10-16 13:10:00 | GOES-19 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 72.3 |
| 1a8b0b7c-992c-3baa-9738-11d9cd090e75 | 1.0398 | -51.0407 | 2025-10-16 13:10:00 | GOES-19 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 77.8 |
| 173660a8-44d2-35b9-b21b-a6f7fc0605cf | -12.9372 | -47.1049 | 2025-10-16 13:10:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 69.1 |
| 45222f16-3d8d-319a-b96a-c1f557895cf9 | -12.2311 | -50.3643 | 2025-10-16 13:10:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 75.8 |
| ce78fc5b-10f3-3df2-a00b-f57bf1369e61 | -12.4866 | -45.4895 | 2025-10-16 13:10:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 71.1 |
| 18413c28-4f19-39c2-b9cc-a7d48418b5b2 | -14.1343 | -51.1942 | 2025-10-16 13:10:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 91.5 |
| 0eaebe91-b9aa-3013-bd90-83d9c7976af3 | 1.8402 | -55.7034 | 2025-10-16 13:10:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 72.0 |
| 60ee2ace-70e3-3df3-86a8-0e5a0e1506f9 | -10.133 | -44.5777 | 2025-10-16 13:10:00 | GOES-19 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 75.2 |
| 88016b72-cc2b-3869-a55b-774dbb32bd24 | -10.1333 | -44.5545 | 2025-10-16 13:10:00 | GOES-19 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 129.1 |
| cdef452b-2f51-3024-adc3-2d6bb442bd67 | -10.6169 | -45.2512 | 2025-10-16 13:20:00 | GOES-19 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 105.6 |
| 0db33cbf-0f8a-3da1-8054-27098b12c46d | -10.5144 | -43.3579 | 2025-10-16 13:20:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 64.2 |
| cbbe5b4c-1d20-3dee-9964-7eed2b0648c4 | -10.6543 | -45.2921 | 2025-10-16 13:20:00 | GOES-19 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 62.0 |
| 562bf580-400d-3cf4-bf60-a2af3b6f8774 | -10.6539 | -45.3151 | 2025-10-16 13:20:00 | GOES-19 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 158.0 |
| 58170b62-29d5-37e8-b8b7-cfbfb49a91ca | 1.8402 | -55.7034 | 2025-10-16 13:20:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 80.9 |
| cb8a419d-d5f9-37c1-8662-d0fe207629e2 | -10.6734 | -45.2896 | 2025-10-16 13:20:00 | GOES-19 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 76.5 |
| 8c1155ce-ec56-3038-83ec-92ee6a6fa5a6 | 1.8401 | -55.7232 | 2025-10-16 13:20:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 75.8 |
| 6320b27c-c33d-359e-a49e-fe7b16a5aed9 | -10.1139 | -44.5801 | 2025-10-16 13:20:00 | GOES-19 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 146.4 |
| 8f149b40-30b5-35d7-83d8-a741cd83b894 | -12.9179 | -47.1078 | 2025-10-16 13:20:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 61.3 |
| 3f70690f-8ccc-3569-8c7e-9b39839c1892 | -10.673 | -45.3125 | 2025-10-16 13:20:00 | GOES-19 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 252.7 |
| cf7e5d9e-8892-3d13-8651-5d4d7ad33e2f | -10.1143 | -44.557 | 2025-10-16 13:20:00 | GOES-19 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 115.0 |
| 72dce865-6dd6-362b-a802-0321fb9e71d1 | -14.1343 | -51.1942 | 2025-10-16 13:20:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 91.2 |
| 217f29ab-33af-3ac3-b71a-2ac96d79f2da | 1.0765 | -51.1026 | 2025-10-16 13:20:00 | GOES-19 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 86.8 |
| 3e9ecc94-44a7-3959-8e69-f7287bf9691f | -12.7063 | -50.4993 | 2025-10-16 13:20:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 76.1 |
| 28484e84-030c-32b1-aed9-8b037964f526 | -9.2255 | -48.6 | 2025-10-16 13:20:00 | GOES-19 | MIRANORTE | TOCANTINS | Brasil | 1713304 | 17 | 33 | nan | nan | nan | Cerrado | 89.5 |
| c35a560e-2263-34fe-9f80-d11fdfb0c990 | -13.4605 | -47.9454 | 2025-10-16 13:20:00 | GOES-19 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 68.0 |
| 8bfa4e83-d96e-3ac3-a70d-9bac21d6e2c8 | -11.5917 | -44.0707 | 2025-10-16 13:20:00 | GOES-19 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 170.8 |
| e6f48fa5-a691-3618-8d69-9c8e41135f7e | -12.7993 | -50.6595 | 2025-10-16 13:20:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 75.6 |
| 879f69b3-c148-35d0-8f3f-245325847716 | -9.2258 | -48.5782 | 2025-10-16 13:20:00 | GOES-19 | MIRANORTE | TOCANTINS | Brasil | 1713304 | 17 | 33 | nan | nan | nan | Cerrado | 67.9 |
| 2f535088-35e8-38dd-b226-9ca943041f69 | 1.0582 | -51.0198 | 2025-10-16 13:20:00 | GOES-19 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 68.9 |
| b2fea689-96ac-3a4c-9bfd-7b4fe3a94ad1 | -13.4609 | -47.923 | 2025-10-16 13:20:00 | GOES-19 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 83.0 |
| 9ab89cda-615a-30dd-80c8-1e5eea29d4ba | -10.6214 | -47.4155 | 2025-10-16 13:20:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 73.9 |
| ddd7f477-6dbe-3446-8cb3-b9a3d245c910 | -11.572 | -44.0971 | 2025-10-16 13:20:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 74.1 |
| 9f90295b-d9ae-3aa0-8ffd-c6a8d8803318 | -11.5724 | -44.0736 | 2025-10-16 13:20:00 | GOES-19 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 174.6 |
| f2083207-63a4-345e-988b-7381a49522d2 | -10.6024 | -47.4178 | 2025-10-16 13:20:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 90.7 |
| 0b1ef597-9e4c-3714-8cbf-22e2d49c53ef | -10.1333 | -44.5545 | 2025-10-16 13:20:00 | GOES-19 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 191.7 |
| ac6ddcc5-3511-3e03-935d-796e97d6f8f8 | -11.5729 | -44.0501 | 2025-10-16 13:20:00 | GOES-19 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 134.8 |
| c6041f6e-8aba-3f59-a8d8-404373e110f9 | -13.0743 | -46.9717 | 2025-10-16 13:20:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 73.9 |
| acf49395-c265-34d0-9ba9-f7922c00f156 | -12.9905 | -47.3442 | 2025-10-16 13:20:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 74.2 |
| a284d029-46cf-3088-8fa1-feb1d1f4accd | -12.9372 | -47.1049 | 2025-10-16 13:20:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 61.3 |
| 73ee1279-8594-35b2-bbeb-e89a7ffa4884 | -11.2862 | -44.0226 | 2025-10-16 13:20:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 181.2 |
| 457e89bf-a635-3b5f-b38b-0b2ac2adfcdb | -10.6172 | -45.2282 | 2025-10-16 13:20:00 | GOES-19 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 142.3 |
| e1d8f7c1-49bd-3e9b-94e9-4776451c3a2b | -10.133 | -44.5777 | 2025-10-16 13:20:00 | GOES-19 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 212.6 |
| 80430e12-6363-3af0-b2a7-a620988a1425 | -11.5912 | -44.0942 | 2025-10-16 13:20:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 75.2 |
| 14cc94bd-3e4a-3f7f-84b9-5589c853dc21 | -13.9127 | -45.5808 | 2025-10-16 13:20:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 274.9 |
| 38504c2c-1646-34a4-8ee7-fef399521d00 | -12.9909 | -47.3217 | 2025-10-16 13:20:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 66.8 |
| c2dede47-db02-3755-b600-6e519bad8634 | -10.5331 | -43.3788 | 2025-10-16 13:30:00 | GOES-19 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 90.3 |
| ba1185f8-26bb-34be-b9aa-8f8cf214bf21 | -10.6172 | -45.2282 | 2025-10-16 13:30:00 | GOES-19 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 154.9 |
| 9c1f11ed-ce36-3329-abb9-64915fe2858c | -12.9372 | -47.1049 | 2025-10-16 13:30:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 75.8 |
| e2bec35a-9192-3d35-a62c-ac6ead98e4cf | -12.2119 | -50.3666 | 2025-10-16 13:30:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 100.9 |
| b4c0f990-0c43-36c2-808d-bbb3b839c395 | 1.8217 | -55.8023 | 2025-10-16 13:30:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 100.1 |
| 463ddf0c-c458-340e-89a8-f83126829242 | -11.5724 | -44.0736 | 2025-10-16 13:30:00 | GOES-19 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 155.0 |
| deed6dea-a202-3c4d-bc5b-f889d8d97f5d | -10.6543 | -45.2921 | 2025-10-16 13:30:00 | GOES-19 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 70.1 |
| bf05b9a5-db6a-34d4-9c6b-c44b2f3dd2ec | -12.2116 | -50.3881 | 2025-10-16 13:30:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 66.5 |
| f78dd0ef-f9ec-3919-a812-af93a2da34d3 | -10.133 | -44.5777 | 2025-10-16 13:30:00 | GOES-19 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 382.6 |
| 1cd06fde-0441-3624-8143-517c3450e8fd | -11.5729 | -44.0501 | 2025-10-16 13:30:00 | GOES-19 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 114.5 |
| 322e2bd5-ccbb-35e6-a8f9-aa05cd8f2eb3 | -13.9127 | -45.5808 | 2025-10-16 13:30:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 149.3 |
| 757adbbf-c8d3-3204-86f3-2baffa1d152a | 1.0582 | -51.0198 | 2025-10-16 13:30:00 | GOES-19 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 87.7 |
| 14d7e177-426f-3d0d-ba22-63818e2225eb | -10.673 | -45.3125 | 2025-10-16 13:30:00 | GOES-19 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 160.9 |
| 05ce64b2-1579-34e2-b3fc-67c271614dec | -13.5173 | -51.2753 | 2025-10-16 13:30:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 93.8 |
| c7bcbe45-5f5e-3ec8-b9d9-8d686911a372 | -12.7063 | -50.4993 | 2025-10-16 13:30:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 85.0 |
| 67adbeef-171f-3b4d-9865-bba5476a53e0 | -10.6024 | -47.4178 | 2025-10-16 13:30:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 138.9 |
| e54882cf-6249-3309-bb05-13ba209bf3bf | -10.1139 | -44.5801 | 2025-10-16 13:30:00 | GOES-19 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 207.5 |
| 20ee38f2-4e2f-3c98-838a-8968874e99d7 | -12.7989 | -50.681 | 2025-10-16 13:30:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 70.1 |
| acd89128-e458-3693-a4da-678d10afdfcb | -10.1143 | -44.557 | 2025-10-16 13:30:00 | GOES-19 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 198.3 |
| 2ad11f1f-ab40-3c49-b820-374d16deb45f | -12.9909 | -47.3217 | 2025-10-16 13:30:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 66.6 |
| d9bffd10-c9b7-390d-8496-2ea235bbd113 | -13.0743 | -46.9717 | 2025-10-16 13:30:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 98.3 |
| 55666320-eae4-3510-a71e-cc1d70fcb2a3 | -12.7993 | -50.6595 | 2025-10-16 13:30:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 75.7 |
| e8964456-465b-356f-b2a2-ba64120fe2c0 | 1.0398 | -51.0407 | 2025-10-16 13:30:00 | GOES-19 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 86.9 |
| 4362ca67-87f8-343e-a980-e99eecbca230 | -11.3603 | -45.2646 | 2025-10-16 13:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 73.3 |
| 7b1b296b-1067-3db8-bed4-7185c6b95bde | -12.2307 | -50.3858 | 2025-10-16 13:30:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 68.7 |
| 5dcfad2b-1f17-35be-ba0e-94fa66bff348 | -10.1326 | -44.6008 | 2025-10-16 13:30:00 | GOES-19 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 72.1 |
| 8337761e-8af9-3254-9580-cf359072e807 | -10.514 | -43.3815 | 2025-10-16 13:30:00 | GOES-19 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 54.2 |
| 466c5821-a3b3-382d-ad6d-010fdea80e1d | -9.7162 | -44.5149 | 2025-10-16 13:30:00 | GOES-19 | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 106.9 |
| 4ed2690e-9ff7-3f66-baf1-22ca61372e37 | -12.2311 | -50.3643 | 2025-10-16 13:30:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 80.7 |
| b9851c5c-b124-379f-bce4-ae838866d150 | -10.1333 | -44.5545 | 2025-10-16 13:30:00 | GOES-19 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 370.5 |
| 927acbfb-6703-3b37-8bad-75de95e6b011 | -13.4605 | -47.9454 | 2025-10-16 13:30:00 | GOES-19 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 58.8 |
| be3a3a18-d414-378c-860b-d6dbeabc5626 | -10.6169 | -45.2512 | 2025-10-16 13:30:00 | GOES-19 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 106.7 |
| e7c868b6-2056-303b-b32b-a55706b7e0ba | -11.5917 | -44.0707 | 2025-10-16 13:30:00 | GOES-19 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 221.9 |
| 0abdb002-c6cf-3a93-8249-d3312a7c13cf | -9.2255 | -48.6 | 2025-10-16 13:30:00 | GOES-19 | MIRANORTE | TOCANTINS | Brasil | 1713304 | 17 | 33 | nan | nan | nan | Cerrado | 101.5 |
| dba5e8f1-5a4d-3b75-93e3-e9ce91278f94 | -13.5366 | -51.2728 | 2025-10-16 13:30:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 90.5 |
| 7e88c48e-4d9a-3be2-8d3e-7d8c97f709f1 | -12.4866 | -45.4895 | 2025-10-16 13:30:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 98.9 |
| d687708c-b110-3e33-b93c-2cd465d3190d | -11.572 | -44.0971 | 2025-10-16 13:30:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 70.6 |
| 085e915f-bec5-39ed-8b73-61f98f737ab3 | -10.6539 | -45.3151 | 2025-10-16 13:30:00 | GOES-19 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 134.7 |
| 1511f941-e9c5-3434-9cca-808c874d7420 | 1.0582 | -51.0405 | 2025-10-16 13:30:00 | GOES-19 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 74.0 |
| f4ce2686-aa18-3136-9e9a-ee0982c2fed4 | -9.2258 | -48.5782 | 2025-10-16 13:30:00 | GOES-19 | MIRANORTE | TOCANTINS | Brasil | 1713304 | 17 | 33 | nan | nan | nan | Cerrado | 68.0 |
| 69fb1a07-6a63-306d-b723-0098464dfcaf | -10.6734 | -45.2896 | 2025-10-16 13:30:00 | GOES-19 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 87.6 |
| 63b8cf7e-2924-3bd2-bacd-7073e885bb31 | -11.2862 | -44.0226 | 2025-10-16 13:30:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 244.8 |
| ac956ede-c450-3e0e-8f88-9c471b334c01 | -12.2498 | -50.3835 | 2025-10-16 13:30:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 71.1 |
| 511cc577-2474-311f-9fe2-f0355deabdc4 | -12.7989 | -50.681 | 2025-10-16 13:40:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 71.7 |
| 3b64b576-f125-343d-9bb7-7aa42586dd37 | -11.3603 | -45.2646 | 2025-10-16 13:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 126.9 |
| f14cbeb3-c636-3675-869b-1cbf323598ac | 1.0398 | -51.0407 | 2025-10-16 13:40:00 | GOES-19 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 80.4 |
| de1a2527-6cf7-3d0e-8961-8cb253915454 | -10.5144 | -43.3579 | 2025-10-16 13:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 100.2 |
| e059d278-4570-3589-a75d-233adb448f63 | -11.3224 | -45.247 | 2025-10-16 13:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 86.2 |


[Clique aqui para ver as próximas entradas](README91.md)
