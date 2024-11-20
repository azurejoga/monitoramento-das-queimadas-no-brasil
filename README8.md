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

## Dados Diários - Página 8

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 2b9c47e7-847b-3c3c-884e-950fafc8b81e | -2.9968 | -45.4584 | 2024-11-20 00:20:00 | GOES-16 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 170.8 |
| b3aa4823-8e7d-3be4-823b-3f20284c6550 | -1.4524 | -47.1166 | 2024-11-20 00:20:00 | GOES-16 | OURÉM | PARÁ | Brasil | 1505403 | 15 | 33 | nan | nan | nan | Amazônia | 113.8 |
| 8b68365b-a306-33f9-a9ff-c4e3df6f3a13 | -11.1109 | -54.6204 | 2024-11-20 00:20:00 | GOES-16 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 92.9 |
| 452ade81-c290-3a02-983a-67683ae8c549 | -3.0109 | -51.0236 | 2024-11-20 00:20:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 74.7 |
| cb089fe1-747b-363b-8bf6-4eb2143ff442 | -4.1497 | -45.498 | 2024-11-20 00:20:00 | GOES-16 | ALTAMIRA DO MARANHÃO | MARANHÃO | Brasil | 2100402 | 21 | 33 | nan | nan | nan | Amazônia | 91.9 |
| 0da31ef9-bfc8-37fd-85d1-060802dd735d | -2.9969 | -45.436 | 2024-11-20 00:20:00 | GOES-16 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 400.8 |
| 8640c36d-f608-3a56-aa8c-e4bd12785b6f | -2.997 | -45.4135 | 2024-11-20 00:20:00 | GOES-16 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 102.4 |
| a5f75aaa-9be1-3920-86c9-fabb3dc57215 | -2.75 | -51.8377 | 2024-11-20 00:20:00 | GOES-16 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 47.0 |
| ca02f118-4c58-3139-9157-d580a9ed7e8e | -2.93 | -53.0601 | 2024-11-20 00:20:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 57.9 |
| bc302487-7b7c-3303-b38f-2a8758655dd9 | -3.802 | -47.8104 | 2024-11-20 00:20:00 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 89.5 |
| cd0ac239-1fa8-3791-967a-99c56e8dbba4 | -4.1495 | -45.5205 | 2024-11-20 00:20:00 | GOES-16 | ALTAMIRA DO MARANHÃO | MARANHÃO | Brasil | 2100402 | 21 | 33 | nan | nan | nan | Amazônia | 95.4 |
| 541a0e9b-4b19-35dc-9129-02aecd047be4 | -2.6212 | -51.8203 | 2024-11-20 00:20:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 55.6 |
| 54f3cadb-06c3-3ecb-9dd5-1bfc28832931 | -3.7858 | -44.0622 | 2024-11-20 00:20:00 | GOES-16 | PIRAPEMAS | MARANHÃO | Brasil | 2108801 | 21 | 33 | nan | nan | nan | Cerrado | 93.6 |
| 410b6fdf-76b0-3d27-bece-8ef44dafe506 | -2.6212 | -51.7997 | 2024-11-20 00:20:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 122.7 |
| 0618f62c-7c2a-32ce-be9d-67d6fd7465b6 | -4.1682 | -45.5195 | 2024-11-20 00:20:00 | GOES-16 | ALTAMIRA DO MARANHÃO | MARANHÃO | Brasil | 2100402 | 21 | 33 | nan | nan | nan | Amazônia | 221.6 |
| d7fc1bd4-1097-36fa-a3c5-387cae30340f | -4.1861 | -45.6308 | 2024-11-20 00:20:00 | GOES-16 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 82.9 |
| 35c1bd18-b251-3ade-b17e-69e46fe34ea7 | -4.4405 | -46.5754 | 2024-11-20 00:20:00 | GOES-16 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 94.7 |
| e779e639-ec5d-3c5f-aaa2-d0ee8978d97e | -5.4015 | -45.1313 | 2024-11-20 00:20:00 | GOES-16 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 66.3 |
| 91215bfb-97e0-3a13-86c6-776fbe10cc10 | -2.6397 | -51.7992 | 2024-11-20 00:30:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 52.0 |
| ed3b226e-1548-31fd-ada1-f50fd0b332b8 | -3.2014 | -54.3243 | 2024-11-20 00:30:00 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 98.4 |
| 9b55499d-1904-3290-9a33-3668e9c55db7 | -3.1477 | -49.1251 | 2024-11-20 00:30:00 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 89.4 |
| 9471d74c-7285-3a94-a1dd-d12523e96916 | -3.8021 | -47.7887 | 2024-11-20 00:30:00 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 90.6 |
| b0fd1da6-7bd6-319a-bbde-1f0a7274e3b2 | -14.8449 | -53.6661 | 2024-11-20 00:30:00 | GOES-16 | SANTO ANTÔNIO DO LESTE | MATO GROSSO | Brasil | 5107792 | 51 | 33 | nan | nan | nan | Cerrado | 63.0 |
| 655df876-1660-3cfc-8100-475634332e11 | -4.5614 | -48.0141 | 2024-11-20 00:30:00 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 102.1 |
| 00c75fc8-fa51-3a32-9092-8a8d183834ae | -11.1109 | -54.6204 | 2024-11-20 00:30:00 | GOES-16 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 113.4 |
| a51d3dae-2a75-3fbc-88c0-19bab83d4601 | -14.3409 | -51.5092 | 2024-11-20 00:30:00 | GOES-16 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 68.5 |
| e2957473-a8ba-3ef4-be2f-99fb33c46e5b | -4.1594 | -43.9739 | 2024-11-20 00:30:00 | GOES-16 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 68.7 |
| 5aa4d6c0-b1e1-3b41-9986-fcb6bf114b37 | -3.1292 | -49.1257 | 2024-11-20 00:30:00 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 70.0 |
| 56059ec9-91ec-333c-8c5b-b013df89e128 | 1.5284 | -55.9242 | 2024-11-20 00:30:00 | GOES-16 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 48.2 |
| 534bae61-da9e-379b-92d5-8017c7a3ce22 | -4.5616 | -47.9925 | 2024-11-20 00:30:00 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 58.5 |
| 9ae44c6d-160d-3bd5-bc33-34a164b99c87 | -11.092 | -54.6221 | 2024-11-20 00:30:00 | GOES-16 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 71.9 |
| c8b4276c-70c2-31bc-8743-0cae88a0f785 | -2.9969 | -45.436 | 2024-11-20 00:30:00 | GOES-16 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 259.7 |
| 7b292584-66f9-3859-a674-7ae0f018fcaa | -3.0109 | -51.0236 | 2024-11-20 00:30:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 83.6 |
| 9fb05e3b-cd56-30a0-afaf-1adbb424a1dc | -11.1106 | -54.6408 | 2024-11-20 00:30:00 | GOES-16 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 84.4 |
| b07168e3-4b8a-30d7-9607-f5477dbaf2f7 | -4.1869 | -45.4961 | 2024-11-20 00:30:00 | GOES-16 | ALTAMIRA DO MARANHÃO | MARANHÃO | Brasil | 2100402 | 21 | 33 | nan | nan | nan | Amazônia | 68.9 |
| a8afbf3e-034b-32a7-b06e-909c4eda2d7d | -2.831 | -45.1267 | 2024-11-20 00:30:00 | GOES-16 | SÃO BENTO | MARANHÃO | Brasil | 2110500 | 21 | 33 | nan | nan | nan | Amazônia | 107.3 |
| 4f86fc69-e8ac-3cc1-8c12-1e8da4ad2a8a | -3.802 | -47.8104 | 2024-11-20 00:30:00 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 106.7 |
| 0294c352-0836-3636-aca3-47fc6862cac9 | -2.1242 | -45.3735 | 2024-11-20 00:30:00 | GOES-16 | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 70.4 |
| bf2da2d7-4c61-3aed-a193-b89ccf13019a | -3.011 | -51.0028 | 2024-11-20 00:30:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 86.9 |
| 49f513aa-966c-32cc-98df-a96fb3f333fd | -2.6028 | -51.8001 | 2024-11-20 00:30:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 45.2 |
| 1105c1eb-5ceb-346c-b98d-f2f4aef403a7 | -4.3959 | -47.7618 | 2024-11-20 00:30:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 49.4 |
| a330121c-491c-3527-9814-e49346ad795d | 1.5284 | -55.9045 | 2024-11-20 00:30:00 | GOES-16 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 67.5 |
| 51a4e243-d24e-3cad-b723-cc2aa22970e5 | -0.9654 | -51.7238 | 2024-11-20 00:30:00 | GOES-16 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 58.8 |
| ee52a60c-138e-3506-a75b-d0a1d3c6dc2c | -2.6212 | -51.8203 | 2024-11-20 00:30:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 44.6 |
| f3123a64-6b2c-39f0-8b53-c3f3bbef62ee | -3.8206 | -47.7879 | 2024-11-20 00:30:00 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 75.6 |
| a497f3aa-ee6b-3ee2-bc63-970979af9f82 | -2.9117 | -53.0403 | 2024-11-20 00:30:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 56.6 |
| a1649ed1-7e48-3331-9eac-03bab80ab375 | -2.9968 | -45.4584 | 2024-11-20 00:30:00 | GOES-16 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 108.0 |
| 6cb5a09f-80b4-3c7d-9e60-93848fc8ff58 | -4.5429 | -48.0151 | 2024-11-20 00:30:00 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 69.3 |
| ec136592-dc7d-3471-9c63-3b2baf110e68 | -4.2528 | -53.6684 | 2024-11-20 00:30:00 | GOES-16 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 77.2 |
| bc938752-7474-3f34-8540-66e88440b766 | -3.7858 | -44.0622 | 2024-11-20 00:30:00 | GOES-16 | PIRAPEMAS | MARANHÃO | Brasil | 2108801 | 21 | 33 | nan | nan | nan | Cerrado | 84.2 |
| a29ae3a8-5d85-3bcf-9a1d-a1c26844bdfa | -0.947 | -51.724 | 2024-11-20 00:30:00 | GOES-16 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 57.8 |
| 0ad58cfe-c814-3d02-8e73-3b70605c2974 | -2.6212 | -51.7997 | 2024-11-20 00:30:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 91.3 |
| 3de748c4-c948-3e35-8c96-a4cd6baf36c6 | -4.1683 | -45.4971 | 2024-11-20 00:30:00 | GOES-16 | ALTAMIRA DO MARANHÃO | MARANHÃO | Brasil | 2100402 | 21 | 33 | nan | nan | nan | Amazônia | 147.4 |
| 2b3320f0-984e-3239-bf9e-67901518cc11 | -4.4592 | -46.5745 | 2024-11-20 00:30:00 | GOES-16 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 96.5 |
| c5124176-545c-33e6-a6dd-e880b2cb1270 | -3.8205 | -47.8096 | 2024-11-20 00:30:00 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 83.6 |
| 5fcdc196-7a5f-38dc-91b9-16df544736ac | -4.0672 | -46.8366 | 2024-11-20 00:30:00 | GOES-16 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 68.4 |
| 13bb9470-fd21-3688-a0c4-3021d879fbfe | -2.9784 | -45.4366 | 2024-11-20 00:30:00 | GOES-16 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 71.5 |
| 477855a6-c229-3f34-aaf3-fb622415602e | -17.1362 | -57.5041 | 2024-11-20 00:30:00 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 55.0 |
| 7cb53267-0356-3261-a1c1-fcd13d59c5b6 | -1.4524 | -47.1166 | 2024-11-20 00:30:00 | GOES-16 | OURÉM | PARÁ | Brasil | 1505403 | 15 | 33 | nan | nan | nan | Amazônia | 74.6 |
| 5afa359c-b0b9-3637-abd0-ab06311fc544 | -4.1682 | -45.5195 | 2024-11-20 00:30:00 | GOES-16 | ALTAMIRA DO MARANHÃO | MARANHÃO | Brasil | 2100402 | 21 | 33 | nan | nan | nan | Amazônia | 178.4 |
| 8af52cf3-3316-3b97-84e1-c1e7e94ed725 | -4.1868 | -45.5186 | 2024-11-20 00:30:00 | GOES-16 | ALTAMIRA DO MARANHÃO | MARANHÃO | Brasil | 2100402 | 21 | 33 | nan | nan | nan | Amazônia | 78.1 |
| d03a893d-fd0c-3d6a-a0ee-abf69fa71d1e | -3.0155 | -45.4353 | 2024-11-20 00:30:00 | GOES-16 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 172.3 |
| 8bea11f8-91cb-3613-9234-72aff26bebcb | -4.459 | -46.5966 | 2024-11-20 00:30:00 | GOES-16 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 69.7 |
| 545a0987-b23c-3a16-9183-dee87de51dce | -3.0154 | -45.4577 | 2024-11-20 00:30:00 | GOES-16 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 78.7 |
| 13c76282-f72c-3c29-92a9-e0a05af90479 | -2.9116 | -53.0606 | 2024-11-20 00:30:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 105.6 |
| 89294259-835d-3a89-babc-f39e52642d3d | -4.2528 | -53.6684 | 2024-11-20 00:40:00 | GOES-16 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 66.1 |
| e7d98eed-c1fe-350a-89a9-5cb67ce089b7 | -9.9329 | -36.1517 | 2024-11-20 00:40:00 | GOES-16 | JEQUIÁ DA PRAIA | ALAGOAS | Brasil | 2703759 | 27 | 33 | nan | nan | nan | Mata Atlântica | 86.5 |
| 28b5c6f1-3ed2-3995-8b0a-4ed2283ed0ad | -2.9968 | -45.4584 | 2024-11-20 00:40:00 | GOES-16 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 91.0 |
| 435dccc0-a5c3-3021-800e-bc007ea9d98b | -4.5614 | -48.0141 | 2024-11-20 00:40:00 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 68.9 |
| dac26f13-456a-3561-9551-7ca974e6f334 | 1.5284 | -55.9045 | 2024-11-20 00:40:00 | GOES-16 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 93.6 |
| 11c8ee02-667e-33d1-bb2d-341ba06b6659 | -4.1682 | -45.5195 | 2024-11-20 00:40:00 | GOES-16 | ALTAMIRA DO MARANHÃO | MARANHÃO | Brasil | 2100402 | 21 | 33 | nan | nan | nan | Amazônia | 153.7 |
| 416a4242-3788-3db9-8e3c-bb1c4ba8be2e | -3.0355 | -49.4476 | 2024-11-20 00:40:00 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 52.9 |
| 4e4aee28-89aa-3529-afa0-ea0f498981be | -0.9654 | -51.7238 | 2024-11-20 00:40:00 | GOES-16 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 58.7 |
| 5f16f662-d11b-3ab3-a140-7c09343f3c98 | -9.9324 | -36.1788 | 2024-11-20 00:40:00 | GOES-16 | JEQUIÁ DA PRAIA | ALAGOAS | Brasil | 2703759 | 27 | 33 | nan | nan | nan | Mata Atlântica | 126.9 |
| eaf4930f-00eb-3114-8421-c11fcd9fbe36 | -4.0672 | -46.8366 | 2024-11-20 00:40:00 | GOES-16 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 65.2 |
| b2b44979-6b2d-3d7c-a786-681632f6afa7 | -1.5072 | -47.4432 | 2024-11-20 00:40:00 | GOES-16 | SÃO MIGUEL DO GUAMÁ | PARÁ | Brasil | 1507607 | 15 | 33 | nan | nan | nan | Amazônia | 71.6 |
| 8d6c7369-6bb2-319d-871c-d2552d5707ff | -4.3959 | -47.7618 | 2024-11-20 00:40:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 59.7 |
| c25c18f5-e97d-3e5d-b2f0-b46ad2b3b96c | -3.0155 | -45.4353 | 2024-11-20 00:40:00 | GOES-16 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 151.2 |
| ea547409-eb0e-32e9-8b86-d31f9ef23d77 | -3.802 | -47.8104 | 2024-11-20 00:40:00 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 103.8 |
| 351d8166-a79f-3ef5-9225-dadb6a51a481 | -3.8206 | -47.7879 | 2024-11-20 00:40:00 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 78.8 |
| 3240bfa0-ab2f-3b7f-8d02-5d03bea3536e | -4.4405 | -46.5754 | 2024-11-20 00:40:00 | GOES-16 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 72.4 |
| ce891502-8795-38d4-b296-09976c105a3f | -2.8124 | -45.1274 | 2024-11-20 00:40:00 | GOES-16 | PALMEIRÂNDIA | MARANHÃO | Brasil | 2107605 | 21 | 33 | nan | nan | nan | Amazônia | 70.3 |
| 709620f5-ac26-3ef1-b494-20e5f5d70d88 | -3.011 | -51.0028 | 2024-11-20 00:40:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 82.9 |
| 46e71e95-0860-3357-857c-5ae157075020 | -3.0354 | -49.4688 | 2024-11-20 00:40:00 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 47.3 |
| d312e62b-cf74-3c49-a1fa-a2a9ed2300b0 | -2.9969 | -45.436 | 2024-11-20 00:40:00 | GOES-16 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 216.0 |
| b944b641-61e4-3b63-b7e3-ef208b6b1bec | -4.1683 | -45.4971 | 2024-11-20 00:40:00 | GOES-16 | ALTAMIRA DO MARANHÃO | MARANHÃO | Brasil | 2100402 | 21 | 33 | nan | nan | nan | Amazônia | 133.0 |
| bacd646b-57a8-3134-91f0-4d5bf9026699 | -4.4592 | -46.5745 | 2024-11-20 00:40:00 | GOES-16 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 84.9 |
| 7891a647-8187-3478-87cd-2d322141853c | -3.8205 | -47.8096 | 2024-11-20 00:40:00 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 92.0 |
| 7d461a09-438a-3404-882d-32900118d387 | -1.2017 | -53.6769 | 2024-11-20 00:40:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 70.9 |
| 7e43c69f-d450-311f-ab36-d8af7e0459c6 | -3.0109 | -51.0236 | 2024-11-20 00:40:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 86.3 |
| 4f0864ec-a0ac-3e1c-8cb0-987a0a5ae8a1 | -4.5429 | -48.0151 | 2024-11-20 00:40:00 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 55.5 |
| 16cbd7d5-4079-386e-b21b-c312b62d8e50 | -4.1594 | -43.9739 | 2024-11-20 00:40:00 | GOES-16 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 55.3 |
| 87e0a582-4577-317c-8cdc-8a66be9e6c61 | -2.9116 | -53.0606 | 2024-11-20 00:40:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 74.4 |
| 6735c890-c595-34e7-849d-019dcfa50a45 | -1.4524 | -47.1166 | 2024-11-20 00:40:00 | GOES-16 | OURÉM | PARÁ | Brasil | 1505403 | 15 | 33 | nan | nan | nan | Amazônia | 61.8 |
| 94584f6a-4f33-353e-9c6b-0f0824e08f36 | -3.2586 | -45.1332 | 2024-11-20 00:40:00 | GOES-16 | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | 90.1 |
| ecb113fc-551c-3ae8-95e1-6bfaa74a634f | -3.1477 | -49.1251 | 2024-11-20 00:40:00 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 64.3 |
| af1ec111-df07-3a9f-b1e3-7462cda364ad | -2.6028 | -51.8001 | 2024-11-20 00:40:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 45.8 |
| 381eaf68-95b8-34c1-9afc-57aaa22eaa36 | -2.831 | -45.1267 | 2024-11-20 00:40:00 | GOES-16 | SÃO BENTO | MARANHÃO | Brasil | 2110500 | 21 | 33 | nan | nan | nan | Amazônia | 205.3 |
| 21af7b33-15d5-359a-b3f8-b82e89cce74d | 1.5284 | -55.9242 | 2024-11-20 00:40:00 | GOES-16 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 65.8 |
| ff2a1a99-6636-3287-8a6a-2a5bc42966af | -3.7301 | -47.3779 | 2024-11-20 00:40:00 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 44.6 |


[Clique aqui para ver as próximas entradas](README9.md)
