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

## Dados Diários - Página 6

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| a1199fc3-399e-3dc7-97e5-cb283a090e2b | -3.50769 | -49.95842 | 2025-11-01 00:16:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 32.8 |
| f21e5191-db50-3e5a-b4da-cac36caaff00 | -3.19393 | -45.79596 | 2025-11-01 00:16:00 | TERRA_M-M | ARAGUANÃ | MARANHÃO | Brasil | 2100873 | 21 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 3b4b3d69-0f60-3b68-8377-1285a986653d | -4.17487 | -47.64614 | 2025-11-01 00:16:00 | TERRA_M-M | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 22.3 |
| 7c2f7167-0bd0-3976-afb3-67554a9591a0 | -2.21526 | -46.1795 | 2025-11-01 00:16:00 | TERRA_M-M | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 13.9 |
| f2923d79-051a-3e14-8914-313c903cb75c | -4.42472 | -47.59354 | 2025-11-01 00:16:00 | TERRA_M-M | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 10.7 |
| 6becd382-b8d3-3d3f-a622-8d63603b2caa | -4.49475 | -49.86935 | 2025-11-01 00:16:00 | TERRA_M-M | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 21.0 |
| 9baabdb4-31c3-3544-98e0-fe6d1671159b | -2.21648 | -46.18829 | 2025-11-01 00:16:00 | TERRA_M-M | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 18.7 |
| 8081df5b-ed72-329a-82ac-3aae5ed93d3f | -4.87641 | -47.53121 | 2025-11-01 00:16:00 | TERRA_M-M | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 6.9 |
| ea9cd178-d308-384c-a819-eac08582d7b4 | -3.0173 | -49.44646 | 2025-11-01 00:16:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 52.3 |
| d930c328-8e9d-31e9-8b29-0be24b34268e | -2.98233 | -45.13098 | 2025-11-01 00:16:00 | TERRA_M-M | VIANA | MARANHÃO | Brasil | 2112803 | 21 | 33 | nan | nan | nan | Amazônia | 7.2 |
| f4914fd7-36d9-3cde-bab1-40c1e218a6ad | -3.43812 | -46.09935 | 2025-11-01 00:16:00 | TERRA_M-M | GOVERNADOR NEWTON BELLO | MARANHÃO | Brasil | 2104651 | 21 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 351d98a6-cc0e-3025-8736-1807605bf774 | -3.64273 | -45.97169 | 2025-11-01 00:16:00 | TERRA_M-M | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 12.6 |
| 19b07f3b-171b-3a0f-b678-4e3d1da4932d | -3.57164 | -50.26174 | 2025-11-01 00:16:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 11.2 |
| c172a82d-3c42-394e-822c-6f5336e07a14 | -4.50357 | -45.67889 | 2025-11-01 00:16:00 | TERRA_M-M | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Amazônia | 7.4 |
| 70ac98a2-c5b7-3d8d-8905-c818eb873800 | -4.40304 | -48.21722 | 2025-11-01 00:16:00 | TERRA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 9.9 |
| f8355935-f581-382c-a1f1-04d45b35b970 | -3.48375 | -46.02418 | 2025-11-01 00:16:00 | TERRA_M-M | GOVERNADOR NEWTON BELLO | MARANHÃO | Brasil | 2104651 | 21 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 511be68b-6915-3719-aa99-409cba028e20 | -3.49326 | -52.36881 | 2025-11-01 00:16:00 | TERRA_M-M | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 22.5 |
| 42026a64-9254-3f6c-a870-457bf545ae0a | -4.67809 | -45.80393 | 2025-11-01 00:16:00 | TERRA_M-M | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 66131fc6-d407-37f0-9a6d-d16ac07b2684 | -3.45488 | -46.02509 | 2025-11-01 00:16:00 | TERRA_M-M | GOVERNADOR NEWTON BELLO | MARANHÃO | Brasil | 2104651 | 21 | 33 | nan | nan | nan | Amazônia | 24.7 |
| 5d1ba279-48f3-3dff-ba5e-ffc82446d0f3 | -4.50235 | -45.67009 | 2025-11-01 00:16:00 | TERRA_M-M | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Amazônia | 12.0 |
| a7060947-547d-32b2-a8ad-614067a252d9 | -4.64726 | -47.95477 | 2025-11-01 00:16:00 | TERRA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 41.3 |
| 8dab3809-ea68-3a1b-bff3-f38940295cf9 | -4.1842 | -47.64476 | 2025-11-01 00:16:00 | TERRA_M-M | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 30.4 |
| ed09d951-2b06-3904-a514-4d7b90fc8b23 | -4.47922 | -45.50291 | 2025-11-01 00:16:00 | TERRA_M-M | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 8f54a772-a339-304d-950e-861c75d3ee20 | -4.44391 | -46.04491 | 2025-11-01 00:16:00 | TERRA_M-M | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 172ef4a2-ce8e-3a03-945b-0b85b5acfdab | -3.40937 | -49.99149 | 2025-11-01 00:16:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 257396a9-6b7c-39cb-b837-d8e7148fdb07 | -3.53595 | -50.16557 | 2025-11-01 00:16:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 8.4 |
| a803b1df-c203-3831-a91b-7c63becb524f | -4.851 | -47.53082 | 2025-11-01 00:16:00 | TERRA_M-M | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 14.5 |
| ea1be045-4cb5-3890-a12e-6096b64c69df | -4.64233 | -47.95039 | 2025-11-01 00:16:00 | TERRA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 23.9 |
| 8987f85a-e0b8-3772-85b1-4866a0c059cb | -3.65615 | -50.19484 | 2025-11-01 00:16:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 48.7 |
| ee76afdf-6298-3d43-95f4-52cf8e1e7e23 | -4.67047 | -45.81401 | 2025-11-01 00:16:00 | TERRA_M-M | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 9.6 |
| 31b609c9-1270-36f3-8a6f-f60a54b40cd8 | -3.98702 | -48.90617 | 2025-11-01 00:16:00 | TERRA_M-M | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 87170c7e-7b44-3060-a032-8131347a9250 | -4.28932 | -46.2601 | 2025-11-01 00:16:00 | TERRA_M-M | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 5.1 |
| edc2617e-298b-3b89-a0ca-908ec6184207 | -5.14814 | -49.86753 | 2025-11-01 00:16:00 | TERRA_M-M | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 12.2 |
| 68fb07a7-003a-307b-a2ad-29197db46bad | -4.65587 | -45.70814 | 2025-11-01 00:16:00 | TERRA_M-M | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 351c54cc-1920-3e76-87b3-9afc619c2547 | -4.18554 | -47.65463 | 2025-11-01 00:16:00 | TERRA_M-M | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 145.4 |
| 57e88e33-da57-39fc-a35d-9da30128d2df | -4.95249 | -48.27018 | 2025-11-01 00:16:00 | TERRA_M-M | ABEL FIGUEIREDO | PARÁ | Brasil | 1500131 | 15 | 33 | nan | nan | nan | Amazônia | 18.1 |
| ed3ece66-f40e-3c8d-9ff4-4678f013f8cf | -4.58229 | -44.98171 | 2025-11-01 00:16:00 | TERRA_M-M | LAGO DOS RODRIGUES | MARANHÃO | Brasil | 2105948 | 21 | 33 | nan | nan | nan | Cerrado | 8.0 |
| b9644c23-73c7-3c29-926f-7d77afe0218d | -3.22592 | -50.58592 | 2025-11-01 00:16:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 205.2 |
| 26588c24-2869-3893-9b53-c236a1832598 | -4.16396 | -45.82296 | 2025-11-01 00:16:00 | TERRA_M-M | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 425fa750-7f0e-3d4b-a2d9-072a1f6c42ff | -4.58352 | -44.99057 | 2025-11-01 00:16:00 | TERRA_M-M | LAGO DO JUNCO | MARANHÃO | Brasil | 2105807 | 21 | 33 | nan | nan | nan | Cerrado | 7.5 |
| e64379b3-748c-3b3d-9667-9580ed3a4453 | -3.12947 | -44.40609 | 2025-11-01 00:16:00 | TERRA_M-M | SANTA RITA | MARANHÃO | Brasil | 2110203 | 21 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 6c1c34e4-a37a-3151-8556-36f92d2d31d1 | -3.41121 | -50.00505 | 2025-11-01 00:16:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 32.8 |
| c55e1805-e1e5-3527-82bd-c1a4da736479 | -3.65322 | -50.18658 | 2025-11-01 00:16:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 29.3 |
| 8552694f-e429-3976-a6fe-15538f854173 | -4.10578 | -44.9985 | 2025-11-01 00:16:00 | TERRA_M-M | LAGO VERDE | MARANHÃO | Brasil | 2105906 | 21 | 33 | nan | nan | nan | Amazônia | 15.6 |
| 7d3d00dc-78c3-3293-95e0-fd71a92c1c22 | -3.18907 | -45.76082 | 2025-11-01 00:16:00 | TERRA_M-M | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 8.9 |
| 8fe4fb8a-0dc3-3e32-abeb-5520a8e24f83 | -3.65518 | -50.20081 | 2025-11-01 00:16:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 22.9 |
| 10e49f94-7c3c-3176-8726-d63825240676 | -1.1805 | -48.85269 | 2025-11-01 00:16:00 | TERRA_M-M | CACHOEIRA DO ARARI | PARÁ | Brasil | 1502004 | 15 | 33 | nan | nan | nan | Amazônia | 7.5 |
| df3007df-90e4-39d4-9f08-73a5874029c2 | -4.44886 | -44.22063 | 2025-11-01 00:16:00 | TERRA_M-M | PERITORÓ | MARANHÃO | Brasil | 2108454 | 21 | 33 | nan | nan | nan | Cerrado | 8.4 |
| da252dec-a3cc-383c-ba60-ef4a528c38fb | -2.02352 | -47.00036 | 2025-11-01 00:16:00 | TERRA_M-M | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | 18.8 |
| 390202ba-7250-32d5-82f6-cbfceac07451 | -3.48657 | -50.21547 | 2025-11-01 00:16:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 9.8 |
| c4c11027-8b80-318b-ac03-795da4dee5b0 | -2.761 | -45.39703 | 2025-11-01 00:16:00 | TERRA_M-M | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 12.6 |
| d788d281-f99e-31ae-8f9b-06dfc628702d | -3.04007 | -45.82085 | 2025-11-01 00:16:00 | TERRA_M-M | ARAGUANÃ | MARANHÃO | Brasil | 2100873 | 21 | 33 | nan | nan | nan | Amazônia | 27.1 |
| 57e01db3-4149-34fa-9ef1-d996139061c4 | -3.72907 | -43.31053 | 2025-11-01 00:16:00 | TERRA_M-M | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 11.1 |
| c06f4452-ba02-322f-a4e1-cde76cdee8cb | -3.13075 | -44.41534 | 2025-11-01 00:16:00 | TERRA_M-M | SANTA RITA | MARANHÃO | Brasil | 2110203 | 21 | 33 | nan | nan | nan | Amazônia | 5.9 |
| f468fb7b-8b65-379a-bf72-05faac640115 | -3.82612 | -45.83496 | 2025-11-01 00:16:00 | TERRA_M-M | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 22.3 |
| 4be11b73-d9e9-37f7-aaff-f051e1e30d21 | -4.64376 | -47.96082 | 2025-11-01 00:16:00 | TERRA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 21.8 |
| 80cbd1f5-de6d-33c6-834f-9181728658f9 | -4.39421 | -45.61989 | 2025-11-01 00:16:00 | TERRA_M-M | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 74008957-a67a-386a-9244-8c8aff75c662 | -3.22388 | -50.571 | 2025-11-01 00:16:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 18.7 |
| 571813b0-0cb6-3fe5-b609-e94cba5d9c5f | -2.20765 | -46.18953 | 2025-11-01 00:16:00 | TERRA_M-M | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 1d86d6a1-7399-3170-aea1-fa9a090e5818 | -3.14813 | -49.42218 | 2025-11-01 00:16:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 9.8 |
| 62725dd7-2d5b-3deb-9f29-e413c20e6fbd | -2.18565 | -46.56721 | 2025-11-01 00:16:00 | TERRA_M-M | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 8.7 |
| ccd38b18-e3e8-3aa8-bfdc-b62f30dff880 | -4.1664 | -45.84059 | 2025-11-01 00:16:00 | TERRA_M-M | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 24.2 |
| bf2b96f8-fcdb-3b08-9c5e-b54662650cc5 | -4.64704 | -45.7094 | 2025-11-01 00:16:00 | TERRA_M-M | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 8.0 |
| 3ffd3446-39ad-367d-9ca9-c321b660739f | -2.20643 | -46.18074 | 2025-11-01 00:16:00 | TERRA_M-M | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 3.2 |
| d7c09d9f-01ef-3ef0-a0e4-f9b09b33b1a4 | -3.43263 | -42.54186 | 2025-11-01 00:16:00 | TERRA_M-M | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 15.5 |
| 1f7a4366-cdad-3937-bf3a-92dda9d32157 | -3.43256 | -42.53568 | 2025-11-01 00:16:00 | TERRA_M-M | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 55212bba-71e8-39b0-90eb-6d9313870f0a | -3.97695 | -48.90755 | 2025-11-01 00:16:00 | TERRA_M-M | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 53.2 |
| 851747b0-4912-36db-929e-dced0972755d | -3.57361 | -50.27599 | 2025-11-01 00:16:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 0a0e14e5-f501-37fd-aef9-25bb156ed2d0 | -3.4369 | -46.09052 | 2025-11-01 00:16:00 | TERRA_M-M | GOVERNADOR NEWTON BELLO | MARANHÃO | Brasil | 2104651 | 21 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 518b59af-d767-3507-8757-9fa6fd860aec | -1.49774 | -47.79817 | 2025-11-01 00:16:00 | TERRA_M-M | SÃO MIGUEL DO GUAMÁ | PARÁ | Brasil | 1507607 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 86c0b9e5-25b2-38bc-bdf6-8f48d702d3b5 | -3.68892 | -49.58007 | 2025-11-01 00:16:00 | TERRA_M-M | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 7.3 |
| 0f7d2d05-0e15-3f94-9498-7c83d9cc6e5f | -4.79847 | -46.47996 | 2025-11-01 00:16:00 | TERRA_M-M | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 4.2 |
| bc0315ae-39b0-3c55-ba50-944ec38752aa | -3.71823 | -43.93501 | 2025-11-01 00:16:00 | TERRA_M-M | VARGEM GRANDE | MARANHÃO | Brasil | 2112704 | 21 | 33 | nan | nan | nan | Cerrado | 6.6 |
| a241b7df-43a8-3ea8-a4de-de0bddb34057 | -3.39068 | -45.48141 | 2025-11-01 00:16:00 | TERRA_M-M | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 3fcaa063-e119-3c17-8585-fd852465b4cf | -2.98109 | -45.1221 | 2025-11-01 00:16:00 | TERRA_M-M | MATINHA | MARANHÃO | Brasil | 2106508 | 21 | 33 | nan | nan | nan | Amazônia | 10.4 |
| 5865313f-317f-3437-b0b5-79f9b6849c13 | -4.16517 | -45.83176 | 2025-11-01 00:16:00 | TERRA_M-M | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 17.6 |
| b1c60d81-ac1d-39de-90d3-ce3c3d5cd2ef | -2.62803 | -45.16907 | 2025-11-01 00:16:00 | TERRA_M-M | PINHEIRO | MARANHÃO | Brasil | 2108603 | 21 | 33 | nan | nan | nan | Amazônia | 4.6 |
| e1bc1cb2-8f8a-3cdd-91f9-1a11ed980874 | -4.11472 | -43.87725 | 2025-11-01 00:16:00 | TERRA_M-M | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 61718cf6-428c-3ba4-846c-2ab15bc66106 | -3.72314 | -43.3073 | 2025-11-01 00:16:00 | TERRA_M-M | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 011b6276-9e7d-3319-a3ab-b19528284962 | -4.61383 | -45.81039 | 2025-11-01 00:16:00 | TERRA_M-M | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 1cce5343-99b4-3eb8-9510-383724184554 | -4.393 | -45.61109 | 2025-11-01 00:16:00 | TERRA_M-M | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 7.4 |
| b878ec43-c5e0-35e8-9a95-14b191898246 | 1.31525 | -51.20795 | 2025-11-01 00:18:00 | TERRA_M-M | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 8.1 |
| 396bf620-1e4f-34ca-9fab-0d144481401b | 1.25236 | -50.84416 | 2025-11-01 00:18:00 | TERRA_M-M | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 2d5fa414-5b96-3b4c-bec1-3f4ae46e2f73 | -1.85028 | -54.5587 | 2025-11-01 00:18:00 | TERRA_M-M | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 26.5 |
| 584b689f-8cb4-3c2d-bd8d-a6b2b4d102c4 | -3.234 | -50.5999 | 2025-11-01 00:20:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 85.9 |
| 6c213201-099a-3c66-ae6d-82bafb39bc56 | -10.6124 | -52.1909 | 2025-11-01 00:20:00 | GOES-19 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 63.1 |
| b3dfdf94-a72d-39b7-94aa-d296b9ca94f6 | -11.7433 | -47.4741 | 2025-11-01 00:20:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 76.7 |
| 5a2b7992-6e1c-3512-a785-aaceced4116e | -4.1738 | -47.6636 | 2025-11-01 00:20:00 | GOES-19 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 66.9 |
| deb52a1a-8235-35a0-80bc-737deaf2aefc | -4.1925 | -47.6409 | 2025-11-01 00:20:00 | GOES-19 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 76.1 |
| 68095040-26c6-3b4b-93db-b7a52eeba9b2 | -4.5047 | -54.9247 | 2025-11-01 00:20:00 | GOES-19 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 80.5 |
| 90802a86-ea45-31cd-af47-0cd6464aa38c | -10.6565 | -45.1542 | 2025-11-01 00:20:00 | GOES-19 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 53.5 |
| 8c520c99-df4e-388e-af8e-1ebebf1e49a2 | -3.2155 | -50.6004 | 2025-11-01 00:20:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 69.2 |
| a4f75ee4-a7b4-33cd-baa3-4c46f06484dc | -13.3337 | -60.7158 | 2025-11-01 00:20:00 | GOES-19 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 67.9 |
| 982be030-ed60-3f4f-8c77-316645ec2d21 | -10.6313 | -52.1891 | 2025-11-01 00:20:00 | GOES-19 | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Amazônia | 108.7 |
| e42a3694-139d-3b28-b51b-0bf3b0e719d9 | -4.1739 | -47.6418 | 2025-11-01 00:20:00 | GOES-19 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 85.4 |
| e4df51b4-97a7-3d67-b95a-ea4f3eba55fb | -13.6657 | -44.4115 | 2025-11-01 00:20:00 | GOES-19 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 69.1 |
| 66a87ffb-6d88-3a2a-a51d-1b0050f63b32 | -6.9481 | -49.6312 | 2025-11-01 00:20:00 | GOES-19 | SAPUCAIA | PARÁ | Brasil | 1507755 | 15 | 33 | nan | nan | nan | Amazônia | 89.6 |
| 9e486134-03ad-3eb4-80b6-7a74f19cbe75 | -13.6463 | -44.4149 | 2025-11-01 00:20:00 | GOES-19 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 69.0 |
| 84ae9d34-2ec9-3ce0-ade2-3ec5159db96e | -6.9295 | -49.6325 | 2025-11-01 00:20:00 | GOES-19 | SAPUCAIA | PARÁ | Brasil | 1507755 | 15 | 33 | nan | nan | nan | Amazônia | 67.3 |
| 3388dc41-e459-3915-9747-e2a3b9664c8c | -10.6502 | -52.1873 | 2025-11-01 00:20:00 | GOES-19 | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Amazônia | 60.8 |


[Clique aqui para ver as próximas entradas](README7.md)
