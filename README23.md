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

## Dados Diários - Página 23

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| fcbaa356-f23b-36e6-a4c2-155fff8e2d15 | -19.8473 | -57.7835 | 2025-11-30 12:50:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 74.4 |
| 2f3a1c87-cbbe-3a0a-a685-79b3db705a0c | -19.9339 | -57.4386 | 2025-11-30 12:50:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 177.8 |
| afdba333-281a-399a-97fd-073d35627138 | -19.9343 | -57.4177 | 2025-11-30 12:50:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 137.9 |
| 5a1afeb5-7398-3e61-997f-e6228504398a | -19.9343 | -57.4177 | 2025-11-30 13:00:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 152.4 |
| 31827f04-99c9-3627-8acb-9bab9df3d3d1 | -19.8473 | -57.7835 | 2025-11-30 13:00:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 70.7 |
| 2faf501b-62a1-3cb1-9f00-b711bb55e996 | -17.4761 | -57.1148 | 2025-11-30 13:00:00 | GOES-19 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 79.7 |
| 88faaed5-e633-386d-855b-75463a2ad516 | -19.9335 | -57.4595 | 2025-11-30 13:00:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 102.8 |
| 9fca76ad-8a47-3b14-89cd-795bad1fce12 | -19.9339 | -57.4386 | 2025-11-30 13:00:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 309.6 |
| d2f765f7-3390-3960-978c-c4d9b2d727bb | -19.8675 | -57.7808 | 2025-11-30 13:10:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 65.8 |
| e38300b2-8ee2-39a4-84c6-cf8df47c3cbf | -19.9343 | -57.4177 | 2025-11-30 13:10:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 82.9 |
| e0ae0ad1-6aa3-3c03-b4a3-fe5f65cc180f | -19.8473 | -57.7835 | 2025-11-30 13:10:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 99.6 |
| cfb88326-1a0e-38dc-b89d-d6d515b68e79 | -19.0522 | -57.5148 | 2025-11-30 13:10:00 | GOES-19 | LADÁRIO | MATO GROSSO DO SUL | Brasil | 5005202 | 50 | 33 | nan | nan | nan | Pantanal | 62.4 |
| fe407002-cfad-3da5-a4e2-6b6375838722 | -19.9339 | -57.4386 | 2025-11-30 13:10:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 126.3 |
| 1d7f0998-06ab-31be-9567-ef326cd78095 | -17.4951 | -57.1537 | 2025-11-30 13:20:00 | GOES-19 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 112.0 |
| a65a2311-f926-3b55-a09a-63d109e298d3 | -17.4954 | -57.133 | 2025-11-30 13:20:00 | GOES-19 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 106.5 |
| 687183e3-0852-390a-998b-8f017ec64b3a | -17.5148 | -57.1513 | 2025-11-30 13:20:00 | GOES-19 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 114.8 |
| 5fd0ce08-2bc4-33cf-a10b-4bd453104a3b | -3.3281 | -42.5018 | 2025-11-30 13:20:00 | GOES-19 | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Cerrado | 90.7 |
| 696bc5de-8067-3a74-9ca0-488252d67233 | -19.0633 | -55.8227 | 2025-11-30 13:20:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 61.9 |
| 9b8ec507-476f-3282-9a00-90652514e10f | -19.8473 | -57.7835 | 2025-11-30 13:20:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 80.3 |
| 0e1fdad5-c33e-30f5-8216-2c76a9bd6a7c | -17.4761 | -57.1148 | 2025-11-30 13:20:00 | GOES-19 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 82.1 |
| 46fdbcb3-a1e5-36c9-807d-8e3ded520b04 | -17.5151 | -57.1306 | 2025-11-30 13:20:00 | GOES-19 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 79.5 |
| 17677c4d-2310-3567-afb0-a15bbb63c259 | -19.0522 | -57.5148 | 2025-11-30 13:20:00 | GOES-19 | LADÁRIO | MATO GROSSO DO SUL | Brasil | 5005202 | 50 | 33 | nan | nan | nan | Pantanal | 68.6 |
| 37547022-7885-3273-8bc8-7f38978b2638 | -3.3281 | -42.5018 | 2025-11-30 13:30:00 | GOES-19 | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Cerrado | 110.8 |
| 115fe745-c91a-326c-8664-2e33db0118ba | -19.8675 | -57.7808 | 2025-11-30 13:30:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 82.1 |
| 6a2b148e-a47a-3bc1-85c1-30248a863b2f | -19.9339 | -57.4386 | 2025-11-30 13:30:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 309.5 |
| e1d6812c-cba0-30ca-b114-a38f6228b2c9 | -19.9138 | -57.4414 | 2025-11-30 13:30:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 69.7 |
| d57d05cc-3f43-303d-babf-626c0b2fdef5 | -19.8473 | -57.7835 | 2025-11-30 13:30:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 84.6 |
| 315e6c6f-bbb8-3cbc-bd47-e90277cbea0e | -19.9335 | -57.4595 | 2025-11-30 13:30:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 98.4 |
| b8a10ada-1091-3f4b-a916-3656910b81bf | -4.9658 | -41.2123 | 2025-11-30 13:30:00 | GOES-19 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 83.2 |
| e05a32f2-d543-3034-96af-738a766fdb37 | -19.9343 | -57.4177 | 2025-11-30 13:30:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 167.2 |
| 2c846120-88cb-3c5d-957b-f264efd25921 | -5.5169 | -42.5806 | 2025-11-30 13:30:00 | GOES-19 | MONSENHOR GIL | PIAUÍ | Brasil | 2206407 | 22 | 33 | nan | nan | nan | Caatinga | 99.7 |
| 03728ee3-9e47-38f1-ac7c-5a237fe9b751 | -20.4076 | -57.9577 | 2025-11-30 13:30:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 78.1 |
| 186c7a1c-a01a-3f66-87ce-e1742409d458 | -20.4076 | -57.9577 | 2025-11-30 13:40:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 76.9 |
| 5e2c17ce-6ce8-3c38-9670-d2e64a299a64 | -20.3874 | -57.9605 | 2025-11-30 13:40:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 73.1 |
| c39aed4e-c976-3da1-aa56-93511cd12b4b | -19.8473 | -57.7835 | 2025-11-30 13:40:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 74.6 |
| 37f86582-3dd8-3405-93fd-9b370860c647 | -4.9472 | -41.1895 | 2025-11-30 13:40:00 | GOES-19 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 87.1 |
| 60cb9ba6-a1d8-3dfd-af04-deba9297275c | -4.9658 | -41.2123 | 2025-11-30 13:40:00 | GOES-19 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 84.0 |
| 49616baf-efa0-3ff5-96b9-45dab46b81cc | -3.3281 | -42.5018 | 2025-11-30 13:40:00 | GOES-19 | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Cerrado | 120.1 |
| bb61e77a-ac8b-32a3-84a7-91f62166f707 | -5.4981 | -42.582 | 2025-11-30 13:50:00 | GOES-19 | LAGOA DO PIAUÍ | PIAUÍ | Brasil | 2205581 | 22 | 33 | nan | nan | nan | Caatinga | 111.6 |
| d7cede93-89d3-39db-9fb9-cc71061fccc8 | -3.5958 | -41.4659 | 2025-11-30 13:50:00 | GOES-19 | COCAL DOS ALVES | PIAUÍ | Brasil | 2202729 | 22 | 33 | nan | nan | nan | Caatinga | 90.2 |
| ec410fae-7d44-3af1-aaf5-fa689349be93 | -4.9472 | -41.1895 | 2025-11-30 13:50:00 | GOES-19 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 95.4 |
| 96064c1e-cc09-31a8-9e5c-5975a991b70f | -20.3874 | -57.9605 | 2025-11-30 13:50:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 72.5 |
| 3e783e75-0430-3909-9eb1-d4b30f1f94db | -4.9658 | -41.2123 | 2025-11-30 13:50:00 | GOES-19 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 101.6 |
| 5ab9f849-1fd7-329b-9e79-3ebf4961a825 | -20.4076 | -57.9577 | 2025-11-30 13:50:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 81.9 |
| 841958dd-f024-3145-86f2-20293fcff3be | -4.9474 | -41.1653 | 2025-11-30 13:50:00 | GOES-19 | PORANGA | CEARÁ | Brasil | 2311009 | 23 | 33 | nan | nan | nan | Caatinga | 94.0 |
| 4b5a2e53-f8d9-349d-828e-5962c5864497 | -20.408 | -57.9368 | 2025-11-30 14:00:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 70.6 |
| b53be895-81ce-3e17-934e-a25d8714e410 | -20.3874 | -57.9605 | 2025-11-30 14:00:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 77.1 |
| 56fefd25-7835-304d-8092-5de7e56209a7 | -19.9142 | -57.4204 | 2025-11-30 14:00:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 111.0 |
| 669520e9-e503-3882-a0ec-216fddf978b2 | -5.9236 | -41.2814 | 2025-11-30 14:00:00 | GOES-19 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 88.6 |
| 915acd5f-5f28-3c20-9966-b92d6a0589f2 | -19.9339 | -57.4386 | 2025-11-30 14:00:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 433.7 |
| b8927235-9ae7-35d1-8f80-5a6aa82d580d | -4.9472 | -41.1895 | 2025-11-30 14:00:00 | GOES-19 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 98.1 |
| 096531a5-0168-39d3-b972-d113ea45fd9d | -4.966 | -41.1881 | 2025-11-30 14:00:00 | GOES-19 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 93.3 |
| d9b75e76-888e-3a1d-be8d-166a2fdabc83 | -20.4076 | -57.9577 | 2025-11-30 14:00:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 87.5 |
| 4fe92958-7c73-3f34-8564-b61408aee35a | -19.9343 | -57.4177 | 2025-11-30 14:00:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 178.0 |
| f1715c01-aec3-3938-8007-f2215b3df915 | -19.9138 | -57.4414 | 2025-11-30 14:00:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 145.3 |
| 03478991-f4ec-3a00-b657-52654ed30c3b | -19.9134 | -57.4623 | 2025-11-30 14:00:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 92.3 |
| 3e5448f8-df47-3c9b-b705-fac1c371304b | -4.9472 | -41.1895 | 2025-11-30 14:10:00 | GOES-19 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 102.3 |
| 48d57db9-0590-3171-9b2f-a72db4035c21 | -4.9474 | -41.1653 | 2025-11-30 14:10:00 | GOES-19 | PORANGA | CEARÁ | Brasil | 2311009 | 23 | 33 | nan | nan | nan | Caatinga | 97.9 |
| 7ff5ec8f-8ca7-30b1-9a37-a4f7b4c81220 | -20.4076 | -57.9577 | 2025-11-30 14:10:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 93.1 |
| 5e9fb063-38db-3b88-b7b4-82e1101a64e5 | -4.9476 | -41.1411 | 2025-11-30 14:10:00 | GOES-19 | PORANGA | CEARÁ | Brasil | 2311009 | 23 | 33 | nan | nan | nan | Caatinga | 95.5 |
| b05cfbf0-56be-38d1-a0b2-cd00a127fa2b | -4.966 | -41.1881 | 2025-11-30 14:10:00 | GOES-19 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 96.7 |
| 429e3032-b698-3a70-887f-95163214b7d2 | -20.3874 | -57.9605 | 2025-11-30 14:10:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 78.8 |


