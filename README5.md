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
| 5a6a3e28-84d8-3290-8972-442204a66802 | -2.3178 | -48.5932 | 2025-11-04 01:50:00 | GOES-19 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 33.1 |
| 78593cce-4b7c-31ce-8765-dad0ea4d2320 | -9.4765 | -40.3613 | 2025-11-04 01:50:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 76.0 |
| bfa002c0-2526-38d8-97fb-bfe4dc07d95f | -3.914 | -47.6752 | 2025-11-04 01:50:00 | GOES-19 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 87.3 |
| 3787bbe3-41dd-3245-8304-e71208f019ad | -5.6186 | -45.9717 | 2025-11-04 01:50:00 | GOES-19 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 125.7 |
| 757f7704-ca12-37be-a8a1-48901d1fed50 | -3.9325 | -47.6744 | 2025-11-04 01:50:00 | GOES-19 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 74.3 |
| 0e48bb6a-9125-3405-a5f0-61ee22922eef | -9.4761 | -40.3862 | 2025-11-04 01:50:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 144.8 |
| 6fdcc4bf-d337-3127-81c4-1814feadf19e | -2.3761 | -47.7288 | 2025-11-04 01:50:00 | GOES-19 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 30.2 |
| b5f59deb-0fea-363c-9b22-2cb556081451 | -6.4131 | -43.0724 | 2025-11-04 01:50:00 | GOES-19 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 67.0 |
| fb0e84be-796f-3e36-89a2-2b615cb881c1 | -2.8675 | -45.2832 | 2025-11-04 01:50:00 | GOES-19 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 228.8 |
| 17d8a0d9-528e-3f7d-968d-65386054ef3e | -2.8674 | -45.3057 | 2025-11-04 01:50:00 | GOES-19 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 238.6 |
| fec12c53-9001-3631-984c-880cb26b2241 | -3.9139 | -47.697 | 2025-11-04 01:50:00 | GOES-19 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 223.6 |
| d0bdd682-721c-3287-9768-7983a488a45b | -3.9324 | -47.6962 | 2025-11-04 01:50:00 | GOES-19 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 200.9 |
| 4bc25650-6ac1-3010-a3b7-deb78f661bbf | -2.886 | -45.3051 | 2025-11-04 01:50:00 | GOES-19 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 202.6 |
| 8ca09e57-9a5d-367c-a01d-f3b5569b25a0 | -5.6186 | -45.9717 | 2025-11-04 02:00:00 | GOES-19 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 102.0 |
| 991103cb-ed1b-37cf-820f-019b7599792e | -3.9325 | -47.6744 | 2025-11-04 02:00:00 | GOES-19 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 87.2 |
| 89db6468-0658-3ea5-9362-878f65848b68 | -3.9139 | -47.697 | 2025-11-04 02:00:00 | GOES-19 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 266.2 |
| 07054e77-f22a-369c-8f26-29825f509f08 | -2.8861 | -45.2826 | 2025-11-04 02:00:00 | GOES-19 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 135.9 |
| ce25b75f-51bd-3fb6-b0c1-e874e7efadbc | -3.914 | -47.6752 | 2025-11-04 02:00:00 | GOES-19 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 117.4 |
| e96cceb5-73c8-3e3c-a9e6-3f196e37e366 | -2.886 | -45.3051 | 2025-11-04 02:00:00 | GOES-19 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 181.0 |
| 891780ec-3243-3eb9-96b2-1e159318fdf7 | -6.4131 | -43.0724 | 2025-11-04 02:00:00 | GOES-19 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 60.5 |
| 16101c42-1261-3614-b379-97d1c273f63b | -2.8674 | -45.3057 | 2025-11-04 02:00:00 | GOES-19 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 226.4 |
| ee1cee77-445e-3480-81f0-8d7bcce34d6b | -3.9324 | -47.6962 | 2025-11-04 02:00:00 | GOES-19 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 194.1 |
| 9784f174-cf2a-3e10-ae01-1e24b69cfee2 | -3.4386 | -50.2368 | 2025-11-04 02:00:00 | GOES-19 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 92.6 |
| 85d888ca-8a0e-327b-b119-be0e3da03ef0 | -2.8675 | -45.2832 | 2025-11-04 02:00:00 | GOES-19 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 173.2 |
| 42c35a37-0fcb-3c39-b52c-c88c6a463dc3 | -2.3178 | -48.5932 | 2025-11-04 02:00:00 | GOES-19 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 24.6 |
| 5247c22b-a0b8-3951-8c0c-218dae89a461 | -3.9324 | -47.6962 | 2025-11-04 02:10:00 | GOES-19 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 148.0 |
| 8fc58b9a-0ce7-313a-9b5d-e0cfd5cfa133 | -3.9139 | -47.697 | 2025-11-04 02:10:00 | GOES-19 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 181.7 |
| cd6d6f49-a709-3f5d-bc63-e6e5108fd2bc | -3.914 | -47.6752 | 2025-11-04 02:10:00 | GOES-19 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 89.7 |
| 568ceea0-be2f-3c3b-b7a5-4d3ea0d1db08 | -2.8675 | -45.2832 | 2025-11-04 02:10:00 | GOES-19 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 134.7 |
| 3d71f69c-9b95-3a19-983f-a05595e8cfe3 | -2.886 | -45.3051 | 2025-11-04 02:10:00 | GOES-19 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 165.4 |
| 0a3b273c-73ff-3acd-931b-af5c6a5800ff | -5.6186 | -45.9717 | 2025-11-04 02:10:00 | GOES-19 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 85.5 |
| 1d47a5b9-f8ab-3071-8b5c-66d5c0365a34 | -6.4131 | -43.0724 | 2025-11-04 02:10:00 | GOES-19 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 66.2 |
| c3369778-a189-39ea-a5d9-1c613f5a312c | -2.8674 | -45.3057 | 2025-11-04 02:10:00 | GOES-19 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 176.7 |
| c4b1520a-2660-3c92-9e55-502828ddfaa9 | -3.9325 | -47.6744 | 2025-11-04 02:10:00 | GOES-19 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 74.5 |
| 5a1f500a-0159-3e9d-b764-eba4f9deaa6d | -2.8861 | -45.2826 | 2025-11-04 02:10:00 | GOES-19 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 124.1 |
| 5e847bb1-d8d1-34ea-bf1c-fd1c007cf7c9 | -3.4386 | -50.2368 | 2025-11-04 02:10:00 | GOES-19 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 87.6 |
| 82016a39-acd1-388b-9271-d62dfd3a04c2 | -3.9324 | -47.6962 | 2025-11-04 02:20:00 | GOES-19 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 123.7 |
| 46fc1f0c-b14e-3ff6-b09d-bfb0eef48754 | -2.886 | -45.3051 | 2025-11-04 02:20:00 | GOES-19 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 85.8 |
| 3e21286c-030d-3d18-8713-8c3412f4410e | -5.6186 | -45.9717 | 2025-11-04 02:20:00 | GOES-19 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 105.6 |
| ffcc36c8-6dfe-3dd3-b389-d15ab8973b76 | -3.914 | -47.6752 | 2025-11-04 02:20:00 | GOES-19 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 64.9 |
| 2290d299-21ee-38c7-86a2-410ee552a3c5 | -2.8674 | -45.3057 | 2025-11-04 02:20:00 | GOES-19 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 118.0 |
| b7f7be82-a2fd-3a93-95eb-07d8a5a4eb7c | -6.4131 | -43.0724 | 2025-11-04 02:20:00 | GOES-19 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 68.2 |
| 328d1c72-b94b-320c-883d-e5d5217ecb4a | -2.8861 | -45.2826 | 2025-11-04 02:20:00 | GOES-19 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 69.8 |
| 1deaefc0-5eee-3b8f-bf60-ad51d3cdee5b | -3.9139 | -47.697 | 2025-11-04 02:20:00 | GOES-19 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 192.6 |
| 52cb272d-9159-38c3-94db-0912ab1de33e | -3.4386 | -50.2368 | 2025-11-04 02:20:00 | GOES-19 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 106.4 |
| 419de82b-4ec2-38c7-b2bf-6a7610ddf662 | -2.8675 | -45.2832 | 2025-11-04 02:20:00 | GOES-19 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 98.8 |
| 62456858-6a4f-3722-84ac-970bca3b6437 | -5.6186 | -45.9717 | 2025-11-04 02:30:00 | GOES-19 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 100.8 |
| 17b4aff1-5bcf-3ea1-9bc9-d8a6194acae6 | -3.9324 | -47.6962 | 2025-11-04 02:30:00 | GOES-19 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 128.7 |
| 21408de0-641d-3e02-8be5-24683645f04f | -2.886 | -45.3051 | 2025-11-04 02:30:00 | GOES-19 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 52.2 |
| 7865e0e0-d4e0-3284-b555-17e0ede213ea | -3.7799 | -52.3211 | 2025-11-04 02:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 45.6 |
| b8bf451e-8935-3383-acb5-b3e0dad2924c | -3.9139 | -47.697 | 2025-11-04 02:30:00 | GOES-19 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 159.1 |
| 58f5ff2f-8735-3be1-9fb6-b1604dd4cf0a | -2.8675 | -45.2832 | 2025-11-04 02:30:00 | GOES-19 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 67.6 |
| aad77caa-f285-37d3-b53c-15c6e1bca132 | -3.914 | -47.6752 | 2025-11-04 02:30:00 | GOES-19 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 68.0 |
| 582d44ed-6ebb-3987-874e-9ade8d1a820e | -3.4386 | -50.2368 | 2025-11-04 02:30:00 | GOES-19 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 92.3 |
| cdf8525d-d0d0-3228-bd82-5209a34c295a | -2.8674 | -45.3057 | 2025-11-04 02:30:00 | GOES-19 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 98.1 |
| dae3b629-f796-3010-8ffa-b4671a3f96a3 | -3.9324 | -47.6962 | 2025-11-04 02:40:00 | GOES-19 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 104.9 |
| e36f5e0b-79cd-37bd-8351-fe53e95d49bd | -2.886 | -45.3051 | 2025-11-04 02:40:00 | GOES-19 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 49.5 |
| 840e86ea-1579-3156-a43f-58be97f4e9b3 | -5.6186 | -45.9717 | 2025-11-04 02:40:00 | GOES-19 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 80.1 |
| ad49ba0a-20d5-33bf-8792-777aebea832a | -2.8674 | -45.3057 | 2025-11-04 02:40:00 | GOES-19 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 65.5 |
| 103cbc54-2a35-38b4-bb77-04c136baf5c8 | -3.4386 | -50.2368 | 2025-11-04 02:40:00 | GOES-19 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 96.9 |
| 9f9ff16b-1487-3732-aa64-81530c6d639f | -2.8675 | -45.2832 | 2025-11-04 02:40:00 | GOES-19 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 52.9 |
| e9cff9f3-c471-30ef-88c4-8d47365d7c0e | -3.7799 | -52.3211 | 2025-11-04 02:40:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 52.0 |
| 4c89d3d7-8826-372d-a2fc-51268f3bf481 | -6.4131 | -43.0724 | 2025-11-04 02:40:00 | GOES-19 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 64.8 |
| b0c95a28-78d3-34e8-b783-55a12f2bc701 | -3.9139 | -47.697 | 2025-11-04 02:40:00 | GOES-19 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 121.6 |
| 5d6d651e-cc73-33cc-9731-fc2482c1c4a6 | -3.4386 | -50.2368 | 2025-11-04 02:50:00 | GOES-19 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 74.1 |
| 6c8beb54-7fc9-364d-972e-5196b5b9d935 | -3.9324 | -47.6962 | 2025-11-04 02:50:00 | GOES-19 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 92.2 |
| 522fee60-fe81-3739-b960-2e5b3638ad6b | -6.4131 | -43.0724 | 2025-11-04 02:50:00 | GOES-19 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 52.1 |
| 2026ed96-cb78-3b8a-bf60-88ed84c2276d | -2.8674 | -45.3057 | 2025-11-04 02:50:00 | GOES-19 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 50.3 |
| dedd2173-2bc9-3737-88a0-13b7d20d5880 | -3.9139 | -47.697 | 2025-11-04 02:50:00 | GOES-19 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 112.5 |
| 55fb2a23-0073-352a-9c09-889994b28f3c | -5.6186 | -45.9717 | 2025-11-04 02:50:00 | GOES-19 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 78.8 |
| 48393866-8e3d-3faa-b4c8-708c6d9d4b62 | -3.4386 | -50.2368 | 2025-11-04 03:00:00 | GOES-19 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 83.4 |
| d2a139ed-f08c-319d-86a5-3401c894bd54 | -3.9139 | -47.697 | 2025-11-04 03:00:00 | GOES-19 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 127.9 |
| 521c835a-7ef8-3a0d-aac8-da8a1252b3ea | -5.6186 | -45.9717 | 2025-11-04 03:00:00 | GOES-19 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 67.9 |
| 7ca62850-6856-3d9f-8bd1-065f3b57f93d | -3.9324 | -47.6962 | 2025-11-04 03:00:00 | GOES-19 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 100.0 |
| 84f905be-d054-37ca-8893-236684268c06 | -3.7799 | -52.3211 | 2025-11-04 03:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 78.8 |
| 37e18fa9-105f-3587-b434-f1a49495322b | -3.4386 | -50.2368 | 2025-11-04 03:10:00 | GOES-19 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 85.5 |
| 90bdab2e-4499-32f0-9a96-179ec4fb2027 | -5.6186 | -45.9717 | 2025-11-04 03:10:00 | GOES-19 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 68.7 |
| f0d98d03-8dfe-36b0-94db-2a1b95353c04 | -3.9139 | -47.697 | 2025-11-04 03:10:00 | GOES-19 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 94.2 |
| 520ff5f0-0c92-35fb-929e-39933821e81c | -3.914 | -47.6752 | 2025-11-04 03:10:00 | GOES-19 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 41.2 |
| 90cfce67-8f3b-365f-b709-f544f40e6fbd | -3.9324 | -47.6962 | 2025-11-04 03:10:00 | GOES-19 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 52.0 |
| 9233128a-74d2-3fcc-ae48-c88910bfe704 | -3.4386 | -50.2368 | 2025-11-04 03:20:00 | GOES-19 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 97.4 |
| a0a1f3a1-ce8f-3515-bb6d-2491dd7c1f31 | -3.4385 | -50.2579 | 2025-11-04 03:20:00 | GOES-19 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 51.3 |
| b637ec8c-47a9-3b3f-89d5-5cc4c81d8403 | -3.9324 | -47.6962 | 2025-11-04 03:20:00 | GOES-19 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 84.7 |
| e67a8bfd-92af-32c9-b7bf-05dad96f2a09 | -3.9139 | -47.697 | 2025-11-04 03:20:00 | GOES-19 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 103.7 |
| d3bde2ea-8095-38a3-ae57-393ef78c0d68 | -3.7799 | -52.3211 | 2025-11-04 03:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 68.2 |
| b58911df-ab15-3161-be7b-6ed96c183e84 | -3.4386 | -50.2368 | 2025-11-04 03:30:00 | GOES-19 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 81.6 |
| b8ddda8d-1df8-3dad-8f0f-220aae28da82 | -3.9139 | -47.697 | 2025-11-04 03:30:00 | GOES-19 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 96.3 |
| a0b3fc09-c015-3b5b-b8cb-1739d8f44cf1 | -3.9324 | -47.6962 | 2025-11-04 03:30:00 | GOES-19 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 58.7 |
| 2b2f091e-6c33-3595-8ab2-928b5568e4a0 | -3.4385 | -50.2579 | 2025-11-04 03:30:00 | GOES-19 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 53.6 |
| 3e6c6df9-17c9-38e3-8efc-4ccc01a6d3c0 | -3.9139 | -47.697 | 2025-11-04 03:40:00 | GOES-19 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 90.1 |
| 34ce2bc5-f3f1-36c8-9920-404c9433cd9c | -3.4386 | -50.2368 | 2025-11-04 03:40:00 | GOES-19 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 58.2 |
| 1f956139-d12d-3855-813e-50f472bd13cb | -5.6186 | -45.9717 | 2025-11-04 03:40:00 | GOES-19 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 56.6 |
| 59f7150f-d091-36fb-89d0-325c34c2f3d8 | -3.914 | -47.6752 | 2025-11-04 03:40:00 | GOES-19 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 47.8 |
| f9974220-c344-3cfd-9150-816f87bde91f | -3.9324 | -47.6962 | 2025-11-04 03:40:00 | GOES-19 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 57.6 |
| f97993ab-8ce6-3f5b-830a-912b54fbcddb | -4.59534 | -44.61198 | 2025-11-04 03:40:00 | NOAA-21 | PEDREIRAS | MARANHÃO | Brasil | 2108207 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 6fd3b486-a26a-31b2-968b-002aef8e8f59 | -5.12601 | -37.96375 | 2025-11-04 03:40:00 | NOAA-21 | LIMOEIRO DO NORTE | CEARÁ | Brasil | 2307601 | 23 | 33 | nan | nan | nan | Caatinga | 2.3 |
| a4cc98d6-1c43-3445-a475-c2378183d03a | -4.47315 | -43.23145 | 2025-11-04 03:40:00 | NOAA-21 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 47cfc48d-cbb7-3504-8b0f-266795b91236 | -4.19292 | -45.78542 | 2025-11-04 03:40:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c216503c-2ba0-332b-9259-db2a1cd5206a | -5.06087 | -39.03033 | 2025-11-04 03:40:00 | NOAA-21 | QUIXADÁ | CEARÁ | Brasil | 2311306 | 23 | 33 | nan | nan | nan | Caatinga | 1.9 |
| ca8e6ddc-584b-372e-ae5e-8127eadca5c9 | -5.61577 | -41.08729 | 2025-11-04 03:40:00 | NOAA-21 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |


[Clique aqui para ver as próximas entradas](README6.md)
