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

## Dados Diários - Página 5

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| b037543f-d8ed-38c5-9dfc-7a935bae6e86 | -2.4676 | -52.149899 | 2024-11-27 00:21:00 | METOP-C | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 982d2b23-2e21-3b14-90ab-2974e4a77f7d | -5.6069 | -47.073299 | 2024-11-27 00:21:00 | METOP-C | BURITIRANA | MARANHÃO | Brasil | 2102358 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| c55efd57-14a3-3ef8-b3d8-7cc24e4ec4b1 | -1.4202 | -52.575298 | 2024-11-27 00:21:00 | METOP-C | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7f5dbf22-379f-3ec7-8263-85b893acf736 | -1.8815 | -50.5966 | 2024-11-27 00:21:00 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 16ec4100-891f-381b-945e-17e59d20822b | -3.3513 | -50.116501 | 2024-11-27 00:21:00 | METOP-C | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| eb066cb2-7c54-31c7-ade6-370088fa4ad2 | -3.9967 | -45.5425 | 2024-11-27 00:21:00 | METOP-C | ALTAMIRA DO MARANHÃO | MARANHÃO | Brasil | 2100402 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| b2dcdfb8-7673-374d-a30d-a3cfe674ddd5 | -1.7598 | -52.721802 | 2024-11-27 00:21:00 | METOP-C | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a4ff09db-d034-3326-9c90-123ef3f18e49 | -4.3664 | -41.712399 | 2024-11-27 00:21:00 | METOP-C | PIRIPIRI | PIAUÍ | Brasil | 2208403 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 12d912f9-73eb-3133-88a0-6aea0c360067 | -1.3751 | -46.7453 | 2024-11-27 00:21:00 | METOP-C | BRAGANÇA | PARÁ | Brasil | 1501709 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c49d6c66-88cf-3a4d-b44f-9c149d3dbeb2 | -8.0307 | -47.079899 | 2024-11-27 00:21:00 | METOP-C | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 5aba9d00-646d-3fcc-84f0-5858eefc91ae | -4.8854 | -38.735001 | 2024-11-27 00:21:00 | METOP-C | IBARETAMA | CEARÁ | Brasil | 2305266 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| 806fdfa3-a8aa-38a2-95bd-f6a48587c1f0 | -3.0774 | -53.235001 | 2024-11-27 00:21:00 | METOP-C | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3d76ed6a-3250-37ce-9d64-5fde1e92062e | -2.7704 | -52.908401 | 2024-11-27 00:21:00 | METOP-C | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 50fa795d-9d44-33e8-ba47-c46f0c6a5a0c | -5.8727 | -43.412399 | 2024-11-27 00:21:00 | METOP-C | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 61c9d824-f214-330d-89ed-44ee5dcbc1d5 | -4.3647 | -41.705002 | 2024-11-27 00:21:00 | METOP-C | PIRIPIRI | PIAUÍ | Brasil | 2208403 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| cfd8589d-085d-3848-b610-c241f70a65cd | -2.9783 | -45.459702 | 2024-11-27 00:21:00 | METOP-C | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 6ed0cd84-ea12-3e2d-a7db-f0b5acb3eb8f | -7.6681 | -42.964802 | 2024-11-27 00:21:00 | METOP-C | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| c578a7d1-119f-3de0-b96d-397454409ecf | -5.966 | -45.368698 | 2024-11-27 00:21:00 | METOP-C | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 6acbed64-f6ef-3b7f-80e6-029c52a2b69e | -5.5946 | -43.956501 | 2024-11-27 00:21:00 | METOP-C | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 25ba566c-e5cd-35a8-b6a5-2f287bb6e468 | -3.0659 | -50.3512 | 2024-11-27 00:21:00 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| def188b7-55b3-34d9-9a75-7eb50bbb4edd | -3.4748 | -50.302799 | 2024-11-27 00:21:00 | METOP-C | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7ad2a2c0-36e4-33f5-aeb7-c9c8380a9c82 | -3.2647 | -41.766701 | 2024-11-27 00:21:00 | METOP-C | BURITI DOS LOPES | PIAUÍ | Brasil | 2202000 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 06de74bd-71f4-3ea3-ac9f-4f1439c08325 | -8.1021 | -44.4739 | 2024-11-27 00:21:00 | METOP-C | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| f2c089f0-d72c-3783-8107-9d8bc9d9c9a9 | -3.467 | -50.497101 | 2024-11-27 00:21:00 | METOP-C | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 725eaa51-f812-30fb-8e0f-8dfcea99a06b | -1.9267 | -45.730499 | 2024-11-27 00:21:00 | METOP-C | CÂNDIDO MENDES | MARANHÃO | Brasil | 2102606 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 233c27ca-fc4e-3504-84c9-afa185ea3553 | -3.8357 | -40.452202 | 2024-11-27 00:21:00 | METOP-C | CARIRÉ | CEARÁ | Brasil | 2303105 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| b99d2aae-6e6f-3d2a-a28e-32cf17022c7c | -1.4105 | -52.577499 | 2024-11-27 00:21:00 | METOP-C | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 06427e7d-4124-3527-92a5-bef3c0ee1031 | -4.998 | -47.015999 | 2024-11-27 00:21:00 | METOP-C | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 586e1d1d-8ec7-338f-8ed1-ce6e5ecaa023 | -3.2501 | -43.043499 | 2024-11-27 00:21:00 | METOP-C | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 6ebd286d-433a-3ee9-b1dc-97ad4f955256 | -2.8032 | -46.819099 | 2024-11-27 00:21:00 | METOP-C | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9204a54e-d9f2-377e-a0d0-622a88a71ff3 | -3.0591 | -41.1474 | 2024-11-27 00:21:00 | METOP-C | BARROQUINHA | CEARÁ | Brasil | 2302057 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| 6eedbdba-6ced-3b26-8c46-3dab8b46cd27 | -3.8231 | -46.503502 | 2024-11-27 00:21:00 | METOP-C | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| a9962fc0-9497-38b4-97e6-d6af823159ec | -3.3465 | -46.308899 | 2024-11-27 00:21:00 | METOP-C | SÃO JOÃO DO CARÚ | MARANHÃO | Brasil | 2111029 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| e233056c-1101-334a-8c3a-3f283d123a0e | -3.464 | -50.483799 | 2024-11-27 00:21:00 | METOP-C | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8c190885-a705-3942-9736-c1d9edee25a5 | -3.2517 | -43.0504 | 2024-11-27 00:21:00 | METOP-C | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 14238086-a8de-3c8d-85ca-a3d2324cd424 | -3.0205 | -48.507099 | 2024-11-27 00:21:00 | METOP-C | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e0b5a990-188b-39a3-96ad-889ad898124f | -4.1262 | -43.803902 | 2024-11-27 00:21:00 | METOP-C | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| e59592a0-71fb-3f1d-ba92-f8e501e58646 | -2.1486 | -53.765301 | 2024-11-27 00:21:00 | METOP-C | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 98ec7c19-bc31-3731-99c3-bd8eefc15208 | -2.7084 | -47.536098 | 2024-11-27 00:21:00 | METOP-C | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 496969e4-0b8c-3150-b3f9-5181c2b6ff05 | -4.998 | -43.601501 | 2024-11-27 00:21:00 | METOP-C | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| d7c637ed-a6f0-34d6-8322-592acce69ab8 | -4.1129 | -43.835602 | 2024-11-27 00:21:00 | METOP-C | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 5ab1939b-8ee7-3720-8f13-4e692c421e48 | -5.9528 | -45.356098 | 2024-11-27 00:21:00 | METOP-C | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| cab410a9-de10-377c-92c9-4f85708d5319 | -1.3938 | -47.459099 | 2024-11-27 00:21:00 | METOP-C | SANTA MARIA DO PARÁ | PARÁ | Brasil | 1506609 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f6bbfd58-cbaa-3471-960c-3a878f1575a8 | -2.6017 | -48.427299 | 2024-11-27 00:21:00 | METOP-C | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e2fb260e-9857-379f-aae5-b990bf1b095f | -2.8788 | -45.385201 | 2024-11-27 00:21:00 | METOP-C | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 8ccec770-0a41-3809-aedf-61860c13132a | -6.8087 | -44.401299 | 2024-11-27 00:21:00 | METOP-C | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| d9856649-131d-3902-9e20-6bad8a541c63 | -6.8804 | -34.984699 | 2024-11-27 00:21:00 | METOP-C | RIO TINTO | PARAÍBA | Brasil | 2512903 | 25 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 64ec99e2-55e0-306a-b5f4-60ba907c719b | -4.9995 | -43.608299 | 2024-11-27 00:21:00 | METOP-C | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 3e8ba73f-7100-391c-b99e-d3914e776b44 | -4.1134 | -50.413601 | 2024-11-27 00:21:00 | METOP-C | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 83af1dfa-e35a-39a8-a6c4-5f7aace6cda3 | -5.0078 | -43.5993 | 2024-11-27 00:21:00 | METOP-C | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| e7acef43-d2be-3aa3-9caf-e6a93c8e3525 | -1.635 | -52.7117 | 2024-11-27 00:21:00 | METOP-C | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e7ca756f-7c52-3ad6-9fe9-4eed7f677d95 | -2.865 | -54.150501 | 2024-11-27 00:21:00 | METOP-C | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0091a158-cf5e-3bff-9856-d5a800cc06d7 | -3.5058 | -52.1394 | 2024-11-27 00:21:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 165ad274-3d30-3589-95b9-52666a4ab8c1 | -4.116 | -43.849201 | 2024-11-27 00:21:00 | METOP-C | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 689c430b-2355-37d0-b9fd-b0cc66087bc3 | -2.801 | -54.091099 | 2024-11-27 00:21:00 | METOP-C | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4ef255f9-1df3-33e3-9ea2-78f0694f7b18 | -5.2886 | -43.0695 | 2024-11-27 00:21:00 | METOP-C | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 3f9963fc-5940-3388-921f-db853a882d1f | -2.7661 | -52.889301 | 2024-11-27 00:21:00 | METOP-C | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5a7f4135-1c8f-3530-ac15-9adba11bdc02 | -3.5468 | -41.9603 | 2024-11-27 00:21:00 | METOP-C | JOAQUIM PIRES | PIAUÍ | Brasil | 2205409 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 37f7e258-8841-3b5a-9081-c3d3c95c35a1 | -7.4759 | -34.854599 | 2024-11-27 00:21:00 | METOP-C | PITIMBU | PARAÍBA | Brasil | 2511905 | 25 | 33 | nan | nan | nan | Mata Atlântica | nan |
| cb1f11e3-8733-38ed-971f-e49041b3044c | -2.1584 | -53.7631 | 2024-11-27 00:21:00 | METOP-C | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6debc25b-4a0e-3a6f-ba86-f8b9758bbdc3 | -1.6911 | -45.376999 | 2024-11-27 00:21:00 | METOP-C | TURIAÇU | MARANHÃO | Brasil | 2112407 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 71f11634-1bd1-38ca-866a-4599ec69e2e4 | -1.3957 | -47.4673 | 2024-11-27 00:21:00 | METOP-C | SANTA MARIA DO PARÁ | PARÁ | Brasil | 1506609 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 712362d4-759c-3573-9752-0080eb82e5cc | -3.0632 | -53.216801 | 2024-11-27 00:21:00 | METOP-C | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f2941fc0-e1ba-37d0-af00-8e74b6150c7f | -6.8749 | -35.004002 | 2024-11-27 00:21:00 | METOP-C | RIO TINTO | PARAÍBA | Brasil | 2512903 | 25 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 28558869-fe2d-38da-9279-a2e4f4433a83 | -4.0674 | -44.855999 | 2024-11-27 00:21:00 | METOP-C | LAGO VERDE | MARANHÃO | Brasil | 2105906 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| fa400323-0c53-3303-b10d-5c61779aba4c | -2.9242 | -45.494099 | 2024-11-27 00:21:00 | METOP-C | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 6ebf55fc-d62f-3cd9-a629-50e041020b1a | -2.8804 | -45.3923 | 2024-11-27 00:21:00 | METOP-C | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| dd9c8ad7-676d-319d-b1d1-526660b497d2 | -2.4639 | -52.133202 | 2024-11-27 00:21:00 | METOP-C | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d4c677c8-bdbc-3e82-890f-6d96a94e15db | -3.0192 | -53.247601 | 2024-11-27 00:21:00 | METOP-C | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 53372186-381a-31f8-b500-8dc4bb31bf7f | -4.1294 | -43.817501 | 2024-11-27 00:21:00 | METOP-C | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| acee5116-fbeb-39d6-8808-af210e0f3439 | -3.0596 | -47.815102 | 2024-11-27 00:21:00 | METOP-C | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e9ec7889-1ab1-3f6c-9dc1-637be0581bac | -8.1119 | -44.471699 | 2024-11-27 00:21:00 | METOP-C | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 78b200c3-2f58-3d2a-8d4a-9bb5b9050f31 | -3.4922 | -52.1241 | 2024-11-27 00:21:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c60f210f-b111-3e1f-9a93-1e6b2018455e | -1.925 | -45.7234 | 2024-11-27 00:21:00 | METOP-C | CÂNDIDO MENDES | MARANHÃO | Brasil | 2102606 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 155599b0-4d61-3a27-bd4d-b280cd855ba2 | -4.4731 | -46.601799 | 2024-11-27 00:21:00 | METOP-C | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 1ae7fa5f-59ea-3281-9af5-1678e84612e7 | -3.3562 | -45.8526 | 2024-11-27 00:21:00 | METOP-C | GOVERNADOR NEWTON BELLO | MARANHÃO | Brasil | 2104651 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 00fad672-38ec-3adc-ad05-6a6b15a2f59a | -5.6365 | -46.422901 | 2024-11-27 00:21:00 | METOP-C | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| aa6f3c3c-8557-3489-9a24-847e8f5357ca | -2.9258 | -45.501202 | 2024-11-27 00:21:00 | METOP-C | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| ce90780f-a5ac-3b5e-aa6d-967ead10842e | -4.2453 | -42.437302 | 2024-11-27 00:21:00 | METOP-C | BARRAS | PIAUÍ | Brasil | 2201200 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 74140760-f202-37ec-9eab-45930141491b | -6.9051 | -37.1394 | 2024-11-27 00:21:00 | METOP-C | SÃO MAMEDE | PARAÍBA | Brasil | 2514909 | 25 | 33 | nan | nan | nan | Caatinga | nan |
| a1e73b1d-5709-38b0-8106-c06b0544340e | -4.6695 | -44.9655 | 2024-11-27 00:21:00 | METOP-C | LAGO DOS RODRIGUES | MARANHÃO | Brasil | 2105948 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 69f23ee3-9c85-3708-8bef-1f0724e9fa66 | -1.7638 | -52.7397 | 2024-11-27 00:21:00 | METOP-C | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 05e0cbfb-da8f-3f1d-a3c1-427dcc791ccc | -2.56 | -47.4711 | 2024-11-27 00:21:00 | METOP-C | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ff6c26a7-440d-3746-b502-1ce819d52c5d | -3.877 | -50.592602 | 2024-11-27 00:21:00 | METOP-C | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b03868e6-2580-3544-90d6-bea77a516147 | -2.6722 | -45.6548 | 2024-11-27 00:21:00 | METOP-C | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 90bf19c6-d760-3291-8f07-894bfff7b6dd | -4.1247 | -43.7971 | 2024-11-27 00:21:00 | METOP-C | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 2b6c43ef-084c-36e9-a452-7bf96848f52b | -2.8213 | -45.494499 | 2024-11-27 00:21:00 | METOP-C | SANTA HELENA | MARANHÃO | Brasil | 2109809 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| e1c54957-eeb5-35dc-8bec-46cb8b5fab4c | -3.0237 | -53.268002 | 2024-11-27 00:21:00 | METOP-C | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 73da7c81-9d9c-3a9a-b767-c6db8cb7bf4c | -2.1438 | -53.7439 | 2024-11-27 00:21:00 | METOP-C | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3c516ab6-5267-36b8-bc08-88269ad8e965 | -2.1535 | -53.741699 | 2024-11-27 00:21:00 | METOP-C | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a379e086-4ebb-3230-8f3e-5082282ff0a4 | -2.8014 | -46.811199 | 2024-11-27 00:21:00 | METOP-C | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2a70dc62-a9ab-3073-a124-86bfb950811f | -1.4188 | -47.1171 | 2024-11-27 00:21:00 | METOP-C | OURÉM | PARÁ | Brasil | 1505403 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0947ce2f-f6c4-3dd6-af7b-872424b83278 | -2.8505 | -45.170502 | 2024-11-27 00:21:00 | METOP-C | SÃO BENTO | MARANHÃO | Brasil | 2110500 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| a928ed5c-e43a-3a22-be48-5772a2c6f19e | -3.7944 | -44.336899 | 2024-11-27 00:21:00 | METOP-C | MATÕES DO NORTE | MARANHÃO | Brasil | 2106631 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| f64bcf81-be68-38a9-bb5d-d948e803011a | -2.6755 | -45.669102 | 2024-11-27 00:21:00 | METOP-C | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 92c858ef-5b40-337a-ac09-f9690fd95129 | -4.3809 | -44.1054 | 2024-11-27 00:21:00 | METOP-C | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| f7288084-2a1b-34cb-9fd8-e794a55bd232 | -3.8149 | -45.921501 | 2024-11-27 00:21:00 | METOP-C | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 7347c6e8-240a-3851-9963-34475dbe9d3a | -3.0729 | -53.214699 | 2024-11-27 00:21:00 | METOP-C | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7a703847-c5a1-3b31-9ce0-8c9096df6d59 | -4.2805 | -48.080002 | 2024-11-27 00:21:00 | METOP-C | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 13e2d2bc-08d4-31c8-815e-fea0544b9ecd | -3.9984 | -45.549801 | 2024-11-27 00:21:00 | METOP-C | ALTAMIRA DO MARANHÃO | MARANHÃO | Brasil | 2100402 | 21 | 33 | nan | nan | nan | Amazônia | nan |


[Clique aqui para ver as próximas entradas](README6.md)
