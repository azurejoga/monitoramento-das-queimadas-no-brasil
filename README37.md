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

## Dados Diários - Página 37

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 8729a851-e009-3bd5-b7fd-dd4fb635fff7 | -10.8661 | -54.10443 | 2026-09-19 04:04:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 4.4 |
| df6532fb-b144-3331-929b-891181d6886d | -12.14033 | -45.143 | 2026-09-19 04:04:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| ec0779f7-5fc1-394f-952c-0da651500060 | -11.50038 | -50.7315 | 2026-09-19 04:04:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 6a4a6bcd-a74f-3d67-9424-2e83abd49d51 | -12.14177 | -47.01429 | 2026-09-19 04:04:00 | NOAA-21 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 055411de-82a6-3646-a01a-a06ff2d9920a | -18.83111 | -44.52279 | 2026-09-19 04:04:00 | NOAA-21 | CURVELO | MINAS GERAIS | Brasil | 3120904 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 73de8a51-9816-3b08-9bcf-fd4204f402a3 | -11.79477 | -46.82539 | 2026-09-19 04:04:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| c8537148-d097-3462-b50f-fca7bc289014 | -12.55285 | -47.08055 | 2026-09-19 04:04:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 3f9677b1-4dc7-3cf4-ac85-ec3ba2d5d8fb | -14.15099 | -45.20732 | 2026-09-19 04:04:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 34a3fb5a-10ae-3511-a5f3-b5304feeef61 | -12.97252 | -46.983 | 2026-09-19 04:04:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 1dc30544-eec7-39ad-a782-9d74f22c152f | -11.91257 | -50.12577 | 2026-09-19 04:04:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 5.7 |
| ad071967-4390-3403-956e-f6d4df12e823 | -12.15333 | -46.97312 | 2026-09-19 04:04:00 | NOAA-21 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| a0670ffd-b693-33a4-a08d-436d4331f23a | -10.89072 | -50.88429 | 2026-09-19 04:04:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| ebb311c1-b5a0-369d-ac05-f1e0cb283a1c | -12.14122 | -46.99339 | 2026-09-19 04:04:00 | NOAA-21 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| dd61d000-cda9-34b5-b817-31f37c48816d | -11.00296 | -48.32347 | 2026-09-19 04:04:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 6.4 |
| f2e4d9de-b025-3286-a7a0-b88aab5f7839 | -11.07907 | -48.2962 | 2026-09-19 04:04:00 | NOAA-21 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |
| c6675132-30bb-32d8-b1e8-1e9e7d0c5512 | -12.13985 | -47.0011 | 2026-09-19 04:04:00 | NOAA-21 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 8b74cee4-d122-332b-b5a6-bee8bcb7d8c8 | -10.82726 | -50.15895 | 2026-09-19 04:04:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 3744a636-df14-31f3-9a38-8ca8b0b74f4f | -14.7939 | -48.58053 | 2026-09-19 04:04:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| deff4de6-9956-3186-b206-5f887ab079b5 | -13.61549 | -48.32519 | 2026-09-19 04:04:00 | NOAA-21 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 3.7 |
| c9455548-a759-3dfc-a211-d4da8f66f855 | -11.06544 | -48.26664 | 2026-09-19 04:04:00 | NOAA-21 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| fe67db8f-8443-3a6f-a7cd-3410b36c6baf | -13.60994 | -48.30653 | 2026-09-19 04:04:00 | NOAA-21 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 44d8be08-0bb9-3236-b049-0e91b84075cf | -12.14917 | -46.97256 | 2026-09-19 04:04:00 | NOAA-21 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 8d1a2d8f-0eb7-3503-952e-d992057b8965 | -13.73337 | -48.80231 | 2026-09-19 04:04:00 | NOAA-21 | FORMOSO | GOIÁS | Brasil | 5208103 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 38d463ea-f5d4-31b5-91cd-4a4baff79548 | -12.38815 | -48.47741 | 2026-09-19 04:04:00 | NOAA-21 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 9dc369ea-bfbb-3fba-b9f4-cd2d03681470 | -12.81697 | -38.41447 | 2026-09-19 04:04:00 | NOAA-21 | SIMÕES FILHO | BAHIA | Brasil | 2930709 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 2c6ff36a-db3e-3485-8246-63fa25f0690b | -14.1019 | -44.82682 | 2026-09-19 04:04:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| cc4866fa-40ff-3422-842c-e76f4fb7c980 | -18.335 | -44.01221 | 2026-09-19 04:04:00 | NOAA-21 | MONJOLOS | MINAS GERAIS | Brasil | 3142502 | 31 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 0266545a-c96e-37db-ac28-8829e33057e3 | -13.74074 | -48.79469 | 2026-09-19 04:04:00 | NOAA-21 | FORMOSO | GOIÁS | Brasil | 5208103 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| b4c8dee5-afff-301d-99d8-07009b0d8ecc | -12.14782 | -46.98017 | 2026-09-19 04:04:00 | NOAA-21 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 6394769c-71c7-3bfb-b1fa-e7e0ea219ecf | -12.33765 | -50.71492 | 2026-09-19 04:04:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 7e6b1f25-5ae5-3cd1-881c-eb4ea048cacb | -11.05613 | -49.75696 | 2026-09-19 04:04:00 | NOAA-21 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| cd30c6cc-e3b6-3c49-98b0-8a4fdc375568 | -10.80336 | -50.89384 | 2026-09-19 04:04:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d19ba801-c941-300d-99b9-11455a8dc4cd | -14.68919 | -46.64808 | 2026-09-19 04:04:00 | NOAA-21 | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 8cf358d0-e1d7-3374-8226-1d7121c2a64e | -12.41781 | -45.03685 | 2026-09-19 04:04:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c104cd01-97e1-3c89-98a8-bbd3713042c2 | -17.83514 | -44.84817 | 2026-09-19 04:04:00 | NOAA-21 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| db1e8047-0105-37e0-9cb1-423a530c2b44 | -13.02274 | -46.93694 | 2026-09-19 04:04:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 1a5f044e-78c2-343d-a037-25d5c4ccdf7d | -14.66797 | -46.65463 | 2026-09-19 04:04:00 | NOAA-21 | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 9.7 |
| 8e716111-7d21-36c4-9e0d-6b6745a98bd2 | -10.82666 | -50.16219 | 2026-09-19 04:04:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 47b1ea9b-7274-3e52-92ac-6ad721b9b2ab | -14.15363 | -45.2202 | 2026-09-19 04:04:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 6edf4074-8a3e-3e99-a6c9-e2e3f793777a | -14.93802 | -49.9348 | 2026-09-19 04:04:00 | NOAA-21 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 27457b51-0993-3765-af66-c86b89a81eda | -10.82605 | -50.16543 | 2026-09-19 04:04:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 392282ee-0aae-34d0-8b0e-71d1ae121724 | -12.41707 | -45.04126 | 2026-09-19 04:04:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 1582a087-2c91-3f30-a02f-80c69630e1da | -13.73896 | -48.79728 | 2026-09-19 04:04:00 | NOAA-21 | FORMOSO | GOIÁS | Brasil | 5208103 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| caa241b7-8a3f-3eb4-9214-afcfd4ca61ed | -12.13822 | -46.98626 | 2026-09-19 04:04:00 | NOAA-21 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 6.0 |
| eb835e31-dfd0-3b75-9c0f-7f859001af10 | -16.8338 | -47.64283 | 2026-09-19 04:04:00 | NOAA-21 | CRISTALINA | GOIÁS | Brasil | 5206206 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| f4f2aefa-60d8-3f29-be77-8ea20146eb1c | -11.85501 | -47.45102 | 2026-09-19 04:04:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| ed4dfc8c-c655-3b2b-8b8f-c95a182e6956 | -14.15459 | -45.16362 | 2026-09-19 04:04:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 8f67a3a5-f3ae-3c85-b963-2469eb8c5c8e | -17.31987 | -46.62756 | 2026-09-19 04:04:00 | NOAA-21 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 5b05131e-3510-3016-831f-6d13941e97b3 | -12.98189 | -46.97765 | 2026-09-19 04:04:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| ff03c81e-7de6-36c6-bbf4-db80a08dde0c | -11.59134 | -47.29496 | 2026-09-19 04:04:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 36d9efdf-1118-3b55-a9df-5d9c266984ff | -12.14058 | -46.99697 | 2026-09-19 04:04:00 | NOAA-21 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 6f81ab92-0eb1-3618-aac2-2dd5776964b6 | -17.31615 | -46.62685 | 2026-09-19 04:04:00 | NOAA-21 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 3.2 |
| ca7bb94d-cc1a-32a3-9bc3-0466cc23921b | -10.79994 | -50.88194 | 2026-09-19 04:04:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 54bc6869-0642-3b5a-9aae-aad700d40065 | -13.009 | -46.96703 | 2026-09-19 04:04:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| e0945f2b-39d4-35b4-b039-96d68c17231c | -13.00501 | -46.96586 | 2026-09-19 04:04:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 5f94bf6b-bca6-3489-82c6-e51197dc859e | -13.74425 | -48.80088 | 2026-09-19 04:04:00 | NOAA-21 | FORMOSO | GOIÁS | Brasil | 5208103 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 0c9b072f-3fa4-3fed-b2c5-f304d7e48de9 | -12.33381 | -50.73491 | 2026-09-19 04:04:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| acdc8bfb-b020-3c77-9a99-08f718d004dd | -11.83074 | -46.82985 | 2026-09-19 04:04:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 59492a95-073f-3140-a218-8359541ddd49 | -12.69821 | -45.95412 | 2026-09-19 04:04:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 6e4c2c5c-987e-3101-8976-17b021bbffef | -11.0589 | -49.74999 | 2026-09-19 04:04:00 | NOAA-21 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 9dc56558-2e14-3abc-974e-ccf699042738 | -16.07284 | -52.25603 | 2026-09-19 04:04:00 | NOAA-21 | ARAGARÇAS | GOIÁS | Brasil | 5201702 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b424c5e0-091a-35d7-9fdf-e1dd8939ccd2 | -12.57744 | -49.07556 | 2026-09-19 04:04:00 | NOAA-21 | ALVORADA | TOCANTINS | Brasil | 1700707 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 295e9891-9d18-3dbf-9f9f-2fbd181cc822 | -14.17495 | -48.75423 | 2026-09-19 04:04:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 246dbcf1-123e-3fff-8e9d-7d01f2cd042d | -12.59878 | -50.87768 | 2026-09-19 04:04:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 577ff7a0-ba11-3c62-8443-2c727242e541 | -11.31236 | -46.7545 | 2026-09-19 04:04:00 | NOAA-21 | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| fedc1137-aa9f-3ead-9637-0c0d5bc19e3d | -11.32856 | -47.68148 | 2026-09-19 04:04:00 | NOAA-21 | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 919d1582-7a7e-34b0-8c9d-8e0488f06fb4 | -11.06567 | -49.76187 | 2026-09-19 04:04:00 | NOAA-21 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 782f17e2-bc1d-336a-9af4-4556bff71616 | -11.13173 | -49.04417 | 2026-09-19 04:04:00 | NOAA-21 | CRIXÁS DO TOCANTINS | TOCANTINS | Brasil | 1706258 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 10a6aef4-d62d-3939-ad95-215f0aada6e9 | -13.63119 | -48.31408 | 2026-09-19 04:04:00 | NOAA-21 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| f7e37a10-7b33-3544-be07-039541d53414 | -12.54663 | -47.09146 | 2026-09-19 04:04:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| c244fa6c-2fd3-383a-8735-7367112dcd79 | -14.69516 | -46.6596 | 2026-09-19 04:04:00 | NOAA-21 | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 20.1 |
| c9b6bdb0-51ea-3e62-beac-74ce94351def | -12.34941 | -48.20328 | 2026-09-19 04:04:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| a62b2a34-d5f8-35c3-ad18-6c8431a784f9 | -13.7351 | -48.79971 | 2026-09-19 04:04:00 | NOAA-21 | FORMOSO | GOIÁS | Brasil | 5208103 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| cd44e7cf-0df6-3bb1-9f1e-0c65abcf7002 | -10.27679 | -50.00338 | 2026-09-19 04:04:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 394b155a-92dd-3c58-889b-132be153b7b6 | -11.07983 | -48.29195 | 2026-09-19 04:04:00 | NOAA-21 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 23.8 |
| 6a24cfde-1601-3dcb-b110-7ca81a72b8c9 | -12.86351 | -46.33072 | 2026-09-19 04:04:00 | NOAA-21 | LAVANDEIRA | TOCANTINS | Brasil | 1712157 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 36b2d87e-8983-3b51-9802-65cf5cc0d6c2 | -12.12991 | -46.98507 | 2026-09-19 04:04:00 | NOAA-21 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 4e5dc170-5b27-382b-95c6-dea679229912 | -13.73716 | -48.78884 | 2026-09-19 04:04:00 | NOAA-21 | FORMOSO | GOIÁS | Brasil | 5208103 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 3e6a1197-a678-3a92-983b-2e707f4578cb | -11.83417 | -46.83437 | 2026-09-19 04:04:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 1817d6a8-26bf-3e5e-84cb-984e92805ca6 | -15.62752 | -52.72461 | 2026-09-19 04:04:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 7c237658-b9c2-3d2f-88ef-9f2dc4de407c | -15.64104 | -52.71601 | 2026-09-19 04:04:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 39b7f7ce-d187-31fe-a0d2-85139d6cf368 | -13.60917 | -48.31082 | 2026-09-19 04:04:00 | NOAA-21 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 8639ba69-be63-3496-a6a2-9530034adc71 | -11.37666 | -47.30367 | 2026-09-19 04:04:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ac79e338-76f8-328b-a903-6de269c3d35e | -11.30063 | -46.77267 | 2026-09-19 04:04:00 | NOAA-21 | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 6e43d5ab-046a-3cd0-9b1a-ecc383acca16 | -12.85565 | -44.39254 | 2026-09-19 04:04:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 87975d3f-46f9-3ef3-954b-3b8e0739c365 | -12.58311 | -49.09791 | 2026-09-19 04:04:00 | NOAA-21 | ALVORADA | TOCANTINS | Brasil | 1700707 | 17 | 33 | nan | nan | nan | Cerrado | 8.4 |
| af0f9b93-18b7-32c3-acc2-897bc34bad2f | -10.83528 | -50.1739 | 2026-09-19 04:04:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 281d24e2-5e4f-34bc-9d6b-a665f2d8357d | -11.32832 | -47.35254 | 2026-09-19 04:04:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 98a6cd1b-9e81-300b-9f58-554b85cb2e3d | -12.99248 | -46.91895 | 2026-09-19 04:04:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a65919ff-a892-36bb-9e67-3347a98100c6 | -12.28004 | -49.16415 | 2026-09-19 04:04:00 | NOAA-21 | ALVORADA | TOCANTINS | Brasil | 1700707 | 17 | 33 | nan | nan | nan | Cerrado | 32.1 |
| 11357e03-a78e-3cc0-bab3-25f221af6887 | -12.86556 | -46.34187 | 2026-09-19 04:04:00 | NOAA-21 | LAVANDEIRA | TOCANTINS | Brasil | 1712157 | 17 | 33 | nan | nan | nan | Cerrado | 12.2 |
| 7beb1e74-cd67-357f-83f7-34568f2e319a | -13.39196 | -49.45647 | 2026-09-19 04:04:00 | NOAA-21 | PORANGATU | GOIÁS | Brasil | 5218003 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 3d626fba-e82d-3165-a38c-74cf2e8389b5 | -12.16284 | -46.96745 | 2026-09-19 04:04:00 | NOAA-21 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ccae5f80-87bd-330a-8065-53a2cc4f6a05 | -13.62326 | -48.30791 | 2026-09-19 04:04:00 | NOAA-21 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 61b359ac-2e8c-3bc5-a610-f5844d91cdcc | -11.49503 | -50.73047 | 2026-09-19 04:04:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f4dc666b-1843-3f91-b137-52de63cad191 | -14.67574 | -46.65604 | 2026-09-19 04:04:00 | NOAA-21 | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 744d8ae7-561c-309f-87e4-666e312f0228 | -12.9774 | -46.98065 | 2026-09-19 04:04:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 59f5878e-a6ac-3972-9634-e5f0db44746b | -12.59724 | -49.10062 | 2026-09-19 04:04:00 | NOAA-21 | ALVORADA | TOCANTINS | Brasil | 1700707 | 17 | 33 | nan | nan | nan | Cerrado | 11.0 |
| f0eb53ac-9b45-30f0-a52a-29c2149e0529 | -15.5822 | -56.55742 | 2026-09-19 04:04:00 | NOAA-21 | NOSSA SENHORA DO LIVRAMENTO | MATO GROSSO | Brasil | 5106109 | 51 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 1db622a5-7fff-3250-a6d2-a2297cad5b46 | -13.24067 | -46.91378 | 2026-09-19 04:04:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |


[Clique aqui para ver as próximas entradas](README38.md)
