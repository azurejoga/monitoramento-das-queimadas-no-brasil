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

## Dados Diários - Página 12

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| a53d66fa-9b29-3edd-a20a-e2a302766138 | -5.53274 | -44.34517 | 2025-09-11 03:53:00 | NOAA-21 | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 10.1 |
| 19fed04b-b70d-3863-8e6a-9d6acf4409a6 | -5.07936 | -41.14949 | 2025-09-11 03:53:00 | NOAA-21 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| fa225a9e-474c-3790-8011-61b6c4c23222 | -5.34345 | -44.80436 | 2025-09-11 03:53:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 2a968ffe-5d59-3215-ae32-3a0b6da4dd6c | -5.5271 | -44.35268 | 2025-09-11 03:53:00 | NOAA-21 | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 39f3e3e1-afcc-3872-9653-242165e03071 | -4.71517 | -47.235 | 2025-09-11 03:53:00 | NOAA-21 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c95ccb9c-5e1b-3315-a2be-95b423a90513 | -5.24001 | -45.46005 | 2025-09-11 03:53:00 | NOAA-21 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| e1c93487-2e9e-33cb-85d5-53a2895fc740 | -5.339 | -44.8036 | 2025-09-11 03:53:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| a4e3cd14-421a-3620-8fe7-48b14fe22563 | -4.71455 | -44.94695 | 2025-09-11 03:53:00 | NOAA-21 | POÇÃO DE PEDRAS | MARANHÃO | Brasil | 2108900 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 9eb93a6a-2870-306c-852e-8173d3ae1964 | -5.66245 | -43.89921 | 2025-09-11 03:53:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 46f58cdf-a7bb-34a7-bd17-3c7beb149c07 | -5.55782 | -43.04605 | 2025-09-11 03:53:00 | NOAA-21 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| da22ad69-a73a-32b6-99ad-784700945387 | -3.08271 | -48.81667 | 2025-09-11 03:53:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| ac063083-4eb4-34f5-9bb2-f4502bfab5bf | -3.24687 | -50.80521 | 2025-09-11 03:53:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 2a1e23f3-1e19-3537-9f6e-e7ef2e06c054 | -5.12297 | -44.66821 | 2025-09-11 03:53:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| d282dc9a-9341-3638-8ed4-edd7a80b1eb7 | -2.22263 | -48.22582 | 2025-09-11 03:53:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 8.5 |
| eef457c2-080f-347f-8d78-1083b8b23c0f | -5.79806 | -35.58015 | 2025-09-11 03:53:00 | NOAA-21 | IELMO MARINHO | RIO GRANDE DO NORTE | Brasil | 2404606 | 24 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 34d5dc68-df7e-35b3-9fbd-930256a4c78f | -4.86695 | -42.76746 | 2025-09-11 03:53:00 | NOAA-21 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Cerrado | 20.3 |
| 9e6b4355-98ac-3cc8-812a-e3b5ea34d75e | -5.45447 | -43.99978 | 2025-09-11 03:53:00 | NOAA-21 | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 81818e4e-3a94-325e-a912-3b90da0ad2bd | -3.6029 | -42.85963 | 2025-09-11 03:53:00 | NOAA-21 | BREJO | MARANHÃO | Brasil | 2102101 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 0c7bb300-b1b3-358d-8ac8-52180df205d7 | -5.2494 | -45.9746 | 2025-09-11 03:53:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 847c188a-0dda-315d-9cfd-749798f7ad75 | -4.55937 | -43.74227 | 2025-09-11 03:53:00 | NOAA-21 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 9fe480bf-4210-35d1-9b27-0dc2ac9b3fcf | -5.5741 | -43.44739 | 2025-09-11 03:53:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 3ad8a8b2-7327-36a5-b0c0-1660e53760c7 | -6.99006 | -35.14841 | 2025-09-11 03:53:00 | NOAA-21 | SAPÉ | PARAÍBA | Brasil | 2515302 | 25 | 33 | nan | nan | nan | Mata Atlântica | 2.9 |
| 55b97f1e-0f60-3a65-ab32-e82306e3ec5b | -5.23122 | -46.09093 | 2025-09-11 03:53:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 912333a6-88cf-3c1a-978c-ae458d357176 | -4.65277 | -47.03544 | 2025-09-11 03:53:00 | NOAA-21 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 4153db9e-5310-3321-8f4a-a645e1638dd8 | -3.08193 | -48.82125 | 2025-09-11 03:53:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 7d9ce32f-801d-3057-b326-37406dad83fe | -5.54854 | -43.80317 | 2025-09-11 03:53:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| a495bf8f-9ca9-3972-9c62-192d7837b519 | -4.96 | -43.22295 | 2025-09-11 03:53:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a16b399d-48bc-305f-b072-3361e19bfbd9 | -4.21782 | -46.36389 | 2025-09-11 03:53:00 | NOAA-21 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 65b0bc29-b412-395c-a163-37ea0b9bcc08 | -4.2188 | -46.36295 | 2025-09-11 03:53:00 | NOAA-21 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 9.0 |
| 8fb62b9b-4708-3d3f-bc31-ef5a56551bbf | -5.52777 | -44.34857 | 2025-09-11 03:53:00 | NOAA-21 | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| fb6b7f15-eec1-3226-ab12-048909ac7835 | -3.24009 | -50.80397 | 2025-09-11 03:53:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| e8105ecc-32ec-3b9d-8444-3544c2ae374f | -3.89215 | -42.54821 | 2025-09-11 03:53:00 | NOAA-21 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| c441a07c-3f25-3f0e-928e-a2eb358c96ba | -3.41825 | -47.61063 | 2025-09-11 03:53:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| de6957b1-15c9-32eb-8a17-7c8dbbb9f775 | -5.47157 | -43.43831 | 2025-09-11 03:53:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 9e7351dd-f421-3ae1-99d9-1b144b8c3d56 | -3.35062 | -42.16118 | 2025-09-11 03:53:00 | NOAA-21 | MAGALHÃES DE ALMEIDA | MARANHÃO | Brasil | 2106300 | 21 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 878e93f7-efcb-35f8-8852-45749e5490d9 | -5.47622 | -43.43543 | 2025-09-11 03:53:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| b0a25c29-84b6-3086-9bac-592274288456 | -5.65891 | -43.89475 | 2025-09-11 03:53:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| cdd21540-ec1e-3c95-9650-581d312ace6a | -2.43948 | -47.32893 | 2025-09-11 03:53:00 | NOAA-21 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 4ad689db-1daa-3dce-8684-db97431fe84d | -2.74061 | -48.68105 | 2025-09-11 03:53:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 9f44448b-89a3-3632-ae8e-efc2ccaa03cd | -3.24119 | -50.79771 | 2025-09-11 03:53:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 9d34203a-0db9-357a-ac45-1a936f534be7 | -5.3601 | -43.40547 | 2025-09-11 03:53:00 | NOAA-21 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 4c5eb7f5-1083-3ae9-a608-e3d0ebbccfd7 | -5.52662 | -44.34318 | 2025-09-11 03:53:00 | NOAA-21 | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 65c87a08-4bf7-3e28-b6f6-0c5fd9848320 | -4.65329 | -47.03229 | 2025-09-11 03:53:00 | NOAA-21 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b663d29e-9b54-31df-84c0-9140a00d1897 | -4.22334 | -46.36192 | 2025-09-11 03:53:00 | NOAA-21 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 67c2a0a2-e7a7-36da-95b9-530f467b0041 | -5.66308 | -43.89542 | 2025-09-11 03:53:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 4a1f9116-0b33-37e4-96e1-068403fb0c79 | -4.65255 | -47.03643 | 2025-09-11 03:53:00 | NOAA-21 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 2ede4038-cf6b-3aba-a15b-122a6673d805 | -4.13745 | -38.70476 | 2025-09-11 03:53:00 | NOAA-21 | GUAIÚBA | CEARÁ | Brasil | 2304954 | 23 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 1476bd30-afcf-36ee-8b74-33adaaec0534 | -5.08169 | -41.15284 | 2025-09-11 03:53:00 | NOAA-21 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 98f7d9fd-8eea-3dc0-b220-3d4a00182832 | -5.57798 | -42.92487 | 2025-09-11 03:53:00 | NOAA-21 | CURRALINHOS | PIAUÍ | Brasil | 2203255 | 22 | 33 | nan | nan | nan | Caatinga | 14.1 |
| 287b1741-2c1f-3e9d-a43a-e101c9a36297 | -4.61952 | -47.41745 | 2025-09-11 03:53:00 | NOAA-21 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b174a5ca-bb4b-31b8-8513-f376ab32fe13 | -5.47218 | -43.43471 | 2025-09-11 03:53:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| c7e2929a-0154-366b-8e71-d0c37bbfb0b8 | -5.41201 | -43.46919 | 2025-09-11 03:53:00 | NOAA-21 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 1230dd71-e826-3802-ae67-38edf79deea2 | -5.57109 | -43.44416 | 2025-09-11 03:53:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 3be7a642-18b2-3d19-b1d8-a3b401160195 | -4.70982 | -47.23436 | 2025-09-11 03:53:00 | NOAA-21 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 023d496e-71f1-3851-96df-c1907601f910 | -5.55388 | -43.04538 | 2025-09-11 03:53:00 | NOAA-21 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 6529aa08-8879-36cd-93d8-a78f3fbe4e44 | -5.53092 | -44.34391 | 2025-09-11 03:53:00 | NOAA-21 | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 2d8b89f1-7135-3cb4-836e-f6ea0fa5b639 | -5.66371 | -43.89161 | 2025-09-11 03:53:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 27e20b88-0833-307a-a0a7-b4475b6f6062 | -5.53022 | -44.348 | 2025-09-11 03:53:00 | NOAA-21 | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| dedb1443-9a83-35d3-9120-866719768cd6 | -6.34092 | -39.85799 | 2025-09-11 03:53:00 | NOAA-21 | CATARINA | CEARÁ | Brasil | 2303600 | 23 | 33 | nan | nan | nan | Caatinga | 3.5 |
| 824df0aa-14b5-3ad3-83d4-15ed3cb071b5 | -5.19714 | -43.0332 | 2025-09-11 03:53:00 | NOAA-21 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b6d0183e-2f2c-37d0-baa6-6d8687b8f1b6 | -3.24689 | -50.79474 | 2025-09-11 03:53:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| f076a9fb-ad6e-31e1-89b4-c11ebcdf3419 | -4.87626 | -42.78439 | 2025-09-11 03:53:00 | NOAA-21 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Cerrado | 6.9 |
| ff52c8b9-d55f-39fe-b018-752d4c617f0d | -4.41425 | -48.9588 | 2025-09-11 03:53:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| dfb917a5-5923-3286-9fd2-1bdca9e418f2 | -5.23916 | -45.46498 | 2025-09-11 03:53:00 | NOAA-21 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| f85c3503-59ac-3f9b-81f2-9b5e1d0413ed | -2.07384 | -47.1431 | 2025-09-11 03:53:00 | NOAA-21 | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 9674482b-ef91-3507-8177-c0117c80fbb7 | -3.40365 | -43.00179 | 2025-09-11 03:53:00 | NOAA-21 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| a38f74be-449e-30c3-9234-d352f82e1c8c | -5.57453 | -43.4484 | 2025-09-11 03:53:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 0f278e05-1cd9-31e9-b2ff-62578d698d45 | -5.44962 | -44.00298 | 2025-09-11 03:53:00 | NOAA-21 | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 5520770e-a472-3f9a-80c1-a9758ffa72db | -2.22192 | -48.23006 | 2025-09-11 03:53:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 8.5 |
| 87f1cd64-d422-369a-ab03-a1d3433af1ac | -4.41391 | -42.13893 | 2025-09-11 03:53:00 | NOAA-21 | BOA HORA | PIAUÍ | Brasil | 2201770 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| c277bcbe-61e3-3746-b95f-0c986471cbba | -5.36077 | -45.22392 | 2025-09-11 03:53:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 07d36956-6f20-3b52-976a-fb00d4e18ccf | -3.71544 | -38.83474 | 2025-09-11 03:53:00 | NOAA-21 | CAUCAIA | CEARÁ | Brasil | 2303709 | 23 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 77dbde9b-d143-39fe-b630-d3298b09a6fd | -5.47096 | -43.44193 | 2025-09-11 03:53:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| af1051bd-732a-3def-a892-7ebd2eb426cc | -2.9473 | -49.34593 | 2025-09-11 03:53:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 33b78473-aeec-359c-b610-16ec0ca83f3e | -5.22311 | -45.42879 | 2025-09-11 03:53:00 | NOAA-21 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 79befd72-b50e-3517-8d5b-07ccfd9aa3a7 | -5.34017 | -44.80432 | 2025-09-11 03:53:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 601e1d49-e93e-36da-b02a-279a4fe7e3ec | -3.79503 | -51.16349 | 2025-09-11 03:53:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 8.1 |
| b0853dab-91e0-35e6-aeb9-d324dbb548ff | -3.34933 | -39.2776 | 2025-09-11 03:53:00 | NOAA-21 | TRAIRI | CEARÁ | Brasil | 2313500 | 23 | 33 | nan | nan | nan | Caatinga | 4.1 |
| 530fe482-fd34-35f6-9963-64c664c97312 | -4.4818 | -48.11488 | 2025-09-11 03:53:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| c7fb60fd-769a-39e9-b321-44d1792f00e8 | -5.5717 | -43.44056 | 2025-09-11 03:53:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 4bf53a5b-533d-31e4-9006-31503d19b9ed | -4.43907 | -38.45486 | 2025-09-11 03:53:00 | NOAA-21 | OCARA | CEARÁ | Brasil | 2309458 | 23 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 60b53412-d231-38a2-aec8-7c42889fb87e | -5.51609 | -42.69055 | 2025-09-11 03:53:00 | NOAA-21 | LAGOA DO PIAUÍ | PIAUÍ | Brasil | 2205581 | 22 | 33 | nan | nan | nan | Caatinga | 12.2 |
| 768a6698-5d3b-355d-8a61-f611062f0867 | -5.47682 | -43.43185 | 2025-09-11 03:53:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 36fc8f09-91d5-3f59-8e27-cdbf95d5b1c7 | -5.35496 | -43.40831 | 2025-09-11 03:53:00 | NOAA-21 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 7de676cb-2f85-34c8-81c9-831b83cca3f0 | -5.22815 | -43.69304 | 2025-09-11 03:53:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 70e8b987-caf6-36c3-ac26-84e6a356051e | -2.79039 | -48.60658 | 2025-09-11 03:53:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| c58a0793-ad26-355a-974a-97b7e0acf137 | -3.68676 | -47.49565 | 2025-09-11 03:53:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e62685af-1e9b-3684-9051-fd703e6b3533 | -5.20322 | -45.72515 | 2025-09-11 03:53:00 | NOAA-21 | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 246699c9-d487-3765-8a36-d955b9e65db9 | -3.41887 | -47.60691 | 2025-09-11 03:53:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| d49d4f59-14af-3d4f-af6e-12fbeea6f965 | -4.71649 | -47.23482 | 2025-09-11 03:53:00 | NOAA-21 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 8269bb42-bf82-3331-973b-a3a97dfa3968 | -2.94646 | -49.35075 | 2025-09-11 03:53:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 54be6196-8a84-3217-99fd-6f36858cf837 | -5.62462 | -43.1091 | 2025-09-11 03:53:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 9b1f9d69-e996-33fe-9294-be7afb077173 | -5.23695 | -45.46101 | 2025-09-11 03:53:00 | NOAA-21 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| ad1fb876-ee96-3dff-b459-e2632848698f | -4.43853 | -38.45831 | 2025-09-11 03:53:00 | NOAA-21 | OCARA | CEARÁ | Brasil | 2309458 | 23 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 8762f63e-b8e3-3fc0-a51b-7a7f09d5bbc6 | -4.733 | -43.53193 | 2025-09-11 03:53:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 158cc9a9-ad7a-3bf7-b3a4-bdad61156895 | -4.21832 | -46.36095 | 2025-09-11 03:53:00 | NOAA-21 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 8.6 |
| 638633a4-33ea-39b0-b407-f7307351ec8e | -5.65698 | -43.90635 | 2025-09-11 03:53:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 00fd6e89-1366-3b70-aadf-b9c55e710655 | -4.6531 | -47.03327 | 2025-09-11 03:53:00 | NOAA-21 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 29ae3592-50b5-3426-99c1-5d881aa9b95a | -5.54994 | -43.0447 | 2025-09-11 03:53:00 | NOAA-21 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 3280bb71-77ba-3219-8403-8936707f539a | -5.45025 | -43.99911 | 2025-09-11 03:53:00 | NOAA-21 | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |


[Clique aqui para ver as próximas entradas](README13.md)
