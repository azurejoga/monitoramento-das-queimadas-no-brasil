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

## Dados Diários - Página 96

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 8fe380d4-becc-3235-85d7-8db2c2e77611 | -16.6411 | -55.56523 | 2024-10-07 04:55:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 4.0 |
| 5ca4d590-b444-3dfc-90ee-c2d197241af0 | -16.63836 | -55.56104 | 2024-10-07 04:55:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.7 |
| e73982c0-db27-35ce-bbd7-9c59b38104d8 | -16.63822 | -55.58326 | 2024-10-07 04:55:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.5 |
| 8221edf3-4b1f-3e41-8ff2-d1373f79b5c3 | -16.63779 | -55.56465 | 2024-10-07 04:55:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.7 |
| 0351c94d-3e81-362f-8795-812a84ebef0e | -16.63721 | -55.56826 | 2024-10-07 04:55:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |
| b2ddf3c5-ad34-34cc-b320-c3f485e5774c | -16.63491 | -55.5827 | 2024-10-07 04:55:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.5 |
| 01dbedad-06e7-3e7c-85ec-27d53915b95e | -16.63448 | -55.56408 | 2024-10-07 04:55:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.7 |
| 39e592ee-e3dc-35fb-b9ed-2b6654851e7d | -16.6339 | -55.56769 | 2024-10-07 04:55:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |
| cee6c20f-b777-3f48-a49c-58dd1a058e88 | -16.63333 | -55.5713 | 2024-10-07 04:55:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |
| 19649fd3-cb76-348d-b6cf-b6391902661d | -16.63275 | -55.57491 | 2024-10-07 04:55:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.9 |
| 096f975e-5e54-3fae-a44f-d6a551bb05f2 | -16.63117 | -55.5635 | 2024-10-07 04:55:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.9 |
| eb50072a-e0ec-38aa-8c07-574b4d027d86 | -16.63059 | -55.56711 | 2024-10-07 04:55:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.7 |
| 7101aec8-1a51-3b88-9ea6-0f30c9c48ceb | -16.62862 | -55.2163 | 2024-10-07 04:55:00 | NOAA-21 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 1.4 |
| b3f88008-b30f-3b1f-b056-8158e61fd40f | -16.62843 | -55.55933 | 2024-10-07 04:55:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.9 |
| 20c23f61-27af-3c10-bae4-ecbd1f51145a | -16.62805 | -55.21989 | 2024-10-07 04:55:00 | NOAA-21 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |
| 47b6d216-c21d-322e-adcc-cee18142732a | -16.62786 | -55.56293 | 2024-10-07 04:55:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.9 |
| 3a964df4-4d3f-3356-abca-467c78254cc7 | -16.62728 | -55.56654 | 2024-10-07 04:55:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.7 |
| 02bdc7a6-2d8e-377f-ab4f-98a1b0c1af1a | -16.62671 | -55.57014 | 2024-10-07 04:55:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.7 |
| 04fdd45d-c25e-3c9a-a80b-ccd0a424c269 | -16.62555 | -55.57738 | 2024-10-07 04:55:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.5 |
| fb1589f3-604d-3793-b4b0-5c9e6a837e42 | -16.62454 | -55.56236 | 2024-10-07 04:55:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 3.8 |
| 567b5287-e89a-3eea-822a-2d6b535b3dfc | -16.62397 | -55.56596 | 2024-10-07 04:55:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 3.1 |
| 4b0812b3-0241-30ff-8308-33f3bd6a4680 | -16.62339 | -55.56956 | 2024-10-07 04:55:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 3.1 |
| dd880720-3fed-3c8d-ac8a-98034d2dcb52 | -16.62295 | -55.55103 | 2024-10-07 04:55:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.4 |
| 078afb24-d17e-3a1a-ae97-0cf28316bde6 | -16.62282 | -55.57318 | 2024-10-07 04:55:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.4 |
| d1ca739e-ff92-306d-be94-56d8eec4dbb1 | -16.62224 | -55.5768 | 2024-10-07 04:55:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.4 |
| fc0b203a-23b3-313b-b2f7-1b560f2d0205 | -16.62123 | -55.5618 | 2024-10-07 04:55:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 3.8 |
| 13352e85-4814-351a-866f-28b680091287 | -16.62066 | -55.5654 | 2024-10-07 04:55:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 3.1 |
| bee384cf-d274-3621-a61e-90f1968e6ad8 | -16.62035 | -55.52469 | 2024-10-07 04:55:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| 5172fcb1-cc82-38b6-8e43-92516234edc4 | -16.62021 | -55.54686 | 2024-10-07 04:55:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.8 |
| 2bc7e8e8-04bb-35c1-ae62-7be83063d364 | -16.62008 | -55.569 | 2024-10-07 04:55:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 3.1 |
| f4e2c9f9-091b-3325-a4b1-a1f57ca44d79 | -16.61978 | -55.52829 | 2024-10-07 04:55:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| 136a45de-9ff4-3de3-936c-b286ceddb595 | -16.61964 | -55.55046 | 2024-10-07 04:55:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 0.9 |
| a81ca20e-d615-37a1-85ab-97028adad27d | -16.6195 | -55.57261 | 2024-10-07 04:55:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.4 |
| fb6bce39-3482-3836-bf73-a78d81700b96 | -16.61835 | -55.57985 | 2024-10-07 04:55:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.5 |
| 3ab033df-d542-3317-908d-9cc1ed421e28 | -16.61777 | -55.58345 | 2024-10-07 04:55:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.5 |
| a5a5ffa3-9a63-35a1-8bb6-4e4ee253378e | -16.61734 | -55.56484 | 2024-10-07 04:55:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 4.6 |
| 7b4c4b6d-461a-3ed3-8118-66e3c8cc645c | -16.61677 | -55.56844 | 2024-10-07 04:55:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 4.6 |
| 8acd77b2-c86c-38e9-931e-99c4f0ad3eaf | -16.61646 | -55.52773 | 2024-10-07 04:55:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 0.6 |
| 45a4ffdd-4a79-3594-a549-c535da7099ff | -16.61633 | -55.5499 | 2024-10-07 04:55:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 0.9 |
| 455a447d-52f7-3563-b6d7-ed94e0f6509e | -16.61619 | -55.57205 | 2024-10-07 04:55:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.9 |
| 47bc4f85-7e29-3fa7-b3fc-9a7628c6e734 | -16.61589 | -55.53132 | 2024-10-07 04:55:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 0.6 |
| aefa6fad-6cb0-3725-9955-30b3d9fa4337 | -16.61561 | -55.57566 | 2024-10-07 04:55:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.9 |
| 70c13be9-714f-3c94-b3cb-76cbc504b065 | -16.61503 | -55.57928 | 2024-10-07 04:55:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.0 |
| bd6e9685-c2d7-36ce-b5d6-f10741b5f664 | -16.61483 | -55.21764 | 2024-10-07 04:55:00 | NOAA-21 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 1.0 |
| e0d794d9-4cf0-3904-9f29-1118a0ab3f44 | -16.61446 | -55.58289 | 2024-10-07 04:55:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.0 |
| efb81730-83fb-3b87-828c-2cca5b8702f2 | -16.61427 | -55.22123 | 2024-10-07 04:55:00 | NOAA-21 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 1.0 |
| fb79ee41-69b7-3ded-ab8c-66a42c4b7c22 | -16.61359 | -55.54573 | 2024-10-07 04:55:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.7 |
| a5b75724-77af-3d0e-b206-f0fa21ad3cbd | -16.61345 | -55.56789 | 2024-10-07 04:55:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 4.6 |
| 9b37fa4a-d5c1-353f-be82-37e57485066f | -16.61288 | -55.57149 | 2024-10-07 04:55:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.9 |
| f376d44f-9de4-3e22-be9f-1038e3463972 | -16.6123 | -55.5751 | 2024-10-07 04:55:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.9 |
| 8a05b7fd-0520-3514-a14b-37be94e208b7 | -16.61182 | -55.21358 | 2024-10-07 04:55:00 | NOAA-21 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |
| dcc6904d-8667-3fd6-9268-67c6e12aeb1e | -16.61172 | -55.57871 | 2024-10-07 04:55:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.0 |
| fc273f1a-4ac9-3436-9135-18dae0eff4af | -16.61125 | -55.21717 | 2024-10-07 04:55:00 | NOAA-21 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 4.2 |
| a79614dd-b201-399b-b8c1-05b105dacee0 | -16.61114 | -55.58232 | 2024-10-07 04:55:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.0 |
| 78b08549-9d01-30fa-90dd-8a51d19940ec | -16.61069 | -55.22075 | 2024-10-07 04:55:00 | NOAA-21 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 4.2 |
| ddb649db-8443-30e6-818d-99995ab16844 | -16.60841 | -55.57815 | 2024-10-07 04:55:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.7 |
| 1046f5bd-d594-3f54-8a7c-a8908fff4e4f | -16.60794 | -55.21661 | 2024-10-07 04:55:00 | NOAA-21 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 4.2 |
| e7ffb077-2268-39cf-8ceb-45879c3f16f9 | -16.60783 | -55.58175 | 2024-10-07 04:55:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.7 |
| 9419a811-4b54-3515-ae9d-d296caf3b42b | -16.60577 | -55.20888 | 2024-10-07 04:55:00 | NOAA-21 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 1.3 |
| 1532f5c3-cb5a-33b8-81f4-ef8b7a04b8a2 | -16.60521 | -55.21246 | 2024-10-07 04:55:00 | NOAA-21 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 1.3 |
| bab7b8a8-23b0-3dbb-bff9-d11ce309a52c | -16.60464 | -55.21605 | 2024-10-07 04:55:00 | NOAA-21 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 2.1 |
| 51c68ade-81e2-37ba-9533-d0f2e8a3743f | -17.02287 | -56.6805 | 2024-10-07 04:55:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 39.5 |
| 53e68f1d-cdff-3b72-a58f-41700896971e | -15.90075 | -55.40552 | 2024-10-07 04:55:00 | NOAA-21 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a1b36a1c-131d-3304-9378-e7fbabbe597e | -15.89744 | -55.40493 | 2024-10-07 04:55:00 | NOAA-21 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 640c8877-d499-3972-9ddc-b4bc209c0f46 | -15.89687 | -55.4085 | 2024-10-07 04:55:00 | NOAA-21 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| fe1edf6c-162d-31d8-bb8e-511d7e878943 | -15.89026 | -55.40734 | 2024-10-07 04:55:00 | NOAA-21 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| d9c11b3f-f0f6-3e7a-8adb-f0ce8e509ae5 | -16.58382 | -55.9013 | 2024-10-07 04:55:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.4 |
| bc30781c-023c-3bc6-9abe-32f8433e9e61 | -16.58125 | -56.06593 | 2024-10-07 04:55:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.7 |
| 3933861c-9107-374b-8fee-b5cfbf299c1d | -16.58066 | -56.06959 | 2024-10-07 04:55:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.7 |
| d178b746-d78f-3783-9b6b-8e3c9da22ae6 | -16.5791 | -56.05803 | 2024-10-07 04:55:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.2 |
| 79a7506d-cff0-3af8-8b0a-87d0e5cc7f01 | -16.5785 | -56.06169 | 2024-10-07 04:55:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.2 |
| 17c50581-a998-3d67-8c16-c8f204131b50 | -16.57791 | -56.06535 | 2024-10-07 04:55:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.5 |
| 787f1a04-3abc-307e-9107-96c9f6e3edeb | -16.57732 | -56.06901 | 2024-10-07 04:55:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.5 |
| d7453d43-2b92-3983-9008-0268118d0b43 | -16.57517 | -56.06112 | 2024-10-07 04:55:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.2 |
| 8f8e3ed2-ed83-3a0c-8e6f-3735d7851d1c | -16.56717 | -55.96207 | 2024-10-07 04:55:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.8 |
| bd6d28a1-18e2-3894-99f5-522296928fc0 | -16.56483 | -55.91298 | 2024-10-07 04:55:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 4.9 |
| af7dd437-93c7-362d-9765-c0042e9c17c1 | -16.56425 | -55.91662 | 2024-10-07 04:55:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 4.9 |
| 70ddc020-b072-3c02-9e19-ca9835512403 | -16.55818 | -55.91182 | 2024-10-07 04:55:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 4.1 |
| 6dbba1d5-93f1-3ea0-b889-5eacd49e36e8 | -16.55759 | -55.91546 | 2024-10-07 04:55:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 4.1 |
| 5e224012-0518-34b6-9a33-bb8d423124f5 | -16.4155 | -55.95103 | 2024-10-07 04:55:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.9 |
| 48a742ca-ae1b-31c8-90b0-2017a2d92a9c | -16.35683 | -55.97875 | 2024-10-07 04:55:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 3.0 |
| b767fca2-e03a-341b-b0fa-b352fb1fd4ef | -16.20382 | -55.99699 | 2024-10-07 04:55:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.9 |
| 1dea7a77-a747-3c10-823d-f8ec128f321d | -16.20322 | -56.00065 | 2024-10-07 04:55:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.4 |
| 8057ada5-b545-3fe2-8821-32894f7426f0 | -16.15779 | -55.92548 | 2024-10-07 04:55:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.2 |
| d971c5ec-b379-31a5-91f6-9b31d8fd3f08 | -16.15721 | -55.92911 | 2024-10-07 04:55:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.2 |
| 02505339-bf50-3b38-8634-f66a5601098a | -16.15446 | -55.92489 | 2024-10-07 04:55:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.2 |
| 280fb493-b1bc-3b45-8b3f-bee0458e08c1 | -16.15387 | -55.92852 | 2024-10-07 04:55:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.2 |
| 84598f4e-86dc-3734-9ab9-d8621aeefe53 | -16.15053 | -55.92797 | 2024-10-07 04:55:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 3.1 |
| 1b55473b-1b5e-37ba-8be8-07f6d7a26305 | -16.14328 | -55.86683 | 2024-10-07 04:55:00 | NOAA-21 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 2.8 |
| a426af3f-3010-3af1-8aed-f92d52f49d45 | -16.14269 | -55.87045 | 2024-10-07 04:55:00 | NOAA-21 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 4.2 |
| f144747c-b487-3e7b-8edd-156bff7533da | -16.13995 | -55.86624 | 2024-10-07 04:55:00 | NOAA-21 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 2.9 |
| 74a82e80-3f32-3f97-b212-bd314bcf4778 | -16.13662 | -55.86566 | 2024-10-07 04:55:00 | NOAA-21 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 2.9 |
| c24d6949-9413-35bf-b0e2-2a1eb71c31ce | -16.13603 | -55.8693 | 2024-10-07 04:55:00 | NOAA-21 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 3.7 |
| 3ec66ae4-1806-3e28-94e4-92d6fda83465 | -17.09904 | -56.68976 | 2024-10-07 04:55:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 0.9 |
| c3b9231f-3a41-3024-84c7-345ab004e6df | -17.27927 | -56.19091 | 2024-10-07 04:55:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.8 |
| 950c3979-9263-3ba4-90f1-c021eba67e15 | -17.27594 | -56.19033 | 2024-10-07 04:55:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.8 |
| 55d40d53-0ab0-3935-8d5d-bfc61913580a | -17.27534 | -56.194 | 2024-10-07 04:55:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 5.5 |
| 44207a10-8317-3bd0-ab2f-2b6ac06e7547 | -17.26594 | -56.18858 | 2024-10-07 04:55:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.4 |
| c4f6e497-c026-3c0b-8e88-93121fe5abe8 | -17.26534 | -56.19225 | 2024-10-07 04:55:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.0 |
| ab3b796b-4a67-3b06-af9c-9d64afb528e2 | -17.19721 | -56.17258 | 2024-10-07 04:55:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.5 |


[Clique aqui para ver as próximas entradas](README97.md)
