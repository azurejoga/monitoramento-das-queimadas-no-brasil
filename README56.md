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

## Dados Diários - Página 56

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 42f8c72b-41da-3b62-a289-375451ea703e | -6.1412 | -51.75079 | 2025-09-06 04:38:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b256170e-8029-3728-aca1-d55890dd44b3 | -4.50581 | -42.88789 | 2025-09-06 04:38:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| e2dbabca-2a33-3abc-ab62-507ba007639d | -5.98405 | -53.59168 | 2025-09-06 04:38:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 5d9dbe80-b3c2-3050-8a78-263df90eab6b | -7.99266 | -45.47196 | 2025-09-06 04:38:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 071f95c6-e2cb-3a7e-b6e3-fdba68737639 | -7.32929 | -48.50059 | 2025-09-06 04:38:00 | NOAA-20 | ARAGUAÍNA | TOCANTINS | Brasil | 1702109 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| a127b262-54be-3314-9501-80e6b1f68cc6 | -8.7778 | -49.638 | 2025-09-06 04:38:00 | NOAA-20 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f1f4babb-3c64-3b63-80f3-4d459e509bf6 | -5.86038 | -49.57323 | 2025-09-06 04:38:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 45dfed4e-6d46-337b-8105-e86c7db05e6a | -3.7936 | -48.87241 | 2025-09-06 04:38:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 692424fc-f2b0-3da4-bdba-b9203153455d | -6.26541 | -53.44281 | 2025-09-06 04:38:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2cfc5046-07a4-344e-9c31-7230907b8f87 | -8.064 | -52.38554 | 2025-09-06 04:38:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| aee1f630-910a-371c-9d52-69804659ffdc | -6.48473 | -43.97694 | 2025-09-06 04:38:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 66974830-bd4b-304b-a185-495e65d0f7e2 | -6.87108 | -45.55429 | 2025-09-06 04:38:00 | NOAA-20 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 6251e067-39b7-3936-a25e-5413a7074961 | -2.55197 | -48.38808 | 2025-09-06 04:38:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 807c2bbd-1f59-3883-b87e-dd3ace9e92b0 | -7.05257 | -44.34965 | 2025-09-06 04:38:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 5.7 |
| fc3c9c9d-fd19-3736-99fe-5cb760624079 | -7.73002 | -50.31567 | 2025-09-06 04:38:00 | NOAA-20 | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| c6ecabd9-38a2-3bd8-ad29-6cf17c186c5d | -8.06666 | -52.36945 | 2025-09-06 04:38:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| edc422bc-9aa5-3a1f-89b9-59192a98e165 | -5.09733 | -56.14979 | 2025-09-06 04:38:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a73b7067-f30b-3063-80fd-6f04d22d5460 | -6.40886 | -43.81885 | 2025-09-06 04:38:00 | NOAA-20 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 154f63b1-ac26-37ce-bde8-113e74dadc68 | -8.54334 | -51.3429 | 2025-09-06 04:38:00 | NOAA-20 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 31811a5b-100b-3147-9302-630d49e1a84a | -5.98131 | -53.59388 | 2025-09-06 04:38:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| f74a0e78-7f69-3682-876a-44a27894f1a6 | -5.94371 | -45.65852 | 2025-09-06 04:38:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 698f7dfc-136d-3a4f-8ea6-51d5f435ee28 | -6.21969 | -43.58033 | 2025-09-06 04:38:00 | NOAA-20 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 93d6067b-4b1a-3857-b010-83ff89f9cc2e | -8.01773 | -45.43624 | 2025-09-06 04:38:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 4.7 |
| d093ae62-1217-373b-89a0-1c181530af63 | -3.25549 | -52.85651 | 2025-09-06 04:38:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2cb28208-6894-30cd-9c57-33f711cdaebd | -7.40934 | -44.94775 | 2025-09-06 04:38:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 9075982f-324b-3ef9-b967-1cd5ea670495 | -7.72946 | -50.31917 | 2025-09-06 04:38:00 | NOAA-20 | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| d253e13d-c310-33a1-90d0-b2258c5ced2c | -8.06759 | -52.34204 | 2025-09-06 04:38:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 72d6c08a-2d57-3ccb-a5e0-335c973d47c0 | -5.72579 | -49.28671 | 2025-09-06 04:38:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 09738e7c-376d-303a-bd3c-599e28c308f9 | -5.94765 | -53.80128 | 2025-09-06 04:38:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 9550c178-59bd-33f2-acad-5bda88528577 | -8.34065 | -47.48192 | 2025-09-06 04:38:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 43815b81-bb02-38de-8af7-6ee30191c55f | -6.40467 | -43.8182 | 2025-09-06 04:38:00 | NOAA-20 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 15bc7112-2a15-3420-bf1e-26baaaeffa46 | -5.89921 | -57.73629 | 2025-09-06 04:38:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 6632c8e4-4cb0-3910-b78d-ce19707babfe | -7.72395 | -50.31111 | 2025-09-06 04:38:00 | NOAA-20 | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| dc82d691-0b05-36d4-99df-b2e5cc9c3c10 | -8.77503 | -49.63399 | 2025-09-06 04:38:00 | NOAA-20 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 9b0c7b1b-18b4-3d9e-bc82-cb96f428b1ee | -8.35121 | -52.55587 | 2025-09-06 04:38:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 952750a6-36ba-3f13-b0a9-e76b4ac6efa9 | -7.33375 | -48.49399 | 2025-09-06 04:38:00 | NOAA-20 | ARAGUAÍNA | TOCANTINS | Brasil | 1702109 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| f176f24d-0690-3c87-9d03-c726f80db6c2 | -6.31974 | -58.17767 | 2025-09-06 04:38:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 11ce91f8-6691-39f9-ac39-0990556bd868 | -8.85543 | -52.01221 | 2025-09-06 04:38:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 06c04f6d-20af-361b-9bae-19dd7799e1ac | -6.51662 | -42.41214 | 2025-09-06 04:38:00 | NOAA-20 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| dece7b57-bb53-3c6f-adfa-7f908304ad89 | -6.32086 | -58.17132 | 2025-09-06 04:38:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e890f5d7-4396-3e16-a652-87b5b0c1c692 | -8.15493 | -54.92312 | 2025-09-06 04:38:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 51ff4317-f05c-37c4-9588-47a6abcddcff | -7.59084 | -46.21501 | 2025-09-06 04:38:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| eaac44f5-6fb3-3dee-a7b2-b09c3631db27 | -7.77346 | -51.08672 | 2025-09-06 04:38:00 | NOAA-20 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 7aa43889-87b4-3b1c-9b04-7b47bb271ead | -7.21362 | -43.98521 | 2025-09-06 04:38:00 | NOAA-20 | MARCOS PARENTE | PIAUÍ | Brasil | 2206001 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 0b50880d-1d83-3f74-b3d3-a2d6133e862b | -6.19645 | -53.2507 | 2025-09-06 04:38:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 1cd2d1d4-365f-3e3b-b511-9efc93f6d96e | -9.01696 | -49.80112 | 2025-09-06 04:38:00 | NOAA-20 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 11c4befc-c0b3-35ea-974b-11f0cdce819e | -7.34721 | -44.32012 | 2025-09-06 04:38:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f782200c-e8c6-3726-a693-8ef7dba37c96 | -8.06049 | -52.38502 | 2025-09-06 04:38:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 8.5 |
| ea070d75-0a05-3890-85f6-f55934c5bdbb | -9.07834 | -47.02636 | 2025-09-06 04:38:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 78809d48-3d7f-392e-89b9-413e3d511251 | -7.95867 | -44.94314 | 2025-09-06 04:38:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 197e4aa0-2866-3e02-bd33-bdc9d448d891 | -7.59316 | -44.68555 | 2025-09-06 04:38:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 65e21b2f-fdf9-3168-a704-62e0b41c1854 | -4.37238 | -48.06543 | 2025-09-06 04:38:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| bbef9d82-a107-3d22-aa6a-96086a76d353 | -7.60388 | -44.66907 | 2025-09-06 04:38:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d31d1f69-1a6c-3b58-b192-3b666ca2fb9b | -8.07788 | -50.19976 | 2025-09-06 04:38:00 | NOAA-20 | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 99260d11-cf4c-3a29-9aed-604e38b53e05 | -8.08754 | -45.31974 | 2025-09-06 04:38:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 2431de4c-1805-3cd5-a494-2f6a54dbf9b5 | -6.19347 | -53.24553 | 2025-09-06 04:38:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 3c8901f5-cb15-3bd9-90e1-51fd71a1ff8f | -5.21283 | -43.6994 | 2025-09-06 04:38:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| beedd93c-75d2-3feb-8c9e-2be5ecbcaf1b | -6.16979 | -44.30711 | 2025-09-06 04:38:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 85b6aeb0-0ecb-34f6-a729-2e2ab25c927a | -8.49335 | -45.06384 | 2025-09-06 04:38:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 50f7c176-a24b-357f-822c-e89004828c25 | -6.20971 | -43.40976 | 2025-09-06 04:38:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| b227baac-9e54-3889-864f-6256b55afb1b | -3.55442 | -52.99709 | 2025-09-06 04:38:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 9c50af3e-8778-3679-a0d1-b2a8f25caa80 | -5.90329 | -57.74282 | 2025-09-06 04:38:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 0.2 |
| 5096179f-e190-367b-86d2-670cb3e4a8a9 | -3.48314 | -48.94677 | 2025-09-06 04:38:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 2de03374-3a4a-321e-a53e-9b6ae366e312 | -5.06264 | -56.07602 | 2025-09-06 04:38:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 4d5e67b9-f727-3dc8-893a-ffc2de908afa | -5.72965 | -49.28378 | 2025-09-06 04:38:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| cfef6916-67b7-3f14-8640-77cd84292352 | -7.04792 | -44.35283 | 2025-09-06 04:38:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 2ae0075f-ecd4-3708-9212-f876387401ea | -8.35255 | -52.54777 | 2025-09-06 04:38:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 209676e3-3767-3762-8ede-9ccf487244ae | -4.98455 | -42.07264 | 2025-09-06 04:38:00 | NOAA-20 | CAMPO MAIOR | PIAUÍ | Brasil | 2202208 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 86c5a3e8-2712-3a0d-bece-8cbcb69a380b | -7.8023 | -45.42972 | 2025-09-06 04:38:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 8c1c6ac8-6a70-394e-a36f-cd8a05495e60 | -6.00053 | -46.68314 | 2025-09-06 04:38:00 | NOAA-20 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 63ef50ac-5d83-33fb-856a-26afca1d8709 | -8.87934 | -47.91682 | 2025-09-06 04:38:00 | NOAA-20 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 648ca9c1-3e47-3770-84b7-7fbe4669a60b | -5.57854 | -51.91532 | 2025-09-06 04:38:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d2c41a9d-d003-3558-9112-d38406ee65df | -3.75714 | -49.06065 | 2025-09-06 04:38:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| caf07fdd-e5d4-361a-a228-684f23fe4d2d | -7.00513 | -44.9472 | 2025-09-06 04:38:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| a75eb440-b131-3cee-a777-3f3e71be71cf | -5.01284 | -56.03539 | 2025-09-06 04:38:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 81668e57-aa36-3291-b6d6-492ed5fa8d1f | -3.67715 | -48.85765 | 2025-09-06 04:38:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 69b0196a-2ec6-3030-9788-7b115cd05a4a | -7.38237 | -48.18143 | 2025-09-06 04:38:00 | NOAA-20 | ARAGUAÍNA | TOCANTINS | Brasil | 1702109 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 70c16808-aded-3220-be16-cff38384197b | -6.73653 | -51.96953 | 2025-09-06 04:38:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 1c9dff4a-3e98-3fcd-8e44-7af3e6cf8bf6 | -8.36265 | -48.27422 | 2025-09-06 04:38:00 | NOAA-20 | PRESIDENTE KENNEDY | TOCANTINS | Brasil | 1718402 | 17 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 945d596d-b90f-3851-ac70-dea15bfcbad4 | -8.35926 | -48.27369 | 2025-09-06 04:38:00 | NOAA-20 | PRESIDENTE KENNEDY | TOCANTINS | Brasil | 1718402 | 17 | 33 | nan | nan | nan | Cerrado | 6.4 |
| b190d515-6fc9-3c7c-b096-32ff03c38598 | -7.33601 | -48.50158 | 2025-09-06 04:38:00 | NOAA-20 | ARAGUAÍNA | TOCANTINS | Brasil | 1702109 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 008b79fd-909f-3d4e-bfc9-37bbecc8fc5e | -8.67735 | -50.01788 | 2025-09-06 04:38:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 68b97497-36ae-380c-a5bf-1674ab337488 | -6.01345 | -46.69331 | 2025-09-06 04:38:00 | NOAA-20 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 4bb85bdd-3d24-3df1-be49-8a91a1bba03c | -1.34645 | -55.47532 | 2025-09-06 04:38:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| cc8adc4a-1685-3181-a14a-a6939c531abb | -7.68203 | -50.29688 | 2025-09-06 04:38:00 | NOAA-20 | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| b094fe38-e2ac-3d5c-bbd2-ff214d5df4c2 | -6.26995 | -53.43887 | 2025-09-06 04:38:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b880f15b-78af-3ef2-849c-6cee0752cd4b | -7.7245 | -50.30763 | 2025-09-06 04:38:00 | NOAA-20 | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 66c4ac8f-2c28-3410-8234-8050d4082330 | -6.15897 | -44.20979 | 2025-09-06 04:38:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 3d3ed490-b76d-3b68-a89c-ff6e98f2a754 | -4.30575 | -48.07661 | 2025-09-06 04:38:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e3b83489-3491-3037-9831-9cec90cbe29c | -5.87205 | -46.03947 | 2025-09-06 04:38:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 6fa9e6e8-fb67-3237-b715-dca9b1b9656f | -3.24386 | -50.7974 | 2025-09-06 04:38:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 523d70b7-7aff-352e-86f2-08633a18bf19 | -6.2059 | -42.62552 | 2025-09-06 04:38:00 | NOAA-20 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 60f84e09-33e5-3f39-86d4-1e5766e74aa7 | -8.15894 | -54.92389 | 2025-09-06 04:38:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a5a3bc5c-06c9-30df-a58f-72b26da2acbe | -6.91097 | -43.80951 | 2025-09-06 04:38:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 3763035d-60fd-3779-9b0f-7cd7eaf5a7d8 | -9.08273 | -46.99732 | 2025-09-06 04:38:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 548f3c51-0158-3e36-aa3a-b5e43e8b6e6d | -8.09288 | -55.728 | 2025-09-06 04:38:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3a12b041-be1c-3965-b3cd-43a08c5cecb4 | -5.9098 | -57.73516 | 2025-09-06 04:38:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 559bf271-3e14-3bc5-8239-1d9fe3de2b3d | -6.81942 | -52.81352 | 2025-09-06 04:38:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 1a0be624-8d33-38c6-8511-5a72ecf602f4 | -3.23742 | -50.0468 | 2025-09-06 04:38:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| b3e90e08-29a7-388d-aabd-36035b1dbbfd | -7.68258 | -50.29341 | 2025-09-06 04:38:00 | NOAA-20 | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |


[Clique aqui para ver as próximas entradas](README57.md)
