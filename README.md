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

## Dados Diários - Página 1

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 9252a232-5785-3b1a-9674-d61ccca46382 | -4.2416 | -45.6728 | 2025-11-04 00:00:00 | GOES-19 | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 32.6 |
| ce276445-77ef-376d-a43a-58c64b0f6152 | -6.4134 | -43.0489 | 2025-11-04 00:00:00 | GOES-19 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 127.1 |
| e892d313-000e-3c5a-baf2-04e04658fc12 | 0.8301 | -59.3246 | 2025-11-04 00:00:00 | GOES-19 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 37.9 |
| 1ea7bf76-569f-30b2-b39f-145db5d91ce7 | -2.3178 | -48.5932 | 2025-11-04 00:00:00 | GOES-19 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 58.3 |
| 41c5d76e-3ac9-3525-a590-b7344c25ba8b | -3.9324 | -47.6962 | 2025-11-04 00:00:00 | GOES-19 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 65.2 |
| 598cd28e-be15-3337-8532-62cd78c9cd82 | -4.1124 | -45.4999 | 2025-11-04 00:00:00 | GOES-19 | ALTAMIRA DO MARANHÃO | MARANHÃO | Brasil | 2100402 | 21 | 33 | nan | nan | nan | Amazônia | 158.4 |
| 65cbd480-1ff1-3aee-9517-063e2ccd1c12 | -2.3761 | -47.7288 | 2025-11-04 00:00:00 | GOES-19 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 79.4 |
| e09a6db5-3cd5-3241-a8a9-f19ddb47f577 | -4.9552 | -44.9106 | 2025-11-04 00:00:00 | GOES-19 | ESPERANTINÓPOLIS | MARANHÃO | Brasil | 2104008 | 21 | 33 | nan | nan | nan | Cerrado | 94.1 |
| 51f0f8a7-142e-35a2-ba3b-dbee4aa4d4fa | -3.9139 | -47.697 | 2025-11-04 00:00:00 | GOES-19 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 109.4 |
| 66f63718-1541-3409-9f17-cde216c10eae | -4.0382 | -45.4586 | 2025-11-04 00:00:00 | GOES-19 | ALTAMIRA DO MARANHÃO | MARANHÃO | Brasil | 2100402 | 21 | 33 | nan | nan | nan | Amazônia | 61.3 |
| 011c46cd-3ebe-3007-a871-af571bf7c3cd | -4.0196 | -45.4595 | 2025-11-04 00:00:00 | GOES-19 | ALTAMIRA DO MARANHÃO | MARANHÃO | Brasil | 2100402 | 21 | 33 | nan | nan | nan | Amazônia | 65.3 |
| bbe8fd2e-e6d1-37e3-b805-c60429c8c008 | -5.6186 | -45.9717 | 2025-11-04 00:00:00 | GOES-19 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 121.9 |
| f59359b1-522c-33cb-b492-9f1fff646f33 | -5.6373 | -45.9705 | 2025-11-04 00:00:00 | GOES-19 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 56.8 |
| 65906954-f437-345e-9410-8b8a5f996fcd | -6.4131 | -43.0724 | 2025-11-04 00:00:00 | GOES-19 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 185.9 |
| cb60bd38-b390-3808-a748-bf4883f7b76d | -5.5999 | -45.973 | 2025-11-04 00:00:00 | GOES-19 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 58.5 |
| 8229f07a-cd20-341b-888c-8d214a2e0de8 | -3.914 | -47.6752 | 2025-11-04 00:00:00 | GOES-19 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 37.4 |
| b1a358a6-32d9-31e5-8f03-ed03ed7cf9d7 | 0.8484 | -59.3245 | 2025-11-04 00:00:00 | GOES-19 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 37.0 |
| 9df89519-25dd-39eb-b2e2-dcb94599cb34 | -2.3761 | -47.7071 | 2025-11-04 00:00:00 | GOES-19 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 48.1 |
| 6fb84d7e-e8ec-3494-95ea-6bb0b2c49ad7 | -4.0938 | -45.5008 | 2025-11-04 00:00:00 | GOES-19 | ALTAMIRA DO MARANHÃO | MARANHÃO | Brasil | 2100402 | 21 | 33 | nan | nan | nan | Amazônia | 59.5 |
| b2251292-94c3-33f3-b2e1-8239c089090e | -5.6184 | -45.9941 | 2025-11-04 00:10:00 | GOES-19 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 65.1 |
| 390db861-95ad-3c55-ae8e-fa46614ab25b | -3.914 | -47.6752 | 2025-11-04 00:10:00 | GOES-19 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 35.6 |
| 21f0c0f4-f796-3ea2-9bab-c7f1bd934d88 | -6.4134 | -43.0489 | 2025-11-04 00:10:00 | GOES-19 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 95.1 |
| d809a3c9-dadb-3e17-9a0e-3ca151e22385 | -4.0938 | -45.5008 | 2025-11-04 00:10:00 | GOES-19 | ALTAMIRA DO MARANHÃO | MARANHÃO | Brasil | 2100402 | 21 | 33 | nan | nan | nan | Amazônia | 43.0 |
| cdcc7934-fc02-3303-8803-2ce0f47c099d | -4.9552 | -44.9106 | 2025-11-04 00:10:00 | GOES-19 | ESPERANTINÓPOLIS | MARANHÃO | Brasil | 2104008 | 21 | 33 | nan | nan | nan | Cerrado | 90.5 |
| 635d99dd-6323-3fcd-bbd5-09b62d821bc0 | -2.3761 | -47.7288 | 2025-11-04 00:10:00 | GOES-19 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 85.2 |
| b3e21619-87bc-328d-b932-e72636fbc6f8 | 0.8301 | -59.3246 | 2025-11-04 00:10:00 | GOES-19 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 45.5 |
| 22d36d88-b80c-3306-b45a-e36a93aa61b5 | -2.8674 | -45.3057 | 2025-11-04 00:10:00 | GOES-19 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 49.1 |
| 1c33fa2e-b998-398d-b335-d5b4ea99ab87 | -2.3178 | -48.5932 | 2025-11-04 00:10:00 | GOES-19 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 54.7 |
| 7d13972b-4f7b-3fed-96e5-84bf0d958957 | -4.1124 | -45.4999 | 2025-11-04 00:10:00 | GOES-19 | ALTAMIRA DO MARANHÃO | MARANHÃO | Brasil | 2100402 | 21 | 33 | nan | nan | nan | Amazônia | 106.0 |
| b629f201-a872-3b90-b142-5490244da9f3 | -5.6186 | -45.9717 | 2025-11-04 00:10:00 | GOES-19 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 114.2 |
| 2b3ae917-954b-349f-bc2a-7618580e8825 | -4.0196 | -45.4595 | 2025-11-04 00:10:00 | GOES-19 | ALTAMIRA DO MARANHÃO | MARANHÃO | Brasil | 2100402 | 21 | 33 | nan | nan | nan | Amazônia | 54.6 |
| d0d23c2d-2e46-3901-9ff2-fc07b796a967 | -6.4131 | -43.0724 | 2025-11-04 00:10:00 | GOES-19 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 179.7 |
| 0886b931-82ab-3c7d-b5b8-12582216f064 | -3.9139 | -47.697 | 2025-11-04 00:10:00 | GOES-19 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 95.1 |
| e5d76260-e9ec-30c4-bb96-6670aea3fafd | -3.9324 | -47.6962 | 2025-11-04 00:10:00 | GOES-19 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 56.9 |
| 42d3a3d6-c491-33cb-a295-302d71365d15 | -5.6186 | -45.9717 | 2025-11-04 00:20:00 | GOES-19 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 167.4 |
| b281fe00-355e-30b9-abab-67ca32e208cf | -2.8674 | -45.3057 | 2025-11-04 00:20:00 | GOES-19 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 64.4 |
| 6a36a54d-8635-336b-8cf8-07699a14e195 | -4.1124 | -45.4999 | 2025-11-04 00:20:00 | GOES-19 | ALTAMIRA DO MARANHÃO | MARANHÃO | Brasil | 2100402 | 21 | 33 | nan | nan | nan | Amazônia | 65.8 |
| 8e7e24e2-ed98-3794-b83d-f03ec59e7c52 | -12.0179 | -43.8402 | 2025-11-04 00:20:00 | GOES-19 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 73.1 |
| c4681fa2-04e2-3282-9bd6-820b65ed340b | -6.4134 | -43.0489 | 2025-11-04 00:20:00 | GOES-19 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 101.6 |
| 9638cd89-d73d-3d9b-b527-c4569d69cb0f | -2.8675 | -45.2832 | 2025-11-04 00:20:00 | GOES-19 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 54.0 |
| a81d0cbb-3f79-318b-99fe-799fdca9178e | 0.9844 | -51.2279 | 2025-11-04 00:20:00 | GOES-19 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 54.5 |
| 07bae0e9-8a56-3667-8ed4-7e9277b14300 | -2.3761 | -47.7288 | 2025-11-04 00:20:00 | GOES-19 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 55.5 |
| a21345ee-3a2c-35ef-a6b3-ef01826f63d3 | 0.966 | -51.2281 | 2025-11-04 00:20:00 | GOES-19 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 45.6 |
| d037a51f-7aa1-3d39-80ef-27f065ea62f5 | -3.9324 | -47.6962 | 2025-11-04 00:20:00 | GOES-19 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 78.4 |
| ff0bb3df-a926-3c70-b8cc-4cb0f8404c64 | -3.9139 | -47.697 | 2025-11-04 00:20:00 | GOES-19 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 160.2 |
| c7f485e6-98b3-3645-b169-772f107a61fa | 0.8301 | -59.3246 | 2025-11-04 00:20:00 | GOES-19 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 39.6 |
| 278c3e92-b446-3cff-9279-80526cdaa112 | -6.4131 | -43.0724 | 2025-11-04 00:20:00 | GOES-19 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 151.8 |
| 592194a7-9b4e-3ca6-80ed-652048c046d2 | -4.0196 | -45.4595 | 2025-11-04 00:20:00 | GOES-19 | ALTAMIRA DO MARANHÃO | MARANHÃO | Brasil | 2100402 | 21 | 33 | nan | nan | nan | Amazônia | 59.5 |
| 73bc0bb9-31a5-3d4b-8539-9bbd1acb21dc | -3.914 | -47.6752 | 2025-11-04 00:20:00 | GOES-19 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 53.6 |
| 474ee632-4bb2-37fe-b829-f715e70a48be | -4.9552 | -44.9106 | 2025-11-04 00:20:00 | GOES-19 | ESPERANTINÓPOLIS | MARANHÃO | Brasil | 2104008 | 21 | 33 | nan | nan | nan | Cerrado | 77.8 |
| 8fcabf5a-e8f7-36ee-8b7f-46756f9875a8 | -12.0179 | -43.8402 | 2025-11-04 00:30:00 | GOES-19 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 76.6 |
| d9e19537-a174-3db4-b8f2-2d40990c7902 | -5.0399 | -43.6205 | 2025-11-04 00:30:00 | GOES-19 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 73.5 |
| f5c0e62e-65ba-3128-90b5-d8e65c6e0d23 | -2.8675 | -45.2832 | 2025-11-04 00:30:00 | GOES-19 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 117.5 |
| c64a9e80-aabf-3554-967b-2715696a5874 | -3.9139 | -47.697 | 2025-11-04 00:30:00 | GOES-19 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 230.3 |
| f0fd3b31-4dc1-3881-a7c0-b8a43189b149 | -2.8861 | -45.2826 | 2025-11-04 00:30:00 | GOES-19 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 80.9 |
| 977a05d3-a778-3ea1-89e0-d86b1db5c611 | -2.3761 | -47.7288 | 2025-11-04 00:30:00 | GOES-19 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 66.1 |
| 142f3866-0d5f-3725-9fa1-35bfae466404 | -3.914 | -47.6752 | 2025-11-04 00:30:00 | GOES-19 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 77.7 |
| 72d7cac4-2be9-3779-b93f-3f8cae1abf29 | 0.8301 | -59.3246 | 2025-11-04 00:30:00 | GOES-19 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 38.8 |
| 224fe63c-d337-3c56-844c-dd4dc241ee23 | -3.9325 | -47.6744 | 2025-11-04 00:30:00 | GOES-19 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 45.7 |
| fe8edbee-944c-3e06-81f5-ac930cb65aa2 | -5.6186 | -45.9717 | 2025-11-04 00:30:00 | GOES-19 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 189.1 |
| 2dc422e3-c04e-35fb-bb10-f28043fa6610 | -3.9137 | -47.7187 | 2025-11-04 00:30:00 | GOES-19 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 34.2 |
| e0b2dcd3-6e5a-3bec-beef-203054c2842c | -4.0196 | -45.4595 | 2025-11-04 00:30:00 | GOES-19 | ALTAMIRA DO MARANHÃO | MARANHÃO | Brasil | 2100402 | 21 | 33 | nan | nan | nan | Amazônia | 65.2 |
| f38bcb42-3269-3279-9e4f-a142ee2667c7 | -3.9324 | -47.6962 | 2025-11-04 00:30:00 | GOES-19 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 125.4 |
| f7344d22-5fbc-36ae-96ba-1dfdc91b0cf5 | -6.4134 | -43.0489 | 2025-11-04 00:30:00 | GOES-19 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 96.3 |
| 29ad1cdc-a310-317b-9b5f-a10b566f0ccf | -2.886 | -45.3051 | 2025-11-04 00:30:00 | GOES-19 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 94.3 |
| d3814923-fae0-3910-a2b8-dedb0c7bd13b | -6.4131 | -43.0724 | 2025-11-04 00:30:00 | GOES-19 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 142.4 |
| 296112ee-166c-39d5-9a39-97713dced785 | -2.8674 | -45.3057 | 2025-11-04 00:30:00 | GOES-19 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 136.5 |
| 1287be1f-a0dc-39e6-9afc-797de67b42bb | -21.39888 | -48.33517 | 2025-11-04 00:30:00 | TERRA_M-M | GUARIBA | SÃO PAULO | Brasil | 3518602 | 35 | 33 | nan | nan | nan | Cerrado | 6.3 |
| c7683349-2a9c-3b1c-894a-4ab09bc9825d | -15.25523 | -42.98604 | 2025-11-04 00:32:00 | TERRA_M-M | MONTE AZUL | MINAS GERAIS | Brasil | 3142908 | 31 | 33 | nan | nan | nan | Caatinga | 10.9 |
| 6cfffb1e-2921-3666-b326-9872b945daf7 | -14.50489 | -43.8295 | 2025-11-04 00:32:00 | TERRA_M-M | MALHADA | BAHIA | Brasil | 2920205 | 29 | 33 | nan | nan | nan | Cerrado | 10.2 |
| cd87cc1f-f0dc-31cf-8b38-2a60788763c8 | -15.79258 | -42.02645 | 2025-11-04 00:32:00 | TERRA_M-M | TAIOBEIRAS | MINAS GERAIS | Brasil | 3168002 | 31 | 33 | nan | nan | nan | Mata Atlântica | 26.0 |
| 025f3ac0-3d2c-3830-809a-12636f8eec37 | -13.32365 | -44.48681 | 2025-11-04 00:32:00 | TERRA_M-M | SANTA MARIA DA VITÓRIA | BAHIA | Brasil | 2928109 | 29 | 33 | nan | nan | nan | Cerrado | 13.9 |
| 745f5731-477f-389c-9ed1-b17414c7c6f5 | -12.01541 | -43.84381 | 2025-11-04 00:32:00 | TERRA_M-M | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 48.6 |
| 7384cff3-ba23-3c01-a965-30dbc9d7cdaf | -12.01729 | -43.84938 | 2025-11-04 00:32:00 | TERRA_M-M | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 86.6 |
| b704b377-dd0b-373b-b13c-2a398c4eb132 | -16.1832 | -42.19759 | 2025-11-04 00:32:00 | TERRA_M-M | SALINAS | MINAS GERAIS | Brasil | 3157005 | 31 | 33 | nan | nan | nan | Mata Atlântica | 13.3 |
| 3280fc6d-877d-358b-b2c8-6af87160087d | -15.30071 | -42.98643 | 2025-11-04 00:32:00 | TERRA_M-M | MONTE AZUL | MINAS GERAIS | Brasil | 3142908 | 31 | 33 | nan | nan | nan | Caatinga | 7.1 |
| 1229516a-c3fb-3914-bd18-66cc4078591e | -15.30066 | -42.97686 | 2025-11-04 00:32:00 | TERRA_M-M | MONTE AZUL | MINAS GERAIS | Brasil | 3142908 | 31 | 33 | nan | nan | nan | Caatinga | 16.0 |
| e7572a21-6ec7-3f90-a85b-7f4167036db4 | -12.0179 | -43.85916 | 2025-11-04 00:32:00 | TERRA_M-M | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 63.7 |
| 7174e300-fdb4-3c2f-9d09-54f7370714a2 | -12.01966 | -43.86472 | 2025-11-04 00:32:00 | TERRA_M-M | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 23.3 |
| b91c0dc3-20a4-362d-817b-bf640665493e | -15.79598 | -42.02054 | 2025-11-04 00:32:00 | TERRA_M-M | TAIOBEIRAS | MINAS GERAIS | Brasil | 3168002 | 31 | 33 | nan | nan | nan | Mata Atlântica | 19.9 |
| 63f26a02-c03b-3eee-9f04-d7af4e4a4da4 | -12.56713 | -43.76128 | 2025-11-04 00:32:00 | TERRA_M-M | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 10.6 |
| df9c3271-ed74-338e-afcf-6cfe7b492939 | -12.56864 | -43.76658 | 2025-11-04 00:32:00 | TERRA_M-M | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 18.0 |
| 5cdc1d94-7c5a-3761-ab3b-234c4ef15254 | -13.82779 | -42.78779 | 2025-11-04 00:32:00 | TERRA_M-M | MATINA | BAHIA | Brasil | 2921054 | 29 | 33 | nan | nan | nan | Caatinga | 14.1 |
| 41691e8a-5c03-3843-87bc-fa6ef7dc5aba | -13.32162 | -44.47345 | 2025-11-04 00:32:00 | TERRA_M-M | SANTA MARIA DA VITÓRIA | BAHIA | Brasil | 2928109 | 29 | 33 | nan | nan | nan | Cerrado | 8.9 |
| f88d83cd-8a04-3126-8812-b8b247a4b503 | -5.43146 | -44.66077 | 2025-11-04 00:34:00 | TERRA_M-M | SANTA FILOMENA DO MARANHÃO | MARANHÃO | Brasil | 2109759 | 21 | 33 | nan | nan | nan | Cerrado | 15.7 |
| eb3b7ff4-17ab-3db1-ba78-58a41c5f3dd2 | -2.88355 | -45.28788 | 2025-11-04 00:34:00 | TERRA_M-M | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 31.7 |
| db9f5742-0e77-3e7f-87e6-2d487ff698cc | -2.86593 | -45.2961 | 2025-11-04 00:34:00 | TERRA_M-M | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 38.8 |
| 5036b6ae-a51b-3b4e-9ea0-8180136824c7 | -3.41625 | -44.45201 | 2025-11-04 00:34:00 | TERRA_M-M | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 14.0 |
| 454933ec-017a-36d5-a467-e730ce917db8 | -7.85822 | -44.20808 | 2025-11-04 00:34:00 | TERRA_M-M | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 14.3 |
| e7bf959e-e555-33b1-a4c7-131683db9e9d | -3.69067 | -49.56792 | 2025-11-04 00:34:00 | TERRA_M-M | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 8.3 |
| 008a603f-cebb-3912-a969-70fb5596a5b5 | -7.55714 | -45.84951 | 2025-11-04 00:34:00 | TERRA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 13.9 |
| ee70e4ff-b45f-39c0-a8ae-3d21f6784d13 | -5.05786 | -45.91466 | 2025-11-04 00:34:00 | TERRA_M-M | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 16.6 |
| 478e2797-c7a5-3e1f-a9de-7030c63bbbd9 | -2.87163 | -45.28963 | 2025-11-04 00:34:00 | TERRA_M-M | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 238.3 |
| 867585ea-a104-3f24-91b3-0f43010d1f0b | -2.88601 | -45.30467 | 2025-11-04 00:34:00 | TERRA_M-M | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 21.4 |
| aa1ade20-c834-31e4-b55c-c2273ed19bcc | -6.01327 | -51.51131 | 2025-11-04 00:34:00 | TERRA_M-M | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 14.4 |
| d46aadc2-fa0a-32aa-8045-142edba93bfd | -5.22962 | -44.21109 | 2025-11-04 00:34:00 | TERRA_M-M | GONÇALVES DIAS | MARANHÃO | Brasil | 2104404 | 21 | 33 | nan | nan | nan | Cerrado | 28.1 |
| b927c494-f110-30ea-9bdf-558854665f13 | -4.10817 | -45.48772 | 2025-11-04 00:34:00 | TERRA_M-M | ALTAMIRA DO MARANHÃO | MARANHÃO | Brasil | 2100402 | 21 | 33 | nan | nan | nan | Amazônia | 8.0 |
| 1d1c7174-76b3-31ce-83b8-d2fa929617bc | -4.23728 | -48.66596 | 2025-11-04 00:34:00 | TERRA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 8.5 |
| 5d3b1ed3-2776-3dd3-9f25-0a9f6c8a9e9d | -3.33456 | -45.3925 | 2025-11-04 00:34:00 | TERRA_M-M | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | 11.3 |
| a0330829-89e0-3152-8533-c2d1d0b2c91e | -3.53497 | -49.4441 | 2025-11-04 00:34:00 | TERRA_M-M | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 16.4 |


[Clique aqui para ver as próximas entradas](README2.md)
