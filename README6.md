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
| e9c24316-d14a-3958-8e63-67147ddf46f1 | -2.8652 | -45.8213 | 2024-10-31 00:45:22 | GOES-16 | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | 62.4 |
| 31e74a5e-eaa3-3016-bde1-3e8c1a275591 | -3.2366 | -45.83 | 2024-10-31 00:45:24 | GOES-16 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 56.3 |
| 03a02513-14ea-34c4-9503-62065238a9a5 | -3.2552 | -45.8293 | 2024-10-31 00:45:24 | GOES-16 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 43.2 |
| 9d047e10-b2c3-3104-9bfb-b150504d50cf | -3.5631 | -47.3847 | 2024-10-31 00:45:26 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 55.1 |
| ed74d0ce-40d7-3052-983e-9b87a3e95c61 | -4.2749 | -43.4357 | 2024-10-31 00:45:30 | GOES-16 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 173.7 |
| 56d2c4c5-0277-379a-a192-1de548cc9ac5 | -4.2751 | -43.4125 | 2024-10-31 00:45:30 | GOES-16 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 77.0 |
| df6a16b2-8a62-36d7-89ee-0fd6731063d4 | -4.3353 | -48.5862 | 2024-10-31 00:45:30 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 65.9 |
| 3d2a3369-a1cc-3be8-a48d-7a46b797c190 | -4.2563 | -43.4368 | 2024-10-31 00:45:30 | GOES-16 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 101.8 |
| 55f66ed8-db0a-3b52-8016-1b5c7569db39 | -4.3539 | -48.5853 | 2024-10-31 00:45:31 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 56.4 |
| 9db1e0e4-2807-3809-b870-b681d34339e9 | -4.6511 | -43.1104 | 2024-10-31 00:45:32 | GOES-16 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 76.2 |
| 63083431-def0-349d-b933-95290310774c | -4.6049 | -44.3161 | 2024-10-31 00:45:32 | GOES-16 | CAPINZAL DO NORTE | MARANHÃO | Brasil | 2102754 | 21 | 33 | nan | nan | nan | Cerrado | 59.6 |
| bc34ea0c-17ad-3570-a5b4-21890adfd3d0 | -4.6051 | -44.2932 | 2024-10-31 00:45:32 | GOES-16 | CAPINZAL DO NORTE | MARANHÃO | Brasil | 2102754 | 21 | 33 | nan | nan | nan | Cerrado | 58.6 |
| 07a47014-ecaf-3a81-beba-cbefadddb95d | -5.0466 | -45.1542 | 2024-10-31 00:45:34 | GOES-16 | SÃO RAIMUNDO DO DOCA BEZERRA | MARANHÃO | Brasil | 2111631 | 21 | 33 | nan | nan | nan | Cerrado | 77.1 |
| fa994488-b927-3951-8f56-466ca5157a72 | -5.028 | -45.1554 | 2024-10-31 00:45:34 | GOES-16 | SÃO RAIMUNDO DO DOCA BEZERRA | MARANHÃO | Brasil | 2111631 | 21 | 33 | nan | nan | nan | Cerrado | 48.1 |
| 9ff2703f-9b01-3ac9-a7de-c497e1d74d04 | -5.0464 | -45.1768 | 2024-10-31 00:45:34 | GOES-16 | SÃO RAIMUNDO DO DOCA BEZERRA | MARANHÃO | Brasil | 2111631 | 21 | 33 | nan | nan | nan | Cerrado | 56.4 |
| 9fd14fbd-899b-30b6-bc0c-849b50432ad9 | -6.1229 | -43.9578 | 2024-10-31 00:45:40 | GOES-16 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 73.5 |
| 34479952-e59f-321a-8eb0-2004d8d0fa80 | -6.1414 | -43.9794 | 2024-10-31 00:45:40 | GOES-16 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 57.9 |
| 845bd409-1e4b-39fa-b7a8-1498331c7d50 | -6.1416 | -43.9563 | 2024-10-31 00:45:40 | GOES-16 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 88.8 |
| 97096e97-5d66-34e9-9dd6-8d31cda889b7 | -5.9788 | -45.3621 | 2024-10-31 00:45:40 | GOES-16 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 70.3 |
| 79f00018-2185-35e8-b496-7be0ebc72d81 | -10.0118 | -64.8023 | 2024-10-31 00:46:03 | GOES-16 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 52.0 |
| fb9ef463-c5af-3503-8ccf-b895ba64f87e | -12.4235 | -43.7511 | 2024-10-31 00:46:15 | GOES-16 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 64.2 |
| ddd6e4e6-2eeb-3a33-a120-eed4d46475af | -12.424 | -43.7274 | 2024-10-31 00:46:15 | GOES-16 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 125.6 |
| 0c310aa4-089f-38fe-bf1b-b590b26a3945 | -12.4433 | -43.7242 | 2024-10-31 00:46:15 | GOES-16 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 111.6 |
| 717db94c-1640-3004-80f0-f9f5710f49b5 | -23.9923 | -54.1106 | 2024-10-31 00:47:18 | GOES-16 | ALTÔNIA | PARANÁ | Brasil | 4100509 | 41 | 33 | nan | nan | nan | Mata Atlântica | 83.6 |
| 99c18ba0-f0bc-38d8-a007-61dd87961aa3 | -0.7552 | -62.8933 | 2024-10-31 00:55:10 | GOES-16 | BARCELOS | AMAZONAS | Brasil | 1300409 | 13 | 33 | nan | nan | nan | Amazônia | 34.0 |
| ca6491e7-af57-3426-b386-9bbb3217da99 | -1.2497 | -46.6147 | 2024-10-31 00:55:13 | GOES-16 | AUGUSTO CORRÊA | PARÁ | Brasil | 1500909 | 15 | 33 | nan | nan | nan | Amazônia | 49.4 |
| 4c71e4a2-c595-38e4-a8a9-307ad146dc91 | -1.4426 | -52.273 | 2024-10-31 00:55:14 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 67.7 |
| 8d267cd2-327c-312f-b500-fe4cb777d299 | -2.1718 | -47.9506 | 2024-10-31 00:55:18 | GOES-16 | SÃO DOMINGOS DO CAPIM | PARÁ | Brasil | 1507201 | 15 | 33 | nan | nan | nan | Amazônia | 60.7 |
| 20d43c4a-9638-3300-8824-8281d2c82f2d | -2.5031 | -48.4596 | 2024-10-31 00:55:20 | GOES-16 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 59.9 |
| 450d1511-3d52-3ae8-accc-f4b17a83732c | -2.503 | -48.4811 | 2024-10-31 00:55:20 | GOES-16 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 56.5 |
| 992fca29-dc75-3244-acdd-3b24093cbbc8 | -2.5215 | -48.4806 | 2024-10-31 00:55:20 | GOES-16 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 101.4 |
| 61edf2d4-bcc0-3f8d-bc56-2bbe940c70bd | -2.5216 | -48.4591 | 2024-10-31 00:55:20 | GOES-16 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 121.2 |
| 6148dfe4-a169-3d1d-a810-d9f189a296d2 | -2.5401 | -48.4586 | 2024-10-31 00:55:20 | GOES-16 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 55.7 |
| 8001da52-844c-394b-9954-6a3ab709e571 | -2.811 | -45.465 | 2024-10-31 00:55:22 | GOES-16 | SANTA HELENA | MARANHÃO | Brasil | 2109809 | 21 | 33 | nan | nan | nan | Amazônia | 60.7 |
| 606abb7b-2dd4-35db-b39b-245874d7bb8c | -2.8109 | -45.4875 | 2024-10-31 00:55:22 | GOES-16 | SANTA HELENA | MARANHÃO | Brasil | 2109809 | 21 | 33 | nan | nan | nan | Amazônia | 76.3 |
| b1ff972c-5270-31d3-b6c0-8e67d380a9f3 | -2.8652 | -45.8213 | 2024-10-31 00:55:22 | GOES-16 | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | 69.5 |
| 8623771c-7201-3a10-a2fd-17a079d1e865 | -3.2366 | -45.83 | 2024-10-31 00:55:24 | GOES-16 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 45.2 |
| a3b2b805-5f34-3230-ba51-8ea089a773da | -4.2563 | -43.4368 | 2024-10-31 00:55:30 | GOES-16 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 65.6 |
| db6b5a08-8920-314a-801d-377917f16819 | -4.2749 | -43.4357 | 2024-10-31 00:55:30 | GOES-16 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 109.7 |
| 71870f58-3c88-3283-9f29-891c99177b58 | -4.2751 | -43.4125 | 2024-10-31 00:55:30 | GOES-16 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 49.7 |
| 0f931255-da32-35f2-b228-aaa7b1fd368f | -4.6511 | -43.1104 | 2024-10-31 00:55:32 | GOES-16 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 63.0 |
| a493fdb3-a7d2-3eda-ab84-5a643db35731 | -4.6051 | -44.2932 | 2024-10-31 00:55:32 | GOES-16 | CAPINZAL DO NORTE | MARANHÃO | Brasil | 2102754 | 21 | 33 | nan | nan | nan | Cerrado | 59.7 |
| 0b348418-e3e4-3378-af17-cb21ff555abe | -4.8862 | -46.706 | 2024-10-31 00:55:34 | GOES-16 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 74.4 |
| 82d50dbc-1bf1-3f2f-8f66-ce4c0c054183 | -5.028 | -45.1554 | 2024-10-31 00:55:34 | GOES-16 | SÃO RAIMUNDO DO DOCA BEZERRA | MARANHÃO | Brasil | 2111631 | 21 | 33 | nan | nan | nan | Cerrado | 52.7 |
| 716b6059-ef89-3910-b29d-f10cd17c32c3 | -5.0464 | -45.1768 | 2024-10-31 00:55:34 | GOES-16 | SÃO RAIMUNDO DO DOCA BEZERRA | MARANHÃO | Brasil | 2111631 | 21 | 33 | nan | nan | nan | Cerrado | 49.7 |
| 018b90a2-fb0a-3ff6-b896-4cd82e3ecaaf | -5.0466 | -45.1542 | 2024-10-31 00:55:34 | GOES-16 | SÃO RAIMUNDO DO DOCA BEZERRA | MARANHÃO | Brasil | 2111631 | 21 | 33 | nan | nan | nan | Cerrado | 78.0 |
| 507b6366-e6cc-33fa-8b97-ed66c1dc240f | -6.1229 | -43.9578 | 2024-10-31 00:55:40 | GOES-16 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 76.8 |
| b57f9f22-7cf4-36c7-a5a0-49a9b1637ea5 | -6.1416 | -43.9563 | 2024-10-31 00:55:40 | GOES-16 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 92.5 |
| f1c1e6e6-478a-34d1-8f12-eea5adff83ab | -10.0118 | -64.8023 | 2024-10-31 00:56:03 | GOES-16 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 55.7 |
| 056b766a-4779-3095-8c23-38dcb488079c | -12.4438 | -43.7005 | 2024-10-31 00:56:15 | GOES-16 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 70.9 |
| ed8bd590-abe7-3625-8a0f-37478cb793b1 | -12.424 | -43.7274 | 2024-10-31 00:56:15 | GOES-16 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 178.4 |
| e97bfba6-8135-3fef-8a16-69e8adcdba8c | -12.4244 | -43.7037 | 2024-10-31 00:56:15 | GOES-16 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 74.9 |
| 5d66d163-51be-3bd2-a800-f37ea7224f2b | -12.4433 | -43.7242 | 2024-10-31 00:56:15 | GOES-16 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 161.3 |
| 3ca56775-210a-382b-baa3-8b91aa3f6230 | -0.7552 | -62.8933 | 2024-10-31 01:05:10 | GOES-16 | BARCELOS | AMAZONAS | Brasil | 1300409 | 13 | 33 | nan | nan | nan | Amazônia | 33.4 |
| 5b3018ca-8997-3851-81d7-688bde4b4373 | -1.2497 | -46.6147 | 2024-10-31 01:05:13 | GOES-16 | AUGUSTO CORRÊA | PARÁ | Brasil | 1500909 | 15 | 33 | nan | nan | nan | Amazônia | 36.6 |
| 7944115f-49c5-3423-964d-453df34c03b4 | -2.1718 | -47.9506 | 2024-10-31 01:05:18 | GOES-16 | SÃO DOMINGOS DO CAPIM | PARÁ | Brasil | 1507201 | 15 | 33 | nan | nan | nan | Amazônia | 65.9 |
| 0194a3a3-c669-3123-a89a-15f4f7111190 | -3.1787 | -50.5807 | 2024-10-31 01:05:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 52.8 |
| f0a71e79-dc41-3658-ae78-59ed61b15b36 | -3.2366 | -45.83 | 2024-10-31 01:05:24 | GOES-16 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 47.6 |
| 4e3cb5c4-6eb0-325e-b7e9-51b9011af364 | -4.2563 | -43.4368 | 2024-10-31 01:05:30 | GOES-16 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 62.1 |
| 807f0506-052f-3798-89f2-90c1b0f4b2cf | -4.2749 | -43.4357 | 2024-10-31 01:05:30 | GOES-16 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 94.7 |
| 05ee296e-fdc6-353a-9019-ba02be08b96d | -4.4969 | -46.4839 | 2024-10-31 01:05:31 | GOES-16 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 55.4 |
| c23fd380-67d3-314e-9f3b-32c7c86a68e3 | -4.4971 | -46.4618 | 2024-10-31 01:05:31 | GOES-16 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 54.2 |
| 6aeb119a-e845-3d7c-a478-48ebe3031aef | -4.6511 | -43.1104 | 2024-10-31 01:05:32 | GOES-16 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 51.1 |
| 0ff6f0e4-7eeb-37f7-8190-b702e4690bb4 | -5.0464 | -45.1768 | 2024-10-31 01:05:34 | GOES-16 | SÃO RAIMUNDO DO DOCA BEZERRA | MARANHÃO | Brasil | 2111631 | 21 | 33 | nan | nan | nan | Cerrado | 48.0 |
| b2625c77-51f1-31e9-9c59-7aebd460993b | -5.0466 | -45.1542 | 2024-10-31 01:05:34 | GOES-16 | SÃO RAIMUNDO DO DOCA BEZERRA | MARANHÃO | Brasil | 2111631 | 21 | 33 | nan | nan | nan | Cerrado | 78.0 |
| 3584cc6d-1060-3cc8-9cf1-4d1e00da85e2 | -5.028 | -45.1554 | 2024-10-31 01:05:34 | GOES-16 | SÃO RAIMUNDO DO DOCA BEZERRA | MARANHÃO | Brasil | 2111631 | 21 | 33 | nan | nan | nan | Cerrado | 47.6 |
| d7b16642-1db4-3f64-ae59-7e9abed71c6d | -5.3228 | -43.3454 | 2024-10-31 01:05:36 | GOES-16 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 60.1 |
| 7fa6d2b5-7010-3bae-86fa-0949671c571d | -6.1416 | -43.9563 | 2024-10-31 01:05:40 | GOES-16 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 98.6 |
| dbe3ca88-f3f0-3b1e-a672-e7617da61635 | -10.0118 | -64.8023 | 2024-10-31 01:06:03 | GOES-16 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 46.0 |
| f91438fb-75b0-349b-bc2e-6d3b1c48e62a | -25.55364 | -51.08713 | 2024-10-31 01:07:00 | TERRA_M-M | IRATI | PARANÁ | Brasil | 4110706 | 41 | 33 | nan | nan | nan | Mata Atlântica | 13.0 |
| 54b7a1bd-88c0-3f6e-897f-557e0d8cdf79 | -23.9933 | -54.10476 | 2024-10-31 01:07:00 | TERRA_M-M | ALTÔNIA | PARANÁ | Brasil | 4100509 | 41 | 33 | nan | nan | nan | Mata Atlântica | 18.2 |
| 52a4531f-a111-3cf4-81d0-5e8fd4ea15a7 | -23.9898 | -54.09874 | 2024-10-31 01:07:00 | TERRA_M-M | ALTÔNIA | PARANÁ | Brasil | 4100509 | 41 | 33 | nan | nan | nan | Mata Atlântica | 40.0 |
| 5b7c83c3-79c1-310d-92f1-125e24ba5dbb | -23.9817 | -54.10618 | 2024-10-31 01:07:00 | TERRA_M-M | ALTÔNIA | PARANÁ | Brasil | 4100509 | 41 | 33 | nan | nan | nan | Mata Atlântica | 62.1 |
| ce9b4a71-a026-388c-9ca0-0a1fc146bb08 | -23.9782 | -54.10019 | 2024-10-31 01:07:00 | TERRA_M-M | ALTÔNIA | PARANÁ | Brasil | 4100509 | 41 | 33 | nan | nan | nan | Mata Atlântica | 31.0 |
| 305c58d6-271f-3579-92cb-0db56e30e6e5 | -23.76886 | -50.03788 | 2024-10-31 01:07:00 | TERRA_M-M | JABOTI | PARANÁ | Brasil | 4111704 | 41 | 33 | nan | nan | nan | Mata Atlântica | 5.9 |
| 3ca310be-d106-3664-bfdf-bc5d2140eab1 | -23.51485 | -51.22152 | 2024-10-31 01:07:00 | TERRA_M-M | LONDRINA | PARANÁ | Brasil | 4113700 | 41 | 33 | nan | nan | nan | Mata Atlântica | 8.4 |
| 6a0b2b46-6591-3a26-8296-d14d812faa90 | -22.36349 | -48.76511 | 2024-10-31 01:07:00 | TERRA_M-M | PEDERNEIRAS | SÃO PAULO | Brasil | 3536703 | 35 | 33 | nan | nan | nan | Mata Atlântica | 8.2 |
| b160737e-f6f6-3dd5-9a0b-328e188560b0 | -22.36214 | -48.75557 | 2024-10-31 01:07:00 | TERRA_M-M | PEDERNEIRAS | SÃO PAULO | Brasil | 3536703 | 35 | 33 | nan | nan | nan | Mata Atlântica | 8.2 |
| 776bd1df-1032-309e-8906-a7eab94992ea | -22.31663 | -48.24381 | 2024-10-31 01:07:00 | TERRA_M-M | BROTAS | SÃO PAULO | Brasil | 3507902 | 35 | 33 | nan | nan | nan | Cerrado | 13.3 |
| 5725bd62-bde8-3d95-9f97-22a9eb62fa9c | -20.95985 | -47.17099 | 2024-10-31 01:07:00 | TERRA_M-M | SANTO ANTÔNIO DA ALEGRIA | SÃO PAULO | Brasil | 3547908 | 35 | 33 | nan | nan | nan | Cerrado | 12.2 |
| df8abc96-9b51-39be-ade6-7a0915064a28 | -20.95056 | -47.17248 | 2024-10-31 01:07:00 | TERRA_M-M | SÃO SEBASTIÃO DO PARAÍSO | MINAS GERAIS | Brasil | 3164704 | 31 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 3d90f377-e0e2-397d-80b8-5b6a5c4156f2 | -20.70986 | -47.28604 | 2024-10-31 01:07:00 | TERRA_M-M | PATROCÍNIO PAULISTA | SÃO PAULO | Brasil | 3536307 | 35 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 918add35-22ce-35fc-95a2-37f99918c43e | -20.31823 | -50.01656 | 2024-10-31 01:07:00 | TERRA_M-M | PARISI | SÃO PAULO | Brasil | 3536257 | 35 | 33 | nan | nan | nan | Mata Atlântica | 37.6 |
| 84c05e2d-aa0f-3d0a-b064-468e79c29af2 | -20.31694 | -50.00707 | 2024-10-31 01:07:00 | TERRA_M-M | PARISI | SÃO PAULO | Brasil | 3536257 | 35 | 33 | nan | nan | nan | Mata Atlântica | 10.3 |
| d0478982-e01a-31a3-947d-f932e0af5f35 | -16.82233 | -56.69022 | 2024-10-31 01:09:00 | TERRA_M-M | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 18.1 |
| 1782458e-2198-3f69-818d-bd1d66f71a71 | -16.41911 | -54.83508 | 2024-10-31 01:09:00 | TERRA_M-M | RONDONÓPOLIS | MATO GROSSO | Brasil | 5107602 | 51 | 33 | nan | nan | nan | Cerrado | 11.3 |
| c26ac9ff-5bbe-33ad-a38a-4e3ace76304f | -12.8151 | -51.62053 | 2024-10-31 01:09:00 | TERRA_M-M | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 4.8 |
| ee4a9c66-539c-3676-939e-2e3735eda3c9 | -12.80623 | -51.62184 | 2024-10-31 01:09:00 | TERRA_M-M | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 07c96e55-e0bc-3bac-bb87-9c5adf018778 | -12.80498 | -51.61274 | 2024-10-31 01:09:00 | TERRA_M-M | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 10.3 |
| 1eefbcc8-192b-3e0a-8ce6-39a11c77da69 | -12.7961 | -51.61405 | 2024-10-31 01:09:00 | TERRA_M-M | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 14.2 |
| 302e8150-6ada-3dbe-ae8e-bd23b5dc6c61 | -17.57105 | -52.41201 | 2024-10-31 01:09:00 | TERRA_M-M | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 5.8 |
| fee9ad92-b0d9-397d-8272-2d185e239fba | -19.6334 | -56.72279 | 2024-10-31 01:09:00 | TERRA_M-M | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 30.5 |
| a8958824-4ffe-3d6c-9c1b-2ad0cb8cc98e | -19.63167 | -56.74038 | 2024-10-31 01:09:00 | TERRA_M-M | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 13.8 |
| ca0c60f0-b6fe-3486-ba1c-b4f390b13f32 | -19.631 | -56.70034 | 2024-10-31 01:09:00 | TERRA_M-M | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 87.5 |
| a7a67a3f-3d77-3c9d-8c7c-e15e48a5868c | -19.62943 | -56.71782 | 2024-10-31 01:09:00 | TERRA_M-M | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 110.4 |
| 7a26cab0-70e7-3c22-bafa-d8ba99c9b029 | -19.6272 | -56.69535 | 2024-10-31 01:09:00 | TERRA_M-M | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 87.5 |
| abf6bde9-a087-3854-8397-cd61fa0d8f69 | -19.62009 | -56.72426 | 2024-10-31 01:09:00 | TERRA_M-M | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 128.9 |
| decc126b-65a2-3abe-a65f-7ead66643731 | -19.61834 | -56.74189 | 2024-10-31 01:09:00 | TERRA_M-M | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 57.8 |
| f0018a17-dddd-3faa-89db-e778e8ad3eab | -19.61771 | -56.70182 | 2024-10-31 01:09:00 | TERRA_M-M | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 62.8 |
| ca88a2f0-5960-3dc5-809f-e6d7999a7e7f | -19.61612 | -56.71932 | 2024-10-31 01:09:00 | TERRA_M-M | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 181.9 |


[Clique aqui para ver as próximas entradas](README7.md)
