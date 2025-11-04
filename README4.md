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

## Dados Diários - Página 4

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 1a79db58-a392-3522-bc6b-3524ef1a43f7 | 0.8392 | -59.31841 | 2025-11-04 00:37:00 | TERRA_M-M | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 21.4 |
| 8a0847a2-81e6-3197-81a8-edd221812fc6 | 0.96142 | -51.23594 | 2025-11-04 00:37:00 | TERRA_M-M | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 21.3 |
| a118dd1f-f219-3560-a221-bcddf581d749 | -6.4134 | -43.0489 | 2025-11-04 00:40:00 | GOES-19 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 85.2 |
| 8914c62c-bfd5-3785-bc8e-e145fd474d27 | -6.4131 | -43.0724 | 2025-11-04 00:40:00 | GOES-19 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 128.8 |
| 14ab2ce0-6097-32ea-9609-9a8b4af17785 | 0.8301 | -59.3246 | 2025-11-04 00:40:00 | GOES-19 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 37.1 |
| 98aa4696-e5d9-3edb-8f0a-beaeb2f7fee0 | -2.3761 | -47.7288 | 2025-11-04 00:40:00 | GOES-19 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 66.5 |
| b4a7d22d-1057-3fb1-a9f9-c8e8daed3f0d | -12.0175 | -43.8638 | 2025-11-04 00:40:00 | GOES-19 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 58.3 |
| c722a363-fc2f-3222-8ab2-bdaf2d786985 | -3.9139 | -47.697 | 2025-11-04 00:40:00 | GOES-19 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 181.5 |
| 007d1ff9-bbf6-3598-9c7e-f7e2c0bc1e19 | -3.9324 | -47.6962 | 2025-11-04 00:40:00 | GOES-19 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 92.9 |
| e9f5f8a0-c46f-3389-b576-067e805cbd8a | -3.9325 | -47.6744 | 2025-11-04 00:40:00 | GOES-19 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 36.6 |
| 11fb36aa-508f-35c5-9bc2-b8cf6ab061b3 | -2.8861 | -45.2826 | 2025-11-04 00:40:00 | GOES-19 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 160.1 |
| 7eb40b1a-78ac-3bf6-ba05-97032892f1bf | -3.914 | -47.6752 | 2025-11-04 00:40:00 | GOES-19 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 62.1 |
| dce6edbb-0a21-3142-bad7-6903d6f03967 | -3.4386 | -50.2368 | 2025-11-04 00:40:00 | GOES-19 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 57.7 |
| c64a9a0f-bbe3-363a-a6a5-f4b215aab42e | -2.8674 | -45.3057 | 2025-11-04 00:40:00 | GOES-19 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 208.3 |
| 07040149-8448-313b-9ca7-6ff02dafa6b1 | -2.886 | -45.3051 | 2025-11-04 00:40:00 | GOES-19 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 143.5 |
| 6d99752a-3a0c-3878-9273-19091c5f514f | -5.6186 | -45.9717 | 2025-11-04 00:40:00 | GOES-19 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 174.9 |
| fd406c9d-5057-3550-91f2-d5ce90670b01 | -12.0179 | -43.8402 | 2025-11-04 00:40:00 | GOES-19 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 81.0 |
| a3e78c1b-7f17-3041-a20c-b5f53e562bbc | -2.8675 | -45.2832 | 2025-11-04 00:40:00 | GOES-19 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 239.7 |
| 79bb0ce5-5ec6-3eba-8c39-de61c5b662ea | -2.8861 | -45.2826 | 2025-11-04 00:50:00 | GOES-19 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 293.3 |
| 5503877e-ff85-3f9a-9a57-92a9a1f86fa4 | -5.6186 | -45.9717 | 2025-11-04 00:50:00 | GOES-19 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 134.4 |
| 00f30389-13a9-3b7e-96dd-d6f8601c5141 | -3.9139 | -47.697 | 2025-11-04 00:50:00 | GOES-19 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 149.6 |
| 314d7e69-fd67-36ca-a88a-095e7e25bbdd | -3.9325 | -47.6744 | 2025-11-04 00:50:00 | GOES-19 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 36.0 |
| f820552d-8747-321e-90dd-0ea5fc4aff81 | -12.0179 | -43.8402 | 2025-11-04 00:50:00 | GOES-19 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 89.9 |
| 89d4f232-8f9b-35c5-8afd-b93b72b47b41 | -3.493 | -50.4658 | 2025-11-04 00:50:00 | GOES-19 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 46.9 |
| 0d3c62b4-bbfe-3874-a045-3e5969f752e8 | -3.914 | -47.6752 | 2025-11-04 00:50:00 | GOES-19 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 50.9 |
| 0912db43-c4f6-381a-9139-abc1ad2e06f4 | -2.3761 | -47.7288 | 2025-11-04 00:50:00 | GOES-19 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 52.9 |
| e4822c6d-d3e5-35f5-acce-c67cc8b5cef3 | -3.9324 | -47.6962 | 2025-11-04 00:50:00 | GOES-19 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 106.3 |
| 0df0ba40-b566-3816-90ec-390cc41d98bc | -6.4131 | -43.0724 | 2025-11-04 00:50:00 | GOES-19 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 120.5 |
| dfa49618-6e8e-3d33-944c-93602127da9c | -2.3178 | -48.5932 | 2025-11-04 00:50:00 | GOES-19 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 50.4 |
| 8580d4eb-8727-3b57-b193-457028fbd4a2 | -2.8674 | -45.3057 | 2025-11-04 00:50:00 | GOES-19 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 256.7 |
| b4b6e62b-da48-3878-b72e-ef0095275dd4 | -2.8675 | -45.2832 | 2025-11-04 00:50:00 | GOES-19 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 306.1 |
| d7f86212-1945-3abc-8c85-fa6095b9473e | -5.5999 | -45.973 | 2025-11-04 00:50:00 | GOES-19 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 83.1 |
| 86abbbd1-ed80-3c23-8d77-2f1a330c9378 | -2.886 | -45.3051 | 2025-11-04 00:50:00 | GOES-19 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 242.3 |
| 81116d65-399f-3409-9366-e855bf475e07 | -9.4761 | -40.3862 | 2025-11-04 00:50:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 47.3 |
| 329c55cb-73c7-3203-9195-dfd037d2c965 | -6.4131 | -43.0724 | 2025-11-04 01:00:00 | GOES-19 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 102.2 |
| 07556bad-800f-3c68-8e92-d73b7b01f36f | -3.914 | -47.6752 | 2025-11-04 01:00:00 | GOES-19 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 42.1 |
| e9738fda-8944-39bc-8c5a-0e08c0ae468c | -3.4386 | -50.2368 | 2025-11-04 01:00:00 | GOES-19 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 69.1 |
| f02ef292-e44b-3233-8758-dc5dd71b6ca0 | -5.6186 | -45.9717 | 2025-11-04 01:00:00 | GOES-19 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 137.7 |
| 749bf77d-7204-32e9-b330-71187fe3cc1a | -2.8861 | -45.2826 | 2025-11-04 01:00:00 | GOES-19 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 363.4 |
| 8a185343-e245-3b8b-83d0-f3d95d34dc66 | -2.8675 | -45.2832 | 2025-11-04 01:00:00 | GOES-19 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 376.3 |
| 35001c0e-832a-39b9-8a5a-cf6744fcbdfb | -5.5999 | -45.973 | 2025-11-04 01:00:00 | GOES-19 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 80.5 |
| ed3a0441-81f9-3a13-a721-cf5ba47525fe | -12.0179 | -43.8402 | 2025-11-04 01:00:00 | GOES-19 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 80.3 |
| 1ca03202-ae26-3d2c-86fd-1121e9195913 | -2.886 | -45.3051 | 2025-11-04 01:00:00 | GOES-19 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 353.8 |
| dd70fa30-e6d9-382e-a60f-6a626b72d1f3 | -2.8674 | -45.3057 | 2025-11-04 01:00:00 | GOES-19 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 366.1 |
| 9566eef8-9641-387e-b129-603e6e965093 | -3.9324 | -47.6962 | 2025-11-04 01:00:00 | GOES-19 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 82.3 |
| 06b0e73b-2e92-33f7-af1e-4ffb02848a4e | -3.9139 | -47.697 | 2025-11-04 01:00:00 | GOES-19 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 85.0 |
| aa08d69c-4254-3470-b80e-d59b69036caf | -4.0382 | -45.4586 | 2025-11-04 01:00:00 | GOES-19 | ALTAMIRA DO MARANHÃO | MARANHÃO | Brasil | 2100402 | 21 | 33 | nan | nan | nan | Amazônia | 45.5 |
| aff802a1-54c9-3730-a377-6296b89f0804 | -3.9325 | -47.6744 | 2025-11-04 01:00:00 | GOES-19 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 39.7 |
| 0255e1f4-3e86-3e18-b9a9-c91202ff849c | -2.8489 | -45.2839 | 2025-11-04 01:00:00 | GOES-19 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 46.9 |
| 12e5853c-6d5d-3282-97c3-0d73a3c77bbb | -2.3761 | -47.7288 | 2025-11-04 01:10:00 | GOES-19 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 51.5 |
| 4e739229-7c0c-34de-b050-438b24d0534c | -2.8675 | -45.2832 | 2025-11-04 01:10:00 | GOES-19 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 481.9 |
| 6238ce0e-ad63-35a9-9358-06016d76e52d | -9.4761 | -40.3862 | 2025-11-04 01:10:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 146.0 |
| 0ecc0240-5dbf-3a11-a8ab-58971cef7020 | -3.9324 | -47.6962 | 2025-11-04 01:10:00 | GOES-19 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 94.2 |
| d31ed609-bcb1-305b-9610-8957c3b3788e | -3.9139 | -47.697 | 2025-11-04 01:10:00 | GOES-19 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 80.2 |
| 57629219-ff00-311b-ac4a-ec1d1fd87456 | -5.6186 | -45.9717 | 2025-11-04 01:10:00 | GOES-19 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 113.7 |
| 4bf79c54-9d78-350d-a86b-554e115dbd60 | -3.4386 | -50.2368 | 2025-11-04 01:10:00 | GOES-19 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 83.0 |
| 7b638d6e-c1fb-324c-a337-67dfad9c2a78 | -2.8861 | -45.2826 | 2025-11-04 01:10:00 | GOES-19 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 442.9 |
| 289b47d2-2475-31ae-a83c-e2f35471ddc7 | -2.3178 | -48.5932 | 2025-11-04 01:10:00 | GOES-19 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 48.0 |
| 7de6844d-4ad9-3879-9bb4-3b673e1ae982 | -2.8489 | -45.3064 | 2025-11-04 01:10:00 | GOES-19 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 61.8 |
| f3244c42-df8f-38b4-952b-5b5590714fac | -2.886 | -45.3051 | 2025-11-04 01:10:00 | GOES-19 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 424.1 |
| 79a252d7-d4be-3b58-869c-544deb72289b | -6.4131 | -43.0724 | 2025-11-04 01:10:00 | GOES-19 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 109.1 |
| 2efe3864-3a49-32c9-98c0-953c87ec1bd6 | -10.9393 | -44.1897 | 2025-11-04 01:10:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 78.6 |
| 78d67b10-3623-3d02-800e-0108dc86ba8a | -2.8489 | -45.2839 | 2025-11-04 01:10:00 | GOES-19 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 62.7 |
| 7bfc9a68-cdc1-3492-8a45-7158ef1844ea | -3.9325 | -47.6744 | 2025-11-04 01:10:00 | GOES-19 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 40.9 |
| 9036b265-6333-306a-a8fb-b9e951bf9f58 | -2.8674 | -45.3057 | 2025-11-04 01:10:00 | GOES-19 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 457.6 |
| 102d618c-3406-341f-ab41-203610619938 | -6.4131 | -43.0724 | 2025-11-04 01:20:00 | GOES-19 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 84.4 |
| e8502e15-074a-3811-af2f-1e3be0ea4fce | -2.8861 | -45.2826 | 2025-11-04 01:20:00 | GOES-19 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 195.0 |
| bb7d7178-44bb-3d2a-94c4-4f4d1fdc875d | -2.3761 | -47.7288 | 2025-11-04 01:20:00 | GOES-19 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 54.5 |
| a4edd34e-5c35-31ef-8673-f81e07e8239b | -3.4386 | -50.2368 | 2025-11-04 01:20:00 | GOES-19 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 64.6 |
| 01145a7f-734a-38f4-ac48-ee2b4a10b5d0 | -3.493 | -50.4658 | 2025-11-04 01:20:00 | GOES-19 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 42.8 |
| 390c09de-aa0b-3730-ab89-4cb6349a2645 | -5.6186 | -45.9717 | 2025-11-04 01:20:00 | GOES-19 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 149.6 |
| 83ebdaac-d81e-3854-8b37-d278d1e2c2b2 | -2.8674 | -45.3057 | 2025-11-04 01:20:00 | GOES-19 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 659.0 |
| 242aeaa1-4d43-3551-aa16-85823323a6f6 | -2.886 | -45.3051 | 2025-11-04 01:20:00 | GOES-19 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 270.3 |
| 94ab8e09-86c6-31da-bd16-bb4ddee12ffc | -2.8675 | -45.2832 | 2025-11-04 01:20:00 | GOES-19 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 482.2 |
| 502ca016-25c9-3174-bf28-dd007c5aa060 | -2.3178 | -48.5932 | 2025-11-04 01:30:00 | GOES-19 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 28.1 |
| b4a3bf04-15df-3628-93cb-c5a8f53065f8 | -3.9139 | -47.697 | 2025-11-04 01:30:00 | GOES-19 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 76.4 |
| ce4d35c9-7c05-3e11-9617-2c9fcb50cb68 | -3.914 | -47.6752 | 2025-11-04 01:30:00 | GOES-19 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 56.8 |
| c9372b5d-af7b-3e86-95ad-6f719e7d1cb7 | -2.886 | -45.3051 | 2025-11-04 01:30:00 | GOES-19 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 386.2 |
| 64a1cbcc-27f2-36ff-b0df-56da3a11195f | -2.8675 | -45.2832 | 2025-11-04 01:30:00 | GOES-19 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 508.3 |
| 7ff2072e-531f-3ac4-bac6-73bc7f3a8d14 | -5.6186 | -45.9717 | 2025-11-04 01:30:00 | GOES-19 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 149.4 |
| 0c4dcc00-b056-3bfb-acbc-abdc65f32bda | -3.4386 | -50.2368 | 2025-11-04 01:30:00 | GOES-19 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 59.5 |
| 23350caf-5dd0-3c3e-9ba0-f43a84c852da | -2.3761 | -47.7288 | 2025-11-04 01:30:00 | GOES-19 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 48.7 |
| 41b7cabe-3e08-3c00-811b-58d892222c17 | -2.8674 | -45.3057 | 2025-11-04 01:30:00 | GOES-19 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 694.9 |
| daa66006-c37b-3254-878d-156c223aecdc | -2.8861 | -45.2826 | 2025-11-04 01:30:00 | GOES-19 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 276.4 |
| 3abd23e1-9f0a-3bad-bbce-0b04639c1ed2 | -6.4131 | -43.0724 | 2025-11-04 01:30:00 | GOES-19 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 74.6 |
| 300a1363-22ef-313a-91d8-f9cbe0781fc5 | -2.886 | -45.3051 | 2025-11-04 01:40:00 | GOES-19 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 333.9 |
| f52adf89-a302-33ce-a92f-5191594b2a2d | -5.6186 | -45.9717 | 2025-11-04 01:40:00 | GOES-19 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 138.7 |
| 278ac8c4-4cd7-391f-b3a6-019d63f29c0b | -13.3204 | -42.4207 | 2025-11-04 01:40:00 | GOES-19 | BOTUPORÃ | BAHIA | Brasil | 2904209 | 29 | 33 | nan | nan | nan | Caatinga | 91.8 |
| 8468741b-4d3d-3633-80d9-26926cb50510 | -3.9139 | -47.697 | 2025-11-04 01:40:00 | GOES-19 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 182.2 |
| 9d1ffc95-17d1-3a0b-8a09-8248ce0bc641 | -3.9324 | -47.6962 | 2025-11-04 01:40:00 | GOES-19 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 124.0 |
| 5544417a-30c5-37f4-a895-77846b604f2e | -2.3761 | -47.7288 | 2025-11-04 01:40:00 | GOES-19 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 38.1 |
| a7d01c4e-cf6f-3409-9ecf-31890a79a302 | -3.4386 | -50.2368 | 2025-11-04 01:40:00 | GOES-19 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 73.8 |
| 82320a01-5f85-3d25-900f-984fcf66da7e | -2.8861 | -45.2826 | 2025-11-04 01:40:00 | GOES-19 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 332.4 |
| 5696da63-f8ad-3f4c-975f-25b98b660038 | -2.8675 | -45.2832 | 2025-11-04 01:40:00 | GOES-19 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 428.5 |
| 84d730c0-d338-3df0-9d70-649aea4cb061 | -3.914 | -47.6752 | 2025-11-04 01:40:00 | GOES-19 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 77.5 |
| 977375b9-ec26-3fb9-a6a5-3388276211c2 | -6.4131 | -43.0724 | 2025-11-04 01:40:00 | GOES-19 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 76.1 |
| 6344cf81-e09b-3135-bb63-34be3079ea81 | -2.3178 | -48.5932 | 2025-11-04 01:40:00 | GOES-19 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 31.3 |
| f9796d40-853e-3c0c-ab48-1cd9f4b515ba | -2.8674 | -45.3057 | 2025-11-04 01:40:00 | GOES-19 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 427.4 |
| 4d29a6f7-dcdd-3195-98c6-05de3358a7ed | -2.8861 | -45.2826 | 2025-11-04 01:50:00 | GOES-19 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 188.7 |
| f09a4d25-b96f-39b4-b5c5-ff4643f7389c | -3.4386 | -50.2368 | 2025-11-04 01:50:00 | GOES-19 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 82.7 |


[Clique aqui para ver as próximas entradas](README5.md)
