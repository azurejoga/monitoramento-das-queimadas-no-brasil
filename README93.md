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

## Dados Diários - Página 93

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 044574be-a546-361c-b949-2ce5e76ed1d8 | -18.83543 | -54.5037 | 2024-09-28 05:12:00 | NOAA-20 | SÃO GABRIEL DO OESTE | MATO GROSSO DO SUL | Brasil | 5007695 | 50 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 0955f404-767d-3c5f-8c79-68139fe65404 | -18.83495 | -54.50743 | 2024-09-28 05:12:00 | NOAA-20 | SÃO GABRIEL DO OESTE | MATO GROSSO DO SUL | Brasil | 5007695 | 50 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 9562f154-fa6f-365f-a429-66c1c8367a4b | -18.83081 | -54.5069 | 2024-09-28 05:12:00 | NOAA-20 | SÃO GABRIEL DO OESTE | MATO GROSSO DO SUL | Brasil | 5007695 | 50 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 9ddcf8f6-7d1b-3da1-9a04-d57b36b2f3b9 | -18.83034 | -54.51061 | 2024-09-28 05:12:00 | NOAA-20 | SÃO GABRIEL DO OESTE | MATO GROSSO DO SUL | Brasil | 5007695 | 50 | 33 | nan | nan | nan | Cerrado | 1.9 |
| d5057ae7-8d82-39ee-a090-94b6930dbec0 | -21.55566 | -55.82101 | 2024-09-28 05:12:00 | NOAA-20 | GUIA LOPES DA LAGUNA | MATO GROSSO DO SUL | Brasil | 5004106 | 50 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 5b5f8b9c-a7ed-3bbd-8eac-ed9ca9c03407 | -16.64723 | -55.22342 | 2024-09-28 05:12:00 | NOAA-20 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 1.3 |
| 5e332fa5-eabf-357b-bb4e-263fb36a6139 | -16.59076 | -55.9725 | 2024-09-28 05:12:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |
| 5f08356c-f4e0-36ac-9ada-e789a5e5c86f | -16.59014 | -55.977 | 2024-09-28 05:12:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.7 |
| f62c1ca2-0e98-3a80-aae6-2c3ecaf1cb68 | -16.58771 | -55.96745 | 2024-09-28 05:12:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |
| e3f5fbfb-857f-3466-9908-668a3afbce36 | -16.58403 | -55.9669 | 2024-09-28 05:12:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 0.8 |
| 4eadaaa6-0cda-3811-b1be-8ab5d40176ff | -16.58035 | -55.96635 | 2024-09-28 05:12:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 0.8 |
| 2d9b3541-3aec-3202-8fda-c26a589d74c8 | -16.57236 | -55.96975 | 2024-09-28 05:12:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.3 |
| 106aafda-5cf4-335d-a6e6-7a2a044b345c | -16.57111 | -55.97873 | 2024-09-28 05:12:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.2 |
| 3f8ecc53-f37d-320e-b5f2-ae9250da26ba | -16.55573 | -56.00842 | 2024-09-28 05:12:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |
| 2fecf899-f524-373e-9a3f-1c909b6d1347 | -16.53978 | -56.04245 | 2024-09-28 05:12:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.7 |
| f05f9c46-8c34-3f7b-8553-afacdc1af4ff | -16.53611 | -56.0419 | 2024-09-28 05:12:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 0.6 |
| 35698708-275a-36c6-a793-c811484ce58a | -17.01259 | -56.10056 | 2024-09-28 05:12:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.8 |
| eb5d41d4-1f4d-3f52-baef-d610197931ff | -17.00891 | -56.10001 | 2024-09-28 05:12:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.8 |
| 7854f53b-a10b-3cc3-9bf4-9141d199dc61 | -17.00524 | -56.09946 | 2024-09-28 05:12:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.7 |
| 01643a3d-fe68-3c39-8e80-66b7145acf82 | -17.00219 | -56.09443 | 2024-09-28 05:12:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.7 |
| a1758c98-1d56-3f27-b96f-aa83b7249365 | -17.00157 | -56.09891 | 2024-09-28 05:12:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.7 |
| 9f5b20af-d597-3513-97c6-5dd56fd755a1 | -16.99852 | -56.09388 | 2024-09-28 05:12:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.9 |
| 47347e08-23e0-39c1-80cc-9513835e5905 | -16.99484 | -56.09332 | 2024-09-28 05:12:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.9 |
| b15a14dc-9a67-380a-b1a8-b50dfb031c18 | -16.99117 | -56.09277 | 2024-09-28 05:12:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| 55159713-168e-3f39-b59d-bcaf1a694a59 | -16.98749 | -56.09222 | 2024-09-28 05:12:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| f5f75ade-bcb5-3d89-b1fc-03f377b0ec8b | -16.74933 | -55.82713 | 2024-09-28 05:12:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 7.8 |
| 2de171a8-8b8e-37ca-ba3b-7c5d54fd2792 | -16.74869 | -55.83171 | 2024-09-28 05:12:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 4.4 |
| 95207bca-5bd8-3c0f-985a-3a146c98c6ae | -16.74562 | -55.82658 | 2024-09-28 05:12:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 7.8 |
| e4f4be4e-bacf-3a6a-b8e4-154ec3739df3 | -16.74497 | -55.83116 | 2024-09-28 05:12:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 4.4 |
| 890c8e2f-b0db-35fd-892e-11ed6cdcfb9a | -16.7419 | -55.82603 | 2024-09-28 05:12:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 7.9 |
| 10ecbcf0-017e-391c-9f08-70399fb94a9d | -16.74126 | -55.83061 | 2024-09-28 05:12:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.7 |
| f981f8c4-1e54-37a2-95f0-8e0130f10177 | -16.73818 | -55.82549 | 2024-09-28 05:12:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 7.9 |
| bfadf0e2-b7ca-36b2-b60e-fa3e7742f87d | -16.73373 | -55.55362 | 2024-09-28 05:12:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.5 |
| 3ceb090f-53c7-3922-b15d-fc0bf23c9354 | -16.72267 | -55.82788 | 2024-09-28 05:12:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.4 |
| d7377738-5559-3ad3-a566-0703c19ad733 | -16.71768 | -55.83649 | 2024-09-28 05:12:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 3.0 |
| 22371dce-e3cd-3d3e-bb70-856b31679953 | -16.71492 | -55.91055 | 2024-09-28 05:12:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 3.7 |
| efcff967-333e-3a31-a370-df9a163243cf | -16.71461 | -55.83136 | 2024-09-28 05:12:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.9 |
| b1776fcd-526c-3641-8280-f50bc3fe1e63 | -16.71397 | -55.83594 | 2024-09-28 05:12:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 3.0 |
| 37114bac-58fe-32e6-a8fe-c95b8faef7cb | -16.71196 | -55.8776 | 2024-09-28 05:12:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.9 |
| 5984456c-9f7b-3793-aa46-47de3c55111c | -17.1178 | -56.17363 | 2024-09-28 05:12:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.5 |
| 3554c78a-3852-3ff3-b68c-3129841b82b0 | -17.11717 | -56.1781 | 2024-09-28 05:12:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.5 |
| 95c6c169-9fc0-3aea-849b-56a5e1496e66 | -17.11654 | -56.18256 | 2024-09-28 05:12:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 4.5 |
| ce1a9b24-21a9-3c44-b63d-6d10241d13ee | -17.11591 | -56.18702 | 2024-09-28 05:12:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 4.5 |
| 891a1191-f970-3f53-8f12-b496780fdacd | -17.11413 | -56.17308 | 2024-09-28 05:12:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.5 |
| bfd54c24-a404-3416-b9d2-79f11d426bda | -17.1135 | -56.17755 | 2024-09-28 05:12:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.5 |
| aee53fc0-8332-31c0-b68a-ad5361acca93 | -17.11288 | -56.182 | 2024-09-28 05:12:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 4.5 |
| a2fb2f68-adc5-361e-b0dd-2c51136ac4e5 | -17.11225 | -56.18646 | 2024-09-28 05:12:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 4.5 |
| f0f15f56-f653-3ecc-a3a6-c6d02d447978 | -17.11047 | -56.17253 | 2024-09-28 05:12:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.1 |
| 29fa2cdf-9841-3c79-8c36-f187111b6071 | -17.10618 | -56.17645 | 2024-09-28 05:12:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.1 |
| f761ab57-5eb5-31a1-83bd-af5228942289 | -17.10555 | -56.1809 | 2024-09-28 05:12:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.1 |
| 2dc79312-affa-31f8-946b-3687a776dcc3 | -17.10251 | -56.17589 | 2024-09-28 05:12:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| a6fa6100-5152-3cce-a2a0-71462ed21e21 | -17.08729 | -56.15081 | 2024-09-28 05:12:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.3 |
| 0c7a3466-68ea-31b3-b84c-c906d6587c63 | -17.03311 | -56.16751 | 2024-09-28 05:12:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.4 |
| 6805ea46-b092-3228-bb27-0c14c55132da | -17.02945 | -56.16696 | 2024-09-28 05:12:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.4 |
| 173e21be-1801-3488-96db-245482aeb74b | -17.02579 | -56.16641 | 2024-09-28 05:12:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |
| 968dbaf5-81cd-3698-ba6d-bbb87172ddc1 | -17.02402 | -56.15249 | 2024-09-28 05:12:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.1 |
| 59e00d9d-dcef-3013-98b9-969aa1082cc3 | -17.02338 | -56.15695 | 2024-09-28 05:12:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.1 |
| 051eac36-6b09-3cf2-a1c5-a25f9c909b0d | -17.02212 | -56.16586 | 2024-09-28 05:12:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |
| f5fdd2cb-b512-35d0-a239-155a30639380 | -17.0215 | -56.1703 | 2024-09-28 05:12:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.0 |
| 2f3ed067-aa12-33e1-824f-615449cf81bd | -17.02035 | -56.15194 | 2024-09-28 05:12:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |
| c262851d-3be6-3ff9-a33e-6ccbe22e9d45 | -17.01972 | -56.1564 | 2024-09-28 05:12:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |
| 56b1cbda-384d-3a62-a211-bb011ea6817d | -17.01846 | -56.16531 | 2024-09-28 05:12:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.7 |
| b815d073-4e97-3b70-8c71-0cd927f1731b | -17.01784 | -56.16976 | 2024-09-28 05:12:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 12.9 |
| e48a7d00-6038-3cb4-8daa-aaae7effc9c2 | -17.01606 | -56.15585 | 2024-09-28 05:12:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |
| f07e8589-15d4-38ef-8e68-797f03e8b048 | -17.0148 | -56.16476 | 2024-09-28 05:12:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.7 |
| e936483c-6868-36c0-b16e-3140b4d7fe5f | -17.01417 | -56.16922 | 2024-09-28 05:12:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 12.9 |
| 112289f7-f53a-3e3c-a505-44f65a10bd38 | -17.01354 | -56.17366 | 2024-09-28 05:12:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 12.9 |
| 60b95826-2bb2-33f9-b21a-4d8a6b231ece | -17.01302 | -56.15083 | 2024-09-28 05:12:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.7 |
| e5bd2f84-6a68-3d6b-b929-12cad4a5f649 | -17.01239 | -56.1553 | 2024-09-28 05:12:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.7 |
| f68926d6-9d7f-3369-96c6-d83af6ecc074 | -17.01114 | -56.16421 | 2024-09-28 05:12:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.7 |
| 5d0772ae-a4c8-34bd-8567-b378c427dc07 | -17.01051 | -56.16867 | 2024-09-28 05:12:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 4.1 |
| f0cc7373-460d-3988-83ca-b6589189e87e | -17.00873 | -56.15474 | 2024-09-28 05:12:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.7 |
| cb9bc421-70e3-32c3-afb5-75a5dbb44851 | -17.00801 | -56.18644 | 2024-09-28 05:12:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.7 |
| 7bc5da6d-e12e-3312-9609-17c02d46588b | -17.00685 | -56.16812 | 2024-09-28 05:12:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 4.1 |
| 3bcaea30-3d0e-3b5d-b340-e9ae826070e5 | -17.00506 | -56.15419 | 2024-09-28 05:12:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |
| c004928a-625d-3d34-a40a-8f58466f7e75 | -17.00381 | -56.16312 | 2024-09-28 05:12:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 6.8 |
| 01b40b49-7503-3763-9274-8e563df570e8 | -17.00318 | -56.16757 | 2024-09-28 05:12:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 4.4 |
| 8bf89448-d1c0-324b-b38c-b31f1480e971 | -17.0014 | -56.15364 | 2024-09-28 05:12:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |
| d6c5f743-4b19-3e38-970a-d62916612669 | -17.00015 | -56.16257 | 2024-09-28 05:12:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 6.8 |
| 530b1a0e-5f71-30c6-9aa5-2a83e787a478 | -16.99953 | -56.16702 | 2024-09-28 05:12:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 4.4 |
| 8284c2ab-390b-3ba7-b71f-7cca2c8583e5 | -16.99774 | -56.1531 | 2024-09-28 05:12:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 3.0 |
| 204d4999-8edc-3df5-9a67-5dd47fa6bedb | -16.99648 | -56.16203 | 2024-09-28 05:12:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 6.5 |
| d9d6d9c9-1c7a-39df-a383-1a0b221ba9f5 | -16.99407 | -56.15255 | 2024-09-28 05:12:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 3.0 |
| 49c5ba4d-e48b-3c52-9cfd-a52cf07cc957 | -16.99345 | -56.15701 | 2024-09-28 05:12:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 6.5 |
| 95eb15f6-5fe5-3e06-874c-f5a1cee9fa3f | -16.99041 | -56.152 | 2024-09-28 05:12:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.8 |
| f9c1cd61-d073-38b0-9ae3-6c234e568fbb | -16.98978 | -56.15646 | 2024-09-28 05:12:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.2 |
| 7af47283-fdf4-36e1-a2ff-52d649999aa5 | -17.08853 | -56.14185 | 2024-09-28 05:12:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 0.8 |
| c407a9bc-dda4-3b5c-abec-6cf04da8cb27 | -17.08424 | -56.14578 | 2024-09-28 05:12:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.8 |
| 4bc68b94-8a9c-3e3f-a330-19d1a4bb28fc | -17.08057 | -56.14523 | 2024-09-28 05:12:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.8 |
| f3861b16-3976-35d5-9360-ead41f6389e9 | -17.0769 | -56.14468 | 2024-09-28 05:12:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.0 |
| a206d47b-cccb-3a1f-aa61-706322bf9eee | -17.06957 | -56.14357 | 2024-09-28 05:12:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.5 |
| 59e454c7-f0b5-305c-9e1c-4ed4516932fb | -17.06651 | -56.13855 | 2024-09-28 05:12:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.5 |
| 176aa79d-c894-3bec-ad3b-864ddde62390 | -17.06284 | -56.138 | 2024-09-28 05:12:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 5.8 |
| 4017f465-20d7-3427-a1e7-548558562448 | -17.0604 | -56.12847 | 2024-09-28 05:12:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 3.3 |
| 3c806ff9-340a-363e-8d7d-21f1cc5c761b | -17.05979 | -56.13297 | 2024-09-28 05:12:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 3.3 |
| fcc4da65-17a0-3628-b659-782dd946bdf2 | -17.05917 | -56.13744 | 2024-09-28 05:12:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 5.8 |
| 5fc02b77-efb6-3766-8328-1ebc0dc83970 | -17.05612 | -56.13241 | 2024-09-28 05:12:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 3.1 |
| 366e9f2f-0aab-3ced-9bbb-6c3ffab9cccb | -17.0555 | -56.13689 | 2024-09-28 05:12:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.5 |
| 840b5306-7e99-3373-84e6-855e07f74ba2 | -17.05367 | -56.12289 | 2024-09-28 05:12:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.2 |
| eec38f0d-85dd-373c-8a90-d54d412c615c | -17.05244 | -56.13185 | 2024-09-28 05:12:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 3.1 |


[Clique aqui para ver as próximas entradas](README94.md)
