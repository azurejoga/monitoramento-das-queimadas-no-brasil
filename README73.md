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

## Dados Diários - Página 73

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 3f3cc2e4-610e-36b9-9f2f-dd6f9fc537bd | -4.29502 | -48.07372 | 2024-11-27 04:42:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 08c5ead7-6fc8-3abc-beb7-dfa45cf5440e | -0.99568 | -51.7294 | 2024-11-27 04:42:00 | NOAA-20 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 5e91e4b8-f82e-3828-9f1a-dacafdf29be2 | -4.81292 | -46.84381 | 2024-11-27 04:42:00 | NOAA-20 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 4.3 |
| f3bbf4c0-e5d2-3d7d-99a9-c1f43e8bcb81 | -3.32854 | -51.63498 | 2024-11-27 04:42:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| fd42dd24-9603-3923-83e9-6b66d51df23f | -4.27485 | -48.61766 | 2024-11-27 04:42:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| d43d4250-f537-38d6-8d8e-cec19a9eae48 | -2.43732 | -50.4182 | 2024-11-27 04:42:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 85a75b23-8524-332c-8847-2527dadd4770 | -3.06997 | -50.95252 | 2024-11-27 04:42:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d2f1b0c9-41d8-3884-913a-4766fc867c20 | -5.98776 | -45.3681 | 2024-11-27 04:42:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 29.8 |
| 8b10f0c2-38d8-35c2-84fa-55d21161f5a2 | -2.94513 | -48.56253 | 2024-11-27 04:42:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 34827487-5f1f-3a4c-8ebe-746ab46a58ca | -3.2342 | -50.19101 | 2024-11-27 04:42:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 33c520e4-87e4-3765-9c37-e3e2e6e3d815 | -2.49721 | -54.53355 | 2024-11-27 04:42:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 89fbba0b-36f1-3392-b353-1258608fd3f2 | -3.77773 | -49.93042 | 2024-11-27 04:42:00 | NOAA-20 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1c1e81ba-c880-39d4-8eb2-8444fefde18d | -3.38436 | -45.85371 | 2024-11-27 04:42:00 | NOAA-20 | GOVERNADOR NEWTON BELLO | MARANHÃO | Brasil | 2104651 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7d39b8c3-6744-3cc4-90e5-d7a69bc39399 | -2.53561 | -47.32669 | 2024-11-27 04:42:00 | NOAA-20 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 3246b487-51c3-3a48-8044-7c17733e431c | -5.9836 | -45.36748 | 2024-11-27 04:42:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 29.8 |
| c3937089-839c-35a4-a5f0-410e50e63ff4 | -1.68545 | -52.5319 | 2024-11-27 04:42:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 25eb92e2-d382-3390-b1bd-ead7fd790b36 | -3.27073 | -43.0425 | 2024-11-27 04:42:00 | NOAA-20 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 38c7f4e5-4985-3d95-bf6d-02db55c2c7c7 | -0.87764 | -51.72283 | 2024-11-27 04:42:00 | NOAA-20 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 52ee5dcf-2fc3-3b1c-8896-464484274328 | -6.82773 | -44.39798 | 2024-11-27 04:44:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| a78927cb-f5ad-3885-8166-edc6b552ab7a | -12.02859 | -49.54414 | 2024-11-27 04:44:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 7660a5fd-114d-3101-b8cc-e19c5076af6b | -6.38107 | -45.68349 | 2024-11-27 04:44:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ea007f5a-e335-302a-8a48-656c9d287c69 | -12.018 | -49.54257 | 2024-11-27 04:44:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 520534b3-3319-30b8-b15b-b7c9e4826369 | -12.02918 | -49.5401 | 2024-11-27 04:44:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| e7e21a2b-2529-3594-a650-55c8318c373f | -7.68516 | -49.12359 | 2024-11-27 04:44:00 | NOAA-20 | ARAPOEMA | TOCANTINS | Brasil | 1702307 | 17 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 901509ba-51e1-3b92-a820-f0d4115f528a | -12.68296 | -52.26873 | 2024-11-27 04:44:00 | NOAA-20 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| e3e74328-6ce3-3e05-a026-397276edda64 | -7.85623 | -48.71547 | 2024-11-27 04:44:00 | NOAA-20 | BANDEIRANTES DO TOCANTINS | TOCANTINS | Brasil | 1703057 | 17 | 33 | nan | nan | nan | Amazônia | 0.7 |
| f8aaa58e-83bc-3ad9-a7a9-b22e559839b6 | -9.81493 | -48.16362 | 2024-11-27 04:44:00 | NOAA-20 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 916f11d2-1329-3f44-86fe-9937d0f2d707 | -9.81429 | -48.16804 | 2024-11-27 04:44:00 | NOAA-20 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| de3ec802-5e56-3511-85d0-5a5e0f9d1680 | -5.93848 | -50.16467 | 2024-11-27 04:44:00 | NOAA-20 | PARAUAPEBAS | PARÁ | Brasil | 1505536 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 2fb128bc-afa2-3809-8b49-f73dbbe8440c | -7.54446 | -47.58742 | 2024-11-27 04:44:00 | NOAA-20 | BARRA DO OURO | TOCANTINS | Brasil | 1703073 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 22f60e15-209b-3917-a453-9fc3f4324ae4 | -9.82166 | -48.16919 | 2024-11-27 04:44:00 | NOAA-20 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| bc73cb61-3acf-3770-8d0c-355a6c8ede25 | -6.83224 | -44.39857 | 2024-11-27 04:44:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| e6f10412-fe40-3585-b7b7-fd6c6bba54dd | -6.6989 | -47.26831 | 2024-11-27 04:44:00 | NOAA-20 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| fcaed119-6d78-340f-b52b-bb4077e39029 | -11.41783 | -55.6624 | 2024-11-27 04:44:00 | NOAA-20 | SINOP | MATO GROSSO | Brasil | 5107909 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 54dd34d3-2c64-38bc-ac20-5b90516e2977 | -6.99189 | -45.62393 | 2024-11-27 04:44:00 | NOAA-20 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 0.3 |
| 08964e4b-61ad-3e8c-8e49-9278c3c18880 | -7.68458 | -49.12738 | 2024-11-27 04:44:00 | NOAA-20 | ARAPOEMA | TOCANTINS | Brasil | 1702307 | 17 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 5cf4aeb6-51a0-3005-88a5-fe5e55586d41 | -8.13255 | -44.46809 | 2024-11-27 04:44:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d34bf16f-68b3-31c1-9327-d433d6b55a7a | -7.98327 | -49.69268 | 2024-11-27 04:44:00 | NOAA-20 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| ba350186-dfd7-3937-9b6a-619918ba2b62 | -9.59476 | -49.52514 | 2024-11-27 04:44:00 | NOAA-20 | DIVINÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1707108 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| e711d4eb-8cac-36bb-b684-0626926ba6de | -7.80716 | -50.76776 | 2024-11-27 04:44:00 | NOAA-20 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| cc88a999-6d40-3a01-99c2-6996d150df39 | -6.37642 | -45.68656 | 2024-11-27 04:44:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a054c3b7-ab2d-32b4-9ae6-2288cb848423 | -6.34689 | -47.30906 | 2024-11-27 04:44:00 | NOAA-20 | PORTO FRANCO | MARANHÃO | Brasil | 2109007 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| c86a82a9-5400-3ce5-a670-708352d4076b | -6.38052 | -45.68714 | 2024-11-27 04:44:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 1629bca5-7db7-3e39-8751-a7f2e0d8f664 | -10.70032 | -49.41932 | 2024-11-27 04:44:00 | NOAA-20 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a6839b30-9611-3e93-b63e-35e5ac24f89d | -5.59544 | -49.86092 | 2024-11-27 04:44:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 79a59a86-e851-3523-ba7d-c23d1aee34ce | -6.13184 | -46.9185 | 2024-11-27 04:44:00 | NOAA-20 | LAJEADO NOVO | MARANHÃO | Brasil | 2105989 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| cdb42bd6-997f-3090-aaae-0b8d061aa42c | -6.8329 | -44.39401 | 2024-11-27 04:44:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 7c97370a-d48d-3d0b-a187-e5de6bfb891d | -10.53038 | -49.05365 | 2024-11-27 04:44:00 | NOAA-20 | NOVA ROSALÂNDIA | TOCANTINS | Brasil | 1715002 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| e75db6c0-ea42-388a-8b83-da48d4367dd5 | -12.68627 | -52.26926 | 2024-11-27 04:44:00 | NOAA-20 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 6a211d5c-b07a-35ce-8a8c-cae415c2fdd5 | -9.81366 | -48.17243 | 2024-11-27 04:44:00 | NOAA-20 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 000a49c3-1b83-3db3-9c54-dfa1369ea3e6 | -9.12308 | -47.7094 | 2024-11-27 04:44:00 | NOAA-20 | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 45a56c99-c7af-31c8-af4d-ed76f82b8463 | -12.33645 | -49.99625 | 2024-11-27 04:44:00 | NOAA-20 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 9b944486-8877-3fe1-961f-e2d63e5b4034 | -9.73315 | -48.05844 | 2024-11-27 04:44:00 | NOAA-20 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 21d4e82f-e741-39aa-a6b9-b81a5b8e8271 | -7.69294 | -42.97128 | 2024-11-27 04:44:00 | NOAA-20 | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 4.6 |
| 113b614e-072c-331d-b769-8c1771eb7d3f | -9.8409 | -48.1404 | 2024-11-27 04:44:00 | NOAA-20 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| c1ed4aa6-2ce0-382d-934d-66ef8f2eb086 | -9.72517 | -50.3477 | 2024-11-27 04:44:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6fa09e75-d4a3-369e-b7b7-7021a00d5191 | -8.13188 | -44.47287 | 2024-11-27 04:44:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 20e726d3-b37b-306f-92a9-fe49dbe3d579 | -7.68749 | -42.97357 | 2024-11-27 04:44:00 | NOAA-20 | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 259658ba-7ad0-367b-8bbd-eb236b379300 | -8.65575 | -49.14064 | 2024-11-27 04:44:00 | NOAA-20 | COUTO MAGALHÃES | TOCANTINS | Brasil | 1706001 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 2774ae5a-75b1-3ea6-a7f7-2c2c11b82ff6 | -7.69253 | -42.97424 | 2024-11-27 04:44:00 | NOAA-20 | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 4.6 |
| 1c077cd0-fdcc-3943-8bf3-240b1bd54490 | -10.75967 | -47.51688 | 2024-11-27 04:44:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| bf91f1d8-0f69-3ac4-a5c0-e8050eb680b9 | -6.99603 | -45.62458 | 2024-11-27 04:44:00 | NOAA-20 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 0.3 |
| c9cdf331-fb4c-3977-a6ab-ee79cc6f1bf0 | -12.02153 | -49.54309 | 2024-11-27 04:44:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 7a7a997f-4c42-3af9-8709-d7f647b81af1 | -9.72854 | -50.34821 | 2024-11-27 04:44:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b57f4e21-21c9-325c-adc2-d0ec790207de | -9.25272 | -50.66302 | 2024-11-27 04:44:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 71283ea1-551d-339d-89db-602d325008bb | -8.57188 | -49.20267 | 2024-11-27 04:44:00 | NOAA-20 | COUTO MAGALHÃES | TOCANTINS | Brasil | 1706001 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c0ffe767-c2ff-39da-b464-1e46537db02c | -6.38028 | -45.683 | 2024-11-27 04:44:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 4f6b85c9-647c-3106-aab3-5148eec30d4b | -7.69212 | -42.97718 | 2024-11-27 04:44:00 | NOAA-20 | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 5.4 |
| faa4e154-bcf2-3c9f-a49b-30318c96c3be | -6.38441 | -47.17201 | 2024-11-27 04:44:00 | NOAA-20 | PORTO FRANCO | MARANHÃO | Brasil | 2109007 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 528dbc55-e5e6-3293-a4fe-d84a277125f4 | -10.9411 | -49.42591 | 2024-11-27 04:44:00 | NOAA-20 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| b4198ad0-9a12-3704-b385-b433b824a89e | -8.40171 | -49.17453 | 2024-11-27 04:44:00 | NOAA-20 | COUTO MAGALHÃES | TOCANTINS | Brasil | 1706001 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 68324b8d-84e7-330a-93b5-1d89c2cc69c3 | -12.68351 | -52.2652 | 2024-11-27 04:44:00 | NOAA-20 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 7d1593b5-0284-38e7-a53b-14bfc775f67f | -5.57793 | -49.45273 | 2024-11-27 04:44:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 56a0a7b1-2ee8-3fc3-b23a-94f80c9ca756 | -6.36877 | -47.35511 | 2024-11-27 04:44:00 | NOAA-20 | PORTO FRANCO | MARANHÃO | Brasil | 2109007 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 3a0b0564-889b-3edd-9fdd-eb9e0c9e6db3 | -7.6879 | -42.97065 | 2024-11-27 04:44:00 | NOAA-20 | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 8fe3068a-b03d-3d8f-98f8-f97556c99e47 | -6.13253 | -46.91392 | 2024-11-27 04:44:00 | NOAA-20 | LAJEADO NOVO | MARANHÃO | Brasil | 2105989 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 279b3b5e-fe8f-3470-b9b9-708bedef9c84 | -6.69438 | -43.0635 | 2024-11-27 04:44:00 | NOAA-20 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 59ba58e1-1d67-3621-b11f-5e0f18cf7b06 | -8.39824 | -49.174 | 2024-11-27 04:44:00 | NOAA-20 | COUTO MAGALHÃES | TOCANTINS | Brasil | 1706001 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 81f1cdca-25f1-3bf1-b344-b650ba31eadd | -7.22345 | -45.30728 | 2024-11-27 04:44:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 70d1348e-e341-332d-bcac-8df6ed58cb62 | -9.84459 | -48.14097 | 2024-11-27 04:44:00 | NOAA-20 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| d1fcb371-b606-3ada-8262-8778a967724f | -7.54512 | -47.58297 | 2024-11-27 04:44:00 | NOAA-20 | BARRA DO OURO | TOCANTINS | Brasil | 1703073 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| cf8a17f4-c7a5-3da0-891d-4e1ec563f180 | -8.13578 | -44.47821 | 2024-11-27 04:44:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 80fb81a9-ba0c-3ba4-9bf8-edc88f8e5a73 | -10.69908 | -49.4204 | 2024-11-27 04:44:00 | NOAA-20 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 3a99edc5-fa31-32e0-aada-6992b1432929 | -8.79841 | -48.74775 | 2024-11-27 04:44:00 | NOAA-20 | COLMÉIA | TOCANTINS | Brasil | 1716703 | 17 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4b3bd096-3a2b-3395-bcc3-d96d1eed1dcf | -7.85331 | -48.71106 | 2024-11-27 04:44:00 | NOAA-20 | BANDEIRANTES DO TOCANTINS | TOCANTINS | Brasil | 1703057 | 17 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 5a8244c7-0952-328c-9294-71cca8a1ec91 | -7.85682 | -48.71157 | 2024-11-27 04:44:00 | NOAA-20 | BANDEIRANTES DO TOCANTINS | TOCANTINS | Brasil | 1703057 | 17 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 0d67ebd5-a288-3688-a49c-1bcc710ea4f1 | -6.38385 | -45.68724 | 2024-11-27 04:44:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| b1e7b4fe-72c6-34af-a8ce-8081eb3b73dc | -9.59189 | -49.52078 | 2024-11-27 04:44:00 | NOAA-20 | DIVINÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1707108 | 17 | 33 | nan | nan | nan | Cerrado | 0.4 |
| dda17093-d163-36be-971c-68c3c7642457 | -8.57245 | -49.19884 | 2024-11-27 04:44:00 | NOAA-20 | COUTO MAGALHÃES | TOCANTINS | Brasil | 1706001 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d54a0e76-c821-39ce-b5da-74bc3de2fdbc | -8.13645 | -44.47346 | 2024-11-27 04:44:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 4.0 |
| b7bfe6c1-402f-3408-806b-9a91fc90dd2e | -6.37975 | -45.68665 | 2024-11-27 04:44:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a6c5b7a2-df4d-373d-9533-75241ab39a20 | -8.1312 | -44.47769 | 2024-11-27 04:44:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| dbb4e420-920b-3f43-a6b7-a9aa3bba0d23 | -6.687 | -48.87227 | 2024-11-27 04:44:00 | NOAA-20 | PIÇARRA | PARÁ | Brasil | 1505635 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| be5ea8c3-73a3-3728-90df-c08f96543593 | -9.27045 | -50.63675 | 2024-11-27 04:44:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| e423f77b-39f6-3646-836e-1a70dd516445 | -17.79745 | -52.048 | 2024-11-27 04:46:00 | NOAA-20 | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 0.5 |
| cde90cbb-6aef-34d6-b82d-d110294cd7a3 | -17.77915 | -42.80955 | 2024-11-27 04:46:00 | NOAA-20 | ITAMARANDIBA | MINAS GERAIS | Brasil | 3132503 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| a8cdcca4-9889-311f-b60e-2145af6b544d | -19.76651 | -48.93665 | 2024-11-27 04:46:00 | NOAA-20 | COMENDADOR GOMES | MINAS GERAIS | Brasil | 3116902 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 22bfc7bf-b0c4-3d95-b93a-0e9c9788ded4 | -16.84099 | -46.66872 | 2024-11-27 04:46:00 | NOAA-20 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 54e960d7-99f1-350e-98b4-647b8ddfb6b1 | -20.38231 | -47.47807 | 2024-11-27 04:46:00 | NOAA-20 | CRISTAIS PAULISTA | SÃO PAULO | Brasil | 3513207 | 35 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 6690c029-b679-3df2-9bea-11c28d62ad9c | -15.89089 | -43.46374 | 2024-11-27 04:46:00 | NOAA-20 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 5.3 |


[Clique aqui para ver as próximas entradas](README74.md)
