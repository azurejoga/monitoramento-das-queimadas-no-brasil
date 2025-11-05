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

## Dados Diários - Página 27

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 7fbc905f-d4eb-3a45-acc0-0d72be81ee07 | -9.73179 | -46.3563 | 2025-11-05 04:14:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| ebb421fe-3d8b-32c8-bff4-85dfada0cd12 | -5.23431 | -48.50211 | 2025-11-05 04:14:00 | NOAA-20 | ESPERANTINA | TOCANTINS | Brasil | 1707405 | 17 | 33 | nan | nan | nan | Amazônia | 15.9 |
| ce078e24-2cfb-385c-99dc-02253e58ef87 | -7.67575 | -47.42194 | 2025-11-05 04:14:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 07fd2603-3d09-34d5-9df1-0b681fcf8060 | -12.65719 | -43.92154 | 2025-11-05 04:14:00 | NOAA-20 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| dd59767a-922f-3c11-9570-01a89f94f976 | -7.03274 | -43.80516 | 2025-11-05 04:14:00 | NOAA-20 | MARCOS PARENTE | PIAUÍ | Brasil | 2206001 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 6c566ad3-6a7a-3ac7-931a-93590430b60c | -9.77787 | -43.6146 | 2025-11-05 04:14:00 | NOAA-20 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 4.2 |
| 62739923-cd81-3873-9c37-ac4f471e6100 | -8.79622 | -40.60165 | 2025-11-05 04:14:00 | NOAA-20 | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 3d58dacc-a910-3f1d-836f-80394e8310f3 | -6.54876 | -44.46957 | 2025-11-05 04:14:00 | NOAA-20 | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 617eeff2-880f-3a64-93a1-d8e241aca773 | -7.2867 | -45.45644 | 2025-11-05 04:14:00 | NOAA-20 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 6f4da409-881b-3776-b77a-4f77b9514db6 | -9.30354 | -49.48376 | 2025-11-05 04:14:00 | NOAA-20 | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 000d5273-83de-37fb-a253-1069a7302258 | -7.64388 | -41.03175 | 2025-11-05 04:14:00 | NOAA-20 | CARIDADE DO PIAUÍ | PIAUÍ | Brasil | 2202554 | 22 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 15d3f22e-c1cc-3abd-a719-edbf7d9255f4 | -6.73648 | -44.14907 | 2025-11-05 04:14:00 | NOAA-20 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 23.3 |
| 60dfe79e-f730-361d-a6fc-2cf1bc92041d | -8.04902 | -49.63768 | 2025-11-05 04:14:00 | NOAA-20 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 11.0 |
| 7162da9f-74a8-348d-8799-f4ea9bb032ee | -8.05912 | -49.63859 | 2025-11-05 04:14:00 | NOAA-20 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| c0267fe2-97e4-3be7-ae35-71118b03fe16 | -8.22775 | -49.98858 | 2025-11-05 04:14:00 | NOAA-20 | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 9f587b41-4c04-3964-abe8-0b734ff06082 | -13.00833 | -43.64917 | 2025-11-05 04:14:00 | NOAA-20 | SÍTIO DO MATO | BAHIA | Brasil | 2930758 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 9498726c-9b6b-34ea-a475-81c6d20a4a5a | -6.52171 | -39.69158 | 2025-11-05 04:14:00 | NOAA-20 | JUCÁS | CEARÁ | Brasil | 2307403 | 23 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 4c2fbfaa-3c5c-363d-a938-844c89a4244f | -6.78247 | -47.07788 | 2025-11-05 04:14:00 | NOAA-20 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 1e6f0e75-eff5-347e-9894-bb9d1eb28d71 | -6.04297 | -42.71545 | 2025-11-05 04:14:00 | NOAA-20 | SANTO ANTÔNIO DOS MILAGRES | PIAUÍ | Brasil | 2209450 | 22 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 96e371a3-c6fa-3ab9-a7a2-eb36e98e16eb | -7.07376 | -44.95135 | 2025-11-05 04:14:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 1a615c9a-cd39-3e9a-8e44-07144f84f59d | -6.13409 | -44.81762 | 2025-11-05 04:14:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 94832930-2ec1-3913-b879-dd29e1a1c936 | -5.5707 | -47.10302 | 2025-11-05 04:14:00 | NOAA-20 | BURITIRANA | MARANHÃO | Brasil | 2102358 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 2fff090f-679c-3e65-ab77-8608c805b083 | -11.37669 | -43.13902 | 2025-11-05 04:14:00 | NOAA-20 | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 6d87c46b-746c-326a-978d-f2379c4f4a2d | -7.54451 | -45.8526 | 2025-11-05 04:14:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| c424f9ff-1cdd-3d81-9e18-cbb6be0f7f0f | -8.05761 | -49.64708 | 2025-11-05 04:14:00 | NOAA-20 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 0ff0feda-7bd1-3adb-b153-ab639cab50b6 | -6.65548 | -42.66686 | 2025-11-05 04:14:00 | NOAA-20 | FRANCISCO AYRES | PIAUÍ | Brasil | 2204105 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| 3cef6479-e4b8-3f43-8026-f8b40b7b5e0d | -6.27019 | -42.56728 | 2025-11-05 04:14:00 | NOAA-20 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 7e564a5f-5c88-38e5-b208-4be03c974a53 | -6.09899 | -44.44255 | 2025-11-05 04:14:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| fd54a5bc-0825-35fd-ad76-546416d40d29 | -6.51806 | -39.69105 | 2025-11-05 04:14:00 | NOAA-20 | JUCÁS | CEARÁ | Brasil | 2307403 | 23 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 3b7a7977-7f5f-3ffc-9fd8-0ad4c1c3184d | -8.40514 | -39.81423 | 2025-11-05 04:14:00 | NOAA-20 | SANTA MARIA DA BOA VISTA | PERNAMBUCO | Brasil | 2612604 | 26 | 33 | nan | nan | nan | Caatinga | 0.4 |
| 16d2a3b8-0657-3504-9599-04bf18594798 | -5.93124 | -44.53075 | 2025-11-05 04:14:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 419f6c5b-2a90-32a6-b2a3-adb37f458429 | -11.00792 | -42.73535 | 2025-11-05 04:14:00 | NOAA-20 | GENTIO DO OURO | BAHIA | Brasil | 2911303 | 29 | 33 | nan | nan | nan | Caatinga | 4.5 |
| 6cf16545-dbed-3871-b4eb-1cf188a81d36 | -10.40296 | -44.38773 | 2025-11-05 04:14:00 | NOAA-20 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| fdd7f632-6286-3ede-849e-a849805b44e7 | -5.69403 | -49.27728 | 2025-11-05 04:14:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 67043843-39ba-3e31-b1a2-2fc4cf1a73fb | -6.85232 | -46.29505 | 2025-11-05 04:14:00 | NOAA-20 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 80018480-e3eb-302e-ba8a-fbc4cc212cb8 | -9.78117 | -43.61514 | 2025-11-05 04:14:00 | NOAA-20 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 4.2 |
| f774788f-e33d-33c0-ae66-8ed44b8d2840 | -7.86957 | -46.78919 | 2025-11-05 04:14:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| b4b8bb67-23f3-32b7-bb02-fc0ebb4cd333 | -10.30507 | -45.01995 | 2025-11-05 04:14:00 | NOAA-20 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| de4141b4-f3c2-3a6e-a6ec-a3f4d8e35fb8 | -5.56299 | -46.38935 | 2025-11-05 04:14:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 4b129eb5-fd75-3ff4-a88d-ef0e981f1aef | -8.58793 | -43.74783 | 2025-11-05 04:14:00 | NOAA-20 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 4b341a9a-1021-3d4f-8c7a-c9c9e7ea482e | -12.39918 | -49.90535 | 2025-11-05 04:14:00 | NOAA-20 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 333ef539-2a5d-3553-9f72-75f976d357e7 | -11.36128 | -49.79414 | 2025-11-05 04:14:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ef1b8050-756d-3c6c-bca5-0f8bd2408cb1 | -9.62588 | -45.22672 | 2025-11-05 04:14:00 | NOAA-20 | MONTE ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2206605 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 12ed2059-40e3-35f0-9685-f5bde79ef944 | -10.37452 | -47.75034 | 2025-11-05 04:14:00 | NOAA-20 | SANTA TEREZA DO TOCANTINS | TOCANTINS | Brasil | 1719004 | 17 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 02fc4125-3f8e-3948-9ee0-0a5673760706 | -9.84698 | -40.26472 | 2025-11-05 04:14:00 | NOAA-20 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 6cc61a99-591f-36cb-ac30-1af0eefdd93d | -12.90365 | -45.09349 | 2025-11-05 04:14:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 09c538c1-c971-36ae-9e6b-fa4dd65dd3cb | -6.04717 | -43.03424 | 2025-11-05 04:14:00 | NOAA-20 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 2fad2a23-fba3-3c78-9700-88ddbb945c57 | -12.33636 | -43.64833 | 2025-11-05 04:14:00 | NOAA-20 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 1b9ddcc0-15c1-3b2b-ad3b-5096653efff4 | -7.5423 | -45.84418 | 2025-11-05 04:14:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 3b6b8d74-968b-33ac-b2ab-2090d14b9040 | -12.65996 | -43.92561 | 2025-11-05 04:14:00 | NOAA-20 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f2d3b798-689a-33e4-8e2f-14e682a8fe6e | -11.0152 | -42.73277 | 2025-11-05 04:14:00 | NOAA-20 | GENTIO DO OURO | BAHIA | Brasil | 2911303 | 29 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 479b72cb-b38d-3703-934e-f4618b35ef4e | -7.01522 | -46.89583 | 2025-11-05 04:14:00 | NOAA-20 | SÃO PEDRO DOS CRENTES | MARANHÃO | Brasil | 2111573 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 90800b1c-a007-34ec-855e-6fd772e0afc8 | -5.84496 | -44.36854 | 2025-11-05 04:14:00 | NOAA-20 | JATOBÁ | MARANHÃO | Brasil | 2105450 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| c389e9f9-b7e6-3d3f-8315-fa5d5823dd45 | -5.33528 | -47.95472 | 2025-11-05 04:14:00 | NOAA-20 | CARRASCO BONITO | TOCANTINS | Brasil | 1703891 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| cd12abfb-e26c-3ec3-884d-a89f3ca1c179 | -9.7083 | -49.37802 | 2025-11-05 04:14:00 | NOAA-20 | DIVINÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1707108 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 739b539f-d822-374a-9ce0-ba8e1c04798b | -7.4995 | -45.88548 | 2025-11-05 04:14:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 60c09df4-3542-3aa5-bce2-dd471c94c07e | -11.43291 | -43.95562 | 2025-11-05 04:14:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 3f6cdf37-19a6-3e8a-9b44-4e3e7d79a0a8 | -7.19423 | -45.03098 | 2025-11-05 04:14:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| d06c54cf-25ff-3a9b-8c4b-05dbde70ff3b | -8.95589 | -42.65876 | 2025-11-05 04:14:00 | NOAA-20 | SÃO RAIMUNDO NONATO | PIAUÍ | Brasil | 2210607 | 22 | 33 | nan | nan | nan | Caatinga | 3.3 |
| 4764bc3c-94a3-3445-a2d3-43f4df2d4229 | -6.55491 | -44.47421 | 2025-11-05 04:14:00 | NOAA-20 | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b6959f5b-5888-3af0-aed3-1528aa6d7e5f | -8.05408 | -49.6342 | 2025-11-05 04:14:00 | NOAA-20 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 11.0 |
| 99d9c286-95ee-378d-ac13-d18e46b39c71 | -7.4326 | -46.77969 | 2025-11-05 04:14:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a7356008-539e-38d6-a14b-d5404274d251 | -11.84675 | -43.71896 | 2025-11-05 04:14:00 | NOAA-20 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 20ea0688-5a9f-39c1-8d6f-dfe0247071e2 | -5.51218 | -46.23983 | 2025-11-05 04:14:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 4b9aa9a9-e959-3513-a47f-f83c95e91d53 | -8.93342 | -40.87008 | 2025-11-05 04:14:00 | NOAA-20 | CASA NOVA | BAHIA | Brasil | 2907202 | 29 | 33 | nan | nan | nan | Caatinga | 2.5 |
| e9aa0717-06a8-352a-b9e2-b30a1cb8e754 | -7.48436 | -41.20637 | 2025-11-05 04:14:00 | NOAA-20 | MASSAPÊ DO PIAUÍ | PIAUÍ | Brasil | 2206050 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 27f1eca6-e4f8-3032-9075-9d8ab793261c | -9.71114 | -49.38636 | 2025-11-05 04:14:00 | NOAA-20 | DIVINÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1707108 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 7f528f74-1ac6-3f7c-bd85-c6b91571c948 | -11.37613 | -43.14259 | 2025-11-05 04:14:00 | NOAA-20 | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 9afd95d7-b4b1-3e4d-9c95-b530c4f91297 | -6.30243 | -42.88044 | 2025-11-05 04:14:00 | NOAA-20 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| d1a364c5-e7de-3d71-88a5-bd27cfb15409 | -13.91401 | -42.51575 | 2025-11-05 04:16:00 | NOAA-20 | CAETITÉ | BAHIA | Brasil | 2905206 | 29 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 25311684-f40f-3bb1-9eda-abc54729e369 | -14.07509 | -44.06145 | 2025-11-05 04:16:00 | NOAA-20 | FEIRA DA MATA | BAHIA | Brasil | 2910776 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 16c3d838-82d1-3542-a637-b157f5dda79f | -16.81493 | -41.00295 | 2025-11-05 04:16:00 | NOAA-20 | JOAÍMA | MINAS GERAIS | Brasil | 3136009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 2416c723-c208-393e-9387-06fa24947520 | -18.51373 | -53.50187 | 2025-11-05 04:16:00 | NOAA-20 | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 6.4 |
| f7dc0ece-848d-3b96-bf52-72a36123a2f1 | -14.47087 | -45.87163 | 2025-11-05 04:16:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 0.3 |
| 71cb33f9-6c71-3151-a013-52b7fafedd01 | -18.26817 | -43.08139 | 2025-11-05 04:16:00 | NOAA-20 | RIO VERMELHO | MINAS GERAIS | Brasil | 3156007 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| c6dd455f-622f-3d9c-bbd8-aca8b987b993 | -18.50692 | -53.51182 | 2025-11-05 04:16:00 | NOAA-20 | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 08f08aeb-8c67-3784-97b0-cc358898e0e1 | -17.95815 | -42.702 | 2025-11-05 04:16:00 | NOAA-20 | ITAMARANDIBA | MINAS GERAIS | Brasil | 3132503 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 03629b04-0eea-326c-9c00-abecc51e7cb0 | -19.33743 | -45.84803 | 2025-11-05 04:16:00 | NOAA-20 | SERRA DA SAUDADE | MINAS GERAIS | Brasil | 3166600 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 3a7d97e1-06da-3746-a137-ad47ce2147e5 | -17.14458 | -44.64569 | 2025-11-05 04:16:00 | NOAA-20 | LAGOA DOS PATOS | MINAS GERAIS | Brasil | 3137304 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 3d254a5c-83af-3c58-a5e1-96c8792bfcef | -14.07454 | -44.06503 | 2025-11-05 04:16:00 | NOAA-20 | FEIRA DA MATA | BAHIA | Brasil | 2910776 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 8a3b6fd7-c188-3fac-afe1-b0557607e935 | -16.08067 | -41.45306 | 2025-11-05 04:16:00 | NOAA-20 | MEDINA | MINAS GERAIS | Brasil | 3141405 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| bf3b52a4-51fe-3e3a-b92d-3a858145e323 | -18.22814 | -43.60813 | 2025-11-05 04:16:00 | NOAA-20 | DIAMANTINA | MINAS GERAIS | Brasil | 3121605 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| c90539cf-02db-3a0e-815c-2b7714612dd5 | -14.58149 | -47.97849 | 2025-11-05 04:16:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 7c667f8f-896c-3741-91a6-2410da54ab2e | -13.00396 | -48.77332 | 2025-11-05 04:16:00 | NOAA-20 | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 6af8b3b5-179f-3476-9014-a82e37ae5966 | -19.34074 | -45.8486 | 2025-11-05 04:16:00 | NOAA-20 | SERRA DA SAUDADE | MINAS GERAIS | Brasil | 3166600 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 7a344da4-541b-3106-b973-ba5173ef3d44 | -18.51156 | -53.51287 | 2025-11-05 04:16:00 | NOAA-20 | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 10.2 |
| 92a911b3-0589-3c59-b9b7-2c4f2ae55d9f | -17.49731 | -44.99804 | 2025-11-05 04:16:00 | NOAA-20 | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 0.4 |
| b33e77be-9383-3843-96d2-2130c8e2c515 | -17.47177 | -44.36698 | 2025-11-05 04:16:00 | NOAA-20 | FRANCISCO DUMONT | MINAS GERAIS | Brasil | 3126604 | 31 | 33 | nan | nan | nan | Cerrado | 0.4 |
| fee9ee75-16ab-3799-8ef1-7222989039de | -16.03926 | -43.72537 | 2025-11-05 04:16:00 | NOAA-20 | SÃO JOÃO DA PONTE | MINAS GERAIS | Brasil | 3162401 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 15bfebd7-5b0f-331d-acf8-cfe6131e8aa4 | -16.03982 | -43.72163 | 2025-11-05 04:16:00 | NOAA-20 | SÃO JOÃO DA PONTE | MINAS GERAIS | Brasil | 3162401 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 45fba6db-32e3-34c2-b0e2-1dc45ae30f76 | -16.88731 | -52.85747 | 2025-11-05 04:16:00 | NOAA-20 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 0a5e7685-2067-3093-8f61-20b3c48e5fac | -14.88333 | -42.2297 | 2025-11-05 04:16:00 | NOAA-20 | MORTUGABA | BAHIA | Brasil | 2921807 | 29 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 54f96741-bf25-30b4-b1d0-b16c32bcd891 | -16.8133 | -40.99934 | 2025-11-05 04:16:00 | NOAA-20 | JOAÍMA | MINAS GERAIS | Brasil | 3136009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| bedf3050-6227-3afe-b388-50391739b421 | -17.71449 | -43.91649 | 2025-11-05 04:16:00 | NOAA-20 | BUENÓPOLIS | MINAS GERAIS | Brasil | 3109204 | 31 | 33 | nan | nan | nan | Cerrado | 0.4 |
| a610555a-6d0b-30d6-93dd-069264348403 | -17.14514 | -44.64204 | 2025-11-05 04:16:00 | NOAA-20 | LAGOA DOS PATOS | MINAS GERAIS | Brasil | 3137304 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 21ba7eb4-c3e3-3745-a66c-d5f70f81e58c | -13.04955 | -48.66953 | 2025-11-05 04:16:00 | NOAA-20 | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| bd4fc900-60bf-3cf3-a06c-1a0c0d50a4c0 | -18.50802 | -53.50624 | 2025-11-05 04:16:00 | NOAA-20 | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 956afb13-e994-3012-8fcb-dfa8c986f583 | -18.51265 | -53.50735 | 2025-11-05 04:16:00 | NOAA-20 | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 10.2 |
| 8d84e335-65c8-3519-911a-5d221adb200f | -14.48141 | -42.7264 | 2025-11-05 04:16:00 | NOAA-20 | PINDAÍ | BAHIA | Brasil | 2924504 | 29 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 1f9b2993-1cea-319b-b959-e7acc8132e7e | -16.81106 | -41.00247 | 2025-11-05 04:16:00 | NOAA-20 | JOAÍMA | MINAS GERAIS | Brasil | 3136009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |


[Clique aqui para ver as próximas entradas](README28.md)
