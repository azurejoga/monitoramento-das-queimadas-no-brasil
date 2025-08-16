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

## Dados Diários - Página 75

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 298de154-9b0b-3afe-bcfc-76691541beb2 | -6.5638 | -43.0357 | 2025-08-16 07:00:00 | GOES-19 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 107.0 |
| a251bf23-94e6-3742-853d-02d0b05995d6 | -6.9486 | -59.549 | 2025-08-16 07:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 39.2 |
| be4dbdc8-07e3-34b3-a030-e4a6f082e5e5 | -8.9785 | -60.5349 | 2025-08-16 07:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 66.7 |
| 9cb9a688-3d9b-37d3-b5c9-77785f5eaed4 | -8.9788 | -60.4964 | 2025-08-16 07:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 78.7 |
| 1544cad8-6432-357d-b821-a35d90bd861d | -6.9486 | -59.549 | 2025-08-16 07:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 35.7 |
| 1a936079-f1b8-3047-960d-4f75399d706d | -12.5562 | -46.9357 | 2025-08-16 07:10:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 79.0 |
| 7f69e9e5-370f-3ede-8bbc-b3c8c58edba9 | -8.9785 | -60.5349 | 2025-08-16 07:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 58.1 |
| 31b3f5b0-8f63-3885-a15d-d84c91be1ad6 | -8.9788 | -60.4964 | 2025-08-16 07:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 63.8 |
| 0181f562-52f6-352e-9340-d4bb1b3aaabb | -8.9974 | -60.4955 | 2025-08-16 07:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 74.6 |
| 004152b3-7450-3f24-9513-7245fce5aee3 | -9.1709 | -59.6374 | 2025-08-16 07:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 53.4 |
| 236baabc-0584-357a-8e20-2bf79807ca72 | -12.6135 | -46.9499 | 2025-08-16 07:10:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 68.9 |
| bf3e1c74-0b0e-3379-b858-5e4da35d8a73 | -6.9487 | -59.5297 | 2025-08-16 07:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 40.7 |
| d6981d08-db98-3e24-b843-1bb56571ab6c | -14.9628 | -54.7351 | 2025-08-16 07:10:00 | GOES-19 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 63.3 |
| bd19838f-83a5-3f86-9af5-f9e237cf69b9 | -12.6139 | -46.9273 | 2025-08-16 07:10:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 113.1 |
| 02db5630-e07f-355d-9530-48e59066ca25 | -8.9787 | -60.5156 | 2025-08-16 07:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 61.9 |
| 4fc9afdf-74c4-32e5-98fd-19e4ef42bd7e | -12.5942 | -46.9527 | 2025-08-16 07:10:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 62.0 |
| 8da23cd8-0037-336e-b811-e798bbf5a553 | -12.5558 | -46.9583 | 2025-08-16 07:10:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 167.4 |
| 3aefc820-87d9-3c6e-b652-fd1cce4d9059 | -8.9973 | -60.5147 | 2025-08-16 07:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 85.0 |
| 4043b04d-3933-31be-be2e-ed01fc46f576 | -8.9709 | -61.6842 | 2025-08-16 07:10:00 | GOES-19 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 60.0 |
| bb06df05-ddbe-3082-aa20-bdc8cc6662e5 | -12.5947 | -46.9301 | 2025-08-16 07:10:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 90.0 |
| 5e4ec7c5-456e-3403-af6c-2fa6bf764939 | -8.9971 | -60.5339 | 2025-08-16 07:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 84.3 |
| 40aa47cd-2000-3032-9638-3c1894589e43 | -8.9785 | -60.5349 | 2025-08-16 07:20:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 56.1 |
| 37efa935-c78e-3e1b-879b-af117fd8d68a | -14.9628 | -54.7351 | 2025-08-16 07:20:00 | GOES-19 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 93.9 |
| d1ed7665-e533-3672-abc4-f65842e1f216 | -8.9971 | -60.5339 | 2025-08-16 07:20:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 83.4 |
| 95f7e287-b484-3a96-b64e-6225b996f29c | -8.9974 | -60.4955 | 2025-08-16 07:20:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 68.1 |
| e59c161b-3f74-3a11-b34f-adeb20abb4ac | -8.9787 | -60.5156 | 2025-08-16 07:20:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 60.2 |
| 4d5b1bf6-f50c-3666-8828-6daa7fb57c69 | -12.5562 | -46.9357 | 2025-08-16 07:20:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 79.2 |
| 1f78cee1-731f-3cab-bce8-31024cbfc03d | -12.5947 | -46.9301 | 2025-08-16 07:20:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 78.6 |
| f0f961f2-52c9-3104-b104-b1b9e24c9fd4 | -14.9441 | -54.6959 | 2025-08-16 07:20:00 | GOES-19 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 50.7 |
| 42c39d7d-b782-3c60-9f0f-dc5617a33026 | -14.9822 | -54.7328 | 2025-08-16 07:20:00 | GOES-19 | CAMPO VERDE | MATO GROSSO | Brasil | 5102678 | 51 | 33 | nan | nan | nan | Cerrado | 41.1 |
| bbd632a5-db5b-3218-b76e-45bfb7216bea | -8.9973 | -60.5147 | 2025-08-16 07:20:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 84.0 |
| 52f1d689-e150-3ff9-beaf-03da7d084404 | -12.5365 | -46.9611 | 2025-08-16 07:20:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 62.3 |
| 04dca6d5-c9be-3b46-8d46-0a9cbf1211a0 | -8.9788 | -60.4964 | 2025-08-16 07:20:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 64.5 |
| fa0ffc56-8008-36cd-97b1-6a07ffc7f3c0 | -12.6139 | -46.9273 | 2025-08-16 07:20:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 105.9 |
| 89030ea9-4bc6-3ff0-b5a8-97b8811aa6fb | -8.9709 | -61.6842 | 2025-08-16 07:20:00 | GOES-19 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 67.0 |
| d89a15f8-19f8-37f8-b928-5ae7185a65e0 | -12.6135 | -46.9499 | 2025-08-16 07:20:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 57.5 |
| 39ecdf12-31aa-3f28-965c-817d4de9d012 | -12.5558 | -46.9583 | 2025-08-16 07:20:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 153.7 |
| ede229f1-8baa-3fea-8751-0389fed6fbc0 | -12.5558 | -46.9583 | 2025-08-16 07:30:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 162.9 |
| 8bda3ea2-698c-325b-933f-70ad47a108c0 | -8.9788 | -60.4964 | 2025-08-16 07:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 72.2 |
| a35e178d-282b-3dc8-820e-816b2db31266 | -12.5942 | -46.9527 | 2025-08-16 07:30:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 59.2 |
| b488f5ec-f305-380a-9ddc-058c55ff49c9 | -12.5947 | -46.9301 | 2025-08-16 07:30:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 139.1 |
| 77515a34-b0c7-3dbc-8260-789d67eb6b4a | -12.6135 | -46.9499 | 2025-08-16 07:30:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 58.0 |
| 7ab1fe9f-8003-3f7a-a291-ca2e65d6d552 | -8.9787 | -60.5156 | 2025-08-16 07:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 72.7 |
| 26bad4ce-0d9b-364d-8259-cba23c6e17e7 | -12.5951 | -46.9075 | 2025-08-16 07:30:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 92.6 |
| 50312ab4-123c-35ab-9dfd-64410e76ca56 | -14.9628 | -54.7351 | 2025-08-16 07:30:00 | GOES-19 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 78.4 |
| 59b7efd8-bc4c-3c55-bd4c-89347c3da24e | -8.9971 | -60.5339 | 2025-08-16 07:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 70.4 |
| 5f63c52c-d667-3cd7-a47c-98bb37613dde | -12.5365 | -46.9611 | 2025-08-16 07:30:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 73.1 |
| e49138e3-1e2a-3f56-bed0-b13fd15276a7 | -8.9709 | -61.6842 | 2025-08-16 07:30:00 | GOES-19 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 52.7 |
| 11ba8435-51a9-39aa-827d-c6fbca071cd2 | -8.9974 | -60.4955 | 2025-08-16 07:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 65.3 |
| c8388ee9-7a14-3e7a-b5fb-6f1c5e6b6167 | -8.9973 | -60.5147 | 2025-08-16 07:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 75.3 |
| a275209d-83c6-3d28-a175-fe3248fe87c4 | -9.1709 | -59.6374 | 2025-08-16 07:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 48.7 |
| 19997427-9fdf-3184-b09d-9c754da4ff00 | -12.5562 | -46.9357 | 2025-08-16 07:30:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 89.4 |
| 33618d10-5d5c-3daa-82c1-c1843051edab | -14.9435 | -54.7374 | 2025-08-16 07:30:00 | GOES-19 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 53.4 |
| 80c26670-4cc8-3c6c-9a0a-80be4d15c360 | -12.6139 | -46.9273 | 2025-08-16 07:30:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 226.6 |
| bc3f4ea8-ae69-35bb-a35d-6825bbd819e6 | -12.6143 | -46.9047 | 2025-08-16 07:30:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 197.9 |
| 74f7efb2-dee0-3f83-975c-f12e73d24dcc | -8.9785 | -60.5349 | 2025-08-16 07:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 63.6 |
| c1411171-9e79-31be-9db2-c3ad775bf760 | -8.9973 | -60.5147 | 2025-08-16 07:40:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 76.9 |
| 5641d65e-d8a5-3445-bb16-5c4ed2f7f0f8 | -12.5365 | -46.9611 | 2025-08-16 07:40:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 60.8 |
| 54cedf0f-4ca8-3890-8435-2e392e53e358 | -12.5562 | -46.9357 | 2025-08-16 07:40:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 74.4 |
| 45ccf91a-7ffc-324c-8ff2-27cbf9059fef | -6.9487 | -59.5297 | 2025-08-16 07:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 37.2 |
| 8cd735bc-4b5f-3f9c-86f0-4f8a3606f869 | -8.9974 | -60.4955 | 2025-08-16 07:40:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 70.6 |
| ee999bb3-38fe-31cc-b0ce-6064baff250e | -6.5638 | -43.0357 | 2025-08-16 07:40:00 | GOES-19 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 54.7 |
| bb9f8c8c-7120-302d-8b3a-37d9270f9fab | -8.9785 | -60.5349 | 2025-08-16 07:40:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 55.1 |
| e1b96b68-3974-3e18-942b-f9d46f6c890e | -9.1709 | -59.6374 | 2025-08-16 07:40:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 50.1 |
| df13ac4e-0729-3938-b117-d26ef00a83a3 | -14.9441 | -54.6959 | 2025-08-16 07:40:00 | GOES-19 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 51.2 |
| c606b345-d873-33d8-b5cc-8a40697f9773 | -12.5558 | -46.9583 | 2025-08-16 07:40:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 155.2 |
| b66e69e7-2222-3674-ade7-37561abb7df6 | -8.9709 | -61.6842 | 2025-08-16 07:40:00 | GOES-19 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 50.1 |
| 1b356b2b-4fc3-354e-a506-b46ecd5b1a94 | -8.9971 | -60.5339 | 2025-08-16 07:40:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 75.1 |
| c8db2704-9991-3119-bf1c-e8e45c293b00 | -8.9787 | -60.5156 | 2025-08-16 07:40:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 60.5 |
| eb3cc16c-5087-3c8c-9870-d000a570f0e3 | -14.9628 | -54.7351 | 2025-08-16 07:40:00 | GOES-19 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 57.5 |
| 99a7f54b-4b21-3fde-8711-bfd30e1d568b | -8.9788 | -60.4964 | 2025-08-16 07:40:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 66.0 |
| 9c9bb386-4819-3999-b01d-e481ca623a05 | -12.5942 | -46.9527 | 2025-08-16 07:50:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 60.5 |
| d306c49d-b5ee-3eab-939f-8939fd22e522 | -14.9628 | -54.7351 | 2025-08-16 07:50:00 | GOES-19 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 60.7 |
| a6931d04-17fe-3f32-abcb-aacb5e71fe24 | -6.9487 | -59.5297 | 2025-08-16 07:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 42.4 |
| 2b987baa-e989-392e-b6e7-9034b319d999 | -12.5562 | -46.9357 | 2025-08-16 07:50:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 80.4 |
| 3011b311-86ee-305d-8bf9-baeb82ecf814 | -8.9788 | -60.4964 | 2025-08-16 07:50:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 60.4 |
| 8337add1-8845-34ff-ba30-db9e251093e1 | -12.6143 | -46.9047 | 2025-08-16 07:50:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 99.9 |
| 07d847ca-0594-3703-90ee-cf02862ddfb5 | -9.1709 | -59.6374 | 2025-08-16 07:50:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 55.0 |
| 4421ede5-e23c-30fd-aca4-3014a140b4dd | -8.9709 | -61.6842 | 2025-08-16 07:50:00 | GOES-19 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 61.6 |
| feb24b2b-87c3-3c8c-8b78-ed1eb2eba4b2 | -6.5638 | -43.0357 | 2025-08-16 07:50:00 | GOES-19 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 114.9 |
| 3f6fa40f-6841-3219-aaf2-39f8fc5efcff | -12.6135 | -46.9499 | 2025-08-16 07:50:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 66.2 |
| c779bc11-56df-3680-92ab-c3655c60ecac | -12.6139 | -46.9273 | 2025-08-16 07:50:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 199.1 |
| 78aeec8a-d59f-3d2d-af82-63ff2ab92319 | -12.5558 | -46.9583 | 2025-08-16 07:50:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 161.6 |
| 1ffb3bc1-e68c-3cb8-836d-fb1f3b36e692 | -8.9787 | -60.5156 | 2025-08-16 07:50:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 60.0 |
| c39f0883-f241-3b00-83a2-1e8e784be19c | -12.5947 | -46.9301 | 2025-08-16 07:50:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 132.8 |
| 51e3b7d7-9a15-3d61-9a00-15186c29f6ef | -12.5951 | -46.9075 | 2025-08-16 07:50:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 66.8 |
| 9857ecc1-4fd8-3266-8311-38660d57b6a9 | -8.9974 | -60.4955 | 2025-08-16 07:50:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 65.8 |
| ac626dde-0a13-3cf2-ab87-23a42370daa5 | -8.9785 | -60.5349 | 2025-08-16 07:50:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 55.2 |
| d1ef060c-50e7-3996-9c8f-91dcd34c7aa3 | -8.9973 | -60.5147 | 2025-08-16 07:50:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 78.3 |
| e849a31e-ef5d-31e4-87da-b8966051d896 | -8.9971 | -60.5339 | 2025-08-16 07:50:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 76.2 |
| 682de034-4ff1-3d51-bcef-a425a41e4681 | -6.545 | -43.0373 | 2025-08-16 08:00:00 | GOES-19 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 71.9 |
| 3d2b22c1-9787-3c1e-a21d-47175565807f | -7.5522 | -45.435 | 2025-08-16 08:00:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 59.7 |
| 2520906e-473c-3923-a4c3-0e61afa0d66e | -12.5558 | -46.9583 | 2025-08-16 08:00:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 140.0 |
| 454f3a5c-cfff-3c1d-8d17-30286ab1417d | -7.5525 | -45.4123 | 2025-08-16 08:00:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 78.8 |
| 4c3416e9-f13a-342f-99e9-b711f7c7678f | -12.6139 | -46.9273 | 2025-08-16 08:00:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 167.7 |
| 4843a5c5-1dc5-39b8-96cb-e7d3b400c812 | -12.6135 | -46.9499 | 2025-08-16 08:00:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 67.3 |
| 0dea22c4-a337-3b41-bbf3-0d907ce00006 | -9.1709 | -59.6374 | 2025-08-16 08:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 55.0 |
| 0b7471e3-368f-3869-bd72-b35e8995e98d | -6.9487 | -59.5297 | 2025-08-16 08:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 38.1 |
| f78e5757-f9e7-3bff-8932-d87688b01609 | -12.5947 | -46.9301 | 2025-08-16 08:00:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 129.0 |
| 3d40d873-0bdf-36ba-800e-d36aa7fb2ce2 | -6.5638 | -43.0357 | 2025-08-16 08:00:00 | GOES-19 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 114.4 |


[Clique aqui para ver as próximas entradas](README76.md)
