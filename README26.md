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
| a1c27dfb-fefe-3273-9503-40f7c6b638dd | -9.9377 | -48.51724 | 2026-09-12 04:34:00 | NOAA-21 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 624fffef-ba65-3d7f-89cf-e37a0977ec4d | -7.60119 | -46.76247 | 2026-09-12 04:34:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 0ebaeaf1-2402-36be-b6d0-a5b3596f5acc | -8.95931 | -48.90349 | 2026-09-12 04:34:00 | NOAA-21 | GOIANORTE | TOCANTINS | Brasil | 1708304 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| ea5c9faa-9ccc-3819-a551-33b266c5cdec | -9.54084 | -45.45138 | 2026-09-12 04:34:00 | NOAA-21 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| eeafab48-c184-3dfd-8540-b9818ba63405 | -6.87691 | -55.62811 | 2026-09-12 04:34:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e7bc6435-096a-3adb-a55a-242506e7b159 | -9.79259 | -47.11249 | 2026-09-12 04:34:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 548575f9-dc1d-3c9b-8354-4822a36d25f3 | -13.16533 | -43.3831 | 2026-09-12 04:34:00 | NOAA-21 | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 449130fc-8bd0-3899-9169-23ea4f7c8294 | -9.18354 | -59.45445 | 2026-09-12 04:34:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| dab9adea-6d41-3640-91eb-7777ac7bb2c6 | -5.77722 | -47.17126 | 2026-09-12 04:34:00 | NOAA-21 | MONTES ALTOS | MARANHÃO | Brasil | 2107001 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| add6b2c0-88e8-3925-bbd4-cf3929af6bb1 | -8.11438 | -54.79892 | 2026-09-12 04:34:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| be0bb72f-8020-30bd-a37c-a3c2c6722e07 | -10.31715 | -49.95493 | 2026-09-12 04:34:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 557526f2-0297-3ddd-958c-60873db9cd98 | -5.81021 | -47.22257 | 2026-09-12 04:34:00 | NOAA-21 | MONTES ALTOS | MARANHÃO | Brasil | 2107001 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 68ca517b-c98a-3d2f-adcc-41f925b59fd3 | -10.90291 | -47.83344 | 2026-09-12 04:34:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| cc45f6d5-125d-31e8-976d-e5c19cfac8bc | -11.18931 | -42.78902 | 2026-09-12 04:34:00 | NOAA-21 | GENTIO DO OURO | BAHIA | Brasil | 2911303 | 29 | 33 | nan | nan | nan | Caatinga | 5.5 |
| d9c80f07-7889-3042-a542-2fb96956dc57 | -6.60696 | -58.84991 | 2026-09-12 04:34:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 6.4 |
| b464759e-e151-3434-b947-498143c297e0 | -10.67722 | -49.07573 | 2026-09-12 04:34:00 | NOAA-21 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 1fac93d1-c05a-3aaf-8810-17899ea8c8b8 | -10.55741 | -51.33727 | 2026-09-12 04:34:00 | NOAA-21 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 47b6420d-6a20-3279-a7f8-51280915fb0c | -8.26052 | -51.19918 | 2026-09-12 04:34:00 | NOAA-21 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 080c1ba3-ef93-325c-8c5b-8fb48c664dff | -8.06944 | -54.84914 | 2026-09-12 04:34:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| d7c3a576-2ba9-3426-8ed9-894fe14c9e6a | -6.23962 | -51.68781 | 2026-09-12 04:34:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 64c67cdf-1310-37bc-a3e4-a3ae8400d7c9 | -6.88762 | -55.65099 | 2026-09-12 04:34:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 18f80ab2-4642-36db-b123-e19b7183da0d | -8.07155 | -54.86307 | 2026-09-12 04:34:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b94ed666-d1c2-369c-88ea-d3336ea0ca09 | -9.28758 | -50.3064 | 2026-09-12 04:34:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 40032a54-a8ee-37b0-9508-112742cced2f | -10.63479 | -46.12266 | 2026-09-12 04:34:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 4c5f05f6-aabe-32ab-a288-56c81ec5edc4 | -4.52826 | -54.96046 | 2026-09-12 04:34:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| d3f86a3d-1271-37c5-af2c-03f08d174264 | -6.313 | -55.15315 | 2026-09-12 04:34:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 22303a26-de3a-314c-83f0-5682c03cc2d4 | -6.23447 | -51.69606 | 2026-09-12 04:34:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 30368688-452f-3d47-bc53-87c1ca7c21b1 | -6.61365 | -58.84656 | 2026-09-12 04:34:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 3.6 |
| fc2e4a20-ba45-3f5d-885b-fd28a1223206 | -6.61735 | -44.20147 | 2026-09-12 04:34:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| e8e74ddb-48b4-3b3b-946f-c97ef6be936a | -8.36298 | -49.72358 | 2026-09-12 04:34:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 405e14e7-4272-36ad-94f8-c8a776322fbd | -10.95499 | -48.33688 | 2026-09-12 04:34:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 39cd6f4b-635a-3b43-8ccb-5d6d0fafb458 | -10.72721 | -50.61901 | 2026-09-12 04:34:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d4f79143-7e5a-3f9b-b3bd-dd69d030b050 | -7.46 | -42.11517 | 2026-09-12 04:34:00 | NOAA-21 | SANTO INÁCIO DO PIAUÍ | PIAUÍ | Brasil | 2209500 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 581a15f9-a266-391e-a2ce-594819b1d1a7 | -5.79109 | -53.82434 | 2026-09-12 04:34:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| c8b4d5dc-43ec-3000-b4cc-6d6a48f512f6 | -5.79801 | -53.80905 | 2026-09-12 04:34:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 05bd102f-a13c-3c36-a037-828cea6315a2 | -10.48732 | -51.36239 | 2026-09-12 04:34:00 | NOAA-21 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 17ac329d-4b05-3463-ac0a-d884c3b12c3d | -6.23817 | -51.69668 | 2026-09-12 04:34:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| fe8e1539-eaa1-3f0b-8652-f190b22ebf20 | -6.26541 | -50.83675 | 2026-09-12 04:34:00 | NOAA-21 | PARAUAPEBAS | PARÁ | Brasil | 1505536 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 828bf88c-d93e-359c-bce2-03b0a4a4d81e | -7.05507 | -42.72069 | 2026-09-12 04:34:00 | NOAA-21 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| e8f0860d-83c0-3a30-9933-87c1a2adf668 | -9.18837 | -46.5379 | 2026-09-12 04:34:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 62e42292-6d74-36d4-b2ae-aad123fa4679 | -6.1917 | -57.72307 | 2026-09-12 04:34:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 77716e3d-a9b1-343b-8cde-5152d77a9aa9 | -10.55659 | -45.20741 | 2026-09-12 04:34:00 | NOAA-21 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 478799e7-9286-3a86-8158-302384dbeeb7 | -6.84455 | -55.58257 | 2026-09-12 04:34:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 89adf074-3954-3bbe-9e6a-88f4e97a279b | -8.58838 | -54.56971 | 2026-09-12 04:34:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6ac6fea2-c4ee-3ea9-be6f-87cd368b86bb | -10.47646 | -48.63896 | 2026-09-12 04:34:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 170ff84e-8ca7-361e-ae69-00bb1838f364 | -10.56182 | -51.35394 | 2026-09-12 04:34:00 | NOAA-21 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 9b0ea799-2332-3410-815b-f5258048a089 | -6.24487 | -51.70234 | 2026-09-12 04:34:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| bda39c79-db11-3101-a8d7-81acf84cb461 | -9.5372 | -45.45089 | 2026-09-12 04:34:00 | NOAA-21 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| e4302ecd-b293-3de6-bcd7-e38561f8c71b | -7.26261 | -45.34712 | 2026-09-12 04:34:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 25a98e87-4604-3499-98eb-8874a425f776 | -6.24333 | -51.68843 | 2026-09-12 04:34:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 3b92046b-1247-3821-ab4b-caa3231d3584 | -6.84549 | -55.8095 | 2026-09-12 04:34:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| f735613c-d70a-30b5-8a4c-abb9ea2ae99f | -10.46875 | -48.64492 | 2026-09-12 04:34:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b9afd29c-0ade-324b-9323-bbd964f28b34 | -10.34284 | -48.09622 | 2026-09-12 04:34:00 | NOAA-21 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 4ab25325-3938-302b-9862-92b980c2629f | -8.11512 | -54.79465 | 2026-09-12 04:34:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 92939612-8c76-3cda-9de1-be503d6498c0 | -9.31923 | -45.64567 | 2026-09-12 04:34:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| ebbb6bf3-b33d-3775-82da-565f32be53fe | -7.56935 | -46.14495 | 2026-09-12 04:34:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| c8f1ad46-4768-37f2-9c6c-ced598c61faa | -6.84929 | -55.58337 | 2026-09-12 04:34:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f1149fff-8f9d-37b7-b37c-14bef3cfe686 | -9.15542 | -49.9876 | 2026-09-12 04:34:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3ada38af-9441-35dc-9c76-67e695a892bb | -10.89513 | -47.83947 | 2026-09-12 04:34:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 5cae63b4-fe88-3325-a609-381fa0457422 | -10.23726 | -56.25876 | 2026-09-12 04:34:00 | NOAA-21 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 537c8ca1-f6b1-3e01-bd1b-fd512fdad086 | -6.50666 | -47.59798 | 2026-09-12 04:34:00 | NOAA-21 | PALMEIRAS DO TOCANTINS | TOCANTINS | Brasil | 1713809 | 17 | 33 | nan | nan | nan | Cerrado | 6.0 |
| d7db6d1a-f93b-366a-8fa1-d493f7227a70 | -11.53789 | -44.89241 | 2026-09-12 04:34:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 8914d243-2c90-39ef-974a-e0ba343c5641 | -10.33768 | -48.0191 | 2026-09-12 04:34:00 | NOAA-21 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 871f8967-5306-3ed0-b994-d95e96ef3216 | -7.42396 | -46.15456 | 2026-09-12 04:34:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 7.6 |
| a514b737-3606-3016-8bcb-684b52540cde | -6.19043 | -57.73026 | 2026-09-12 04:34:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| f6f0f323-9ed5-3771-a09b-5c3494635d51 | -11.24417 | -54.14067 | 2026-09-12 04:34:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 53994ccc-0216-3d34-812a-8203032b943b | -6.42862 | -56.10499 | 2026-09-12 04:34:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 6e6047b6-b4c2-395f-94c1-578d28fd3683 | -8.956 | -48.90297 | 2026-09-12 04:34:00 | NOAA-21 | GOIANORTE | TOCANTINS | Brasil | 1708304 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 263fc5fc-1a75-370b-9732-eba892811db7 | -13.65784 | -43.92813 | 2026-09-12 04:34:00 | NOAA-21 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 4c0badb8-bf2d-38d5-8faf-e86d4260605e | -9.7026 | -43.39729 | 2026-09-12 04:34:00 | NOAA-21 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 2.5 |
| b276d6b0-0816-372f-bfa2-640238e88df0 | -12.03269 | -49.95099 | 2026-09-12 04:34:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| e8f72043-839f-3879-bfb0-0ff2757da0e2 | -11.24541 | -54.13357 | 2026-09-12 04:34:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 9918ed95-ce8c-30ca-994f-b34c4d3c270b | -4.86888 | -56.00696 | 2026-09-12 04:34:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| db5700c0-140a-3e32-a5ec-32b5934006ab | -6.72366 | -45.43867 | 2026-09-12 04:34:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 8f251f3a-3cf9-391e-b13e-f5f2f6e46b2e | -8.57978 | -54.56834 | 2026-09-12 04:34:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 1be37bdc-5ad0-3b07-a093-a91e00dada18 | -4.47262 | -55.43621 | 2026-09-12 04:34:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 768de7d5-4a4e-38c8-a1f5-70818ea895bb | -7.27581 | -46.80227 | 2026-09-12 04:34:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 6.6 |
| b3776d1e-5c96-3687-a916-da2ff82b2c55 | -4.86979 | -56.00159 | 2026-09-12 04:34:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b3a79779-91ee-3ec8-a7f1-7fc8449d2600 | -5.78882 | -53.81163 | 2026-09-12 04:34:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 5bd24db6-09c0-340d-b5c3-492a9bbdeb67 | -11.40888 | -47.74018 | 2026-09-12 04:34:00 | NOAA-21 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 2543c85b-2546-3d23-ba8e-f4e22511d8c6 | -11.38706 | -43.95002 | 2026-09-12 04:34:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 84149c52-5a61-3523-94a5-f5786cc4e372 | -8.08844 | -54.87045 | 2026-09-12 04:34:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b26003b8-2d28-3f30-b664-6bf8e2e567d4 | -4.53689 | -54.96679 | 2026-09-12 04:34:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ba57ae3b-ca02-336c-918a-3008fc489485 | -11.04069 | -49.68408 | 2026-09-12 04:34:00 | NOAA-21 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 2809110a-7601-3886-b2d7-c44a9974f2f7 | -7.59781 | -46.76194 | 2026-09-12 04:34:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| d926793e-f8eb-32b5-aa41-fe683a7372ee | -11.81311 | -46.36977 | 2026-09-12 04:34:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 76fc6ac1-1cda-304e-83c6-d6be21d5fb77 | -12.64096 | -51.42354 | 2026-09-12 04:34:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 85717149-b66b-34a2-8bed-b13e56f812e2 | -11.81724 | -46.36629 | 2026-09-12 04:34:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 0f1db8a4-1627-3ddb-b4aa-2bb6a8f90083 | -12.12618 | -48.98531 | 2026-09-12 04:34:00 | NOAA-21 | FIGUEIRÓPOLIS | TOCANTINS | Brasil | 1707652 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| d286ff37-3ee0-366f-96dc-d9dd35cdb0e4 | -10.55579 | -51.36911 | 2026-09-12 04:34:00 | NOAA-21 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e645c9a6-0e89-352d-818b-f6770fcadca3 | -4.53293 | -55.61575 | 2026-09-12 04:34:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 800eb45f-280d-3465-8bbb-9ac6d9cafb1d | -9.70671 | -43.39788 | 2026-09-12 04:34:00 | NOAA-21 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 5e8c3704-913a-3a2a-b8fd-deef0eb66857 | -11.96948 | -49.77055 | 2026-09-12 04:34:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| f7e16492-a8ef-3ad3-9e43-599ca3946a45 | -6.40469 | -54.97509 | 2026-09-12 04:34:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 824d4aac-ea3e-3bce-a612-5bf5e1c0fd0d | -6.06348 | -53.4911 | 2026-09-12 04:34:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| e12172e1-41bc-362c-ac25-717f961b7f51 | -4.87435 | -56.00524 | 2026-09-12 04:34:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 19a4afa4-0d78-38c7-b87a-0d1f62e55e9f | -7.42453 | -46.15078 | 2026-09-12 04:34:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 374bf795-f7b9-3237-bae6-b6d29c4e5a7d | -10.52994 | -46.34454 | 2026-09-12 04:34:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ea252526-8f3a-3473-beb4-f917ffd36a7c | -8.45851 | -47.53061 | 2026-09-12 04:34:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a880a408-6472-34e5-b164-e0895296fa57 | -6.19892 | -55.27085 | 2026-09-12 04:34:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |


[Clique aqui para ver as próximas entradas](README27.md)
