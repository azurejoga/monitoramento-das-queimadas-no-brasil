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

## Dados Diários - Página 3

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| dc9eb198-4ed7-3a42-9a8f-c03a26198b08 | -8.1217 | -47.99109 | 2026-01-01 03:55:00 | NOAA-21 | ITAPIRATINS | TOCANTINS | Brasil | 1710904 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 6dfdb86a-7061-354f-a177-4bb90243aad5 | -5.72556 | -45.03658 | 2026-01-01 03:55:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 11.7 |
| 12558f8f-71a4-36d1-9bec-da7ef4231b1e | -9.58487 | -44.59911 | 2026-01-01 03:55:00 | NOAA-21 | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ad0a9b7c-c976-3a52-8d44-fbcec0ffe218 | -12.61329 | -38.05048 | 2026-01-01 03:57:00 | NOAA-21 | CAMAÇARI | BAHIA | Brasil | 2905701 | 29 | 33 | nan | nan | nan | Mata Atlântica | 4.3 |
| 9d98d3cc-4eeb-3ba4-8500-f8d891c52b2c | -16.65755 | -43.5256 | 2026-01-01 03:57:00 | NOAA-21 | FRANCISCO SÁ | MINAS GERAIS | Brasil | 3126703 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 9ca6d100-4b0d-3366-91f5-bf8b61a55e69 | -13.47141 | -44.03435 | 2026-01-01 03:57:00 | NOAA-21 | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 63a6fbe5-2aad-3272-afaf-3551382b307a | -13.62709 | -44.32858 | 2026-01-01 03:57:00 | NOAA-21 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| de29e697-ce76-30fc-8db8-21f50c9ffeb8 | -16.42774 | -41.01305 | 2026-01-01 03:57:00 | NOAA-21 | JEQUITINHONHA | MINAS GERAIS | Brasil | 3135803 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| d12f81b6-6c9e-35cd-b0ad-44281910647a | -12.66011 | -46.76101 | 2026-01-01 03:57:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 66ba4998-6271-3ac2-9a2b-3e5cfc413436 | -16.39236 | -41.04369 | 2026-01-01 03:57:00 | NOAA-21 | JEQUITINHONHA | MINAS GERAIS | Brasil | 3135803 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 9dcd825a-b6cd-3fcd-b444-0b77297c39f0 | -18.16657 | -46.98695 | 2026-01-01 03:57:00 | NOAA-21 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| bc8b02c5-5c25-346b-a485-c6732bd833e5 | -17.3647 | -41.51973 | 2026-01-01 03:57:00 | NOAA-21 | CATUJI | MINAS GERAIS | Brasil | 3115458 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.4 |
| 35212ea1-5e13-389c-9d52-725dfbaf0120 | -13.47534 | -44.01137 | 2026-01-01 03:57:00 | NOAA-21 | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 0cca196e-2afc-3198-9c55-288a659a63fc | -15.14069 | -45.27466 | 2026-01-01 03:57:00 | NOAA-21 | JANUÁRIA | MINAS GERAIS | Brasil | 3135209 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| bcdd9172-7a90-3643-9138-c1476c5e188d | -13.17625 | -39.88708 | 2026-01-01 03:57:00 | NOAA-21 | SANTA INÊS | BAHIA | Brasil | 2927903 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| a2c67569-9db4-31c8-88ca-a528c5a1d586 | -19.2034 | -39.70798 | 2026-01-01 03:57:00 | NOAA-21 | LINHARES | ESPÍRITO SANTO | Brasil | 3203205 | 32 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| d8d948ce-88de-341d-b0eb-308ebf827705 | -12.84832 | -43.63123 | 2026-01-01 03:57:00 | NOAA-21 | SERRA DOURADA | BAHIA | Brasil | 2930303 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| a1c15044-f535-3199-966d-27bcbe43c262 | -19.71555 | -40.61384 | 2026-01-01 03:57:00 | NOAA-21 | SÃO ROQUE DO CANAÃ | ESPÍRITO SANTO | Brasil | 3204955 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 6d6598c5-b1b6-3fb3-a542-a731b03d2730 | -12.61385 | -38.04671 | 2026-01-01 03:57:00 | NOAA-21 | CAMAÇARI | BAHIA | Brasil | 2905701 | 29 | 33 | nan | nan | nan | Mata Atlântica | 4.3 |
| 78852b45-4da5-3945-83cf-ecf18b18ea6c | -14.55511 | -40.1381 | 2026-01-01 03:57:00 | NOAA-21 | IGUAÍ | BAHIA | Brasil | 2913507 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 2eec4f99-a95c-30fe-adcf-7a2c7a58673f | -12.82492 | -38.22832 | 2026-01-01 03:57:00 | NOAA-21 | CAMAÇARI | BAHIA | Brasil | 2905701 | 29 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| daa508cb-ed71-3377-acbd-228f9613c2b3 | -15.43728 | -41.86237 | 2026-01-01 03:57:00 | NOAA-21 | SÃO JOÃO DO PARAÍSO | MINAS GERAIS | Brasil | 3162708 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 3ab8d77c-8f4f-3a6a-94cb-d059dde002bf | -13.62792 | -44.32378 | 2026-01-01 03:57:00 | NOAA-21 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 7f7b5a3f-1571-3610-a47d-cd458a29e7dc | -13.47455 | -44.01596 | 2026-01-01 03:57:00 | NOAA-21 | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 87387d9a-946e-326d-b2a1-4c80b7c5696b | -16.14774 | -42.30908 | 2026-01-01 03:57:00 | NOAA-21 | SALINAS | MINAS GERAIS | Brasil | 3157005 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.9 |
| b1e4f688-a6fd-39bd-acae-a49bb1afdf7d | -16.91705 | -43.49476 | 2026-01-01 03:57:00 | NOAA-21 | JURAMENTO | MINAS GERAIS | Brasil | 3136801 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 1e317c6b-3820-3dc7-95b9-d9d296c5885c | -14.75092 | -40.77504 | 2026-01-01 03:57:00 | NOAA-21 | VITÓRIA DA CONQUISTA | BAHIA | Brasil | 2933307 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| a0be8e23-bf75-3add-860f-d37c88b63c99 | -17.29719 | -41.74995 | 2026-01-01 03:57:00 | NOAA-21 | CARAÍ | MINAS GERAIS | Brasil | 3113008 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 8caa4944-3aa8-3e4d-aab2-37c38984d65f | -18.50067 | -47.60234 | 2026-01-01 03:57:00 | NOAA-21 | MONTE CARMELO | MINAS GERAIS | Brasil | 3143104 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 5e629705-8a46-39b9-89fe-1c33c2e6625a | -15.14043 | -45.27697 | 2026-01-01 03:57:00 | NOAA-21 | JANUÁRIA | MINAS GERAIS | Brasil | 3135209 | 31 | 33 | nan | nan | nan | Cerrado | 2.6 |
| bcb837be-6518-3a8b-8ff0-d3120fec79df | -17.51812 | -39.52853 | 2026-01-01 03:57:00 | NOAA-21 | ALCOBAÇA | BAHIA | Brasil | 2900801 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 291852d3-1e30-3ce4-a87b-8f3bcb246c8e | -19.38922 | -41.47292 | 2026-01-01 03:57:00 | NOAA-21 | CONSELHEIRO PENA | MINAS GERAIS | Brasil | 3118403 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 4bf92e9d-c73f-3636-af23-d1104d17d579 | -12.9538 | -41.18138 | 2026-01-01 03:57:00 | NOAA-21 | ITAETÉ | BAHIA | Brasil | 2915007 | 29 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 6d268162-b587-3817-91a5-7f9ff6b957ba | -12.95045 | -41.18082 | 2026-01-01 03:57:00 | NOAA-21 | ITAETÉ | BAHIA | Brasil | 2915007 | 29 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 2441a450-6a47-3a5c-9344-fa6b8d217745 | -13.26427 | -41.32534 | 2026-01-01 03:57:00 | NOAA-21 | MUCUGÊ | BAHIA | Brasil | 2921906 | 29 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 4c90ff8f-73ff-3124-8d41-3232f38e3beb | -15.24662 | -43.0557 | 2026-01-01 03:57:00 | NOAA-21 | MONTE AZUL | MINAS GERAIS | Brasil | 3142908 | 31 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 7dc4a7a7-74d9-3966-b52b-16843365f501 | -16.91287 | -43.49817 | 2026-01-01 03:57:00 | NOAA-21 | JURAMENTO | MINAS GERAIS | Brasil | 3136801 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 1a909dab-7802-3e86-b825-94841821cdff | -16.91356 | -43.4941 | 2026-01-01 03:57:00 | NOAA-21 | JURAMENTO | MINAS GERAIS | Brasil | 3136801 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 4bbc4050-f7e3-31fc-84ce-c047376eeac4 | -10.93822 | -49.429 | 2026-01-01 03:57:00 | NOAA-21 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 7abe5426-033c-3e43-abaa-954f461c4948 | -16.13562 | -40.4464 | 2026-01-01 03:57:00 | NOAA-21 | ALMENARA | MINAS GERAIS | Brasil | 3101706 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 77f92289-9805-35f5-bf1d-d887d7b8a8b5 | -12.6646 | -46.76183 | 2026-01-01 03:57:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 4.8 |
| a28a01a3-4455-3319-abbc-61103d52cd98 | -16.3918 | -41.04727 | 2026-01-01 03:57:00 | NOAA-21 | JEQUITINHONHA | MINAS GERAIS | Brasil | 3135803 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| b189c7e8-b19b-3a37-8208-cc6c0fc53d53 | -12.98298 | -42.64592 | 2026-01-01 03:57:00 | NOAA-21 | MACAÚBAS | BAHIA | Brasil | 2919801 | 29 | 33 | nan | nan | nan | Caatinga | 1.3 |
| dbd70d99-713e-35de-a654-65c207bf74c5 | -16.25644 | -42.2045 | 2026-01-01 03:57:00 | NOAA-21 | SALINAS | MINAS GERAIS | Brasil | 3157005 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 02f2ad54-19ff-36ae-b3f9-885f8642ba7c | -13.46766 | -44.03373 | 2026-01-01 03:57:00 | NOAA-21 | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 93615804-4e7c-3b0c-a7ac-df6ce79e3770 | -14.8387 | -40.84423 | 2026-01-01 03:57:00 | NOAA-21 | VITÓRIA DA CONQUISTA | BAHIA | Brasil | 2933307 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 43ca451a-c8de-3a01-9404-2bf1b9a5f819 | -20.38944 | -40.33113 | 2026-01-01 03:59:00 | NOAA-21 | VILA VELHA | ESPÍRITO SANTO | Brasil | 3205200 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| ac84dc17-7b55-3b62-b01c-1ba52c3facfa | -22.32001 | -42.6441 | 2026-01-01 03:59:00 | NOAA-21 | NOVA FRIBURGO | RIO DE JANEIRO | Brasil | 3303401 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 16e7fbe0-1fed-3008-b63d-ba0912435e2d | -22.61871 | -43.73471 | 2026-01-01 03:59:00 | NOAA-21 | PARACAMBI | RIO DE JANEIRO | Brasil | 3303609 | 33 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| 81ccebb8-f47d-3523-883f-8f2b467c8814 | -20.3417 | -40.37379 | 2026-01-01 03:59:00 | NOAA-21 | CARIACICA | ESPÍRITO SANTO | Brasil | 3201308 | 32 | 33 | nan | nan | nan | Mata Atlântica | 2.6 |
| 2ca3c514-958d-3cb5-a245-46bed27ff850 | -17.70656 | -53.26962 | 2026-01-01 03:59:00 | NOAA-21 | ALTO TAQUARI | MATO GROSSO | Brasil | 5100607 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 6c89bc52-1f45-3431-8f7e-f9a5d6cc9de7 | -22.81941 | -42.21656 | 2026-01-01 03:59:00 | NOAA-21 | IGUABA GRANDE | RIO DE JANEIRO | Brasil | 3301876 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| f9716350-9ccf-3423-9f6f-6dcb18b78e67 | -19.57914 | -43.68843 | 2026-01-01 03:59:00 | NOAA-21 | TAQUARAÇU DE MINAS | MINAS GERAIS | Brasil | 3168309 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| be51d335-2426-3b41-99c6-66c70593c599 | -20.39224 | -40.33549 | 2026-01-01 03:59:00 | NOAA-21 | VILA VELHA | ESPÍRITO SANTO | Brasil | 3205200 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 025357eb-1d35-3e65-af75-783f007a00df | -22.41966 | -43.74543 | 2026-01-01 03:59:00 | NOAA-21 | VASSOURAS | RIO DE JANEIRO | Brasil | 3306206 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| 86c91080-f0c1-3316-8dd0-e41846e71fc9 | -22.7412 | -42.71305 | 2026-01-01 03:59:00 | NOAA-21 | TANGUÁ | RIO DE JANEIRO | Brasil | 3305752 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 76609e85-68af-3117-804d-d93f9b720c0b | -19.91071 | -42.32335 | 2026-01-01 03:59:00 | NOAA-21 | BOM JESUS DO GALHO | MINAS GERAIS | Brasil | 3107802 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 0bbccb31-0efe-327e-9833-672b87c59afb | -23.21046 | -45.35077 | 2026-01-01 03:59:00 | NOAA-21 | SÃO LUIZ DO PARAITINGA | SÃO PAULO | Brasil | 3550001 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| d79b81e0-3bb5-3a49-ba9c-576bf0cf9613 | -20.02548 | -41.20701 | 2026-01-01 03:59:00 | NOAA-21 | AFONSO CLÁUDIO | ESPÍRITO SANTO | Brasil | 3200102 | 32 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| a39fc4eb-eeaa-3600-a172-582ee6dbf206 | -22.92582 | -42.64264 | 2026-01-01 03:59:00 | NOAA-21 | MARICÁ | RIO DE JANEIRO | Brasil | 3302700 | 33 | 33 | nan | nan | nan | Mata Atlântica | 3.3 |
| 06b5152d-c71c-39ee-9eee-120117cb27e4 | -20.39281 | -40.33169 | 2026-01-01 03:59:00 | NOAA-21 | VILA VELHA | ESPÍRITO SANTO | Brasil | 3205200 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| fc4f4e79-8294-3296-b6a9-b46feb8534ce | -9.5821 | -44.6007 | 2026-01-01 04:00:00 | GOES-19 | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 46.6 |
| 352d6a65-1067-3335-b990-0659983a5b1d | -3.86752 | -54.23378 | 2026-01-01 04:23:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 46dc624f-86c6-39a4-827c-939862d5f607 | -4.31278 | -39.37464 | 2026-01-01 04:23:00 | NPP-375D | CANINDÉ | CEARÁ | Brasil | 2302800 | 23 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 83d92056-3411-3e5e-8c65-9d5ce7b97a7a | -2.55274 | -48.93016 | 2026-01-01 04:23:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| dccb7f84-071e-36af-9dc3-c0ce20fd596e | -4.60064 | -45.99184 | 2026-01-01 04:23:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 34437108-b19f-344e-a0e9-d18c8387d3c5 | -5.26592 | -44.77335 | 2026-01-01 04:23:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 6bbf654f-23fc-3238-bd1b-485f7404939e | -1.49834 | -45.91555 | 2026-01-01 04:23:00 | NPP-375D | LUÍS DOMINGUES | MARANHÃO | Brasil | 2106201 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 83e84ca7-21b1-3322-a1b2-fb60635a2b2a | -2.89248 | -52.58544 | 2026-01-01 04:23:00 | NPP-375D | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| b5b7a1c6-5033-36bc-8e66-10db7e537ee3 | -3.49899 | -47.17274 | 2026-01-01 04:23:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5d24c3e8-76ff-3c0c-993f-d276f12260da | -2.33839 | -44.90793 | 2026-01-01 04:23:00 | NPP-375D | CENTRAL DO MARANHÃO | MARANHÃO | Brasil | 2103125 | 21 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 72fc6d76-2dce-3789-b27f-c2da1b09fb94 | -1.79369 | -45.89822 | 2026-01-01 04:23:00 | NPP-375D | MARACAÇUMÉ | MARANHÃO | Brasil | 2106326 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 4d85dc74-3e09-3ea2-91a8-1f5f25e8bd5a | -6.59027 | -35.17525 | 2026-01-01 04:23:00 | NPP-375D | MAMANGUAPE | PARAÍBA | Brasil | 2508901 | 25 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 398d422f-0ceb-3688-b53b-4ddbe330733d | -2.27471 | -44.81147 | 2026-01-01 04:23:00 | NPP-375D | CENTRAL DO MARANHÃO | MARANHÃO | Brasil | 2103125 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d7bd652c-8619-366b-b02d-3c50910f9e90 | -3.87335 | -43.374 | 2026-01-01 04:23:00 | NPP-375D | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| cdf5ce9b-7407-3a57-962a-8cd75b0b5c1c | -3.09087 | -43.37717 | 2026-01-01 04:23:00 | NPP-375D | BELÁGUA | MARANHÃO | Brasil | 2101731 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 066e5817-e923-312a-b0cd-bda8534f03d4 | -1.82913 | -44.88954 | 2026-01-01 04:23:00 | NPP-375D | CURURUPU | MARANHÃO | Brasil | 2103703 | 21 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 0f863194-5e87-38bd-80d2-655381159026 | -5.265 | -44.90813 | 2026-01-01 04:23:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c5170f41-cff4-3003-82bf-cf174f1016e0 | -2.54464 | -44.07172 | 2026-01-01 04:23:00 | NPP-375D | SÃO JOSÉ DE RIBAMAR | MARANHÃO | Brasil | 2111201 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| b66cdf84-9088-3425-ad9c-6b17f5769335 | -6.60028 | -35.18468 | 2026-01-01 04:23:00 | NPP-375D | MAMANGUAPE | PARAÍBA | Brasil | 2508901 | 25 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 4228c35c-4427-348e-a0bf-df794b72668a | -1.54293 | -47.2154 | 2026-01-01 04:23:00 | NPP-375D | OURÉM | PARÁ | Brasil | 1505403 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 349d9908-515f-3e3c-8f84-a654cbcae745 | -3.81789 | -40.95328 | 2026-01-01 04:23:00 | NPP-375D | UBAJARA | CEARÁ | Brasil | 2313609 | 23 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 3ed306ff-6769-352f-80a0-4f276990cd2c | -3.41753 | -49.48727 | 2026-01-01 04:23:00 | NPP-375D | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 3bfe78fe-1a46-3602-9a96-c303ff44d73c | -4.33039 | -45.35154 | 2026-01-01 04:23:00 | NPP-375D | VITORINO FREIRE | MARANHÃO | Brasil | 2113009 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 7f15620e-0247-3a01-9a02-0529ebf0e946 | -2.3754 | -47.41888 | 2026-01-01 04:23:00 | NPP-375D | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| fce07213-5131-3764-a991-782bc7d70449 | -2.12553 | -46.30505 | 2026-01-01 04:23:00 | NPP-375D | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| bf8eca45-1a47-3c63-be75-e6359b55e692 | -2.09377 | -45.98638 | 2026-01-01 04:23:00 | NPP-375D | MARACAÇUMÉ | MARANHÃO | Brasil | 2106326 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e0482eab-3778-30a3-b24e-c6a17c288eb2 | -3.027 | -50.51183 | 2026-01-01 04:23:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 336176cb-6ab9-3966-bae6-452a2d6fd76a | -3.13819 | -40.11665 | 2026-01-01 04:23:00 | NPP-375D | MARCO | CEARÁ | Brasil | 2307809 | 23 | 33 | nan | nan | nan | Caatinga | 0.6 |
| cae376b1-c5fb-3ff3-be72-a5568f7eb49a | -2.53195 | -51.79844 | 2026-01-01 04:23:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5863d5c8-f50f-3325-ac30-e7fa5f1919b7 | -2.41605 | -46.1562 | 2026-01-01 04:23:00 | NPP-375D | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 25f70337-7fa3-3134-8f32-5f70665689e9 | -1.54141 | -47.21374 | 2026-01-01 04:23:00 | NPP-375D | OURÉM | PARÁ | Brasil | 1505403 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 355fc17a-f2fb-36af-9f68-d22ee79b7f9b | -1.83249 | -44.89006 | 2026-01-01 04:23:00 | NPP-375D | CURURUPU | MARANHÃO | Brasil | 2103703 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 8500c3d1-aad9-36dc-849b-fb54c3e77acf | -3.42167 | -49.48794 | 2026-01-01 04:23:00 | NPP-375D | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 78935305-90bd-383b-94d9-b02528bf08ac | -2.95274 | -40.19464 | 2026-01-01 04:23:00 | NPP-375D | BELA CRUZ | CEARÁ | Brasil | 2302305 | 23 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 32d7dc49-0df3-3e2b-89a6-2d4c636480bd | -3.02182 | -50.5155 | 2026-01-01 04:23:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 925c7581-2b68-370c-b10d-45dd34d53156 | -3.44243 | -50.11939 | 2026-01-01 04:23:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 2ec3be93-9001-3072-a9b8-cf09035a3b70 | -2.54927 | -48.92595 | 2026-01-01 04:23:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ad3a7e9a-c89b-322e-8134-403a034ef901 | -3.02628 | -50.51626 | 2026-01-01 04:23:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| f584430c-e5a6-345f-9433-4afd71ef8e3b | -2.33615 | -44.90037 | 2026-01-01 04:23:00 | NPP-375D | CENTRAL DO MARANHÃO | MARANHÃO | Brasil | 2103125 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |


[Clique aqui para ver as próximas entradas](README4.md)
