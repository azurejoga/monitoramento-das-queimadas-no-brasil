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

## Dados Diários - Página 84

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| b9837d16-0afe-3099-b214-89a0d7a000ae | -10.46667 | -51.26231 | 2026-09-19 04:57:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 68c24777-3099-368b-a69a-f9c3a2b24e38 | -9.65114 | -55.08377 | 2026-09-19 04:57:00 | NOAA-20 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0f4fc56b-5677-3498-9b99-996e181ee312 | -10.09691 | -48.41647 | 2026-09-19 04:57:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| ba5bf006-ca40-3aab-a834-2acf728ee00b | -8.6084 | -54.60645 | 2026-09-19 04:57:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| d9ef9c9a-d907-3db0-b009-948f30fc8e31 | -8.48485 | -57.6224 | 2026-09-19 04:57:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 34d4eecc-eb85-342e-8c58-7123fe082ba1 | -6.77139 | -47.86474 | 2026-09-19 04:57:00 | NOAA-20 | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 75a9060c-bf6d-379c-a85d-416a44717a4f | -9.72985 | -47.1285 | 2026-09-19 04:57:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 4d485477-3c91-3be3-b3cf-40dbc5b52888 | -7.05596 | -47.48476 | 2026-09-19 04:57:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| c7be1384-bffe-3be0-9628-ce93493b4d0b | -10.8487 | -50.18868 | 2026-09-19 04:57:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| adc6b3ff-55ce-3ec9-919b-308283020041 | -10.83392 | -50.92934 | 2026-09-19 04:57:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 9836c7e2-4c38-346c-b8bb-cf879f79fd90 | -3.55632 | -50.28971 | 2026-09-19 04:57:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| e463e311-2391-3336-b3c4-852112a8f95b | -3.0125 | -52.49649 | 2026-09-19 04:57:00 | NOAA-20 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 436e6f9a-2962-3235-9bfa-1ad484b39bfe | -2.8513 | -57.64219 | 2026-09-19 04:57:00 | NOAA-20 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b0c7a216-41ae-31b3-8a44-e124d14ab09a | -4.76785 | -55.7054 | 2026-09-19 04:57:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 38944180-009a-3b81-8d9c-700ff3176e3e | -5.22637 | -49.3033 | 2026-09-19 04:57:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| c72073ee-ff28-3c0c-b525-e7bdeca3eee1 | -10.45277 | -51.23546 | 2026-09-19 04:57:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 59dc3af5-558c-3318-96b0-e0f298d15f97 | -9.79863 | -48.32263 | 2026-09-19 04:57:00 | NOAA-20 | LAJEADO | TOCANTINS | Brasil | 1712009 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 069ae4a9-7e3e-334d-9e27-bf191fdf2c2d | -5.9158 | -52.11734 | 2026-09-19 04:57:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e2b2387a-8205-3d2c-b6d8-87ff4fa1c375 | -10.36505 | -48.89935 | 2026-09-19 04:57:00 | NOAA-20 | PUGMIL | TOCANTINS | Brasil | 1718451 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 543a175b-43c1-30e5-805a-dbfb8c8e6d56 | -9.03782 | -48.75916 | 2026-09-19 04:57:00 | NOAA-20 | GOIANORTE | TOCANTINS | Brasil | 1708304 | 17 | 33 | nan | nan | nan | Amazônia | 3.8 |
| f851f33a-e758-34d6-90fb-76b365c58597 | -9.56507 | -45.4751 | 2026-09-19 04:57:00 | NOAA-20 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |
| ec1f0fac-8c71-3a4b-9e4d-2a3252b2855a | -7.86791 | -46.44273 | 2026-09-19 04:57:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| eaf72889-04e6-38ad-b116-46fc0b45d330 | -3.75679 | -55.95549 | 2026-09-19 04:57:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| a5b86b73-567a-30c6-9fc8-5a6aa8092d64 | -11.27955 | -43.51187 | 2026-09-19 04:57:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 76796ef8-eadc-31b0-b159-bb66e5a4581b | -6.15378 | -57.69877 | 2026-09-19 04:57:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 46d6ae3a-97ff-3717-b4c4-42be1404d228 | -10.79682 | -50.89105 | 2026-09-19 04:57:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 3.8 |
| bf40dc57-70c5-3c9f-bf0f-a628f88ca4d5 | -7.02431 | -44.64978 | 2026-09-19 04:57:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 8c57c153-ba37-3885-9986-643262bef1a6 | -8.77494 | -48.66578 | 2026-09-19 04:57:00 | NOAA-20 | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Amazônia | 7.6 |
| acb7ba9f-3100-332d-87f4-50a42d424836 | -6.65576 | -50.92282 | 2026-09-19 04:57:00 | NOAA-20 | ÁGUA AZUL DO NORTE | PARÁ | Brasil | 1500347 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 9a4a430d-cb13-3303-89a5-cba062fab4ad | -3.64535 | -49.96653 | 2026-09-19 04:57:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| c080660c-3e2e-366b-8e40-281244a84f63 | -9.91036 | -46.58279 | 2026-09-19 04:57:00 | NOAA-20 | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 412f3521-41a8-3334-80cf-0bedbcc6685e | -11.00179 | -48.31862 | 2026-09-19 04:57:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 11.3 |
| 4586731b-1fd2-3d39-8554-eb2fb46a5ddc | -8.98887 | -50.17318 | 2026-09-19 04:57:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 721e5174-288a-392a-a8b4-e0ad25feb410 | -10.79867 | -50.87874 | 2026-09-19 04:57:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 891b5d44-1986-3d3c-882d-72d0a3193b7f | -3.32066 | -50.43081 | 2026-09-19 04:57:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c5ce434f-4b2b-3e62-ae4d-c731d7ff3291 | -6.37147 | -58.29442 | 2026-09-19 04:57:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ebb2fd20-f355-3119-a457-7951b9ba079e | -11.05039 | -48.30515 | 2026-09-19 04:57:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| be3c205e-5a78-3c91-ba7a-012cca63d770 | -11.46518 | -45.71805 | 2026-09-19 04:57:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| e00d4b21-b993-3e1a-8071-88c2bf109575 | -8.16385 | -54.82388 | 2026-09-19 04:57:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| aa81d875-4fa7-32ca-ad88-2856aff545c5 | -7.88411 | -46.42629 | 2026-09-19 04:57:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 8e49adbf-ce8f-3fb0-8fee-87eeff6384a9 | -4.42388 | -55.51315 | 2026-09-19 04:57:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 33558dee-5837-36ca-9d62-e9a996fc036c | -11.32677 | -47.35508 | 2026-09-19 04:57:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| cdddd512-7b9c-3f09-b414-5027909ab40b | -10.58984 | -46.59982 | 2026-09-19 04:57:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 1b809496-aaae-376d-96b5-6c445c7d6f5b | -2.89905 | -57.79994 | 2026-09-19 04:57:00 | NOAA-20 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 7.3 |
| 2e5bc6aa-0fe1-3945-961c-a8b34b0fbcc6 | -8.77029 | -48.67014 | 2026-09-19 04:57:00 | NOAA-20 | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Amazônia | 2.8 |
| c2134650-7cb2-3a32-a596-c315f7ff1069 | -9.93756 | -53.98418 | 2026-09-19 04:57:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 01e525ef-996e-35db-a212-99bf384671c7 | -9.79022 | -46.08772 | 2026-09-19 04:57:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 75f0c6fe-7e48-35ec-861b-48be888ed449 | -10.17623 | -48.52843 | 2026-09-19 04:57:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 0a6ddbe0-4e90-3d48-ad50-a39c299a4b34 | -6.65254 | -51.48718 | 2026-09-19 04:57:00 | NOAA-20 | TUCUMÃ | PARÁ | Brasil | 1508084 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6014ce5c-9c40-31ff-853f-7ee14d0da2ad | -8.61177 | -54.61782 | 2026-09-19 04:57:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 25806834-b76c-3b08-9e12-d570c23d7da5 | -9.93823 | -45.27792 | 2026-09-19 04:57:00 | NOAA-20 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 54326eb9-d6fe-325e-860b-ba62b9d26e51 | -7.36194 | -50.3306 | 2026-09-19 04:57:00 | NOAA-20 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| e9d34a5c-b2e6-31dd-a223-e4a91e00b65d | -8.66998 | -45.44095 | 2026-09-19 04:57:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 131e1003-7703-3b5b-a10a-d2e8959d1a1e | -7.00122 | -49.74976 | 2026-09-19 04:57:00 | NOAA-20 | XINGUARA | PARÁ | Brasil | 1508407 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6d0810f2-fa9b-3727-80d8-653af9a312b6 | -8.41853 | -54.72343 | 2026-09-19 04:57:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 83056515-fdf4-343e-bb53-d55a9532b439 | -3.81837 | -50.74368 | 2026-09-19 04:57:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 2f8c562d-34ab-3cd6-8e77-0d16bf8ce6b9 | -10.30784 | -49.95375 | 2026-09-19 04:57:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 18fdeb92-6429-3178-8845-b424c837ca71 | -11.07516 | -48.31024 | 2026-09-19 04:57:00 | NOAA-20 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 4.7 |
| d0a075f2-80b4-3065-b882-6cff37c17641 | -6.76559 | -59.42276 | 2026-09-19 04:57:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 8f98018d-8fd3-3c5e-be06-646b4a503046 | -11.36562 | -47.32594 | 2026-09-19 04:57:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 67345aff-1810-3c10-854d-6121c962e435 | -10.00006 | -50.27601 | 2026-09-19 04:57:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 9d344286-4e97-3e82-aa49-5a695fdfe993 | -6.65292 | -50.91856 | 2026-09-19 04:57:00 | NOAA-20 | ÁGUA AZUL DO NORTE | PARÁ | Brasil | 1500347 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 300f4acc-e921-353b-a723-093efff12000 | -5.89321 | -53.56639 | 2026-09-19 04:57:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 2cf36a15-5cb3-3d55-ba5c-bba784f4aead | -10.45326 | -48.68066 | 2026-09-19 04:57:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 11.2 |
| 2a5bc61f-37ed-3b23-91c9-cdee5eafc706 | -11.33901 | -47.35472 | 2026-09-19 04:57:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 0cc4526d-81aa-3ffd-8f78-188be73b5ed7 | -8.76635 | -48.66952 | 2026-09-19 04:57:00 | NOAA-20 | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Amazônia | 8.7 |
| 2849effc-d7cf-3237-8d16-1b0be88d00b4 | -7.56738 | -57.66969 | 2026-09-19 04:57:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 10b32a7a-3923-31c6-82e8-7e97cd9df201 | -8.36018 | -47.2374 | 2026-09-19 04:57:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| d44e3f7b-83f8-368e-b5ed-4e20e1799bf3 | -10.70403 | -50.25914 | 2026-09-19 04:57:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| f92a5afd-6500-3da2-953b-3c1fdcb47eec | -6.23401 | -51.71455 | 2026-09-19 04:57:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ced31646-4122-3ca1-8b57-6e7320062c5c | -11.05702 | -47.94834 | 2026-09-19 04:57:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 619b0e41-bf1b-3ab9-a730-34d1f13ae777 | -8.27114 | -62.73923 | 2026-09-19 04:57:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 7a29fe0f-bfe8-39f3-a89d-8200a461771d | -8.16326 | -54.82753 | 2026-09-19 04:57:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| aa54e037-c765-3ba2-a332-b4cc4bc2ec2e | -8.61133 | -54.59933 | 2026-09-19 04:57:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 3697ba6a-ce0f-3f10-a067-9fac199c3192 | -10.83512 | -50.92115 | 2026-09-19 04:57:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b6246718-d6ab-3bc0-8604-4c095d9bc36f | -9.34132 | -48.18665 | 2026-09-19 04:57:00 | NOAA-20 | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| d5054753-f3b2-3c99-8aff-5d6a7b357766 | -4.53435 | -54.93549 | 2026-09-19 04:57:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| ca2254ff-48bf-3f10-82a1-c5bd905e6a35 | -7.60345 | -45.42346 | 2026-09-19 04:57:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 487b0522-ec13-3b34-aaa6-d4123b2b209b | -8.76959 | -48.67501 | 2026-09-19 04:57:00 | NOAA-20 | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 8b1daac6-2261-398a-b6ce-d0e1d17b6921 | -9.15378 | -49.99068 | 2026-09-19 04:57:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 55bd16f2-6539-399b-8eac-0c0ae4dfede0 | -10.79898 | -46.641 | 2026-09-19 04:57:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| b2d21068-762f-3dc6-b0b4-4a61dba90198 | -4.28519 | -48.58934 | 2026-09-19 04:57:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 9c314cc8-634f-3948-8c73-bc5432a973f2 | -8.16505 | -54.81656 | 2026-09-19 04:57:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 94fb287c-6951-3233-bd6d-42a8ad8b16da | -6.01019 | -51.79916 | 2026-09-19 04:57:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 28b81d13-90d3-3308-a84c-dc2172f587a0 | -11.28532 | -43.51266 | 2026-09-19 04:57:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 5fc5e615-58df-3ba6-ae81-e0c35d7a796d | -8.77676 | -48.6811 | 2026-09-19 04:57:00 | NOAA-20 | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Amazônia | 8.5 |
| 1c9636f1-bc91-33a9-b7a1-4ab7fea3c8db | -6.93921 | -55.03983 | 2026-09-19 04:57:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 54e5c3a0-ed00-36f9-a9df-c536335ecfd9 | -3.89013 | -49.06612 | 2026-09-19 04:57:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| a70b230d-017f-3e71-bb4a-afe9979188d8 | -4.18139 | -49.40561 | 2026-09-19 04:57:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a35c7615-a8d7-333b-ba2b-885809b0aff2 | -6.66951 | -50.90206 | 2026-09-19 04:57:00 | NOAA-20 | ÁGUA AZUL DO NORTE | PARÁ | Brasil | 1500347 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| bfeaea06-a7c8-3138-ae75-1022b371d9b8 | -8.85805 | -45.94547 | 2026-09-19 04:57:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 11.6 |
| cdabc756-60d3-3135-b035-9694f351a864 | -4.55186 | -42.97737 | 2026-09-19 04:57:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 51b11dd7-dfe4-35c2-9f46-c8bd91bf2cfb | -9.83793 | -48.39796 | 2026-09-19 04:57:00 | NOAA-20 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 545b2da8-843f-3411-9715-820a2f821ccd | -6.57877 | -44.15762 | 2026-09-19 04:57:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 4245dda4-9e8a-394d-bf71-cc57cfc23eea | -11.07733 | -48.29506 | 2026-09-19 04:57:00 | NOAA-20 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 19d98682-e250-3ec2-99c8-4864b938d9cb | -7.6075 | -45.42954 | 2026-09-19 04:57:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| c02c6449-dcbe-3ca0-957a-a84e4279e3e8 | -3.42717 | -50.66554 | 2026-09-19 04:57:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 0a163d5d-beaf-3a95-b092-9f5d22757284 | -4.50418 | -54.96669 | 2026-09-19 04:57:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 55df1a8b-37f1-3f4a-acb5-7faa886314d1 | -4.48923 | -55.48407 | 2026-09-19 04:57:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 11c74b8f-00e7-37a2-a1fd-2fa7fd011cd3 | -9.1525 | -49.99932 | 2026-09-19 04:57:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |


[Clique aqui para ver as próximas entradas](README85.md)
