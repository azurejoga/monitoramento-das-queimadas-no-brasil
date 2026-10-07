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

## Dados Diários - Página 171

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 33b0e254-0f2b-3251-b6a3-9f0814cc729f | -5.72651 | -41.71803 | 2026-10-07 16:03:00 | NOAA-21 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 13.1 |
| e67bab92-1c92-3465-b45a-76bcb7c3265d | -4.32442 | -43.8135 | 2026-10-07 16:03:00 | NOAA-21 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 2df4e27e-01c9-3177-8d8e-a0d69c98a60b | -4.16557 | -38.4314 | 2026-10-07 16:03:00 | NOAA-21 | PACAJUS | CEARÁ | Brasil | 2309607 | 23 | 33 | nan | nan | nan | Caatinga | 4.3 |
| 454feb69-537f-3037-85b7-ed455d6b062a | -5.7334 | -41.73917 | 2026-10-07 16:03:00 | NOAA-21 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 50.3 |
| 159cd085-c994-374d-8530-ad426c5a06c1 | -3.78891 | -50.7551 | 2026-10-07 16:03:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 36.3 |
| 24bf9543-41d0-34f8-9343-8f776d34e416 | -4.68187 | -40.8233 | 2026-10-07 16:03:00 | NOAA-21 | IPUEIRAS | CEARÁ | Brasil | 2305902 | 23 | 33 | nan | nan | nan | Caatinga | 7.5 |
| b1532924-c107-387d-872b-427b9937e4e3 | -5.23662 | -48.39566 | 2026-10-07 16:03:00 | NOAA-21 | SÃO SEBASTIÃO DO TOCANTINS | TOCANTINS | Brasil | 1720309 | 17 | 33 | nan | nan | nan | Amazônia | 14.2 |
| bdd22c9f-c00b-308d-9b0f-4bea83e10ac5 | -5.44294 | -47.52856 | 2026-10-07 16:03:00 | NOAA-21 | IMPERATRIZ | MARANHÃO | Brasil | 2105302 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 7907316e-6374-3ce6-891b-fc3180b84d4f | -7.54607 | -46.73284 | 2026-10-07 16:03:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 10.5 |
| 3b87ddc0-4dd9-3b46-b013-31ba0adc5b40 | -3.35818 | -50.47546 | 2026-10-07 16:03:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 9ea5463c-1c6b-3773-97c9-06f1d03bd349 | -5.45052 | -42.89267 | 2026-10-07 16:03:00 | NOAA-21 | NAZÁRIA | PIAUÍ | Brasil | 2206720 | 22 | 33 | nan | nan | nan | Caatinga | 15.1 |
| e03cf5d9-636f-3dcb-8dc4-bfca51ce65e8 | -5.5064 | -42.83575 | 2026-10-07 16:03:00 | NOAA-21 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Caatinga | 47.8 |
| 1730afec-08de-3b07-8a2d-8fa59fc66f81 | -3.91425 | -44.13547 | 2026-10-07 16:03:00 | NOAA-21 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 30737f68-535c-3f8e-ac93-602e0091b85e | -6.59764 | -47.40244 | 2026-10-07 16:03:00 | NOAA-21 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 09af1b57-e545-3d11-b450-642798faddc1 | -3.65298 | -39.44043 | 2026-10-07 16:03:00 | NOAA-21 | TURURU | CEARÁ | Brasil | 2313559 | 23 | 33 | nan | nan | nan | Caatinga | 4.6 |
| 6cedd309-7088-3dd6-94b1-8de068e42cfc | -6.94487 | -45.26637 | 2026-10-07 16:03:00 | NOAA-21 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 23.3 |
| 0cc53ac8-b701-32a1-b5cc-0a7e9009bdf1 | -8.29729 | -51.2387 | 2026-10-07 16:03:00 | NOAA-21 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 14.2 |
| bc3e8dde-5232-3fe1-8a49-db1f16e16fa8 | -5.3411 | -46.1974 | 2026-10-07 16:03:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Amazônia | 12.6 |
| 93ccf21d-c844-3f34-81a0-6bf4ef3547c9 | -6.63454 | -43.77963 | 2026-10-07 16:03:00 | NOAA-21 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 94.2 |
| a262b0bb-6d43-32a0-9ff8-3fa794542445 | -8.28191 | -50.27593 | 2026-10-07 16:03:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 10.7 |
| 20d5d528-50fe-3e40-b6b0-f8bf7c8b1f8f | -7.76392 | -43.79197 | 2026-10-07 16:03:00 | NOAA-21 | ELISEU MARTINS | PIAUÍ | Brasil | 2203602 | 22 | 33 | nan | nan | nan | Caatinga | 6.6 |
| 01283679-98b7-37c5-8e1d-b5b62c757f79 | -7.75933 | -43.82159 | 2026-10-07 16:03:00 | NOAA-21 | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Caatinga | 12.2 |
| 6b109f61-c271-3fa2-8071-e5f27ba2c65f | -5.72329 | -41.69636 | 2026-10-07 16:03:00 | NOAA-21 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 36.6 |
| f0df6366-e1d4-3b9d-82bd-210e80a61020 | -3.88121 | -44.1132 | 2026-10-07 16:03:00 | NOAA-21 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 35.6 |
| b86bc42c-e8d8-3d69-b538-f89e76122281 | -5.26144 | -47.92743 | 2026-10-07 16:03:00 | NOAA-21 | SAMPAIO | TOCANTINS | Brasil | 1718808 | 17 | 33 | nan | nan | nan | Cerrado | 24.7 |
| 11946d23-c324-3e8f-8dcd-bbde092b3abc | -4.63075 | -48.86004 | 2026-10-07 16:03:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 22.9 |
| 70a2b19a-fa11-3cb8-ada4-9ad8f92a03ed | -6.43591 | -44.84359 | 2026-10-07 16:03:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 8.2 |
| 24fc0bb7-4c29-33e1-9d34-d4cf3addb4ea | -6.0262 | -51.71585 | 2026-10-07 16:03:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 68.4 |
| 4247bcc6-0650-3e10-82c7-6fd4c91f5350 | -6.05224 | -47.3268 | 2026-10-07 16:03:00 | NOAA-21 | RIBAMAR FIQUENE | MARANHÃO | Brasil | 2109551 | 21 | 33 | nan | nan | nan | Cerrado | 8.7 |
| 79cfe228-c740-3455-a726-8baa981cbb6a | -2.9878 | -42.83535 | 2026-10-07 16:03:00 | NOAA-21 | BARREIRINHAS | MARANHÃO | Brasil | 2101707 | 21 | 33 | nan | nan | nan | Cerrado | 12.9 |
| 54dcaa66-227c-36ec-95c1-16fb5f133141 | -4.63133 | -48.86422 | 2026-10-07 16:03:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 22.9 |
| 54edf0b8-67f4-3179-8736-3312057524ba | -4.03239 | -46.98178 | 2026-10-07 16:03:00 | NOAA-21 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 4d896bf4-6caa-36f5-8175-082c2ada91be | -7.77659 | -43.8192 | 2026-10-07 16:03:00 | NOAA-21 | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Caatinga | 22.3 |
| 09feff33-1c09-3828-aa34-8417c7d66ffa | -3.74225 | -39.53673 | 2026-10-07 16:03:00 | NOAA-21 | ITAPAJÉ | CEARÁ | Brasil | 2306306 | 23 | 33 | nan | nan | nan | Caatinga | 6.2 |
| ae932813-75ba-35cb-9593-954faa91e889 | -3.48939 | -39.50496 | 2026-10-07 16:03:00 | NOAA-21 | ITAPIPOCA | CEARÁ | Brasil | 2306405 | 23 | 33 | nan | nan | nan | Caatinga | 12.9 |
| afaec167-fbfe-3eda-b9b6-7b0dcf7f38b7 | -8.28117 | -50.27009 | 2026-10-07 16:03:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 10.7 |
| a7e67a97-6e1e-30af-99fc-52ab8670a58c | -7.00153 | -44.05597 | 2026-10-07 16:03:00 | NOAA-21 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 9.5 |
| f7df3c3a-f646-3e78-bf9e-155b3be68100 | -7.24195 | -43.76597 | 2026-10-07 16:03:00 | NOAA-21 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 59d2118a-18bc-38a7-b4c3-20b89971dd5d | -4.62116 | -45.52087 | 2026-10-07 16:03:00 | NOAA-21 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Cerrado | 5.8 |
| ca551844-70bf-3293-a3a6-7375877d4737 | -4.21449 | -44.61154 | 2026-10-07 16:03:00 | NOAA-21 | BACABAL | MARANHÃO | Brasil | 2101202 | 21 | 33 | nan | nan | nan | Cerrado | 32.3 |
| cadf81d9-ebb4-36ce-8ea2-7324d6a656d6 | -5.94196 | -45.38239 | 2026-10-07 16:03:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 11.1 |
| 1e96dd0b-f688-31c2-9e78-6f663a9569ac | -7.21926 | -44.29649 | 2026-10-07 16:03:00 | NOAA-21 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 13.0 |
| 3b660cc8-7317-3ae0-813e-dfe85d1584f1 | -7.39192 | -46.22013 | 2026-10-07 16:03:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 55.1 |
| 2f065347-566f-395d-932f-44a893c9366a | -6.69204 | -45.354 | 2026-10-07 16:03:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 26.7 |
| 3ca1aaec-5ab7-3300-8bf8-ecb60069aa9e | -3.93365 | -42.81343 | 2026-10-07 16:03:00 | NOAA-21 | BURITI | MARANHÃO | Brasil | 2102200 | 21 | 33 | nan | nan | nan | Caatinga | 9.7 |
| 29dc5f89-e7dd-3831-98ef-9bce4407025b | -3.50357 | -41.94443 | 2026-10-07 16:03:00 | NOAA-21 | CAXINGÓ | PIAUÍ | Brasil | 2202653 | 22 | 33 | nan | nan | nan | Caatinga | 39.7 |
| 53031c55-fe79-3e9a-9123-eed017ab790a | -3.88426 | -44.10503 | 2026-10-07 16:03:00 | NOAA-21 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 10.4 |
| 5372662e-0ff1-3501-b0b2-f3953d0f36b2 | -1.87821 | -45.43153 | 2026-10-07 16:03:00 | NOAA-21 | TURIAÇU | MARANHÃO | Brasil | 2112407 | 21 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 86ff8df2-d168-358f-9db1-e19eea3d4a4e | -3.73665 | -44.97159 | 2026-10-07 16:03:00 | NOAA-21 | CONCEIÇÃO DO LAGO-AÇU | MARANHÃO | Brasil | 2103554 | 21 | 33 | nan | nan | nan | Amazônia | 42.0 |
| 99f8a7db-6d20-3d78-8c50-c220fdb09f2b | -3.50483 | -41.95272 | 2026-10-07 16:03:00 | NOAA-21 | CAXINGÓ | PIAUÍ | Brasil | 2202653 | 22 | 33 | nan | nan | nan | Caatinga | 61.3 |
| ee7a7058-5644-351d-96a6-c1b7849d1fe9 | -5.24173 | -50.90598 | 2026-10-07 16:03:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 26.0 |
| 9de78baa-c1e3-37f0-a152-6ffca8b93396 | -3.18957 | -50.55836 | 2026-10-07 16:03:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 18.4 |
| 4feccfaf-cceb-3cc1-8e52-b940d035b0bf | -5.46674 | -45.68691 | 2026-10-07 16:03:00 | NOAA-21 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 6d1d8a5f-974a-3cfc-8537-06fe8dc66705 | -5.96977 | -40.91999 | 2026-10-07 16:03:00 | NOAA-21 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 71.6 |
| 35da2eed-d1e0-3f16-81fc-210b6b58b439 | -4.42454 | -43.73176 | 2026-10-07 16:03:00 | NOAA-21 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 35.0 |
| 05b29e1d-94cc-3669-bb3b-13cda534579d | -5.28441 | -42.74243 | 2026-10-07 16:03:00 | NOAA-21 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Caatinga | 10.6 |
| d1472bd6-bc3a-3faa-990f-b85a0e60bd7c | -4.93854 | -40.54816 | 2026-10-07 16:03:00 | NOAA-21 | TAMBORIL | CEARÁ | Brasil | 2313203 | 23 | 33 | nan | nan | nan | Caatinga | 16.4 |
| ffca7a6c-e0fb-369a-9c85-c351f1101e45 | -6.82119 | -38.52963 | 2026-10-07 16:03:00 | NOAA-21 | CAJAZEIRAS | PARAÍBA | Brasil | 2503704 | 25 | 33 | nan | nan | nan | Caatinga | 9.9 |
| 0eba61cc-bc7e-3c28-b8f2-8ca18e1aa2e7 | -1.88261 | -45.43093 | 2026-10-07 16:03:00 | NOAA-21 | TURIAÇU | MARANHÃO | Brasil | 2112407 | 21 | 33 | nan | nan | nan | Amazônia | 190.5 |
| cf42a9db-5b16-339f-ac44-e0fb218ee9a7 | -7.5332 | -45.87298 | 2026-10-07 16:03:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 19.2 |
| 88a51945-bc2e-3e8a-ae16-c977bdb7bd39 | -3.19964 | -42.9551 | 2026-10-07 16:03:00 | NOAA-21 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 24.7 |
| 28f1d184-683e-3cfc-a315-37283f81ac3a | -3.26216 | -50.39475 | 2026-10-07 16:03:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 11.4 |
| 0fba912d-7e15-3403-91c7-7fc39091bcac | -3.85044 | -42.2326 | 2026-10-07 16:03:00 | NOAA-21 | ESPERANTINA | PIAUÍ | Brasil | 2203701 | 22 | 33 | nan | nan | nan | Caatinga | 4.6 |
| 0433accd-ed4f-3799-99c3-35661ce99f9d | -3.44039 | -49.25347 | 2026-10-07 16:03:00 | NOAA-21 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 17.5 |
| 4b740adc-8014-32bc-80ad-ad47a873e36f | -4.3171 | -41.77623 | 2026-10-07 16:03:00 | NOAA-21 | PIRIPIRI | PIAUÍ | Brasil | 2208403 | 22 | 33 | nan | nan | nan | Caatinga | 15.5 |
| 7a7613d5-946d-3a07-ab39-2edbc1b9c4b7 | -3.75913 | -40.83532 | 2026-10-07 16:03:00 | NOAA-21 | FRECHEIRINHA | CEARÁ | Brasil | 2304509 | 23 | 33 | nan | nan | nan | Caatinga | 37.5 |
| 4ba9f534-fb12-312d-9583-c63c98a45140 | -3.874 | -44.12192 | 2026-10-07 16:03:00 | NOAA-21 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 21.1 |
| af34abcf-ae16-31a7-8a5c-3181d572c4b1 | -4.51096 | -42.89164 | 2026-10-07 16:03:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 13.2 |
| 2eb15fa6-3754-3fbe-872d-d78a01ae525f | -6.61706 | -37.87814 | 2026-10-07 16:03:00 | NOAA-21 | LAGOA | PARAÍBA | Brasil | 2508109 | 25 | 33 | nan | nan | nan | Caatinga | 20.7 |
| ec20a4bd-5c1e-36fc-9bd4-15ffff4399b4 | -7.57882 | -46.19864 | 2026-10-07 16:03:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 10.9 |
| 6d045fbc-e00b-34e0-b8d4-c8580dc9b639 | -3.96973 | -42.87102 | 2026-10-07 16:03:00 | NOAA-21 | BURITI | MARANHÃO | Brasil | 2102200 | 21 | 33 | nan | nan | nan | Caatinga | 8.4 |
| 11e388f1-69c0-3d9a-857f-29a174352c35 | -2.17129 | -48.36673 | 2026-10-07 16:03:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 12.7 |
| 92743ae3-c8a3-37ea-b575-b6427baa8f5e | -6.33591 | -43.74741 | 2026-10-07 16:03:00 | NOAA-21 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 10.5 |
| dd25019b-21db-3caa-b777-7b89358510a5 | -3.78518 | -45.24577 | 2026-10-07 16:03:00 | NOAA-21 | BELA VISTA DO MARANHÃO | MARANHÃO | Brasil | 2101772 | 21 | 33 | nan | nan | nan | Amazônia | 2.4 |
| e19baaac-cb29-3ad9-bcd0-01f22dd10467 | -7.10183 | -45.24022 | 2026-10-07 16:03:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 7.6 |
| c333daa8-0441-3fca-8e02-be47ee97dcd3 | -5.21209 | -48.34364 | 2026-10-07 16:03:00 | NOAA-21 | SÃO SEBASTIÃO DO TOCANTINS | TOCANTINS | Brasil | 1720309 | 17 | 33 | nan | nan | nan | Amazônia | 28.0 |
| d2ac9d53-a5af-3a96-9600-0cf68c66a033 | -7.55966 | -46.71445 | 2026-10-07 16:03:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 9.8 |
| 904dcb01-5ec6-397f-8f26-1f8506d4e5dd | -5.04392 | -49.76736 | 2026-10-07 16:03:00 | NOAA-21 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 14.0 |
| fc9ac8b7-f2ba-3fd0-a7e8-1d9f8787c6c8 | -5.85316 | -42.6567 | 2026-10-07 16:03:00 | NOAA-21 | LAGOINHA DO PIAUÍ | PIAUÍ | Brasil | 2205540 | 22 | 33 | nan | nan | nan | Caatinga | 76.0 |
| dbff34bd-183f-3204-acf4-993766926022 | -6.28805 | -43.65175 | 2026-10-07 16:03:00 | NOAA-21 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 10.7 |
| 334ddde5-a45b-36c8-b66e-b91d23035eec | -4.91615 | -43.21862 | 2026-10-07 16:03:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 16.8 |
| b3c55e98-66e9-302a-9cfe-e3dc2ee17259 | -4.3626 | -43.90933 | 2026-10-07 16:03:00 | NOAA-21 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 10.3 |
| 4cebe0bd-ad77-3b88-8781-dab831fbbaa6 | -3.78967 | -45.24514 | 2026-10-07 16:03:00 | NOAA-21 | SATUBINHA | MARANHÃO | Brasil | 2111722 | 21 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 6e94d4f5-0e59-3bec-8b2c-6df8b6f9ca8c | -3.55597 | -39.13626 | 2026-10-07 16:03:00 | NOAA-21 | SÃO GONÇALO DO AMARANTE | CEARÁ | Brasil | 2312403 | 23 | 33 | nan | nan | nan | Caatinga | 55.1 |
| ca44e7fb-372d-3137-bf6c-e86146acedb8 | -4.11574 | -41.78229 | 2026-10-07 16:03:00 | NOAA-21 | BRASILEIRA | PIAUÍ | Brasil | 2201960 | 22 | 33 | nan | nan | nan | Caatinga | 4.2 |
| 72985f2b-abae-32ab-83e9-d8ee7d1a2c89 | -4.45285 | -49.14788 | 2026-10-07 16:03:00 | NOAA-21 | JACUNDÁ | PARÁ | Brasil | 1503804 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| c6e1d8d3-97da-3b21-aff7-9bd3ef23bbd0 | -6.70295 | -44.01578 | 2026-10-07 16:03:00 | NOAA-21 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 9.1 |
| 23a5f574-da73-3ac7-b434-62645dd044d3 | -5.97799 | -40.92686 | 2026-10-07 16:03:00 | NOAA-21 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 8.1 |
| a634af75-c2f6-3c16-8ec5-24fd50677104 | -4.67893 | -40.82745 | 2026-10-07 16:03:00 | NOAA-21 | IPUEIRAS | CEARÁ | Brasil | 2305902 | 23 | 33 | nan | nan | nan | Caatinga | 39.8 |
| a51e33a1-24bf-34d9-b944-04d5934e344f | -6.65039 | -43.76955 | 2026-10-07 16:03:00 | NOAA-21 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 10.8 |
| ad8f783f-0898-39f1-8f6b-65f8716074f0 | -3.4107 | -40.03894 | 2026-10-07 16:03:00 | NOAA-21 | SANTANA DO ACARAÚ | CEARÁ | Brasil | 2312007 | 23 | 33 | nan | nan | nan | Caatinga | 6.3 |
| d33928dd-f959-330f-9f5f-0e04a7b016f9 | -6.97806 | -45.1273 | 2026-10-07 16:03:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 9c242e58-5715-3af4-98a6-651dace216a0 | -4.50486 | -43.68361 | 2026-10-07 16:03:00 | NOAA-21 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 15.1 |
| d1f945b5-0ff4-37f6-9b72-104125475e3c | -4.61652 | -45.52142 | 2026-10-07 16:03:00 | NOAA-21 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Cerrado | 8.8 |
| 8b55ed39-9005-3ddf-b57e-a6fe7936d01f | -5.73688 | -41.71209 | 2026-10-07 16:03:00 | NOAA-21 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 4.8 |
| b6dacf33-3c5d-3459-8eb2-753a042c8343 | -6.29488 | -44.90337 | 2026-10-07 16:03:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 28d3c4c3-7f7f-38a9-b046-ba372e55ab7b | -5.30061 | -41.87336 | 2026-10-07 16:03:00 | NOAA-21 | NOVO SANTO ANTÔNIO | PIAUÍ | Brasil | 2206951 | 22 | 33 | nan | nan | nan | Caatinga | 22.1 |
| cc2a6c6a-fb7d-311d-9c28-f2af24af9006 | -4.93572 | -38.84617 | 2026-10-07 16:03:00 | NOAA-21 | QUIXADÁ | CEARÁ | Brasil | 2311306 | 23 | 33 | nan | nan | nan | Caatinga | 18.5 |
| 2c041ab7-b41f-3406-b97d-aca124ae38d4 | -2.27397 | -48.75117 | 2026-10-07 16:03:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 606f3e47-7fde-3a13-98cc-edeaafd0570c | -3.1825 | -50.55412 | 2026-10-07 16:03:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 22.1 |


[Clique aqui para ver as próximas entradas](README172.md)
