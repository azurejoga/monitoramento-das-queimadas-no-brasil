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

## Dados Diários - Página 8

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| c9dd770e-1b64-3e40-a147-cb406e7c5c3d | -16.80441 | -54.58915 | 2026-07-19 04:21:00 | NOAA-20 | RONDONÓPOLIS | MATO GROSSO | Brasil | 5107602 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a04a876e-a5c6-3688-a616-3345b5aa2c30 | -15.95186 | -47.27759 | 2026-07-19 04:21:00 | NOAA-20 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 2784eb27-d328-3828-b6b0-9b277cb6d797 | -22.25348 | -52.87732 | 2026-07-19 04:21:00 | NOAA-20 | ANAURILÂNDIA | MATO GROSSO DO SUL | Brasil | 5000807 | 50 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| af70fb7f-2579-39c1-a22e-0df0b6bea645 | -22.90697 | -43.44866 | 2026-07-19 04:21:00 | NOAA-20 | RIO DE JANEIRO | RIO DE JANEIRO | Brasil | 3304557 | 33 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| 929af35d-1543-3c9a-9215-5a0b9995ec96 | -23.23081 | -46.68136 | 2026-07-19 04:21:00 | NOAA-20 | ATIBAIA | SÃO PAULO | Brasil | 3504107 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 7df6393e-ff58-31b8-bf72-6074978fde53 | -20.5312 | -57.39762 | 2026-07-19 04:21:00 | NOAA-20 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 1.6 |
| c026827a-80df-30b3-abf7-3bc4d41d1d91 | -19.84487 | -57.91997 | 2026-07-19 04:21:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.2 |
| 13c0b7cb-02bb-341f-a78b-0c50de0c43cd | -19.17568 | -47.35349 | 2026-07-19 04:21:00 | NOAA-20 | PERDIZES | MINAS GERAIS | Brasil | 3149804 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| fba94087-933c-3505-ab07-45c7e6b069a0 | -17.37475 | -42.71625 | 2026-07-19 04:21:00 | NOAA-20 | VEREDINHA | MINAS GERAIS | Brasil | 3171071 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 57ad88ae-5775-3959-854d-0b9490f18ab6 | -16.48893 | -52.7219 | 2026-07-19 04:21:00 | NOAA-20 | RIBEIRÃOZINHO | MATO GROSSO | Brasil | 5107198 | 51 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 8ecb0554-2a77-30b6-8156-dba67ace06e8 | -15.9491 | -47.27317 | 2026-07-19 04:21:00 | NOAA-20 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| a74681dd-1a12-34e4-9127-bf2d34aa0bb7 | -19.98594 | -43.97414 | 2026-07-19 04:21:00 | NOAA-20 | BELO HORIZONTE | MINAS GERAIS | Brasil | 3106200 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 660fd7f9-f46d-314c-b07a-e130cc354926 | -18.49131 | -46.91645 | 2026-07-19 04:21:00 | NOAA-20 | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| a34aae8c-620f-308a-8418-e657b7f5c618 | -19.85355 | -57.92445 | 2026-07-19 04:21:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.2 |
| 341ed94b-2cac-38ed-b727-b0175d58366e | -23.37276 | -47.31548 | 2026-07-19 04:21:00 | NOAA-20 | ITU | SÃO PAULO | Brasil | 3523909 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| fdfab73d-be2f-3079-8fe0-e8fab754707a | -22.33352 | -43.14729 | 2026-07-19 04:21:00 | NOAA-20 | PETRÓPOLIS | RIO DE JANEIRO | Brasil | 3303906 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| f3f8fb66-2b7c-3458-ba4f-66fce4cf494b | -17.37056 | -42.71999 | 2026-07-19 04:21:00 | NOAA-20 | VEREDINHA | MINAS GERAIS | Brasil | 3171071 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 57ca0836-1b19-3bfd-a568-8f1b79ac79a9 | -18.02719 | -54.36508 | 2026-07-19 04:21:00 | NOAA-20 | PEDRO GOMES | MATO GROSSO DO SUL | Brasil | 5006408 | 50 | 33 | nan | nan | nan | Cerrado | 1.6 |
| bf757c93-d160-3f31-b84a-5b64eae3ef67 | -19.72222 | -48.02651 | 2026-07-19 04:21:00 | NOAA-20 | UBERABA | MINAS GERAIS | Brasil | 3170107 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 711972c7-42be-3b18-aa1d-4efb43d7b4d1 | -22.90822 | -43.44665 | 2026-07-19 04:21:00 | NOAA-20 | RIO DE JANEIRO | RIO DE JANEIRO | Brasil | 3304557 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 0d490e8b-be56-393d-94c2-1912b9ae3120 | -19.88213 | -44.77497 | 2026-07-19 04:21:00 | NOAA-20 | IGARATINGA | MINAS GERAIS | Brasil | 3130200 | 31 | 33 | nan | nan | nan | Cerrado | 0.3 |
| bbb5994f-c32d-3bdb-bc2a-dd53b6b3f0cb | -16.80379 | -54.5922 | 2026-07-19 04:21:00 | NOAA-20 | RONDONÓPOLIS | MATO GROSSO | Brasil | 5107602 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ebfcc4aa-fe6a-318d-a659-0cd5fc3d5a80 | -17.36699 | -42.71936 | 2026-07-19 04:21:00 | NOAA-20 | VEREDINHA | MINAS GERAIS | Brasil | 3171071 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 579df08a-d14e-39db-84e1-03a01e31f702 | -20.56695 | -54.57913 | 2026-07-19 04:21:00 | NOAA-20 | CAMPO GRANDE | MATO GROSSO DO SUL | Brasil | 5002704 | 50 | 33 | nan | nan | nan | Cerrado | 2.1 |
| a7f4a77c-b9db-3732-bb64-6e111e972957 | -20.53212 | -57.39354 | 2026-07-19 04:21:00 | NOAA-20 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 35f8d8d6-fd8b-33c5-96fa-d9288b0aa925 | -19.74266 | -46.47083 | 2026-07-19 04:21:00 | NOAA-20 | PRATINHA | MINAS GERAIS | Brasil | 3153004 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 43197a55-3e32-3fda-bdfb-a532db814729 | -22.72081 | -43.47947 | 2026-07-19 04:21:00 | NOAA-20 | NOVA IGUAÇU | RIO DE JANEIRO | Brasil | 3303500 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 7a74f93e-6ca7-34d6-835f-eb5a1361509d | -22.29045 | -42.59391 | 2026-07-19 04:21:00 | NOAA-20 | NOVA FRIBURGO | RIO DE JANEIRO | Brasil | 3303401 | 33 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 3bdd64c0-f2a6-3e2c-aa5a-a2d25229832a | -19.93322 | -44.06878 | 2026-07-19 04:21:00 | NOAA-20 | CONTAGEM | MINAS GERAIS | Brasil | 3118601 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| 7b15df91-471a-32c3-b903-fbff58398d1f | -22.92058 | -43.43067 | 2026-07-19 04:21:00 | NOAA-20 | RIO DE JANEIRO | RIO DE JANEIRO | Brasil | 3304557 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| f3c1b0aa-b79e-342d-adf0-889865a30438 | -19.8477 | -57.92294 | 2026-07-19 04:21:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.2 |
| 8f6842b1-1b2d-3074-b2e4-9172d265997c | -21.53435 | -46.7622 | 2026-07-19 04:21:00 | NOAA-20 | TAPIRATIBA | SÃO PAULO | Brasil | 3553609 | 35 | 33 | nan | nan | nan | Mata Atlântica | 5.1 |
| 495e64c0-24b9-3366-92cf-fe346e526772 | -15.60511 | -52.95831 | 2026-07-19 04:21:00 | NOAA-20 | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 9f33af76-1264-370b-aa35-8c3194a117dc | -22.24938 | -52.87634 | 2026-07-19 04:21:00 | NOAA-20 | ANAURILÂNDIA | MATO GROSSO DO SUL | Brasil | 5000807 | 50 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 95dff24a-b12a-3035-ac56-333afbe4d2f1 | -16.6678 | -48.29795 | 2026-07-19 04:21:00 | NOAA-20 | SILVÂNIA | GOIÁS | Brasil | 5220603 | 52 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 36fafd12-3cff-3d15-973e-31dbd1097ca5 | -20.52783 | -57.4014 | 2026-07-19 04:21:00 | NOAA-20 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 1d4d555d-70b9-3a77-ad6e-ac31ba6be848 | -20.52468 | -57.40025 | 2026-07-19 04:21:00 | NOAA-20 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ee665662-f9ee-3644-905b-c019de88d045 | -17.25777 | -48.28489 | 2026-07-19 04:21:00 | NOAA-20 | PIRES DO RIO | GOIÁS | Brasil | 5217401 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e9ba361b-f2c2-3e70-acad-8cf192b037a9 | -19.17628 | -47.34979 | 2026-07-19 04:21:00 | NOAA-20 | PERDIZES | MINAS GERAIS | Brasil | 3149804 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| bc44b942-b8cf-3120-ae68-3c31c29cf5d1 | -23.73628 | -46.61855 | 2026-07-19 04:23:00 | NOAA-20 | DIADEMA | SÃO PAULO | Brasil | 3513801 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| d089443f-a850-305e-8b31-aac228652d2b | -21.99738 | -56.02507 | 2026-07-19 04:23:00 | NOAA-20 | PONTA PORÃ | MATO GROSSO DO SUL | Brasil | 5006606 | 50 | 33 | nan | nan | nan | Cerrado | 13.6 |
| 995435be-5657-34b2-9412-5c7c045fb317 | -22.25757 | -55.97307 | 2026-07-19 04:23:00 | NOAA-20 | ANTÔNIO JOÃO | MATO GROSSO DO SUL | Brasil | 5000906 | 50 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 173a4c15-a4bb-3101-8535-612ec4936f4c | -22.00307 | -56.02314 | 2026-07-19 04:23:00 | NOAA-20 | PONTA PORÃ | MATO GROSSO DO SUL | Brasil | 5006606 | 50 | 33 | nan | nan | nan | Cerrado | 13.2 |
| 1fe78d09-6086-3ecf-9d58-74918e74e452 | -22.25351 | -55.97105 | 2026-07-19 04:23:00 | NOAA-20 | ANTÔNIO JOÃO | MATO GROSSO DO SUL | Brasil | 5000906 | 50 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 8b3f02e6-f12d-31e5-9cdb-b2e0a0f757c1 | -23.76639 | -53.27389 | 2026-07-19 04:23:00 | NOAA-20 | UMUARAMA | PARANÁ | Brasil | 4128104 | 41 | 33 | nan | nan | nan | Mata Atlântica | 15.0 |
| 7f418532-f908-3c3c-ba3c-06dce729f346 | -23.37596 | -47.42406 | 2026-07-19 04:23:00 | NOAA-20 | SOROCABA | SÃO PAULO | Brasil | 3552205 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| c371a5d1-19e3-32ad-8c6c-0e1da811eecc | -22.22202 | -55.99598 | 2026-07-19 04:23:00 | NOAA-20 | ANTÔNIO JOÃO | MATO GROSSO DO SUL | Brasil | 5000906 | 50 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 48c438d4-1aab-3368-9fe0-e301d44c1159 | -29.14092 | -50.81667 | 2026-07-19 04:23:00 | NOAA-20 | SÃO FRANCISCO DE PAULA | RIO GRANDE DO SUL | Brasil | 4318200 | 43 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| ae92dc2b-af6e-301f-aa0c-7432323609a8 | -22.23253 | -55.9959 | 2026-07-19 04:23:00 | NOAA-20 | ANTÔNIO JOÃO | MATO GROSSO DO SUL | Brasil | 5000906 | 50 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 719a7417-a9de-3745-a187-a4c9b290776d | -22.23188 | -55.99897 | 2026-07-19 04:23:00 | NOAA-20 | ANTÔNIO JOÃO | MATO GROSSO DO SUL | Brasil | 5000906 | 50 | 33 | nan | nan | nan | Cerrado | 2.3 |
| b22bf21b-c2bb-3356-b29f-6aaaf41505d6 | -22.25824 | -55.96999 | 2026-07-19 04:23:00 | NOAA-20 | ANTÔNIO JOÃO | MATO GROSSO DO SUL | Brasil | 5000906 | 50 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 47361a04-7ac5-32a2-9009-cbb14e2e8c0b | -28.59097 | -53.62149 | 2026-07-19 04:23:00 | NOAA-20 | CRUZ ALTA | RIO GRANDE DO SUL | Brasil | 4306106 | 43 | 33 | nan | nan | nan | Mata Atlântica | 2.9 |
| 87d36410-604e-3f44-8c39-2578c2b07279 | -22.25336 | -55.96835 | 2026-07-19 04:23:00 | NOAA-20 | ANTÔNIO JOÃO | MATO GROSSO DO SUL | Brasil | 5000906 | 50 | 33 | nan | nan | nan | Cerrado | 2.2 |
| a11f1848-2f73-3b2b-8faa-89d49857c632 | -23.89217 | -51.75012 | 2026-07-19 04:23:00 | NOAA-20 | KALORÉ | PARANÁ | Brasil | 4113106 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| bc02b0bc-ef82-3bd5-9623-3e999e095fa0 | -23.72752 | -46.51947 | 2026-07-19 04:23:00 | NOAA-20 | SÃO BERNARDO DO CAMPO | SÃO PAULO | Brasil | 3548708 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| 6690ef91-6f5d-3fba-8ad1-5f793ee35a1b | -23.7281 | -46.51566 | 2026-07-19 04:23:00 | NOAA-20 | SANTO ANDRÉ | SÃO PAULO | Brasil | 3547809 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| ba9de5a1-2602-3b78-97d6-52583ae0bcf7 | -23.45404 | -47.22956 | 2026-07-19 04:23:00 | NOAA-20 | MAIRINQUE | SÃO PAULO | Brasil | 3528403 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| f8d50305-0002-3ba5-9cc4-8c3f6bd85c72 | -23.7615 | -53.27697 | 2026-07-19 04:23:00 | NOAA-20 | UMUARAMA | PARANÁ | Brasil | 4128104 | 41 | 33 | nan | nan | nan | Mata Atlântica | 15.0 |
| 9858beee-531f-38d9-b5d7-000cf53275fd | -23.76558 | -53.27801 | 2026-07-19 04:23:00 | NOAA-20 | UMUARAMA | PARANÁ | Brasil | 4128104 | 41 | 33 | nan | nan | nan | Mata Atlântica | 15.0 |
| 91a729a9-7e5c-3e41-849f-1426a620ca1a | -22.22696 | -55.99741 | 2026-07-19 04:23:00 | NOAA-20 | ANTÔNIO JOÃO | MATO GROSSO DO SUL | Brasil | 5000906 | 50 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 185efe09-0ff7-34b1-a1e3-b901ccc25f71 | -28.61222 | -49.2337 | 2026-07-19 04:23:00 | NOAA-20 | MORRO DA FUMAÇA | SANTA CATARINA | Brasil | 4211207 | 42 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| fd8c2eab-8e52-3287-9fda-45460cbcfb39 | -23.45794 | -47.22643 | 2026-07-19 04:23:00 | NOAA-20 | MAIRINQUE | SÃO PAULO | Brasil | 3528403 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| cce5a40c-7345-3f15-b08e-8d055f784aba | -21.99311 | -56.02034 | 2026-07-19 04:23:00 | NOAA-20 | PONTA PORÃ | MATO GROSSO DO SUL | Brasil | 5006606 | 50 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 32c346e8-d57b-34b9-851d-fce991431728 | -23.76231 | -53.27284 | 2026-07-19 04:23:00 | NOAA-20 | UMUARAMA | PARANÁ | Brasil | 4128104 | 41 | 33 | nan | nan | nan | Mata Atlântica | 15.0 |
| c602cf14-4484-364e-8407-6da5b0c539d7 | -29.0063 | -50.36952 | 2026-07-19 04:23:00 | NOAA-20 | JAQUIRANA | RIO GRANDE DO SUL | Brasil | 4311122 | 43 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 2d2eab8f-8542-34fb-a46f-1bfcbd6fb353 | -21.99238 | -56.02376 | 2026-07-19 04:23:00 | NOAA-20 | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 5.1 |
| f04a405b-d0a5-3ad5-bc7c-de7da533286c | -29.10622 | -50.61025 | 2026-07-19 04:23:00 | NOAA-20 | SÃO FRANCISCO DE PAULA | RIO GRANDE DO SUL | Brasil | 4318200 | 43 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| a0960764-8be7-31cb-af9f-64dc55eb2f37 | -23.70589 | -46.74926 | 2026-07-19 04:23:00 | NOAA-20 | SÃO PAULO | SÃO PAULO | Brasil | 3550308 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| c7bfa525-b01c-358b-8fde-7473f9a51c1c | -29.06949 | -50.72017 | 2026-07-19 04:23:00 | NOAA-20 | SÃO FRANCISCO DE PAULA | RIO GRANDE DO SUL | Brasil | 4318200 | 43 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| b8a5fb21-a83f-3861-bc81-dfe42219b4d5 | -22.25269 | -55.97141 | 2026-07-19 04:23:00 | NOAA-20 | ANTÔNIO JOÃO | MATO GROSSO DO SUL | Brasil | 5000906 | 50 | 33 | nan | nan | nan | Cerrado | 2.0 |
| c8d54bae-0c6b-327c-b958-8f52622c62d2 | -23.67371 | -46.89094 | 2026-07-19 04:23:00 | NOAA-20 | ITAPECERICA DA SERRA | SÃO PAULO | Brasil | 3522208 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.8 |
| 02b00fbb-6b90-3ead-8a7f-3953c6c5b801 | -21.99809 | -56.02174 | 2026-07-19 04:23:00 | NOAA-20 | PONTA PORÃ | MATO GROSSO DO SUL | Brasil | 5006606 | 50 | 33 | nan | nan | nan | Cerrado | 13.2 |
| fc3267c6-7db4-39b2-9718-993c4ef6dbea | -28.88698 | -50.92036 | 2026-07-19 04:23:00 | NOAA-20 | CAXIAS DO SUL | RIO GRANDE DO SUL | Brasil | 4305108 | 43 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| a26d8735-8551-3f94-80ed-f613846b8d40 | -22.00238 | -56.02637 | 2026-07-19 04:23:00 | NOAA-20 | PONTA PORÃ | MATO GROSSO DO SUL | Brasil | 5006606 | 50 | 33 | nan | nan | nan | Cerrado | 13.6 |
| 6421b713-2abe-32ac-a32e-53243231f66e | -29.96693 | -55.05085 | 2026-07-19 04:25:00 | NOAA-20 | CACEQUI | RIO GRANDE DO SUL | Brasil | 4302907 | 43 | 33 | nan | nan | nan | Pampa | 1.3 |
| 6d0db358-b8d9-3a42-b4f8-c5e4ea70b5b8 | -29.29972 | -50.21844 | 2026-07-19 04:25:00 | NOAA-20 | SÃO FRANCISCO DE PAULA | RIO GRANDE DO SUL | Brasil | 4318200 | 43 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| 645230e0-2b15-37ee-88d4-f8212cf77bb9 | -29.97449 | -55.01384 | 2026-07-19 04:25:00 | NOAA-20 | CACEQUI | RIO GRANDE DO SUL | Brasil | 4302907 | 43 | 33 | nan | nan | nan | Pampa | 1.1 |
| 2783ca76-1ef9-3959-9435-d50572c6f38e | -29.95654 | -55.03926 | 2026-07-19 04:25:00 | NOAA-20 | CACEQUI | RIO GRANDE DO SUL | Brasil | 4302907 | 43 | 33 | nan | nan | nan | Pampa | 1.2 |
| 92650439-2e20-30dc-b708-1a214a9a5024 | -30.41235 | -52.60745 | 2026-07-19 04:25:00 | NOAA-20 | ENCRUZILHADA DO SUL | RIO GRANDE DO SUL | Brasil | 4306908 | 43 | 33 | nan | nan | nan | Pampa | 3.5 |
| 76fd2ffa-43a7-3566-b09b-79de083896c9 | -29.9082 | -54.67638 | 2026-07-19 04:25:00 | NOAA-20 | CACEQUI | RIO GRANDE DO SUL | Brasil | 4302907 | 43 | 33 | nan | nan | nan | Pampa | 2.6 |
| 0093b5cb-f9ba-3af8-8d37-47aac706f4ea | -30.40878 | -52.6066 | 2026-07-19 04:25:00 | NOAA-20 | ENCRUZILHADA DO SUL | RIO GRANDE DO SUL | Brasil | 4306908 | 43 | 33 | nan | nan | nan | Pampa | 3.5 |
| 5dcf0530-ce98-3986-88f7-378ce813b525 | -29.96394 | -55.02387 | 2026-07-19 04:25:00 | NOAA-20 | CACEQUI | RIO GRANDE DO SUL | Brasil | 4302907 | 43 | 33 | nan | nan | nan | Pampa | 0.9 |
| efaf3695-da07-30dc-88aa-c08995725d25 | -29.96963 | -55.01682 | 2026-07-19 04:25:00 | NOAA-20 | CACEQUI | RIO GRANDE DO SUL | Brasil | 4302907 | 43 | 33 | nan | nan | nan | Pampa | 1.1 |
| 0018bb0f-ae89-3a90-9f49-842fd389b6ff | -29.01487 | -54.49914 | 2026-07-19 04:25:00 | NOAA-20 | CAPÃO DO CIPÓ | RIO GRANDE DO SUL | Brasil | 4304655 | 43 | 33 | nan | nan | nan | Pampa | 1.2 |
| a682e1c3-dbda-3fe8-97aa-7746f4dd8383 | -29.9688 | -55.02086 | 2026-07-19 04:25:00 | NOAA-20 | CACEQUI | RIO GRANDE DO SUL | Brasil | 4302907 | 43 | 33 | nan | nan | nan | Pampa | 1.3 |
| 7c31677e-5f25-314d-97ab-d1e307d82433 | -29.90921 | -54.6714 | 2026-07-19 04:25:00 | NOAA-20 | CACEQUI | RIO GRANDE DO SUL | Brasil | 4302907 | 43 | 33 | nan | nan | nan | Pampa | 3.4 |
| 13343d8f-aca1-343d-a48e-62c667ffa858 | -29.96478 | -55.01979 | 2026-07-19 04:25:00 | NOAA-20 | CACEQUI | RIO GRANDE DO SUL | Brasil | 4302907 | 43 | 33 | nan | nan | nan | Pampa | 0.9 |
| f324569a-95f7-31dd-9525-0b00a6810262 | -29.91214 | -54.67748 | 2026-07-19 04:25:00 | NOAA-20 | CACEQUI | RIO GRANDE DO SUL | Brasil | 4302907 | 43 | 33 | nan | nan | nan | Pampa | 1.1 |
| bc624552-b131-365a-ac89-ee9d64856043 | -29.2395 | -50.67318 | 2026-07-19 04:25:00 | NOAA-20 | SÃO FRANCISCO DE PAULA | RIO GRANDE DO SUL | Brasil | 4318200 | 43 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| c5e8027b-3193-352f-b45a-f6e786fd84b4 | -29.53989 | -53.73162 | 2026-07-19 04:25:00 | NOAA-20 | ITAARA | RIO GRANDE DO SUL | Brasil | 4310538 | 43 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| f7c7fbe0-ae0b-3cf2-8886-32f25cae05e1 | -29.53884 | -53.73695 | 2026-07-19 04:25:00 | NOAA-20 | ITAARA | RIO GRANDE DO SUL | Brasil | 4310538 | 43 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 72235c5a-2b77-3372-b473-2cf50c1e5285 | -29.96374 | -55.04564 | 2026-07-19 04:25:00 | NOAA-20 | CACEQUI | RIO GRANDE DO SUL | Brasil | 4302907 | 43 | 33 | nan | nan | nan | Pampa | 1.3 |
| d862f7c8-860b-3fbb-95be-b7575880b1fa | -29.54721 | -51.39039 | 2026-07-19 04:25:00 | NOAA-20 | HARMONIA | RIO GRANDE DO SUL | Brasil | 4309555 | 43 | 33 | nan | nan | nan | Mata Atlântica | 11.3 |
| 7e0fd563-08fb-3025-8933-8ffc3d14c20f | -29.97046 | -55.01277 | 2026-07-19 04:25:00 | NOAA-20 | CACEQUI | RIO GRANDE DO SUL | Brasil | 4302907 | 43 | 33 | nan | nan | nan | Pampa | 1.1 |
| 8c93832b-ffd2-3233-9eb1-36a3d787fc0b | -30.39363 | -52.60799 | 2026-07-19 04:25:00 | NOAA-20 | ENCRUZILHADA DO SUL | RIO GRANDE DO SUL | Brasil | 4306908 | 43 | 33 | nan | nan | nan | Pampa | 1.9 |
| f4e15a66-191e-367d-baa3-e8e4a4dfa466 | -13.6764 | -48.7786 | 2026-07-19 04:30:00 | GOES-19 | FORMOSO | GOIÁS | Brasil | 5208103 | 52 | 33 | nan | nan | nan | Cerrado | 73.5 |
| 659b3cc3-11da-3fd4-9404-03fab510f56c | -10.6904 | -46.6256 | 2026-07-19 04:40:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 58.5 |
| 73a9099e-2816-3695-a21d-d7f67c2cb15b | -13.6764 | -48.7786 | 2026-07-19 04:40:00 | GOES-19 | FORMOSO | GOIÁS | Brasil | 5208103 | 52 | 33 | nan | nan | nan | Cerrado | 62.0 |
| 0b726eb1-0d75-32e6-857d-b11bfcb2591d | -13.6764 | -48.7786 | 2026-07-19 04:50:00 | GOES-19 | FORMOSO | GOIÁS | Brasil | 5208103 | 52 | 33 | nan | nan | nan | Cerrado | 66.2 |
| e6d18c18-e8de-3943-9474-4fddaa1a7e7e | -13.6764 | -48.7786 | 2026-07-19 05:00:00 | GOES-19 | FORMOSO | GOIÁS | Brasil | 5208103 | 52 | 33 | nan | nan | nan | Cerrado | 60.8 |


[Clique aqui para ver as próximas entradas](README9.md)
