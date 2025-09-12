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

## Dados Diários - Página 26

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| ccfecf0a-727d-3822-9664-87d0315a391a | -20.01627 | -47.64406 | 2025-09-12 03:40:00 | NOAA-21 | CONQUISTA | MINAS GERAIS | Brasil | 3118205 | 31 | 33 | nan | nan | nan | Cerrado | 5.9 |
| a133e02e-8060-34a3-b6b4-cbf97d102999 | -23.15325 | -48.25636 | 2025-09-12 03:40:00 | NOAA-21 | BOFETE | SÃO PAULO | Brasil | 3506904 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 1657e91d-a8e4-3e41-a191-ba5fc967de52 | -19.97123 | -47.59355 | 2025-09-12 03:40:00 | NOAA-21 | CONQUISTA | MINAS GERAIS | Brasil | 3118205 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| a75544f7-6ba6-3e6f-9677-c4c6206a955d | -15.52938 | -48.55 | 2025-09-12 03:40:00 | NOAA-21 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 20e1383b-2e63-357f-9769-4926cd2dcb5e | -15.86979 | -48.33474 | 2025-09-12 03:40:00 | NOAA-21 | SANTO ANTÔNIO DO DESCOBERTO | GOIÁS | Brasil | 5219753 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |
| fffc8559-08bc-3fb7-8851-595e008db1c5 | -19.83989 | -44.58943 | 2025-09-12 03:40:00 | NOAA-21 | PARÁ DE MINAS | MINAS GERAIS | Brasil | 3147105 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 72423cbe-3349-3eae-a809-b82d12948647 | -23.10977 | -47.50008 | 2025-09-12 03:40:00 | NOAA-21 | PORTO FELIZ | SÃO PAULO | Brasil | 3540606 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| fc189c53-eb73-3610-83c7-1ce783e68eae | -19.20666 | -43.80043 | 2025-09-12 03:40:00 | NOAA-21 | BALDIM | MINAS GERAIS | Brasil | 3105004 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 3f15454f-6402-336d-955e-12ace3393d78 | -18.44566 | -47.18568 | 2025-09-12 03:40:00 | NOAA-21 | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 9cfbb112-8b7e-37f5-89f2-2f867dc3ef2c | -18.05916 | -45.43812 | 2025-09-12 03:40:00 | NOAA-21 | SÃO GONÇALO DO ABAETÉ | MINAS GERAIS | Brasil | 3161700 | 31 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 7062ea99-8925-3585-aa02-6b053d18a7d9 | -15.88153 | -48.17771 | 2025-09-12 03:40:00 | NOAA-21 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 4aa75a39-80d0-32a9-ae64-88d5c7082d02 | -15.53079 | -48.54346 | 2025-09-12 03:40:00 | NOAA-21 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 2615652e-3f43-3f6a-8670-39e6e2d6075e | -20.56062 | -46.93289 | 2025-09-12 03:40:00 | NOAA-21 | CÁSSIA | MINAS GERAIS | Brasil | 3115102 | 31 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 6d55b57d-9a25-3a37-bf21-a6d595ec3c3f | -17.75665 | -44.44229 | 2025-09-12 03:40:00 | NOAA-21 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ff7bdf75-e9ec-3fa9-bfc8-3f5118c1a362 | -19.99833 | -47.61883 | 2025-09-12 03:40:00 | NOAA-21 | CONQUISTA | MINAS GERAIS | Brasil | 3118205 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 1da73f73-62be-33d4-b697-2ffea3b85413 | -18.62265 | -46.47063 | 2025-09-12 03:40:00 | NOAA-21 | PATOS DE MINAS | MINAS GERAIS | Brasil | 3148004 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 4a9b464b-6d74-3369-8e1f-553a97de7ba8 | -19.23669 | -48.04433 | 2025-09-12 03:40:00 | NOAA-21 | UBERLÂNDIA | MINAS GERAIS | Brasil | 3170206 | 31 | 33 | nan | nan | nan | Cerrado | 9.3 |
| 62f0e236-60eb-3e2f-be37-f5d565a2c11a | -20.23493 | -49.26153 | 2025-09-12 03:40:00 | NOAA-21 | FRONTEIRA | MINAS GERAIS | Brasil | 3127008 | 31 | 33 | nan | nan | nan | Cerrado | 38.7 |
| 0c31ec43-1ad4-3654-bb2c-2aa350c7bc8f | -21.33528 | -45.03896 | 2025-09-12 03:40:00 | NOAA-21 | LAVRAS | MINAS GERAIS | Brasil | 3138203 | 31 | 33 | nan | nan | nan | Mata Atlântica | 9.3 |
| 6bab85d6-3078-3f8f-a856-e11e6107b6a2 | -18.81579 | -46.88242 | 2025-09-12 03:40:00 | NOAA-21 | PATROCÍNIO | MINAS GERAIS | Brasil | 3148103 | 31 | 33 | nan | nan | nan | Cerrado | 3.3 |
| b0a00218-18cb-3ad2-b908-891c0d06bd32 | -21.93927 | -47.5521 | 2025-09-12 03:40:00 | NOAA-21 | DESCALVADO | SÃO PAULO | Brasil | 3513702 | 35 | 33 | nan | nan | nan | Cerrado | 2.0 |
| bc1457dd-ccdc-336a-a57d-c5b2d03e0015 | -20.98555 | -46.98696 | 2025-09-12 03:40:00 | NOAA-21 | SÃO SEBASTIÃO DO PARAÍSO | MINAS GERAIS | Brasil | 3164704 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 53d05df0-a53c-3fe5-8379-03678f0772e5 | -21.94463 | -47.55334 | 2025-09-12 03:40:00 | NOAA-21 | DESCALVADO | SÃO PAULO | Brasil | 3513702 | 35 | 33 | nan | nan | nan | Cerrado | 2.0 |
| fd024f17-7a67-3fbd-bc7d-0151557a1fe7 | -16.28142 | -45.68221 | 2025-09-12 03:40:00 | NOAA-21 | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 2c0ba77f-9e10-30ec-bf77-0a779cb4b883 | -19.05291 | -48.74241 | 2025-09-12 03:40:00 | NOAA-21 | MONTE ALEGRE DE MINAS | MINAS GERAIS | Brasil | 3142809 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 40f1f443-e48f-3f94-8420-3d51a6baa857 | -17.54799 | -44.54729 | 2025-09-12 03:40:00 | NOAA-21 | VÁRZEA DA PALMA | MINAS GERAIS | Brasil | 3170800 | 31 | 33 | nan | nan | nan | Cerrado | 2.7 |
| ac08101a-884b-3bd7-ba67-f3e9d32e9e57 | -17.81982 | -46.7393 | 2025-09-12 03:40:00 | NOAA-21 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 5d3a060d-aa30-3b63-877a-f00d045786e4 | -21.6479 | -46.40633 | 2025-09-12 03:40:00 | NOAA-21 | BOTELHOS | MINAS GERAIS | Brasil | 3108404 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 1c2983db-abe5-33bb-8017-7c301c102740 | -18.44928 | -47.16908 | 2025-09-12 03:40:00 | NOAA-21 | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 13f27fad-8867-35af-898a-952ed801aa47 | -17.55658 | -44.55492 | 2025-09-12 03:40:00 | NOAA-21 | VÁRZEA DA PALMA | MINAS GERAIS | Brasil | 3170800 | 31 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 04f09ed3-bb01-34a9-8cb7-44a8075b505c | -23.3494 | -47.2368 | 2025-09-12 03:40:00 | NOAA-21 | ITU | SÃO PAULO | Brasil | 3523909 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| e2344a24-0537-303b-948d-7a8476b62abf | -20.12145 | -42.34925 | 2025-09-12 03:40:00 | NOAA-21 | RAUL SOARES | MINAS GERAIS | Brasil | 3154002 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.6 |
| a8a9b2c5-54ca-38c8-a903-6816cb4b9441 | -17.5529 | -44.54798 | 2025-09-12 03:40:00 | NOAA-21 | VÁRZEA DA PALMA | MINAS GERAIS | Brasil | 3170800 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 37cb14a6-a387-3901-a002-13c644e8c7c2 | -19.24443 | -48.03711 | 2025-09-12 03:40:00 | NOAA-21 | UBERABA | MINAS GERAIS | Brasil | 3170107 | 31 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 39aa1f6c-277e-3788-b695-54f65976d7ef | -17.33501 | -46.67048 | 2025-09-12 03:40:00 | NOAA-21 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 94fb93c7-2c4e-3923-adf1-8470e3f2863e | -17.35842 | -46.69707 | 2025-09-12 03:40:00 | NOAA-21 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 2.7 |
| a4c3b89c-04f7-38ce-88ae-0bfc4d2e086d | -22.19019 | -49.73877 | 2025-09-12 03:40:00 | NOAA-21 | GARÇA | SÃO PAULO | Brasil | 3516705 | 35 | 33 | nan | nan | nan | Mata Atlântica | 14.0 |
| 8529204a-10e0-3b30-9f84-9fb70c9c3e4b | -16.42661 | -45.69524 | 2025-09-12 03:40:00 | NOAA-21 | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| cb3944b1-d2f9-306a-a2af-e595b36feade | -20.08397 | -44.47874 | 2025-09-12 03:40:00 | NOAA-21 | ITAÚNA | MINAS GERAIS | Brasil | 3133808 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.4 |
| 39a3b2b8-6c6d-37f7-8bc8-fc51566f6e6b | -22.70679 | -48.69353 | 2025-09-12 03:40:00 | NOAA-21 | LENÇÓIS PAULISTA | SÃO PAULO | Brasil | 3526803 | 35 | 33 | nan | nan | nan | Cerrado | 1.8 |
| cd285b09-c362-3cf2-928e-9f1ae2490302 | -21.95609 | -47.55247 | 2025-09-12 03:40:00 | NOAA-21 | DESCALVADO | SÃO PAULO | Brasil | 3513702 | 35 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 3e124988-3d87-344e-93dc-d4bccc6de689 | -23.28158 | -46.47781 | 2025-09-12 03:40:00 | NOAA-21 | MAIRIPORÃ | SÃO PAULO | Brasil | 3528502 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| ff930b4f-0004-3bf0-81d6-52f827c308a4 | -17.72359 | -46.13395 | 2025-09-12 03:40:00 | NOAA-21 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 18ef3b25-02f6-36d6-8474-6672b83bd5b0 | -21.96117 | -47.56467 | 2025-09-12 03:40:00 | NOAA-21 | DESCALVADO | SÃO PAULO | Brasil | 3513702 | 35 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 934abd3f-13c7-305a-bdb6-5b8a72b450e7 | -19.64401 | -41.58661 | 2025-09-12 03:40:00 | NOAA-21 | POCRANE | MINAS GERAIS | Brasil | 3151909 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 5d8bc95d-3966-3671-b855-663a269bbe7d | -18.65224 | -47.6508 | 2025-09-12 03:40:00 | NOAA-21 | ESTRELA DO SUL | MINAS GERAIS | Brasil | 3124807 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f77011ad-d71d-366c-a51d-4709051e2722 | -17.54911 | -44.54158 | 2025-09-12 03:40:00 | NOAA-21 | VÁRZEA DA PALMA | MINAS GERAIS | Brasil | 3170800 | 31 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 7d0adf30-9064-395a-bb92-3f75929e33c2 | -21.32217 | -45.00824 | 2025-09-12 03:40:00 | NOAA-21 | LAVRAS | MINAS GERAIS | Brasil | 3138203 | 31 | 33 | nan | nan | nan | Mata Atlântica | 6.3 |
| 15d567ba-b37e-3c14-a69c-0581b97964df | -23.30838 | -46.61583 | 2025-09-12 03:40:00 | NOAA-21 | MAIRIPORÃ | SÃO PAULO | Brasil | 3528502 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 2368dea4-7770-3605-8bf0-194bacd7642f | -23.497 | -47.25992 | 2025-09-12 03:40:00 | NOAA-21 | MAIRINQUE | SÃO PAULO | Brasil | 3528403 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 39566635-04df-3616-ab2c-c86e5a39b405 | -22.86157 | -46.55908 | 2025-09-12 03:40:00 | NOAA-21 | BRAGANÇA PAULISTA | SÃO PAULO | Brasil | 3507605 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.9 |
| b725e4f8-3340-39db-bbbc-29f5eba71d0f | -22.69898 | -46.22509 | 2025-09-12 03:40:00 | NOAA-21 | ITAPEVA | MINAS GERAIS | Brasil | 3133600 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| 48a55a0c-3f9f-380d-a2fe-273fad1bb3ca | -22.82019 | -46.43493 | 2025-09-12 03:40:00 | NOAA-21 | VARGEM | SÃO PAULO | Brasil | 3556354 | 35 | 33 | nan | nan | nan | Mata Atlântica | 8.9 |
| e54a53c3-1c2f-3e74-8f31-81f1f01d3f33 | -19.19113 | -48.00725 | 2025-09-12 03:40:00 | NOAA-21 | UBERLÂNDIA | MINAS GERAIS | Brasil | 3170206 | 31 | 33 | nan | nan | nan | Cerrado | 10.7 |
| 4c30a8f2-06d6-36e5-bd8c-7a0261853c5d | -17.93852 | -46.93019 | 2025-09-12 03:40:00 | NOAA-21 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 004832eb-b6d6-381a-a0ff-1937051c189b | -18.61919 | -48.25599 | 2025-09-12 03:40:00 | NOAA-21 | ARAGUARI | MINAS GERAIS | Brasil | 3103504 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| 36b30482-3582-3817-a2f6-d40e7468f210 | -17.75437 | -44.45376 | 2025-09-12 03:40:00 | NOAA-21 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 8b63859a-b71a-3745-99c8-7ff6c8bee574 | -23.38544 | -47.01073 | 2025-09-12 03:40:00 | NOAA-21 | PIRAPORA DO BOM JESUS | SÃO PAULO | Brasil | 3539103 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 34ef66f2-ab1c-319c-8ca5-5daa356b29a4 | -20.58357 | -48.57713 | 2025-09-12 03:40:00 | NOAA-21 | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 357e309b-cbd9-3eb6-8998-39ab3815847f | -20.86974 | -46.50885 | 2025-09-12 03:40:00 | NOAA-21 | PASSOS | MINAS GERAIS | Brasil | 3147907 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| a31d4bb4-3621-3dc4-b0ae-22b96e7c62b8 | -18.05782 | -45.44462 | 2025-09-12 03:40:00 | NOAA-21 | SÃO GONÇALO DO ABAETÉ | MINAS GERAIS | Brasil | 3161700 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 57cdc7d3-e18f-3ae0-87c3-52751e35ad9a | -22.45254 | -46.1516 | 2025-09-12 03:40:00 | NOAA-21 | BOM REPOUSO | MINAS GERAIS | Brasil | 3107901 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 0471d8b1-0b46-34ff-9305-d1f1ea5523ee | -19.60954 | -43.5759 | 2025-09-12 03:40:00 | NOAA-21 | NOVA UNIÃO | MINAS GERAIS | Brasil | 3136603 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 0e929181-82e5-3583-8a09-e266dd20611c | -16.66374 | -47.62794 | 2025-09-12 03:40:00 | NOAA-21 | CRISTALINA | GOIÁS | Brasil | 5206206 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 6f895412-c4a8-3f7c-bf75-c6319b4d3a5f | -21.37197 | -45.17041 | 2025-09-12 03:40:00 | NOAA-21 | CARMO DA CACHOEIRA | MINAS GERAIS | Brasil | 3113909 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.8 |
| f37f1f59-78e5-33f5-a200-05d309a7d4a5 | -22.22926 | -49.60562 | 2025-09-12 03:40:00 | NOAA-21 | GARÇA | SÃO PAULO | Brasil | 3516705 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| 5bc2e397-e8a7-37a9-9ab7-efbdd53aea10 | -22.45381 | -46.14558 | 2025-09-12 03:40:00 | NOAA-21 | BOM REPOUSO | MINAS GERAIS | Brasil | 3107901 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 2beb35af-c3e3-3433-bec9-2abc6cead780 | -19.74917 | -46.0928 | 2025-09-12 03:40:00 | NOAA-21 | CÓRREGO DANTA | MINAS GERAIS | Brasil | 3119807 | 31 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 6b42ee19-a344-36d6-b763-ee0e9012d6e3 | -20.39691 | -42.19942 | 2025-09-12 03:40:00 | NOAA-21 | SANTA MARGARIDA | MINAS GERAIS | Brasil | 3157906 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| b424242f-ff62-3ec1-8e03-84fde0c817a9 | -22.8489 | -47.34266 | 2025-09-12 03:40:00 | NOAA-21 | SUMARÉ | SÃO PAULO | Brasil | 3552403 | 35 | 33 | nan | nan | nan | Mata Atlântica | 5.9 |
| 2ef52954-4e21-3274-9564-2dbda7905feb | -19.75135 | -46.09215 | 2025-09-12 03:40:00 | NOAA-21 | CÓRREGO DANTA | MINAS GERAIS | Brasil | 3119807 | 31 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 4d88a0cc-ebc1-3982-a5c4-1ca1217d6743 | -20.55911 | -46.92943 | 2025-09-12 03:40:00 | NOAA-21 | CÁSSIA | MINAS GERAIS | Brasil | 3115102 | 31 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 694ab773-f5a4-3e43-b2d9-08c2c5d8e451 | -19.8652 | -44.93739 | 2025-09-12 03:40:00 | NOAA-21 | NOVA SERRANA | MINAS GERAIS | Brasil | 3145208 | 31 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 16c27078-e0ad-3707-8b06-211ff038bbbf | -21.95763 | -47.54542 | 2025-09-12 03:40:00 | NOAA-21 | DESCALVADO | SÃO PAULO | Brasil | 3513702 | 35 | 33 | nan | nan | nan | Cerrado | 4.1 |
| edbe5a78-af7a-33c4-904a-4ed94810728a | -20.01341 | -47.65705 | 2025-09-12 03:40:00 | NOAA-21 | CONQUISTA | MINAS GERAIS | Brasil | 3118205 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 634187d4-2726-30c6-9829-6a09c401109d | -17.56507 | -44.55246 | 2025-09-12 03:40:00 | NOAA-21 | VÁRZEA DA PALMA | MINAS GERAIS | Brasil | 3170800 | 31 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 0cc1faba-29f9-3122-b4ef-2f4866f0ef89 | -23.14412 | -47.46876 | 2025-09-12 03:40:00 | NOAA-21 | PORTO FELIZ | SÃO PAULO | Brasil | 3540606 | 35 | 33 | nan | nan | nan | Mata Atlântica | 6.9 |
| 14ac6809-cfbf-3a6d-9d61-cc3ed11e8347 | -18.65188 | -47.65159 | 2025-09-12 03:40:00 | NOAA-21 | ESTRELA DO SUL | MINAS GERAIS | Brasil | 3124807 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 77c352d4-c3aa-317c-8cd3-1d2ca3096af5 | -18.44745 | -47.17746 | 2025-09-12 03:40:00 | NOAA-21 | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 7.1 |
| f2377d81-efe5-30a9-89d9-0b9bea062cdd | -17.6654 | -46.68163 | 2025-09-12 03:40:00 | NOAA-21 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 3.4 |
| e57e8ffc-3bd9-3f3e-b086-12a3064e2738 | -21.95293 | -47.56699 | 2025-09-12 03:40:00 | NOAA-21 | DESCALVADO | SÃO PAULO | Brasil | 3513702 | 35 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 6aa94d1a-31a6-3718-9f03-1f38652cf77c | -21.94748 | -47.55026 | 2025-09-12 03:40:00 | NOAA-21 | DESCALVADO | SÃO PAULO | Brasil | 3513702 | 35 | 33 | nan | nan | nan | Cerrado | 8.4 |
| 7eb402a7-b866-31b5-85ec-814bc836add4 | -19.19596 | -48.01305 | 2025-09-12 03:40:00 | NOAA-21 | UBERLÂNDIA | MINAS GERAIS | Brasil | 3170206 | 31 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 31177f00-ee48-3fc2-a477-578f84f9d4fa | -23.34811 | -47.19435 | 2025-09-12 03:40:00 | NOAA-21 | ITU | SÃO PAULO | Brasil | 3523909 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.5 |
| 274b8118-f221-3472-8fdc-4aa857ff2fc5 | -20.00948 | -46.91798 | 2025-09-12 03:40:00 | NOAA-21 | TAPIRA | MINAS GERAIS | Brasil | 3168101 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 62ff4495-920c-35cf-96cf-32a73ea9e01c | -21.33644 | -45.03329 | 2025-09-12 03:40:00 | NOAA-21 | LAVRAS | MINAS GERAIS | Brasil | 3138203 | 31 | 33 | nan | nan | nan | Mata Atlântica | 9.3 |
| a1006f36-e562-3b27-b4a6-58955e09e26b | -20.23475 | -49.25837 | 2025-09-12 03:40:00 | NOAA-21 | FRONTEIRA | MINAS GERAIS | Brasil | 3127008 | 31 | 33 | nan | nan | nan | Cerrado | 40.0 |
| ae96f0cb-655f-3ad3-8330-612a67db5d29 | -22.45528 | -46.14898 | 2025-09-12 03:40:00 | NOAA-21 | BOM REPOUSO | MINAS GERAIS | Brasil | 3107901 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.6 |
| efb6521f-550a-3230-9e28-b8b04fdcf516 | -16.42969 | -49.04036 | 2025-09-12 03:40:00 | NOAA-21 | TEREZÓPOLIS DE GOIÁS | GOIÁS | Brasil | 5221197 | 52 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 0b1f15ac-3d28-3cb0-83c3-e5b12bb52520 | -18.76034 | -48.19598 | 2025-09-12 03:40:00 | NOAA-21 | UBERLÂNDIA | MINAS GERAIS | Brasil | 3170206 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 07245ef4-2e5f-32d9-9aad-38d5c8d973eb | -18.02367 | -46.85948 | 2025-09-12 03:40:00 | NOAA-21 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 80c1e338-3f5a-3489-8532-f2e13b17543a | -21.49044 | -45.94683 | 2025-09-12 03:40:00 | NOAA-21 | ALFENAS | MINAS GERAIS | Brasil | 3101607 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.6 |
| 14be8886-0a5f-3d78-bcd4-fb915f95ee60 | -22.81522 | -46.43403 | 2025-09-12 03:40:00 | NOAA-21 | PEDRA BELA | SÃO PAULO | Brasil | 3536802 | 35 | 33 | nan | nan | nan | Mata Atlântica | 8.9 |
| 546a85e9-284c-3f22-99cc-eb758db7bada | -18.68286 | -47.67619 | 2025-09-12 03:40:00 | NOAA-21 | ESTRELA DO SUL | MINAS GERAIS | Brasil | 3124807 | 31 | 33 | nan | nan | nan | Cerrado | 5.2 |
| fa8e3588-bb31-3d54-9fdc-43b2051f7bf5 | -21.31993 | -45.01913 | 2025-09-12 03:40:00 | NOAA-21 | LAVRAS | MINAS GERAIS | Brasil | 3138203 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.5 |
| 38e4df66-928d-3a10-a532-25bb0d8a0500 | -20.23741 | -49.25069 | 2025-09-12 03:40:00 | NOAA-21 | FRONTEIRA | MINAS GERAIS | Brasil | 3127008 | 31 | 33 | nan | nan | nan | Cerrado | 24.0 |
| 18da8344-fc77-3a92-8a1c-408b5c650b50 | -20.27176 | -42.12935 | 2025-09-12 03:40:00 | NOAA-21 | MANHUAÇU | MINAS GERAIS | Brasil | 3139409 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| 4ce9d983-23d9-35e9-950b-77f2318d70ac | -18.9782 | -47.90142 | 2025-09-12 03:40:00 | NOAA-21 | INDIANÓPOLIS | MINAS GERAIS | Brasil | 3130705 | 31 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 43162b8c-545e-3691-b21f-f8481b28a2fa | -22.18295 | -49.74233 | 2025-09-12 03:40:00 | NOAA-21 | GARÇA | SÃO PAULO | Brasil | 3516705 | 35 | 33 | nan | nan | nan | Mata Atlântica | 8.0 |
| 07c10b23-25cc-3ced-8929-a8da0c5ab7a5 | -23.11342 | -47.5084 | 2025-09-12 03:40:00 | NOAA-21 | PORTO FELIZ | SÃO PAULO | Brasil | 3540606 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.9 |


[Clique aqui para ver as próximas entradas](README27.md)
