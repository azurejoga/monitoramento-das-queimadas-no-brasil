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

## Dados Diários - Página 20

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 37097093-0c4e-3596-aa71-60e1a8f6ea84 | -23.38537 | -47.15041 | 2025-09-19 03:57:00 | NOAA-20 | ITU | SÃO PAULO | Brasil | 3523909 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 2a947c4b-461b-3ab6-8026-33d737edbf2d | -19.91817 | -44.70942 | 2025-09-19 03:57:00 | NOAA-20 | IGARATINGA | MINAS GERAIS | Brasil | 3130200 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 52aea193-3522-3df2-8fdf-9a52ea7b76b7 | -21.35051 | -45.78634 | 2025-09-19 03:57:00 | NOAA-20 | CAMPOS GERAIS | MINAS GERAIS | Brasil | 3111606 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 758c195d-d548-34b5-89f7-6c44ff40154b | -20.79503 | -47.24072 | 2025-09-19 03:57:00 | NOAA-20 | PATROCÍNIO PAULISTA | SÃO PAULO | Brasil | 3536307 | 35 | 33 | nan | nan | nan | Cerrado | 3.1 |
| c651dd5a-98ef-3c6a-997b-f5654a4568c3 | -19.95382 | -42.41535 | 2025-09-19 03:57:00 | NOAA-20 | RAUL SOARES | MINAS GERAIS | Brasil | 3154002 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 8fb5b61d-60ed-3501-ba84-7424530b4a16 | -18.58797 | -45.04252 | 2025-09-19 03:57:00 | NOAA-20 | FELIXLÂNDIA | MINAS GERAIS | Brasil | 3125705 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 40ab5039-4774-39da-8003-ff6a9fab2551 | -18.57874 | -43.4697 | 2025-09-19 03:57:00 | NOAA-20 | SERRO | MINAS GERAIS | Brasil | 3167103 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.8 |
| b3486773-c0cd-3113-ae8c-32b44f982995 | -21.07197 | -45.61141 | 2025-09-19 03:57:00 | NOAA-20 | BOA ESPERANÇA | MINAS GERAIS | Brasil | 3107109 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 1f03b256-84e1-318e-b0b8-6d03f1ba3a86 | -19.92514 | -44.15532 | 2025-09-19 03:57:00 | NOAA-20 | BETIM | MINAS GERAIS | Brasil | 3106705 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 3e5f5814-a4cd-3c73-ad32-2fa7c0b53397 | -21.28228 | -48.79464 | 2025-09-19 03:57:00 | NOAA-20 | SANTA ADÉLIA | SÃO PAULO | Brasil | 3545605 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.9 |
| 08fb425a-727a-38e8-9128-7251b22d8a1d | -18.64677 | -43.90339 | 2025-09-19 03:57:00 | NOAA-20 | GOUVEIA | MINAS GERAIS | Brasil | 3127602 | 31 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 638aa4ea-07d4-30c9-a22b-a586f0d393dc | -19.37737 | -47.34935 | 2025-09-19 03:57:00 | NOAA-20 | PERDIZES | MINAS GERAIS | Brasil | 3149804 | 31 | 33 | nan | nan | nan | Cerrado | 11.6 |
| 19a0363e-49b7-3b3d-874a-03f7af4c1a29 | -21.28667 | -48.79578 | 2025-09-19 03:57:00 | NOAA-20 | SANTA ADÉLIA | SÃO PAULO | Brasil | 3545605 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.9 |
| 2cac5f0e-3123-36ee-b4f8-59b29b40dac4 | -19.81976 | -44.21749 | 2025-09-19 03:57:00 | NOAA-20 | ESMERALDAS | MINAS GERAIS | Brasil | 3124104 | 31 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 887782d5-29db-3803-86dd-09e4f1f7647e | -22.68324 | -47.49425 | 2025-09-19 03:57:00 | NOAA-20 | LIMEIRA | SÃO PAULO | Brasil | 3526902 | 35 | 33 | nan | nan | nan | Cerrado | 7.1 |
| c9910f94-8d96-345b-8485-dc2680ec123a | -23.23449 | -47.62045 | 2025-09-19 03:57:00 | NOAA-20 | BOITUVA | SÃO PAULO | Brasil | 3507001 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 43280be7-9650-3610-9557-08b3b20c1b1d | -18.69695 | -43.7389 | 2025-09-19 03:57:00 | NOAA-20 | CONCEIÇÃO DO MATO DENTRO | MINAS GERAIS | Brasil | 3117504 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| e433665a-7c0a-34a6-bef0-83202d5b5df7 | -19.37659 | -47.3534 | 2025-09-19 03:57:00 | NOAA-20 | PERDIZES | MINAS GERAIS | Brasil | 3149804 | 31 | 33 | nan | nan | nan | Cerrado | 10.1 |
| c0b4b911-0879-333e-bb26-8cf59a2ddec9 | -22.33708 | -46.76382 | 2025-09-19 03:57:00 | NOAA-20 | ITAPIRA | SÃO PAULO | Brasil | 3522604 | 35 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 5a2196cf-bbe7-3943-9ce0-6fb50a1c2cb5 | -18.58367 | -43.37731 | 2025-09-19 03:57:00 | NOAA-20 | SERRO | MINAS GERAIS | Brasil | 3167103 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| f07cdb61-e94a-3bd2-b0d3-aa6ef684fe11 | -22.0398 | -45.58849 | 2025-09-19 03:57:00 | NOAA-20 | HELIODORA | MINAS GERAIS | Brasil | 3129202 | 31 | 33 | nan | nan | nan | Mata Atlântica | 7.4 |
| 0462cbee-dcce-3a52-96e7-6711dad98994 | -20.67068 | -47.86101 | 2025-09-19 03:57:00 | NOAA-20 | ORLÂNDIA | SÃO PAULO | Brasil | 3534302 | 35 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 04ba0ede-5077-316a-8ff8-b8ae2022da53 | -23.15222 | -49.62648 | 2025-09-19 03:57:00 | NOAA-20 | TIMBURI | SÃO PAULO | Brasil | 3554607 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| ca7b9c5e-8d8e-3476-b992-051510e1123b | -21.76093 | -45.35878 | 2025-09-19 03:57:00 | NOAA-20 | CAMPANHA | MINAS GERAIS | Brasil | 3110905 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| ca964eeb-ba85-3c4f-9764-4bde9d378d8c | -18.95766 | -42.07896 | 2025-09-19 03:57:00 | NOAA-20 | GOVERNADOR VALADARES | MINAS GERAIS | Brasil | 3127701 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 1cbd529f-c675-335d-b710-fe6346586232 | -21.34926 | -46.72832 | 2025-09-19 03:57:00 | NOAA-20 | GUAXUPÉ | MINAS GERAIS | Brasil | 3128709 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 32588f82-e518-381d-b5ae-3fde7cfa0dc7 | -19.79876 | -43.52099 | 2025-09-19 03:57:00 | NOAA-20 | BARÃO DE COCAIS | MINAS GERAIS | Brasil | 3105400 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 0fb79b9d-8645-3711-b8b3-7b1079173bbd | -20.08964 | -46.1376 | 2025-09-19 03:57:00 | NOAA-20 | BAMBUÍ | MINAS GERAIS | Brasil | 3105103 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e836b1ea-8409-328c-af28-f99584c785c0 | -23.60343 | -51.05204 | 2025-09-19 03:57:00 | NOAA-20 | LONDRINA | PARANÁ | Brasil | 4113700 | 41 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| d6d1aa07-9070-3425-acaa-f3b41e0ba77c | -21.40287 | -44.27851 | 2025-09-19 03:57:00 | NOAA-20 | MADRE DE DEUS DE MINAS | MINAS GERAIS | Brasil | 3139102 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| bfbe6ab9-3dbf-3a55-8a03-08bbef28e9c4 | -20.16345 | -41.48635 | 2025-09-19 03:57:00 | NOAA-20 | LAJINHA | MINAS GERAIS | Brasil | 3137700 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| ab8bb62a-8094-34a9-9d09-4e76a935e9cb | -20.54564 | -44.02805 | 2025-09-19 03:57:00 | NOAA-20 | JECEABA | MINAS GERAIS | Brasil | 3135407 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.0 |
| ebb32e4d-c04e-31c4-a9fa-26855a806f44 | -22.6195 | -47.34465 | 2025-09-19 03:57:00 | NOAA-20 | LIMEIRA | SÃO PAULO | Brasil | 3526902 | 35 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 4b6eadc4-168e-3b3e-91ac-9e16283a4c3b | -19.91695 | -44.58057 | 2025-09-19 03:57:00 | NOAA-20 | PARÁ DE MINAS | MINAS GERAIS | Brasil | 3147105 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| ed84ce2b-1779-3c98-930e-66a0796ef775 | -21.7582 | -45.3561 | 2025-09-19 03:57:00 | NOAA-20 | CAMPANHA | MINAS GERAIS | Brasil | 3110905 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| dc3d72cb-ba1b-3f6c-a38d-54bff94499b0 | -20.54218 | -44.02738 | 2025-09-19 03:57:00 | NOAA-20 | JECEABA | MINAS GERAIS | Brasil | 3135407 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.0 |
| cb0b83a9-c648-310d-a4f4-a5e69bdd3652 | -23.14684 | -46.60138 | 2025-09-19 03:57:00 | NOAA-20 | ATIBAIA | SÃO PAULO | Brasil | 3504107 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| 7785583e-9c7e-3638-af95-06c657b4b0a8 | -21.28292 | -54.80699 | 2025-09-19 03:57:00 | NOAA-20 | SIDROLÂNDIA | MATO GROSSO DO SUL | Brasil | 5007901 | 50 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a4bec201-b87d-33c4-bc65-252ee16cba51 | -20.22927 | -43.80056 | 2025-09-19 03:57:00 | NOAA-20 | ITABIRITO | MINAS GERAIS | Brasil | 3131901 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 84a3244c-a4f5-30a8-983d-070989a04a3e | -20.4582 | -45.94338 | 2025-09-19 03:57:00 | NOAA-20 | PIUMHI | MINAS GERAIS | Brasil | 3151503 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| b5a4d0d1-efa1-3a4d-9ebd-00cca3b9a3e5 | -20.78399 | -46.11746 | 2025-09-19 03:57:00 | NOAA-20 | GUAPÉ | MINAS GERAIS | Brasil | 3128105 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 4f833420-b3b9-31ff-aaa1-e9a56acb08ff | -17.49944 | -46.74392 | 2025-09-19 03:57:00 | NOAA-20 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ff510c6c-0d01-3f0b-8c91-d8fb0fe1a7f4 | -21.12059 | -45.72388 | 2025-09-19 03:57:00 | NOAA-20 | CAMPO DO MEIO | MINAS GERAIS | Brasil | 3111309 | 31 | 33 | nan | nan | nan | Mata Atlântica | 13.9 |
| 9b11908b-2663-318d-89c5-ca9a7f744523 | -18.12105 | -44.66851 | 2025-09-19 03:57:00 | NOAA-20 | CORINTO | MINAS GERAIS | Brasil | 3119104 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| bd865640-7109-3089-ad5c-4a85ef559002 | -20.34437 | -48.7897 | 2025-09-19 03:57:00 | NOAA-20 | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 3.3 |
| f74aaeef-b828-3da1-b31f-2f9535adef91 | -22.68175 | -47.50192 | 2025-09-19 03:57:00 | NOAA-20 | LIMEIRA | SÃO PAULO | Brasil | 3526902 | 35 | 33 | nan | nan | nan | Mata Atlântica | 21.5 |
| cf8b5e07-0ceb-3162-bbbd-72a6b67933ae | -19.95321 | -42.41903 | 2025-09-19 03:57:00 | NOAA-20 | RAUL SOARES | MINAS GERAIS | Brasil | 3154002 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| dbacc479-e1d1-39bb-94f2-07d9fca7ca5a | -20.16403 | -41.48268 | 2025-09-19 03:57:00 | NOAA-20 | LAJINHA | MINAS GERAIS | Brasil | 3137700 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 3d59529a-7c91-3b68-b41e-d0075943f4cd | -18.63084 | -43.91054 | 2025-09-19 03:57:00 | NOAA-20 | GOUVEIA | MINAS GERAIS | Brasil | 3127602 | 31 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 8b68e3ed-1e53-3beb-b895-81eb507cd677 | -18.3978 | -44.10157 | 2025-09-19 03:57:00 | NOAA-20 | MONJOLOS | MINAS GERAIS | Brasil | 3142502 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 0d7cd2d1-bcb5-3bb2-8a2b-b12ad64b1c35 | -23.27369 | -47.52384 | 2025-09-19 03:57:00 | NOAA-20 | PORTO FELIZ | SÃO PAULO | Brasil | 3540606 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 7483291f-8b2d-3d6d-a511-5e80e70e2db7 | -20.54288 | -44.02328 | 2025-09-19 03:57:00 | NOAA-20 | JECEABA | MINAS GERAIS | Brasil | 3135407 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.0 |
| 316c40f3-6f0b-32e0-89bf-c1d7860aa60d | -23.60027 | -51.05311 | 2025-09-19 03:57:00 | NOAA-20 | LONDRINA | PARANÁ | Brasil | 4113700 | 41 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| e2504058-6faa-3210-8db0-2f153ead24c5 | -10.2979 | -50.2372 | 2025-09-19 04:00:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 131.3 |
| 440e2c59-99e8-3084-88bb-7324c166c601 | -10.2982 | -50.2158 | 2025-09-19 04:00:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 119.7 |
| 1d142425-03e9-3c12-a06a-ae1de4fe1c15 | -11.1957 | -49.6462 | 2025-09-19 04:00:00 | GOES-19 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 67.6 |
| 09f93a15-2dde-3a03-9fef-b50b4d47ac24 | -11.196 | -49.6246 | 2025-09-19 04:00:00 | GOES-19 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 64.4 |
| 4cd52b87-eaa0-3a4d-b44f-8271b407f021 | -11.215 | -49.6224 | 2025-09-19 04:00:00 | GOES-19 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 117.8 |
| 91a3794a-1045-3846-be84-4e75e71bcdb9 | -11.2147 | -49.6441 | 2025-09-19 04:00:00 | GOES-19 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 126.0 |
| 7fa3b9f7-e3dc-38bc-9682-7db862f20962 | -25.68679 | -49.9003 | 2025-09-19 04:00:00 | NOAA-20 | LAPA | PARANÁ | Brasil | 4113205 | 41 | 33 | nan | nan | nan | Mata Atlântica | 11.4 |
| a5b5b92a-19ba-3530-8189-7fed678381fd | -29.81039 | -51.22705 | 2025-09-19 04:00:00 | NOAA-20 | NOVA SANTA RITA | RIO GRANDE DO SUL | Brasil | 4313375 | 43 | 33 | nan | nan | nan | Pampa | 1.3 |
| c5efc2dc-8498-33d9-8105-71724375008c | -25.68723 | -49.8981 | 2025-09-19 04:00:00 | NOAA-20 | LAPA | PARANÁ | Brasil | 4113205 | 41 | 33 | nan | nan | nan | Mata Atlântica | 6.7 |
| 5886feda-0ac5-33a3-9fbb-a84aa1e5278e | -25.68625 | -49.90289 | 2025-09-19 04:00:00 | NOAA-20 | LAPA | PARANÁ | Brasil | 4113205 | 41 | 33 | nan | nan | nan | Mata Atlântica | 6.7 |
| b18c0310-fcb3-389a-b896-58ee0c3085cb | -24.15058 | -53.05903 | 2025-09-19 04:00:00 | NOAA-20 | GOIOERÊ | PARANÁ | Brasil | 4108601 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 66f458b7-9f3c-3b42-b884-e312c1b3bb3e | -29.8096 | -51.22976 | 2025-09-19 04:00:00 | NOAA-20 | NOVA SANTA RITA | RIO GRANDE DO SUL | Brasil | 4313375 | 43 | 33 | nan | nan | nan | Pampa | 0.9 |
| 3943dfc8-d142-3267-99ec-95bd9825c0ce | -25.91859 | -50.05854 | 2025-09-19 04:00:00 | NOAA-20 | ANTÔNIO OLINTO | PARANÁ | Brasil | 4101309 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 01c6f48b-1cd8-3137-965c-5ea26ac7001f | -28.41902 | -49.73634 | 2025-09-19 04:00:00 | NOAA-20 | BOM JARDIM DA SERRA | SANTA CATARINA | Brasil | 4202503 | 42 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| e0e344a2-93c4-31d0-ab34-08179caa7d6b | -24.15145 | -53.05529 | 2025-09-19 04:00:00 | NOAA-20 | GOIOERÊ | PARANÁ | Brasil | 4108601 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| c7d8c848-5678-38c2-a4af-e499d1d11bbe | -21.3035 | -54.8095 | 2025-09-19 04:10:00 | GOES-19 | SIDROLÂNDIA | MATO GROSSO DO SUL | Brasil | 5007901 | 50 | 33 | nan | nan | nan | Cerrado | 123.4 |
| 75066524-44ce-32b6-a258-95d8fce6e240 | -21.2831 | -54.813 | 2025-09-19 04:10:00 | GOES-19 | SIDROLÂNDIA | MATO GROSSO DO SUL | Brasil | 5007901 | 50 | 33 | nan | nan | nan | Cerrado | 177.2 |
| d5c442ff-f809-3e1a-b38d-29f496735ce9 | -21.304 | -54.7879 | 2025-09-19 04:10:00 | GOES-19 | SIDROLÂNDIA | MATO GROSSO DO SUL | Brasil | 5007901 | 50 | 33 | nan | nan | nan | Cerrado | 67.1 |
| f1ca385d-b650-3c17-9449-bddc9b822c5e | -21.2835 | -54.7914 | 2025-09-19 04:10:00 | GOES-19 | SIDROLÂNDIA | MATO GROSSO DO SUL | Brasil | 5007901 | 50 | 33 | nan | nan | nan | Cerrado | 90.5 |
| d7e27b43-905f-358f-8edc-eef7c4a5537b | -4.66818 | -49.3331 | 2025-09-19 04:44:00 | NOAA-21 | JACUNDÁ | PARÁ | Brasil | 1503804 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| fd0f566c-452a-3df9-834a-44f81f69bbbd | -1.46136 | -55.21655 | 2025-09-19 04:44:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6613bf4d-a05f-3f58-9c3a-3be1ffbd1741 | -3.70167 | -47.68494 | 2025-09-19 04:44:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 56dcdf37-d002-3acd-8e09-e3483ba992b4 | -2.27474 | -48.1232 | 2025-09-19 04:44:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 557b0544-3fb2-395b-a473-0832ff34bc17 | -3.15566 | -43.26519 | 2025-09-19 04:44:00 | NOAA-21 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| ebe225ee-e0a8-3e45-8171-f0e02219459b | -1.45729 | -55.21592 | 2025-09-19 04:44:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2a9e4062-b780-3784-a7ec-98d2a7cd4162 | -3.78767 | -48.87093 | 2025-09-19 04:44:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9e92bd09-9c06-3af6-997c-47a180d5bedb | -2.9418 | -49.45735 | 2025-09-19 04:44:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b08b867f-08b8-3297-8faf-749e8e88285b | -2.26878 | -47.88659 | 2025-09-19 04:44:00 | NOAA-21 | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| e04b7693-9d1d-3ff3-8b34-5bfd1999e7b8 | -5.20836 | -45.17551 | 2025-09-19 04:44:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 8e958542-e46b-32bd-9612-0545ac5c21e3 | -2.44229 | -49.36534 | 2025-09-19 04:44:00 | NOAA-21 | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| aa71edb5-fa82-3766-9e44-d8cb4c313809 | -3.58021 | -55.54766 | 2025-09-19 04:44:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a2a4212d-f20e-34d3-803c-1986ee7a90b4 | -4.25657 | -49.31364 | 2025-09-19 04:44:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8703d850-5144-3070-a4d8-0d6f0c8ff203 | -5.47951 | -44.116 | 2025-09-19 04:44:00 | NOAA-21 | GOVERNADOR LUIZ ROCHA | MARANHÃO | Brasil | 2104628 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 1482e2da-9361-3902-b269-25bffba672fc | -3.45433 | -53.82762 | 2025-09-19 04:44:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9ae77c90-54e6-307e-983e-1d6bd0621a96 | -2.63762 | -48.0467 | 2025-09-19 04:44:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| a1cc7cfa-4e8c-3900-a694-f642aeea506f | -5.20414 | -45.17498 | 2025-09-19 04:44:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 729856e7-cee3-3106-8674-25f0bbcb9639 | -2.26245 | -47.8436 | 2025-09-19 04:44:00 | NOAA-21 | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 12.6 |
| 45bfa532-f06d-3ab3-b0b9-0c21f6e7c651 | -4.69787 | -41.95687 | 2025-09-19 04:44:00 | NOAA-21 | CAMPO MAIOR | PIAUÍ | Brasil | 2202208 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| fd161110-887b-3ae2-aa33-f9a2164383cd | -5.04465 | -47.90458 | 2025-09-19 04:44:00 | NOAA-21 | CIDELÂNDIA | MARANHÃO | Brasil | 2103257 | 21 | 33 | nan | nan | nan | Amazônia | 29.2 |
| 6db6db95-df70-3114-a475-9e7ec8788f19 | -2.73912 | -49.40424 | 2025-09-19 04:44:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9db234da-5a90-31c8-b640-bde68c9288cb | -5.46849 | -44.68964 | 2025-09-19 04:44:00 | NOAA-21 | SANTA FILOMENA DO MARANHÃO | MARANHÃO | Brasil | 2109759 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 18b1ebff-fd55-3eb9-af8c-0c5d66607139 | -4.86483 | -42.97519 | 2025-09-19 04:44:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 7f1a164e-a1e8-3fe7-932a-4f81e049943a | -5.44873 | -44.82777 | 2025-09-19 04:44:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| bdb28273-8e2b-3a6a-abe6-a0f9650f7c17 | 1.95253 | -50.97063 | 2025-09-19 04:44:00 | NOAA-21 | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 71b6f8e4-cdc2-3114-9cd7-d1cbf2253a8d | -1.90359 | -47.93774 | 2025-09-19 04:44:00 | NOAA-21 | CONCÓRDIA DO PARÁ | PARÁ | Brasil | 1502756 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 69d5fd38-0187-3884-9df7-997e70d57f00 | -3.2785 | -49.14906 | 2025-09-19 04:44:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 26961ac3-f028-3d0c-8d38-34c1c453df64 | -4.63713 | -42.81633 | 2025-09-19 04:44:00 | NOAA-21 | UNIÃO | PIAUÍ | Brasil | 2211100 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |


[Clique aqui para ver as próximas entradas](README21.md)
