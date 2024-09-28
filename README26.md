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
| 171b9f35-b0d5-36b9-984e-de00f1fdc697 | -8.10515 | -41.14857 | 2024-09-28 03:28:00 | NOAA-20 | PAULISTANA | PIAUÍ | Brasil | 2207801 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 15f4b2ab-3eb7-312c-ad37-0197b46ad05c | -8.43741 | -41.92873 | 2024-09-28 03:28:00 | NOAA-20 | CAPITÃO GERVÁSIO OLIVEIRA | PIAUÍ | Brasil | 2202455 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| ae4a9f68-d166-3492-ad53-ff1ea693a7a5 | -8.43674 | -41.93235 | 2024-09-28 03:28:00 | NOAA-20 | CAPITÃO GERVÁSIO OLIVEIRA | PIAUÍ | Brasil | 2202455 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| c7e82791-31d7-3e54-94e3-8ee01c35870f | -8.43595 | -41.9315 | 2024-09-28 03:28:00 | NOAA-20 | CAPITÃO GERVÁSIO OLIVEIRA | PIAUÍ | Brasil | 2202455 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 3fde6c43-4974-3441-88c6-78b1f3e4f2a0 | -4.86297 | -42.78323 | 2024-09-28 03:28:00 | NOAA-20 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Cerrado | 8.6 |
| d4ac57e0-eb78-33ae-8427-81d5a4c546e7 | -4.86208 | -42.78822 | 2024-09-28 03:28:00 | NOAA-20 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Cerrado | 8.6 |
| 7306ea4a-d457-3764-9109-d55d345c7919 | -6.32455 | -43.42099 | 2024-09-28 03:28:00 | NOAA-20 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 5dc9b60f-879b-34c0-941a-fadfa0d04454 | -6.31837 | -43.41974 | 2024-09-28 03:28:00 | NOAA-20 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 119b88e8-92c8-3d7c-8245-90053e657532 | -6.31751 | -43.4244 | 2024-09-28 03:28:00 | NOAA-20 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 2ba3946d-f6ca-36bb-9b78-c00b2e72cd18 | -6.31423 | -43.41744 | 2024-09-28 03:28:00 | NOAA-20 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 78717db6-2b25-3dec-aa24-e4e240facdca | -6.3134 | -43.42208 | 2024-09-28 03:28:00 | NOAA-20 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 8872aaa6-7ac8-3cf3-8a02-7c7548e63dc1 | -6.313 | -43.4141 | 2024-09-28 03:28:00 | NOAA-20 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 87595045-18ec-3557-b3fd-b0b8859e8899 | -6.31257 | -43.42673 | 2024-09-28 03:28:00 | NOAA-20 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 6bcde213-46b6-3f8a-97cd-12967ae6b34d | -6.31215 | -43.41872 | 2024-09-28 03:28:00 | NOAA-20 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 13637017-a77f-3f84-a135-8be67f8b2a79 | -6.31129 | -43.42335 | 2024-09-28 03:28:00 | NOAA-20 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 6.8 |
| acd22aa0-e698-366e-a9e9-8faf38fd6a08 | -6.31042 | -43.428 | 2024-09-28 03:28:00 | NOAA-20 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 64c8ebce-1332-34e7-982b-d3614daed358 | -6.20058 | -43.27456 | 2024-09-28 03:28:00 | NOAA-20 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c47f14a5-a69d-35a2-8508-05b6f39ee70e | -6.19974 | -43.27927 | 2024-09-28 03:28:00 | NOAA-20 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 38c49d07-d751-3a0b-8ee1-fd5665adb37f | -6.1751 | -43.45198 | 2024-09-28 03:28:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| b338e8db-f1fe-30d5-a990-d50a99a9bf2a | -6.17411 | -43.45752 | 2024-09-28 03:28:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 64d7ff06-203f-35b0-aa98-d07736031462 | -6.1698 | -43.44569 | 2024-09-28 03:28:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 218876a6-2d8e-3aa7-9317-0c587bbb55f1 | -6.16881 | -43.45121 | 2024-09-28 03:28:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| cec05745-f4ce-357f-8df0-e52787b789de | -6.16345 | -43.44527 | 2024-09-28 03:28:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| b39795c9-5956-3bd5-a72a-fdfa06bcaf11 | -5.30288 | -43.07215 | 2024-09-28 03:28:00 | NOAA-20 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| a19e3314-1e79-38d4-a643-27bf9801638e | -6.72292 | -43.56431 | 2024-09-28 03:28:00 | NOAA-20 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| c2b7ae13-f649-3852-a5bb-9fb742853222 | -6.72148 | -43.5605 | 2024-09-28 03:28:00 | NOAA-20 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| a89d9d8d-8500-3718-8b96-9e4b8a986afd | -6.72054 | -43.56552 | 2024-09-28 03:28:00 | NOAA-20 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| a7462d34-3a5f-375b-857a-f7cde759e719 | -6.71672 | -43.5631 | 2024-09-28 03:28:00 | NOAA-20 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 378a6567-67fa-3838-b4a6-8d7c72e44037 | -6.71526 | -43.55935 | 2024-09-28 03:28:00 | NOAA-20 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ed8d51c3-649c-3861-8c56-afcb360bf13a | -6.66433 | -42.58669 | 2024-09-28 03:28:00 | NOAA-20 | ARRAIAL | PIAUÍ | Brasil | 2201002 | 22 | 33 | nan | nan | nan | Caatinga | 3.2 |
| 4483b6c0-e892-3559-a8e9-efa966ac8f4a | -6.55647 | -43.1554 | 2024-09-28 03:28:00 | NOAA-20 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 1e47362d-0a58-3d4d-afd7-0b36d39bc0f6 | -9.12368 | -43.15724 | 2024-09-28 03:28:00 | NOAA-20 | JUREMA | PIAUÍ | Brasil | 2205532 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| e4b91146-ffb6-3fb4-9aeb-458ce9a2e3d2 | -10.27924 | -43.57 | 2024-09-28 03:28:00 | NOAA-20 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 3febc36a-9602-3f8b-bdc8-2c21bba6e5b4 | -10.27844 | -43.57424 | 2024-09-28 03:28:00 | NOAA-20 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f04fc9b6-822b-3f2c-adf6-2b6093c79e42 | -10.27791 | -43.56884 | 2024-09-28 03:28:00 | NOAA-20 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| f9087a6e-e804-30d7-871d-c1adfa01b436 | -10.27708 | -43.57309 | 2024-09-28 03:28:00 | NOAA-20 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 15dcaa46-4cb1-3e4e-bd6c-dbf50055e61f | -10.27626 | -43.57732 | 2024-09-28 03:28:00 | NOAA-20 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 5f7ebb61-9ae6-3110-b243-91fffd9808a0 | -10.2734 | -43.56873 | 2024-09-28 03:28:00 | NOAA-20 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 53578a51-1633-3a63-8c77-9e3475519581 | -10.2726 | -43.57294 | 2024-09-28 03:28:00 | NOAA-20 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 14e68825-5e25-3647-8e34-1b735b8af39e | -10.2718 | -43.57719 | 2024-09-28 03:28:00 | NOAA-20 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 99bcf391-5929-3af2-b3fe-09b2478baea5 | -10.27124 | -43.57183 | 2024-09-28 03:28:00 | NOAA-20 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| f223b2c8-61d0-39da-8b2f-b7da460ba710 | -10.27042 | -43.57606 | 2024-09-28 03:28:00 | NOAA-20 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 07e217bb-44cb-3bed-aa65-0947fc544a0a | -10.26959 | -43.58027 | 2024-09-28 03:28:00 | NOAA-20 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 26e36c1b-d13c-3d52-9abc-4293db6b909f | -10.26877 | -43.58443 | 2024-09-28 03:28:00 | NOAA-20 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 77a6d24f-0be4-320f-82ce-49e42d805824 | -10.26797 | -43.58854 | 2024-09-28 03:28:00 | NOAA-20 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 9ee9c170-6851-3998-b4a0-69b8e1644e58 | -10.26595 | -43.57594 | 2024-09-28 03:28:00 | NOAA-20 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 5d431902-11e7-3980-99bd-7143b088dfc7 | -10.26517 | -43.58011 | 2024-09-28 03:28:00 | NOAA-20 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 8e6b0d92-1385-3633-9ed4-7c97f7a50570 | -10.26439 | -43.58422 | 2024-09-28 03:28:00 | NOAA-20 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 57ce99ea-a7a9-3860-a10b-8de4134004b6 | -10.26375 | -43.57901 | 2024-09-28 03:28:00 | NOAA-20 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| e978ca47-6cec-3c29-86b4-e248fbf9646d | -10.26361 | -43.58832 | 2024-09-28 03:28:00 | NOAA-20 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 75780332-4d48-3164-819f-74ff820e6196 | -10.26294 | -43.58311 | 2024-09-28 03:28:00 | NOAA-20 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 33c9aa4a-08fd-3629-b128-35aa20ff8cff | -10.26213 | -43.5872 | 2024-09-28 03:28:00 | NOAA-20 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 043121a8-3532-348e-9865-2c60284d8d50 | -10.25931 | -43.57888 | 2024-09-28 03:28:00 | NOAA-20 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 61ac26e9-d3b2-3235-b3de-c2d107dba405 | -10.25871 | -43.57365 | 2024-09-28 03:28:00 | NOAA-20 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 1c247d49-f08a-3e63-a8d3-e68994e4108a | -10.25789 | -43.57782 | 2024-09-28 03:28:00 | NOAA-20 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| e4bb95a0-bf6b-333b-8f7b-d67a6c183f55 | -10.25504 | -43.56933 | 2024-09-28 03:28:00 | NOAA-20 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c972c4ae-95a9-3def-a99d-06c315c4e889 | -10.25425 | -43.57352 | 2024-09-28 03:28:00 | NOAA-20 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| f202fdc8-e7b0-36dc-ba86-a20aac6849bb | -10.25346 | -43.57769 | 2024-09-28 03:28:00 | NOAA-20 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| df07b8d0-e501-302d-ab79-c85f2ac79d73 | -11.21304 | -43.32634 | 2024-09-28 03:28:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 4ee8a4d5-c415-3350-a1cc-5aeb18e9310d | -10.98948 | -44.42834 | 2024-09-28 03:28:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 5.1 |
| e8e15c2f-d6a1-3a3b-844a-94057821f2b1 | -10.98926 | -44.42917 | 2024-09-28 03:28:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 351fde94-97dd-34b7-ae5c-9496eee18eed | -10.98857 | -44.43309 | 2024-09-28 03:28:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 9b8df104-451d-3cc8-866f-a3cf4aed56c1 | -10.98832 | -44.43391 | 2024-09-28 03:28:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 7.5 |
| d4f9f416-780f-38fe-aa66-353cd4c43702 | -10.98765 | -44.43785 | 2024-09-28 03:28:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 34c061fb-4c65-3c8b-90a9-a7a769af7db9 | -10.98737 | -44.43866 | 2024-09-28 03:28:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 32d1a325-8f09-3fed-81a1-579713d73399 | -4.65537 | -43.76637 | 2024-09-28 03:28:00 | NOAA-20 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| bde54da1-93ed-3611-a143-c304f93b01c7 | -6.50061 | -43.62881 | 2024-09-28 03:28:00 | NOAA-20 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| fc81ffa4-8169-3569-bc01-17ec6d08048f | -6.3917 | -44.78333 | 2024-09-28 03:28:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 8c142a38-58df-332f-9ad9-e93cf3ee7e1e | -6.39059 | -44.78918 | 2024-09-28 03:28:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| a213927f-f2bf-38d4-ae78-884e416e860e | -6.38843 | -44.78671 | 2024-09-28 03:28:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 5.8 |
| c4319487-a358-3101-8fe0-aeeba791e944 | -6.38496 | -44.78217 | 2024-09-28 03:28:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 14f83f4f-4a9f-31bc-9245-e8ed31dcfbd7 | -6.38383 | -44.78819 | 2024-09-28 03:28:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 8e1e0800-4b8e-37cb-92fd-80407fde1272 | -5.87992 | -43.86636 | 2024-09-28 03:28:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 963115e5-dec1-3a63-8ebb-1f4ed1da6834 | -5.87899 | -43.87152 | 2024-09-28 03:28:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 35c3a084-b5c9-379a-b84a-2c2a232b6666 | -5.87351 | -43.86511 | 2024-09-28 03:28:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 81d10a07-f11c-3d56-8625-5726e70f17c1 | -5.87258 | -43.87026 | 2024-09-28 03:28:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 8b5bb5a7-ee70-3fdd-a628-03d507297083 | -5.83729 | -43.65453 | 2024-09-28 03:28:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| e6b5753b-9fde-3c09-a29e-3205277accd7 | -5.83638 | -43.65969 | 2024-09-28 03:28:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| d06e878b-c601-325b-b07c-8bd2ff6e3390 | -5.83331 | -43.6524 | 2024-09-28 03:28:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| d952a440-c2c1-36c9-9b2a-8083293db351 | -5.83236 | -43.65755 | 2024-09-28 03:28:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 07878abc-38fe-3a45-9b9a-af34dd2f6c64 | -5.83003 | -43.65854 | 2024-09-28 03:28:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 65fa378a-d3b4-32d0-b414-bf426f0e9b31 | -5.80556 | -43.98302 | 2024-09-28 03:28:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 2ca47f7e-ced3-37c3-a1b8-03501ca1af80 | -5.40219 | -43.43765 | 2024-09-28 03:28:00 | NOAA-20 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 3b3bd370-cdab-3a4e-967d-bdd4efe97333 | -6.09967 | -44.70454 | 2024-09-28 03:28:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 488981fb-2cc4-30d0-bc00-928983560da9 | -6.09849 | -44.71084 | 2024-09-28 03:28:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 79306225-dacc-3cf6-a7ef-f8e7d2e813ed | -6.0974 | -44.7038 | 2024-09-28 03:28:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 22c30205-2c2d-3eee-8af9-9fae1b86af57 | -6.09178 | -44.70955 | 2024-09-28 03:28:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 8c29c17f-8aea-318b-b01a-1cbf6a8169b4 | -6.08953 | -44.70889 | 2024-09-28 03:28:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 2bc79996-db39-394d-9c3e-3ac52afb68ff | -5.98033 | -44.56865 | 2024-09-28 03:28:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 3016e0b2-69e2-3fed-b575-755987f99438 | -5.9736 | -44.5677 | 2024-09-28 03:28:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 9cd37e00-7451-357a-aad1-0803458edc16 | -5.79299 | -44.85887 | 2024-09-28 03:28:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 17a878a5-b1d9-3e3f-8173-1de5dc7d454b | -5.78617 | -44.85766 | 2024-09-28 03:28:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| db66386b-5777-3baa-85cf-f20ecbeb240d | -5.76322 | -44.4743 | 2024-09-28 03:28:00 | NOAA-20 | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| c891bceb-4377-3068-8608-34ceb5327496 | -5.75763 | -44.46716 | 2024-09-28 03:28:00 | NOAA-20 | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 12e522f8-3d08-3a63-93db-867c21d6880b | -5.71512 | -44.81608 | 2024-09-28 03:28:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 59f5a106-ba81-378a-a961-8ffbf1765b1c | -5.71395 | -44.82253 | 2024-09-28 03:28:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| dd75c5f6-56fe-3b85-afb5-04c802ce3439 | -5.5545 | -44.67964 | 2024-09-28 03:28:00 | NOAA-20 | SANTA FILOMENA DO MARANHÃO | MARANHÃO | Brasil | 2109759 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| aa0ec1a6-2e40-39bd-b4a3-8cd06393567a | -5.55036 | -44.67461 | 2024-09-28 03:28:00 | NOAA-20 | SANTA FILOMENA DO MARANHÃO | MARANHÃO | Brasil | 2109759 | 21 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 86d7e6ec-4ac6-3eb3-8ecf-a0d620ff096f | -5.54922 | -44.68078 | 2024-09-28 03:28:00 | NOAA-20 | SANTA FILOMENA DO MARANHÃO | MARANHÃO | Brasil | 2109759 | 21 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 45c93f39-f8f4-3006-9338-1445ae9a99de | -5.54779 | -44.67811 | 2024-09-28 03:28:00 | NOAA-20 | SANTA FILOMENA DO MARANHÃO | MARANHÃO | Brasil | 2109759 | 21 | 33 | nan | nan | nan | Cerrado | 4.8 |


[Clique aqui para ver as próximas entradas](README27.md)
