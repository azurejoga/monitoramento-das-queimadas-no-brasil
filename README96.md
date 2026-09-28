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

## Dados Diários - Página 96

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 39bccd1c-7fdb-385d-866c-9d604ceff719 | -15.47651 | -46.14298 | 2026-09-28 16:24:00 | NOAA-20 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 10.0 |
| 7e41e95b-9f1a-34c0-85af-42476af2200d | -12.75844 | -47.343 | 2026-09-28 16:24:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 8fb9f652-1163-3fae-8e88-73d337414ecb | -13.16598 | -48.54525 | 2026-09-28 16:24:00 | NOAA-20 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 7.3 |
| c441e7c1-a961-3faa-9f5f-eb85da43c6ec | -11.19972 | -44.79744 | 2026-09-28 16:24:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 158.9 |
| ea7c92e1-577b-3834-a363-28dfd1f1e7c9 | -13.07507 | -47.44982 | 2026-09-28 16:24:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| ce9d72c8-e0c5-3a95-acbd-b90cc7ddac47 | -11.26751 | -43.53706 | 2026-09-28 16:24:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 30.1 |
| 8e2b3c0f-6abb-3585-ba28-04cf860a8899 | -12.38083 | -50.23895 | 2026-09-28 16:24:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 16.8 |
| 5d764d0a-321b-377c-8dd4-fff1ffb62d54 | -12.75489 | -47.3051 | 2026-09-28 16:24:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 11.2 |
| c523adc1-5dd5-3e87-8ca7-b4b2ff054c9f | -12.06414 | -50.22482 | 2026-09-28 16:24:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 13.1 |
| c7cebd12-93cc-37c0-8c29-2816cbc54402 | -12.88143 | -44.79213 | 2026-09-28 16:24:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 777e058d-265b-349b-b0ac-90a41a9637ae | -12.51857 | -49.97955 | 2026-09-28 16:24:00 | NOAA-20 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 15.6 |
| 156a0525-67d3-39a1-bcc1-232d23884629 | -15.26648 | -47.62831 | 2026-09-28 16:24:00 | NOAA-20 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 17.4 |
| 52dd6713-b69e-3d42-9ce4-ae7cb671ddfa | -12.68943 | -45.02042 | 2026-09-28 16:24:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 57.6 |
| 4e33137f-0de6-3277-b0bf-22a02813d9fa | -14.88497 | -40.41005 | 2026-09-28 16:24:00 | NOAA-20 | CAATIBA | BAHIA | Brasil | 2904803 | 29 | 33 | nan | nan | nan | Mata Atlântica | 3.6 |
| 9d54feb7-6268-3beb-b8b9-0dfcf641867f | -16.19613 | -41.33796 | 2026-09-28 16:24:00 | NOAA-20 | MEDINA | MINAS GERAIS | Brasil | 3141405 | 31 | 33 | nan | nan | nan | Mata Atlântica | 17.2 |
| b0c8a3b2-fd6f-346e-a479-60578a10b460 | -11.26409 | -43.53757 | 2026-09-28 16:24:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 46.3 |
| 7fddfbc0-64a0-351f-8af8-3ac8a3a1aa87 | -11.89917 | -47.02577 | 2026-09-28 16:24:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 6.8 |
| bfbfd0c7-d086-3996-8430-29ae90a07395 | -13.54097 | -40.84986 | 2026-09-28 16:24:00 | NOAA-20 | IRAMAIA | BAHIA | Brasil | 2914307 | 29 | 33 | nan | nan | nan | Caatinga | 11.2 |
| b2c15495-ddb7-36fd-bd43-c9bc66b1e110 | -11.68361 | -39.81506 | 2026-09-28 16:24:00 | NOAA-20 | CAPELA DO ALTO ALEGRE | BAHIA | Brasil | 2906857 | 29 | 33 | nan | nan | nan | Caatinga | 9.5 |
| 02b1451e-ac7f-358e-a66f-2f6715157003 | -12.62333 | -47.32209 | 2026-09-28 16:24:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 17.4 |
| bb2ee48d-f30c-3c9a-a693-b7df58072dd7 | -12.80631 | -50.58438 | 2026-09-28 16:24:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 11.0 |
| 3ecc4995-01bc-3834-9fc1-88dc41faad80 | -15.65356 | -52.68056 | 2026-09-28 16:24:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 0de0eada-d19f-3c0e-80e6-255940639421 | -11.72183 | -43.46464 | 2026-09-28 16:24:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 12.2 |
| 79f1e9d6-38ed-30dc-ac78-24d1b04a7fbc | -15.16055 | -43.61473 | 2026-09-28 16:24:00 | NOAA-20 | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Caatinga | 77.9 |
| 0acd335e-242d-396e-ba0e-edc3243b7c67 | -14.31944 | -44.81459 | 2026-09-28 16:24:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 39.1 |
| 68b346b5-e5f3-373b-b717-a722c2d582f4 | -12.75468 | -47.34771 | 2026-09-28 16:24:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 19.7 |
| 7c967250-3304-3a4d-bb52-7bd1ad889391 | -13.17289 | -40.90643 | 2026-09-28 16:24:00 | NOAA-20 | ITAETÉ | BAHIA | Brasil | 2915007 | 29 | 33 | nan | nan | nan | Caatinga | 9.6 |
| f2af2329-885a-3826-9a23-5629880d6037 | -11.50551 | -47.36675 | 2026-09-28 16:24:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 7.7 |
| dad9614c-fabf-3b34-90fd-cde6bc0add1f | -12.38007 | -50.23261 | 2026-09-28 16:24:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 11.4 |
| ff584b9f-6132-342c-af69-8a9c6a9150ca | -15.03867 | -49.59076 | 2026-09-28 16:24:00 | NOAA-20 | ITAPACI | GOIÁS | Brasil | 5210901 | 52 | 33 | nan | nan | nan | Cerrado | 10.8 |
| 7809f0bd-46d0-38c8-8b23-dce15e270fe4 | -11.17754 | -44.79637 | 2026-09-28 16:24:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 197.8 |
| 87e129aa-240a-3564-aa4f-0bfe92ae227e | -16.21378 | -48.82214 | 2026-09-28 16:24:00 | NOAA-20 | ABADIÂNIA | GOIÁS | Brasil | 5200100 | 52 | 33 | nan | nan | nan | Cerrado | 8.2 |
| 1f5cb66c-fe1f-31fd-a85b-5ecbdcb606eb | -13.51616 | -40.84295 | 2026-09-28 16:24:00 | NOAA-20 | IRAMAIA | BAHIA | Brasil | 2914307 | 29 | 33 | nan | nan | nan | Caatinga | 4.7 |
| a6adf4d6-e51c-39da-919f-75db3d5e35d0 | -13.17132 | -48.54996 | 2026-09-28 16:24:00 | NOAA-20 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 8.6 |
| 27c0b3a7-ee2d-3b46-bece-c4464cb9bd47 | -15.40387 | -47.91449 | 2026-09-28 16:24:00 | NOAA-20 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 10.9 |
| a0a20563-7c92-3710-b282-db1a7fa30a73 | -15.17025 | -46.14235 | 2026-09-28 16:24:00 | NOAA-20 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 6.7 |
| ee6d2d56-cf7a-3f1b-b9fa-0716c66f08c5 | -12.64798 | -47.34365 | 2026-09-28 16:24:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 31.5 |
| 20ddce7f-0647-3db9-be74-c98caed7ee38 | -15.20565 | -50.25038 | 2026-09-28 16:24:00 | NOAA-20 | ARAGUAPAZ | GOIÁS | Brasil | 5202155 | 52 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 832da187-9c12-359f-8dc5-5afe6077eecf | -15.21515 | -46.1741 | 2026-09-28 16:24:00 | NOAA-20 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 3.7 |
| d6c0b767-b935-357b-a2d0-f5fd4e9464e2 | -16.54771 | -50.51229 | 2026-09-28 16:24:00 | NOAA-20 | SÃO LUÍS DE MONTES BELOS | GOIÁS | Brasil | 5220108 | 52 | 33 | nan | nan | nan | Cerrado | 8.4 |
| caefafc8-08a0-3c9c-b630-395674157b8d | -16.2028 | -42.87247 | 2026-09-28 16:24:00 | NOAA-20 | GRÃO MOGOL | MINAS GERAIS | Brasil | 3127800 | 31 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 4680232c-1b02-38e0-8038-6a9d074fa777 | -15.19637 | -46.15773 | 2026-09-28 16:24:00 | NOAA-20 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 5d67c68c-ba42-3726-954e-a562e1edf82e | -12.88388 | -44.78283 | 2026-09-28 16:24:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 11.4 |
| 3b8759b3-1f39-3f2f-8142-1ad2982ec4a1 | -11.373 | -43.3983 | 2026-09-28 16:24:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 12.9 |
| bf2e4033-72a9-38fb-a846-ae76faccb325 | -14.52514 | -40.76257 | 2026-09-28 16:24:00 | NOAA-20 | ANAGÉ | BAHIA | Brasil | 2901205 | 29 | 33 | nan | nan | nan | Caatinga | 5.6 |
| eba782cf-d2e4-38bf-9f3e-dcfaf54e0df6 | -12.94768 | -39.10247 | 2026-09-28 16:24:00 | NOAA-20 | SÃO FELIPE | BAHIA | Brasil | 2929107 | 29 | 33 | nan | nan | nan | Mata Atlântica | 6.3 |
| 69b0a00a-0b68-3b8c-9591-aedf4e45a5ca | -12.47352 | -38.34329 | 2026-09-28 16:24:00 | NOAA-20 | MATA DE SÃO JOÃO | BAHIA | Brasil | 2921005 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| b5891752-7b63-311e-9242-4963f61a7251 | -13.36635 | -44.03154 | 2026-09-28 16:24:00 | NOAA-20 | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 18.2 |
| e6ec3566-7b29-33ca-9104-0303da4f0af7 | -14.84881 | -41.48645 | 2026-09-28 16:24:00 | NOAA-20 | TREMEDAL | BAHIA | Brasil | 2931806 | 29 | 33 | nan | nan | nan | Caatinga | 4.5 |
| c173993a-30ee-335b-a506-5e7691b91591 | -15.17431 | -46.14155 | 2026-09-28 16:24:00 | NOAA-20 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 6.7 |
| c7badcbf-3f59-346e-84ee-5d9992cc1e9e | -14.67092 | -40.05991 | 2026-09-28 16:24:00 | NOAA-20 | IGUAÍ | BAHIA | Brasil | 2913507 | 29 | 33 | nan | nan | nan | Mata Atlântica | 11.4 |
| 4c970fd0-3884-35ba-af20-8730f4dafb31 | -14.1752 | -40.5178 | 2026-09-28 16:24:00 | NOAA-20 | MANOEL VITORINO | BAHIA | Brasil | 2920403 | 29 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 1732c2e4-aecf-3b44-ba69-47f4837707fc | -11.63782 | -43.48853 | 2026-09-28 16:24:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 48.3 |
| d237eb6d-595c-3929-a53e-9675ee91387b | -12.076 | -48.55249 | 2026-09-28 16:24:00 | NOAA-20 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 424.5 |
| 0c3747b9-a578-3d78-9dfa-12a130187151 | -11.3768 | -43.42432 | 2026-09-28 16:24:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 17.6 |
| 978b2f67-72b0-30b5-8a87-25a213446f1b | -11.90809 | -49.9876 | 2026-09-28 16:24:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 11.9 |
| 483aa417-057b-3bd4-9175-235526ff2d78 | -12.21275 | -50.30836 | 2026-09-28 16:24:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 9.2 |
| 2150b0bb-8570-3ce4-adff-60c61acf9a2e | -15.68648 | -47.59574 | 2026-09-28 16:24:00 | NOAA-20 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 16.5 |
| 784787cb-95da-32ac-a517-f49bed6a80e8 | -13.19784 | -48.53417 | 2026-09-28 16:24:00 | NOAA-20 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 16.3 |
| afcd1fa5-ca49-3b13-bf13-b511c5700621 | -11.38648 | -43.41909 | 2026-09-28 16:24:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 85.1 |
| be0feb64-8197-3ac1-a832-b3d83485bb7f | -17.17815 | -47.41814 | 2026-09-28 16:24:00 | NOAA-20 | CRISTALINA | GOIÁS | Brasil | 5206206 | 52 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 21308fa3-013c-3438-bab6-85b95a3739de | -14.45339 | -40.80325 | 2026-09-28 16:24:00 | NOAA-20 | ANAGÉ | BAHIA | Brasil | 2901205 | 29 | 33 | nan | nan | nan | Caatinga | 8.4 |
| 39d4144b-0b2b-3f41-ac10-51fa87107267 | -15.4073 | -47.9045 | 2026-09-28 16:24:00 | NOAA-20 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 10.0 |
| 5ae9d093-7f46-3444-8448-fe34356f8505 | -15.12889 | -43.61838 | 2026-09-28 16:24:00 | NOAA-20 | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Caatinga | 6.4 |
| df134b2d-989c-3fb8-b5a2-d52ce5938118 | -11.86675 | -47.1003 | 2026-09-28 16:24:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 11.7 |
| 4148965d-0460-311c-b82b-7d8f4c41ac83 | -13.38638 | -51.32272 | 2026-09-28 16:24:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 47402364-68cc-32f9-be69-d3c252570073 | -12.68573 | -45.02098 | 2026-09-28 16:24:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 19.7 |
| ea4625c6-77a4-3238-9219-4cf55482b09a | -13.72104 | -48.8207 | 2026-09-28 16:24:00 | NOAA-20 | FORMOSO | GOIÁS | Brasil | 5208103 | 52 | 33 | nan | nan | nan | Cerrado | 9.5 |
| 98a0d2d7-a864-36b0-a170-47a84b96ef4d | -17.17828 | -51.74051 | 2026-09-28 16:24:00 | NOAA-20 | CAIAPÔNIA | GOIÁS | Brasil | 5204409 | 52 | 33 | nan | nan | nan | Cerrado | 14.0 |
| 7908037a-0eb0-3e60-b9a5-39e389efdebd | -14.5174 | -52.48939 | 2026-09-28 16:24:00 | NOAA-20 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 32.4 |
| d4005c6c-44b3-3b74-80cf-90c4370e3311 | -11.18533 | -44.79945 | 2026-09-28 16:24:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 161.3 |
| 9b99af1e-9bc1-3073-be4e-3bef7fc9c84e | -15.10206 | -54.71225 | 2026-09-28 16:24:00 | NOAA-20 | CAMPO VERDE | MATO GROSSO | Brasil | 5102678 | 51 | 33 | nan | nan | nan | Cerrado | 30.6 |
| c30f0b0b-f914-36ac-8110-a77aee74d973 | -12.59307 | -51.96371 | 2026-09-28 16:24:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 6d4cacc4-389c-39cd-a211-0d6d708f6ff4 | -12.68388 | -47.36077 | 2026-09-28 16:24:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 42.8 |
| 3314337c-9767-3328-b9a4-319f289fc44d | -12.39641 | -50.237 | 2026-09-28 16:24:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 19.5 |
| 256f0217-e2a5-33a2-aa49-0c5149653fd7 | -13.9436 | -49.07874 | 2026-09-28 16:24:00 | NOAA-20 | MARA ROSA | GOIÁS | Brasil | 5212808 | 52 | 33 | nan | nan | nan | Cerrado | 8.0 |
| e8f13b25-1ef6-307e-8c7e-a5bc6799f187 | -13.45696 | -48.585 | 2026-09-28 16:24:00 | NOAA-20 | TROMBAS | GOIÁS | Brasil | 5221452 | 52 | 33 | nan | nan | nan | Cerrado | 10.8 |
| b74623aa-0f0d-30cc-9123-9cc1cfd6c998 | -12.39198 | -50.24401 | 2026-09-28 16:24:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 26.1 |
| 3416c71b-e892-3480-9a21-c6a9d4e41362 | -11.50656 | -47.37464 | 2026-09-28 16:24:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 7138284b-b1ce-3551-80cb-fe9f8b6fe9cc | -12.62814 | -47.32555 | 2026-09-28 16:24:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 15.0 |
| fb3dccf2-049f-3005-a993-2256ec2db3d5 | -12.71291 | -46.98828 | 2026-09-28 16:24:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 1038cd9c-d1cd-3775-b5d5-6a5c13ac4012 | -11.18233 | -44.80414 | 2026-09-28 16:24:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 117.8 |
| 9599bac2-0c9c-3e50-8367-a313ade47809 | -10.49267 | -40.3971 | 2026-09-28 16:24:00 | NOAA-20 | CAMPO FORMOSO | BAHIA | Brasil | 2906006 | 29 | 33 | nan | nan | nan | Caatinga | 2.4 |
| caa62721-ef2a-3ef7-9550-1fed5ea5b2fb | -13.36581 | -40.96891 | 2026-09-28 16:24:00 | NOAA-20 | IRAMAIA | BAHIA | Brasil | 2914307 | 29 | 33 | nan | nan | nan | Caatinga | 10.9 |
| 13db6394-b8da-3aa5-b17b-00bd08effef2 | -11.85385 | -47.11076 | 2026-09-28 16:24:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 12.8 |
| 36e66a9e-13df-34dc-a21d-59de8f0e66bc | -12.26995 | -46.48638 | 2026-09-28 16:24:00 | NOAA-20 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| e074aa9a-a592-3a63-be9b-6bff87ae9c0d | -13.3187 | -43.95118 | 2026-09-28 16:24:00 | NOAA-20 | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 103.7 |
| 74991e3f-3384-31c7-8836-58e7f56868f7 | -16.09092 | -47.86416 | 2026-09-28 16:24:00 | NOAA-20 | CIDADE OCIDENTAL | GOIÁS | Brasil | 5205497 | 52 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 7dfbf616-5fad-36f6-a9d9-eac887edf8c3 | -15.03424 | -49.59754 | 2026-09-28 16:24:00 | NOAA-20 | ITAPACI | GOIÁS | Brasil | 5210901 | 52 | 33 | nan | nan | nan | Cerrado | 8.5 |
| fc3887e6-1dca-3937-bdce-994d2a412eba | -16.54955 | -50.51574 | 2026-09-28 16:24:00 | NOAA-20 | SÃO LUÍS DE MONTES BELOS | GOIÁS | Brasil | 5220108 | 52 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 88acab6f-8807-3808-929f-d2f8b0c77a2e | -15.47243 | -46.14375 | 2026-09-28 16:24:00 | NOAA-20 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 16.1 |
| 3b4cb2bd-a2cc-3ba6-bc60-859c5726b068 | -12.05822 | -50.21922 | 2026-09-28 16:24:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 61fa0f43-e5ad-38db-b484-8156e8098517 | -12.29795 | -40.49461 | 2026-09-28 16:24:00 | NOAA-20 | RUY BARBOSA | BAHIA | Brasil | 2927200 | 29 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 0bf5f441-03e7-380c-ab03-1475f9595bc2 | -11.84772 | -47.78229 | 2026-09-28 16:24:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 844e84ad-2cf0-39d7-9f5f-3ac1b2cb687a | -12.61426 | -47.31925 | 2026-09-28 16:24:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 9.1 |
| ed39df89-ecf8-33f2-8e6a-37d9825d2f64 | -12.65283 | -39.84364 | 2026-09-28 16:24:00 | NOAA-20 | IAÇU | BAHIA | Brasil | 2911907 | 29 | 33 | nan | nan | nan | Caatinga | 7.6 |
| 27fde3c8-3673-3cf1-8a41-9dc0afb7b0ac | -12.31335 | -50.30269 | 2026-09-28 16:24:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 10.7 |
| dd2a516f-75fa-36e1-8101-e3222d44a57e | -13.7108 | -39.82473 | 2026-09-28 16:24:00 | NOAA-20 | JAGUAQUARA | BAHIA | Brasil | 2917607 | 29 | 33 | nan | nan | nan | Mata Atlântica | 3.0 |
| cda87f9d-21d5-39e9-80b0-ab6488ff6c14 | -11.54508 | -47.37362 | 2026-09-28 16:24:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 15.2 |
| 65f5a790-3cbb-375c-87ac-e672db5bf7e1 | -13.52934 | -48.17163 | 2026-09-28 16:24:00 | NOAA-20 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 4.6 |


[Clique aqui para ver as próximas entradas](README97.md)
