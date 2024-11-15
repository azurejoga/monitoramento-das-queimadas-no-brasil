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
| a3ddf98c-33d8-3445-b9d1-8576518c64de | -3.1468 | -45.1827 | 2024-11-15 04:10:00 | GOES-16 | VIANA | MARANHÃO | Brasil | 2112803 | 21 | 33 | nan | nan | nan | Amazônia | 64.8 |
| 0b277b66-c5c4-3268-a777-87d3f52b1c3c | 1.3035 | -60.4074 | 2024-11-15 04:10:00 | GOES-16 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 40.9 |
| e4a9593d-872c-31a4-b493-036ea4dea0f6 | -17.2543 | -57.4698 | 2024-11-15 04:10:00 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 135.1 |
| bfa66eef-1313-37cb-bc87-d894baa5beea | -17.5882 | -57.4711 | 2024-11-15 04:10:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 97.9 |
| 5fcea765-fe50-31f9-9213-40179aafd588 | -3.1469 | -45.1602 | 2024-11-15 04:10:00 | GOES-16 | VIANA | MARANHÃO | Brasil | 2112803 | 21 | 33 | nan | nan | nan | Amazônia | 118.5 |
| c61f6d33-c307-36b4-bfd2-2706a0083713 | -17.2347 | -57.4721 | 2024-11-15 04:10:00 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 71.4 |
| c9402c02-8593-30ad-a8db-9ce14b9157fb | -17.5879 | -57.4917 | 2024-11-15 04:20:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 66.1 |
| 07acfe52-5b76-3b3b-8ca2-7771886e0ee3 | -17.2347 | -57.4721 | 2024-11-15 04:20:00 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 64.6 |
| 7aea2284-3aaa-30fd-8aa4-926e22b4b686 | -17.5869 | -57.5533 | 2024-11-15 04:20:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 147.8 |
| af5c8bef-0e65-35ac-8ef7-d79f0419f9d8 | -17.5882 | -57.4711 | 2024-11-15 04:20:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 107.8 |
| 13c7a0bb-de24-37b2-b927-8b1e762711d6 | -17.626 | -57.5692 | 2024-11-15 04:20:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 53.0 |
| fcb631e3-509f-38ac-967b-11abb7692da3 | -17.5668 | -57.5762 | 2024-11-15 04:20:00 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 65.8 |
| 13ae4d25-ce3b-39dd-98f6-6ba834bdf5d9 | -17.5672 | -57.5557 | 2024-11-15 04:20:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 97.4 |
| 94fa3c2d-1d4e-3c15-9e14-6326e5e09edd | -17.2547 | -57.4493 | 2024-11-15 04:20:00 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 106.0 |
| d4f26e30-ef9f-3360-abbd-c2c1a5c45ea1 | -17.274 | -57.4675 | 2024-11-15 04:20:00 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 55.3 |
| b288522f-2e92-33a2-ae36-023dd8794f3e | -17.2543 | -57.4698 | 2024-11-15 04:20:00 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 126.4 |
| 7500129e-49cc-3066-a716-0a12b838a640 | -17.646 | -57.5463 | 2024-11-15 04:20:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 74.6 |
| 12a7ed6d-9109-3861-90bc-4cec5aee15a0 | -17.6263 | -57.5486 | 2024-11-15 04:20:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 109.5 |
| 21eac9fd-d6a7-3b3a-8ec9-dbddb22c2911 | -17.5675 | -57.5351 | 2024-11-15 04:20:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 120.7 |
| 19bfbb6d-779e-3001-bf62-0848d4262ade | -17.5678 | -57.5146 | 2024-11-15 04:20:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 74.1 |
| c036f4df-467f-3b09-a7c4-dee579dab4d4 | -17.7052 | -57.5392 | 2024-11-15 04:20:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 58.5 |
| 6a41b04f-d659-3212-9abe-5fc923cafe75 | -17.5865 | -57.5739 | 2024-11-15 04:20:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 156.7 |
| aa4c3f45-162c-3426-8d1c-821dba4ba181 | -17.235 | -57.4516 | 2024-11-15 04:20:00 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 73.7 |
| 4e0d79bb-f534-3f0b-b78e-e4fa2377b1ad | -2.64686 | -46.16431 | 2024-11-15 04:21:00 | NOAA-21 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1446353a-84a2-3ca6-97ac-6e8cd21e3a83 | -2.65367 | -46.18839 | 2024-11-15 04:21:00 | NOAA-21 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 62af2cd6-3503-3e24-8b5f-73b283ddb36f | -2.52338 | -46.12268 | 2024-11-15 04:21:00 | NOAA-21 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e1f94fcf-04b6-3703-96c0-9986626b9495 | -2.38364 | -54.64632 | 2024-11-15 04:21:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| db678e27-9fc1-3b37-acee-67b1dc01f048 | -2.32916 | -46.87458 | 2024-11-15 04:21:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 5b188c78-3a0e-3245-88d6-017dde557d3b | -4.39255 | -43.69831 | 2024-11-15 04:21:00 | NOAA-21 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 171400b6-ebdc-3012-b99b-5efcb77b6d7c | -2.09477 | -46.36448 | 2024-11-15 04:21:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b3d7fb9d-a2c4-302d-8633-0d99317ef02d | -2.63243 | -46.18892 | 2024-11-15 04:21:00 | NOAA-21 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 66c90270-876e-33f9-8d85-ebf1bf2ddbbb | -2.64217 | -46.19429 | 2024-11-15 04:21:00 | NOAA-21 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 18f960f1-f6b3-37ed-b9aa-d82c0103684c | -2.66458 | -46.18625 | 2024-11-15 04:21:00 | NOAA-21 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 3.4 |
| d16022d2-6e7e-3245-8210-cf64a39d82e2 | -2.66056 | -46.18946 | 2024-11-15 04:21:00 | NOAA-21 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 28837bd7-46cc-346a-b2c3-4a60e53d4d62 | -2.6577 | -46.18518 | 2024-11-15 04:21:00 | NOAA-21 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 27fcd029-7e51-3e92-a88b-28110581b6cb | -2.6462 | -46.19107 | 2024-11-15 04:21:00 | NOAA-21 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 7201669b-7bdc-30a6-9930-cfa6bb646b7a | -3.2487 | -45.92807 | 2024-11-15 04:21:00 | NOAA-21 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5823c39e-672d-3cfd-b93c-fa941d04f3a2 | -2.66283 | -46.19754 | 2024-11-15 04:21:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 1fd1d46f-975b-3c54-8c77-e0da8121727b | -2.63889 | -46.14774 | 2024-11-15 04:21:00 | NOAA-21 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 3b7486a2-af0d-3bf6-b624-93fa1ac6bb98 | 0.11802 | -49.85023 | 2024-11-15 04:21:00 | NOAA-21 | CHAVES | PARÁ | Brasil | 1502509 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 97720e18-1120-378a-9522-29275126a79f | -2.63691 | -46.55666 | 2024-11-15 04:21:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e3ac194a-273b-34a0-854f-8837e45d16d1 | -4.01404 | -43.24224 | 2024-11-15 04:21:00 | NOAA-21 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 438ef0ec-682a-32f1-9246-7eea6ed2053d | -2.3733 | -54.63598 | 2024-11-15 04:21:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| bc0a4770-2700-3c82-9940-f2b86307b7a5 | -2.63873 | -46.19375 | 2024-11-15 04:21:00 | NOAA-21 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 2.3 |
| b9a65b57-1309-3739-9fbe-92e8c4fc9812 | -1.91302 | -45.4541 | 2024-11-15 04:21:00 | NOAA-21 | TURIAÇU | MARANHÃO | Brasil | 2112407 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b0d9cfa7-1d27-3f6b-a1c4-8a0584a2df78 | -2.65887 | -46.17768 | 2024-11-15 04:21:00 | NOAA-21 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 498445ba-07aa-31bf-b909-8d3e618ff713 | -4.4572 | -43.91827 | 2024-11-15 04:21:00 | NOAA-21 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 0.3 |
| 64c7597d-6ac6-3aab-a2cb-c697eabdbd0f | -2.65023 | -46.18785 | 2024-11-15 04:21:00 | NOAA-21 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| e095cb0a-9365-380b-a3c2-132ebb08fac4 | -4.01645 | -38.24692 | 2024-11-15 04:21:00 | NOAA-21 | AQUIRAZ | CEARÁ | Brasil | 2301000 | 23 | 33 | nan | nan | nan | Caatinga | 5.6 |
| 412b78a3-8dd6-3d12-855c-f3ec90545240 | -2.64744 | -46.16057 | 2024-11-15 04:21:00 | NOAA-21 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 6141588b-cf17-3d04-a803-86642fa2de1a | -2.6404 | -46.55719 | 2024-11-15 04:21:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c6ea549d-49d8-3dad-9b2b-25147a1995a5 | -2.62957 | -46.18463 | 2024-11-15 04:21:00 | NOAA-21 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 0d51edc8-2c54-30be-b3c4-c5c22d5b630d | -1.9838 | -46.3676 | 2024-11-15 04:21:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 9e147c16-7330-31b9-8f67-bb455e00a3fd | -3.14649 | -45.16604 | 2024-11-15 04:21:00 | NOAA-21 | VIANA | MARANHÃO | Brasil | 2112803 | 21 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 8292e9a2-905c-33ff-b5ae-b2689ed6879f | -2.64971 | -46.16859 | 2024-11-15 04:21:00 | NOAA-21 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 43322ce5-cb85-321a-929b-d4763172011f | -2.18876 | -46.15257 | 2024-11-15 04:21:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e5e7fda0-8eea-31e5-8ed3-2c5b47ad0a20 | -1.14323 | -47.6925 | 2024-11-15 04:21:00 | NOAA-21 | IGARAPÉ-AÇU | PARÁ | Brasil | 1503200 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e5fcc270-3119-31a9-b905-7103d84a9ea0 | -1.70961 | -46.16101 | 2024-11-15 04:21:00 | NOAA-21 | BOA VISTA DO GURUPI | MARANHÃO | Brasil | 2101970 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| deb99ebf-c966-3110-86cd-58645bdea3df | -4.32097 | -43.63388 | 2024-11-15 04:21:00 | NOAA-21 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| f56d8acf-c85c-317e-9747-f0deed21ec7d | -3.88598 | -43.15008 | 2024-11-15 04:21:00 | NOAA-21 | BURITI | MARANHÃO | Brasil | 2102200 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 751d8d09-f97c-3d85-9b81-ca88526051da | -3.71422 | -41.68972 | 2024-11-15 04:21:00 | NOAA-21 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 3.7 |
| 77978bf6-2fd6-345f-89f1-e5b3a8feb6b5 | -2.64913 | -46.17233 | 2024-11-15 04:21:00 | NOAA-21 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| fca0fc05-dca2-3e96-a2ee-15a503e6e87c | -2.98815 | -45.86885 | 2024-11-15 04:21:00 | NOAA-21 | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| c63001a4-f971-3593-986d-6eca0d4743b2 | -4.01584 | -38.25109 | 2024-11-15 04:21:00 | NOAA-21 | AQUIRAZ | CEARÁ | Brasil | 2301000 | 23 | 33 | nan | nan | nan | Caatinga | 5.1 |
| f880c074-8785-3e8b-9914-bb736afa405a | -3.1437 | -45.16203 | 2024-11-15 04:21:00 | NOAA-21 | VIANA | MARANHÃO | Brasil | 2112803 | 21 | 33 | nan | nan | nan | Amazônia | 12.4 |
| fbc92cd3-9187-37ad-8cdc-28afb123638c | -2.32623 | -46.87005 | 2024-11-15 04:21:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 00849916-ce85-38ce-939f-67de1afe326a | -3.09828 | -45.97169 | 2024-11-15 04:21:00 | NOAA-21 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 40761568-898e-34d3-b91b-3d89617d8066 | -4.45773 | -43.91482 | 2024-11-15 04:21:00 | NOAA-21 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 8247a5c5-f934-3acb-b2f2-98a16843ac63 | -2.64276 | -46.19053 | 2024-11-15 04:21:00 | NOAA-21 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| bebbe50f-6e76-3e8f-bd14-c3ce2d3cbab0 | -2.72342 | -44.78228 | 2024-11-15 04:21:00 | NOAA-21 | BACURITUBA | MARANHÃO | Brasil | 2101350 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| fa20699e-09c3-31a1-9810-fda5d107f84e | -3.14261 | -45.16903 | 2024-11-15 04:21:00 | NOAA-21 | VIANA | MARANHÃO | Brasil | 2112803 | 21 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 4739f9ed-9476-3b70-95f0-f25b49750bef | -2.34305 | -47.22106 | 2024-11-15 04:21:00 | NOAA-21 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 75c800d1-92bc-37ac-93c6-21d649d09fd2 | -2.63931 | -46.18999 | 2024-11-15 04:21:00 | NOAA-21 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| dffe7b3a-1a36-3921-819a-f43dd5a8f529 | -2.66231 | -46.17822 | 2024-11-15 04:21:00 | NOAA-21 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f024c6ec-0c49-3964-a498-26bff27027c0 | -2.66101 | -46.83799 | 2024-11-15 04:21:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| bc71c2a3-0e53-3ad9-9577-8b4fe29e5639 | -1.6269 | -46.15273 | 2024-11-15 04:21:00 | NOAA-21 | CARUTAPERA | MARANHÃO | Brasil | 2102903 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 56435c5b-15e2-3836-8974-016656f14c70 | -2.98476 | -45.86833 | 2024-11-15 04:21:00 | NOAA-21 | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 090b18d7-b6af-32a0-aaca-1e284f50977e | -2.65594 | -46.19644 | 2024-11-15 04:21:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 8450c2c1-0a24-306d-b76f-9c9c03589320 | -1.90198 | -46.4783 | 2024-11-15 04:21:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 22f516b9-69b3-3617-9102-43c96e0cc82c | -2.3023 | -46.45053 | 2024-11-15 04:21:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8da4fc10-2bc6-35a3-b2d6-3daf8eff3190 | -2.09841 | -46.32957 | 2024-11-15 04:21:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b7d8af11-f5f8-3d85-b1b9-53a7d5889bb4 | -3.24397 | -45.38716 | 2024-11-15 04:21:00 | NOAA-21 | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | 0.3 |
| 255372a3-7749-35bd-8a22-19e9539d9109 | -2.62336 | -46.82386 | 2024-11-15 04:21:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| a6e73ed4-a19e-39c3-b140-e50bb5fd1437 | -2.23366 | -46.83616 | 2024-11-15 04:21:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a49855af-da7f-36bd-add5-453a95af4793 | -3.79478 | -43.91384 | 2024-11-15 04:21:00 | NOAA-21 | VARGEM GRANDE | MARANHÃO | Brasil | 2112704 | 21 | 33 | nan | nan | nan | Cerrado | 5.2 |
| ab93f35b-2a0d-387e-b951-209bf445b5a9 | -3.09943 | -45.96438 | 2024-11-15 04:21:00 | NOAA-21 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f8e97f83-fa02-35cd-8d27-324e5b7dde92 | -2.90813 | -46.85818 | 2024-11-15 04:21:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 67887043-96ed-33a3-8b38-cec45361dc19 | -2.6336 | -46.18142 | 2024-11-15 04:21:00 | NOAA-21 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| b185f43a-baf7-3779-bf10-e26b87275b6a | -2.56207 | -46.01037 | 2024-11-15 04:21:00 | NOAA-21 | MARANHÃOZINHO | MARANHÃO | Brasil | 2106375 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ea5fa58d-7939-3d9b-a5db-84444c9fa3ae | -2.65938 | -46.19699 | 2024-11-15 04:21:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 866095ab-2377-38f8-8bb6-1c062a42d308 | -1.71021 | -46.15721 | 2024-11-15 04:21:00 | NOAA-21 | BOA VISTA DO GURUPI | MARANHÃO | Brasil | 2101970 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0c1d6c2f-af8f-32e1-8422-4dc8dccbe5eb | -4.39811 | -43.70629 | 2024-11-15 04:21:00 | NOAA-21 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 5ebf017a-5b6b-3210-b3ac-b39c7982fcc6 | -3.61669 | -44.79104 | 2024-11-15 04:21:00 | NOAA-21 | ARARI | MARANHÃO | Brasil | 2101004 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 6645d611-8883-3906-9089-848b949ed040 | -2.63424 | -46.52842 | 2024-11-15 04:21:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a2a369cc-3144-33ba-932f-e15c55d2d424 | -2.63587 | -46.18945 | 2024-11-15 04:21:00 | NOAA-21 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| a307b828-2f3b-3541-aef1-530b48cff518 | -2.664 | -46.19001 | 2024-11-15 04:21:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 2.9 |
| cc8592f8-4284-3fa0-8c62-1deb738ee4b6 | -4.10369 | -38.74137 | 2024-11-15 04:21:00 | NOAA-21 | GUAIÚBA | CEARÁ | Brasil | 2304954 | 23 | 33 | nan | nan | nan | Caatinga | 4.9 |
| a55590f1-3bfd-31cf-a470-bf50c02fcab8 | -1.34503 | -46.56083 | 2024-11-15 04:21:00 | NOAA-21 | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f881853d-fca0-3976-9c29-2646c232a3e4 | -3.14316 | -45.16553 | 2024-11-15 04:21:00 | NOAA-21 | VIANA | MARANHÃO | Brasil | 2112803 | 21 | 33 | nan | nan | nan | Amazônia | 12.4 |
| d482425f-7ee5-36ac-a37d-3db6ec2de2c7 | 1.07267 | -51.14527 | 2024-11-15 04:21:00 | NOAA-21 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 3.6 |


[Clique aqui para ver as próximas entradas](README12.md)
