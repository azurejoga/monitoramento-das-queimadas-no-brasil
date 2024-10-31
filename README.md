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
| 0833f640-8d42-3228-bcae-fcae9ad63b58 | -0.7552 | -62.8933 | 2024-10-31 00:05:10 | GOES-16 | BARCELOS | AMAZONAS | Brasil | 1300409 | 13 | 33 | nan | nan | nan | Amazônia | 33.7 |
| 62473940-e7b1-30e2-8219-0c5290e67aca | -0.7734 | -62.8932 | 2024-10-31 00:05:10 | GOES-16 | BARCELOS | AMAZONAS | Brasil | 1300409 | 13 | 33 | nan | nan | nan | Amazônia | 32.8 |
| 55488858-9e87-319d-aced-fdbacf25efcb | -1.063 | -47.6235 | 2024-10-31 00:05:12 | GOES-16 | MARAPANIM | PARÁ | Brasil | 1504406 | 15 | 33 | nan | nan | nan | Amazônia | 64.1 |
| 9263098a-b27b-3f83-8323-75fb40c303b6 | -1.063 | -47.6452 | 2024-10-31 00:05:12 | GOES-16 | MARAPANIM | PARÁ | Brasil | 1504406 | 15 | 33 | nan | nan | nan | Amazônia | 58.2 |
| 3852f094-e920-34e7-8e38-0815b87a1d82 | -1.2497 | -46.6147 | 2024-10-31 00:05:13 | GOES-16 | AUGUSTO CORRÊA | PARÁ | Brasil | 1500909 | 15 | 33 | nan | nan | nan | Amazônia | 56.2 |
| 59091d41-836c-37c5-b60e-c5fb60b04136 | -2.1718 | -47.9506 | 2024-10-31 00:05:18 | GOES-16 | SÃO DOMINGOS DO CAPIM | PARÁ | Brasil | 1507201 | 15 | 33 | nan | nan | nan | Amazônia | 77.4 |
| dcb37cec-e4de-3867-907b-f17eb9794047 | -2.503 | -48.4811 | 2024-10-31 00:05:20 | GOES-16 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 71.9 |
| e4c71bae-87ef-35cc-88f2-62daa5608b4c | -2.5031 | -48.4596 | 2024-10-31 00:05:20 | GOES-16 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 81.1 |
| db627c03-8141-377d-88d6-e3fd95e16f99 | -2.5215 | -48.4806 | 2024-10-31 00:05:20 | GOES-16 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 105.0 |
| b9a21e8e-10ef-3f55-899d-882fa2793f6e | -2.5216 | -48.4591 | 2024-10-31 00:05:20 | GOES-16 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 133.5 |
| 652aa694-72ec-346d-94ef-d6938929f443 | -2.5401 | -48.4586 | 2024-10-31 00:05:20 | GOES-16 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 56.4 |
| fe86e1f7-306a-374b-b5ee-a268966b4db4 | -2.8652 | -45.8213 | 2024-10-31 00:05:22 | GOES-16 | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | 79.2 |
| eb129660-88e4-3845-9b5b-d81b45f69822 | -2.8838 | -45.8207 | 2024-10-31 00:05:22 | GOES-16 | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | 74.5 |
| 02b74013-1458-35d5-8457-1b758883ceb7 | -3.2366 | -45.83 | 2024-10-31 00:05:24 | GOES-16 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 84.4 |
| a670284e-3012-3094-8a0e-4886921b1be8 | -3.2535 | -50.3479 | 2024-10-31 00:05:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 81.9 |
| 53fc41b5-13ff-3a8a-ad74-8ef6d5cf04a4 | -3.2535 | -50.3269 | 2024-10-31 00:05:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 70.3 |
| 4973b2d4-371f-375e-874c-0864693c2a39 | -3.2719 | -50.3473 | 2024-10-31 00:05:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 58.2 |
| ac4830db-94ad-31ef-9864-ba23c7a89d92 | -3.5631 | -47.3847 | 2024-10-31 00:05:26 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 72.9 |
| 9bf015f4-d9e8-3222-b357-fbf7e6c4687f | -3.5632 | -47.3629 | 2024-10-31 00:05:26 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 71.9 |
| c4fe70b5-fc49-3679-97fc-4d265f6f5381 | -3.5818 | -47.3621 | 2024-10-31 00:05:26 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 71.3 |
| 23fee888-8973-33c4-9433-11f6965c38f7 | -3.6157 | -44.4824 | 2024-10-31 00:05:26 | GOES-16 | MATÕES DO NORTE | MARANHÃO | Brasil | 2106631 | 21 | 33 | nan | nan | nan | Cerrado | 45.7 |
| 9df0c094-d32c-305b-b28f-2c0d05bc37f4 | -3.8227 | -51.0389 | 2024-10-31 00:05:28 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 83.0 |
| 4b41f7cf-899d-316c-8ba6-e82bd6397373 | -3.8228 | -51.0181 | 2024-10-31 00:05:28 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 57.1 |
| dbc34d5d-7939-3307-b36c-b2d547626fe0 | -3.8412 | -51.0383 | 2024-10-31 00:05:28 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 53.2 |
| 8529646b-6b67-3314-be75-6ee18a6ec831 | -4.2563 | -43.4368 | 2024-10-31 00:05:30 | GOES-16 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 119.5 |
| 8f469d72-94cc-3e3c-9a8e-52671d8cc847 | -4.2749 | -43.4357 | 2024-10-31 00:05:30 | GOES-16 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 132.3 |
| 52b793b1-0738-3d48-924d-c30cccf21cd2 | -4.3353 | -48.5862 | 2024-10-31 00:05:30 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 69.1 |
| fb956183-510c-36cf-bfa1-d4678066a045 | -4.6511 | -43.1104 | 2024-10-31 00:05:32 | GOES-16 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 65.9 |
| 10792fac-c4bc-38a4-ac5f-e1b311397306 | -4.7158 | -44.4697 | 2024-10-31 00:05:32 | GOES-16 | SANTO ANTÔNIO DOS LOPES | MARANHÃO | Brasil | 2110302 | 21 | 33 | nan | nan | nan | Cerrado | 44.8 |
| db4f88b8-4036-36c5-af4d-633086c5e317 | -5.0278 | -45.178 | 2024-10-31 00:05:34 | GOES-16 | SÃO RAIMUNDO DO DOCA BEZERRA | MARANHÃO | Brasil | 2111631 | 21 | 33 | nan | nan | nan | Cerrado | 49.4 |
| bb31f0e8-5789-36d2-8c0b-6b3c61b85aca | -5.028 | -45.1554 | 2024-10-31 00:05:34 | GOES-16 | SÃO RAIMUNDO DO DOCA BEZERRA | MARANHÃO | Brasil | 2111631 | 21 | 33 | nan | nan | nan | Cerrado | 66.6 |
| 70a3511e-0634-3e73-9479-24e958b007e8 | -5.0464 | -45.1768 | 2024-10-31 00:05:34 | GOES-16 | SÃO RAIMUNDO DO DOCA BEZERRA | MARANHÃO | Brasil | 2111631 | 21 | 33 | nan | nan | nan | Cerrado | 74.4 |
| 1cfc4310-08ed-3002-b547-f83ffe2928e6 | -5.0466 | -45.1542 | 2024-10-31 00:05:34 | GOES-16 | SÃO RAIMUNDO DO DOCA BEZERRA | MARANHÃO | Brasil | 2111631 | 21 | 33 | nan | nan | nan | Cerrado | 113.7 |
| 0248bd23-cd6d-312e-8df0-f2e2e1c46bb8 | -6.1229 | -43.9578 | 2024-10-31 00:05:40 | GOES-16 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 93.1 |
| 32fdc8a6-0c4f-3c65-95fa-89a6a2b40385 | -6.1414 | -43.9794 | 2024-10-31 00:05:40 | GOES-16 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 75.0 |
| 69603d6d-b41e-3c5a-bfe7-de6fe6578dc4 | -6.1416 | -43.9563 | 2024-10-31 00:05:40 | GOES-16 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 119.2 |
| 19d5d54b-20b1-346c-8085-56e4114ca947 | -5.9788 | -45.3621 | 2024-10-31 00:05:40 | GOES-16 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 55.2 |
| 1e55742e-ebf4-32cf-aabf-1d38c59ac441 | -6.1857 | -47.3065 | 2024-10-31 00:05:41 | GOES-16 | CAMPESTRE DO MARANHÃO | MARANHÃO | Brasil | 2102556 | 21 | 33 | nan | nan | nan | Cerrado | 89.5 |
| 9793e280-e875-366e-8037-015ba5fb0044 | -6.1859 | -47.2845 | 2024-10-31 00:05:41 | GOES-16 | CAMPESTRE DO MARANHÃO | MARANHÃO | Brasil | 2102556 | 21 | 33 | nan | nan | nan | Cerrado | 65.1 |
| 357b696c-1c4b-3bb9-b282-0d57c296b179 | -6.167 | -47.3078 | 2024-10-31 00:05:41 | GOES-16 | CAMPESTRE DO MARANHÃO | MARANHÃO | Brasil | 2102556 | 21 | 33 | nan | nan | nan | Cerrado | 131.9 |
| 42ba1f21-2688-37a5-a1a7-76274e0ea8fd | -6.1672 | -47.2858 | 2024-10-31 00:05:41 | GOES-16 | CAMPESTRE DO MARANHÃO | MARANHÃO | Brasil | 2102556 | 21 | 33 | nan | nan | nan | Cerrado | 82.3 |
| ed1348a0-45fa-31d5-8ec5-d6b11bb51012 | -10.0118 | -64.8023 | 2024-10-31 00:06:03 | GOES-16 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 64.3 |
| 7385f853-ca3f-3b03-96d9-c9ed6ea3bc28 | -12.424 | -43.7274 | 2024-10-31 00:06:15 | GOES-16 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 121.6 |
| 27a48b56-3128-376c-91b3-843c6fc24d1a | -12.4428 | -43.7479 | 2024-10-31 00:06:15 | GOES-16 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 68.0 |
| a6f99f4d-243d-393f-9172-fad6835d2c6e | -12.4433 | -43.7242 | 2024-10-31 00:06:15 | GOES-16 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 127.1 |
| 418c9418-8ec1-372f-8dfa-9c2e61388ca4 | -20.3209 | -50.0096 | 2024-10-31 00:06:58 | GOES-16 | PARISI | SÃO PAULO | Brasil | 3536257 | 35 | 33 | nan | nan | nan | Mata Atlântica | 98.4 |
| a4121365-1faa-310b-bc72-9d1233e8f05e | -0.7552 | -62.8933 | 2024-10-31 00:15:10 | GOES-16 | BARCELOS | AMAZONAS | Brasil | 1300409 | 13 | 33 | nan | nan | nan | Amazônia | 40.1 |
| aede0f6b-2717-3f0b-a81f-73ca0f3a5198 | -0.7734 | -62.8932 | 2024-10-31 00:15:10 | GOES-16 | BARCELOS | AMAZONAS | Brasil | 1300409 | 13 | 33 | nan | nan | nan | Amazônia | 35.6 |
| 020c1508-a9cb-3f64-940e-1d80de4f60f5 | -1.063 | -47.6452 | 2024-10-31 00:15:12 | GOES-16 | MARAPANIM | PARÁ | Brasil | 1504406 | 15 | 33 | nan | nan | nan | Amazônia | 58.6 |
| 696cc7df-5c43-32ff-aa26-6572e93a0340 | -1.2497 | -46.6147 | 2024-10-31 00:15:13 | GOES-16 | AUGUSTO CORRÊA | PARÁ | Brasil | 1500909 | 15 | 33 | nan | nan | nan | Amazônia | 43.9 |
| 26398246-3fcc-3b88-ac7f-2b7b22b1b401 | -2.1718 | -47.9506 | 2024-10-31 00:15:18 | GOES-16 | SÃO DOMINGOS DO CAPIM | PARÁ | Brasil | 1507201 | 15 | 33 | nan | nan | nan | Amazônia | 73.9 |
| d9a1f0c4-6a78-3aaa-b5f5-460dc32a609c | -2.8838 | -45.8207 | 2024-10-31 00:15:22 | GOES-16 | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | 81.2 |
| ca6f8d20-5565-3f3a-b205-0ef59f561bcb | -2.8652 | -45.8213 | 2024-10-31 00:15:22 | GOES-16 | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | 82.4 |
| 45e7a44d-bfb7-3e02-8f9d-6a3d4f05a34b | -3.2366 | -45.83 | 2024-10-31 00:15:24 | GOES-16 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 74.1 |
| b5647e0f-bf8b-3963-b6a3-029ddd5fcda4 | -3.2945 | -45.402 | 2024-10-31 00:15:24 | GOES-16 | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | 55.6 |
| f7641946-e424-309f-889f-3aabb6f0d628 | -3.8227 | -51.0389 | 2024-10-31 00:15:28 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 57.0 |
| f068237e-2d86-3e44-a511-85f39ac7e326 | -4.2563 | -43.4368 | 2024-10-31 00:15:30 | GOES-16 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 120.0 |
| 447f6e88-591e-3145-90a8-d0eb18d2505c | -4.2749 | -43.4357 | 2024-10-31 00:15:30 | GOES-16 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 134.5 |
| 86306a85-a4a2-3c25-b28a-be8fa3776d3d | -4.3353 | -48.5862 | 2024-10-31 00:15:30 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 63.9 |
| e6b0be65-0e27-3d97-ac4d-6101d5d83929 | -4.6511 | -43.1104 | 2024-10-31 00:15:32 | GOES-16 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 73.4 |
| e0cacffb-59e4-35a3-9ba1-92fbe9b6f5b0 | -4.7158 | -44.4697 | 2024-10-31 00:15:32 | GOES-16 | SANTO ANTÔNIO DOS LOPES | MARANHÃO | Brasil | 2110302 | 21 | 33 | nan | nan | nan | Cerrado | 41.3 |
| 4ceccb09-a156-3dce-aceb-f4173c51e49a | -5.0278 | -45.178 | 2024-10-31 00:15:34 | GOES-16 | SÃO RAIMUNDO DO DOCA BEZERRA | MARANHÃO | Brasil | 2111631 | 21 | 33 | nan | nan | nan | Cerrado | 48.4 |
| bdecde86-3bb9-34b2-b81a-2e2a66803814 | -5.028 | -45.1554 | 2024-10-31 00:15:34 | GOES-16 | SÃO RAIMUNDO DO DOCA BEZERRA | MARANHÃO | Brasil | 2111631 | 21 | 33 | nan | nan | nan | Cerrado | 62.7 |
| 703271c4-e912-3f9c-b13c-32359fa8f452 | -5.0464 | -45.1768 | 2024-10-31 00:15:34 | GOES-16 | SÃO RAIMUNDO DO DOCA BEZERRA | MARANHÃO | Brasil | 2111631 | 21 | 33 | nan | nan | nan | Cerrado | 71.6 |
| b5169d1e-fc6b-3e75-b11e-a4bf6207620d | -5.0466 | -45.1542 | 2024-10-31 00:15:34 | GOES-16 | SÃO RAIMUNDO DO DOCA BEZERRA | MARANHÃO | Brasil | 2111631 | 21 | 33 | nan | nan | nan | Cerrado | 100.8 |
| 8056e3a4-a55f-35ca-8027-ec8f85c82d9c | -6.1229 | -43.9578 | 2024-10-31 00:15:40 | GOES-16 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 84.4 |
| d9b8a0a1-f2aa-3cf6-b813-f9c0a07a5439 | -6.1414 | -43.9794 | 2024-10-31 00:15:40 | GOES-16 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 74.2 |
| 8c69fd24-6a4f-3266-80de-f7a4f6a25aa8 | -6.1416 | -43.9563 | 2024-10-31 00:15:40 | GOES-16 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 107.9 |
| 9306e830-b6eb-3994-96d3-bd87a99c4224 | -5.9788 | -45.3621 | 2024-10-31 00:15:40 | GOES-16 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 58.7 |
| 95cf528e-3d8b-3a56-a313-2c73751a24ef | -10.0118 | -64.8023 | 2024-10-31 00:16:03 | GOES-16 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 63.9 |
| 57a6ebfa-6d5a-311d-a24b-d52b3eaa0485 | -12.1031 | -43.4008 | 2024-10-31 00:16:14 | GOES-16 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 70.1 |
| faacb192-7db1-3c30-b448-b005098722ec | -12.4428 | -43.7479 | 2024-10-31 00:16:15 | GOES-16 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 77.4 |
| 45e09227-9e38-3593-b350-fb5e2ebbc269 | -12.4433 | -43.7242 | 2024-10-31 00:16:15 | GOES-16 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 180.4 |
| 3521af90-ef7d-31be-bbba-9500b29e4974 | -12.4438 | -43.7005 | 2024-10-31 00:16:15 | GOES-16 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 80.2 |
| a04acabf-b1fa-3036-ba70-b04795f9ee2f | -12.4235 | -43.7511 | 2024-10-31 00:16:15 | GOES-16 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 73.5 |
| 65b6ccf6-23dd-3686-a2fd-57eb1b12d7d2 | -12.424 | -43.7274 | 2024-10-31 00:16:15 | GOES-16 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 163.4 |
| 6867a08c-9468-3818-9909-5be64e1375da | -12.4244 | -43.7037 | 2024-10-31 00:16:15 | GOES-16 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 78.4 |
| 76005f40-785b-3ac0-a2cf-7598ab833a64 | -19.4878 | -56.6227 | 2024-10-31 00:16:55 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 85.4 |
| fd75923a-d5e9-3a54-9d8a-518db5c93f88 | -20.3209 | -50.0096 | 2024-10-31 00:16:58 | GOES-16 | PARISI | SÃO PAULO | Brasil | 3536257 | 35 | 33 | nan | nan | nan | Mata Atlântica | 94.3 |
| f667da96-fd12-3821-8794-c6115e5432f8 | -0.7552 | -62.8933 | 2024-10-31 00:25:10 | GOES-16 | BARCELOS | AMAZONAS | Brasil | 1300409 | 13 | 33 | nan | nan | nan | Amazônia | 39.3 |
| 9277f800-ca2c-3cc7-8e4b-7c8e2b7798be | -0.7734 | -62.8932 | 2024-10-31 00:25:10 | GOES-16 | BARCELOS | AMAZONAS | Brasil | 1300409 | 13 | 33 | nan | nan | nan | Amazônia | 35.8 |
| 330ea571-e219-36fe-8434-d7afd8db9877 | -1.4426 | -52.273 | 2024-10-31 00:25:14 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 70.5 |
| c209a5a7-f8ce-326e-8306-bdf76ba00cc4 | -2.1718 | -47.9506 | 2024-10-31 00:25:18 | GOES-16 | SÃO DOMINGOS DO CAPIM | PARÁ | Brasil | 1507201 | 15 | 33 | nan | nan | nan | Amazônia | 87.3 |
| e4257db9-3716-3441-8f09-fb71772105cb | -2.5031 | -48.4596 | 2024-10-31 00:25:20 | GOES-16 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 60.3 |
| 3b7fc66d-961b-3117-b129-ec8e23da90b6 | -2.5215 | -48.4806 | 2024-10-31 00:25:20 | GOES-16 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 126.6 |
| ecbc4049-c01b-34b8-99ca-356c9b2f24c3 | -2.5216 | -48.4591 | 2024-10-31 00:25:20 | GOES-16 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 176.5 |
| 157d45db-94ae-3c77-862a-8f48f14af056 | -2.8838 | -45.8207 | 2024-10-31 00:25:22 | GOES-16 | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | 71.7 |
| 04145b29-0c7e-3665-aaea-7df69a1dc711 | -3.1787 | -50.5807 | 2024-10-31 00:25:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 54.3 |
| 8b3a69f0-a667-3916-ba81-ea663224b330 | -3.2945 | -45.402 | 2024-10-31 00:25:24 | GOES-16 | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | 92.4 |
| a433e3f7-9430-34ce-b77e-a900045b908d | -4.2563 | -43.4368 | 2024-10-31 00:25:30 | GOES-16 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 93.8 |
| d5a2ab72-4f85-3378-804f-e6248c2dfeaf | -4.2749 | -43.4357 | 2024-10-31 00:25:30 | GOES-16 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 157.0 |
| 7d8dc164-01f1-3d5f-98e4-7120213f8a1d | -4.3539 | -48.5853 | 2024-10-31 00:25:31 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 55.5 |
| 35dc1114-261b-3ac8-921e-a84cfa23db03 | -5.0464 | -45.1768 | 2024-10-31 00:25:34 | GOES-16 | SÃO RAIMUNDO DO DOCA BEZERRA | MARANHÃO | Brasil | 2111631 | 21 | 33 | nan | nan | nan | Cerrado | 60.7 |
| ab8624ae-5a3d-3785-ae93-f0692325add7 | -5.0466 | -45.1542 | 2024-10-31 00:25:34 | GOES-16 | SÃO RAIMUNDO DO DOCA BEZERRA | MARANHÃO | Brasil | 2111631 | 21 | 33 | nan | nan | nan | Cerrado | 107.8 |
| 1e2027f0-f947-3430-88ed-aba9e5c4f7bb | -6.1229 | -43.9578 | 2024-10-31 00:25:40 | GOES-16 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 86.6 |
| ef8dace9-06fc-3fa7-89fa-890094adf225 | -6.1416 | -43.9563 | 2024-10-31 00:25:40 | GOES-16 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 101.5 |
| d22c5d02-6943-3fc7-8701-9cf3776f7036 | -24.0187 | -54.0443 | 2024-10-31 00:25:58 | METOP-B | ALTÔNIA | PARANÁ | Brasil | 4100509 | 41 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 1e8df597-3274-3b47-966b-dcd3c827f4da | -24.009001 | -54.045898 | 2024-10-31 00:25:58 | METOP-B | ALTÔNIA | PARANÁ | Brasil | 4100509 | 41 | 33 | nan | nan | nan | Mata Atlântica | nan |
| a6a4f235-ca0c-30ab-830e-68d1a0de6cf8 | -24.0126 | -54.070599 | 2024-10-31 00:25:58 | METOP-B | ALTÔNIA | PARANÁ | Brasil | 4100509 | 41 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 212651b6-49c1-34d1-b9a5-e9113bd9958b | -22.3528 | -48.223301 | 2024-10-31 00:26:09 | METOP-B | BROTAS | SÃO PAULO | Brasil | 3507902 | 35 | 33 | nan | nan | nan | Cerrado | nan |


[Clique aqui para ver as próximas entradas](README2.md)
