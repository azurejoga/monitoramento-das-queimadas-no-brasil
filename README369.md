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

## Dados Diários - Página 369

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| fa6dc4ea-0ce9-3b8d-940e-7910b0850b5b | -5.97269 | -55.3628 | 2026-10-08 16:39:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 4868617e-d3e9-395d-a5c7-4d8c6a359939 | -5.37874 | -44.1849 | 2026-10-08 16:39:00 | NOAA-20 | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | 9.9 |
| 00964f9e-0ff6-3e00-bcb9-5d310db958b5 | -2.81932 | -59.24768 | 2026-10-08 16:39:00 | NOAA-20 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 29.9 |
| 1410c95a-5d62-33b7-94e8-08bed328e3e9 | -3.91123 | -55.7479 | 2026-10-08 16:39:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 11.9 |
| bdd62221-1d4f-342c-8e45-f07b9307c48d | -4.50095 | -43.6189 | 2026-10-08 16:39:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| df769d7c-a65d-3adb-a95a-da5d788d9c8f | -3.17576 | -53.82621 | 2026-10-08 16:39:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 3eb012a4-9c94-392b-a09b-3fb66aa98ec6 | -3.05057 | -54.03204 | 2026-10-08 16:39:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 816666ba-1830-39a3-9e56-2e5ee11654bb | -2.9956 | -43.28533 | 2026-10-08 16:39:00 | NOAA-20 | PRIMEIRA CRUZ | MARANHÃO | Brasil | 2109403 | 21 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 19bd08a4-6a59-38b6-bb04-ddc82e99c703 | -7.22519 | -55.08778 | 2026-10-08 16:39:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| a82082a5-29da-3679-8ff6-a713499b90b2 | -3.00477 | -54.04895 | 2026-10-08 16:39:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 15.1 |
| b7fba61d-b275-3ffd-8f2d-080addbf4809 | -7.18641 | -52.62811 | 2026-10-08 16:39:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 13.9 |
| 99b9816b-881b-3e60-b0e5-15851dc60d76 | -3.51599 | -59.09114 | 2026-10-08 16:39:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 3.7 |
| a0581f64-9fae-37f9-9c62-22b096bd7ede | -4.82734 | -45.62304 | 2026-10-08 16:39:00 | NOAA-20 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 7.0 |
| f7f3b89b-2208-3f9b-bb95-006a26eab928 | -5.62591 | -43.04063 | 2026-10-08 16:39:00 | NOAA-20 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 5.9 |
| 1afdb3cf-c1ee-37f6-a321-1f05caf2e6ea | -3.77358 | -44.36145 | 2026-10-08 16:39:00 | NOAA-20 | MATÕES DO NORTE | MARANHÃO | Brasil | 2106631 | 21 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 98cf3ca1-5279-3e89-b85d-f4619cf9e6b3 | -3.74772 | -59.44781 | 2026-10-08 16:39:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 63bd7241-7b4b-34e7-9383-620a7978c50d | -1.8898 | -54.38629 | 2026-10-08 16:39:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 13.3 |
| 675980b6-eec9-3cf8-a1c3-1a9f73d3065c | -3.13908 | -40.07845 | 2026-10-08 16:39:00 | NOAA-20 | MARCO | CEARÁ | Brasil | 2307809 | 23 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 142924af-29cb-3568-93d4-1d00a95613b7 | -3.31702 | -54.05038 | 2026-10-08 16:39:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 16.4 |
| febe4de8-b8a6-3f96-8281-fc506b525a8e | -6.15135 | -52.64548 | 2026-10-08 16:39:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 15.5 |
| e830d663-cdae-3f7b-9e8d-dc312d25d2bc | -4.57342 | -43.87372 | 2026-10-08 16:39:00 | NOAA-20 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 5.4 |
| ad623f8d-a8ea-37f8-b898-c467d9c0c18e | -5.45174 | -42.90899 | 2026-10-08 16:39:00 | NOAA-20 | NAZÁRIA | PIAUÍ | Brasil | 2206720 | 22 | 33 | nan | nan | nan | Caatinga | 9.4 |
| b6b73cbe-cebc-3e0e-8805-81c52aaba9b7 | -6.22609 | -52.78357 | 2026-10-08 16:39:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 19.4 |
| e7daf963-59cc-3e29-b574-cf13183ee4a9 | -4.92254 | -43.04101 | 2026-10-08 16:39:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 578bb1bc-f3bd-3587-bf47-48ae4ae59902 | -3.15003 | -43.02811 | 2026-10-08 16:39:00 | NOAA-20 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 6.8 |
| e46eedec-df6e-3d31-98ec-1f829be62c52 | -4.0883 | -44.10682 | 2026-10-08 16:39:00 | NOAA-20 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 34.1 |
| 4188b884-61d5-3938-b251-1fe13fcbf45c | -6.36156 | -52.1909 | 2026-10-08 16:39:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| d4c7e1f8-16df-3f1a-9831-26f9b1980823 | -3.03014 | -57.6398 | 2026-10-08 16:39:00 | NOAA-20 | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | 18.7 |
| 109e8fd2-70df-37b9-99c6-0a8c2707f9cc | -2.99948 | -57.73809 | 2026-10-08 16:39:00 | NOAA-20 | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | 5.9 |
| f57ec242-e612-3a77-bbca-1aa002b618c6 | -3.0164 | -54.06263 | 2026-10-08 16:39:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 18.3 |
| 436f7f8b-191c-3215-882a-d01fbd410429 | -5.70976 | -53.48734 | 2026-10-08 16:39:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 31.9 |
| eb1ee710-4c78-3bfd-8b0e-d849f4e29c89 | -7.00108 | -59.1021 | 2026-10-08 16:39:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 14.9 |
| edf3d288-bd9b-3fc7-8d60-c5dec6dacc03 | -5.87853 | -45.94874 | 2026-10-08 16:39:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 9.0 |
| a3e0d43b-0eaf-33a2-8a5f-bdaf3af98973 | -6.14598 | -53.56365 | 2026-10-08 16:39:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| ffd45b48-f57a-38b6-8f16-2d8a18031ff7 | -3.01582 | -54.74214 | 2026-10-08 16:39:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 21.2 |
| fd94e74e-a0cf-38e7-b8da-419150e5f582 | -5.09832 | -46.2168 | 2026-10-08 16:39:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 52.5 |
| a592fd8f-e8d0-3488-adb5-e64cacfbbee7 | -3.02368 | -54.04621 | 2026-10-08 16:39:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 27.0 |
| 20cc8d46-0f31-3862-ad4e-ae51e37f58d5 | -4.57654 | -55.99767 | 2026-10-08 16:39:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 29.6 |
| 0d97d5ea-f827-3f59-8b95-f1ff5be8d680 | -1.96362 | -56.3093 | 2026-10-08 16:39:00 | NOAA-20 | TERRA SANTA | PARÁ | Brasil | 1507979 | 15 | 33 | nan | nan | nan | Amazônia | 7.2 |
| a05e267a-db72-3a1f-9fdd-81793da5128b | -4.29502 | -48.60381 | 2026-10-08 16:39:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 37.2 |
| 3381fb29-b438-3841-9c17-49555ac7ab5b | -5.68985 | -53.44965 | 2026-10-08 16:39:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 9.3 |
| 510635d0-18b8-3577-bf35-7ccd777e7148 | -3.39102 | -50.21123 | 2026-10-08 16:39:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 13.3 |
| e7975b6e-ecad-3b30-94ab-07c2e2d671f9 | -3.00539 | -54.06168 | 2026-10-08 16:39:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 17.0 |
| f7c05973-7e65-3c7e-bf05-efe71376d1b0 | -7.19098 | -52.62752 | 2026-10-08 16:39:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 13.9 |
| abda0743-604f-32c4-b102-dff13a33091c | -5.96268 | -53.54691 | 2026-10-08 16:39:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 14.4 |
| 26db1681-9f46-3f84-899f-84fd63efb150 | -3.40735 | -57.99908 | 2026-10-08 16:39:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 8.4 |
| d55ad4df-b061-3826-b64c-ffb51888534c | -3.52983 | -44.84502 | 2026-10-08 16:39:00 | NOAA-20 | VITÓRIA DO MEARIM | MARANHÃO | Brasil | 2112902 | 21 | 33 | nan | nan | nan | Amazônia | 8.7 |
| 33ff6c59-a02c-3532-89e0-75b5a56e67ca | -2.10279 | -46.58265 | 2026-10-08 16:39:00 | NOAA-20 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 409d5366-7bc2-3f2d-8958-8d1a77b03405 | -6.15272 | -47.94712 | 2026-10-08 16:39:00 | NOAA-20 | CACHOEIRINHA | TOCANTINS | Brasil | 1703826 | 17 | 33 | nan | nan | nan | Cerrado | 86.5 |
| 65bfa95f-9405-3191-94f4-b9e871572cab | -3.37169 | -41.36186 | 2026-10-08 16:39:00 | NOAA-20 | GRANJA | CEARÁ | Brasil | 2304707 | 23 | 33 | nan | nan | nan | Caatinga | 39.1 |
| eef55ef1-70c5-39fd-a3e8-52e630abecd9 | -1.37898 | -48.04609 | 2026-10-08 16:39:00 | NOAA-20 | SANTA IZABEL DO PARÁ | PARÁ | Brasil | 1506500 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 2af70380-6d79-36c7-ad5f-6072a168172f | -4.66954 | -56.21494 | 2026-10-08 16:39:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 26.2 |
| 109b0fe2-4370-336c-af1d-3f9e7d95fcad | -3.16453 | -50.44937 | 2026-10-08 16:39:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 13.6 |
| e28d5db5-ed75-3f35-8397-3955ba214051 | -5.55572 | -45.61345 | 2026-10-08 16:39:00 | NOAA-20 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 8.8 |
| 24e05d34-a64d-3397-9975-131482288c5c | -6.74396 | -55.11188 | 2026-10-08 16:39:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 64863886-0261-3201-a1ca-2f1c4c9fd001 | -3.74244 | -44.7024 | 2026-10-08 16:39:00 | NOAA-20 | ARARI | MARANHÃO | Brasil | 2101004 | 21 | 33 | nan | nan | nan | Amazônia | 5.1 |
| b6dd8c0e-130a-33dd-83f9-7ad2d9bd0223 | -6.32213 | -54.80442 | 2026-10-08 16:39:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 06291f83-95b9-33a8-9a2d-d48c19544c30 | -5.96142 | -46.38143 | 2026-10-08 16:39:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 18.3 |
| 32f0456e-1c0d-38eb-8024-201a74be88cd | 0.53025 | -50.80675 | 2026-10-08 16:39:00 | NOAA-20 | ITAUBAL | AMAPÁ | Brasil | 1600253 | 16 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 2fb9b90d-1fbb-3ba9-97c6-de7529cfa058 | -5.09621 | -46.203 | 2026-10-08 16:39:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 27.4 |
| 26457c5c-10da-3508-99c8-21bc08fdbecf | -1.4173 | -55.34432 | 2026-10-08 16:39:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 19.8 |
| 77080ec8-d17e-3c61-ac29-e485160a3aa0 | -6.1419 | -47.94501 | 2026-10-08 16:39:00 | NOAA-20 | CACHOEIRINHA | TOCANTINS | Brasil | 1703826 | 17 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 4a7387f7-f6e4-361f-8a28-fb42ba3e8960 | -5.69414 | -53.47958 | 2026-10-08 16:39:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 75.6 |
| 0070d416-25cc-3ad7-987b-444d042d4c40 | -6.72969 | -55.12801 | 2026-10-08 16:39:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 12.2 |
| 14578aec-8771-3f26-9069-df8d2ceb80a0 | -1.76107 | -55.28113 | 2026-10-08 16:39:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| e12d6906-c664-3a42-b13d-5548b1d98777 | -3.77872 | -41.6132 | 2026-10-08 16:39:00 | NOAA-20 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 9.6 |
| fac0468b-d0c9-37cd-a59a-c569eb1f566d | -5.98934 | -44.30074 | 2026-10-08 16:39:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| c2484e10-4117-3ddc-bdf1-aa2dd27bd317 | -3.25711 | -54.03861 | 2026-10-08 16:39:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 32.8 |
| f89f5829-de5b-3d2b-bfba-23f5eed5d274 | -1.75703 | -55.12046 | 2026-10-08 16:39:00 | NOAA-20 | CURUÁ | PARÁ | Brasil | 1502855 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| b5c5ba58-cd5e-3b1d-b5c3-ce763faae180 | -7.19029 | -55.12975 | 2026-10-08 16:39:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 14.0 |
| e0bb6517-653e-3d1c-a4cd-0ef712da1619 | -5.37538 | -44.20833 | 2026-10-08 16:39:00 | NOAA-20 | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | 116.3 |
| 7de17323-5893-333e-92e9-dd33443c8ca5 | -3.00438 | -54.07992 | 2026-10-08 16:39:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 38.2 |
| 0108468b-c44d-3e23-9f0d-df526b6ba303 | -6.27299 | -52.84973 | 2026-10-08 16:39:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 10.3 |
| 565df350-aa17-3996-93f6-ef01aa7a77c8 | -1.33342 | -52.45049 | 2026-10-08 16:39:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 14.0 |
| 789c0698-cd8e-3e5d-b2c4-7c53b0b85da2 | -5.17393 | -46.26881 | 2026-10-08 16:39:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 9df67dea-6818-39ae-9eb8-8117caf24a04 | -3.16929 | -54.7373 | 2026-10-08 16:39:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 13.9 |
| ad25341c-fa61-30bd-ba4e-998c7335fb0b | -3.92044 | -57.51859 | 2026-10-08 16:39:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 05fda983-4f33-39bf-8b8e-dcc874eb0f66 | -5.30844 | -45.72787 | 2026-10-08 16:39:00 | NOAA-20 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 117.4 |
| 04a1d3f6-f9cb-361a-b101-bb6f71a5fb00 | -3.79981 | -50.61047 | 2026-10-08 16:39:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 13.7 |
| f5ae1e02-4c8e-3962-b021-b5faa1b4d844 | -5.34771 | -45.96238 | 2026-10-08 16:39:00 | NOAA-20 | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| adc39a63-2bdb-303e-b9c5-c310d0357244 | -3.71219 | -59.64582 | 2026-10-08 16:39:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 13.5 |
| 4310ff3c-6a86-32d3-ad86-ed28804b638d | -6.7477 | -55.13945 | 2026-10-08 16:39:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 44.7 |
| 4a53efbc-8c02-30de-be27-b953b070f071 | -0.7268 | -49.45049 | 2026-10-08 16:39:00 | NOAA-20 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 8.4 |
| b7a04182-4572-364b-9875-255ab79bf07b | -6.12824 | -53.50777 | 2026-10-08 16:39:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 38.6 |
| 4debf723-604f-346a-b28c-25512b16736f | -4.49579 | -42.54287 | 2026-10-08 16:39:00 | NOAA-20 | LAGOA ALEGRE | PIAUÍ | Brasil | 2205557 | 22 | 33 | nan | nan | nan | Caatinga | 12.3 |
| 3343740e-ae6b-3bf5-bdc4-5b91752b3f31 | -1.82716 | -55.04091 | 2026-10-08 16:39:00 | NOAA-20 | CURUÁ | PARÁ | Brasil | 1502855 | 15 | 33 | nan | nan | nan | Amazônia | 11.2 |
| fad079d8-adeb-38f1-9970-00df335e1ed9 | -2.78963 | -57.63824 | 2026-10-08 16:39:00 | NOAA-20 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 2c06e359-8a00-3262-8656-8322258db8d5 | -3.89996 | -44.13153 | 2026-10-08 16:39:00 | NOAA-20 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 36.0 |
| f1f37fc7-2686-36f2-92cd-9deffe4c763b | -2.54622 | -48.17618 | 2026-10-08 16:39:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| ab9713a1-0128-3a8c-b739-0a355910ee4a | -6.2496 | -52.67887 | 2026-10-08 16:39:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 10.6 |
| 4491779d-8d5f-3014-b7df-bf6aa01db99d | -4.37498 | -41.8265 | 2026-10-08 16:39:00 | NOAA-20 | PIRIPIRI | PIAUÍ | Brasil | 2208403 | 22 | 33 | nan | nan | nan | Caatinga | 5.1 |
| 769199b4-40aa-34ff-9b29-34df6e600a2d | -6.44414 | -52.67297 | 2026-10-08 16:39:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 1914114c-bf13-3f7c-9ace-d5b771a6ffb2 | -6.85702 | -55.77974 | 2026-10-08 16:39:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 11.8 |
| 2813d373-c364-3af3-a887-45a0f4a91d93 | -3.30619 | -53.8661 | 2026-10-08 16:39:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 8.9 |
| c844e941-09f3-3878-af59-95d4f3e60d86 | -5.72782 | -45.23278 | 2026-10-08 16:39:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 01cb6852-3022-3cfd-b801-ad86060f650f | -2.09181 | -46.57726 | 2026-10-08 16:39:00 | NOAA-20 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 15.6 |
| 2b3de2f0-61ac-3ed3-a72b-b655aa4b9e5a | -3.01485 | -54.06029 | 2026-10-08 16:39:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 29.0 |
| 0f61efa0-ee8a-36e0-888e-2b825c71c696 | -6.18137 | -52.83441 | 2026-10-08 16:39:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 7c6d3be1-0711-3829-8bf2-3fa8fe24e06c | -1.26341 | -54.68113 | 2026-10-08 16:39:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 10.5 |
| bbc733f9-7dd1-3689-ba1b-75c8a51e5153 | -6.32036 | -54.79184 | 2026-10-08 16:39:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |


[Clique aqui para ver as próximas entradas](README370.md)
