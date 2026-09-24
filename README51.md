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

## Dados Diários - Página 51

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 5941083a-62ff-3085-8ed8-4401706c287b | -15.24263 | -43.26464 | 2026-09-24 04:46:00 | NPP-375D | PAI PEDRO | MINAS GERAIS | Brasil | 3146552 | 31 | 33 | nan | nan | nan | Caatinga | 1.9 |
| cbea66e2-6f28-3476-a54a-f9c5ff5cc616 | -14.62206 | -50.60633 | 2026-09-24 04:46:00 | NPP-375D | NOVA CRIXÁS | GOIÁS | Brasil | 5214838 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| ca91d338-90bb-3b1f-bb48-900c2e81ef0b | -10.33537 | -48.25678 | 2026-09-24 04:46:00 | NPP-375D | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| cf70ab79-e693-3c90-b51e-0d60fa6bbf27 | -11.43433 | -44.20341 | 2026-09-24 04:46:00 | NPP-375D | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 15b6b4de-c640-30f5-9120-788a7bb3bf6b | -10.08419 | -46.04874 | 2026-09-24 04:46:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| d7d8ed18-bd52-3d38-86cd-e4199d085f21 | -7.55558 | -55.01248 | 2026-09-24 04:46:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| df6b0f3e-ba43-344f-97c8-c2d5b7110a68 | -7.88723 | -61.17778 | 2026-09-24 04:46:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 010e728e-f122-34db-9dfb-b71c2182710f | -11.94376 | -38.29191 | 2026-09-24 04:46:00 | NPP-375D | INHAMBUPE | BAHIA | Brasil | 2913705 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 3d1db89b-4436-3df7-a64d-12094b615624 | -12.7611 | -52.82811 | 2026-09-24 04:46:00 | NPP-375D | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 74972eee-6a53-379c-8b51-696b91a9e3a6 | -13.07284 | -47.39942 | 2026-09-24 04:46:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 50d86085-3245-3176-8ae2-6576ba28695c | -10.55956 | -44.61176 | 2026-09-24 04:46:00 | NPP-375D | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| a0390e21-a19a-36f3-8ed7-6985dca12106 | -10.27988 | -49.95944 | 2026-09-24 04:46:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 99dae28f-43e5-365d-a1a7-3cc0acdf338c | -10.27709 | -49.95527 | 2026-09-24 04:46:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| ecbdef40-665a-33a0-b5b4-3a5f27c22ede | -8.45918 | -51.49548 | 2026-09-24 04:46:00 | NPP-375D | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a08a6601-b1ba-3f18-a095-aa24a1037af2 | -7.51499 | -61.49031 | 2026-09-24 04:46:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b9b854da-05ca-3d94-886f-fa5a4ca33448 | -8.23762 | -48.21651 | 2026-09-24 04:46:00 | NPP-375D | TUPIRATINS | TOCANTINS | Brasil | 1721307 | 17 | 33 | nan | nan | nan | Cerrado | 6.7 |
| d54314cf-fdd7-3c69-bd0e-c126bda744a8 | -6.88848 | -59.22225 | 2026-09-24 04:46:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 12f33adf-214e-373f-aecf-e6ec6e3acf29 | -6.66318 | -58.57164 | 2026-09-24 04:46:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 3.3 |
| c8bb73a1-7110-34c3-ba69-b4f4cf42c2c6 | -11.99736 | -52.46174 | 2026-09-24 04:46:00 | NPP-375D | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 69be5d5b-88d9-3a76-bd4c-17e10928f231 | -8.29653 | -50.85107 | 2026-09-24 04:46:00 | NPP-375D | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| a781c4ba-a593-3ca8-88c4-6aa97cbb3a33 | -6.45003 | -59.95604 | 2026-09-24 04:46:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 50d5d36e-2e93-3c50-96e2-7903ec42c5a7 | -6.8987 | -55.5731 | 2026-09-24 04:46:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 7de7a37f-13c3-3296-9b66-14111c5b4b84 | -11.12635 | -48.30336 | 2026-09-24 04:46:00 | NPP-375D | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 793dc746-f67d-3219-92cc-53f5db921b7c | -12.13197 | -50.75006 | 2026-09-24 04:46:00 | NPP-375D | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 6.3 |
| b90b2cd5-3ae8-3d64-b0f3-d8e9d56d7c17 | -11.48966 | -47.33671 | 2026-09-24 04:46:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| de61c3b5-2562-306a-b240-937c5633b0bc | -11.63308 | -50.61768 | 2026-09-24 04:46:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 17bf4921-fcc6-3dfe-bac4-07283740ac0a | -6.07193 | -57.8026 | 2026-09-24 04:46:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 7cee909a-18c9-3ada-9237-39dd22a51b1e | -6.63531 | -59.92695 | 2026-09-24 04:46:00 | NPP-375D | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 82439428-dc5f-34ee-97db-6f693d2b00a2 | -11.49488 | -54.47721 | 2026-09-24 04:46:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| dc21f064-173a-323f-83cc-afe9e7f40df7 | -12.01451 | -50.31552 | 2026-09-24 04:46:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| a6a5f5d5-1382-30fb-b3ed-6d3b3c78532b | -11.47998 | -47.33141 | 2026-09-24 04:46:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| bcecd15a-b7cd-328e-b314-d7f940f7596c | -8.30971 | -50.38052 | 2026-09-24 04:46:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f7399c33-93a0-3888-a9d8-422f924544ef | -10.27431 | -49.9511 | 2026-09-24 04:46:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 3f26a231-57f4-3bc4-884b-508699dead4b | -8.27767 | -54.77364 | 2026-09-24 04:46:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| da1fc369-995b-31a9-b58e-dd0ff47e2392 | -6.62779 | -59.93433 | 2026-09-24 04:46:00 | NPP-375D | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 25bf2f09-b4cf-3f96-bbd0-305b3505a4ff | -11.21065 | -54.12415 | 2026-09-24 04:46:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| bffb5bc4-76fd-3160-b70a-8fa3934dff49 | -11.12858 | -48.32529 | 2026-09-24 04:46:00 | NPP-375D | IPUEIRAS | TOCANTINS | Brasil | 1709807 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 99aba40e-2dcd-3ae5-b5fe-ed08e6a4a75e | -7.78499 | -50.2232 | 2026-09-24 04:46:00 | NPP-375D | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 0c4d0b46-2beb-3f3c-b490-3091a0f4b620 | -9.85724 | -48.50085 | 2026-09-24 04:46:00 | NPP-375D | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 5813f334-e650-35d4-82ee-a3faf775a698 | -8.14965 | -49.54739 | 2026-09-24 04:46:00 | NPP-375D | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 63a7acb1-4b3d-3c64-b243-922b70bb213e | -11.12522 | -48.3323 | 2026-09-24 04:46:00 | NPP-375D | IPUEIRAS | TOCANTINS | Brasil | 1709807 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 3afb4136-a67c-39f5-9ff8-2076d5b22f22 | -12.14662 | -50.74424 | 2026-09-24 04:46:00 | NPP-375D | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 0.3 |
| af97d54e-e31a-3d0a-a43f-0b6a9ebbbe2d | -10.07968 | -46.01259 | 2026-09-24 04:46:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 23.1 |
| 0545b7ba-1e95-3772-ae62-c7c9868c708d | -7.99756 | -44.94585 | 2026-09-24 04:46:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 887a300e-e458-3ca4-a616-3afdcbe99da5 | -11.93232 | -48.22231 | 2026-09-24 04:46:00 | NPP-375D | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 31fe2353-92c1-30e1-83f7-76e0e7f0a4b3 | -12.76478 | -52.82879 | 2026-09-24 04:46:00 | NPP-375D | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 0c713783-97e2-39dd-8e51-8fa307342f9a | -8.30554 | -56.36464 | 2026-09-24 04:46:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 7.7 |
| db916a1a-2c03-3db3-b270-2b3321900838 | -10.72204 | -48.74438 | 2026-09-24 04:46:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 583a5105-8dd8-315d-ac1a-99b4421ee8a1 | -10.45709 | -44.94608 | 2026-09-24 04:46:00 | NPP-375D | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 61d46993-1e9f-3c21-872d-0a6b3905927a | -6.24152 | -60.03803 | 2026-09-24 04:46:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 2da2d60f-22ca-3476-96be-db457cdf535b | -10.25493 | -49.98502 | 2026-09-24 04:46:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 78bfb761-b72a-3aed-9945-e7c2aa704e63 | -10.14932 | -50.24507 | 2026-09-24 04:46:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 1e78ad65-cfe5-330c-98bc-616f8d4baeb2 | -10.09714 | -46.05897 | 2026-09-24 04:46:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 6d28d3c7-be55-3dcd-a94e-add6feb43ad0 | -6.6778 | -58.57269 | 2026-09-24 04:46:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| f67d12af-b47a-3fae-95c7-ef5d87a42959 | -9.86335 | -48.50543 | 2026-09-24 04:46:00 | NPP-375D | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 803a36e9-79c6-371f-b958-3143c6575f63 | -6.61416 | -59.93398 | 2026-09-24 04:46:00 | NPP-375D | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 294bf75b-c438-3685-8516-e84445549f99 | -12.12418 | -50.73349 | 2026-09-24 04:46:00 | NPP-375D | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 65a18133-e858-3721-8746-5488f1210393 | -10.08359 | -46.05274 | 2026-09-24 04:46:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| be7e11b2-2ddb-3fa9-a0f4-143135eba523 | -12.13741 | -50.71671 | 2026-09-24 04:46:00 | NPP-375D | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 8f314293-c276-37c6-899f-651c4cf0698a | -10.71594 | -48.73978 | 2026-09-24 04:46:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 3e144e5a-7479-3743-b305-346f0e98ddf7 | -6.67269 | -58.56725 | 2026-09-24 04:46:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 59c9d589-920d-3f94-83e6-1f5f36884611 | -9.84338 | -48.48065 | 2026-09-24 04:46:00 | NPP-375D | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 2e1e7e6f-304b-32d0-8a8f-cbe1d5fd8a0b | -9.84671 | -48.48118 | 2026-09-24 04:46:00 | NPP-375D | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c880ebc8-e281-3bfe-9d21-5a7096c6a9ca | -9.17957 | -46.50989 | 2026-09-24 04:46:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 7683ec86-9314-3156-abf0-f671eac9c491 | -7.41675 | -49.86452 | 2026-09-24 04:46:00 | NPP-375D | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3fa8eb01-72cb-32c9-aa8c-62b185a20b1d | -8.74455 | -44.26556 | 2026-09-24 04:46:00 | NPP-375D | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 9d1cc850-a7dd-3c4a-a325-1259c23ed030 | -12.86878 | -43.82602 | 2026-09-24 04:46:00 | NPP-375D | SERRA DOURADA | BAHIA | Brasil | 2930303 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 1b4534bc-007d-31b9-810b-a4f2b0cf66d2 | -12.1494 | -50.74852 | 2026-09-24 04:46:00 | NPP-375D | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 8.4 |
| 0ccaad19-369b-37fc-beda-660ed7afea6d | -12.7902 | -46.50323 | 2026-09-24 04:46:00 | NPP-375D | LAVANDEIRA | TOCANTINS | Brasil | 1712157 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| da8e63be-3cec-346d-83a2-8826b7b3b8a5 | -8.20475 | -54.7314 | 2026-09-24 04:46:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 997f538e-238b-30d8-89dd-59231bde1529 | -11.9068 | -48.45247 | 2026-09-24 04:46:00 | NPP-375D | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d6ae9ad2-88ec-375b-8c3d-824e00e17bbb | -10.26859 | -49.96499 | 2026-09-24 04:46:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| daaf911c-24e0-356e-998b-1bb92b784bbf | -10.24143 | -49.98278 | 2026-09-24 04:46:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f1141b0a-7c7e-32c9-847f-23b115142ab8 | -9.86002 | -48.50489 | 2026-09-24 04:46:00 | NPP-375D | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 18.2 |
| 1c9d65ca-7ec7-3039-8175-d4daa788b0c8 | -8.29262 | -49.91365 | 2026-09-24 04:46:00 | NPP-375D | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 6c57afb2-f61d-38dc-b984-b137a3a37747 | -8.72297 | -47.61075 | 2026-09-24 04:46:00 | NPP-375D | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 0b5242ee-20b2-3d1f-8ac5-6bead5efc7cd | -6.68427 | -55.05748 | 2026-09-24 04:46:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 8285bb02-f34f-37c4-93ae-064644fd921d | -14.62541 | -50.6069 | 2026-09-24 04:46:00 | NPP-375D | NOVA CRIXÁS | GOIÁS | Brasil | 5214838 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 6ec32b4c-b3d9-35d2-942e-c12e1e0f5646 | -12.59484 | -47.85859 | 2026-09-24 04:46:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| dd2d73cd-aaf0-3d87-8869-a819b6377db8 | -9.59536 | -47.77328 | 2026-09-24 04:46:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 3e8cab7b-60cb-35f3-90de-ebd695ce4072 | -12.35145 | -48.19641 | 2026-09-24 04:46:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 0282d802-e669-3023-b6e7-10782be9985e | -10.43385 | -46.26226 | 2026-09-24 04:46:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| f10ff4dd-fc05-34c0-b956-7695f34db2e6 | -8.08679 | -54.76225 | 2026-09-24 04:46:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 5334affb-5f6e-3384-bc42-f1143981feaa | -13.93753 | -47.8281 | 2026-09-24 04:46:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 354b6044-d685-3115-a02f-73550c9618f1 | -10.41731 | -49.36255 | 2026-09-24 04:46:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 6.0 |
| b3d9a35f-e2ea-31d3-a05c-e428bf697a7a | -10.46042 | -44.94869 | 2026-09-24 04:46:00 | NPP-375D | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 9.2 |
| 93c3d2a6-f498-3821-9797-e13ce0642786 | -10.28047 | -49.95583 | 2026-09-24 04:46:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| a2611431-cea7-3c3c-a5fa-721d80ede7a8 | -7.41331 | -49.86413 | 2026-09-24 04:46:00 | NPP-375D | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6999f406-bf06-30ac-a91c-b7a7c11cf585 | -11.70823 | -44.49772 | 2026-09-24 04:46:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| bc26b224-0ab6-3ba6-ad81-8e93e63d4a0a | -6.65072 | -55.05704 | 2026-09-24 04:46:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 91b4e5a4-fbac-30ca-801e-691ba1688cdd | -8.26282 | -54.77986 | 2026-09-24 04:46:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| b6e9cb6f-cf5b-3eb2-a57f-9d176c373efe | -10.8341 | -48.48079 | 2026-09-24 04:46:00 | NPP-375D | BREJINHO DE NAZARÉ | TOCANTINS | Brasil | 1703701 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 813c0539-5b57-3961-a6fd-d089c89105cc | -12.16744 | -47.37088 | 2026-09-24 04:46:00 | NPP-375D | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 8da11da3-0da0-3794-b7b3-7f252d28f8e0 | -9.1518 | -49.95872 | 2026-09-24 04:46:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 7bf3fe48-2db7-3a47-a7b4-57ca3bea6958 | -11.36325 | -43.37932 | 2026-09-24 04:46:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| be3ad45e-28ff-33d2-bebd-70407afd4911 | -9.53169 | -46.48954 | 2026-09-24 04:46:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 4caebad5-d07e-3544-af6a-b3135cb9488d | -11.99522 | -44.94205 | 2026-09-24 04:46:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 74c58c9a-f693-32d5-ac6b-66b55bd00dff | -8.31049 | -56.36557 | 2026-09-24 04:46:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 46e5d9cc-d9d6-3ff1-954e-80939b090b82 | -10.41176 | -49.35439 | 2026-09-24 04:46:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 15.6 |
| 207ef669-6de6-3c58-80cd-0b4075529660 | -9.53034 | -45.36713 | 2026-09-24 04:46:00 | NPP-375D | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |


[Clique aqui para ver as próximas entradas](README52.md)
