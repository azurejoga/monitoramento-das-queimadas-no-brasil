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
| 7c5c48ad-e2f8-34db-8c0a-b26d51baee07 | -4.82104 | -48.67182 | 2025-10-24 03:47:00 | NOAA-21 | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 66429a0b-6ce2-3bf2-a77e-6b57bc1f7cb8 | -7.62863 | -41.85643 | 2025-10-24 03:47:00 | NOAA-21 | CAMPINAS DO PIAUÍ | PIAUÍ | Brasil | 2202109 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 429f1589-4447-32aa-b20a-ba735b7503fc | -6.30127 | -41.88481 | 2025-10-24 03:47:00 | NOAA-21 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| dec8c60c-b02b-36a7-8419-3946144b498d | -8.206 | -46.98516 | 2025-10-24 03:47:00 | NOAA-21 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 16.0 |
| 266c36e6-2481-3969-8398-4bb80126126e | -7.55046 | -47.3649 | 2025-10-24 03:47:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 14.1 |
| d75fe3e2-537d-385b-afcc-72af3c96276c | -7.77683 | -45.40276 | 2025-10-24 03:47:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 82049bdd-9e39-3a23-9a1e-29b8201fe4d7 | -7.14266 | -44.11529 | 2025-10-24 03:47:00 | NOAA-21 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 3.1 |
| c7dbe3c3-d0d5-3dd9-959f-8895b6db64e0 | -4.9175 | -47.32436 | 2025-10-24 03:47:00 | NOAA-21 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 3.2 |
| de250a5b-e49a-3eef-ab22-56fac38d9392 | -6.31092 | -41.85355 | 2025-10-24 03:47:00 | NOAA-21 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 3.6 |
| 77e4c090-5f08-3ea6-85df-fce44cc89bb7 | -6.9203 | -44.0188 | 2025-10-24 03:47:00 | NOAA-21 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 8.1 |
| d894feb3-1fab-3fb7-bf82-dd496a853988 | -7.32395 | -45.2837 | 2025-10-24 03:47:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| ea5e5e6c-a27d-369d-98ce-9bb75235e4bd | -6.97817 | -45.2847 | 2025-10-24 03:47:00 | NOAA-21 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| b56aed13-a4f7-347d-8470-a9a209ce9de9 | -6.91566 | -44.01795 | 2025-10-24 03:47:00 | NOAA-21 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 2c064c76-bdfb-3b0e-99c8-8dcb69caaedd | -8.67629 | -36.68747 | 2025-10-24 03:47:00 | NOAA-21 | CAPOEIRAS | PERNAMBUCO | Brasil | 2603801 | 26 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 35c7ff39-0eb9-363a-95f1-9e78ea603f02 | -7.62186 | -41.8482 | 2025-10-24 03:47:00 | NOAA-21 | CAMPINAS DO PIAUÍ | PIAUÍ | Brasil | 2202109 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| bed76989-0059-39dd-bad4-6acf1b14ce43 | -8.05548 | -36.23574 | 2025-10-24 03:47:00 | NOAA-21 | BREJO DA MADRE DE DEUS | PERNAMBUCO | Brasil | 2602605 | 26 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 6f0b95f5-17f3-3032-8220-e0cba1b9ba8f | -2.87454 | -45.25468 | 2025-10-24 03:47:00 | NOAA-21 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 6.8 |
| ecc975b9-8f0d-32af-8d33-9f1cd37975fa | -7.90414 | -43.1428 | 2025-10-24 03:47:00 | NOAA-21 | PAVUSSU | PIAUÍ | Brasil | 2207850 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| a22d56a0-4401-320a-b9c4-f4859bff50cf | -7.62126 | -41.85171 | 2025-10-24 03:47:00 | NOAA-21 | CAMPINAS DO PIAUÍ | PIAUÍ | Brasil | 2202109 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 56abd0b0-3563-3742-b3fd-7e982c0e858b | -4.90811 | -47.65584 | 2025-10-24 03:47:00 | NOAA-21 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 15130c81-969c-3a23-9bcc-03897d0e5cdc | -5.65567 | -45.9581 | 2025-10-24 03:47:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 061bcb8b-a947-3137-8b9d-f1dd28f40749 | -7.78193 | -45.40329 | 2025-10-24 03:47:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 3b0edd61-719d-3f2f-8406-5296e4bf3b34 | -6.11579 | -41.74541 | 2025-10-24 03:47:00 | NOAA-21 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| e4c9f4e6-b97d-32ab-afb6-8fa9035aaf96 | -8.61227 | -44.81437 | 2025-10-24 03:47:00 | NOAA-21 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 7.2 |
| dd5ee58c-8250-339c-8717-79af79b2404d | -6.31374 | -41.86145 | 2025-10-24 03:47:00 | NOAA-21 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 3.2 |
| 82fd7777-47cd-3156-a941-36a6fa36e8fe | -7.85451 | -49.6523 | 2025-10-24 03:47:00 | NOAA-21 | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 86983ecb-73f4-3c15-84a4-245008ed6a40 | -8.32226 | -46.78385 | 2025-10-24 03:47:00 | NOAA-21 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| ba567c29-f0c2-3353-91c8-f034857fc76d | -8.6322 | -40.9642 | 2025-10-24 03:47:00 | NOAA-21 | AFRÂNIO | PERNAMBUCO | Brasil | 2600203 | 26 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 18cdeb05-6be7-3507-9b29-db362e9b2f3b | -6.73113 | -44.15357 | 2025-10-24 03:47:00 | NOAA-21 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| f7106b4b-cd48-322c-8465-f355a4f689b7 | -8.29809 | -42.29873 | 2025-10-24 03:47:00 | NOAA-21 | SÃO JOÃO DO PIAUÍ | PIAUÍ | Brasil | 2210003 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 5e0f32e5-275e-355d-8a69-4186bd22d873 | -8.32771 | -46.78492 | 2025-10-24 03:47:00 | NOAA-21 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| fa557d37-3532-3c18-96e8-23b55b292edc | -7.55621 | -47.36592 | 2025-10-24 03:47:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 13.7 |
| ff3dac66-8ac4-38a1-bbdc-ba2bf09e98dc | -2.26133 | -47.85244 | 2025-10-24 03:47:00 | NOAA-21 | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 795cbf0e-f8ad-3523-802e-c4144ba63262 | -5.81511 | -46.21557 | 2025-10-24 03:47:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 21610e3f-1f7c-3dc5-a955-be9107666d9b | -6.30313 | -41.87474 | 2025-10-24 03:47:00 | NOAA-21 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 7519ffb2-28fd-33de-87e1-964a779fcb3b | -7.66092 | -47.41509 | 2025-10-24 03:47:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 92b7bd39-d630-359f-b7ab-f9fa6b47c43b | -6.9189 | -44.01735 | 2025-10-24 03:47:00 | NOAA-21 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 20.8 |
| a2505b99-7ac9-37f1-87be-f057b964427c | -7.97603 | -47.2398 | 2025-10-24 03:47:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| ebe3ee3a-f49f-387a-a2cd-9b780c508014 | -6.30245 | -41.87757 | 2025-10-24 03:47:00 | NOAA-21 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 4.6 |
| dea5c782-d152-3bfc-ba55-832abded6fc0 | -6.88421 | -43.6149 | 2025-10-24 03:47:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 0ae93fe7-7769-30be-9c6c-557fba1b6e3d | -5.76112 | -46.68636 | 2025-10-24 03:47:00 | NOAA-21 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| b85e988d-2533-36f6-911c-7b9536440d41 | -7.68463 | -42.2384 | 2025-10-24 03:47:00 | NOAA-21 | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| e960b35a-933d-3d18-9584-67020e4ccc3d | -7.29715 | -46.94728 | 2025-10-24 03:47:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| c52ed700-fd61-3fd5-b2da-d779d9bd5c9b | -7.82801 | -45.37748 | 2025-10-24 03:47:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 7ba39d5f-4a07-3f5d-b600-d17a1899359e | -6.73582 | -44.15448 | 2025-10-24 03:47:00 | NOAA-21 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 5af194b4-d204-3b6e-b2ac-876912ec1eab | -7.05823 | -43.1675 | 2025-10-24 03:47:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 4b43d055-efdc-30ef-9045-cebeed79b710 | -7.73507 | -47.0093 | 2025-10-24 03:47:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 6a90a032-dbcd-3710-a5bf-be1c5220da2e | -7.14649 | -44.12088 | 2025-10-24 03:47:00 | NOAA-21 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 3fac1004-84e5-313c-bde0-f905230c0c41 | -6.83784 | -41.55318 | 2025-10-24 03:47:00 | NOAA-21 | SÃO JOSÉ DO PIAUÍ | PIAUÍ | Brasil | 2210201 | 22 | 33 | nan | nan | nan | Caatinga | 4.2 |
| 7dec3c5b-7ac4-3bca-8282-4e8ce16e448a | -8.65112 | -44.79193 | 2025-10-24 03:47:00 | NOAA-21 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 3b21ec5c-407e-36a6-aa1e-69cbe231bcb1 | -7.29572 | -46.95514 | 2025-10-24 03:47:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 58aecdda-097c-3594-8201-875e33c40dd6 | -6.44083 | -45.66822 | 2025-10-24 03:47:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 22383e24-b9fb-3969-8086-ff4a1af77334 | -8.17208 | -47.76519 | 2025-10-24 03:47:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 585e13ae-6504-3e40-a93c-01473b7e015f | -8.04166 | -39.87205 | 2025-10-24 03:47:00 | NOAA-21 | OURICURI | PERNAMBUCO | Brasil | 2609907 | 26 | 33 | nan | nan | nan | Caatinga | 1.8 |
| f89311fb-7cf2-3a96-ace5-da3a603e9832 | -6.1303 | -41.73324 | 2025-10-24 03:47:00 | NOAA-21 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 3.3 |
| a9c3c74d-00d6-3f87-bc3f-dc07c7d4ccaf | -8.32673 | -46.25352 | 2025-10-24 03:47:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 7.1 |
| cd7e5366-e88d-3c19-ba68-3f7cbaa736fe | -7.64066 | -42.29873 | 2025-10-24 03:47:00 | NOAA-21 | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 999682fe-8b47-3760-a3c8-1faf78436114 | -7.54898 | -47.37293 | 2025-10-24 03:47:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 860eaa74-e013-3643-be94-6ee0b9270820 | -7.77737 | -45.39976 | 2025-10-24 03:47:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 3ef1479e-1633-3736-8e25-562128753f09 | -6.37129 | -41.74183 | 2025-10-24 03:47:00 | NOAA-21 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 61e794b7-4273-32ff-bd4b-37e5f617e46b | -6.78184 | -38.57182 | 2025-10-24 03:47:00 | NOAA-21 | SANTA HELENA | PARAÍBA | Brasil | 2513307 | 25 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 6fbd5827-265b-3bad-9ceb-836e6e852d30 | -8.65021 | -44.79699 | 2025-10-24 03:47:00 | NOAA-21 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 4.5 |
| c87a6f1c-916a-3827-8c6c-b893eaa73667 | -8.1144 | -47.04569 | 2025-10-24 03:47:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| dfc0ab19-732d-32d9-9ce2-cb0adcf5aa49 | -6.29796 | -40.87325 | 2025-10-24 03:47:00 | NOAA-21 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 5.0 |
| e2bc4de8-3473-32ed-a035-d55f0f11d7e2 | -8.17776 | -47.7631 | 2025-10-24 03:47:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 7348ac84-85bf-3ea4-811a-ecd44680f3f4 | -6.91297 | -41.53626 | 2025-10-24 03:47:00 | NOAA-21 | SANTANA DO PIAUÍ | PIAUÍ | Brasil | 2209351 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| e900fb0a-7594-313e-b2de-bb9a599c677f | -7.64165 | -42.17103 | 2025-10-24 03:47:00 | NOAA-21 | SIMPLÍCIO MENDES | PIAUÍ | Brasil | 2210805 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 1634fe6a-72f5-37b6-8f6b-35ec753c379d | -6.24152 | -41.76779 | 2025-10-24 03:47:00 | NOAA-21 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| a5eec9f4-2b28-3f7b-9af5-c32c7432b9dc | -8.19546 | -44.43775 | 2025-10-24 03:47:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 54bd2ab4-400b-3961-9a18-987499aecec4 | -6.91212 | -41.54128 | 2025-10-24 03:47:00 | NOAA-21 | PICOS | PIAUÍ | Brasil | 2208007 | 22 | 33 | nan | nan | nan | Caatinga | 5.0 |
| 519cd82c-84ca-3b60-b167-7ecb66ebe529 | -7.13839 | -45.04625 | 2025-10-24 03:47:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 2bb87243-15ce-30c9-9684-477f7776a469 | -7.83558 | -45.59079 | 2025-10-24 03:47:00 | NOAA-21 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| ab24ca61-4c5b-3390-9e5d-cfa2fb2013e6 | -7.68807 | -42.2428 | 2025-10-24 03:47:00 | NOAA-21 | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| e16c9f03-0c98-3254-89cd-8d28b9c27e26 | -6.27881 | -47.01308 | 2025-10-24 03:47:00 | NOAA-21 | SÃO JOÃO DO PARAÍSO | MARANHÃO | Brasil | 2111052 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| bdec16cb-c25e-3a23-ae5b-ea968d79eae1 | -6.4414 | -45.66496 | 2025-10-24 03:47:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| ac4493f4-c23a-34f9-98b6-71931a30f910 | -5.02188 | -47.15084 | 2025-10-24 03:47:00 | NOAA-21 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 75a7ef16-9f49-3e95-9079-ce724492641e | -6.92354 | -44.0182 | 2025-10-24 03:47:00 | NOAA-21 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 8c0d4720-cd48-3f2d-acaf-41f3bd29b70b | -6.11051 | -48.10393 | 2025-10-24 03:47:00 | NOAA-21 | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 89e9fa95-92a8-30a4-b745-e27528345f29 | -6.8928 | -38.27987 | 2025-10-24 03:47:00 | NOAA-21 | SOUSA | PARAÍBA | Brasil | 2516201 | 25 | 33 | nan | nan | nan | Caatinga | 1.6 |
| a2f0a98b-f265-3e99-885d-2257d6e2b068 | -6.02318 | -48.90931 | 2025-10-24 03:47:00 | NOAA-21 | SÃO GERALDO DO ARAGUAIA | PARÁ | Brasil | 1507458 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 6e7bf7be-be13-316f-926a-f70fed785c66 | -7.37178 | -41.75858 | 2025-10-24 03:47:00 | NOAA-21 | SANTA CRUZ DO PIAUÍ | PIAUÍ | Brasil | 2209104 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 33c16525-3f43-3c2c-bc83-b778fdc4fe0b | -2.26862 | -47.84831 | 2025-10-24 03:47:00 | NOAA-21 | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| b121923c-dfd7-3fc1-a3a3-5c4f22b8c4ba | -7.69214 | -42.24354 | 2025-10-24 03:47:00 | NOAA-21 | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 3455707f-35b0-3efa-85b0-5aad8e7e8b0e | -5.65688 | -45.95116 | 2025-10-24 03:47:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 6eb4906d-90d2-36aa-8951-373f7c269fbf | -8.35124 | -46.17741 | 2025-10-24 03:47:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| a0fbde3b-61c4-3d78-9bda-c73c9aa3188d | -6.77734 | -45.46947 | 2025-10-24 03:47:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 1d36a60f-f09a-3d1f-82df-68425538e7df | -6.84266 | -41.54865 | 2025-10-24 03:47:00 | NOAA-21 | SÃO JOSÉ DO PIAUÍ | PIAUÍ | Brasil | 2210201 | 22 | 33 | nan | nan | nan | Caatinga | 5.6 |
| 8b1c3d49-05c0-3b74-b046-49e96c9e7e8b | -4.82006 | -48.67752 | 2025-10-24 03:47:00 | NOAA-21 | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 10.4 |
| 188e5f42-1831-3a85-92c6-fb62e7462b25 | -7.66165 | -47.41107 | 2025-10-24 03:47:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 92edb55d-e00d-3ad8-a625-78813135236c | -5.59506 | -47.31881 | 2025-10-24 03:47:00 | NOAA-21 | DAVINÓPOLIS | MARANHÃO | Brasil | 2103752 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 74ee205b-6f02-3956-8045-7dfc5617b163 | -8.03458 | -39.87092 | 2025-10-24 03:47:00 | NOAA-21 | OURICURI | PERNAMBUCO | Brasil | 2609907 | 26 | 33 | nan | nan | nan | Caatinga | 3.8 |
| 54daa6bc-693b-3f23-bf36-f8a16bdcdab8 | -8.61702 | -44.81531 | 2025-10-24 03:47:00 | NOAA-21 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 7412b62b-21da-3bfa-aae0-5eab823e98bc | -8.03877 | -39.86747 | 2025-10-24 03:47:00 | NOAA-21 | OURICURI | PERNAMBUCO | Brasil | 2609907 | 26 | 33 | nan | nan | nan | Caatinga | 1.8 |
| b06f4521-a779-3b1f-b4f8-d50e70bf4c9c | -6.30189 | -41.88198 | 2025-10-24 03:47:00 | NOAA-21 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 9658c59e-3db1-32bf-8b5d-fb2783477d81 | -5.6551 | -46.57642 | 2025-10-24 03:47:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 3a295601-2b41-3a8b-a30c-2f1978541844 | -7.07387 | -41.66153 | 2025-10-24 03:47:00 | NOAA-21 | PAQUETÁ | PIAUÍ | Brasil | 2207553 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 0e977fa5-1173-3487-a1dd-b59734e667ec | -5.75546 | -46.68531 | 2025-10-24 03:47:00 | NOAA-21 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 02a6b406-9784-3984-8cc4-e25d8b4b2b50 | -7.78702 | -45.40385 | 2025-10-24 03:47:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 61c774af-4fd0-34fb-a7e0-f2c19dba1ea4 | -7.6321 | -42.20321 | 2025-10-24 03:47:00 | NOAA-21 | SIMPLÍCIO MENDES | PIAUÍ | Brasil | 2210805 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 3faa1918-cb28-3da2-a276-82fc4d5cdf06 | -6.30658 | -41.87903 | 2025-10-24 03:47:00 | NOAA-21 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 8.5 |


[Clique aqui para ver as próximas entradas](README5.md)
