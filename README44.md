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

## Dados Diários - Página 44

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 626545ad-dab9-3c48-b889-65501dbde4d1 | -19.58829 | -56.73726 | 2024-10-31 04:53:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 14.4 |
| 7774f0e6-c84b-3c16-9378-bb525e54b997 | -19.58441 | -56.72622 | 2024-10-31 04:53:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 6.6 |
| 41a38fc2-fb3d-3e42-8175-36d0bf3d990d | -19.58228 | -56.71818 | 2024-10-31 04:53:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 5.1 |
| 4a45cd2a-5a41-314d-9dcc-c94e93303de1 | -19.58108 | -56.72562 | 2024-10-31 04:53:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 6.6 |
| 28c0d9fc-d314-3a69-8480-d087e8ee5b93 | -19.57561 | -56.71697 | 2024-10-31 04:53:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 1.8 |
| 624b6012-f984-3bb9-a3e7-ada6218cc244 | -19.57227 | -56.71636 | 2024-10-31 04:53:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 2.1 |
| c7b9ff82-cbfe-3977-841a-dd29e05cf7fc | -19.59891 | -56.73536 | 2024-10-31 04:53:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 77.3 |
| cea436f0-a9fe-3186-a604-fb0ac83a108f | -19.59831 | -56.697 | 2024-10-31 04:53:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 1.2 |
| b7720a9a-09f4-33cb-a0c4-61ce4e7bbb1f | -19.598 | -56.71989 | 2024-10-31 04:53:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 15.2 |
| 5f757530-a30e-30cf-b696-f849acb7de0f | -19.59798 | -56.762 | 2024-10-31 04:53:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 48.4 |
| 20e7eb6f-1d71-3393-b991-30b0317dcb25 | -19.59587 | -56.75395 | 2024-10-31 04:53:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 0.0 |
| 479476ef-d945-3827-9138-a9270b556f67 | -19.59557 | -56.73475 | 2024-10-31 04:53:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 19.7 |
| f597a32b-1151-375d-a517-a9ddf73eba2f | -19.59498 | -56.69639 | 2024-10-31 04:53:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 0.9 |
| 4fa8e027-6de6-3469-bbb6-25d942e7f3df | -19.59467 | -56.71928 | 2024-10-31 04:53:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 15.2 |
| 49680775-b083-3fa1-8818-622708e9ad1c | -19.59436 | -56.74219 | 2024-10-31 04:53:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 19.4 |
| b7e3af4d-2fb5-316b-bdf2-4fc437620eca | -19.59406 | -56.723 | 2024-10-31 04:53:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 15.2 |
| cff5223e-e702-33bc-99cb-43b3f663b6f8 | -19.59375 | -56.7459 | 2024-10-31 04:53:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 19.4 |
| 0bc30a7f-0a2c-38d4-8aff-d20fa0835645 | -19.5898 | -56.74902 | 2024-10-31 04:53:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 23.0 |
| 5f362daa-77ec-32de-8b37-a358ebc07556 | -19.58707 | -56.7447 | 2024-10-31 04:53:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 10.5 |
| c2735f88-abc1-38f9-969e-4447fa90ccbf | -19.58135 | -56.70271 | 2024-10-31 04:53:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 1.4 |
| 401c7531-f521-37b4-9665-783705011dba | -19.57774 | -56.72501 | 2024-10-31 04:53:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 3.1 |
| 57ea3dc7-729c-316b-8903-a3457462f10c | -19.56801 | -56.70029 | 2024-10-31 04:53:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 3.2 |
| cb16396e-1fa5-372e-a730-2ef7c6ba3606 | -19.5668 | -56.70772 | 2024-10-31 04:53:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 11.5 |
| 8ef3cfbe-787f-33a7-a058-5675cf79fe41 | -19.60073 | -56.72421 | 2024-10-31 04:53:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 5.2 |
| 75dc4203-0018-3b7e-bec7-bba376e120ab | -19.5971 | -56.70442 | 2024-10-31 04:53:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 2.0 |
| 25895802-98ef-3b94-925a-e44c735f6529 | -19.59528 | -56.71557 | 2024-10-31 04:53:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 4.6 |
| 28396df3-4b8a-341f-ba27-98f9ad9e5428 | -19.58982 | -56.70693 | 2024-10-31 04:53:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 2.0 |
| d693499f-7bc7-33eb-9c8d-1e0c5bdb5eca | -19.58739 | -56.72179 | 2024-10-31 04:53:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 13.1 |
| d2f54b98-f248-32f5-bfac-743c0faf0d06 | -19.58373 | -56.74409 | 2024-10-31 04:53:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 10.5 |
| df495a17-2c01-37b1-a9d0-41d07baad551 | -19.58015 | -56.71014 | 2024-10-31 04:53:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 2.8 |
| b57ae86d-0cca-375e-a8d1-d929b2252331 | -19.56954 | -56.71204 | 2024-10-31 04:53:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 6.6 |
| 8896cd66-3b00-3299-b231-e3a803e06a8d | -19.5662 | -56.71143 | 2024-10-31 04:53:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 11.5 |
| e8cad952-824e-3ce3-b2dd-9582d6c8e224 | -19.5656 | -56.71515 | 2024-10-31 04:53:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 9.7 |
| 7bd53929-e560-34e3-b201-f4c878d37372 | -19.56347 | -56.70711 | 2024-10-31 04:53:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 11.5 |
| aa489b0d-03c4-3382-b65b-82afa5601bc3 | -19.55944 | -56.62619 | 2024-10-31 04:53:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 0.6 |
| 688069cf-6503-381b-9658-9df6e86b902c | -19.5977 | -56.70071 | 2024-10-31 04:53:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 1.2 |
| e4fc4d74-847d-356a-8a28-d8cd472737ff | -19.59649 | -56.70814 | 2024-10-31 04:53:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 2.0 |
| d3c446f7-3dbc-34c8-bb73-3acbf78c7b80 | -19.58742 | -56.70764 | 2024-10-31 04:53:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 1.7 |
| 58f5a09f-9b41-3a3e-8c30-74d1472afb81 | -19.58682 | -56.71135 | 2024-10-31 04:53:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 1.6 |
| e846ac08-8046-3bef-b59c-bff29de31e34 | -19.58468 | -56.70332 | 2024-10-31 04:53:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 1.7 |
| c529464e-e7e3-324a-9026-1e15f476186b | -19.58075 | -56.70642 | 2024-10-31 04:53:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 1.4 |
| 088cc1b1-d024-3bc6-b49c-2713c31a9d22 | -19.57882 | -56.63351 | 2024-10-31 04:53:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 0.6 |
| 1341db31-4930-3506-8e92-be35fc99bd79 | -19.57468 | -56.7015 | 2024-10-31 04:53:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 4.8 |
| 4759d954-2962-3abf-a6d3-bd61a5d00d81 | -19.56741 | -56.704 | 2024-10-31 04:53:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 3.2 |
| 83449a8f-512e-3d79-8c6a-e7a457ce5d22 | -19.56227 | -56.71454 | 2024-10-31 04:53:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 9.7 |
| 7aaf21e5-e11d-34fc-925e-5aba89ad6b23 | -19.60134 | -56.72049 | 2024-10-31 04:53:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 5.2 |
| 58e09e32-237d-34e4-afea-5280f0206147 | -19.59073 | -56.72239 | 2024-10-31 04:53:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 13.1 |
| cb03d43f-691f-38fe-8152-4ff332e26f63 | -19.5889 | -56.73354 | 2024-10-31 04:53:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 14.4 |
| d13044a3-8e18-354d-95ad-5fff598f0593 | -19.588 | -56.71807 | 2024-10-31 04:53:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 13.1 |
| e9f1605a-e95f-36eb-9d8b-438fcdb93019 | -19.58585 | -56.75213 | 2024-10-31 04:53:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 2.9 |
| 8bfe2364-d5cf-32a9-8cdf-ece09117095f | -19.58496 | -56.73665 | 2024-10-31 04:53:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 14.4 |
| 14c17fd5-f057-39eb-a927-6d32680fbf9c | -19.58321 | -56.73366 | 2024-10-31 04:53:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 5.5 |
| 04e55134-c0b5-35e2-84b5-8f4ae1b53563 | -18.08099 | -57.37249 | 2024-10-31 04:53:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.8 |
| 912a1c6a-676e-3c2a-8d24-930ffacfa435 | -18.08033 | -57.37637 | 2024-10-31 04:53:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.8 |
| 1c46be34-4a46-3ee0-86ce-b4adebc6ee7c | -18.07481 | -57.36734 | 2024-10-31 04:53:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.3 |
| 934a3005-21e3-3766-b195-be9c401662e2 | -18.05315 | -57.2242 | 2024-10-31 04:53:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.9 |
| bd726b05-095c-332b-bd0c-40acf93e9259 | -18.04975 | -57.22357 | 2024-10-31 04:53:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.9 |
| 9a6fd208-85c9-3886-8f44-ab974023dbac | -18.03594 | -57.34863 | 2024-10-31 04:53:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.0 |
| e5fa0a4d-6a50-32e8-a9a0-17683d311ac1 | -17.81476 | -57.3904 | 2024-10-31 04:53:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 6.5 |
| 44d2ef07-960e-3468-a492-d3973883cfe6 | -17.81263 | -57.38196 | 2024-10-31 04:53:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 20.8 |
| e2b9bfcf-e0c3-3e5c-adc7-dcf8534e0ac3 | -17.81133 | -57.38976 | 2024-10-31 04:53:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 6.5 |
| 0a63363a-914b-3fa6-95f1-5e897b6218b8 | -17.81116 | -57.36962 | 2024-10-31 04:53:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.8 |
| ef49d818-37c2-3ddc-bd19-ed35765826b4 | -17.81051 | -57.37352 | 2024-10-31 04:53:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 11.7 |
| 71edf2c6-19e3-3b7c-980f-10a53f2c372e | -17.8092 | -57.38133 | 2024-10-31 04:53:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.4 |
| 9252c20f-1e67-3c91-80f3-b20e5eb42f6b | -17.80773 | -57.36898 | 2024-10-31 04:53:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.8 |
| 9a6f4c66-6df7-3155-8f27-8fb31d5c0177 | -17.79614 | -57.37491 | 2024-10-31 04:53:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.2 |
| 78ffc6ee-3377-30e1-bcc8-fe4062211679 | -17.79272 | -57.37427 | 2024-10-31 04:53:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.2 |
| ff088eb5-ec99-32b3-841c-b2d92da1bf0f | -17.79206 | -57.37818 | 2024-10-31 04:53:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.4 |
| f2d9909f-03aa-3b0f-82fc-8dc2868a0fba | -17.78308 | -57.36849 | 2024-10-31 04:53:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| 328fc70b-da58-3714-b4b7-3d0fbef053c7 | -17.74358 | -57.53941 | 2024-10-31 04:53:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 5.0 |
| 3880497a-68c5-30a0-9708-3f4ae2abc5c5 | -17.73256 | -57.54145 | 2024-10-31 04:53:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.8 |
| 4c9f21bf-0729-3f1c-aa2b-bbde854eb737 | -17.73189 | -57.54541 | 2024-10-31 04:53:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.3 |
| 18fa5311-5003-3261-b944-e470aa4423be | -17.73037 | -57.51254 | 2024-10-31 04:53:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.2 |
| 9cf2eba2-da4c-3bf2-a092-c3363453b700 | -17.72911 | -57.54082 | 2024-10-31 04:53:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.8 |
| e752b52b-5367-39e0-8dd5-3901e197e026 | -17.72364 | -57.55205 | 2024-10-31 04:53:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 14.7 |
| d69a961c-8b8b-3002-ae66-4c70304b0dbe | -17.72297 | -57.55601 | 2024-10-31 04:53:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 14.7 |
| 916413c3-9e81-3e91-9a39-c20a398383d4 | -17.72019 | -57.55141 | 2024-10-31 04:53:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 14.7 |
| ad22fd3c-2061-3bae-bf96-705ea4aa5c4c | -17.71951 | -57.55537 | 2024-10-31 04:53:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 14.7 |
| 7e3ef7ca-254f-3c43-9239-cdda895c69ce | -17.71733 | -57.52642 | 2024-10-31 04:53:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 0.8 |
| 91c48da1-2b42-311b-875b-7a5b207fd8d7 | -17.71666 | -57.53036 | 2024-10-31 04:53:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 0.8 |
| cc8fb977-9bcb-3c3d-b65d-bf858e95b751 | -17.68114 | -57.49637 | 2024-10-31 04:53:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.5 |
| 1f2adbe4-6df5-39a6-8509-6ad850d284da | -17.67769 | -57.49573 | 2024-10-31 04:53:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.5 |
| 33c39c4e-3803-3fea-bd62-a55c023bd54e | -17.67424 | -57.49508 | 2024-10-31 04:53:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.0 |
| 14cf9063-1c3a-3629-930c-a7436f06b7b4 | -17.67358 | -57.49903 | 2024-10-31 04:53:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.0 |
| 980d7a38-d14a-30c3-a52d-15a205d2b062 | -17.65701 | -57.49191 | 2024-10-31 04:53:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 8.1 |
| 2853c8f7-3e5d-315a-bfb6-fce02dd10f3b | -17.65357 | -57.49127 | 2024-10-31 04:53:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.1 |
| eb2a91b3-28d9-3cb5-add7-c232879773ae | -17.65279 | -57.47487 | 2024-10-31 04:53:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 9.8 |
| 8b8e77f2-4e94-3ecb-ba1e-753d907ecbb4 | -17.64934 | -57.47423 | 2024-10-31 04:53:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 0.9 |
| 6d2f2a85-4c24-39b6-b301-c1686b1034b3 | -17.64867 | -57.47817 | 2024-10-31 04:53:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 0.9 |
| 6fc3bf27-81a5-37b0-9e86-48bc52ccac0c | -17.27722 | -57.49942 | 2024-10-31 04:53:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 9.3 |
| 3c24b39b-ded3-3675-b1d3-7a998f577662 | -17.27656 | -57.50339 | 2024-10-31 04:53:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 9.3 |
| e9197bb0-997e-3949-9837-14151909b90c | -17.27376 | -57.49878 | 2024-10-31 04:53:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 15.1 |
| 4ee607a2-4bb3-3386-ad4e-b1c8d8eaacb5 | -17.2731 | -57.50275 | 2024-10-31 04:53:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 15.1 |
| e1ce4058-4ef3-3b05-ac26-8f9a4d7149f5 | -17.2703 | -57.49815 | 2024-10-31 04:53:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 15.1 |
| 22a5e8bd-2ac5-3169-a1c4-b13e3b7e4329 | -17.25992 | -57.49623 | 2024-10-31 04:53:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.5 |
| 7e0a25a2-aa1e-3f13-a02b-f225befd15ae | -17.24609 | -57.49368 | 2024-10-31 04:53:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.7 |
| 35fc3bad-371b-381e-b248-865c53fdd8f7 | -17.24196 | -57.49702 | 2024-10-31 04:53:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.7 |
| 817348fa-1d52-37d5-bef8-8b64cec6e8f2 | -17.21519 | -57.21729 | 2024-10-31 04:53:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 0.8 |
| 9c0359fe-fa4f-39f6-86a7-eca5f29966ec | -19.19133 | -57.8486 | 2024-10-31 04:53:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.6 |
| b740e7e4-02af-3f54-a982-ee7b81c536f1 | -24.65807 | -50.17565 | 2024-10-31 04:55:00 | NOAA-20 | CASTRO | PARANÁ | Brasil | 4104907 | 41 | 33 | nan | nan | nan | Cerrado | 1.5 |


[Clique aqui para ver as próximas entradas](README45.md)
