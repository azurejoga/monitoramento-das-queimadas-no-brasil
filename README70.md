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

## Dados Diários - Página 70

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 080efe0f-fcae-322d-ab88-ad48f6c55e99 | -3.12668 | -50.60183 | 2024-10-26 04:42:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 08132afe-9843-3683-b593-4b73c28d09b7 | -3.12613 | -50.60526 | 2024-10-26 04:42:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 511055ed-5789-33ab-a47e-a082e97a8dc8 | -3.12559 | -50.6087 | 2024-10-26 04:42:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| be0f1302-55f4-311c-baa2-6566275e0cdc | -3.12283 | -50.60475 | 2024-10-26 04:42:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 830f6d6a-c8a4-3798-b7ef-412d59cd44c6 | -3.12007 | -50.6008 | 2024-10-26 04:42:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| a9a53ca2-07ad-3456-ab38-3b7230088266 | -3.09759 | -51.34325 | 2024-10-26 04:42:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 842c08cd-1fbb-34fb-b4ff-c65c11e37344 | -3.09703 | -51.34677 | 2024-10-26 04:42:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 04212e37-a3d2-315e-8b95-8dee98bcd21d | -3.09647 | -51.35028 | 2024-10-26 04:42:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 11e6fcd9-c0ff-3f53-9460-a06ec66206c4 | -3.09425 | -51.34273 | 2024-10-26 04:42:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 478bfa04-365e-3fba-856f-2586cfff1c09 | -3.09369 | -51.34624 | 2024-10-26 04:42:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| c84a0b13-603b-30e0-b178-26943bb9808b | -3.09036 | -51.34572 | 2024-10-26 04:42:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 33122e84-a4c2-3364-aba9-b51c4404009d | -3.08374 | -51.26215 | 2024-10-26 04:42:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4dbc46dc-17f7-3408-97a1-e75e6a0d0ef9 | -3.05041 | -51.21392 | 2024-10-26 04:42:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| edcaad65-ebfa-3ab3-9dd8-7d1df714d1a5 | -3.51551 | -51.0232 | 2024-10-26 04:42:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 6cd0b4a6-0de4-345e-b472-62fc37600e1b | -3.51274 | -51.01922 | 2024-10-26 04:42:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 0c7fdc38-2f01-397a-9b43-4ef7845a04fe | -3.50942 | -51.0187 | 2024-10-26 04:42:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 8f054a6c-3baa-3713-b56d-78408f86bc67 | -3.38555 | -50.96351 | 2024-10-26 04:42:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 27b8e8ac-6e99-3e3a-a7f8-40983c5f5360 | -3.385 | -50.96696 | 2024-10-26 04:42:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 4c5057a4-c085-37fe-8642-80d8a2505ba3 | -3.33654 | -50.82196 | 2024-10-26 04:42:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 15ac6812-8129-3e98-bb9c-8f1c69b92142 | -3.33378 | -50.818 | 2024-10-26 04:42:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| b6a4da6b-5846-3f10-9365-abb22c276eed | -3.2656 | -50.77518 | 2024-10-26 04:42:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 5d23434b-2097-3b53-9eec-fbc39874910c | -3.26506 | -50.77863 | 2024-10-26 04:42:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ddd7ad43-9fd6-3de8-974b-1f045309bec3 | -3.1289 | -50.60922 | 2024-10-26 04:42:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| d7cae262-c396-38f3-9f52-27e982d3715e | -3.12337 | -50.60131 | 2024-10-26 04:42:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 40fd2387-e02c-3392-8ed5-32a976bf09f5 | -3.11953 | -50.60423 | 2024-10-26 04:42:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 8a3d2d9d-9ce3-3a56-b576-304dea4b2a2e | -3.11622 | -50.60372 | 2024-10-26 04:42:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| f493fbc5-2090-331f-abe3-82aa66993a15 | -2.98179 | -51.06715 | 2024-10-26 04:42:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 39d121d8-aea3-31a3-b505-4d2fc67e173a | -3.51219 | -51.02269 | 2024-10-26 04:42:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 002f0903-f83a-30e5-9c87-37876dc7a92f | -3.38556 | -51.67052 | 2024-10-26 04:42:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3f748c8a-e694-3c9d-82da-5672e8b90d02 | -3.33985 | -50.82248 | 2024-10-26 04:42:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| bb51d112-f39d-30c6-8ca9-c6a9febb7888 | -3.33432 | -50.81456 | 2024-10-26 04:42:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 579fba84-b37c-3b31-9cbf-6e21d618e8cf | -3.33324 | -50.82145 | 2024-10-26 04:42:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 5105a1d8-78a8-398e-9906-2220536ca6fc | -3.27627 | -51.07477 | 2024-10-26 04:42:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 69672e40-0ed2-39a6-8d8b-374ff4cf6dc7 | -3.27295 | -51.07426 | 2024-10-26 04:42:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 92e677b4-beaa-33a7-b57b-d697d3f2fe0a | -3.26229 | -50.77467 | 2024-10-26 04:42:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 4bad1359-88e4-3cca-a9b2-219aea6b1921 | -2.89892 | -50.73154 | 2024-10-26 04:42:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ef53ebee-142e-3cef-9aa5-d674b896883e | -2.89837 | -50.73499 | 2024-10-26 04:42:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b1a51a51-c360-308b-8388-378652284e10 | -2.89783 | -50.73844 | 2024-10-26 04:42:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 41656203-6299-3035-aeb8-e8fa1a7644b0 | -2.55843 | -50.69234 | 2024-10-26 04:42:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 27c8d4d1-6745-3e03-a315-e18c68963b00 | -2.87817 | -51.31227 | 2024-10-26 04:42:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 65ac8f3e-d42a-3332-ad88-ccac81e66863 | -2.87558 | -51.31194 | 2024-10-26 04:42:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 9eff5717-2ddd-3c7f-b34d-f66420e5842f | -2.8522 | -51.28669 | 2024-10-26 04:42:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 54c31d0c-bc44-3cff-a307-8495287a2b66 | -2.85165 | -51.29019 | 2024-10-26 04:42:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 892d8288-bb61-396e-a14d-d58f56723649 | -2.84887 | -51.28617 | 2024-10-26 04:42:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 81e52498-a755-3cf1-b527-d5cc68a7ff66 | -2.83982 | -51.81285 | 2024-10-26 04:42:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| cac9ee41-c5dd-387d-a95b-f224b6eb53d5 | -2.83364 | -51.80818 | 2024-10-26 04:42:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d80e5073-b614-3392-b195-9c8b94d1d21c | -2.83307 | -51.81179 | 2024-10-26 04:42:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 3467d553-b947-334a-9ade-978e72a30f9d | -2.81608 | -51.34225 | 2024-10-26 04:42:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ef70efd7-6e84-393e-85f4-8cf9fdfbdf21 | -2.81218 | -51.34525 | 2024-10-26 04:42:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6c0cfb87-6fdf-3551-901f-4168f435879e | -2.80605 | -51.36233 | 2024-10-26 04:42:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e5384659-b561-3159-ae2c-910fae0cdbdb | -2.80271 | -51.3618 | 2024-10-26 04:42:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9401eb44-45d3-3831-a34f-05bdddf67a2c | -2.79982 | -51.59739 | 2024-10-26 04:42:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 1b84328f-d930-3351-85b8-a46d80a537aa | -2.79881 | -51.36481 | 2024-10-26 04:42:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 168732e6-fb50-3080-89d7-c48dc73de9ff | -2.79646 | -51.59685 | 2024-10-26 04:42:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 58f32554-f1c2-3743-bac9-f26d5121f111 | -2.79547 | -51.36428 | 2024-10-26 04:42:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 124be37c-7b77-319a-8997-3f132dd34a1e | -2.79213 | -51.36376 | 2024-10-26 04:42:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 643a08e6-0e8b-34f0-b205-faf46c45cb51 | -2.79157 | -51.36729 | 2024-10-26 04:42:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 009569ef-94b2-3ecc-b0d7-8a476c1b4c3c | -2.78879 | -51.36324 | 2024-10-26 04:42:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| c558b347-3e4d-360e-ab4a-caa50b60e08c | -2.78823 | -51.36677 | 2024-10-26 04:42:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 0e7fd33b-e9a8-381e-b27d-13720e3ea7cd | -2.69661 | -51.79065 | 2024-10-26 04:42:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| d486d18b-8fa5-3b74-b8e2-b21346c260b5 | -2.69603 | -51.79427 | 2024-10-26 04:42:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 89f449a6-019e-3346-b3c2-c5ad07bc8b96 | -2.69323 | -51.79012 | 2024-10-26 04:42:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 06615435-d00b-343c-9de1-e979c1b00546 | -2.69265 | -51.79374 | 2024-10-26 04:42:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 99df3389-3218-3422-bd11-fb6c66765bb9 | -2.69176 | -51.79043 | 2024-10-26 04:42:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 9cf27ce1-2d15-31f0-a8b5-e19eb7bc2087 | -2.69119 | -51.79404 | 2024-10-26 04:42:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| ddaed62c-2826-3628-aa80-d481f124d266 | -2.60444 | -51.77303 | 2024-10-26 04:42:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f14a3f73-75ff-3b6c-80bd-89133531659a | -2.60049 | -51.77612 | 2024-10-26 04:42:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 7c07c15e-55fe-3f55-9fc4-9e1171f89c47 | -2.5982 | -51.36642 | 2024-10-26 04:42:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 439e90c2-f789-3c02-869b-e969b419927b | -2.59542 | -51.36237 | 2024-10-26 04:42:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 1469e4eb-d2de-3ceb-b68a-f3324a94ecb7 | -2.59485 | -51.36593 | 2024-10-26 04:42:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 8adc1297-9f94-35d7-82f0-5c00eb5d194d | -2.5841 | -51.92232 | 2024-10-26 04:42:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| ef3d2f5b-a724-31dc-902c-8719d7551f1b | -2.57819 | -51.85053 | 2024-10-26 04:42:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 456a6a6f-07d5-3f44-8082-f604d92882da | -2.5748 | -51.85 | 2024-10-26 04:42:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 732ee6b7-ed6e-3372-8c62-ad11ca17f5f8 | -2.57379 | -51.85019 | 2024-10-26 04:42:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 250ffe4f-ae21-3711-8a1d-526103b18605 | -2.55488 | -51.23315 | 2024-10-26 04:42:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 21833675-8e48-3ae3-ad36-7afa2adc9de3 | -2.41521 | -50.47913 | 2024-10-26 04:42:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 7595c9dc-f604-3051-b8d4-8c0541a882d3 | -2.41191 | -50.47861 | 2024-10-26 04:42:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 2624c177-6576-3943-b795-f6fcef5269ab | -2.4116 | -50.56665 | 2024-10-26 04:42:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f7629b7a-f46f-3489-9b48-f272f368bc05 | -2.41071 | -50.4432 | 2024-10-26 04:42:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 81f59065-b1a0-393b-a5a4-4e3efb17420a | -2.40775 | -50.56958 | 2024-10-26 04:42:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 98977df6-2ae8-383e-aa8e-205af06f9523 | -2.40297 | -50.42791 | 2024-10-26 04:42:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f84eea89-63a3-34d1-bf19-a68d0808bb01 | -2.39966 | -50.4274 | 2024-10-26 04:42:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 4eba7989-631d-3316-9a1e-6ed23a98bd30 | -2.30752 | -50.49458 | 2024-10-26 04:42:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a482192f-0ac0-39ad-aada-15401fd23960 | -2.30475 | -50.49063 | 2024-10-26 04:42:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 34a9d512-90f7-3f5c-b213-2f1348c0516c | -2.28698 | -50.4315 | 2024-10-26 04:42:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1e34e6e7-de88-3087-9b18-19f85cc981c9 | 2.37036 | -51.44078 | 2024-10-26 04:42:00 | NOAA-20 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f86a2fe2-919c-3a7e-bff8-5a347dd409cc | 2.24911 | -51.03921 | 2024-10-26 04:42:00 | NOAA-20 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 9ca2840b-d4ec-30e1-91f4-940287cf98df | 1.26116 | -51.26766 | 2024-10-26 04:42:00 | NOAA-20 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 723a1bcb-eded-3077-a5d5-6fa955f516db | 1.23427 | -51.27517 | 2024-10-26 04:42:00 | NOAA-20 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c4e6ea95-2b3f-343d-a854-e5d3f8ba6dfe | 1.01014 | -52.22027 | 2024-10-26 04:42:00 | NOAA-20 | PEDRA BRANCA DO AMAPARI | AMAPÁ | Brasil | 1600154 | 16 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d196b088-2d2c-3f61-8887-57b95e108eee | 0.61958 | -51.8963 | 2024-10-26 04:42:00 | NOAA-20 | PORTO GRANDE | AMAPÁ | Brasil | 1600535 | 16 | 33 | nan | nan | nan | Amazônia | 1.4 |
| edc8e37c-5fe4-31d7-ac43-340a81f32307 | 0.0635 | -51.58932 | 2024-10-26 04:42:00 | NOAA-20 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c83949d0-7062-31bd-b9a2-72f15caa5589 | -0.40766 | -51.78289 | 2024-10-26 04:42:00 | NOAA-20 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 7e97b366-9ec2-385e-a847-d0ee3e48e4af | -0.96514 | -52.04799 | 2024-10-26 04:42:00 | NOAA-20 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 639ed3c1-d934-3a3a-a6be-05bf15505184 | -1.75156 | -52.32568 | 2024-10-26 04:42:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c153c608-904a-3e8d-b019-3bc5c1eda014 | -1.75095 | -52.32949 | 2024-10-26 04:42:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 42d6cc74-a974-3079-8074-65b8fa44b803 | -1.744 | -52.3284 | 2024-10-26 04:42:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 0bb2eda4-0992-33b8-b114-45d7d5643efc | -1.74339 | -52.33222 | 2024-10-26 04:42:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 62514c31-ad78-3589-8d71-c67186a873bc | -1.74053 | -52.32787 | 2024-10-26 04:42:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 5bb0e0fb-0951-3169-a2f6-cdd953713da1 | -1.72526 | -52.07399 | 2024-10-26 04:42:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |


[Clique aqui para ver as próximas entradas](README71.md)
