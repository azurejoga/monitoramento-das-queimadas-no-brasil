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

## Dados Diários - Página 7

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 0cffa988-383d-3109-b59b-7313de231082 | -2.64178 | -44.64486 | 2025-09-16 04:00:00 | NOAA-21 | BACURITUBA | MARANHÃO | Brasil | 2101350 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 9cba02fe-b64b-39b7-b41e-451fec22fb9b | -3.07712 | -48.81407 | 2025-09-16 04:00:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 001cfa4e-2751-3da3-bd94-643bb685f5b1 | -3.81236 | -41.55636 | 2025-09-16 04:00:00 | NOAA-21 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 5.2 |
| 140a4dc5-d039-3421-a68c-f39c87c3127e | -3.81225 | -41.57938 | 2025-09-16 04:00:00 | NOAA-21 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 9f74c64a-d644-3c45-bc6a-4fcd98ed88c1 | -5.07442 | -41.16948 | 2025-09-16 04:00:00 | NOAA-21 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| 95ab62db-5abe-3c55-ba54-629f190fab12 | -3.21845 | -47.13026 | 2025-09-16 04:00:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 25.2 |
| 37d9ac00-a36e-3f99-b9e8-fa14f37dba9d | -3.89649 | -42.51671 | 2025-09-16 04:00:00 | NOAA-21 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 918f7c4a-b746-30da-b243-4181033f6c6c | -3.00103 | -47.45406 | 2025-09-16 04:00:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 799bdac6-c0cc-3570-bdd7-6fad2b70a903 | -3.81285 | -41.57562 | 2025-09-16 04:00:00 | NOAA-21 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| bbf0a991-0b34-369c-bc5c-fd5c61cf830e | -4.01383 | -43.23747 | 2025-09-16 04:00:00 | NOAA-21 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| dcc1b84e-413e-306c-9da6-921508725dd8 | -3.42486 | -43.14925 | 2025-09-16 04:00:00 | NOAA-21 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| c927bf4d-3cce-343c-8c36-c21428218825 | -5.07498 | -41.1659 | 2025-09-16 04:00:00 | NOAA-21 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| cd679d75-0293-3091-a653-bc7ae86c418a | -3.81628 | -41.57616 | 2025-09-16 04:00:00 | NOAA-21 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 34177815-f98a-33d9-a667-78e537b779c7 | -3.07746 | -48.81825 | 2025-09-16 04:00:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| db9f3cc4-75c7-3b2c-81bb-721833607144 | -3.13972 | -44.42949 | 2025-09-16 04:00:00 | NOAA-21 | SANTA RITA | MARANHÃO | Brasil | 2110203 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 589f3dfa-b349-336b-9346-d8f9f554b8d7 | -3.81462 | -41.56437 | 2025-09-16 04:00:00 | NOAA-21 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 5.5 |
| 42233372-f0c0-310f-8e09-24e702f39898 | -4.15902 | -46.79124 | 2025-09-16 04:00:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 553565ee-ebfa-372f-9b25-6920a29d06be | -3.74091 | -49.05072 | 2025-09-16 04:00:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 10.6 |
| 7cf780c6-bc8a-37bd-b471-4f152b81be66 | -3.08257 | -48.81499 | 2025-09-16 04:00:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| daf79f86-a4d5-335f-a08f-1635bb56a4fd | -3.81119 | -41.56383 | 2025-09-16 04:00:00 | NOAA-21 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 5.5 |
| 63bd9565-0e1a-3d83-98ac-8de08c523000 | -3.81344 | -41.57186 | 2025-09-16 04:00:00 | NOAA-21 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 37751d96-fb84-3dfe-89b2-4ebcb0c849a1 | -3.07654 | -48.8176 | 2025-09-16 04:00:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 7aadf563-5029-3331-b759-0d8c645874ee | -3.73602 | -49.0463 | 2025-09-16 04:00:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 68e106fc-7980-3b5d-a33e-602cad6887c4 | -4.70926 | -41.32614 | 2025-09-16 04:00:00 | NOAA-21 | MILTON BRANDÃO | PIAUÍ | Brasil | 2206357 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 3b4bd971-2a7e-3114-ba3a-10d8b6c287dc | -3.83394 | -44.11131 | 2025-09-16 04:00:00 | NOAA-21 | PIRAPEMAS | MARANHÃO | Brasil | 2108801 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 6d9eeac6-61b4-38dd-a1b1-5866edee0979 | -3.21932 | -47.12495 | 2025-09-16 04:00:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 25.2 |
| 68e58ad6-7579-3588-b312-90be8ae4e5c4 | -4.90909 | -38.00363 | 2025-09-16 04:00:00 | NOAA-21 | RUSSAS | CEARÁ | Brasil | 2311801 | 23 | 33 | nan | nan | nan | Caatinga | 2.4 |
| cc2ac4aa-e69f-361c-8e5c-79cf0fa3b1fd | -3.21359 | -47.12948 | 2025-09-16 04:00:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| e2907a68-b9a3-3a2a-b5bd-c54fb6581cab | -3.8277 | -44.10007 | 2025-09-16 04:00:00 | NOAA-21 | PIRAPEMAS | MARANHÃO | Brasil | 2108801 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| dd02c702-7fb6-3d23-8745-55c8d4acbe95 | -3.97298 | -43.24176 | 2025-09-16 04:00:00 | NOAA-21 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 3dc2d0d0-e04b-3611-a248-b814ef1cde28 | -3.8158 | -41.5569 | 2025-09-16 04:00:00 | NOAA-21 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 5.2 |
| 48502c2e-e582-37fa-922c-f9da957afa41 | -3.83555 | -44.10128 | 2025-09-16 04:00:00 | NOAA-21 | PIRAPEMAS | MARANHÃO | Brasil | 2108801 | 21 | 33 | nan | nan | nan | Cerrado | 11.6 |
| da3218f3-771e-3882-af22-446760112f79 | -3.40362 | -46.9022 | 2025-09-16 04:00:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 1d7e3461-689b-3bb1-807e-86bd16fa3360 | -3.21445 | -47.12422 | 2025-09-16 04:00:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| b5a29eef-ceb8-308c-9f83-409677c70574 | -3.42788 | -43.15423 | 2025-09-16 04:00:00 | NOAA-21 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 6df00c76-26c3-3eb9-b3c1-51e57915a61d | -3.8917 | -47.60616 | 2025-09-16 04:00:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c662e78d-34dc-3266-af8a-28988cdd28e4 | -5.07385 | -41.17309 | 2025-09-16 04:00:00 | NOAA-21 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 1d52ccdf-2663-3a6f-a788-8251e89e0f73 | -3.99297 | -43.23576 | 2025-09-16 04:00:00 | NOAA-21 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 6ddb9e08-51b4-3dd8-92c6-b974d5e1a386 | -4.06043 | -46.94069 | 2025-09-16 04:00:00 | NOAA-21 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 16.2 |
| 963204e0-1f7b-377c-88fa-a3c1e96be6b0 | -3.81 | -41.57132 | 2025-09-16 04:00:00 | NOAA-21 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 8a1ae755-c2c0-35bb-bc11-c96f9cd9e1a5 | -3.82529 | -44.11506 | 2025-09-16 04:00:00 | NOAA-21 | PIRAPEMAS | MARANHÃO | Brasil | 2108801 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| b836e3ba-7a38-34f2-9609-7a7920d7da8e | -3.81639 | -41.55316 | 2025-09-16 04:00:00 | NOAA-21 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 5.2 |
| 5fc1d0fd-1127-31af-996d-2c51a4889e5e | -5.09461 | -41.15054 | 2025-09-16 04:00:00 | NOAA-21 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| c5267c6a-4bca-3045-83ad-387aa4dd84d4 | -2.25863 | -47.84842 | 2025-09-16 04:00:00 | NOAA-21 | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 0aaf5d7c-5589-34e8-86de-7c0f00506aea | -3.81521 | -41.56063 | 2025-09-16 04:00:00 | NOAA-21 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 5.5 |
| b00a037a-5857-346b-8c8d-c058fc205674 | -3.42416 | -43.15366 | 2025-09-16 04:00:00 | NOAA-21 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 09f0cf7e-c4db-3834-8bf9-1ecb18d36254 | -3.24148 | -43.2244 | 2025-09-16 04:00:00 | NOAA-21 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 78d64515-3f1d-3f99-bf9d-60534805e5aa | -4.80116 | -42.73163 | 2025-09-16 04:00:00 | NOAA-21 | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 6119d517-efb9-3f76-b7f4-541d3a974f35 | -3.82137 | -44.11443 | 2025-09-16 04:00:00 | NOAA-21 | PIRAPEMAS | MARANHÃO | Brasil | 2108801 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 8b2dbaf1-a465-33df-843f-15685770ccb4 | -2.25913 | -47.84533 | 2025-09-16 04:00:00 | NOAA-21 | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 8af66c9f-5b0b-3334-a13a-df3c21ba2b8c | -3.83475 | -44.1063 | 2025-09-16 04:00:00 | NOAA-21 | PIRAPEMAS | MARANHÃO | Brasil | 2108801 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 9d2f7c1e-2923-3e85-8313-080f7ea4ce47 | -4.59745 | -43.32249 | 2025-09-16 04:00:00 | NOAA-21 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 73c53bfd-3c9b-3e30-b02a-bc75c9912f8d | -3.14029 | -44.42593 | 2025-09-16 04:00:00 | NOAA-21 | SANTA RITA | MARANHÃO | Brasil | 2110203 | 21 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 0bcde218-65f0-30a8-a7a6-dd2946c1a96e | -3.74214 | -49.04348 | 2025-09-16 04:00:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| dd7c00c1-c2ca-34bc-8a21-5ba3e89b507d | -2.30243 | -48.14501 | 2025-09-16 04:00:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2b7164d7-18a7-33b0-a37a-7a7fc27b3a82 | -2.57377 | -48.39567 | 2025-09-16 04:00:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| a4bbbe5b-4258-3f13-b599-f02de24de444 | -4.01083 | -43.23251 | 2025-09-16 04:00:00 | NOAA-21 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| ee92f1bf-ae73-3d2c-b1e9-a5d42eed5a85 | -4.06208 | -46.93845 | 2025-09-16 04:00:00 | NOAA-21 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 28.1 |
| 1b1024d6-4a2e-3528-94f5-c3a6ebdfa0b4 | -3.07807 | -48.81472 | 2025-09-16 04:00:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 39889c40-12d9-3f99-bdd0-f93c525d5208 | -3.84339 | -44.1025 | 2025-09-16 04:00:00 | NOAA-21 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 24787cb4-a8cc-3812-8766-572c9e7ebeca | -2.64643 | -48.05091 | 2025-09-16 04:00:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 1f4eb683-f889-30df-ac23-590f317fd800 | -3.80941 | -41.57508 | 2025-09-16 04:00:00 | NOAA-21 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 03a1678a-8c9c-3ae6-9ed4-1bbe45c83b77 | -3.24285 | -43.22347 | 2025-09-16 04:00:00 | NOAA-21 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 5efca069-9ae1-3655-a494-b2967e018af2 | -3.89905 | -42.51596 | 2025-09-16 04:00:00 | NOAA-21 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 0e97851f-eabb-3e42-ab37-24091837688c | -2.29715 | -48.14416 | 2025-09-16 04:00:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 78944295-87a3-3e03-9e65-799a37d000ac | -5.09628 | -41.16182 | 2025-09-16 04:00:00 | NOAA-21 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| cd33da8d-f96f-3ee9-b4e2-a98a303384c8 | -4.45292 | -38.44383 | 2025-09-16 04:00:00 | NOAA-21 | OCARA | CEARÁ | Brasil | 2309458 | 23 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 53594c54-01b1-316a-a265-8193bc2554e6 | -8.12349 | -48.26775 | 2025-09-16 04:02:00 | NOAA-21 | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 5ca37b4c-1f45-322c-8ba2-8a2dcb8cb259 | -7.5382 | -44.02187 | 2025-09-16 04:02:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 761b1bae-de52-3e6d-aa58-d32093341f9d | -6.88158 | -46.06549 | 2025-09-16 04:02:00 | NOAA-21 | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 3ce59eba-ec85-3f4f-9673-523721c2d77e | -11.24281 | -49.94563 | 2025-09-16 04:02:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 6.6 |
| b707248b-2f3c-353f-835d-5b06d29d7186 | -11.13696 | -45.34107 | 2025-09-16 04:02:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 0143055b-f870-34f7-8b44-140d69d7380f | -11.43353 | -46.94077 | 2025-09-16 04:02:00 | NOAA-21 | PORTO ALEGRE DO TOCANTINS | TOCANTINS | Brasil | 1718006 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 95733767-d64d-36a6-982c-843ff005702f | -6.12725 | -43.37489 | 2025-09-16 04:02:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| fa421305-2b56-363a-82a1-d1413448e7fb | -6.17689 | -46.81174 | 2025-09-16 04:02:00 | NOAA-21 | LAJEADO NOVO | MARANHÃO | Brasil | 2105989 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| af9ab281-a6f1-3992-8ad3-9b68f0e8bf76 | -12.26817 | -45.29845 | 2025-09-16 04:02:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 01d69bac-7312-31bb-8054-bcf1227ef215 | -5.47569 | -45.34775 | 2025-09-16 04:02:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d640780a-e1ed-3049-8fac-5a10ac0bed35 | -10.71744 | -44.74756 | 2025-09-16 04:02:00 | NOAA-21 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 9.5 |
| 8f5a33ad-9a8c-3330-b1f4-42f0430551cd | -10.7163 | -46.50392 | 2025-09-16 04:02:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 29.0 |
| 02abe610-cc1a-332f-ae92-3f47ceb6e73d | -7.51311 | -44.66642 | 2025-09-16 04:02:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 145b7710-e013-38ab-a7cf-78540fad8e63 | -10.47684 | -45.17223 | 2025-09-16 04:02:00 | NOAA-21 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 0a6a8ab8-02ec-39c8-b5f5-b8a1df0ca8dc | -9.47562 | -54.44322 | 2025-09-16 04:02:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| d5f09e38-6a38-3ac0-8422-177a37f9da8f | -11.20939 | -49.31945 | 2025-09-16 04:02:00 | NOAA-21 | CRIXÁS DO TOCANTINS | TOCANTINS | Brasil | 1706258 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c6de36fb-3333-3d8b-916d-94cef0637f84 | -5.67519 | -43.50245 | 2025-09-16 04:02:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| cc1a519a-6643-3c10-b057-d8c80c6ec0eb | -7.67336 | -44.47588 | 2025-09-16 04:02:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 15911b29-8897-31a5-9d30-cd1c303d90fa | -10.9624 | -49.56989 | 2025-09-16 04:02:00 | NOAA-21 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e8a91674-7628-3078-b132-8c7eb3262069 | -10.76789 | -44.71897 | 2025-09-16 04:02:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 450e2701-7539-3ef1-a35c-8daeef024fa1 | -8.9122 | -45.52665 | 2025-09-16 04:02:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 18067509-ea9f-35ba-9e9c-d80e18f444dc | -7.0633 | -44.16862 | 2025-09-16 04:02:00 | NOAA-21 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 7e00ae9a-3895-3553-bdb2-8a23802ea060 | -11.43019 | -46.92897 | 2025-09-16 04:02:00 | NOAA-21 | PORTO ALEGRE DO TOCANTINS | TOCANTINS | Brasil | 1718006 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 79361ad9-3569-3c80-af01-236976110ef8 | -9.04707 | -44.84152 | 2025-09-16 04:02:00 | NOAA-21 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 2b7a258b-dd88-3376-bbe8-06841d4192e7 | -4.89514 | -49.92501 | 2025-09-16 04:02:00 | NOAA-21 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 637100d5-23e2-3ce7-936e-cdadfcd0ae02 | -7.72001 | -45.30531 | 2025-09-16 04:02:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 5bcca00f-bea5-3351-9fb2-41350025d955 | -10.63891 | -48.73589 | 2025-09-16 04:02:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 26902eb9-79f1-3dc6-a8b9-bb631c815d62 | -6.82423 | -47.83497 | 2025-09-16 04:02:00 | NOAA-21 | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 80522bb6-3d60-370b-8404-7a5f1ee1f2e1 | -10.67128 | -48.69279 | 2025-09-16 04:02:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 58811dad-24cb-35c6-97ef-49fc7fdbee76 | -8.66884 | -46.36827 | 2025-09-16 04:02:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| d375f397-3a74-3140-b251-53c49b9e736d | -11.12014 | -45.34805 | 2025-09-16 04:02:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 54c643b3-64f7-38f2-a5de-fd6e26aa3e65 | -7.44591 | -46.17036 | 2025-09-16 04:02:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| b818b2ef-dae6-333e-bd76-581f5e4ea1cd | -9.0513 | -47.0174 | 2025-09-16 04:02:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |


[Clique aqui para ver as próximas entradas](README8.md)
