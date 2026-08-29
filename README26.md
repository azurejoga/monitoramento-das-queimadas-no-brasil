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
| cf285c11-69ef-3987-a95c-3c4d5ec38971 | -14.04113 | -40.9555 | 2026-08-29 03:57:00 | NOAA-21 | MIRANTE | BAHIA | Brasil | 2921450 | 29 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 086b6e58-808c-39b5-b556-eefeea1638bd | -12.43538 | -43.41011 | 2026-08-29 03:57:00 | NOAA-21 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 04729412-840c-3918-818f-e9eb2d173dc6 | -14.19728 | -52.85507 | 2026-08-29 03:57:00 | NOAA-21 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 6.9 |
| dedcd56f-43e6-35ac-8c7a-a5746f88fbb2 | -13.3141 | -48.20372 | 2026-08-29 03:57:00 | NOAA-21 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 4.0 |
| b25bb16b-36d8-33ca-90ef-1f6bcb45470c | -13.49465 | -42.44056 | 2026-08-29 03:57:00 | NOAA-21 | TANQUE NOVO | BAHIA | Brasil | 2931053 | 29 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 85701f9a-69f2-3044-bf7f-60f7fe7dcddb | -16.47963 | -49.4291 | 2026-08-29 03:57:00 | NOAA-21 | GOIANIRA | GOIÁS | Brasil | 5208806 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d8064bbe-7a47-3371-ab53-8cfe8b0ec32c | -17.24528 | -46.92439 | 2026-08-29 03:57:00 | NOAA-21 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 12d51120-0d0c-304f-a4dd-4163da501847 | -14.90744 | -43.41201 | 2026-08-29 03:57:00 | NOAA-21 | GAMELEIRAS | MINAS GERAIS | Brasil | 3127339 | 31 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 75f2fd6c-4bc3-334e-a02d-745e153cd291 | -12.24666 | -50.53697 | 2026-08-29 03:57:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| c163aecb-d14d-34a0-9c1a-82b93ede4de8 | -14.76796 | -48.74841 | 2026-08-29 03:57:00 | NOAA-21 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 4c2369db-530e-3d9b-a8eb-505ad3106d71 | -13.59612 | -45.78197 | 2026-08-29 03:57:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 1051a7b0-5138-3831-a290-c27657f0d917 | -14.42818 | -52.58712 | 2026-08-29 03:57:00 | NOAA-21 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 10f6d7f9-bfd8-395d-aacc-547f9a439f59 | -12.38095 | -48.19087 | 2026-08-29 03:57:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 692db48a-9651-34f0-acc9-d8471adc3fad | -17.39872 | -41.59622 | 2026-08-29 03:57:00 | NOAA-21 | ITAIPÉ | MINAS GERAIS | Brasil | 3132305 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 5e5cad36-966d-3373-ac9f-21ad04b9db2e | -14.19225 | -48.7569 | 2026-08-29 03:57:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| be39fc6d-6da2-3d74-a8e3-2055784cf628 | -17.28085 | -46.04454 | 2026-08-29 03:57:00 | NOAA-21 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| f628606d-eb61-33a4-ad6e-06c694079ef3 | -14.41356 | -51.73761 | 2026-08-29 03:57:00 | NOAA-21 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 0f60c4e8-9a93-3cbe-9a0f-403a29ee27d7 | -14.41382 | -52.57478 | 2026-08-29 03:57:00 | NOAA-21 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 3.1 |
| ff4a39d4-4eb2-3852-88fb-00e0adf0c5a6 | -14.76198 | -48.75298 | 2026-08-29 03:57:00 | NOAA-21 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 1784a6fc-3ca3-3c5e-933f-0b0e5a6849f4 | -14.18113 | -48.76091 | 2026-08-29 03:57:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |
| c1b08419-b253-3834-9ac9-f7dd763a6c05 | -19.29453 | -45.81694 | 2026-08-29 03:57:00 | NOAA-21 | QUARTEL GERAL | MINAS GERAIS | Brasil | 3153707 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 3c1f9975-db0d-33c0-bb85-430d5c9f14be | -14.75863 | -48.74953 | 2026-08-29 03:57:00 | NOAA-21 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 097f2561-0e1c-3654-9aa8-6a6f6b0d02f0 | -17.58361 | -51.63726 | 2026-08-29 03:57:00 | NOAA-21 | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 796c4210-92af-3094-b8c6-4dc0834abbae | -14.07565 | -44.06166 | 2026-08-29 03:57:00 | NOAA-21 | FEIRA DA MATA | BAHIA | Brasil | 2910776 | 29 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 017bd340-46a2-3b18-b339-4a63f6ffde72 | -12.43097 | -43.41388 | 2026-08-29 03:57:00 | NOAA-21 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 0614dfaa-9f3e-3a54-bdd2-f638c718b5ce | -15.65463 | -48.37204 | 2026-08-29 03:57:00 | NOAA-21 | COCALZINHO DE GOIÁS | GOIÁS | Brasil | 5205513 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| ecc52792-6faa-3819-b23c-a0551bebd631 | -12.76834 | -44.26414 | 2026-08-29 03:57:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 695a3214-a0d4-3207-9386-fbda12a224b0 | -5.8894 | -57.7708 | 2026-08-29 04:00:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 75.2 |
| 4a7ec665-1d67-39cb-bf69-715565947864 | -5.9819 | -57.6892 | 2026-08-29 04:00:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 56.0 |
| dcded2c3-b79a-3623-a396-e374fe615cb6 | -10.4794 | -64.5012 | 2026-08-29 04:00:00 | GOES-19 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 85.0 |
| 035cc9ca-0c9a-3c5c-b696-8afcb49445b4 | -5.9079 | -57.7506 | 2026-08-29 04:00:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 42.3 |
| 4d070cc4-24d2-34da-bbcb-4498ac360a44 | -6.7884 | -55.6635 | 2026-08-29 04:00:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 120.6 |
| 215807c2-cac2-337d-9326-9a13119ef3dc | -6.7699 | -55.6644 | 2026-08-29 04:00:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 118.8 |
| c44bccd3-e349-3285-88d3-b4985c6bb30a | -10.4608 | -64.502 | 2026-08-29 04:00:00 | GOES-19 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 44.1 |
| 4259ac3e-c743-388b-973b-73a5828c70f0 | -7.5139 | -55.2851 | 2026-08-29 04:00:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 56.3 |
| 73a3a324-25d6-3ac8-ab17-572e401cf9aa | -7.5137 | -55.3051 | 2026-08-29 04:00:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 118.8 |
| 0c82f095-52df-3e18-a8e7-49ebf7030537 | -7.4952 | -55.3062 | 2026-08-29 04:00:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 62.5 |
| 6aba264f-20d1-30ac-a095-8463ff57c80f | -10.4795 | -64.4824 | 2026-08-29 04:00:00 | GOES-19 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 46.5 |
| d7638a71-4191-3970-9afa-59be5d94ecc2 | -5.8895 | -57.7513 | 2026-08-29 04:00:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 91.2 |
| 5722ad2c-6242-3f5d-ba4d-e3df5cfbbd8b | -23.20376 | -46.99052 | 2026-08-29 04:00:00 | NOAA-21 | JUNDIAÍ | SÃO PAULO | Brasil | 3525904 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.2 |
| 536ef9ba-754d-382f-ae2d-e28cadc79d85 | -19.28409 | -49.51746 | 2026-08-29 04:00:00 | NOAA-21 | ITUIUTABA | MINAS GERAIS | Brasil | 3134202 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 61250087-fd64-39e4-a08a-e84296f7ae9b | -21.41425 | -45.11121 | 2026-08-29 04:00:00 | NOAA-21 | CARMO DA CACHOEIRA | MINAS GERAIS | Brasil | 3113909 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.9 |
| 722d97ce-9aff-3134-b7a1-1f5ce8a94f8b | -23.66683 | -47.45811 | 2026-08-29 04:00:00 | NOAA-21 | PIEDADE | SÃO PAULO | Brasil | 3537800 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| c32b6e78-3e72-3d77-8ce4-1d5e2f82e83d | -22.26143 | -47.52174 | 2026-08-29 04:00:00 | NOAA-21 | RIO CLARO | SÃO PAULO | Brasil | 3543907 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 2ab85d3f-65ba-36a1-bfe8-a4910a389755 | -22.56722 | -44.85705 | 2026-08-29 04:00:00 | NOAA-21 | LAVRINHAS | SÃO PAULO | Brasil | 3526605 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 871ed787-4de4-34fa-a23a-0c4690ae1e9b | -20.2301 | -47.39618 | 2026-08-29 04:00:00 | NOAA-21 | PEDREGULHO | SÃO PAULO | Brasil | 3537008 | 35 | 33 | nan | nan | nan | Cerrado | 7.8 |
| ca2441c7-8b61-3f8a-8650-982acf2fa514 | -22.43466 | -49.76477 | 2026-08-29 04:00:00 | NOAA-21 | ALVINLÂNDIA | SÃO PAULO | Brasil | 3501509 | 35 | 33 | nan | nan | nan | Mata Atlântica | 5.4 |
| dbde19c1-d3f6-3776-8169-c0afec100ac4 | -20.23999 | -47.36602 | 2026-08-29 04:00:00 | NOAA-21 | PEDREGULHO | SÃO PAULO | Brasil | 3537008 | 35 | 33 | nan | nan | nan | Cerrado | 1.7 |
| f8b864a8-f38e-3d4d-99b6-70040a5db61f | -20.23085 | -47.39221 | 2026-08-29 04:00:00 | NOAA-21 | PEDREGULHO | SÃO PAULO | Brasil | 3537008 | 35 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 04060f5a-3b73-3779-86d0-a00ba2a95b87 | -23.18371 | -49.16016 | 2026-08-29 04:00:00 | NOAA-21 | CERQUEIRA CÉSAR | SÃO PAULO | Brasil | 3511409 | 35 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e6447c24-64ab-3f33-bd70-68e3ab608630 | -22.56373 | -44.8564 | 2026-08-29 04:00:00 | NOAA-21 | LAVRINHAS | SÃO PAULO | Brasil | 3526605 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 2e61a17b-d332-364c-9e71-b7e7db2f62dc | -23.20096 | -46.8621 | 2026-08-29 04:00:00 | NOAA-21 | JUNDIAÍ | SÃO PAULO | Brasil | 3525904 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| f565a7e4-51d2-3f99-9804-d7cc1778b854 | -23.50864 | -46.94754 | 2026-08-29 04:00:00 | NOAA-21 | ITAPEVI | SÃO PAULO | Brasil | 3522505 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 1c47f34f-129a-35e5-87bf-042756361144 | -19.28934 | -49.51607 | 2026-08-29 04:00:00 | NOAA-21 | ITUIUTABA | MINAS GERAIS | Brasil | 3134202 | 31 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 89493668-9eb5-38ce-a26e-0ebde607ea04 | -23.07818 | -48.62061 | 2026-08-29 04:00:00 | NOAA-21 | ITATINGA | SÃO PAULO | Brasil | 3523503 | 35 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 6b7b7bfe-f29e-377e-abac-cf7acb8c7248 | -20.95704 | -44.3465 | 2026-08-29 04:00:00 | NOAA-21 | RITÁPOLIS | MINAS GERAIS | Brasil | 3156106 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 6597d14d-f945-316c-a06d-c3728aa78c52 | -23.16284 | -49.23764 | 2026-08-29 04:00:00 | NOAA-21 | CERQUEIRA CÉSAR | SÃO PAULO | Brasil | 3511409 | 35 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 562d88a4-ce4c-3ab2-89a2-76442d17610b | -23.19719 | -46.86124 | 2026-08-29 04:00:00 | NOAA-21 | JUNDIAÍ | SÃO PAULO | Brasil | 3525904 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| fec73368-5e59-3b61-bad1-691a452d8f6a | -23.50879 | -46.94972 | 2026-08-29 04:00:00 | NOAA-21 | ITAPEVI | SÃO PAULO | Brasil | 3522505 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| edb40f6a-7179-3a7d-b913-b231943601e0 | -23.23485 | -49.3565 | 2026-08-29 04:00:00 | NOAA-21 | PIRAJU | SÃO PAULO | Brasil | 3538808 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.9 |
| 66338906-2c89-3729-83d8-0d71376813c9 | -21.71302 | -47.14537 | 2026-08-29 04:00:00 | NOAA-21 | CASA BRANCA | SÃO PAULO | Brasil | 3510807 | 35 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 79190c1c-8d92-3cc6-8e54-4f6120badd7e | -19.96574 | -44.7186 | 2026-08-29 04:00:00 | NOAA-21 | IGARATINGA | MINAS GERAIS | Brasil | 3130200 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 75bbab92-e3be-3cd9-bdc3-a672295617bf | -20.27395 | -45.55768 | 2026-08-29 04:00:00 | NOAA-21 | ARCOS | MINAS GERAIS | Brasil | 3104205 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| af7b341a-2b6f-3651-8861-29d47d4d45af | -21.71263 | -47.14245 | 2026-08-29 04:00:00 | NOAA-21 | CASA BRANCA | SÃO PAULO | Brasil | 3510807 | 35 | 33 | nan | nan | nan | Cerrado | 3.0 |
| b98c0da9-8925-33fb-b2d2-a7f994209348 | -23.18756 | -49.15818 | 2026-08-29 04:00:00 | NOAA-21 | CERQUEIRA CÉSAR | SÃO PAULO | Brasil | 3511409 | 35 | 33 | nan | nan | nan | Cerrado | 0.2 |
| 8d1edc2b-ff87-3a92-b2c8-d9ded0b9ed59 | -20.38594 | -47.41291 | 2026-08-29 04:00:00 | NOAA-21 | CRISTAIS PAULISTA | SÃO PAULO | Brasil | 3513207 | 35 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 19794604-5db9-3976-b7b4-0105a303cbec | -20.47355 | -48.78351 | 2026-08-29 04:00:00 | NOAA-21 | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| a37f1437-fe48-3775-b5cc-bf6a7d79dea0 | -23.15591 | -48.66996 | 2026-08-29 04:00:00 | NOAA-21 | ITATINGA | SÃO PAULO | Brasil | 3523503 | 35 | 33 | nan | nan | nan | Cerrado | 18.4 |
| cc84716f-d0bc-3707-bf5a-e18072a4c0eb | -19.2709 | -49.50895 | 2026-08-29 04:00:00 | NOAA-21 | ITUIUTABA | MINAS GERAIS | Brasil | 3134202 | 31 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 7f402fdb-5e5a-3733-afa3-790d2c93be88 | -19.27934 | -49.51641 | 2026-08-29 04:00:00 | NOAA-21 | ITUIUTABA | MINAS GERAIS | Brasil | 3134202 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| b6319a96-b628-3416-bd9b-ec52c8c4b11d | -22.31452 | -51.88871 | 2026-08-29 04:00:00 | NOAA-21 | MIRANTE DO PARANAPANEMA | SÃO PAULO | Brasil | 3530201 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| b147d822-b0f5-390b-809f-ac3fd94496f2 | -22.25674 | -47.52468 | 2026-08-29 04:00:00 | NOAA-21 | RIO CLARO | SÃO PAULO | Brasil | 3543907 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| 814654bc-ecd6-31eb-b43b-90974fe6b6c3 | -22.98403 | -45.51976 | 2026-08-29 04:00:00 | NOAA-21 | TREMEMBÉ | SÃO PAULO | Brasil | 3554805 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| c755630a-807e-357f-8c24-5fc7e41baed3 | -23.15176 | -48.66879 | 2026-08-29 04:00:00 | NOAA-21 | ITATINGA | SÃO PAULO | Brasil | 3523503 | 35 | 33 | nan | nan | nan | Cerrado | 18.4 |
| 430692ab-ad1c-3021-b793-782796b50976 | -19.28297 | -49.52313 | 2026-08-29 04:00:00 | NOAA-21 | ITUIUTABA | MINAS GERAIS | Brasil | 3134202 | 31 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 46cc3c14-4490-3e31-b48f-120a8c551217 | -21.38514 | -45.6852 | 2026-08-29 04:00:00 | NOAA-21 | TRÊS PONTAS | MINAS GERAIS | Brasil | 3169406 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 757da0e7-37c4-3927-9098-d999446e4747 | -22.26071 | -47.52555 | 2026-08-29 04:00:00 | NOAA-21 | RIO CLARO | SÃO PAULO | Brasil | 3543907 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| d3aa5723-88b9-3329-be9a-494664aba992 | -20.22935 | -47.40022 | 2026-08-29 04:00:00 | NOAA-21 | PEDREGULHO | SÃO PAULO | Brasil | 3537008 | 35 | 33 | nan | nan | nan | Cerrado | 5.3 |
| d525a18f-2260-3f24-b3da-cf93cf3183b2 | -23.18327 | -49.15708 | 2026-08-29 04:00:00 | NOAA-21 | CERQUEIRA CÉSAR | SÃO PAULO | Brasil | 3511409 | 35 | 33 | nan | nan | nan | Cerrado | 0.2 |
| 3ed3d162-4ed4-3239-8808-7fd058a4fd7f | -21.38264 | -45.33556 | 2026-08-29 04:00:00 | NOAA-21 | TRÊS PONTAS | MINAS GERAIS | Brasil | 3169406 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| e05c053b-4358-3857-85f8-4807c09959f4 | -23.66091 | -47.46805 | 2026-08-29 04:00:00 | NOAA-21 | PIEDADE | SÃO PAULO | Brasil | 3537800 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 806aa5d9-7a36-3106-a91f-a2539c89ec90 | -19.28884 | -49.51855 | 2026-08-29 04:00:00 | NOAA-21 | ITUIUTABA | MINAS GERAIS | Brasil | 3134202 | 31 | 33 | nan | nan | nan | Cerrado | 5.8 |
| f8f28747-faca-3204-b0f4-23bece7526ca | -22.45936 | -48.15792 | 2026-08-29 04:00:00 | NOAA-21 | TORRINHA | SÃO PAULO | Brasil | 3554706 | 35 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 665e4d42-24e1-31d8-a7c7-4722e34e2dda | -23.58221 | -47.28431 | 2026-08-29 04:00:00 | NOAA-21 | ALUMÍNIO | SÃO PAULO | Brasil | 3501152 | 35 | 33 | nan | nan | nan | Mata Atlântica | 7.8 |
| 90005fbd-c22e-3054-af63-ba92a71e1749 | -23.20078 | -46.85909 | 2026-08-29 04:00:00 | NOAA-21 | JUNDIAÍ | SÃO PAULO | Brasil | 3525904 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 2ffaa3db-89a9-3d3e-8512-d68d4c449f15 | -23.23046 | -49.35563 | 2026-08-29 04:00:00 | NOAA-21 | PIRAJU | SÃO PAULO | Brasil | 3538808 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| 435cea79-2985-3095-8cb3-6b5e89e4ab89 | -23.11703 | -46.91199 | 2026-08-29 04:00:00 | NOAA-21 | JUNDIAÍ | SÃO PAULO | Brasil | 3525904 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 390e8809-084f-3264-bb23-dfd7797ee7fb | -23.0778 | -48.62166 | 2026-08-29 04:00:00 | NOAA-21 | ITATINGA | SÃO PAULO | Brasil | 3523503 | 35 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 6328f393-b2c3-3d9a-bc86-ffc843d5a9c6 | -23.15096 | -48.6729 | 2026-08-29 04:00:00 | NOAA-21 | ITATINGA | SÃO PAULO | Brasil | 3523503 | 35 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 1db0e091-329f-3bae-ad71-928cc4a84288 | -19.26983 | -49.51427 | 2026-08-29 04:00:00 | NOAA-21 | ITUIUTABA | MINAS GERAIS | Brasil | 3134202 | 31 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 2441bd71-8213-3170-b1ef-409c35936c09 | -23.23576 | -49.35197 | 2026-08-29 04:00:00 | NOAA-21 | PIRAJU | SÃO PAULO | Brasil | 3538808 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.9 |
| c1caadf7-5dd3-3236-99ba-7d10373b9302 | -19.28817 | -49.52175 | 2026-08-29 04:00:00 | NOAA-21 | ITUIUTABA | MINAS GERAIS | Brasil | 3134202 | 31 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 41ace46e-a9ae-32be-b390-20b87d84b14e | -22.25746 | -47.52086 | 2026-08-29 04:00:00 | NOAA-21 | RIO CLARO | SÃO PAULO | Brasil | 3543907 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.1 |
| 8c434450-d85b-3782-a4e9-b2e6cb5058f5 | -19.28342 | -49.52067 | 2026-08-29 04:00:00 | NOAA-21 | ITUIUTABA | MINAS GERAIS | Brasil | 3134202 | 31 | 33 | nan | nan | nan | Cerrado | 4.0 |
| bb2f39e8-26fe-3f05-ac8c-be6be5b543f2 | -19.27459 | -49.51532 | 2026-08-29 04:00:00 | NOAA-21 | ITUIUTABA | MINAS GERAIS | Brasil | 3134202 | 31 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 0904369e-6521-3ec2-9fd9-b2a968a40f62 | -23.23136 | -49.35114 | 2026-08-29 04:00:00 | NOAA-21 | PIRAJU | SÃO PAULO | Brasil | 3538808 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| 13fc2cc4-2e44-332e-87e7-789c8f1e8faf | -21.96972 | -48.18139 | 2026-08-29 04:00:00 | NOAA-21 | RIBEIRÃO BONITO | SÃO PAULO | Brasil | 3542909 | 35 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 16873432-be75-318f-8035-bee6f9ab2081 | -23.32244 | -46.77332 | 2026-08-29 04:00:00 | NOAA-21 | FRANCO DA ROCHA | SÃO PAULO | Brasil | 3516408 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.8 |
| 568e2313-e794-3d7d-a658-4c45443b423c | -19.27868 | -49.51957 | 2026-08-29 04:00:00 | NOAA-21 | ITUIUTABA | MINAS GERAIS | Brasil | 3134202 | 31 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 0fc3f407-13c3-3975-bf27-e93833c8a477 | -21.38187 | -45.33996 | 2026-08-29 04:00:00 | NOAA-21 | TRÊS PONTAS | MINAS GERAIS | Brasil | 3169406 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |


[Clique aqui para ver as próximas entradas](README27.md)
