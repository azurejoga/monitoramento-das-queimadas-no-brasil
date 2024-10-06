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

## Dados Diários - Página 13

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| b0990294-871c-30c7-841e-3aa62c315f7d | -9.2627 | -48.141701 | 2024-10-06 00:48:21 | METOP-B | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 3eef068d-15b1-3340-a8ae-688c78be99f2 | -9.2647 | -48.150002 | 2024-10-06 00:48:21 | METOP-B | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| a12cf517-4e27-3b3b-a8fa-a20d0a503811 | -9.7166 | -50.111301 | 2024-10-06 00:48:21 | METOP-B | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| ca305207-9f1d-39be-9ac1-7d74530e9dd1 | -9.7413 | -50.630199 | 2024-10-06 00:48:23 | METOP-B | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 73f50d9d-767d-3ced-9da1-2c1a8e62a748 | -9.7429 | -50.637199 | 2024-10-06 00:48:23 | METOP-B | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9fb9a1a5-76ae-3794-b3a2-b23c210efb29 | -9.7445 | -50.644199 | 2024-10-06 00:48:23 | METOP-B | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c45923a1-1257-3a9b-942b-8c48b251dbbe | -9.7331 | -50.6394 | 2024-10-06 00:48:23 | METOP-B | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f2ad3747-7f9d-3607-b0c7-2516db1ef474 | -9.7347 | -50.6464 | 2024-10-06 00:48:23 | METOP-B | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1cdbf6ff-453b-3427-b7b8-6a4075c97223 | -9.7233 | -50.641602 | 2024-10-06 00:48:23 | METOP-B | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| fa749122-b61f-30d6-aae2-d863f94b06f4 | -9.7249 | -50.648602 | 2024-10-06 00:48:23 | METOP-B | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c0544472-a1c8-3a17-85b5-c19ff4902150 | -9.5861 | -50.081402 | 2024-10-06 00:48:23 | METOP-B | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 2072fc9c-b937-38e2-88f5-d04508b7cf14 | -9.5743 | -50.210999 | 2024-10-06 00:48:24 | METOP-B | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7824bfba-3e93-317b-815f-8fd59cdd78bd | -9.5645 | -50.2132 | 2024-10-06 00:48:24 | METOP-B | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c8eb0c01-d7f1-3bdc-a79b-4d3b0db5f0b1 | -9.5661 | -50.220299 | 2024-10-06 00:48:24 | METOP-B | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 75c22323-63a9-3a1a-8c7b-5d81cceb546f | -9.5677 | -50.227402 | 2024-10-06 00:48:24 | METOP-B | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5c4aa2a0-dca4-3f9a-a49c-6ab6e358873a | -9.5417 | -50.203602 | 2024-10-06 00:48:25 | METOP-B | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7225496d-272b-353a-8b32-c1a923e3d38f | -9.5433 | -50.210701 | 2024-10-06 00:48:25 | METOP-B | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f6f65b1f-5a2b-3385-aec5-e078929fe970 | -7.7232 | -43.038601 | 2024-10-06 00:48:26 | METOP-B | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| d496a091-1870-36f1-99a2-6108dcac381f | -7.6135 | -42.473801 | 2024-10-06 00:48:26 | METOP-B | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 17b17bc6-cd56-3843-a14b-3ff28c6ab92f | -8.6049 | -46.4911 | 2024-10-06 00:48:26 | METOP-B | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 0a1187a9-93db-383d-9394-3f904d50d15d | -8.6024 | -46.480598 | 2024-10-06 00:48:26 | METOP-B | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 8abd3fd0-71b4-320c-98f2-7a512697a4ad | -7.681 | -42.951 | 2024-10-06 00:48:27 | METOP-B | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 3b7447b3-b00f-3192-8dcc-80b4cb76811d | -7.6856 | -42.9697 | 2024-10-06 00:48:27 | METOP-B | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 2fb299be-f31e-3559-8f76-2acc2bdd764b | -7.6759 | -42.972099 | 2024-10-06 00:48:27 | METOP-B | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 993fcc39-4299-38f3-9141-e3430204118d | -7.6713 | -42.9534 | 2024-10-06 00:48:27 | METOP-B | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 5f9a4645-8e0f-37e5-9e10-e6fa6d9e05d1 | -8.4431 | -46.418201 | 2024-10-06 00:48:28 | METOP-B | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| bc3fc266-2c5f-387d-969b-70b493350ac4 | -8.4333 | -46.420601 | 2024-10-06 00:48:28 | METOP-B | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| db415bfe-7218-3c34-b6f2-3e1ed094c021 | -8.3875 | -46.271999 | 2024-10-06 00:48:28 | METOP-B | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| f7a29e24-7cec-3b65-bc26-2b88aa1f1f23 | -8.3901 | -46.282902 | 2024-10-06 00:48:28 | METOP-B | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| dc20c195-c70e-33e1-a203-802c649ad422 | -9.6357 | -51.768101 | 2024-10-06 00:48:29 | METOP-B | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b2fa3a9b-9beb-3570-89e6-786317ae9c98 | -9.6372 | -51.775101 | 2024-10-06 00:48:29 | METOP-B | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 475e6222-d78f-35e5-97bf-54fe7285ef59 | -8.3804 | -46.285198 | 2024-10-06 00:48:29 | METOP-B | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| f6fc7e3a-fea8-3370-bfe8-c81adaf6c7c4 | -9.3736 | -50.736 | 2024-10-06 00:48:29 | METOP-B | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1785e97e-6f8e-37a4-b446-26200afea20b | -9.3751 | -50.742901 | 2024-10-06 00:48:29 | METOP-B | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7d00dd4a-b2ea-346d-9c4a-563ee6ab4551 | -9.3752 | -51.063499 | 2024-10-06 00:48:30 | METOP-B | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a68dedf0-f181-332c-91d0-a9f0bed0779f | -9.3768 | -51.070499 | 2024-10-06 00:48:30 | METOP-B | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a6c83c80-d786-3a88-9095-c73fac226db3 | -9.3783 | -51.0774 | 2024-10-06 00:48:30 | METOP-B | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7fe45ffc-960a-386e-be33-f03fd1f4e55a | -9.3639 | -51.058899 | 2024-10-06 00:48:31 | METOP-B | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 327cf5ab-e447-3d14-9592-27f848d8f625 | -9.3654 | -51.0658 | 2024-10-06 00:48:31 | METOP-B | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ee74997c-7731-3795-b755-ab916f34ba32 | -9.367 | -51.0728 | 2024-10-06 00:48:31 | METOP-B | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 23816bb0-7937-3534-91e5-f5b69861ba0c | -9.3685 | -51.0797 | 2024-10-06 00:48:31 | METOP-B | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 086d2e76-7bc3-3d65-a01e-fb83dfacdeb8 | -9.3701 | -51.086601 | 2024-10-06 00:48:31 | METOP-B | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 55982c7b-22f9-3763-97f7-30befd4eb857 | -9.3572 | -51.075001 | 2024-10-06 00:48:31 | METOP-B | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ea399f4b-3d9f-3ab2-bffe-ac46736a6cfe | -8.9291 | -49.7327 | 2024-10-06 00:48:33 | METOP-B | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 590d7d4f-ab8c-3e91-97d6-ee0aea95f744 | -8.886 | -49.634701 | 2024-10-06 00:48:33 | METOP-B | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 96a07a72-99b6-380b-8fbc-1f1744335eaf | -8.8765 | -49.683201 | 2024-10-06 00:48:33 | METOP-B | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 0552eeaa-ec2d-301a-877e-be0b8a87c805 | -8.7876 | -49.9258 | 2024-10-06 00:48:36 | METOP-B | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| cf4ddf3c-7e64-3557-9ca6-75b177a379f3 | -8.7893 | -49.932999 | 2024-10-06 00:48:36 | METOP-B | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| def77ed2-a67e-33b8-9fed-2adb1ce10a3a | -8.6582 | -49.405899 | 2024-10-06 00:48:36 | METOP-B | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 5c8a1a83-8695-3686-bbfa-5ff2240b8d4a | -8.6599 | -49.413399 | 2024-10-06 00:48:36 | METOP-B | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| c5537c0f-2e4e-3f47-ac83-989f4a20a376 | -8.6616 | -49.420898 | 2024-10-06 00:48:36 | METOP-B | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 5c426e9c-bec4-376f-9040-61f22ef6038b | -8.7795 | -49.9352 | 2024-10-06 00:48:36 | METOP-B | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f0d12e6e-0595-345b-a81a-0e7ec6fc4cb8 | -8.7697 | -49.9375 | 2024-10-06 00:48:36 | METOP-B | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9c40e1d9-28d6-3abd-ada2-8d248c6b090e | -8.7713 | -49.944698 | 2024-10-06 00:48:36 | METOP-B | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9e13ab3e-98b4-36be-9970-77853130fad1 | -8.7582 | -49.932499 | 2024-10-06 00:48:36 | METOP-B | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ed955661-17ff-361e-afe0-1163c9f0b484 | -8.7599 | -49.939701 | 2024-10-06 00:48:36 | METOP-B | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| cca95816-d9a0-38fe-a0dc-4a872473ac7b | -8.7615 | -49.946899 | 2024-10-06 00:48:36 | METOP-B | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 341379d8-5959-3b62-ab77-766a5ed4fa24 | -8.7632 | -49.954102 | 2024-10-06 00:48:36 | METOP-B | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 23a2d3e0-f37d-3296-ba40-69380dd36d3a | -8.7648 | -49.9613 | 2024-10-06 00:48:36 | METOP-B | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c198ba12-13c5-3270-aebd-16f3105247a3 | -8.7501 | -49.942001 | 2024-10-06 00:48:36 | METOP-B | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 890c8dc5-eeed-3fba-8801-d711cfc3f933 | -8.7517 | -49.9492 | 2024-10-06 00:48:36 | METOP-B | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d54e1596-9923-345f-8624-3b78ac8309e2 | -8.7534 | -49.956402 | 2024-10-06 00:48:36 | METOP-B | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d2e50a18-492e-3689-9f03-301ebc17f99f | -7.4427 | -44.745899 | 2024-10-06 00:48:38 | METOP-B | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 3c0cec65-4e50-32aa-8286-e2a37a296b5c | -7.4461 | -44.759998 | 2024-10-06 00:48:38 | METOP-B | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 1c15f580-3935-3d53-b2bc-402a2a8fd997 | -8.6244 | -50.023899 | 2024-10-06 00:48:39 | METOP-B | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4e9f4621-aa91-3864-8ad8-af4187c405e7 | -8.626 | -50.031101 | 2024-10-06 00:48:39 | METOP-B | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 48914c63-9ae1-32bd-b84d-c54dbb768c05 | -8.6277 | -50.0383 | 2024-10-06 00:48:39 | METOP-B | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 637850aa-1cb4-3c54-8adc-2853ce6d999a | -8.1161 | -49.5154 | 2024-10-06 00:48:45 | METOP-B | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| fe650fbd-c96e-3308-ac02-84f38775a800 | -8.1045 | -49.509998 | 2024-10-06 00:48:45 | METOP-B | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c20ca182-6ba4-3a6b-a2be-1ebe2ca5e2ec | -8.1063 | -49.517601 | 2024-10-06 00:48:45 | METOP-B | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| dcb7a5dc-e664-3b22-9ac9-76e519a502b7 | -8.3259 | -50.6147 | 2024-10-06 00:48:46 | METOP-B | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| fa1b7e56-de72-3cc8-afd5-ed9c3c8c2a3f | -8.1309 | -49.9851 | 2024-10-06 00:48:47 | METOP-B | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 37fddf73-15fb-3b2c-bead-50f79ea0afdf | -9.8819 | -59.4674 | 2024-10-06 00:48:51 | METOP-B | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| f897dbec-aaf9-3448-802a-dfbfa70c74b6 | -7.0585 | -46.578899 | 2024-10-06 00:48:51 | METOP-B | FEIRA NOVA DO MARANHÃO | MARANHÃO | Brasil | 2104073 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| abd39eb3-f2b9-357a-865d-91f1cb351edc | -7.7133 | -49.827099 | 2024-10-06 00:48:53 | METOP-B | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 705777c2-8222-3fb3-97aa-aa16bb95ce2a | -6.9038 | -47.670898 | 2024-10-06 00:48:58 | METOP-B | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 435a8875-c452-3e14-b1e9-d196417022bd | -6.9061 | -47.680302 | 2024-10-06 00:48:58 | METOP-B | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| a925cc2d-d83f-3494-a3d8-0f23667647c3 | -6.8918 | -47.6637 | 2024-10-06 00:48:58 | METOP-B | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 1651fa1f-8736-33e5-88b4-9ea060f52532 | -6.894 | -47.6731 | 2024-10-06 00:48:58 | METOP-B | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 09939416-4a80-38f0-a9e2-66aebb91e82f | -6.8963 | -47.682499 | 2024-10-06 00:48:58 | METOP-B | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 98ac9b66-a4b3-39ce-9159-e4f511fc6bd2 | -6.8843 | -47.6754 | 2024-10-06 00:48:58 | METOP-B | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 8ca6e402-78aa-3843-bb2b-c0cd0586c43e | -6.4023 | -45.812698 | 2024-10-06 00:48:59 | METOP-B | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 9356912b-0293-3afc-8be8-cd329e1d50d7 | -6.3302 | -45.683201 | 2024-10-06 00:48:59 | METOP-B | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 6179a988-9cb0-32b3-91ec-48697dc9a16f | -6.3333 | -45.6959 | 2024-10-06 00:48:59 | METOP-B | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| d55056a3-87f3-30d3-adc7-c922aeb8b852 | -5.8064 | -44.103901 | 2024-10-06 00:49:02 | METOP-B | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| f9777cad-2121-3a06-8df8-adc02f576aae | -5.8104 | -44.120499 | 2024-10-06 00:49:02 | METOP-B | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 2289349a-6963-33fc-9a82-79c6dfef86fa | -5.7967 | -44.106201 | 2024-10-06 00:49:02 | METOP-B | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 79552904-cd24-382d-b797-0918ae0f719f | -5.8007 | -44.122799 | 2024-10-06 00:49:02 | METOP-B | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 347e707d-18f5-38b3-9225-c2919727c053 | -5.8048 | -44.1394 | 2024-10-06 00:49:02 | METOP-B | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| ce78f6a0-a0b3-3d09-a311-ac391c497a76 | -5.791 | -44.125198 | 2024-10-06 00:49:02 | METOP-B | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 4a9a8eea-54d8-3e0a-8a69-65325ed4abd7 | -6.5043 | -47.813702 | 2024-10-06 00:49:05 | METOP-B | SANTA TEREZINHA DO TOCANTINS | TOCANTINS | Brasil | 1720002 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| c9089e02-73bf-39bd-a0fc-68a3e4bc350b | -8.1144 | -55.289001 | 2024-10-06 00:49:06 | METOP-B | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| df9f49ae-6137-323b-b2e0-5ff7f0fca868 | -8.1163 | -55.297901 | 2024-10-06 00:49:06 | METOP-B | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2d9d51f7-4d28-3e66-83da-f66b1d6c8fc1 | -7.975 | -54.7388 | 2024-10-06 00:49:06 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 18d26b6c-acf8-3089-9317-297847b6f260 | -7.9768 | -54.747101 | 2024-10-06 00:49:06 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b6d393b4-5458-32f2-b36d-53006c6ddbc7 | -7.9786 | -54.755402 | 2024-10-06 00:49:06 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0f3eb874-55ad-3eb4-b360-352637eae912 | -7.9803 | -54.763599 | 2024-10-06 00:49:06 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c750102d-59c6-3641-b0d7-48d667c49c50 | -7.9652 | -54.741001 | 2024-10-06 00:49:06 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5bc76bba-c7d2-328b-b8b4-8887e0e1fe48 | -7.967 | -54.749298 | 2024-10-06 00:49:06 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 18e167c8-706a-3ab3-8c3c-eb98fe3e608a | -7.9688 | -54.7575 | 2024-10-06 00:49:06 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |


[Clique aqui para ver as próximas entradas](README14.md)
