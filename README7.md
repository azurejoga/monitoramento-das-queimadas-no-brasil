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

## Dados Diários - Página 7

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| e6d6d28b-0014-3195-8dc1-5d6380ceedff | -6.53895 | -55.15839 | 2026-07-22 04:44:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f0bd4a35-5ada-38a2-a146-829dfdcfc554 | -8.82716 | -47.06934 | 2026-07-22 04:44:00 | NPP-375D | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| aef3d199-2137-3eb0-bc05-b4e439bfac9c | -11.38299 | -47.48518 | 2026-07-22 04:44:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ecdfa21c-5461-32ad-8dbf-382fa56b3400 | -6.56332 | -51.69652 | 2026-07-22 04:44:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 82bcdb7e-7e36-34bf-8d73-4b64549c1a49 | -7.83291 | -47.11276 | 2026-07-22 04:44:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d1db737c-c184-395c-827b-d85878ef34ba | -9.90242 | -47.8769 | 2026-07-22 04:44:00 | NPP-375D | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 23d798fc-8f8b-3db1-acb8-a3c5cc529c15 | -11.63159 | -48.5434 | 2026-07-22 04:44:00 | NPP-375D | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 30a5dc63-0f92-3536-ad1f-18332151764c | -11.38981 | -47.48619 | 2026-07-22 04:44:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d6d9b6df-78e3-3f83-8a32-7bfb7d3081c9 | -8.55858 | -47.60554 | 2026-07-22 04:44:00 | NPP-375D | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 42de3782-30cf-3f9d-8611-54141bcbe9c3 | -11.55459 | -47.61718 | 2026-07-22 04:44:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 8c8ce132-d8d8-3958-aff3-0f74089ca6c6 | -11.33058 | -48.00476 | 2026-07-22 04:44:00 | NPP-375D | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 852e9512-bca3-36bd-b414-0575b6fee8c7 | -6.01432 | -47.1103 | 2026-07-22 04:44:00 | NPP-375D | MONTES ALTOS | MARANHÃO | Brasil | 2107001 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a1ea5016-b962-3220-a317-51578d1a64c3 | -10.62987 | -47.48325 | 2026-07-22 04:44:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b39d7fe1-e915-3bf2-a9ea-ffb53f447ed4 | -6.01097 | -47.10978 | 2026-07-22 04:44:00 | NPP-375D | MONTES ALTOS | MARANHÃO | Brasil | 2107001 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e343dd47-d0fa-3a03-9dee-d0bdb7894613 | -9.09912 | -59.40066 | 2026-07-22 04:44:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 319dd5f5-f2d1-3aee-9f57-ba5858159666 | -11.33338 | -48.00891 | 2026-07-22 04:44:00 | NPP-375D | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| b327c13b-a2af-3176-84c7-f14ed82e7749 | -8.60214 | -49.84165 | 2026-07-22 04:44:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 80720e90-2cf5-3799-96ea-a643c1804bb9 | -3.9874 | -48.38839 | 2026-07-22 04:44:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| ede29f40-a146-3596-95d0-7b9ae7570ea6 | -9.64135 | -47.8108 | 2026-07-22 04:44:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ad9b389f-8bd1-3d55-87ef-487ba426a056 | -8.75251 | -49.0773 | 2026-07-22 04:44:00 | NPP-375D | GOIANORTE | TOCANTINS | Brasil | 1708304 | 17 | 33 | nan | nan | nan | Cerrado | 5.3 |
| ff344acd-2143-32a5-8c2d-a11992ab2bdc | -7.46411 | -43.39757 | 2026-07-22 04:44:00 | NPP-375D | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 3981de95-2c87-39fa-9395-f255178ba15d | -9.18617 | -58.06752 | 2026-07-22 04:44:00 | NPP-375D | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 9faef9de-e4b8-394e-aa69-9a57999f1765 | -6.56703 | -51.69713 | 2026-07-22 04:44:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a15ddc45-cad9-304d-a17a-dd7133b68485 | -5.63445 | -47.09804 | 2026-07-22 04:44:00 | NPP-375D | BURITIRANA | MARANHÃO | Brasil | 2102358 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 6c1a7894-80b5-384c-a2be-5e61ce4ce8e3 | -9.10498 | -59.40181 | 2026-07-22 04:44:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 319330d2-ec4b-3aee-8eac-c99b931451a4 | -7.88558 | -46.9067 | 2026-07-22 04:44:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a3d91465-42ec-3a81-97d9-d533ecfb4c38 | -5.66956 | -43.57248 | 2026-07-22 04:44:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 8ff8c8c8-866f-38c1-8bf0-a3aa993bcadd | -9.22444 | -48.55546 | 2026-07-22 04:44:00 | NPP-375D | RIO DOS BOIS | TOCANTINS | Brasil | 1718709 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 2cc40d16-7ad5-341b-b84a-8f21c0ca736d | -11.38356 | -47.48144 | 2026-07-22 04:44:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 52263f24-7ab5-33a7-824b-9c3063d4ee29 | -11.63548 | -48.54037 | 2026-07-22 04:44:00 | NPP-375D | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 8207aa89-e065-38ae-8f9a-d69adb28e5a0 | -10.50972 | -50.27774 | 2026-07-22 04:44:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 0fc09fed-ca0a-361b-be10-8d38cfe2c837 | -9.69647 | -47.69883 | 2026-07-22 04:44:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 3b2aab1d-58cb-316b-a071-34e7649b6ebf | -11.91189 | -43.84888 | 2026-07-22 04:44:00 | NPP-375D | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| dddbeac9-2bdf-3e29-b5c0-a0d52859950d | -11.3864 | -47.48569 | 2026-07-22 04:44:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 6ba0e308-2080-35d3-9228-7fc6a455ca8b | -8.73696 | -49.44301 | 2026-07-22 04:44:00 | NPP-375D | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| e14a9f66-6cf6-3096-af70-e563b129fcb1 | -6.20316 | -43.29173 | 2026-07-22 04:44:00 | NPP-375D | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 948e9c56-9c35-3e6d-8db9-7efb84a373e1 | -11.63881 | -48.54092 | 2026-07-22 04:44:00 | NPP-375D | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 1c511c88-b1c3-35de-9ead-226cc5a02e43 | -10.16255 | -56.80149 | 2026-07-22 04:44:00 | NPP-375D | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 425fc6a9-4bdb-3f5d-9213-63238b164b18 | -9.10418 | -59.40605 | 2026-07-22 04:44:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f0e6a953-c17b-3862-8a5f-6566867c2cfe | -5.9864 | -47.06994 | 2026-07-22 04:44:00 | NPP-375D | MONTES ALTOS | MARANHÃO | Brasil | 2107001 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 73442f49-4a3b-3ac6-87da-c739121e8250 | -9.38163 | -47.09319 | 2026-07-22 04:44:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e41b046d-91c9-375b-9730-19180b63fe1f | -7.19728 | -45.49595 | 2026-07-22 04:44:00 | NPP-375D | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e30bd0f7-ab25-3817-9911-785e801ce426 | -10.95648 | -49.81119 | 2026-07-22 04:44:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 8de3b495-0f55-3b2f-add7-2fe84defb281 | -8.74863 | -49.08027 | 2026-07-22 04:44:00 | NPP-375D | GOIANORTE | TOCANTINS | Brasil | 1708304 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 75c0978d-b7ff-3519-b7be-9cc07e782ee6 | -6.15544 | -47.11777 | 2026-07-22 04:44:00 | NPP-375D | CAMPESTRE DO MARANHÃO | MARANHÃO | Brasil | 2102556 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 1b3180cd-48ae-31a1-97b2-b30b97ba4056 | -11.42258 | -47.52124 | 2026-07-22 04:44:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 1a4c909c-e339-3c89-8d68-57c5afeeeb56 | -9.12362 | -44.28804 | 2026-07-22 04:44:00 | NPP-375D | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e74747c5-3823-38f3-aff1-de2b429b19d3 | -7.45725 | -49.72069 | 2026-07-22 04:44:00 | NPP-375D | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 60be883b-c856-3067-a6d7-595d2ba7eb86 | -11.40801 | -47.50407 | 2026-07-22 04:44:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 1e6bf68c-4082-3d00-b3c6-31ff6e44f5c3 | -11.63103 | -48.54694 | 2026-07-22 04:44:00 | NPP-375D | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| e39b8f48-a912-304d-8ddd-418974e0162b | -6.1184 | -55.80991 | 2026-07-22 04:44:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 530867b2-0ad6-33d4-8aec-7e8d4ca0318e | -6.59595 | -51.7064 | 2026-07-22 04:44:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a51a20e5-a30a-308a-8b14-aba629fa73ce | -5.74721 | -43.26756 | 2026-07-22 04:44:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| ead97eb5-a6de-3a00-a576-f9c7178a9c12 | -6.53977 | -55.15361 | 2026-07-22 04:44:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ebc534cd-6551-393b-9fee-e875a1d4c204 | -5.70886 | -45.66371 | 2026-07-22 04:44:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 22dab4a9-ef82-3e00-8d3b-b611199508c2 | -11.41426 | -47.50883 | 2026-07-22 04:44:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| d6acd3b5-2bc8-3964-a208-d950546d6c2d | -11.39608 | -47.49083 | 2026-07-22 04:44:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 5ca66e00-7893-3739-ab83-83308cd376b0 | -14.25369 | -54.76217 | 2026-07-22 04:46:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 3.2 |
| ff9333c6-b3fa-3604-896f-23e577f9eabf | -12.52069 | -48.25735 | 2026-07-22 04:46:00 | NPP-375D | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 97d583b5-eb31-3398-915d-a9157131adfd | -17.58167 | -47.50901 | 2026-07-22 04:46:00 | NPP-375D | CATALÃO | GOIÁS | Brasil | 5205109 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| fd0beea6-4f9e-3075-85eb-2c30a8bff186 | -19.72297 | -46.16973 | 2026-07-22 04:46:00 | NPP-375D | CAMPOS ALTOS | MINAS GERAIS | Brasil | 3111507 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 64da7b79-f916-3109-a64f-ea8fa2f2529d | -12.13929 | -48.26076 | 2026-07-22 04:46:00 | NPP-375D | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 1870c270-db81-386b-bedb-a2dff311d991 | -17.57366 | -47.50529 | 2026-07-22 04:46:00 | NPP-375D | CATALÃO | GOIÁS | Brasil | 5205109 | 52 | 33 | nan | nan | nan | Cerrado | 11.2 |
| b2642a87-0af7-326b-8682-5bac8d9b4669 | -12.2313 | -46.58533 | 2026-07-22 04:46:00 | NPP-375D | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| fb2c6846-dbb8-387f-9dbd-0b262bd31dfd | -12.02824 | -50.5503 | 2026-07-22 04:46:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 82eb9d5a-a092-3d8a-9877-34452de888ec | -13.71211 | -49.85404 | 2026-07-22 04:46:00 | NPP-375D | AMARALINA | GOIÁS | Brasil | 5200829 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| f03b6c3f-119c-3b1e-af24-5cc4b486268f | -12.23486 | -46.58587 | 2026-07-22 04:46:00 | NPP-375D | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 802cda82-4115-33d2-879b-16823358e852 | -12.46069 | -46.51719 | 2026-07-22 04:46:00 | NPP-375D | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| e69f8ce6-d149-31d3-a7ac-362e062c7224 | -17.57866 | -47.50417 | 2026-07-22 04:46:00 | NPP-375D | CATALÃO | GOIÁS | Brasil | 5205109 | 52 | 33 | nan | nan | nan | Cerrado | 15.6 |
| b07cee71-e292-32ce-8a95-47b255973d42 | -12.52643 | -48.53203 | 2026-07-22 04:46:00 | NPP-375D | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 0f27643f-0c96-30ba-839b-2d34cdae293b | -17.84569 | -52.48681 | 2026-07-22 04:46:00 | NPP-375D | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 8cbcdddb-2f2b-37f8-8053-38a7415ed45c | -19.72695 | -46.17039 | 2026-07-22 04:46:00 | NPP-375D | CAMPOS ALTOS | MINAS GERAIS | Brasil | 3111507 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| b998e22c-25b1-3c9c-aa8b-ccf1191fcd99 | -16.50863 | -50.40013 | 2026-07-22 04:46:00 | NPP-375D | SÃO LUÍS DE MONTES BELOS | GOIÁS | Brasil | 5220108 | 52 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 53a4997c-d070-35fe-910c-0b606ab62812 | -13.36623 | -54.31179 | 2026-07-22 04:46:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 5b3b7c3f-a3d2-3eac-ae20-c4e1d5eebef3 | -17.57006 | -47.50473 | 2026-07-22 04:46:00 | NPP-375D | CATALÃO | GOIÁS | Brasil | 5205109 | 52 | 33 | nan | nan | nan | Cerrado | 11.2 |
| f370f6c2-8eb6-3d8d-8d94-30d55c329516 | -12.32353 | -53.2808 | 2026-07-22 04:46:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 2ba56773-c30a-3a8b-94ef-42e1c4b5e345 | -17.58107 | -47.51328 | 2026-07-22 04:46:00 | NPP-375D | CATALÃO | GOIÁS | Brasil | 5205109 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 39cf192f-2949-37a6-80a1-bca158674bda | -14.43483 | -56.4491 | 2026-07-22 04:46:00 | NPP-375D | DIAMANTINO | MATO GROSSO | Brasil | 5103502 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 0faa2f27-b9b7-3870-9b0f-360e955dbf90 | -12.32079 | -53.27811 | 2026-07-22 04:46:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 9dd0aefd-f130-33bc-841e-43cff18bdb32 | -17.57446 | -47.5079 | 2026-07-22 04:46:00 | NPP-375D | CATALÃO | GOIÁS | Brasil | 5205109 | 52 | 33 | nan | nan | nan | Cerrado | 20.9 |
| 4f231d9a-dc1c-399e-894e-088bed9795ed | -18.8042 | -47.0526 | 2026-07-22 04:46:00 | NPP-375D | PATROCÍNIO | MINAS GERAIS | Brasil | 3148103 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 19827c63-9257-30cb-96ca-b0eea908e840 | -17.57806 | -47.50847 | 2026-07-22 04:46:00 | NPP-375D | CATALÃO | GOIÁS | Brasil | 5205109 | 52 | 33 | nan | nan | nan | Cerrado | 20.9 |
| 342af0f0-9a8c-3bd1-a3b7-384f0fad3382 | -15.24091 | -48.57338 | 2026-07-22 04:46:00 | NPP-375D | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e019bb18-595c-36f6-8822-d7018020999e | -17.56646 | -47.50415 | 2026-07-22 04:46:00 | NPP-375D | CATALÃO | GOIÁS | Brasil | 5205109 | 52 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 2cadce7e-9177-39e0-a5f8-99ea21b85707 | -12.69441 | -45.32407 | 2026-07-22 04:46:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| db615a74-37cd-3ee4-8db5-72b26e404428 | -12.14321 | -48.25768 | 2026-07-22 04:46:00 | NPP-375D | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 36f0ea03-e5aa-34b7-a8fe-d6398eb414fd | -17.56726 | -47.50674 | 2026-07-22 04:46:00 | NPP-375D | CATALÃO | GOIÁS | Brasil | 5205109 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| eebafeaf-8f84-39a5-bdf3-de3450c2efdd | -17.57145 | -47.50306 | 2026-07-22 04:46:00 | NPP-375D | CATALÃO | GOIÁS | Brasil | 5205109 | 52 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 465c6525-1418-33d8-a7d0-39a56aab2e71 | -17.56785 | -47.50248 | 2026-07-22 04:46:00 | NPP-375D | CATALÃO | GOIÁS | Brasil | 5205109 | 52 | 33 | nan | nan | nan | Cerrado | 5.8 |
| a6972bca-43f8-3506-a02f-0a577d6e8d07 | -17.58588 | -47.50524 | 2026-07-22 04:46:00 | NPP-375D | CATALÃO | GOIÁS | Brasil | 5205109 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| e4e3144b-4548-3329-b1d4-1e06c4959f45 | -16.48656 | -49.00953 | 2026-07-22 04:46:00 | NPP-375D | GOIANÁPOLIS | GOIÁS | Brasil | 5208400 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 8a3051b4-f439-3cdc-94f3-0243d74377e7 | -12.45711 | -46.51668 | 2026-07-22 04:46:00 | NPP-375D | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 7ca22e33-925e-3879-88c9-c1097c93ce79 | -15.24148 | -48.56963 | 2026-07-22 04:46:00 | NPP-375D | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 1d4c1bd5-5e6c-3ef6-8ed7-5e49d4ea1e21 | -17.67794 | -47.22004 | 2026-07-22 04:46:00 | NPP-375D | GUARDA-MOR | MINAS GERAIS | Brasil | 3128600 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| abece7e7-acf7-3a90-a2a3-af1737d80cb4 | -12.32914 | -50.01127 | 2026-07-22 04:46:00 | NPP-375D | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 8713f4e4-62f6-371c-87c5-4e089de5c106 | -18.98905 | -47.95052 | 2026-07-22 04:46:00 | NPP-375D | INDIANÓPOLIS | MINAS GERAIS | Brasil | 3130705 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 584e3ea0-8c06-3d12-8e72-b8996f8cd1b2 | -17.56585 | -47.50839 | 2026-07-22 04:46:00 | NPP-375D | CATALÃO | GOIÁS | Brasil | 5205109 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 26a4e497-6833-37bb-bdde-a83eac961e2b | -17.57304 | -47.50955 | 2026-07-22 04:46:00 | NPP-375D | CATALÃO | GOIÁS | Brasil | 5205109 | 52 | 33 | nan | nan | nan | Cerrado | 13.9 |
| af9283b9-2ef3-325d-94f5-b10e97036740 | -15.43836 | -49.76221 | 2026-07-22 04:46:00 | NPP-375D | CARMO DO RIO VERDE | GOIÁS | Brasil | 5205000 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| fa0f36fb-83b9-38e5-9159-d3f9dcf45bd4 | -17.57687 | -47.51694 | 2026-07-22 04:46:00 | NPP-375D | CATALÃO | GOIÁS | Brasil | 5205109 | 52 | 33 | nan | nan | nan | Cerrado | 4.4 |


[Clique aqui para ver as próximas entradas](README8.md)
