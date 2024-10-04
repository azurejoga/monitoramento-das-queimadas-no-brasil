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

## Dados Diários - Página 60

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| d87a9498-a548-3246-8303-1d81e2108f52 | -7.66492 | -45.22533 | 2024-10-04 04:08:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 3.7 |
| c7818274-5826-3550-9b0e-b0fbcbce0fd2 | -7.59246 | -45.00528 | 2024-10-04 04:08:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 67749970-9970-3474-8a5d-7796b107c6f5 | -7.58957 | -45.00038 | 2024-10-04 04:08:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 938fc36a-cbe9-34f4-85d6-8fbcc77c56f8 | -7.58095 | -45.27935 | 2024-10-04 04:08:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 5ab567c8-a6c1-3ac4-9654-763b37dc0797 | -7.55412 | -45.14676 | 2024-10-04 04:08:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 18b45123-2dfb-352f-8b7d-ca62dbf34ce4 | -7.55343 | -45.15091 | 2024-10-04 04:08:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| a7a6c466-b391-3ca7-ab72-fa11ceb8b67a | -7.49509 | -44.84542 | 2024-10-04 04:08:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.8 |
| ea826e76-651a-383f-b501-27a75957a5f3 | -6.65687 | -45.00722 | 2024-10-04 04:08:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| f42e01a1-dd36-3d77-ad84-cf505e40de62 | -6.61474 | -45.03543 | 2024-10-04 04:08:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| f41c8886-0623-3417-9387-678e1d72a73e | -6.61108 | -45.03488 | 2024-10-04 04:08:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 19525f95-bed5-36d5-93b6-3d7db790a9bc | -6.60236 | -45.04221 | 2024-10-04 04:08:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| df6f8818-586a-351b-8a64-c52a3572d983 | -6.59869 | -45.04166 | 2024-10-04 04:08:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| d1b8b5e1-bcf8-37b9-8a59-0ec3f68aa514 | -6.54854 | -44.79839 | 2024-10-04 04:08:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 7eb63026-65fa-3057-bbb6-28849f6b8b02 | -6.54492 | -44.79779 | 2024-10-04 04:08:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 7929e80f-6a41-3dab-ba19-ea49fb0bd25a | -7.74937 | -44.04868 | 2024-10-04 04:08:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 7f790d49-a8e4-38af-b6e3-881fd2c33298 | -7.74592 | -44.04814 | 2024-10-04 04:08:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 8b9bc78b-fed1-3543-bda6-fd3b2692cc66 | -7.46023 | -43.79434 | 2024-10-04 04:08:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 1566a477-db0b-3fdb-b6eb-4cdcf37925e6 | -7.41206 | -44.04689 | 2024-10-04 04:08:00 | NOAA-21 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| b2cb9b26-dc1f-3d9c-a090-08b460c2a78d | -6.63054 | -43.73226 | 2024-10-04 04:08:00 | NOAA-21 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 893cfaef-1f1c-3e1f-9811-4435322ff50f | -6.6271 | -43.73171 | 2024-10-04 04:08:00 | NOAA-21 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 9d8c0dff-958b-3426-a268-3e6b0e4b577e | -6.71928 | -44.55392 | 2024-10-04 04:08:00 | NOAA-21 | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| fd45afcf-eb09-37d0-9411-6d47699abaa6 | -6.71569 | -44.55347 | 2024-10-04 04:08:00 | NOAA-21 | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 10ef9441-8db4-3a93-8c96-922a9ae5b25b | -6.58333 | -44.2967 | 2024-10-04 04:08:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 4128f526-660d-3195-a2d4-58b18a8c6583 | -8.68409 | -45.26099 | 2024-10-04 04:08:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 0b05e8c9-75a4-3130-a836-befdd548699c | -8.68049 | -45.26033 | 2024-10-04 04:08:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| a8a12103-66d6-3d57-8117-4db646221b27 | -8.67979 | -45.26463 | 2024-10-04 04:08:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 3cf5cf9a-9078-3251-8a7e-320d0d82500b | -8.67689 | -45.25969 | 2024-10-04 04:08:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| ac7b604a-5d30-35a1-a0e9-1bf403638836 | -8.29985 | -45.47336 | 2024-10-04 04:08:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 3.5 |
| fa376afb-0138-3aff-9006-1ecb995e95b0 | -8.29914 | -45.47768 | 2024-10-04 04:08:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 48b81e43-0e4c-3373-a236-5ad9f3c65f48 | -8.29688 | -45.46857 | 2024-10-04 04:08:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 74280a64-3bf4-3c9b-aa0e-0e73a6b38d1d | -8.29615 | -45.47293 | 2024-10-04 04:08:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| f59ea45a-ecdc-336f-bda4-d56359d45021 | -8.2945 | -45.41486 | 2024-10-04 04:08:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 8331c598-1a8e-37e6-af3a-dbad116ff6eb | -8.2894 | -45.42297 | 2024-10-04 04:08:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 24c168b4-5bc1-38e0-90a0-312c65f78396 | -8.28868 | -45.42732 | 2024-10-04 04:08:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 1f3957cb-7c68-3d18-ba7b-7cec692b6876 | -8.28795 | -45.43166 | 2024-10-04 04:08:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 25076a3c-2bf0-3261-a6b2-30b2cd100a08 | -8.27914 | -45.41687 | 2024-10-04 04:08:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 3.2 |
| db7d1c98-ce24-3bed-b310-2aa678b6794c | -8.13283 | -44.81018 | 2024-10-04 04:08:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| dc7f9583-2c27-360b-bbfe-ad8b93f5920f | -8.13213 | -44.8144 | 2024-10-04 04:08:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| a41174c5-fbf7-3324-92ee-4af73eaa3c43 | -7.85809 | -45.3512 | 2024-10-04 04:08:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 7.4 |
| ef532e85-03ad-3307-bafe-7417f558b46b | -7.85737 | -45.35553 | 2024-10-04 04:08:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 16253b46-c70c-39cd-9c5a-0e471e4b49b3 | -7.85664 | -45.35987 | 2024-10-04 04:08:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 32.0 |
| 943b3b9c-67f4-38c7-bd30-7b52a3e9e640 | -7.85658 | -45.33763 | 2024-10-04 04:08:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 83ec020f-68d5-37da-9edd-dfd880f8f183 | -7.85515 | -45.34627 | 2024-10-04 04:08:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 54e53bcf-6901-307e-aa95-2377910399f2 | -7.85442 | -45.35059 | 2024-10-04 04:08:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 481f86b5-f694-3d09-98b8-0ee5af0a4f31 | -7.8537 | -45.35493 | 2024-10-04 04:08:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 326c4650-28f2-3459-a8a9-1561bd11ad52 | -7.85298 | -45.35926 | 2024-10-04 04:08:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 32.0 |
| 5e4386f7-7feb-39e2-a8aa-e16bbd4be0ae | -8.2275 | -44.36916 | 2024-10-04 04:08:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| d41f6be5-f0d9-3658-a7f1-67217a0f7c8d | -8.22685 | -44.37308 | 2024-10-04 04:08:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| b829ba2c-c92a-3d36-a784-b56dba4bbdc0 | -8.22621 | -44.37699 | 2024-10-04 04:08:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ec33f6ca-6a51-3e38-9d4d-fb289404aab0 | -8.22054 | -44.36798 | 2024-10-04 04:08:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f5f96a2c-6742-3952-a882-85b26169141d | -8.21989 | -44.37191 | 2024-10-04 04:08:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 221154f9-8673-3204-b891-ceddf905e9b6 | -8.17138 | -44.39618 | 2024-10-04 04:08:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 6608099e-959d-3349-96d4-9abb65b84305 | -8.16726 | -44.39951 | 2024-10-04 04:08:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| a6d2803b-0769-398a-9626-f311da9991a5 | -8.16315 | -44.40284 | 2024-10-04 04:08:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 35c2ae41-fb3f-3d24-86da-97cc923655ac | -8.16251 | -44.40675 | 2024-10-04 04:08:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 0282aaee-355a-310d-a39d-2cb093926ff0 | -3.05974 | -44.4836 | 2024-10-04 04:08:00 | NOAA-21 | SANTA RITA | MARANHÃO | Brasil | 2110203 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0f5ca9a4-6abe-33ea-87ba-29a5d9501eda | -3.05745 | -44.48426 | 2024-10-04 04:08:00 | NOAA-21 | SANTA RITA | MARANHÃO | Brasil | 2110203 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 93c2c6c8-baf0-30b7-b0cb-c7d7c346f9de | -5.02112 | -45.48497 | 2024-10-04 04:08:00 | NOAA-21 | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 5524dcb3-e9de-342b-97b2-bb768ef93812 | -5.00417 | -45.49221 | 2024-10-04 04:08:00 | NOAA-21 | LAGOA GRANDE DO MARANHÃO | MARANHÃO | Brasil | 2105963 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| a7385064-359e-3ddf-a603-ccb26f18f1fa | -4.95797 | -45.50912 | 2024-10-04 04:08:00 | NOAA-21 | LAGOA GRANDE DO MARANHÃO | MARANHÃO | Brasil | 2105963 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 7284e965-664c-3155-b259-81aa99555b71 | -4.95625 | -45.5064 | 2024-10-04 04:08:00 | NOAA-21 | LAGOA GRANDE DO MARANHÃO | MARANHÃO | Brasil | 2105963 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f7ca4b25-9d9d-3cdd-be28-50861b5ac995 | -4.95549 | -45.51114 | 2024-10-04 04:08:00 | NOAA-21 | LAGOA GRANDE DO MARANHÃO | MARANHÃO | Brasil | 2105963 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 3c09b1cd-eb14-3a6a-a44c-3f6a46f8d4f1 | -4.86852 | -45.77719 | 2024-10-04 04:08:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 3e1c78d4-743e-3640-bb82-e2109b09a944 | -4.80906 | -45.79566 | 2024-10-04 04:08:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| cb0b05b3-4418-3b40-a56a-90f12b04d28e | -4.78307 | -45.95777 | 2024-10-04 04:08:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 37d470a6-90f4-32cd-81ce-5db44eda7cad | -4.70676 | -45.8779 | 2024-10-04 04:08:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 26a8c400-d679-3195-acb6-b9cf2e310238 | -4.7028 | -45.8773 | 2024-10-04 04:08:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| e7e607dd-907f-3ce3-94cc-011fca27d457 | -4.69129 | -45.87843 | 2024-10-04 04:08:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 35.7 |
| f0903fa9-7622-3b24-ae18-c0aacd5565b0 | -4.69048 | -45.88348 | 2024-10-04 04:08:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 2.8 |
| c35ade35-ed85-36a6-9316-8c1ed3f01251 | -4.6901 | -45.88051 | 2024-10-04 04:08:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 29.0 |
| 83fedd87-ac27-3bc3-ae9f-4d071cd9dd5a | -4.68815 | -45.87273 | 2024-10-04 04:08:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 56.4 |
| c5f4a099-8a8c-31b7-a273-18100964837e | -4.68734 | -45.87777 | 2024-10-04 04:08:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 56.4 |
| 0355fdeb-5410-3591-a0d6-656750bea571 | -4.68699 | -45.87484 | 2024-10-04 04:08:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 50.6 |
| bdf950aa-0933-3a48-88a5-08437fdc1563 | -4.68653 | -45.88283 | 2024-10-04 04:08:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 54.2 |
| 8365e649-9221-3b04-9a26-0ce6a299a346 | -4.68615 | -45.87987 | 2024-10-04 04:08:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 29.0 |
| 068dcb0e-1b10-3b2a-9cbb-8bf24d2797fd | -4.68571 | -45.88793 | 2024-10-04 04:08:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 54.2 |
| e5eed8ce-a341-3195-82b3-e07b42b828f5 | -4.6853 | -45.88494 | 2024-10-04 04:08:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 29.0 |
| 3548dfbe-06d6-3124-b445-0b5b419dd318 | -4.68418 | -45.87219 | 2024-10-04 04:08:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 56.4 |
| b8b8c7a3-3c28-31c8-876d-5065dc73858b | -4.68302 | -45.87429 | 2024-10-04 04:08:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 26.2 |
| 65c6a70f-e2b4-37f7-b440-f68fe3f69b6c | -4.68257 | -45.88223 | 2024-10-04 04:08:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 54.2 |
| b7f7ead8-acd1-3260-8c54-45042a143a50 | -4.6822 | -45.87923 | 2024-10-04 04:08:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 89.4 |
| 595d0a5a-60a7-360a-bca3-bcb419cb65bf | -4.68174 | -45.88742 | 2024-10-04 04:08:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 54.2 |
| f95c6719-0b54-3e64-9f6b-0c18fba8a431 | -4.68133 | -45.88438 | 2024-10-04 04:08:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 89.4 |
| 241c395b-9320-3beb-92d9-49505d020056 | -4.68045 | -45.8896 | 2024-10-04 04:08:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 5eb9df6f-443e-3451-bcb4-0df588b138e5 | -4.68021 | -45.87172 | 2024-10-04 04:08:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 27.4 |
| 027747d9-7740-360c-97d7-819da5a73257 | -4.67942 | -45.87658 | 2024-10-04 04:08:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 27.4 |
| 17d53a17-f1b6-32f2-b10a-e41b51b65870 | -4.67905 | -45.87378 | 2024-10-04 04:08:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 26.2 |
| a5f8393f-8090-360a-b950-f2ba56db2af3 | -4.67861 | -45.88163 | 2024-10-04 04:08:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 9.0 |
| 9ca2a8fb-cf67-3efc-ab54-8ea2377bfbd3 | -4.67824 | -45.87865 | 2024-10-04 04:08:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 89.4 |
| eddb1123-3ba6-3fd2-ac0a-bab6f5769433 | -4.67777 | -45.88687 | 2024-10-04 04:08:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 9.0 |
| e4b9fe87-cad9-3fd2-b492-229c9d01a0e0 | -4.67737 | -45.88382 | 2024-10-04 04:08:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 89.4 |
| 2384fb36-8689-3384-9ec7-e3e001b5f826 | -4.67624 | -45.87118 | 2024-10-04 04:08:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 27.4 |
| 61469fe4-34e3-37f4-b8dd-593cca6633de | -4.67545 | -45.8761 | 2024-10-04 04:08:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 27.4 |
| fb8f0747-57b4-32e4-bd4b-7e0c49ae2e78 | -4.67464 | -45.88112 | 2024-10-04 04:08:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 9.0 |
| 6224257b-d5b3-3eb2-948e-8f917fad604e | -4.67381 | -45.88627 | 2024-10-04 04:08:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 9.0 |
| eb0b9941-4530-300f-afd1-e77ac42f2aa6 | -4.67228 | -45.87062 | 2024-10-04 04:08:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 7.2 |
| a7b41619-792f-3423-ac65-88344f65bd7b | -4.67147 | -45.87561 | 2024-10-04 04:08:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 7.2 |
| c43d83b8-09ab-3678-827d-cb0b1cbc6ea5 | -4.67066 | -45.88064 | 2024-10-04 04:08:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 5.1 |
| d2ac19d1-dc4a-3c6a-a916-8a3f8bb528d5 | -4.59863 | -45.75289 | 2024-10-04 04:08:00 | NOAA-21 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| f95577b0-6beb-3b2c-96f2-6ccff4a9f50e | -4.55372 | -45.65819 | 2024-10-04 04:08:00 | NOAA-21 | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |


[Clique aqui para ver as próximas entradas](README61.md)
