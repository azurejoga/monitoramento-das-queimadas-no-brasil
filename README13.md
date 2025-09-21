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
| 2a802953-741e-3457-8b1c-598b7287b912 | -6.31772 | -42.37286 | 2025-09-21 04:08:00 | NOAA-21 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 05b6293a-d784-35a0-8ad8-68920a46c0e8 | -7.23643 | -46.62514 | 2025-09-21 04:08:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 6dd013ac-fedb-3248-b16e-d3c17e796949 | -10.78537 | -47.33552 | 2025-09-21 04:08:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 6aad1592-a95b-3c70-9291-208f0d71f4c2 | -4.84562 | -43.40188 | 2025-09-21 04:08:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 85f52da5-f910-344d-add8-abd00c03dd10 | -9.16744 | -44.62402 | 2025-09-21 04:08:00 | NOAA-21 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 12fefad5-ebf7-382a-b172-94e4d39fec8a | -9.17673 | -44.76485 | 2025-09-21 04:08:00 | NOAA-21 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 87f9a793-043e-39d7-8cdd-5eb44359e963 | -8.60381 | -45.33846 | 2025-09-21 04:08:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a529038e-6f51-385e-a23e-e72537415098 | -8.01413 | -45.72627 | 2025-09-21 04:08:00 | NOAA-21 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 7e564c79-d59b-3d9d-aedd-ffba57b1fef7 | -7.4272 | -44.54159 | 2025-09-21 04:08:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 76a979bf-f780-30e7-a983-38a6d36b9876 | -5.64924 | -51.46432 | 2025-09-21 04:08:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| cd4673d4-3323-38ab-a11b-22fbdde6cb60 | -7.91296 | -44.1023 | 2025-09-21 04:08:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 95c8fcb3-91ec-3255-8892-c5b60deb28ba | -7.91357 | -44.09853 | 2025-09-21 04:08:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 36ad3d66-5ce4-3a09-933d-f12b3c9cc05f | -8.84146 | -43.00701 | 2025-09-21 04:08:00 | NOAA-21 | SÃO BRAZ DO PIAUÍ | PIAUÍ | Brasil | 2209559 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 1fd253e4-e8d3-330a-a827-4be81df2af33 | -7.17872 | -42.2429 | 2025-09-21 04:08:00 | NOAA-21 | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 460aacd9-0a53-34ec-9b56-56f51ffd9729 | -5.78149 | -42.44865 | 2025-09-21 04:08:00 | NOAA-21 | BARRO DURO | PIAUÍ | Brasil | 2201408 | 22 | 33 | nan | nan | nan | Caatinga | 5.7 |
| eb2f80bd-937a-346a-8b58-3ed527482552 | -6.91228 | -44.75895 | 2025-09-21 04:08:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| e64afaf8-0a4d-320f-83a3-f71f80b59dbb | -16.87075 | -43.90377 | 2025-09-21 04:10:00 | NOAA-21 | MONTES CLAROS | MINAS GERAIS | Brasil | 3143302 | 31 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 4a3aabb9-cfb1-3b6d-a837-6e2a3a272e36 | -16.42438 | -43.51337 | 2025-09-21 04:10:00 | NOAA-21 | FRANCISCO SÁ | MINAS GERAIS | Brasil | 3126703 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 3b98b760-01a5-3df4-a127-56d81eb59770 | -14.9743 | -44.42586 | 2025-09-21 04:10:00 | NOAA-21 | ITACARAMBI | MINAS GERAIS | Brasil | 3132107 | 31 | 33 | nan | nan | nan | Cerrado | 3.0 |
| b908b7eb-1388-36d9-96df-9f9f974caf41 | -12.47259 | -46.69111 | 2025-09-21 04:10:00 | NOAA-21 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 100b6d58-463d-3379-851e-b1ca64b3ba0a | -13.64845 | -45.69863 | 2025-09-21 04:10:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 9b70cd84-f730-333b-b9bf-453d2413db71 | -11.29623 | -47.41499 | 2025-09-21 04:10:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 8.0 |
| db03a041-bb63-3426-bbe4-ee38c15d18b9 | -11.27841 | -47.40177 | 2025-09-21 04:10:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 83836841-54e3-3779-addf-f5b6fc0ab4f3 | -18.72987 | -43.88535 | 2025-09-21 04:10:00 | NOAA-21 | SANTANA DE PIRAPAMA | MINAS GERAIS | Brasil | 3158508 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 70f7f794-7f62-3556-b91b-f92b7ba23bbd | -11.62913 | -50.58746 | 2025-09-21 04:10:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 10.2 |
| 7f33a28e-7d52-3589-af19-75e9b5e049d1 | -14.61412 | -49.75939 | 2025-09-21 04:10:00 | NOAA-21 | GUARINOS | GOIÁS | Brasil | 5209457 | 52 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 34ec0c5b-3360-3801-9f56-ce30c68da817 | -13.68222 | -43.90421 | 2025-09-21 04:10:00 | NOAA-21 | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 2b91933c-a146-300e-a83a-7f814b38ab49 | -14.45554 | -46.51575 | 2025-09-21 04:10:00 | NOAA-21 | SIMOLÂNDIA | GOIÁS | Brasil | 5220686 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 06de05e7-bfee-397f-849c-665cac13c200 | -17.67128 | -44.08972 | 2025-09-21 04:10:00 | NOAA-21 | JOAQUIM FELÍCIO | MINAS GERAIS | Brasil | 3136405 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b7cc0f6a-bc7b-3b6d-962a-2ca94390c5c0 | -12.43503 | -45.1272 | 2025-09-21 04:10:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 4.5 |
| cde75e0e-b696-304e-a745-d1811b83046b | -11.43449 | -47.31422 | 2025-09-21 04:10:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 81e94ee8-8c47-3f51-8b4b-c3511f319f3c | -17.07532 | -43.19073 | 2025-09-21 04:10:00 | NOAA-21 | ITACAMBIRA | MINAS GERAIS | Brasil | 3132008 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| c216cb3e-ce17-3187-add8-e82022c4deca | -18.24047 | -43.79642 | 2025-09-21 04:10:00 | NOAA-21 | DIAMANTINA | MINAS GERAIS | Brasil | 3121605 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| df9ee7f1-9089-3e63-9f0f-cd3b6e5fac1c | -17.67514 | -44.08668 | 2025-09-21 04:10:00 | NOAA-21 | JOAQUIM FELÍCIO | MINAS GERAIS | Brasil | 3136405 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b9f9d3f5-6489-3217-b64d-f5cd1f8c1fb4 | -14.46411 | -46.50859 | 2025-09-21 04:10:00 | NOAA-21 | SIMOLÂNDIA | GOIÁS | Brasil | 5220686 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| c9625af5-596c-33a7-84ac-a55f8725b117 | -17.679 | -44.08364 | 2025-09-21 04:10:00 | NOAA-21 | JOAQUIM FELÍCIO | MINAS GERAIS | Brasil | 3136405 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| d18a7ee9-141a-3a82-9199-dcb68c800da4 | -14.44 | -47.56073 | 2025-09-21 04:10:00 | NOAA-21 | ALTO PARAÍSO DE GOIÁS | GOIÁS | Brasil | 5200605 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 36a6a08e-8a4f-3572-9c50-6b4548f4806b | -14.97213 | -44.41813 | 2025-09-21 04:10:00 | NOAA-21 | ITACARAMBI | MINAS GERAIS | Brasil | 3132107 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 5bddd333-676b-3bec-8463-a3b6c83c0dd3 | -12.41848 | -45.12066 | 2025-09-21 04:10:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 26a66286-63cc-335d-95e2-cb3086a81d69 | -15.53348 | -44.31374 | 2025-09-21 04:10:00 | NOAA-21 | PEDRAS DE MARIA DA CRUZ | MINAS GERAIS | Brasil | 3149150 | 31 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 712ca5c9-9cf7-370c-b3b5-31660f884383 | -12.28438 | -45.27205 | 2025-09-21 04:10:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| ddd6b23c-f0bf-3a22-a31d-1ef476e3caa7 | -13.35954 | -44.28395 | 2025-09-21 04:10:00 | NOAA-21 | SANTA MARIA DA VITÓRIA | BAHIA | Brasil | 2928109 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 58db9109-da03-3a5c-8963-24469591c354 | -11.29011 | -47.40388 | 2025-09-21 04:10:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 7.4 |
| ddb63653-4b09-343d-81a8-8bfeae684a88 | -13.04059 | -48.69719 | 2025-09-21 04:10:00 | NOAA-21 | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| e3984d8c-9044-3c26-bcca-4948bf1bad99 | -14.46553 | -46.50032 | 2025-09-21 04:10:00 | NOAA-21 | SIMOLÂNDIA | GOIÁS | Brasil | 5220686 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 633f86ae-9570-348d-a0ee-32503a7d55cc | -12.42815 | -45.12613 | 2025-09-21 04:10:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 215979d3-5200-3995-b836-af7b0c8132f2 | -11.61283 | -50.59538 | 2025-09-21 04:10:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 99880e01-603e-32c4-be36-202256439c08 | -12.07944 | -44.8083 | 2025-09-21 04:10:00 | NOAA-21 | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 62f842c2-94d7-3beb-9a01-8d214d13b1d6 | -13.87111 | -43.78688 | 2025-09-21 04:10:00 | NOAA-21 | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 84c1d9ee-af88-3dd3-8ad8-a870cc19a073 | -12.25068 | -49.17336 | 2025-09-21 04:10:00 | NOAA-21 | ALVORADA | TOCANTINS | Brasil | 1700707 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a0e8fca5-051a-3599-9394-e52877e1ad1c | -11.631 | -50.60427 | 2025-09-21 04:10:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 8f540f94-61fe-39b2-bee8-3e798055fbb2 | -18.98961 | -44.2307 | 2025-09-21 04:10:00 | NOAA-21 | CORDISBURGO | MINAS GERAIS | Brasil | 3118908 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| a65d0d27-3ed2-31d0-89bf-e8329042de06 | -11.28232 | -47.40244 | 2025-09-21 04:10:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 61c5ca91-363b-3722-abfa-e3d8aadff6eb | -15.26414 | -51.47708 | 2025-09-21 04:10:00 | NOAA-21 | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 12.7 |
| d7ca9dc7-40f9-3425-994e-2b3528ed578b | -11.64289 | -52.86108 | 2025-09-21 04:10:00 | NOAA-21 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 8277b43c-bb8b-3671-8850-9ac3e2ca18d9 | -12.71295 | -46.84937 | 2025-09-21 04:10:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 35d90354-0f63-3df2-8ea6-1bf0c25d6a14 | -17.16726 | -46.84354 | 2025-09-21 04:10:00 | NOAA-21 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 3.0 |
| ea28840b-a788-3dfe-9e99-2d98db40a734 | -17.44566 | -44.80967 | 2025-09-21 04:10:00 | NOAA-21 | PIRAPORA | MINAS GERAIS | Brasil | 3151206 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 75e451f9-f485-3693-bdd5-5128f1a6e467 | -13.36012 | -44.28035 | 2025-09-21 04:10:00 | NOAA-21 | SANTA MARIA DA VITÓRIA | BAHIA | Brasil | 2928109 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 77ccb9c2-fdd7-37c5-a1ca-39b391700965 | -12.41784 | -45.1245 | 2025-09-21 04:10:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 1c8acbe2-471a-350f-af57-42ef923ac34c | -11.43364 | -47.31917 | 2025-09-21 04:10:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 928aed6f-86b8-3f25-8150-416226d9e47c | -12.09651 | -44.85397 | 2025-09-21 04:10:00 | NOAA-21 | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| e3543fde-beb7-3a11-9869-4e141adfa1d0 | -13.51978 | -42.39424 | 2025-09-21 04:10:00 | NOAA-21 | PARAMIRIM | BAHIA | Brasil | 2923605 | 29 | 33 | nan | nan | nan | Caatinga | 0.3 |
| 5f497767-752b-37e1-99fa-b3fd4b136a9f | -19.51562 | -44.17001 | 2025-09-21 04:10:00 | NOAA-21 | PRUDENTE DE MORAIS | MINAS GERAIS | Brasil | 3153608 | 31 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 074765b6-41c5-380c-aa24-21fb43e8580c | -14.45761 | -46.50857 | 2025-09-21 04:10:00 | NOAA-21 | SIMOLÂNDIA | GOIÁS | Brasil | 5220686 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 6d8b85a8-7d93-32cc-bcd2-70a0206ec271 | -14.97705 | -44.43002 | 2025-09-21 04:10:00 | NOAA-21 | JANUÁRIA | MINAS GERAIS | Brasil | 3135209 | 31 | 33 | nan | nan | nan | Cerrado | 4.5 |
| fe986703-b781-3fb6-b53a-a2ac5a46399a | -12.71072 | -46.86244 | 2025-09-21 04:10:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 30c2a756-e43c-31e9-b201-19f8dddb605d | -13.6862 | -43.90179 | 2025-09-21 04:10:00 | NOAA-21 | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 12cc4e8d-b731-3a93-837d-26c0267c59d4 | -11.29879 | -47.49361 | 2025-09-21 04:10:00 | NOAA-21 | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| a2e14f9e-c66e-3631-93f5-02ae63d31313 | -12.51385 | -44.75339 | 2025-09-21 04:10:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 50b7c622-c8fa-3495-b038-ca74e9dd9cf6 | -12.71594 | -46.85424 | 2025-09-21 04:10:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 9f5ca5a3-2f88-38f6-959e-f0c2b8684fb5 | -15.7037 | -46.99885 | 2025-09-21 04:10:00 | NOAA-21 | CABECEIRAS | GOIÁS | Brasil | 5204003 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 5f5e594f-3f88-3cb7-af96-6bc6ece85ee8 | -12.42038 | -45.10918 | 2025-09-21 04:10:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 481d4ab8-675d-3823-81ef-ea1e4b48e8b1 | -14.6133 | -49.76387 | 2025-09-21 04:10:00 | NOAA-21 | GUARINOS | GOIÁS | Brasil | 5209457 | 52 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 986ce811-fa89-3d62-98c2-beb004820c9f | -14.45543 | -46.4997 | 2025-09-21 04:10:00 | NOAA-21 | SIMOLÂNDIA | GOIÁS | Brasil | 5220686 | 52 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 3b6d71d3-9b83-3a57-b9c9-1034f2f8e91a | -15.53421 | -42.17099 | 2025-09-21 04:10:00 | NOAA-21 | INDAIABIRA | MINAS GERAIS | Brasil | 3130655 | 31 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 17e6d5ef-0ead-35dd-95a1-dbe0ce79de6b | -14.45628 | -46.51147 | 2025-09-21 04:10:00 | NOAA-21 | SIMOLÂNDIA | GOIÁS | Brasil | 5220686 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| e16e02d5-8016-3185-b4da-09f8a232904e | -14.97545 | -44.41868 | 2025-09-21 04:10:00 | NOAA-21 | ITACARAMBI | MINAS GERAIS | Brasil | 3132107 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 208e0d17-32e6-3dfb-8992-e3beec7c5f88 | -13.54135 | -43.00504 | 2025-09-21 04:10:00 | NOAA-21 | RIACHO DE SANTANA | BAHIA | Brasil | 2926400 | 29 | 33 | nan | nan | nan | Caatinga | 6.8 |
| e36845f1-6e92-304c-8286-c628aa421477 | -14.79296 | -51.37894 | 2025-09-21 04:10:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| f9e637b9-e5f7-3f67-9b9d-09a29d13b270 | -12.71892 | -46.85912 | 2025-09-21 04:10:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 903a731e-eed6-30ff-9c94-29bc8c991680 | -14.79068 | -51.36413 | 2025-09-21 04:10:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 4527704c-ec5a-3223-989f-5bd53d945379 | -14.46486 | -46.50427 | 2025-09-21 04:10:00 | NOAA-21 | SIMOLÂNDIA | GOIÁS | Brasil | 5220686 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| adcd3325-9ba2-3151-9a73-b941a7a2a70d | -12.47105 | -46.70004 | 2025-09-21 04:10:00 | NOAA-21 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 100d421c-8d88-3482-be4b-fab3d28ce396 | -17.70644 | -44.0848 | 2025-09-21 04:10:00 | NOAA-21 | JOAQUIM FELÍCIO | MINAS GERAIS | Brasil | 3136405 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| f310d5b8-aca9-39df-9bcd-e7346b595891 | -19.13658 | -42.66089 | 2025-09-21 04:10:00 | NOAA-21 | JOANÉSIA | MINAS GERAIS | Brasil | 3136108 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| cc652cab-5024-3b51-b866-4dc563af78ce | -12.07541 | -44.81157 | 2025-09-21 04:10:00 | NOAA-21 | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 145d1342-7a60-3562-9b63-785f6b10a551 | -14.46198 | -46.49969 | 2025-09-21 04:10:00 | NOAA-21 | SIMOLÂNDIA | GOIÁS | Brasil | 5220686 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 36bfbcb5-946b-3e2f-80de-650ea6ea81c6 | -13.77555 | -43.70224 | 2025-09-21 04:10:00 | NOAA-21 | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 6cb155be-c1cf-30b7-bc45-08768d8e87a6 | -18.97204 | -41.09503 | 2025-09-21 04:10:00 | NOAA-21 | CUPARAQUE | MINAS GERAIS | Brasil | 3120839 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 04db63c8-db8a-351b-9c24-13499f78f5dc | -12.71147 | -46.83575 | 2025-09-21 04:10:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| c1207ebd-282d-33fb-a72d-913c216c1ccc | -19.18375 | -43.55756 | 2025-09-21 04:10:00 | NOAA-21 | SANTANA DO RIACHO | MINAS GERAIS | Brasil | 3159001 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 0bc29585-ac61-3a07-8b8c-e86ca606f8f4 | -13.36403 | -44.27732 | 2025-09-21 04:10:00 | NOAA-21 | SANTA MARIA DA VITÓRIA | BAHIA | Brasil | 2928109 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b093c047-4cd5-3098-93d1-b90a2adab572 | -13.86781 | -43.78633 | 2025-09-21 04:10:00 | NOAA-21 | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 8f8ee251-f2f9-34b6-be3a-e04467f05eb7 | -17.6823 | -44.0842 | 2025-09-21 04:10:00 | NOAA-21 | JOAQUIM FELÍCIO | MINAS GERAIS | Brasil | 3136405 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 3a476462-f464-30e8-a239-bc55c49e2eaa | -12.0745 | -44.83861 | 2025-09-21 04:10:00 | NOAA-21 | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 1999bf6d-f50d-35d4-a4b3-659853eebe3a | -18.23717 | -43.79585 | 2025-09-21 04:10:00 | NOAA-21 | DIAMANTINA | MINAS GERAIS | Brasil | 3121605 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| d7c42362-3f2f-3cc7-8d06-8bde1292b450 | -13.5375 | -43.00803 | 2025-09-21 04:10:00 | NOAA-21 | RIACHO DE SANTANA | BAHIA | Brasil | 2926400 | 29 | 33 | nan | nan | nan | Caatinga | 13.1 |
| 1c948db5-792a-3e8c-8848-4d8d8f85aef5 | -18.97627 | -41.09133 | 2025-09-21 04:10:00 | NOAA-21 | CUPARAQUE | MINAS GERAIS | Brasil | 3120839 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.1 |
| f08998f6-43a1-37a3-b27b-37fab40d7fab | -11.29787 | -47.4055 | 2025-09-21 04:10:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |


[Clique aqui para ver as próximas entradas](README14.md)
