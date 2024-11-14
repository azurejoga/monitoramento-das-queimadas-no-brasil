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

## Dados Diários - Página 2

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| e1d7bfde-f4de-3a66-9978-99bfacf0d294 | -3.0504 | -50.3332 | 2024-11-14 00:10:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 60.5 |
| 5702c46d-60aa-301b-a09c-abf3dabcf9b0 | -1.3894 | -51.1197 | 2024-11-14 00:10:00 | GOES-16 | MELGAÇO | PARÁ | Brasil | 1504505 | 15 | 33 | nan | nan | nan | Amazônia | 110.8 |
| 70608586-fcd7-368f-a9b7-e12ad5e56694 | -17.2543 | -57.4698 | 2024-11-14 00:10:00 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 78.5 |
| 7568a8b3-9720-3e64-bb0e-4826d41fec97 | -2.8975 | -51.7927 | 2024-11-14 00:10:00 | GOES-16 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 54.6 |
| ddc939bc-c834-32be-98c3-81f75c2c12dc | -17.6066 | -57.551 | 2024-11-14 00:10:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 73.2 |
| 6b7f9b41-3775-34f4-a0c7-d94e5859bf30 | -2.6751 | -46.9783 | 2024-11-14 00:10:00 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 102.4 |
| 629e58ee-f9b4-346b-9668-bd1cc6630e3e | -1.3873 | -52.376 | 2024-11-14 00:10:00 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 80.6 |
| 6cb63c40-d60b-3b96-86e0-4c177c6c35f1 | 1.2852 | -60.4454 | 2024-11-14 00:10:00 | GOES-16 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 52.0 |
| 66d8233e-ed3d-3b67-b7d6-46aef65ec1af | -17.5869 | -57.5533 | 2024-11-14 00:10:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 216.1 |
| 8be02392-b498-38f3-9744-3e9c9232f776 | -2.0267 | -46.9519 | 2024-11-14 00:10:00 | GOES-16 | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | 63.9 |
| 91fa3cdd-6043-332f-a015-285f351d1c93 | 1.0663 | -60.5985 | 2024-11-14 00:10:00 | GOES-16 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 50.6 |
| 18700cdb-9d8e-3509-a7a6-b91b4c9b766e | -3.4014 | -50.3011 | 2024-11-14 00:10:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 55.1 |
| 7e5e648b-97f5-336b-91b0-0f0a8310b4f7 | -17.5675 | -57.5351 | 2024-11-14 00:10:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 108.1 |
| 3e6105eb-5703-3fb2-912b-c7be387c6b8d | 1.2852 | -60.4265 | 2024-11-14 00:10:00 | GOES-16 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 57.2 |
| 51b0c56b-c89d-3621-8244-786fa0244c5a | -2.8792 | -51.7726 | 2024-11-14 00:10:00 | GOES-16 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 50.1 |
| c16074d3-94a0-3bb0-860b-84b4e77914d5 | -17.5872 | -57.5328 | 2024-11-14 00:10:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 118.4 |
| a293264a-5fe5-302d-a3b4-510ea8077b3c | -3.7333 | -50.4364 | 2024-11-14 00:10:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 47.3 |
| fdc318b9-e88a-3063-a610-e819c6a0465e | -0.8918 | -51.7245 | 2024-11-14 00:10:00 | GOES-16 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 53.7 |
| d0f85d8f-c4d2-3f8f-b39d-2471913a7614 | -4.3755 | -48.0665 | 2024-11-14 00:10:00 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 49.2 |
| ceaa64bb-239c-39c5-87e0-9e1f0533aaa1 | -9.4792 | -35.7156 | 2024-11-14 00:10:00 | GOES-16 | MACEIÓ | ALAGOAS | Brasil | 2704302 | 27 | 33 | nan | nan | nan | Mata Atlântica | 86.4 |
| d3ab730c-c89c-359d-b0ad-4228837d2637 | 1.048 | -60.5986 | 2024-11-14 00:10:00 | GOES-16 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 59.8 |
| 9004bb27-c0ca-3c99-88be-7728bb9a1658 | -3.1464 | -45.2729 | 2024-11-14 00:10:00 | GOES-16 | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | 117.6 |
| 52effd0b-225b-38ff-83f3-c266a1dbb781 | -3.4198 | -50.3005 | 2024-11-14 00:10:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 58.3 |
| 3c81f00d-6f4e-3d75-a76d-6a2ecd2db433 | -1.3895 | -51.099 | 2024-11-14 00:10:00 | GOES-16 | MELGAÇO | PARÁ | Brasil | 1504505 | 15 | 33 | nan | nan | nan | Amazônia | 64.9 |
| 02a9a4da-48d7-37f1-b862-a71be1370cbc | -2.6992 | -45.5585 | 2024-11-14 00:10:00 | GOES-16 | SANTA HELENA | MARANHÃO | Brasil | 2109809 | 21 | 33 | nan | nan | nan | Amazônia | 75.9 |
| 6380d135-1ea8-3370-95b6-45b420b86b48 | -2.6411 | -46.1627 | 2024-11-14 00:10:00 | GOES-16 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 67.6 |
| a3e15a0e-18b6-3660-a7a0-d265ab43b385 | -3.1244 | -50.31 | 2024-11-14 00:10:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 74.4 |
| 22c62568-bbec-319f-b0c1-9f337f0b74e1 | -3.271 | -50.5778 | 2024-11-14 00:10:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 46.4 |
| c4f144be-f555-3685-8951-eb84b42847f4 | -1.3874 | -52.3555 | 2024-11-14 00:10:00 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 93.8 |
| 0e110c88-1398-3f37-9029-b1b77e1220f1 | -2.0268 | -46.9299 | 2024-11-14 00:10:00 | GOES-16 | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | 114.7 |
| 9006972e-4d71-3182-898e-67df8fbbae9d | -3.0523 | -45.5237 | 2024-11-14 00:10:00 | GOES-16 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 94.9 |
| 1f5a648f-754c-3b6a-b33d-97e3f7a5fb2c | -2.675 | -47.0003 | 2024-11-14 00:10:00 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 101.5 |
| 3c38d23f-2e6e-3a42-a086-1959ad8e4dd8 | -3.4755 | -50.2566 | 2024-11-14 00:10:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 53.5 |
| a9a31ef0-dc9b-30c5-bb2f-a83a0bbd929a | -3.1463 | -45.2954 | 2024-11-14 00:10:00 | GOES-16 | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | 72.6 |
| fd23fa12-4e87-3502-89fa-57f55ddf19a9 | -0.8918 | -51.7245 | 2024-11-14 00:20:00 | GOES-16 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 58.3 |
| 7ae37fb8-db76-399f-b5f8-c9f740f1b7c7 | -1.6627 | -52.5561 | 2024-11-14 00:20:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 84.1 |
| 088db554-0836-3542-bd3c-e6b89b1f8e41 | 1.3034 | -60.4263 | 2024-11-14 00:20:00 | GOES-16 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 57.4 |
| 399a967a-6362-32e8-b29f-37b16c2f8be8 | -3.1463 | -45.2954 | 2024-11-14 00:20:00 | GOES-16 | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | 71.6 |
| 6d1b9151-33b0-3bcb-91d8-1cd3495dec7e | -4.0191 | -45.5494 | 2024-11-14 00:20:00 | GOES-16 | ALTAMIRA DO MARANHÃO | MARANHÃO | Brasil | 2100402 | 21 | 33 | nan | nan | nan | Amazônia | 111.2 |
| d294fcd5-b63e-37cc-9dd8-2bd31bdf28db | -2.6565 | -46.9789 | 2024-11-14 00:20:00 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 98.1 |
| 96d97ce2-f95f-3e57-b5ce-fe1c52d89c97 | -2.675 | -47.0003 | 2024-11-14 00:20:00 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 117.0 |
| b6c5be10-843c-3548-a853-4289df62231d | -4.0005 | -45.5503 | 2024-11-14 00:20:00 | GOES-16 | ALTAMIRA DO MARANHÃO | MARANHÃO | Brasil | 2100402 | 21 | 33 | nan | nan | nan | Amazônia | 145.8 |
| b8a24330-79bb-3cab-b463-e3990af6619e | -0.34 | -52.0359 | 2024-11-14 00:20:00 | GOES-16 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 39.8 |
| 3e7991a3-cbb0-300e-9493-ddf65ac6d4e7 | -17.6076 | -57.4893 | 2024-11-14 00:20:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 53.0 |
| 999cf77d-c0fb-3e88-bfa1-1bb57392a1dd | -2.898 | -46.8614 | 2024-11-14 00:20:00 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 73.0 |
| e00285ed-e914-3236-b8d3-fb52eafaf2c4 | -4.0682 | -50.0029 | 2024-11-14 00:20:00 | GOES-16 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 48.3 |
| e6faa781-d762-3a36-bf25-3b8d45c4f416 | -2.0267 | -46.9519 | 2024-11-14 00:20:00 | GOES-16 | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | 70.7 |
| c40232ef-50e0-31ff-aef9-e8d09dff6428 | -3.5194 | -52.9218 | 2024-11-14 00:20:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 55.0 |
| 6f3454ee-8231-37b4-aeea-08d621301966 | -2.8791 | -51.7932 | 2024-11-14 00:20:00 | GOES-16 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 118.2 |
| bc087b7d-4734-3754-8eca-b40e318d9fb0 | -2.0268 | -46.9299 | 2024-11-14 00:20:00 | GOES-16 | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | 132.9 |
| 508ece7b-c002-300e-997a-66718fe2d24a | -1.4078 | -51.1195 | 2024-11-14 00:20:00 | GOES-16 | MELGAÇO | PARÁ | Brasil | 1504505 | 15 | 33 | nan | nan | nan | Amazônia | 69.6 |
| 4981d020-a47a-31cd-940a-cbf908bbf69d | -1.3873 | -52.376 | 2024-11-14 00:20:00 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 77.8 |
| 4a2957fd-69dc-36be-a507-4155b8dcaf0b | -3.714 | -50.6046 | 2024-11-14 00:20:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 53.7 |
| 0143fac4-b19a-3479-b1a8-d21c086a85dc | 1.2852 | -60.4265 | 2024-11-14 00:20:00 | GOES-16 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 62.4 |
| de2f456f-b17b-3845-b86d-0f6b18782ec7 | -3.6402 | -50.5863 | 2024-11-14 00:20:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 71.0 |
| 7311b0f2-68a9-3371-829c-6c8378029fa3 | 1.2852 | -60.4454 | 2024-11-14 00:20:00 | GOES-16 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 54.1 |
| 034c42ca-8f9c-37ee-8ff4-7d3e0d5965d9 | -2.6288 | -49.523 | 2024-11-14 00:20:00 | GOES-16 | MOCAJUBA | PARÁ | Brasil | 1504604 | 15 | 33 | nan | nan | nan | Amazônia | 48.3 |
| 080cb418-55fe-3bb3-a5fb-a7c4a1ab7796 | -4.145 | -46.2578 | 2024-11-14 00:20:00 | GOES-16 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 72.9 |
| 54467221-8baf-3b2e-89a5-163efb4b0b12 | -1.369 | -52.3558 | 2024-11-14 00:20:00 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 76.3 |
| fbddbbff-ce95-39a5-b201-cec837e11f7a | -3.4014 | -50.3011 | 2024-11-14 00:20:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 53.3 |
| 5d610708-6cf1-3f42-a548-62c2cca7985a | -1.3895 | -51.099 | 2024-11-14 00:20:00 | GOES-16 | MELGAÇO | PARÁ | Brasil | 1504505 | 15 | 33 | nan | nan | nan | Amazônia | 55.5 |
| 632ef95f-03e4-3cca-af9c-8ca768f9b83e | -17.2543 | -57.4698 | 2024-11-14 00:20:00 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 73.3 |
| c0dba85b-dd2b-3d0b-8263-8db010c2ed53 | -1.3894 | -51.1197 | 2024-11-14 00:20:00 | GOES-16 | MELGAÇO | PARÁ | Brasil | 1504505 | 15 | 33 | nan | nan | nan | Amazônia | 88.5 |
| b8080f86-2953-3fb4-9c12-28be65b7e762 | -3.1464 | -45.2729 | 2024-11-14 00:20:00 | GOES-16 | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | 97.9 |
| 408d149a-2d2a-3292-8758-3bd4ff4d67ba | -3.4198 | -50.3005 | 2024-11-14 00:20:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 48.7 |
| 48a8d1eb-4dae-38f2-9085-b7d2d883ccae | -6.0472 | -44.0331 | 2024-11-14 00:20:00 | GOES-16 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 82.4 |
| 8c9165ca-e6d5-3002-94e7-a8f8523d62ec | -3.7333 | -50.4364 | 2024-11-14 00:20:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 53.8 |
| c3c64ea9-baff-3c78-bd0b-1684096c0649 | -4.0003 | -45.5728 | 2024-11-14 00:20:00 | GOES-16 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 218.0 |
| 635eecc0-ec1a-30ff-af29-6fca600c0cc6 | -3.1244 | -50.31 | 2024-11-14 00:20:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 67.0 |
| 571dc657-19f2-3286-8d42-ff52167fd09b | -3.3359 | -52.7847 | 2024-11-14 00:20:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 54.5 |
| 69e5155a-56cf-384a-bca8-2ff61bd03b77 | -3.0504 | -50.3332 | 2024-11-14 00:20:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 56.3 |
| 414aa7d6-7327-3c3c-90fa-cb0d311f354d | -2.6751 | -46.9783 | 2024-11-14 00:20:00 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 129.0 |
| c924de5c-0286-34a9-a23f-98b96fbb8fbc | -4.0189 | -45.5719 | 2024-11-14 00:20:00 | GOES-16 | ALTAMIRA DO MARANHÃO | MARANHÃO | Brasil | 2100402 | 21 | 33 | nan | nan | nan | Amazônia | 166.8 |
| 889e12c6-2637-35aa-8902-84d0b5c8ec7d | -1.3874 | -52.3555 | 2024-11-14 00:20:00 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 92.2 |
| db1af7f9-cafd-3f85-aeb7-8f7f2e97ef58 | -3.0358 | -45.0741 | 2024-11-14 00:20:00 | GOES-16 | MATINHA | MARANHÃO | Brasil | 2106508 | 21 | 33 | nan | nan | nan | Amazônia | 104.7 |
| dab05785-2c29-3461-af58-f6604f8edc3c | -17.7052 | -57.5392 | 2024-11-14 00:20:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 52.4 |
| 63841d3d-bcd7-35ba-b7cf-91f1f7f09e5f | -3.0523 | -45.5237 | 2024-11-14 00:20:00 | GOES-16 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 99.9 |
| ff723634-5b6a-340a-a89e-76a9f8cf7f22 | -2.6564 | -47.0008 | 2024-11-14 00:20:00 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 93.2 |
| 9e6365d9-23f4-35b5-8b15-fff040ec5b28 | -4.1451 | -46.2356 | 2024-11-14 00:20:00 | GOES-16 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 73.3 |
| a947d75c-19ea-38a1-b65a-6dfc79bb1dce | -3.271 | -50.5778 | 2024-11-14 00:20:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 45.8 |
| a40adf47-3fb0-3107-b457-6c4f7066cccf | -3.0522 | -45.5461 | 2024-11-14 00:20:00 | GOES-16 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 63.0 |
| 5cf0efc5-e0e6-3245-91cc-678c38f43fde | -6.0472 | -44.0331 | 2024-11-14 00:30:00 | GOES-16 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 79.6 |
| 9581f66f-163b-354d-b6da-0a491cc6fdda | 1.2852 | -60.4265 | 2024-11-14 00:30:00 | GOES-16 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 71.3 |
| 84a8bb84-055e-3614-a1e3-6ff8832b0f9d | -17.7052 | -57.5392 | 2024-11-14 00:30:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 49.7 |
| 852581fe-6506-34cc-9395-5db66edd37cc | -2.0267 | -46.9519 | 2024-11-14 00:30:00 | GOES-16 | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | 59.4 |
| cfca8a0a-52bf-34b1-93ec-401a89cb690d | -1.3894 | -51.1197 | 2024-11-14 00:30:00 | GOES-16 | MELGAÇO | PARÁ | Brasil | 1504505 | 15 | 33 | nan | nan | nan | Amazônia | 103.1 |
| f6f0128a-df18-3b3c-9de2-ff0d272c7aa1 | -4.145 | -46.2578 | 2024-11-14 00:30:00 | GOES-16 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 71.0 |
| 6a65b259-c26b-33a2-b526-a268787620bc | -17.5872 | -57.5328 | 2024-11-14 00:30:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 108.7 |
| 816f2af5-e36c-3d3d-868a-2f88367d11a4 | -3.3358 | -52.805 | 2024-11-14 00:30:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 54.4 |
| bf9b2048-8022-3c5e-9e59-a4a7f9aecc39 | -3.1278 | -45.2736 | 2024-11-14 00:30:00 | GOES-16 | VIANA | MARANHÃO | Brasil | 2112803 | 21 | 33 | nan | nan | nan | Amazônia | 66.0 |
| 699f186e-d8e8-3d84-8580-c29b224b0906 | 1.2852 | -60.4454 | 2024-11-14 00:30:00 | GOES-16 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 62.8 |
| b138620f-8042-3279-8dbb-c8ec77ee3249 | -17.5675 | -57.5351 | 2024-11-14 00:30:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 107.8 |
| 561f6874-388e-30b8-b9e7-f43adcf54135 | -3.0504 | -50.3332 | 2024-11-14 00:30:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 58.7 |
| 5422445e-cfc8-330a-a292-29fb955c2b57 | -3.4198 | -50.3005 | 2024-11-14 00:30:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 53.7 |
| 6ca253d4-6123-3a2c-aa01-edc1a0a195a0 | -3.1244 | -50.31 | 2024-11-14 00:30:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 71.0 |
| a7bb1f82-e6af-365a-a020-6d9140fe983e | -4.0191 | -45.5494 | 2024-11-14 00:30:00 | GOES-16 | ALTAMIRA DO MARANHÃO | MARANHÃO | Brasil | 2100402 | 21 | 33 | nan | nan | nan | Amazônia | 112.8 |
| 2ed9fad1-2963-31b7-9c0f-8d255b9d38d7 | -4.0003 | -45.5728 | 2024-11-14 00:30:00 | GOES-16 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 164.3 |
| e1d75456-7af8-38ee-aab0-634e9861065c | -1.3895 | -51.099 | 2024-11-14 00:30:00 | GOES-16 | MELGAÇO | PARÁ | Brasil | 1504505 | 15 | 33 | nan | nan | nan | Amazônia | 50.0 |
| ef2c2796-25d7-3c1e-b175-72693ffc6a57 | -1.3874 | -52.3555 | 2024-11-14 00:30:00 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 77.7 |
| 8552d3a3-9be3-3871-bae6-f47024787c02 | -1.3873 | -52.376 | 2024-11-14 00:30:00 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 76.4 |


[Clique aqui para ver as próximas entradas](README3.md)
