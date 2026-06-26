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
| 6b33ea6b-08e3-3558-97f6-e023f07ba272 | -12.76119 | -44.49676 | 2026-06-26 03:55:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 9541f942-c410-3438-a25c-45faae153b60 | -6.93406 | -43.67377 | 2026-06-26 03:55:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b9c7c07a-81bb-3151-9da0-d7333a6c343f | -10.10118 | -49.59564 | 2026-06-26 03:55:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 841cc5c2-c6c9-366d-8044-cde1342a1a36 | -12.6749 | -48.22111 | 2026-06-26 03:55:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 4209e935-e752-3c27-9268-2e94ae660d68 | -11.47762 | -47.3407 | 2026-06-26 03:55:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 2fb1c29d-cfc1-3f7a-9153-31a907644371 | -7.63505 | -50.21735 | 2026-06-26 03:55:00 | NOAA-21 | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| b8f58b77-b1f1-3108-965b-b81c4171397f | -7.93588 | -47.81707 | 2026-06-26 03:55:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 03f44fce-f2b7-34b9-85b4-d4a3399b9295 | -11.91438 | -43.77704 | 2026-06-26 03:55:00 | NOAA-21 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| b46381db-190e-3c02-89d0-498223036fa0 | -12.7512 | -44.48757 | 2026-06-26 03:55:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 921217d3-41b2-3b25-9b6b-9171c8230e74 | -6.30127 | -44.64976 | 2026-06-26 03:55:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 9b206dd7-75ca-37ad-8977-a857ed7651b8 | -6.30472 | -44.65411 | 2026-06-26 03:55:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 4.9 |
| a525edb6-6d24-3ada-b51c-43dfd40d4c6a | -11.25685 | -43.32227 | 2026-06-26 03:55:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 5.1 |
| e92c8ad6-a1b6-36ad-af3f-97687edc9b1e | -12.86972 | -44.33768 | 2026-06-26 03:55:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| a498aaff-3d69-3b74-8a43-4666ab550228 | -12.87275 | -44.34339 | 2026-06-26 03:55:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| a5d036c8-f4b0-35e1-89d3-966d6ce15ffc | -10.39461 | -50.13461 | 2026-06-26 03:55:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 331ff052-6c22-3bc8-b5c4-09ef71700462 | -9.1308 | -47.64454 | 2026-06-26 03:55:00 | NOAA-21 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 5578d643-f373-3c0b-8b42-1208236d1481 | -6.40043 | -45.44284 | 2026-06-26 03:55:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 14dcceb9-ad39-34d7-be66-90f3da07b27b | -12.75031 | -44.49275 | 2026-06-26 03:55:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 17e61e74-f1d7-3161-a8f1-caf9e2c2ad05 | -11.87717 | -51.72493 | 2026-06-26 03:55:00 | NOAA-21 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 83bc7846-090c-3800-be37-285d2f390592 | -12.75031 | -44.48949 | 2026-06-26 03:55:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 11.9 |
| f2eff05b-1475-33aa-8b78-066c31348990 | -8.01224 | -49.64824 | 2026-06-26 03:55:00 | NOAA-21 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 7c0c4e33-5ee4-379f-9e66-b904ac785a50 | -10.10278 | -49.58736 | 2026-06-26 03:55:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 10298814-9e77-3989-bd43-94b2ad689af7 | -6.50398 | -42.22533 | 2026-06-26 03:55:00 | NOAA-21 | VÁRZEA GRANDE | PIAUÍ | Brasil | 2211407 | 22 | 33 | nan | nan | nan | Caatinga | 6.4 |
| 18d8ff4f-04a1-3262-9872-c60706d9814f | -8.13398 | -47.88696 | 2026-06-26 03:55:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 4c2f7033-ae4d-3a6a-8fc1-61d42ee1579c | -8.50842 | -50.15175 | 2026-06-26 03:55:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 37e98287-96d5-3005-a146-8ef5ef81f034 | -7.74025 | -44.17456 | 2026-06-26 03:55:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 8cf12c45-a4a4-3578-bab6-5188965bd213 | -12.75425 | -44.49345 | 2026-06-26 03:55:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 8.9 |
| 8fa50b8e-3201-308b-b1df-fa351fd3c5cd | -12.86886 | -44.34266 | 2026-06-26 03:55:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 5d788675-b2ac-3bf2-b0cc-a1cc094755eb | -8.2007 | -42.42562 | 2026-06-26 03:55:00 | NOAA-21 | SÃO JOÃO DO PIAUÍ | PIAUÍ | Brasil | 2210003 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| c8cdc30b-8214-3ffc-971a-ea59ededf013 | -10.13248 | -52.11089 | 2026-06-26 03:55:00 | NOAA-21 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 93e1e9bb-2958-3423-8076-476c5139e2a9 | -8.86194 | -46.92832 | 2026-06-26 03:55:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 002ddd02-fbaa-3fa2-abcf-f50fe042ce83 | -9.40302 | -50.67747 | 2026-06-26 03:55:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 062fe905-c2e2-33b4-8a30-d76610767d74 | -11.20086 | -43.35271 | 2026-06-26 03:55:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 62494410-e4d9-3b56-83da-741710ee20b2 | -9.09908 | -47.52656 | 2026-06-26 03:55:00 | NOAA-21 | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 23cdd305-b6ff-357c-b300-c49084fd8864 | -6.98497 | -42.89295 | 2026-06-26 03:55:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 10.7 |
| 8be7aa68-5ef9-3f70-baf9-3eb1b7d6debe | -12.52248 | -48.28592 | 2026-06-26 03:55:00 | NOAA-21 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| a1eb1763-da9e-3e4c-8fa8-b2b9dff246dd | -7.93229 | -47.81643 | 2026-06-26 03:55:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 06f62bbb-f9f1-36e9-b285-80db7ecfccc3 | -8.14185 | -47.88446 | 2026-06-26 03:55:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 6.3 |
| fa3a6c1e-4364-3db5-85e6-4ddeeb52f526 | -6.50281 | -42.21349 | 2026-06-26 03:55:00 | NOAA-21 | VÁRZEA GRANDE | PIAUÍ | Brasil | 2211407 | 22 | 33 | nan | nan | nan | Caatinga | 3.7 |
| bea5a20a-2b61-3abb-a759-0150fdd752f8 | -12.5186 | -48.27879 | 2026-06-26 03:55:00 | NOAA-21 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| de0d2478-c35b-38ae-9479-c91e07d5b5f0 | -11.54896 | -48.26434 | 2026-06-26 03:55:00 | NOAA-21 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 32b091cf-69a5-3f50-9e0f-7437ee233d2d | -9.19954 | -45.32455 | 2026-06-26 03:55:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| a207c1e6-746b-3d1b-9ecb-dda337398268 | -12.51411 | -48.27483 | 2026-06-26 03:55:00 | NOAA-21 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| ab1d1ba7-155f-35e3-b325-1b22c98cfb69 | -7.6245 | -47.29547 | 2026-06-26 03:55:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 7368433a-9836-3fbe-b88d-f1a28dfe5e4e | -11.91354 | -43.78185 | 2026-06-26 03:55:00 | NOAA-21 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 279c725a-088d-311e-acd4-a0b1a5d1a4de | -6.30548 | -44.64977 | 2026-06-26 03:55:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 32cf9122-7514-36b8-9a1b-9c925eafc2dc | -11.78341 | -46.4308 | 2026-06-26 03:55:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 413f5f87-15dc-351d-adf4-7d96d5954805 | -12.75907 | -44.48897 | 2026-06-26 03:55:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 8.9 |
| bf4f9206-78ff-3c0e-b577-01742c269d0d | -12.75817 | -44.49089 | 2026-06-26 03:55:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 11.0 |
| d8980163-d285-3792-b3f9-a3850007a150 | -8.12735 | -47.89304 | 2026-06-26 03:55:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 845544fe-1cba-3bab-b07d-746b970c836b | -10.36251 | -47.33837 | 2026-06-26 03:55:00 | NOAA-21 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 9f11b737-2ef0-397c-8641-50844eb66fbc | -6.50472 | -42.22068 | 2026-06-26 03:55:00 | NOAA-21 | VÁRZEA GRANDE | PIAUÍ | Brasil | 2211407 | 22 | 33 | nan | nan | nan | Caatinga | 6.4 |
| 62b0608e-6389-3fa7-a3b4-556ddd491e40 | -10.36148 | -47.34408 | 2026-06-26 03:55:00 | NOAA-21 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 8390eb37-08b7-30f4-b08f-c3a24fffdae7 | -12.75818 | -44.49415 | 2026-06-26 03:55:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 8.9 |
| 0c9e8c9c-c5d4-3fa3-9596-3dc0352b56fd | -8.13653 | -47.88347 | 2026-06-26 03:55:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 9f8c218c-7c9b-3fc2-baeb-86a81561bcec | -6.81833 | -44.72162 | 2026-06-26 03:55:00 | NOAA-21 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 22bb59b6-90f7-3d67-8e5e-0cc63b6fe9c5 | -6.50876 | -42.22411 | 2026-06-26 03:55:00 | NOAA-21 | VÁRZEA GRANDE | PIAUÍ | Brasil | 2211407 | 22 | 33 | nan | nan | nan | Caatinga | 3.6 |
| ee3703f6-d4d8-34dc-b09e-113df6718c3e | -11.39119 | -47.81443 | 2026-06-26 03:55:00 | NOAA-21 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 536a356d-ca11-3213-b2bc-98df1bd9b5aa | -10.54264 | -47.71207 | 2026-06-26 03:55:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c773d89b-b1ae-3f0d-8991-e4ee80beca67 | -8.77355 | -46.93051 | 2026-06-26 03:55:00 | NOAA-21 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 41ab2f48-d1a1-3f3f-a96d-c290c6a11700 | -6.50049 | -42.22738 | 2026-06-26 03:55:00 | NOAA-21 | VÁRZEA GRANDE | PIAUÍ | Brasil | 2211407 | 22 | 33 | nan | nan | nan | Caatinga | 5.6 |
| 586ccf18-d008-316c-863c-99485119ed64 | -6.50323 | -42.23 | 2026-06-26 03:55:00 | NOAA-21 | VÁRZEA GRANDE | PIAUÍ | Brasil | 2211407 | 22 | 33 | nan | nan | nan | Caatinga | 3.9 |
| 26bfafea-4467-3758-ae71-1c02eb195233 | -11.91337 | -43.39778 | 2026-06-26 03:55:00 | NOAA-21 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 41b26161-65d1-3e1b-9687-7f96bdbebed4 | -11.5432 | -48.26658 | 2026-06-26 03:55:00 | NOAA-21 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| aca1c47b-09c8-339b-becb-21c67ea1b170 | -11.77076 | -46.44852 | 2026-06-26 03:55:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 17.6 |
| 9acdebfa-5675-3a84-8b0d-a27108eae53b | -11.77165 | -46.44371 | 2026-06-26 03:55:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 4.8 |
| d8e43b69-23f9-3596-9856-78a4e91ffa30 | -11.48034 | -47.34431 | 2026-06-26 03:55:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| b59c43ca-7712-38f2-ab37-cd00a62d6d11 | -6.5058 | -42.21873 | 2026-06-26 03:55:00 | NOAA-21 | VÁRZEA GRANDE | PIAUÍ | Brasil | 2211407 | 22 | 33 | nan | nan | nan | Caatinga | 6.1 |
| e5b30dfe-460f-3d6b-9838-06df1def7617 | -8.13531 | -47.89039 | 2026-06-26 03:55:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 71e3ad54-3cc7-38ed-b8b1-6d7bd23ab9d4 | -7.75003 | -44.6232 | 2026-06-26 03:55:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 8.5 |
| 87fc4fa3-5598-3960-a737-e67fb1d60245 | -11.25309 | -43.32165 | 2026-06-26 03:55:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 4.9 |
| 639cf372-3b51-3c50-a291-58eedf1c5f4c | -7.62913 | -47.29942 | 2026-06-26 03:55:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 83251913-125d-3578-9a6c-6849aea458b2 | -8.12935 | -47.89296 | 2026-06-26 03:55:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 2fe5fd68-a57d-33a4-8ece-036a97c1ceb5 | -12.08636 | -45.75809 | 2026-06-26 03:55:00 | NOAA-21 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| ef8db4b1-ea86-3c35-9186-507877f2884c | -12.74244 | -44.49135 | 2026-06-26 03:55:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 29c18968-03da-3771-a6fa-d0321b8ebe22 | -7.75505 | -44.61982 | 2026-06-26 03:55:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 8.5 |
| 0f4cddf0-0a7d-3bfd-ab6b-af3c280b9fe5 | -8.13333 | -47.89046 | 2026-06-26 03:55:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 8.0 |
| fe8a212f-980e-31f6-97a3-442c283e405f | -11.77798 | -46.43482 | 2026-06-26 03:55:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 5.0 |
| baa68f91-f376-36c1-a908-5f7662955d85 | -9.19514 | -45.32377 | 2026-06-26 03:55:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| d144577e-c1bc-3047-8600-c4be2792dba0 | -9.36532 | -50.5458 | 2026-06-26 03:55:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 9689a406-6e84-39b1-b873-84b3abcb3771 | -12.5219 | -48.28895 | 2026-06-26 03:55:00 | NOAA-21 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 8d254e1d-e643-3c8f-81d1-3cd1c5cd75d4 | -8.68547 | -47.86234 | 2026-06-26 03:55:00 | NOAA-21 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| d1488693-17ee-3afd-9649-0711d073e2d2 | -12.76211 | -44.4916 | 2026-06-26 03:55:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 11.0 |
| 969e2fcf-58fb-37fe-ab87-78c5dbd6b8eb | -11.37978 | -47.82162 | 2026-06-26 03:55:00 | NOAA-21 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 42124d31-7142-320b-8a10-c2ab5bde983a | -12.74727 | -44.48688 | 2026-06-26 03:55:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 4a1e7dad-30b8-3db0-aaee-2bdd3822403e | -10.36641 | -47.34503 | 2026-06-26 03:55:00 | NOAA-21 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 0f0e6666-aa39-3604-8a53-4f093824fa5d | -8.22849 | -47.12104 | 2026-06-26 03:55:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 45c4b832-62b1-32ba-8531-fad30106e6b6 | -11.7762 | -46.44448 | 2026-06-26 03:55:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 43.2 |
| d3407fdc-09b6-35f6-965d-43a485fd4802 | -8.23351 | -47.12214 | 2026-06-26 03:55:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 1a53f6bd-63ba-31a3-81f3-563afcae8b3a | -12.45026 | -44.75432 | 2026-06-26 03:55:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| daa28180-f7a0-34c7-bc6f-1cab5677e254 | -10.10232 | -49.58624 | 2026-06-26 03:55:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 18262aac-d0f3-315c-9b5d-2839d613a69c | -7.74714 | -44.61435 | 2026-06-26 03:55:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 1c76c14b-5672-37b8-9d95-46436a3edd4a | -10.36044 | -47.3498 | 2026-06-26 03:55:00 | NOAA-21 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| e986d795-1a9c-37d4-b96c-ccb7dbaef396 | -8.01562 | -49.64464 | 2026-06-26 03:55:00 | NOAA-21 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 6cd57813-a153-36fc-826c-d8ae2be68ce2 | -10.54079 | -47.71572 | 2026-06-26 03:55:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 377297a3-2299-3032-8478-3d8784c030fe | -9.36392 | -50.54742 | 2026-06-26 03:55:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 7.7 |
| df72b82f-eb4a-3ffe-b55e-ecbd7dcbca42 | -8.85592 | -46.92601 | 2026-06-26 03:55:00 | NOAA-21 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 34120888-4535-3c0f-b6cb-6e629e639c63 | -6.98026 | -42.89721 | 2026-06-26 03:55:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 10.7 |
| 687e202f-3b33-34f1-89be-8d0902cc73ab | -6.98415 | -42.89788 | 2026-06-26 03:55:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 10.7 |
| c3da4b05-05fa-3267-951c-540b250c0489 | -12.35504 | -47.42649 | 2026-06-26 03:55:00 | NOAA-21 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 4.8 |


[Clique aqui para ver as próximas entradas](README5.md)
