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

## Dados Diários - Página 69

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 6a900025-713a-39d9-ad0c-65faa7505b06 | -5.9682 | -51.94838 | 2026-08-21 05:23:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 2ce4efc5-0aab-3e34-ada3-dae586e125fb | -6.71426 | -59.08801 | 2026-08-21 05:23:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e319bb78-3fa6-317e-a021-a8910b5c553e | -8.89966 | -60.54899 | 2026-08-21 05:23:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 8.2 |
| 22bd04e2-823a-33b5-a182-9752cce6e69d | -5.80816 | -55.7256 | 2026-08-21 05:23:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 8ecc3d64-e194-32fb-8788-ecbecd02276a | -7.37899 | -45.82046 | 2026-08-21 05:23:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 320e7369-7f86-3902-8b5a-79e415c2c709 | -14.09877 | -58.8152 | 2026-08-21 05:23:00 | NPP-375D | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| fa319e26-60bd-3cf1-b0f4-b1e03de43ddf | -7.60411 | -60.82879 | 2026-08-21 05:23:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| ae9bee0f-8a1b-3d1f-a8fa-b638edc85ed6 | -8.57345 | -54.66909 | 2026-08-21 05:23:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6876780f-a571-349d-bd85-826ffd1ca1da | -8.38442 | -62.70284 | 2026-08-21 05:23:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 11.3 |
| f65e520b-590c-32dc-888f-ce454c1ba860 | -6.93836 | -52.77578 | 2026-08-21 05:23:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 01984053-7bf2-3e5e-9d60-644880a46e13 | -15.16868 | -48.77989 | 2026-08-21 05:23:00 | NPP-375D | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 8792b79f-1f47-38df-927d-a4aa767975fd | -6.38703 | -54.9386 | 2026-08-21 05:23:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| fc31dca7-f646-3830-a6ae-6ac92492ebfd | -9.44227 | -51.63057 | 2026-08-21 05:23:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| dabb05fe-62f8-3565-9f60-f3f23849aa80 | -5.99676 | -57.83752 | 2026-08-21 05:23:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 4441d473-64ab-3504-84d4-f837c86342a7 | -6.61548 | -56.34448 | 2026-08-21 05:23:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a6c2a638-595c-34c6-9edc-aa882d370349 | -6.12049 | -59.90232 | 2026-08-21 05:23:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 1d5abc4f-9622-38b3-882e-826a8374a46b | -6.85718 | -59.02538 | 2026-08-21 05:23:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c2191446-8dbd-3af0-81e8-16825dcb1903 | -15.059 | -48.70806 | 2026-08-21 05:23:00 | NPP-375D | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 5.7 |
| e846c7cc-2eed-3427-8094-f2f7887f2c01 | -15.00601 | -52.6892 | 2026-08-21 05:23:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 5ffadec1-064f-3853-81b2-ed945477586e | -4.01706 | -48.06624 | 2026-08-21 05:23:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f5e78fd6-2314-308a-baa8-6e4ed4a7ae94 | -8.53647 | -54.86674 | 2026-08-21 05:23:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c9953ae0-d178-3d7d-a113-826ec7059959 | -2.70552 | -54.7599 | 2026-08-21 05:23:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 062fd91c-3ca3-30b5-8a74-c3ee66324398 | -9.39667 | -55.98437 | 2026-08-21 05:23:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 84d59b56-db92-3edf-bbd0-dd0281830be6 | -6.86991 | -59.44408 | 2026-08-21 05:23:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 2625b40d-de49-3ffb-995f-c772897b2624 | -6.14693 | -57.85419 | 2026-08-21 05:23:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1d2780da-47aa-39a3-bee3-8a115709cc4a | -9.54745 | -56.79532 | 2026-08-21 05:23:00 | NPP-375D | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3d3164b5-4eee-3c9a-827c-16758ca9005d | -6.20446 | -57.77081 | 2026-08-21 05:23:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 1bfbfa27-7190-31ba-9fac-e8ae2fc78fb9 | -3.2005 | -61.28179 | 2026-08-21 05:23:00 | NPP-375D | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| a9e449b4-3493-3ea7-ab2b-f817878f05b9 | -5.86842 | -57.66793 | 2026-08-21 05:23:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| af52f031-6e7c-3bfd-8a51-f0f73a125a4c | -6.33127 | -46.52235 | 2026-08-21 05:23:00 | NPP-375D | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 8184cb94-c8de-3c3a-b01b-37e8ea9ee957 | -8.53814 | -54.78106 | 2026-08-21 05:23:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 1d3237a6-8427-3aba-b272-25df6dda8d26 | -8.05191 | -61.71666 | 2026-08-21 05:23:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| aeb8cb64-e428-3856-bc44-40d9334000a2 | -9.05455 | -57.07232 | 2026-08-21 05:23:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 001002cd-9a49-3810-9b8f-e284a23aef9f | -8.38925 | -62.69841 | 2026-08-21 05:23:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 0cf4a973-47fe-358c-a646-c2f42b2dfbf1 | -10.72376 | -44.78197 | 2026-08-21 05:23:00 | NPP-375D | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| fd3ddd6d-80c9-3465-b7c1-11fc3438dbe1 | -7.44751 | -59.9995 | 2026-08-21 05:23:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ed492556-16dd-3dd8-8806-70e453eca3a1 | -11.1678 | -54.01144 | 2026-08-21 05:25:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 8.6 |
| 79c7759a-ec61-36b2-8135-d301014b129a | -10.39096 | -61.20856 | 2026-08-21 05:25:00 | NPP-375D | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 95b7dce8-410f-31b5-bed7-8cf4eda522de | -11.21709 | -54.00315 | 2026-08-21 05:25:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| a999e330-a168-3550-8598-100b5b45c741 | -17.95727 | -49.37841 | 2026-08-21 05:25:00 | NPP-375D | GOIATUBA | GOIÁS | Brasil | 5209101 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ef51c45b-1700-39f7-aa70-e12ae21866aa | -12.74924 | -48.47694 | 2026-08-21 05:25:00 | NPP-375D | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 7be9a424-76ef-3cda-b48e-b2e3e2fdffb0 | -9.41339 | -60.43554 | 2026-08-21 05:25:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| fb5eac07-aa17-3624-bd2a-5f57ca3bfc5c | -11.17492 | -54.01761 | 2026-08-21 05:25:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 7659d975-2917-3eff-8683-50a984b39fe0 | -10.76159 | -50.31173 | 2026-08-21 05:25:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 89032ffe-25be-3db5-bde5-5a7f968b5da3 | -10.25139 | -54.3625 | 2026-08-21 05:25:00 | NPP-375D | MATUPÁ | MATO GROSSO | Brasil | 5105606 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 5c2b2e1c-5c12-3157-a108-ac438d729b62 | -9.2095 | -60.77205 | 2026-08-21 05:25:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 1aa643f8-bd73-393c-9e0c-fb60cd9c2272 | -9.39071 | -60.59504 | 2026-08-21 05:25:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a2d6bd4c-630e-3161-9539-ffb702ac206d | -12.81016 | -48.40954 | 2026-08-21 05:25:00 | NPP-375D | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| e3594038-8854-3479-a0e4-6964489c640e | -19.7251 | -57.96508 | 2026-08-21 05:25:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 20.1 |
| 86109f2b-85ff-31e0-a2be-98ed033e2a3b | -10.77095 | -50.31342 | 2026-08-21 05:25:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 6.7 |
| aa7fd127-9251-33f3-8f96-dc1b306658b8 | -9.3977 | -60.59624 | 2026-08-21 05:25:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3c02cf89-abb2-3829-814e-e0b5dc02cc0a | -11.20493 | -55.05602 | 2026-08-21 05:25:00 | NPP-375D | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b23d63f7-29c8-3a32-b186-18bf2eae00bf | -17.9581 | -49.3706 | 2026-08-21 05:25:00 | NPP-375D | GOIATUBA | GOIÁS | Brasil | 5209101 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 76e8e3bc-536a-3120-8ae8-316b55fab45f | -11.18203 | -54.02375 | 2026-08-21 05:25:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| a44dbae7-0cdd-31b5-bf2b-afa1da0a04ac | -9.40424 | -60.42612 | 2026-08-21 05:25:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 7.6 |
| dbc3cdf1-4136-3344-8b60-f12292deb53e | -12.76189 | -48.46982 | 2026-08-21 05:25:00 | NPP-375D | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| e238d7b3-d17a-3be7-9f2d-148cfb087112 | -9.42003 | -60.41686 | 2026-08-21 05:25:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| f718fc78-caaf-3566-99b1-5889b22c4a6c | -11.18815 | -54.00922 | 2026-08-21 05:25:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 13e67916-4603-3134-a159-1807c0034427 | -19.66741 | -46.04958 | 2026-08-21 05:25:00 | NPP-375D | CÓRREGO DANTA | MINAS GERAIS | Brasil | 3119807 | 31 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 086932c1-5f3a-3cf1-a02a-a006223948ee | -9.19919 | -60.87717 | 2026-08-21 05:25:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6289c940-fc70-342d-9fa7-bd3d37432519 | -12.71976 | -48.47709 | 2026-08-21 05:25:00 | NPP-375D | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| f9909b61-0a4d-3a73-8f6a-39d797a368cd | -20.26259 | -46.7602 | 2026-08-21 05:25:00 | NPP-375D | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 4a5e81e0-9e03-3183-9f55-c388b96c7415 | -10.76169 | -50.30626 | 2026-08-21 05:25:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 1901802c-ab14-3fd9-a7a5-81481dfab0fe | -10.76738 | -50.30666 | 2026-08-21 05:25:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 3e08a378-c694-3048-a8d9-21ba5efc25ff | -9.11875 | -61.60243 | 2026-08-21 05:25:00 | NPP-375D | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 48f5dc79-19e0-31c0-8f61-dce97f54f8a4 | -9.41276 | -60.43939 | 2026-08-21 05:25:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c907042e-46d8-35a9-835c-49f51efde4a7 | -10.84414 | -57.52412 | 2026-08-21 05:25:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7bc38b68-b9ac-3af5-9c75-7444fb117a64 | -9.40951 | -60.54617 | 2026-08-21 05:25:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 23fe1224-5c1f-3ce8-ace4-e5c8e5cb612a | -11.21326 | -53.99905 | 2026-08-21 05:25:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 78b456b7-c8d5-337f-9681-a0d2ecabfc37 | -11.20924 | -54.00198 | 2026-08-21 05:25:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 7e481077-9856-3045-94e9-ca1ba9726818 | -9.42413 | -60.4136 | 2026-08-21 05:25:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| dfca3b1f-9d09-3f67-90ed-9e4831d2993b | -9.41025 | -60.4113 | 2026-08-21 05:25:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 41.1 |
| 884cd6cf-4d0c-3311-bb22-756b9b08c908 | -11.17811 | -54.02318 | 2026-08-21 05:25:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| e4672c3f-33c0-3435-8956-49f6605f021b | -9.40615 | -60.41456 | 2026-08-21 05:25:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 78.9 |
| e3fd53a9-35e0-3e1a-9590-060d7d952df5 | -12.84863 | -48.43488 | 2026-08-21 05:25:00 | NPP-375D | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 61a44f56-7a0b-36ad-85ae-e47836883c3e | -9.40962 | -60.41514 | 2026-08-21 05:25:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 35.8 |
| 20171d8d-16f7-3949-b2c4-8c44ffd913fd | -9.39998 | -60.56055 | 2026-08-21 05:25:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 9ec6aa8f-7f64-35df-86cc-d8cad41eb80a | -10.79625 | -50.27577 | 2026-08-21 05:25:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d14f7030-c025-358e-b279-28f18fad1977 | -11.22466 | -54.86773 | 2026-08-21 05:25:00 | NPP-375D | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 136a5df9-f8bf-3faa-aad4-e06b00cc60be | -10.63793 | -51.60424 | 2026-08-21 05:25:00 | NPP-375D | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 2a53697f-2da1-3c5f-ace3-8a2b63bb028e | -12.72554 | -48.47802 | 2026-08-21 05:25:00 | NPP-375D | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 5.5 |
| e26f903d-cc63-3bda-ad88-cc8ac7fbe190 | -10.24312 | -54.36606 | 2026-08-21 05:25:00 | NPP-375D | MATUPÁ | MATO GROSSO | Brasil | 5105606 | 51 | 33 | nan | nan | nan | Amazônia | 5.5 |
| e0a5aafd-9959-3557-81e8-5e865b354cc3 | -10.7667 | -50.30695 | 2026-08-21 05:25:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 3fa756c0-1566-36cf-a323-06a0f2ad7429 | -9.41245 | -60.41956 | 2026-08-21 05:25:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 35.8 |
| f10c81de-c017-34c4-8d65-dcafdae679c8 | -12.74335 | -48.47688 | 2026-08-21 05:25:00 | NPP-375D | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| b02e81e7-fbe0-3d75-ac53-bbe1ec5f2711 | -9.12343 | -60.92387 | 2026-08-21 05:25:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 698e9b09-16cf-3179-97b6-d52ace2bc4d1 | -9.3992 | -60.41341 | 2026-08-21 05:25:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| a5688e02-0ea9-33c6-aa28-8753350a0607 | -11.68599 | -54.57306 | 2026-08-21 05:25:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ee629ec3-93a6-3219-8e89-3942cca9bffa | -11.17564 | -54.01257 | 2026-08-21 05:25:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 6.0 |
| f1b980c1-ad8c-346b-a3e9-ca34ce65cd8d | -12.80334 | -48.42072 | 2026-08-21 05:25:00 | NPP-375D | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| ffe40f08-b2ed-37fb-a3d2-2b52aa9f6614 | -22.19168 | -48.74481 | 2026-08-21 05:25:00 | NPP-375D | BORACÉIA | SÃO PAULO | Brasil | 3507308 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 6ce20cd6-7b3d-3e4c-8c2e-12caeb3300f8 | -9.40062 | -60.55666 | 2026-08-21 05:25:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 31b2ece8-0a90-35dd-a6a9-bf9e96cfe474 | -11.16885 | -54.03195 | 2026-08-21 05:25:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 1abc9c0c-9041-37a5-8a09-9aa2d47b2546 | -9.40678 | -60.41072 | 2026-08-21 05:25:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 76a95b88-20e8-3ed0-9164-20075ab0fc01 | -10.34361 | -57.57349 | 2026-08-21 05:25:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 94683d9b-5e7e-3648-af22-2dd3f0c6de9c | -11.1774 | -54.02814 | 2026-08-21 05:25:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 0d00ee28-3973-3099-b65d-3fc823add95c | -10.81759 | -50.99912 | 2026-08-21 05:25:00 | NPP-375D | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 8fecfef0-6250-3385-963d-7402fb7c586f | -9.20663 | -60.7675 | 2026-08-21 05:25:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 5a42bce1-acad-3faf-8de4-e04127987c25 | -11.8151 | -56.59966 | 2026-08-21 05:25:00 | NPP-375D | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| c60017d3-1ff1-3aaa-8cf8-94be6ad0ada4 | -12.79884 | -48.40907 | 2026-08-21 05:25:00 | NPP-375D | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |


[Clique aqui para ver as próximas entradas](README70.md)
