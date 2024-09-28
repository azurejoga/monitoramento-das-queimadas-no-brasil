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

## Dados Diários - Página 78

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 88bcd1db-dd07-38c3-8ca0-bba82ded25cf | -14.86807 | -51.53571 | 2024-09-28 05:10:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 3.2 |
| d5d5b276-3ec9-334f-be8e-4b26c77b4c27 | -14.86786 | -51.45889 | 2024-09-28 05:10:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 22.2 |
| 1ec3c072-c4fb-3d41-a8d7-834fbabae311 | -14.86745 | -51.46033 | 2024-09-28 05:10:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 20.1 |
| 2bdadcd5-5517-35cd-8d30-54236146d78e | -14.86743 | -51.54098 | 2024-09-28 05:10:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 12.3 |
| 015385c8-3e91-3f4d-9c0c-c2a92928a58a | -14.86718 | -51.46421 | 2024-09-28 05:10:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 22.2 |
| 53ef1c8a-a816-30a0-b392-476112f734a0 | -14.86679 | -51.54623 | 2024-09-28 05:10:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 12.3 |
| 558612a5-c599-34a3-ae6e-6d502b83e176 | -14.86616 | -51.5515 | 2024-09-28 05:10:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 10.2 |
| af7dbd96-acd7-32ad-875a-781f728e450b | -14.8633 | -51.53508 | 2024-09-28 05:10:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 0414a8a6-9825-306f-89ef-4671492910ff | -14.86203 | -51.54561 | 2024-09-28 05:10:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 12.3 |
| 8fb8a7a5-2116-3d49-b292-85da4df82c4d | -14.85944 | -51.40495 | 2024-09-28 05:10:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 6a8b5204-31a5-37ff-85e9-61919d2b1b36 | -14.85914 | -51.4484 | 2024-09-28 05:10:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 3bdab87b-03f8-34f2-ade8-1750201a2362 | -14.85896 | -51.45232 | 2024-09-28 05:10:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 9.0 |
| 49b2de5b-6ce0-3ba4-a904-c5bc056ed049 | -14.85477 | -51.40834 | 2024-09-28 05:10:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 3.0 |
| e811fedb-b31c-39c0-b531-d4a0ccd58f0a | -14.85463 | -51.40432 | 2024-09-28 05:10:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 17b36081-8653-32ff-a122-c2283dfa3906 | -14.854 | -51.40969 | 2024-09-28 05:10:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 25b0d23f-5125-366c-93ed-e62a572199fc | -14.85064 | -51.40236 | 2024-09-28 05:10:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 4a2bcbcc-e57b-3dcf-920d-75bf86b035f0 | -14.84997 | -51.40772 | 2024-09-28 05:10:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 8b56b718-9f80-3994-9f53-773bca7e532c | -14.84982 | -51.4037 | 2024-09-28 05:10:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 59a0d5a3-b278-3555-af92-77987cf7e543 | -14.84583 | -51.40174 | 2024-09-28 05:10:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 86f7d3f4-dbc1-3d5c-8c0c-521ca6c92d8d | -14.8294 | -51.41594 | 2024-09-28 05:10:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 12.8 |
| 25e49fcf-e100-32af-873a-f6b207dbd470 | -14.82593 | -51.40458 | 2024-09-28 05:10:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 11.4 |
| b926d3ee-e438-3679-bbff-c474c5b0d4f2 | -14.82527 | -51.40995 | 2024-09-28 05:10:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 10.2 |
| fd228d64-cabc-34fc-9662-5ce6c097719d | -14.82394 | -51.42065 | 2024-09-28 05:10:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 499359ef-a685-3010-9049-206ea0e55161 | -14.82327 | -51.42599 | 2024-09-28 05:10:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 6.4 |
| debf326a-ac3a-35bb-a734-f501b5024849 | -14.82046 | -51.40932 | 2024-09-28 05:10:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 10.2 |
| 8f017fe3-50ed-3fd2-bb16-2a74db6b02b2 | -14.81914 | -51.42002 | 2024-09-28 05:10:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 6.4 |
| f9454dfa-0dab-3509-a6ff-0a56370d6841 | -14.81566 | -51.40871 | 2024-09-28 05:10:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 3.9 |
| a6c0970a-4360-3e34-9719-35834167e5c8 | -9.3492 | -50.75068 | 2024-09-28 05:10:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 24e966a9-d6c2-3709-9cc6-538b03332f70 | -9.34852 | -50.75557 | 2024-09-28 05:10:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| cd5863d1-1bfd-3e9e-85ba-aa1067725966 | -9.34591 | -50.74026 | 2024-09-28 05:10:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 894798d1-8049-358f-875f-b8d75ca9fd2a | -9.34522 | -50.74521 | 2024-09-28 05:10:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 8c071b2d-7389-344c-89f1-d38ec2f9a622 | -9.34452 | -50.75025 | 2024-09-28 05:10:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| b940360d-bede-3218-8386-96c0ae8ad6a8 | -9.34382 | -50.75527 | 2024-09-28 05:10:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 8ce8d0b4-27e8-3f81-9e0c-9499c41b791e | -9.34051 | -50.74499 | 2024-09-28 05:10:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 39df72a4-2616-36d3-8063-3556f14efcf8 | -9.33651 | -50.73968 | 2024-09-28 05:10:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| c8cc27d7-f041-3a51-841c-7425f02d9e8f | -9.33379 | -50.75937 | 2024-09-28 05:10:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 9a78af12-972e-3ef6-a221-b70ff3291490 | -9.31259 | -50.776 | 2024-09-28 05:10:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| e2306442-4d46-32c5-858c-f278ee65fa89 | -9.30793 | -50.7755 | 2024-09-28 05:10:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| f5168e44-ed82-3b07-92bb-4c85051308c5 | -9.29866 | -50.77416 | 2024-09-28 05:10:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| f2684410-22d4-3f77-933a-5d56abe057c2 | -9.03855 | -51.52628 | 2024-09-28 05:10:00 | NOAA-20 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 7f75e676-2980-3ee3-9a6e-9c9fbf3ce19b | -9.03795 | -51.53049 | 2024-09-28 05:10:00 | NOAA-20 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 27244a32-c193-3193-bdb3-bb600ef423f5 | -9.03353 | -51.5301 | 2024-09-28 05:10:00 | NOAA-20 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ff9e6d9e-99c6-3208-829a-12c03888f161 | -9.52968 | -51.37742 | 2024-09-28 05:10:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| c9e2a38f-8741-3911-9fc8-c3f93d9c199a | -9.45106 | -51.46419 | 2024-09-28 05:10:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| f3387e7a-b430-33d6-9571-5e4a0a44b0f1 | -9.44722 | -51.45937 | 2024-09-28 05:10:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 8a55b3ba-682c-31dc-a9ed-bde19714be59 | -9.44337 | -51.45457 | 2024-09-28 05:10:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 372df7a7-a94e-36af-bdac-d7ea34a7d6ca | -9.43891 | -51.45409 | 2024-09-28 05:10:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| e9ea54c6-b4b5-3188-9621-62f69495f256 | -9.4345 | -51.45332 | 2024-09-28 05:10:00 | NOAA-20 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 3867285e-6082-3206-a920-ad5a40b43804 | -9.40732 | -51.45382 | 2024-09-28 05:10:00 | NOAA-20 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 3b22a36b-e57a-3e47-8557-020c929ad665 | -9.40291 | -51.45303 | 2024-09-28 05:10:00 | NOAA-20 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| d8b38386-e176-33d4-92ec-c25546eb901c | -10.45147 | -50.79111 | 2024-09-28 05:10:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b64a6cc6-2380-3e04-b3fa-7281d6cfafa5 | -10.45009 | -50.80115 | 2024-09-28 05:10:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 646623fe-4483-3571-a531-9235b496d224 | -10.85086 | -51.06706 | 2024-09-28 05:10:00 | NOAA-20 | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c5566442-8c42-391f-9454-3ab89855e69b | -10.60982 | -51.09709 | 2024-09-28 05:10:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 8bab58a9-b619-356f-92c3-769e16c1599f | -10.60915 | -51.09407 | 2024-09-28 05:10:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 585605b3-8563-325c-ac23-ce32a10ea794 | -10.60586 | -51.09163 | 2024-09-28 05:10:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 5.0 |
| a78b320b-e2c0-3ae0-846e-bec7ea7a87b1 | -10.60519 | -51.09647 | 2024-09-28 05:10:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 7c657708-3688-3d3f-aff2-57b483c3c146 | -10.60452 | -51.09344 | 2024-09-28 05:10:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 8a331593-3e57-3a16-8ed9-d5bd3383cdf9 | -10.60057 | -51.09584 | 2024-09-28 05:10:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 4252e8d3-a42c-3a47-ae21-81adc18dbbd8 | -10.59991 | -51.10069 | 2024-09-28 05:10:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 3.6 |
| e43912b4-b26a-37d3-a673-3e4aea8f662f | -10.59528 | -51.10006 | 2024-09-28 05:10:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f705f163-ec83-314a-be74-69844b8b8134 | -10.54374 | -51.09846 | 2024-09-28 05:10:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 4.2 |
| a5fd1b7e-dd58-3587-ad84-d9b92a1b2430 | -10.5431 | -51.10323 | 2024-09-28 05:10:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 4.3 |
| df5de87f-b240-32f1-9a28-7bd404d7f79d | -10.53846 | -51.10279 | 2024-09-28 05:10:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 9614ef7f-b82e-3d12-8d8a-ce63cdc1b443 | -10.53375 | -51.10286 | 2024-09-28 05:10:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| c31c2f0f-48a1-3244-9041-68e6ada855a4 | -10.52839 | -51.10781 | 2024-09-28 05:10:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 3.4 |
| f1f5fbc4-7a5b-317a-8c86-ccd92a09c1b4 | -10.49981 | -51.1468 | 2024-09-28 05:10:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 9b2fca75-5ff8-3d7f-b948-4fc2e79c96ff | -10.48998 | -51.15031 | 2024-09-28 05:10:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| b17dcc92-7d75-31b5-a234-277bbcf8bd06 | -10.48969 | -51.15375 | 2024-09-28 05:10:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 4734842c-af5e-319e-9592-0b64ad97656d | -10.48934 | -51.15527 | 2024-09-28 05:10:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 3.9 |
| e95a60b8-3a2f-350a-bb8f-940c0875bf0f | -10.48512 | -51.15291 | 2024-09-28 05:10:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 3962f079-10a9-3f0a-a82b-ff40cac0f048 | -10.47134 | -51.18513 | 2024-09-28 05:10:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 4.1 |
| a1a70d00-5a67-3f42-847d-918bf0080c62 | -11.02636 | -51.33005 | 2024-09-28 05:10:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 3d950da4-4a17-30f8-82d1-044f50350452 | -11.01532 | -51.34198 | 2024-09-28 05:10:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d5ab5723-aee6-33c2-b410-a902be8ae936 | -11.09913 | -50.80732 | 2024-09-28 05:10:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 8450bb5d-3b57-3313-80a4-8675c73d9c38 | -13.63479 | -51.46838 | 2024-09-28 05:10:00 | NOAA-20 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 3.6 |
| b1b5baea-d6a4-3b4b-8bbc-9cdf488f3195 | -13.63414 | -51.47347 | 2024-09-28 05:10:00 | NOAA-20 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 00e0353c-1d5a-3688-baa9-345b41d53b99 | -13.63349 | -51.47855 | 2024-09-28 05:10:00 | NOAA-20 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 2e3c7557-babf-3c91-897d-5d48daa7da09 | -13.62944 | -51.47285 | 2024-09-28 05:10:00 | NOAA-20 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 23172f56-d177-3789-a6cc-7fb6d196ce7b | -13.62879 | -51.47793 | 2024-09-28 05:10:00 | NOAA-20 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 3.0 |
| ed030a86-922b-34da-8ee0-b66783974e7a | -13.25241 | -51.29472 | 2024-09-28 05:10:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| b47efbc9-561c-38f5-ba86-89ff5b131eea | -13.23269 | -51.26059 | 2024-09-28 05:10:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 3.6 |
| b15c353f-902d-3c0f-9170-973df95c4ca5 | -13.23203 | -51.26577 | 2024-09-28 05:10:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 0a05f3bb-e697-3485-975d-fe09ec244479 | -13.23137 | -51.27093 | 2024-09-28 05:10:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d39d14d3-3449-33b0-849b-5651495cb957 | -13.23071 | -51.27611 | 2024-09-28 05:10:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 540c0b41-1acc-367b-a1bf-feb220df2800 | -13.22386 | -51.25412 | 2024-09-28 05:10:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 0938dbbb-ba24-32c9-a0e1-289f7da4cc89 | -13.2232 | -51.25933 | 2024-09-28 05:10:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 3.0 |
| a2079e07-ae9c-3015-b057-82ba6ea7b5f3 | -13.21093 | -51.24184 | 2024-09-28 05:10:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 4.6 |
| a3f0005e-4519-3cc1-9556-20bedac6ec14 | -13.21027 | -51.24705 | 2024-09-28 05:10:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 5ac16c6d-a05f-3c0e-83de-ab956fc1349c | -13.20683 | -51.23603 | 2024-09-28 05:10:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 3c71943e-698e-396a-8b7b-f8a6895effb3 | -13.20617 | -51.24123 | 2024-09-28 05:10:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 6bf927b7-d7e4-3a38-8129-1005578867c8 | -13.20552 | -51.24641 | 2024-09-28 05:10:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 76ab7734-f540-32ca-b238-ff4a802e684e | -16.09901 | -51.93552 | 2024-09-28 05:10:00 | NOAA-20 | BOM JARDIM DE GOIÁS | GOIÁS | Brasil | 5203401 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| f9d0ed62-2868-3934-b435-2d467a28bbf6 | -9.11046 | -53.29382 | 2024-09-28 05:10:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 787ee51b-d5fc-36de-b7da-7ce8e3339d74 | -8.89157 | -53.03672 | 2024-09-28 05:10:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 6617b7f6-1700-33d5-b113-d2f2527cf153 | -8.8876 | -53.03623 | 2024-09-28 05:10:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0a7714a0-0b73-3420-bdad-26eeb86b4bf0 | -8.88435 | -53.03073 | 2024-09-28 05:10:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e68d50e3-2b63-3ecf-880e-91039173f976 | -8.88364 | -53.03569 | 2024-09-28 05:10:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| cf38ca61-cc42-3518-9f40-4c9e6e2d7e09 | -9.77104 | -53.54572 | 2024-09-28 05:10:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| bda324fe-fcc9-3699-89ed-0ca92694c7a9 | -9.76716 | -53.54514 | 2024-09-28 05:10:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |


[Clique aqui para ver as próximas entradas](README79.md)
