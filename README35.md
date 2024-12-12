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

## Dados Diários - Página 35

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 346c2fe5-0bfb-38b5-a802-0c85794aa5ce | -9.3933 | -38.87534 | 2024-12-12 12:04:00 | TERRA_M-T | MACURURÉ | BAHIA | Brasil | 2919900 | 29 | 33 | nan | nan | nan | Caatinga | 9.9 |
| a6163de8-dcf5-3692-8f21-44755c80f827 | -7.6566 | -37.86198 | 2024-12-12 12:04:00 | TERRA_M-T | TAVARES | PARAÍBA | Brasil | 2516607 | 25 | 33 | nan | nan | nan | Caatinga | 13.0 |
| 405f003c-e302-3b5a-b615-34d810726e90 | -8.19687 | -40.28337 | 2024-12-12 12:04:00 | TERRA_M-T | SANTA CRUZ | PERNAMBUCO | Brasil | 2612455 | 26 | 33 | nan | nan | nan | Caatinga | 11.2 |
| 2d6b30f1-cdf1-373e-a4da-7c8e0dbfe249 | -15.9905 | -57.1647 | 2024-12-12 12:10:00 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 122.3 |
| 6d125eea-7a6f-30a7-bb68-622e056aa054 | -15.9905 | -57.1647 | 2024-12-12 12:20:00 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 120.6 |
| d4cfe18a-a2c0-30dd-a55d-25f66955be9f | -6.9346 | -43.5168 | 2024-12-12 12:20:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 69.5 |
| 93311f14-be76-336c-b232-c1f35b8ff641 | -15.9905 | -57.1647 | 2024-12-12 12:30:00 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 123.5 |
| dcb3bb8e-cc8d-37c7-b720-be35e46e3718 | -15.9707 | -57.1873 | 2024-12-12 12:30:00 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 116.1 |
| 31e0e9fa-2614-350a-b162-9982c98e562d | -15.971 | -57.1669 | 2024-12-12 12:30:00 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 124.1 |
| 2906c58e-49f3-3f1d-b378-8f815a7f67c7 | -6.9346 | -43.5168 | 2024-12-12 12:30:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 71.5 |
| 664421a2-2c64-35b6-9ae9-0928bb04c038 | -15.9707 | -57.1873 | 2024-12-12 12:40:00 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 112.9 |
| e25238c5-fb62-3e5a-b6a6-606b6642203b | -15.9905 | -57.1647 | 2024-12-12 12:40:00 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 137.9 |
| 85c1d848-b527-3451-97bd-ffe302f00acd | -15.971 | -57.1669 | 2024-12-12 12:40:00 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 123.9 |
| ce9a4750-ea55-377d-977e-e82d95f45bd0 | -15.971 | -57.1669 | 2024-12-12 12:50:00 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 159.4 |
| cbb19297-af4a-3c1a-b2fb-83551397dd9a | -15.9905 | -57.1647 | 2024-12-12 12:50:00 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 130.9 |
| 0f8d05dd-df44-30d7-9cc2-df0eeeee8ef8 | -15.9707 | -57.1873 | 2024-12-12 12:50:00 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 126.3 |
| 47a9ac2a-c3b7-3d29-961d-857acde93e7b | -9.2708 | -37.7742 | 2024-12-12 13:00:00 | GOES-16 | INHAPI | ALAGOAS | Brasil | 2703304 | 27 | 33 | nan | nan | nan | Caatinga | 104.7 |
| 3b67ad80-3b3e-3325-bb54-5ca2a7941a0f | -4.9413 | -44.2726 | 2024-12-12 13:00:00 | GOES-16 | GOVERNADOR ARCHER | MARANHÃO | Brasil | 2104503 | 21 | 33 | nan | nan | nan | Cerrado | 96.5 |
| 6f790cff-35ef-3d85-8e69-fadd6fef535d | -7.7244 | -37.8122 | 2024-12-12 13:00:00 | GOES-16 | QUIXABA | PERNAMBUCO | Brasil | 2611533 | 26 | 33 | nan | nan | nan | Caatinga | 85.8 |
| 044ce618-dd35-384e-b50d-9ae7f1f117c9 | -15.971 | -57.1669 | 2024-12-12 13:00:00 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 127.7 |
| 49c89e9e-39e4-34fe-98d7-bb5c72df926c | -5.9956 | -37.9837 | 2024-12-12 13:00:00 | GOES-16 | PORTALEGRE | RIO GRANDE DO NORTE | Brasil | 2410207 | 24 | 33 | nan | nan | nan | Caatinga | 86.6 |
| 63325e32-d317-3954-b1c6-d1b0f78d3705 | -4.69 | -44.69 | 2024-12-12 13:00:00 | MSG-03 | BERNARDO DO MEARIM | MARANHÃO | Brasil | 2101939 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 94a68639-4d5d-3bae-9337-a8a1abb28f37 | -4.69 | -44.74 | 2024-12-12 13:00:00 | MSG-03 | BERNARDO DO MEARIM | MARANHÃO | Brasil | 2101939 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 1e1c00f9-f835-38e6-a2f2-60b7db6e94e9 | -3.05 | -42.03 | 2024-12-12 13:00:00 | MSG-03 | ARAIOSES | MARANHÃO | Brasil | 2100907 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| b3511a45-c77b-3b86-9411-e25d0527393d | -7.7244 | -37.8122 | 2024-12-12 13:10:00 | GOES-16 | QUIXABA | PERNAMBUCO | Brasil | 2611533 | 26 | 33 | nan | nan | nan | Caatinga | 88.8 |
| bc650d0e-3d9f-3b9d-b97b-d4ed15b6508b | -8.3864 | -36.8826 | 2024-12-12 13:10:00 | GOES-16 | PESQUEIRA | PERNAMBUCO | Brasil | 2610905 | 26 | 33 | nan | nan | nan | Caatinga | 107.9 |
| 91727913-f0f4-38e5-b1d7-b7731939c400 | -8.3864 | -36.8826 | 2024-12-12 13:20:00 | GOES-16 | PESQUEIRA | PERNAMBUCO | Brasil | 2610905 | 26 | 33 | nan | nan | nan | Caatinga | 113.2 |
| 5854e36c-22ef-3b1c-abf5-4818ae4decbb | -6.2434 | -37.8295 | 2024-12-12 13:20:00 | GOES-16 | ANTÔNIO MARTINS | RIO GRANDE DO NORTE | Brasil | 2400901 | 24 | 33 | nan | nan | nan | Caatinga | 88.4 |
| 6e6db31f-6304-39cc-9bc3-27072e0342bb | -7.7244 | -37.8122 | 2024-12-12 13:20:00 | GOES-16 | QUIXABA | PERNAMBUCO | Brasil | 2611533 | 26 | 33 | nan | nan | nan | Caatinga | 92.1 |
| 50b85fb2-4d99-3ad9-9bd5-83de6e9193ba | -10.6022 | -44.9775 | 2024-12-12 13:20:00 | GOES-16 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 97.7 |
| 10364081-3757-3873-9d54-300454541e1a | -15.9707 | -57.1873 | 2024-12-12 13:30:00 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 127.6 |
| 90ea8c95-fbb2-389b-ba9e-e24722b8d314 | -15.971 | -57.1669 | 2024-12-12 13:30:00 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 165.5 |
| 0e7c3090-5ea8-3f88-9bfc-2503ef28487d | -15.971 | -57.1669 | 2024-12-12 13:40:00 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 119.6 |
| dbd1206f-8c39-3b02-964a-50d473fd4fcf | -6.6952 | -38.0905 | 2024-12-12 13:50:00 | GOES-16 | APARECIDA | PARAÍBA | Brasil | 2500775 | 25 | 33 | nan | nan | nan | Caatinga | 90.2 |
| 944cd873-e12d-37a3-b20f-91b043977c42 | -15.971 | -57.1669 | 2024-12-12 13:50:00 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 140.6 |
| bf6c9d4d-7b21-356a-8295-66e09814f8b9 | -15.9707 | -57.1873 | 2024-12-12 13:50:00 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 129.3 |
| fa6c7efa-5f63-3cd5-b519-6bdab414fd8b | -6.6952 | -38.0905 | 2024-12-12 14:00:00 | GOES-16 | APARECIDA | PARAÍBA | Brasil | 2500775 | 25 | 33 | nan | nan | nan | Caatinga | 90.9 |
| 9be98801-44d2-3b3c-bb1e-fbf70d02d015 | -15.971 | -57.1669 | 2024-12-12 14:00:00 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 128.9 |
| a13674e5-cbb6-3491-a840-271e56fdc9f3 | -15.9707 | -57.1873 | 2024-12-12 14:00:00 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 115.0 |
| 531412d0-31dd-3c2e-924e-9c0d8bb57f46 | -15.971 | -57.1669 | 2024-12-12 14:10:00 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 142.3 |
| 6d6328bb-01cd-326d-a473-ef374c496384 | -15.9707 | -57.1873 | 2024-12-12 14:10:00 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 123.6 |
| 0e17aa42-34cc-3697-96c1-81a3b588ba57 | -6.6952 | -38.0905 | 2024-12-12 14:10:00 | GOES-16 | APARECIDA | PARAÍBA | Brasil | 2500775 | 25 | 33 | nan | nan | nan | Caatinga | 89.6 |


