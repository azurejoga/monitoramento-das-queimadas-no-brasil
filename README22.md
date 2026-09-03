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

## Dados Diários - Página 22

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 372e884c-6798-3003-adb7-19bcf06ab917 | -20.9676 | -47.4127 | 2026-09-03 04:06:00 | NOAA-21 | ALTINÓPOLIS | SÃO PAULO | Brasil | 3501004 | 35 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 43cf9f71-fadc-3f19-8854-47c70d330a5e | -18.16692 | -51.7948 | 2026-09-03 04:06:00 | NOAA-21 | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 8076e096-19fc-33ed-9311-992352c64302 | -18.53144 | -46.82259 | 2026-09-03 04:06:00 | NOAA-21 | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 10ed1788-498a-3a53-9915-5f7759a32cf1 | -18.77978 | -48.91697 | 2026-09-03 04:06:00 | NOAA-21 | MONTE ALEGRE DE MINAS | MINAS GERAIS | Brasil | 3142809 | 31 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 76ebc6d8-886d-322f-ac9c-b0a0ed640d27 | -18.16461 | -51.7953 | 2026-09-03 04:06:00 | NOAA-21 | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 4.1 |
| bcbc8311-be97-3fc0-82a0-84449eb95663 | -19.09489 | -48.49138 | 2026-09-03 04:06:00 | NOAA-21 | UBERLÂNDIA | MINAS GERAIS | Brasil | 3170206 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a86a5b6c-5cd9-3b3a-ab88-f45f1d325348 | -23.51309 | -46.47606 | 2026-09-03 04:06:00 | NOAA-21 | SÃO PAULO | SÃO PAULO | Brasil | 3550308 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.3 |
| e9d7b166-5dc2-3907-b1db-3f187b53bba9 | -23.04886 | -46.5751 | 2026-09-03 04:06:00 | NOAA-21 | ATIBAIA | SÃO PAULO | Brasil | 3504107 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 94767cef-98b4-308c-895a-2347ce61d0d2 | -18.16716 | -51.80853 | 2026-09-03 04:06:00 | NOAA-21 | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 93f910fc-cbf9-3144-b8a9-afdf8a71361d | -18.16385 | -51.81004 | 2026-09-03 04:06:00 | NOAA-21 | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 28710679-8568-31bc-9256-703c496059b7 | -18.64766 | -47.28693 | 2026-09-03 04:06:00 | NOAA-21 | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 5a5085b3-8b36-3e6e-8f63-12a3992ea862 | -18.16571 | -51.80083 | 2026-09-03 04:06:00 | NOAA-21 | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 0ab34092-64f3-326e-8cdd-790f23205502 | -18.16968 | -51.7964 | 2026-09-03 04:06:00 | NOAA-21 | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 4.1 |
| db73415b-9812-3b4e-9fe3-44e524f8342c | -18.78242 | -48.92596 | 2026-09-03 04:06:00 | NOAA-21 | MONTE ALEGRE DE MINAS | MINAS GERAIS | Brasil | 3142809 | 31 | 33 | nan | nan | nan | Cerrado | 6.3 |
| d7619270-98f4-3034-999d-4e65d82a863b | -17.08418 | -56.84455 | 2026-09-03 04:06:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 5.0 |
| ceeba964-85dc-3a30-baad-1147e7954a36 | -22.42902 | -49.76729 | 2026-09-03 04:06:00 | NOAA-21 | ALVINLÂNDIA | SÃO PAULO | Brasil | 3501509 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.9 |
| 435fd75f-d016-318e-8c94-43f0073d27a0 | -18.78395 | -48.91784 | 2026-09-03 04:06:00 | NOAA-21 | MONTE ALEGRE DE MINAS | MINAS GERAIS | Brasil | 3142809 | 31 | 33 | nan | nan | nan | Cerrado | 22.2 |
| 456f3cad-9569-3a42-b77b-2e7d0e8f46fb | -18.77823 | -48.92513 | 2026-09-03 04:06:00 | NOAA-21 | MONTE ALEGRE DE MINAS | MINAS GERAIS | Brasil | 3142809 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 9f338625-250a-39a4-b1cf-1369d3e9ed39 | -18.16651 | -51.81165 | 2026-09-03 04:06:00 | NOAA-21 | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| a03230b8-7107-33df-bbb2-cecdc03fd7e7 | -18.14724 | -51.81355 | 2026-09-03 04:06:00 | NOAA-21 | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 90c9700a-deb8-3efc-a288-7975c3d2925b | -18.16905 | -51.7994 | 2026-09-03 04:06:00 | NOAA-21 | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 9.1 |
| fadd0c42-832e-368f-a5e7-9a9e0cf5b7c7 | -18.78131 | -48.90887 | 2026-09-03 04:06:00 | NOAA-21 | MONTE ALEGRE DE MINAS | MINAS GERAIS | Brasil | 3142809 | 31 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 04ed6df3-aa78-37ac-a7f0-3e0fe507ca22 | -18.16843 | -51.80239 | 2026-09-03 04:06:00 | NOAA-21 | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 9.1 |
| 6c79ad1a-60a4-3bff-89da-7a1df59043e3 | -20.40283 | -47.15432 | 2026-09-03 04:06:00 | NOAA-21 | IBIRACI | MINAS GERAIS | Brasil | 3129707 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 8d2c4579-3a71-3ec2-93e6-013e4a4fa6de | -18.77483 | -48.92021 | 2026-09-03 04:06:00 | NOAA-21 | MONTE ALEGRE DE MINAS | MINAS GERAIS | Brasil | 3142809 | 31 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 19fa3314-9f17-3d92-9ee4-4bb8283006ee | -18.51621 | -48.23687 | 2026-09-03 04:06:00 | NOAA-21 | ARAGUARI | MINAS GERAIS | Brasil | 3103504 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 90aae85f-49fe-3946-9a78-bbf830774a95 | -18.83872 | -46.44207 | 2026-09-03 04:06:00 | NOAA-21 | LAGOA FORMOSA | MINAS GERAIS | Brasil | 3137502 | 31 | 33 | nan | nan | nan | Cerrado | 3.8 |
| ceab4a30-ab67-3709-a31a-fa038a4a0b83 | -17.0826 | -56.85151 | 2026-09-03 04:06:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.5 |
| ba46f1b8-667c-34cc-8177-8cc58de2609e | -20.96545 | -47.41471 | 2026-09-03 04:06:00 | NOAA-21 | ALTINÓPOLIS | SÃO PAULO | Brasil | 3501004 | 35 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 4548051e-135c-313e-a47d-f6155718218b | -22.75087 | -41.99667 | 2026-09-03 04:06:00 | NOAA-21 | CABO FRIO | RIO DE JANEIRO | Brasil | 3300704 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 18af1a27-6d42-3756-87d2-97cbfccc9ae1 | -21.90013 | -55.3712 | 2026-09-03 04:06:00 | NOAA-21 | DOURADOS | MATO GROSSO DO SUL | Brasil | 5003702 | 50 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 8ca6513f-4a6c-37e6-8ba6-93ae74e54e6a | -18.59204 | -48.23626 | 2026-09-03 04:06:00 | NOAA-21 | ARAGUARI | MINAS GERAIS | Brasil | 3103504 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 2afb7fb6-d71b-3fec-96fb-150cc96a7c79 | -18.16272 | -51.80437 | 2026-09-03 04:06:00 | NOAA-21 | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 4a24aa28-4eca-3ffe-b367-c08cc4264d91 | -18.54579 | -47.15888 | 2026-09-03 04:06:00 | NOAA-21 | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 0774cc85-bc5a-3e7b-aeed-7453683f80e1 | -18.78055 | -48.91289 | 2026-09-03 04:06:00 | NOAA-21 | MONTE ALEGRE DE MINAS | MINAS GERAIS | Brasil | 3142809 | 31 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 88808721-c3a2-3886-9091-349470e6f421 | -18.82918 | -47.60139 | 2026-09-03 04:06:00 | NOAA-21 | ROMARIA | MINAS GERAIS | Brasil | 3156403 | 31 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 9838665a-b2c8-35c8-a774-df5bb0c70061 | -18.7756 | -48.91614 | 2026-09-03 04:06:00 | NOAA-21 | MONTE ALEGRE DE MINAS | MINAS GERAIS | Brasil | 3142809 | 31 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 8cb74000-67a5-34fb-adb9-5e1a2881d56e | -18.82532 | -47.60064 | 2026-09-03 04:06:00 | NOAA-21 | ROMARIA | MINAS GERAIS | Brasil | 3156403 | 31 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 94daf583-f8fb-3f28-8f42-bb492c3bb23f | -18.74855 | -47.44255 | 2026-09-03 04:06:00 | NOAA-21 | MONTE CARMELO | MINAS GERAIS | Brasil | 3143104 | 31 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 2a81f302-52e3-308f-9681-b27c7b034437 | -17.08614 | -56.85975 | 2026-09-03 04:06:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.5 |
| 3730a930-6785-312f-9634-a4d6d82f1012 | -19.87369 | -45.14938 | 2026-09-03 04:06:00 | NOAA-21 | ARAÚJOS | MINAS GERAIS | Brasil | 3103900 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 6aa4ca23-1931-307d-8f8d-e35305f5631c | -18.15938 | -51.80593 | 2026-09-03 04:06:00 | NOAA-21 | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 6.1 |
| d2d5f6c7-90c2-3220-afc6-97900a150031 | -18.13708 | -51.81136 | 2026-09-03 04:06:00 | NOAA-21 | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 5.6 |
| f0a7b41a-9780-3791-bcae-1dc4242a87e5 | -18.14153 | -51.81556 | 2026-09-03 04:06:00 | NOAA-21 | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 8a89e53f-40b5-37b5-a06a-9fed51331d55 | -18.84938 | -47.14084 | 2026-09-03 04:06:00 | NOAA-21 | PATROCÍNIO | MINAS GERAIS | Brasil | 3148103 | 31 | 33 | nan | nan | nan | Cerrado | 2.9 |
| c9fd3165-de91-35c8-b3e4-1a7bdd4207b7 | -18.16001 | -51.80283 | 2026-09-03 04:06:00 | NOAA-21 | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 6.1 |
| e2548b52-2222-30e6-b757-35c21fdd6f1e | -18.1651 | -51.80385 | 2026-09-03 04:06:00 | NOAA-21 | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 248e99e4-f035-3251-bc8c-504253000ad6 | -17.08245 | -56.84423 | 2026-09-03 04:06:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.5 |
| 96558b99-1c6b-3cb8-a9f6-b63d5bda21a8 | -22.43313 | -49.76822 | 2026-09-03 04:06:00 | NOAA-21 | ALVINLÂNDIA | SÃO PAULO | Brasil | 3501509 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.9 |
| 81e4a36b-fbbf-3afa-a1b3-2c75197b438f | -19.19371 | -46.84433 | 2026-09-03 04:06:00 | NOAA-21 | SERRA DO SALITRE | MINAS GERAIS | Brasil | 3166808 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| babae794-2bff-371f-8a6b-e00d3f551909 | -19.35649 | -47.09356 | 2026-09-03 04:06:00 | NOAA-21 | PERDIZES | MINAS GERAIS | Brasil | 3149804 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 97c38402-b73c-3460-ba9b-b754c8b3b180 | -18.77636 | -48.91208 | 2026-09-03 04:06:00 | NOAA-21 | MONTE ALEGRE DE MINAS | MINAS GERAIS | Brasil | 3142809 | 31 | 33 | nan | nan | nan | Cerrado | 5.6 |
| aa3459d1-e547-38aa-bf33-33c092409e03 | -18.13644 | -51.81447 | 2026-09-03 04:06:00 | NOAA-21 | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 5.6 |
| eacfa592-448f-38b2-90a3-8ddb3b19b710 | -17.08777 | -56.85281 | 2026-09-03 04:06:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.5 |
| b70b869a-3e40-30d4-92e9-3f0816966986 | -17.08938 | -56.84593 | 2026-09-03 04:06:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.5 |
| 61fc6d73-e717-3b00-85ca-b9812c2d9d07 | -18.16398 | -51.79832 | 2026-09-03 04:06:00 | NOAA-21 | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 9.1 |
| 34038f62-8879-3f25-b265-bfabe9f9ac66 | -18.16142 | -51.8106 | 2026-09-03 04:06:00 | NOAA-21 | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 580dfd67-d8b1-3628-8ac9-e18c3882ea35 | -18.84158 | -46.44723 | 2026-09-03 04:06:00 | NOAA-21 | LAGOA FORMOSA | MINAS GERAIS | Brasil | 3137502 | 31 | 33 | nan | nan | nan | Cerrado | 4.8 |
| d69eb0eb-7d8e-3e46-956e-3eb0f542db3a | -18.65144 | -47.28774 | 2026-09-03 04:06:00 | NOAA-21 | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 3.0 |
| bf3b5829-b3e7-3bac-a8bf-7a7ae7de4e02 | -19.36021 | -47.0943 | 2026-09-03 04:06:00 | NOAA-21 | PERDIZES | MINAS GERAIS | Brasil | 3149804 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 0c4d2365-8506-3b5b-9cd0-05e6dea57cf0 | -18.84234 | -46.4428 | 2026-09-03 04:06:00 | NOAA-21 | LAGOA FORMOSA | MINAS GERAIS | Brasil | 3137502 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 204ea735-87cd-3d75-91a5-cd43092e31b5 | -20.87247 | -50.01058 | 2026-09-03 04:06:00 | NOAA-21 | MACAUBAL | SÃO PAULO | Brasil | 3528106 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| fa48af70-603f-352f-ae49-68299ce0115f | -29.71835 | -51.10262 | 2026-09-03 04:08:00 | NOAA-21 | NOVO HAMBURGO | RIO GRANDE DO SUL | Brasil | 4313409 | 43 | 33 | nan | nan | nan | Pampa | 0.8 |
| 56e14d6f-5a58-3993-822c-eb4485e6ef14 | -7.0232 | -62.9708 | 2026-09-03 04:10:00 | GOES-19 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 34.7 |
| 043a0567-f813-39b8-96ef-07680eaa0d6e | -3.2486 | -47.2438 | 2026-09-03 04:10:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 80.1 |
| c56750b8-1514-3852-9eac-29231cee0243 | -6.3236 | -56.0632 | 2026-09-03 04:10:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 26.1 |
| 21d73794-f3c2-31e1-836b-61bcfcdba832 | -6.3052 | -56.0442 | 2026-09-03 04:10:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 44.9 |
| d6a8c4d0-e2c3-3d38-817b-632ddacd8400 | -3.2485 | -47.2657 | 2026-09-03 04:10:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 67.4 |
| 0631ba1a-b7c5-30d2-9471-a882d4354bde | -9.06 | -65.7344 | 2026-09-03 04:10:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 51.7 |
| f0a1c87d-fcb8-3ac0-bdc3-e3de9a4c7077 | -9.0415 | -65.7349 | 2026-09-03 04:10:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 42.7 |
| f80c561c-0bed-3a1a-816a-9ba834ed1da9 | -6.6883 | -59.9436 | 2026-09-03 04:10:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 124.2 |
| a78223e1-acc2-346a-8316-0e15239b2083 | -6.3237 | -56.0434 | 2026-09-03 04:10:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 51.5 |
| 4addbf22-2e4e-3e51-84bf-cf203cf8ef4a | -9.0787 | -65.6964 | 2026-09-03 04:10:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 46.3 |
| b38d8b58-e1c3-3fc8-b638-a9b8de5df283 | -6.6357 | -59.4459 | 2026-09-03 04:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 66.2 |
| 9970cac3-ed85-3a71-bacf-e7ede78484ba | -6.6697 | -59.9635 | 2026-09-03 04:10:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 34.7 |
| 7fee557d-19ce-338c-9285-0c00d9b5ad1f | -6.6764 | -58.7686 | 2026-09-03 04:10:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 27.9 |
| 57d41344-ab1f-364e-aec4-d9eef6f571ab | -6.6882 | -59.9628 | 2026-09-03 04:10:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 61.4 |
| e6fbab20-c59a-3553-a60a-c4f49e744617 | -6.6698 | -59.9443 | 2026-09-03 04:10:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 61.9 |
| b979769d-439c-34d3-94d1-0035fb7df341 | -6.6541 | -59.4452 | 2026-09-03 04:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 52.0 |
| 916734bc-3323-3bce-882f-5805b23b34c6 | -9.0786 | -65.7338 | 2026-09-03 04:10:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 105.2 |
| b009b152-f4dd-36d6-af28-6c1469cf86d1 | -9.0787 | -65.7151 | 2026-09-03 04:10:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 283.1 |
| b3dd0ce8-fec0-3e94-9cae-6f1513e46983 | -6.7648 | -59.4408 | 2026-09-03 04:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 36.2 |
| f9ecd184-6b7d-3d06-ba25-796ab4ac9707 | -9.0601 | -65.7157 | 2026-09-03 04:10:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 99.3 |
| dd1fff50-0696-3007-a76a-f732d2f99c26 | -6.6357 | -59.4459 | 2026-09-03 04:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 52.7 |
| c57b5090-cf0b-3447-bcd0-c2381ef1604c | -6.6541 | -59.4452 | 2026-09-03 04:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 58.9 |
| d40d340c-3552-35cb-ab3a-d8aef637a4d9 | -9.0786 | -65.7338 | 2026-09-03 04:20:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 51.1 |
| 6dafc6ce-29e0-3b16-836d-e2f910019e9b | -9.0787 | -65.7151 | 2026-09-03 04:20:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 89.7 |
| 54e15dd8-b9e5-38b5-8d0b-1e5747d54f14 | -6.3052 | -56.0442 | 2026-09-03 04:20:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 45.1 |
| 7a0ec4db-869b-3b9e-bee8-6e60ae30d2c1 | -3.2486 | -47.2438 | 2026-09-03 04:20:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 121.0 |
| 10b240b5-37b3-3ed3-a3bc-79437601df1b | -7.566 | -61.343 | 2026-09-03 04:20:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 34.6 |
| b6f46041-5a77-3c36-af9c-9a851c55ae18 | -9.0601 | -65.7157 | 2026-09-03 04:20:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 55.0 |
| 115b6fc5-f7c6-3160-b62e-b9da5fa3237b | -6.6883 | -59.9436 | 2026-09-03 04:20:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 102.5 |
| 2fab5145-88ff-3f78-a02a-f0727cbf1626 | -6.6542 | -59.426 | 2026-09-03 04:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 32.3 |
| 272863a6-dd0e-3d4c-9a88-70f82bd1dcf8 | -6.6698 | -59.9443 | 2026-09-03 04:20:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 98.3 |
| ef91817e-da0c-35d1-9347-78be380ab55b | -6.7648 | -59.4408 | 2026-09-03 04:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 31.6 |
| 32f9c5a2-f38b-35c8-9dd8-572737b7a5c3 | -3.2485 | -47.2657 | 2026-09-03 04:20:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 64.0 |
| 4f3ac556-35ea-3090-9c6b-1406ab0ae921 | -6.3237 | -56.0434 | 2026-09-03 04:20:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 26.6 |
| 418141f3-9bcc-351d-ba79-ed35d9c6193b | -6.3052 | -56.0442 | 2026-09-03 04:30:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 50.3 |
| a6b76229-2855-3f0a-be57-c612ac7d5ec3 | -8.0737 | -50.9656 | 2026-09-03 04:30:00 | GOES-19 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 84.6 |
| d679c57b-1667-3fa1-9754-265324e3441b | -3.2486 | -47.2438 | 2026-09-03 04:30:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 132.7 |


[Clique aqui para ver as próximas entradas](README23.md)
