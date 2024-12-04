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

## Dados Diários - Página 16

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 6f16446f-23f0-3a70-951e-230e50453488 | -2.8013 | -53.043 | 2024-12-04 01:20:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 46.0 |
| 47684ebe-d417-32e3-9eea-822d39275b21 | -3.1969 | -50.6428 | 2024-12-04 01:20:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 79.5 |
| a0e53057-fc4e-3fb6-854b-3885c5173d8d | -2.8196 | -53.0629 | 2024-12-04 01:20:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 95.7 |
| a16d9f1a-8ec7-3975-af70-65edcdb0e357 | -1.7361 | -52.6366 | 2024-12-04 01:20:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 58.2 |
| d0a45f67-298e-3d88-9a40-acdc9cf40676 | -3.2021 | -45.2932 | 2024-12-04 01:20:00 | GOES-16 | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | 67.2 |
| 3560c934-e5b5-3ec1-a48d-c61498ab8ec8 | -2.8012 | -53.0633 | 2024-12-04 01:20:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 67.3 |
| 01301b1a-d6b1-3aed-b834-771d3a83b59c | -3.259 | -53.659 | 2024-12-04 01:20:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 78.7 |
| 97cf7b81-0cc6-34f0-9cd1-cd3964a1769c | -3.259 | -53.6388 | 2024-12-04 01:20:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 68.6 |
| 6eaadb16-ac76-3553-a5cd-023556b09085 | -2.5517 | -45.2712 | 2024-12-04 01:20:00 | GOES-16 | PRESIDENTE SARNEY | MARANHÃO | Brasil | 2109270 | 21 | 33 | nan | nan | nan | Amazônia | 65.4 |
| 6dfb9d11-6989-3ebe-8118-a12c9495f87b | -3.1269 | -54.6263 | 2024-12-04 01:20:00 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 824.9 |
| c7b63931-aa3f-365b-95a5-1df293b06d1e | -3.127 | -54.6063 | 2024-12-04 01:20:00 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 642.9 |
| 72f59fc5-73d8-341d-adc9-63da6e07e65f | -1.7545 | -52.6159 | 2024-12-04 01:20:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 78.9 |
| 0d95f09c-b9a9-34fc-b7da-409262022cde | -3.058 | -53.28 | 2024-12-04 01:30:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 65.9 |
| 4fd876c8-ff3f-32cd-8a7a-051cf9b49b32 | -4.1223 | -43.9299 | 2024-12-04 01:30:00 | GOES-16 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 44.0 |
| 2b066aed-ed0a-34c4-8086-5c10c4c5f86f | -3.1969 | -50.6428 | 2024-12-04 01:30:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 75.4 |
| 1d9a5e06-b497-39be-b31c-8fb04ab4581d | -3.259 | -53.659 | 2024-12-04 01:30:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 78.6 |
| dae6f549-5e50-3804-a35d-0ff395c28701 | -3.2774 | -53.6585 | 2024-12-04 01:30:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 67.1 |
| 47beb60d-99a4-3dfa-bf7f-7429890500a9 | -1.6623 | -52.7599 | 2024-12-04 01:30:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 46.2 |
| 7ad88de4-ac51-3a15-b8ce-dcec624998af | -3.1269 | -54.6263 | 2024-12-04 01:30:00 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 793.8 |
| 5389ef93-0cbc-3fc0-82de-3aa505646f17 | -3.1454 | -54.6059 | 2024-12-04 01:30:00 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 120.9 |
| efad4ecd-4134-3483-9e44-79e599f70017 | -5.6281 | -44.8433 | 2024-12-04 01:30:00 | GOES-16 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 64.4 |
| dcb5a8eb-d935-3641-9e00-6c848150c17e | -1.7545 | -52.6159 | 2024-12-04 01:30:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 78.9 |
| bc7c05ba-eea3-3cd1-9ced-845ede138e30 | -2.6428 | -45.7394 | 2024-12-04 01:30:00 | GOES-16 | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | 124.5 |
| df522853-f489-3c68-a5be-c8fdba33a0a7 | -1.7361 | -52.6162 | 2024-12-04 01:30:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 66.9 |
| 2dd01eec-0ff4-3c14-b699-647490ed9227 | -2.6242 | -45.7399 | 2024-12-04 01:30:00 | GOES-16 | SANTA LUZIA DO PARUÁ | MARANHÃO | Brasil | 2110039 | 21 | 33 | nan | nan | nan | Amazônia | 79.2 |
| a115b450-34e8-3f22-8b61-29ea0b5044e9 | -1.7361 | -52.6366 | 2024-12-04 01:30:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 54.4 |
| 920c7a72-dec2-3b89-a5a4-342b33d8baf1 | -2.1925 | -47.2544 | 2024-12-04 01:30:00 | GOES-16 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 49.4 |
| 52b22b15-e686-39f6-839e-665d31786269 | -3.127 | -54.6063 | 2024-12-04 01:30:00 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 630.9 |
| b7b8d706-8e4a-3599-8710-e2777758fa1a | -3.1086 | -54.6068 | 2024-12-04 01:30:00 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 184.8 |
| 2b07535d-0530-35bf-8b88-9c745a3abf82 | -3.1453 | -54.6259 | 2024-12-04 01:30:00 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 137.5 |
| 5ba0e4ec-ef3b-33a1-8315-42d53a85a68f | -3.259 | -53.6388 | 2024-12-04 01:30:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 68.4 |
| cfc78373-a913-353d-ab99-625a990dfb97 | -1.4768 | -53.7947 | 2024-12-04 01:30:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 35.2 |
| dff375c0-d019-3b65-8604-c9acfdef0c9f | -1.7544 | -52.6363 | 2024-12-04 01:30:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 80.2 |
| b80e7409-96d6-378f-8a9d-73572882d52f | -2.2111 | -47.2321 | 2024-12-04 01:30:00 | GOES-16 | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | 42.5 |
| 26a8189a-d77c-3844-9191-e2675f9b53a6 | -6.086 | -48.0557 | 2024-12-04 01:30:00 | GOES-16 | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 72.7 |
| 6ee87be3-b2f6-36df-a720-699c2739c011 | -3.586 | -50.3158 | 2024-12-04 01:30:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 63.8 |
| 4bc01342-51b9-3c5b-82e8-ace5e34c5f5b | -2.211 | -47.254 | 2024-12-04 01:30:00 | GOES-16 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 56.4 |
| 3d9a18ce-5c9d-3f27-9a25-2294874c9d78 | -2.8196 | -53.0629 | 2024-12-04 01:30:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 43.4 |
| 5475b7f5-1218-3f99-ae89-daa95feafc36 | -3.1086 | -54.6268 | 2024-12-04 01:30:00 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 228.1 |
| 1293baf8-312f-38ac-ae7b-954749ad4d95 | -4.1037 | -43.9309 | 2024-12-04 01:40:00 | GOES-16 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 43.7 |
| ee3ab222-3ae7-30ee-aaae-ed0e4f72c361 | -1.663 | -52.3927 | 2024-12-04 01:40:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 53.1 |
| f7c6bfd5-51b6-3b97-84b2-d51ddbbf2009 | -1.7545 | -52.6159 | 2024-12-04 01:40:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 115.0 |
| df406185-3e34-3674-b602-870090199ac0 | -1.6446 | -52.393 | 2024-12-04 01:40:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 54.0 |
| 77d12c2c-dfbb-36ed-8bae-1f8979059161 | -3.2153 | -50.6423 | 2024-12-04 01:40:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 69.5 |
| 1c969a0e-0b43-3274-81a9-a340cf099bd4 | -2.6428 | -45.7394 | 2024-12-04 01:40:00 | GOES-16 | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | 93.2 |
| 39e1ab98-073e-3cac-8e3b-a2ed77f23c2e | -3.1969 | -50.6428 | 2024-12-04 01:40:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 58.7 |
| 532cb3df-ef10-373c-ba38-1a3d74747114 | -3.5675 | -50.3164 | 2024-12-04 01:40:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 56.5 |
| 6a542e6a-e6e1-318a-b2b8-6609786d9ef7 | -2.1925 | -47.2326 | 2024-12-04 01:40:00 | GOES-16 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 47.7 |
| 6ebc133c-bb90-33c5-b54d-b80b98148239 | -6.086 | -48.0557 | 2024-12-04 01:40:00 | GOES-16 | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 110.1 |
| 8f614ffb-d1ac-34cf-a2e5-5f20317bf8bc | -2.1925 | -47.2544 | 2024-12-04 01:40:00 | GOES-16 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 57.8 |
| 5ad11f86-7a40-3228-8cdd-205c335d0339 | -1.6447 | -52.3725 | 2024-12-04 01:40:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 53.9 |
| 3ccd2b01-db97-3c55-bd51-ffbbdf081a50 | -2.6242 | -45.7399 | 2024-12-04 01:40:00 | GOES-16 | SANTA LUZIA DO PARUÁ | MARANHÃO | Brasil | 2110039 | 21 | 33 | nan | nan | nan | Amazônia | 116.8 |
| 503c21bd-43b3-3a66-a987-f42bf6b8adec | -3.259 | -53.659 | 2024-12-04 01:40:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 88.9 |
| bdd2b9c0-229c-3e3f-a4ab-3368ebb29c64 | -1.7361 | -52.6162 | 2024-12-04 01:40:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 70.8 |
| fdb536bf-1b5f-3442-9b2c-09c1e7868429 | -1.7361 | -52.6366 | 2024-12-04 01:40:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 55.7 |
| 0585b13d-2f24-31d0-aa61-d621f387de11 | -3.0764 | -53.2796 | 2024-12-04 01:40:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 63.6 |
| 5c89fb8c-6d02-3bd8-83bb-95041ca15799 | -1.7544 | -52.6363 | 2024-12-04 01:40:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 143.7 |
| 7ebe8955-5687-34e0-b7aa-1a09bad754a5 | -6.1047 | -48.0544 | 2024-12-04 01:40:00 | GOES-16 | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 59.6 |
| 6a6f9e94-591e-3a36-a34e-30c81fc25ac1 | -2.211 | -47.254 | 2024-12-04 01:40:00 | GOES-16 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 52.5 |
| 7c53f3b4-9efa-3931-977a-8175609edc78 | -5.6281 | -44.8433 | 2024-12-04 01:40:00 | GOES-16 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 66.1 |
| 46218910-e75f-394a-acb2-5797f6e9cf38 | -3.0765 | -53.2593 | 2024-12-04 01:40:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 59.6 |
| fe7c0961-72e7-3648-b5b5-10cc26e2517a | -6.0862 | -48.0339 | 2024-12-04 01:40:00 | GOES-16 | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 54.2 |
| d63ac61c-273b-36fa-b23a-03ada8bb85ce | -2.8975 | -51.8133 | 2024-12-04 01:40:00 | GOES-16 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 65.9 |
| 52950b9f-2ff3-3e88-a653-ea8a5e8408d0 | -3.586 | -50.3158 | 2024-12-04 01:40:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 55.0 |
| 31e7f255-dabf-3ca7-b148-a4aa766d0f57 | -4.1223 | -43.9299 | 2024-12-04 01:40:00 | GOES-16 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 67.3 |
| 5cd8ba81-4e9d-33a0-9453-b42d3ce4b35f | -3.259 | -53.6388 | 2024-12-04 01:40:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 74.9 |
| cfa78a55-76da-3c23-b406-517b0ad9a26a | -6.086 | -48.0557 | 2024-12-04 01:50:00 | GOES-16 | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 100.3 |
| b307c2ea-a3fe-39aa-be22-815d967a5e1c | -3.259 | -53.6388 | 2024-12-04 01:50:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 70.7 |
| 022b351d-8579-31a2-b455-c3af87bb2f9d | -4.1222 | -43.9529 | 2024-12-04 01:50:00 | GOES-16 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 49.2 |
| 9d2b623a-c454-3f2f-af30-d6f5a6572af0 | -3.259 | -53.659 | 2024-12-04 01:50:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 83.3 |
| c997cc0f-a4f4-3830-a069-d10a99852a66 | -2.6428 | -45.7394 | 2024-12-04 01:50:00 | GOES-16 | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | 110.6 |
| 30071397-09a0-399b-a0b2-4c3fb70ee990 | -6.0862 | -48.0339 | 2024-12-04 01:50:00 | GOES-16 | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 52.3 |
| 0f8d8f8f-bcbc-37ff-af5e-51968c59f9c6 | -3.5675 | -50.3164 | 2024-12-04 01:50:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 52.1 |
| 79c04c39-a74b-3156-94b0-876c84d96e00 | -6.1047 | -48.0544 | 2024-12-04 01:50:00 | GOES-16 | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 52.3 |
| d10086bc-a96b-3e37-9283-28196daafee4 | -1.7361 | -52.6162 | 2024-12-04 01:50:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 59.0 |
| 2ed4a805-7d80-35ca-acad-ff78d3648c64 | -3.1969 | -50.6428 | 2024-12-04 01:50:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 62.2 |
| 4b4f0674-87ed-340e-9fd0-4e298c67d343 | -1.6446 | -52.393 | 2024-12-04 01:50:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 49.0 |
| 41b91163-8fab-3916-9e80-c209489a5031 | -1.7545 | -52.6159 | 2024-12-04 01:50:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 76.0 |
| 27a83871-715c-39ed-b658-fa9dd94317a1 | -2.6242 | -45.7399 | 2024-12-04 01:50:00 | GOES-16 | SANTA LUZIA DO PARUÁ | MARANHÃO | Brasil | 2110039 | 21 | 33 | nan | nan | nan | Amazônia | 106.9 |
| 1ec9f120-85d3-3e5e-ae93-69414f1daa8e | -1.7361 | -52.6366 | 2024-12-04 01:50:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 52.3 |
| e6af451d-f252-3d75-8983-91eb830dd0de | -4.1223 | -43.9299 | 2024-12-04 01:50:00 | GOES-16 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 115.2 |
| e0be4dfd-cb23-3bc6-8253-e0f41cbfea27 | -3.2153 | -50.6423 | 2024-12-04 01:50:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 58.5 |
| d13b5ab5-004a-332b-a79e-abc637632d84 | -3.586 | -50.3158 | 2024-12-04 01:50:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 50.3 |
| 2f04f1a4-f355-3dbf-93d9-aa0d701124b2 | -1.6447 | -52.3725 | 2024-12-04 01:50:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 41.7 |
| 7c0c9d80-8127-3a04-a03e-701c8ece4332 | -1.7544 | -52.6363 | 2024-12-04 01:50:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 96.7 |
| 551cf6f3-7f03-3356-9a0b-042786f82532 | -5.6281 | -44.8433 | 2024-12-04 01:50:00 | GOES-16 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 46.6 |
| d9270e80-b987-35a3-8a53-f2bc5463aa15 | -2.211 | -47.254 | 2024-12-04 01:50:00 | GOES-16 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 66.6 |
| 0f0a2312-7cd4-39c7-8eea-bfb6dd4db86f | -2.8975 | -51.8133 | 2024-12-04 01:50:00 | GOES-16 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 61.8 |
| 87531e43-d6e3-3089-9bd4-bd6415f8f8d6 | -4.1037 | -43.9309 | 2024-12-04 01:50:00 | GOES-16 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 47.4 |
| 4925d4da-5733-345b-ad2f-f98dcc728118 | -1.6623 | -52.7599 | 2024-12-04 01:50:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 47.6 |
| c88f0cb6-536e-3e2f-abd3-1b77ba9bae96 | -1.663 | -52.3927 | 2024-12-04 01:50:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 57.7 |
| 7992bf71-1074-3fe0-b6e6-732495b4a7b9 | -1.7545 | -52.6159 | 2024-12-04 02:00:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 59.8 |
| 4d4e93e5-0821-3790-bb03-28595c8ab246 | -3.0764 | -53.2796 | 2024-12-04 02:00:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 60.1 |
| 95ea1f28-b22d-3009-a94f-09cea842e900 | -1.663 | -52.3927 | 2024-12-04 02:00:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 50.5 |
| f8858118-d015-38ba-9d8b-5605e5e7199e | -6.086 | -48.0557 | 2024-12-04 02:00:00 | GOES-16 | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 114.2 |
| d4879df6-967b-313f-8f16-2b8c60c7c5af | -3.259 | -53.659 | 2024-12-04 02:00:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 84.4 |
| 9f9582ef-6870-3d43-a520-c3d2ef5b3622 | -2.1925 | -47.2544 | 2024-12-04 02:00:00 | GOES-16 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 57.2 |
| 69dbc100-cba1-3966-becc-2363e01c3e07 | -4.1037 | -43.9309 | 2024-12-04 02:00:00 | GOES-16 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 54.3 |
| 921eb047-7976-3463-b438-796462ff9df8 | -1.6623 | -52.7599 | 2024-12-04 02:00:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 44.4 |
| b307ae02-eaf4-3788-a4fe-d8b0c3dda111 | -4.1223 | -43.9299 | 2024-12-04 02:00:00 | GOES-16 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 107.5 |


[Clique aqui para ver as próximas entradas](README17.md)
