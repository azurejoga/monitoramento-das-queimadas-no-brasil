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

## Dados Diários - Página 141

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 26c072dc-911e-3219-80e2-2bf0b4ac3d29 | -10.50984 | -64.51894 | 2026-08-28 17:45:00 | NOAA-20 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 13.4 |
| f99d97de-b150-3514-957e-01e321c8268d | -11.36045 | -48.39105 | 2026-08-28 17:45:00 | NOAA-20 | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 13817973-4504-36c0-bb73-232982da00cb | -8.59171 | -54.79611 | 2026-08-28 17:45:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 79.1 |
| 4b698408-9c28-3645-8b3e-2e7866903c51 | -9.10608 | -60.31049 | 2026-08-28 17:45:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 20.8 |
| c0f4ab16-31ce-375d-8872-1c79c92c385d | -11.68027 | -54.53855 | 2026-08-28 17:45:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 881f5b80-3099-34af-bf7e-02e2d69fe283 | -12.39146 | -48.1928 | 2026-08-28 17:45:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 43.7 |
| f71ee0ac-cc19-355a-b993-7efecfe6e6cc | -14.87811 | -52.6172 | 2026-08-28 17:45:00 | NOAA-20 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 18.2 |
| 6f8f39e6-99a1-315b-b5f0-916f83c363a1 | -14.90571 | -56.32116 | 2026-08-28 17:45:00 | NOAA-20 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 3ab05c5a-1b44-30d2-b194-e3619fc8029c | -9.19341 | -61.08953 | 2026-08-28 17:45:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 8.3 |
| 690328b3-5f25-3864-b5c6-1ad211737c91 | -14.18541 | -52.85229 | 2026-08-28 17:45:00 | NOAA-20 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 25faf623-b972-37a7-b59f-0c82833a4e90 | -14.19264 | -52.83493 | 2026-08-28 17:45:00 | NOAA-20 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 8.6 |
| c5bdf3ef-11f4-3948-9780-770a0f6393e2 | -14.43676 | -52.60685 | 2026-08-28 17:45:00 | NOAA-20 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 11.8 |
| 05aa3ea2-49f6-3a24-8cee-468e8d11be1c | -14.9291 | -56.31306 | 2026-08-28 17:45:00 | NOAA-20 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 16.0 |
| 3022b8ef-d5d4-3743-bf0e-c9cc1d4fa1ab | -10.51225 | -59.63535 | 2026-08-28 17:45:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 170d0153-08a6-39e8-9b85-6466a4050bba | -9.4617 | -60.47664 | 2026-08-28 17:45:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 142.8 |
| 8d6def58-3d7a-3a7a-9e42-1db1085a005b | -9.9195 | -60.4301 | 2026-08-28 17:45:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 58.7 |
| 71d10915-e97f-3f3a-a7b8-63fb1e3efe67 | -8.56996 | -54.81718 | 2026-08-28 17:45:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 13.8 |
| 1cf22045-90ca-3a24-9be5-625e712413e5 | -14.86911 | -52.62532 | 2026-08-28 17:45:00 | NOAA-20 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 8.5 |
| 1be1bf57-6913-355a-922a-088fb3d6d09e | -8.95537 | -50.79483 | 2026-08-28 17:45:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 34.8 |
| 31086907-2548-34c4-8b20-ba52ad781e73 | -9.76544 | -64.97663 | 2026-08-28 17:45:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 14.3 |
| 7f75a500-a953-33e1-a23d-3fedfd35d538 | -9.17472 | -59.60667 | 2026-08-28 17:45:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 15.6 |
| 50deb3d3-a960-393e-a220-2b0777021ecd | -11.61267 | -50.1942 | 2026-08-28 17:45:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 11.8 |
| 2daf6ffe-53bd-33ae-8f7b-34f4e6513146 | -14.91309 | -56.3161 | 2026-08-28 17:45:00 | NOAA-20 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 17.5 |
| e2d70af7-d1f5-3277-8023-5c38278bc31d | -9.23091 | -51.52029 | 2026-08-28 17:45:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 21390fda-ddf6-3f17-b25b-2dddaf80f4d3 | -14.19497 | -52.84713 | 2026-08-28 17:45:00 | NOAA-20 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 7.6 |
| f2132d75-74ab-3a0f-877f-d5400bc3d92b | -8.11945 | -51.6646 | 2026-08-28 17:45:00 | NOAA-20 | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 8.1 |
| 9d3869de-3017-351e-9802-9f030a44e469 | -13.46564 | -57.04689 | 2026-08-28 17:45:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Cerrado | 7.4 |
| f6b3fdfd-d80c-3542-a908-22947d928aef | -8.79889 | -49.98505 | 2026-08-28 17:45:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 11.7 |
| 747ffc66-51dd-3023-81a3-b4caba2b948b | -9.85582 | -67.89941 | 2026-08-28 17:45:00 | NOAA-20 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 4.2 |
| ff9a16bb-abdf-3598-baa4-275ee238c2c5 | -9.9254 | -60.44478 | 2026-08-28 17:45:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 94.3 |
| df04e6a2-4768-3414-941d-97979c54ebd7 | -10.4057 | -61.19894 | 2026-08-28 17:45:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 23.1 |
| b43ee51c-436e-3d55-a456-60cdb5faf8a1 | -10.76218 | -53.97153 | 2026-08-28 17:45:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 7.8 |
| b2c1a0c1-aed6-3a50-84c4-910e4bc99c92 | -14.87535 | -52.63019 | 2026-08-28 17:45:00 | NOAA-20 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 7.9 |
| dc719f06-2b69-325e-bc84-3d426ef88e41 | -9.85697 | -65.00715 | 2026-08-28 17:45:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 7.8 |
| 69b3aabc-94c0-3fc0-88a1-10a739fc47f5 | -14.23871 | -51.77329 | 2026-08-28 17:45:00 | NOAA-20 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 41bb683f-0725-39f4-b038-79b7a79a3426 | -9.10732 | -60.31071 | 2026-08-28 17:45:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 31.0 |
| 863a851c-b585-37e7-8638-30260ca7b06b | -14.41079 | -52.5834 | 2026-08-28 17:45:00 | NOAA-20 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 18b8f377-aab9-32cf-b779-7b34f627411f | -8.58588 | -54.82096 | 2026-08-28 17:45:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 16.6 |
| 15816873-0a5a-372a-b8f2-a4cc30400a78 | -14.18694 | -52.83274 | 2026-08-28 17:45:00 | NOAA-20 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 72456358-0980-3641-acd0-8d1a2d7051fe | -8.78745 | -50.06659 | 2026-08-28 17:45:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 15.8 |
| 0f712e81-0692-3463-8995-1f6b665faf30 | -14.88322 | -52.61625 | 2026-08-28 17:45:00 | NOAA-20 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 13.2 |
| f7216a53-937d-385d-a0e5-5eaf788bdfa4 | -14.87986 | -52.62615 | 2026-08-28 17:45:00 | NOAA-20 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 11.3 |
| 153a2097-cf1d-365f-966d-2d5af7ba6674 | -11.21924 | -53.98794 | 2026-08-28 17:45:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 13.8 |
| 78cefbb1-c965-3a0c-b318-5069e0b8f96f | -10.81071 | -61.40456 | 2026-08-28 17:45:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 17.3 |
| 893d3564-e271-3bed-9eab-91678dbab3a9 | -14.63579 | -57.014 | 2026-08-28 17:45:00 | NOAA-20 | DENISE | MATO GROSSO | Brasil | 5103452 | 51 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 62f7bbfa-7ecc-382e-a015-e9597356297c | -10.75208 | -54.00091 | 2026-08-28 17:45:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 4.2 |
| d22bb821-a0fa-39d2-94c3-8a8396576eeb | -9.2443 | -57.07978 | 2026-08-28 17:45:00 | NOAA-20 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 10.5 |
| 27aea86a-11a8-3017-aea1-4effe5956df3 | -9.18667 | -59.63488 | 2026-08-28 17:45:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 13.1 |
| 75a6c6d8-d9c1-3c84-b171-f8338119a8a0 | -10.16391 | -69.01228 | 2026-08-28 17:45:00 | NOAA-20 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 1fe75170-3547-3d5c-832d-7ff5e2bc382c | -9.97572 | -53.93124 | 2026-08-28 17:45:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 32c0e7c8-8465-3593-b86d-883cda210544 | -10.47679 | -64.48529 | 2026-08-28 17:45:00 | NOAA-20 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 78.0 |
| a025194a-b818-3e06-8d6a-a7d2bf45df61 | -10.28312 | -68.86324 | 2026-08-28 17:45:00 | NOAA-20 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 11.9 |
| a51c4f23-f0ad-36e3-862c-1147fb57a894 | -14.90909 | -56.31686 | 2026-08-28 17:45:00 | NOAA-20 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 17.5 |
| db3ef7b2-2122-3da0-92b8-834b80521e3f | -9.69289 | -65.09914 | 2026-08-28 17:45:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 17.7 |
| ad17dbe7-c0d1-359d-9206-65439eaa6d5a | -14.19381 | -52.84107 | 2026-08-28 17:45:00 | NOAA-20 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 42991f5d-5e7c-335f-8422-bf8a6aea23ee | -10.91609 | -50.49421 | 2026-08-28 17:45:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 11e0594a-39db-3460-837c-66de70964bb3 | -8.25153 | -54.99447 | 2026-08-28 17:45:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 3612c17f-b178-3f77-829a-669dea985efe | -10.40962 | -61.20201 | 2026-08-28 17:45:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 23.1 |
| 84264437-0847-38cc-aef5-c03e06760c97 | -14.44988 | -53.36799 | 2026-08-28 17:45:00 | NOAA-20 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 4.8 |
| be383c45-6615-3d8b-957f-aa581618564b | -10.54145 | -69.90757 | 2026-08-28 17:45:00 | NOAA-20 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 15.0 |
| f84be52b-1d10-3c20-a899-70a0b909a26c | -14.18636 | -52.82969 | 2026-08-28 17:45:00 | NOAA-20 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 5.2 |
| c8c05339-e143-359d-9407-db4822887eb6 | -9.23436 | -59.77193 | 2026-08-28 17:45:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 14.2 |
| 4231e4e6-0c02-32ef-9d9b-706c5bc5a96c | -14.74179 | -58.7096 | 2026-08-28 17:45:00 | NOAA-20 | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 362f6778-b211-32ab-8f74-d9e24f90fbc5 | -11.60639 | -50.19545 | 2026-08-28 17:45:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 11.8 |
| 9f31e423-99ae-304d-9628-d3ce1fcee7ea | -14.40952 | -52.57693 | 2026-08-28 17:45:00 | NOAA-20 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 10.3 |
| bfc57253-13ec-30b9-9c2a-a31a73d67fd6 | -15.23929 | -53.85609 | 2026-08-28 17:45:00 | NOAA-20 | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 16.4 |
| cc3baf22-354d-39df-8171-b0b025d6716f | -13.55401 | -52.6124 | 2026-08-28 17:45:00 | NOAA-20 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 0977b074-922d-373c-a377-8bf36907d75c | -14.8822 | -52.63818 | 2026-08-28 17:45:00 | NOAA-20 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 28.9 |
| 39643011-4eab-3a64-8055-7cef9b347434 | -11.59968 | -65.13299 | 2026-08-28 17:45:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 5.2 |
| d48bb9d1-dc21-3f91-9edf-4e62c3d25923 | -8.54731 | -55.30344 | 2026-08-28 17:45:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 57c64023-3904-3387-895c-2015ff2e17ef | -10.39225 | -61.20106 | 2026-08-28 17:45:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 19.8 |
| 4a718ffb-b5df-33c4-bcf0-de76fe291c60 | -12.39216 | -48.18845 | 2026-08-28 17:45:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 13.8 |
| 3f80c6e0-5369-3f3f-bd1f-8952fa5f8432 | -8.59668 | -54.79545 | 2026-08-28 17:45:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 79.1 |
| fc97335c-f753-3ca5-8a0f-c70339a49d98 | -9.51357 | -56.92994 | 2026-08-28 17:45:00 | NOAA-20 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 7.7 |
| 26e69eb1-9c83-305f-80ef-7a16704b8c94 | -14.43495 | -52.59753 | 2026-08-28 17:45:00 | NOAA-20 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 5.8 |
| fa933c24-2e86-3334-b55b-e8b41cc46245 | -14.57892 | -52.1137 | 2026-08-28 17:45:00 | NOAA-20 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 14.4 |
| 5a0b42a9-add4-387c-b535-c2a8d3ebbc45 | -12.08755 | -64.24128 | 2026-08-28 17:45:00 | NOAA-20 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 8b8406ab-5f6e-3cff-977f-e8790168c756 | -10.50575 | -69.35057 | 2026-08-28 17:45:00 | NOAA-20 | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 5.6 |
| db48a360-4825-3c36-9b69-a658db949182 | -14.5796 | -52.11721 | 2026-08-28 17:45:00 | NOAA-20 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 14.4 |
| 06e4ef19-1837-305a-b010-b9c1f670b103 | -10.50297 | -64.51998 | 2026-08-28 17:45:00 | NOAA-20 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 19.7 |
| cf92876d-b2bc-3737-b805-4871fac6c14d | -15.57432 | -56.29461 | 2026-08-28 17:45:00 | NOAA-20 | VÁRZEA GRANDE | MATO GROSSO | Brasil | 5108402 | 51 | 33 | nan | nan | nan | Cerrado | 18.7 |
| 6f655051-7035-30bd-aa37-2b4cb9ec2627 | -9.10795 | -60.31462 | 2026-08-28 17:45:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 31.0 |
| ef0ecd1e-35e2-320b-ae85-c153acad36b4 | -10.0507 | -68.83286 | 2026-08-28 17:45:00 | NOAA-20 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 22.8 |
| 13367d6f-1d4d-3feb-901b-ee8605a22883 | -10.51739 | -59.62194 | 2026-08-28 17:45:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 12.5 |
| 815c3e4c-591c-301f-b2c3-9b86c52a4c60 | -10.49163 | -64.49077 | 2026-08-28 17:45:00 | NOAA-20 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 22.5 |
| c3055f31-96fb-35af-bbdb-ab4080235ca6 | -9.1067 | -60.31441 | 2026-08-28 17:45:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 20.8 |
| b929cf53-698d-30f2-9790-815e6bda1f25 | -9.91543 | -60.42682 | 2026-08-28 17:45:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 58.7 |
| 6c410164-9561-338c-8353-a4ec65732f7a | -13.11104 | -50.05064 | 2026-08-28 17:45:00 | NOAA-20 | SÃO MIGUEL DO ARAGUAIA | GOIÁS | Brasil | 5220207 | 52 | 33 | nan | nan | nan | Cerrado | 17.9 |
| e2c68b54-cb28-3880-9b58-8f1e6b4b462c | -8.21374 | -54.95285 | 2026-08-28 17:45:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 7.3 |
| dbb995b8-2a86-3f50-8d84-b5a8726918d8 | -8.77833 | -50.07608 | 2026-08-28 17:45:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 11.3 |
| 9776a9cf-353f-3dee-b1d6-9235194ac693 | -8.5819 | -54.82723 | 2026-08-28 17:45:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 19.2 |
| c8bc290e-47ee-32cd-afea-1b5f83c491ec | -14.64955 | -57.0013 | 2026-08-28 17:45:00 | NOAA-20 | DENISE | MATO GROSSO | Brasil | 5103452 | 51 | 33 | nan | nan | nan | Amazônia | 16.5 |
| 9b39e7a7-06d1-38eb-98ea-5cad80fb8609 | -8.95724 | -50.79221 | 2026-08-28 17:45:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 26.5 |
| b3340cc8-a219-3420-b080-d32a4fca34ef | -15.61438 | -56.4068 | 2026-08-28 17:45:00 | NOAA-20 | NOSSA SENHORA DO LIVRAMENTO | MATO GROSSO | Brasil | 5106109 | 51 | 33 | nan | nan | nan | Cerrado | 20.8 |
| 6c29913e-a1f7-364d-a2b2-1afc8e50a84b | -9.50743 | -56.91918 | 2026-08-28 17:45:00 | NOAA-20 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 10.6 |
| f5f68661-e7dd-38dc-b996-30500c6380fe | -14.24271 | -51.765 | 2026-08-28 17:45:00 | NOAA-20 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 6.1 |
| dd73ac6c-6330-3e75-bd3c-389aad2d145a | -10.20729 | -69.3575 | 2026-08-28 17:45:00 | NOAA-20 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 32.3 |
| a30c6af3-8b82-3103-be1a-329f88bbb3ef | -11.91149 | -49.99604 | 2026-08-28 17:45:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 9.3 |
| 7d4840d8-a589-30e3-a87f-2983bbd5d65f | -15.56684 | -55.99089 | 2026-08-28 17:45:00 | NOAA-20 | CUIABÁ | MATO GROSSO | Brasil | 5103403 | 51 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 6aa5b3e2-9ad5-376f-b9df-a2c38534c6e1 | -13.42894 | -51.77225 | 2026-08-28 17:45:00 | NOAA-20 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 71.3 |


[Clique aqui para ver as próximas entradas](README142.md)
