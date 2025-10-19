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

## Dados Diários - Página 52

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 3235c832-edb6-3ce6-a7b8-19bbe62c370a | -7.17087 | -46.3995 | 2025-10-19 04:32:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| ca3f3977-4011-3d0a-a292-52eeee046a1a | -10.9545 | -45.4649 | 2025-10-19 04:32:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 3fa9fafe-9416-3f5a-bb45-3eac0fbfc29b | -10.92043 | -60.93493 | 2025-10-19 04:34:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b5df4673-3e8c-33dc-a27c-4b43cc116950 | -13.71536 | -40.98517 | 2025-10-19 04:34:00 | NOAA-20 | BARRA DA ESTIVA | BAHIA | Brasil | 2902807 | 29 | 33 | nan | nan | nan | Caatinga | 0.5 |
| b87dffc3-6777-36c1-a831-5cd4ce1ddf60 | -14.1095 | -44.08337 | 2025-10-19 04:34:00 | NOAA-20 | FEIRA DA MATA | BAHIA | Brasil | 2910776 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 378f884f-6bc3-3df6-9584-a0000b599c14 | -15.27368 | -46.01281 | 2025-10-19 04:34:00 | NOAA-20 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 7287977c-103d-39a0-b989-bfff9906f0f9 | -10.92678 | -60.93628 | 2025-10-19 04:34:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| fea85388-6b1a-301b-ade9-a99c2393ea2d | -15.51427 | -41.67444 | 2025-10-19 04:34:00 | NOAA-20 | ÁGUAS VERMELHAS | MINAS GERAIS | Brasil | 3101003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| 58a7eedc-e917-3743-bb3e-34c9914eda3a | -13.62159 | -44.10444 | 2025-10-19 04:34:00 | NOAA-20 | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 0ff1cd84-de39-34ca-9d2a-8aa41b9467b0 | -11.75278 | -61.07717 | 2025-10-19 04:34:00 | NOAA-20 | PIMENTA BUENO | RONDÔNIA | Brasil | 1100189 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2cc112ad-9c2a-3311-834e-c4ed681cbaac | -16.82298 | -41.79717 | 2025-10-19 04:34:00 | NOAA-20 | ARAÇUAÍ | MINAS GERAIS | Brasil | 3103405 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 8365c4a0-d572-3561-a4bd-c6169749f7ad | -15.78119 | -43.25121 | 2025-10-19 04:34:00 | NOAA-20 | NOVA PORTEIRINHA | MINAS GERAIS | Brasil | 3145059 | 31 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 0d012f8c-22f6-3176-9c49-95b8b50cd648 | -13.88961 | -45.51421 | 2025-10-19 04:34:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 53f6e8da-5f5c-303b-8647-bf25c8ba7e5b | -15.2597 | -43.58744 | 2025-10-19 04:34:00 | NOAA-20 | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 137b4606-2842-32c5-ab37-e7a82dacf4ba | -10.92571 | -60.94162 | 2025-10-19 04:34:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| a3434805-29e9-3429-97ea-de6896318c93 | -12.99109 | -47.2855 | 2025-10-19 04:34:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 1adbab4a-80a9-331c-8aef-79982f2f1ad2 | -10.92463 | -60.94699 | 2025-10-19 04:34:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 18bb03ab-a31e-3ecd-96f9-b64c0bb6a8e1 | -13.89644 | -43.4534 | 2025-10-19 04:34:00 | NOAA-20 | MALHADA | BAHIA | Brasil | 2920205 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 9892891e-f8af-3799-955a-3e0167c101f5 | -13.71036 | -40.9844 | 2025-10-19 04:34:00 | NOAA-20 | BARRA DA ESTIVA | BAHIA | Brasil | 2902807 | 29 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 7a06d3d2-08c0-35fa-94f0-f05207a94b90 | -15.6912 | -45.34566 | 2025-10-19 04:34:00 | NOAA-20 | CHAPADA GAÚCHA | MINAS GERAIS | Brasil | 3116159 | 31 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 3641f45f-4606-3d75-a11e-47e4689af13a | -13.60591 | -43.11453 | 2025-10-19 04:34:00 | NOAA-20 | RIACHO DE SANTANA | BAHIA | Brasil | 2926400 | 29 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 4781cbea-035e-3845-81ff-d3e76525bfa1 | -13.53417 | -43.01106 | 2025-10-19 04:34:00 | NOAA-20 | RIACHO DE SANTANA | BAHIA | Brasil | 2926400 | 29 | 33 | nan | nan | nan | Caatinga | 22.8 |
| 61490471-de16-34b1-84fd-730a329b6bea | -16.14719 | -41.14935 | 2025-10-19 04:34:00 | NOAA-20 | JEQUITINHONHA | MINAS GERAIS | Brasil | 3135803 | 31 | 33 | nan | nan | nan | Mata Atlântica | 6.3 |
| 8c7fab63-9195-3989-a7a0-0570c626bb19 | -15.48902 | -41.33579 | 2025-10-19 04:34:00 | NOAA-20 | CÂNDIDO SALES | BAHIA | Brasil | 2906709 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 70d2ecb9-d47e-355b-b9f3-664c4c4b028b | -16.76558 | -42.77885 | 2025-10-19 04:34:00 | NOAA-20 | CRISTÁLIA | MINAS GERAIS | Brasil | 3120300 | 31 | 33 | nan | nan | nan | Cerrado | 25.1 |
| cdf4decd-c831-3236-b936-7709d2b52f4a | -13.90571 | -45.53541 | 2025-10-19 04:34:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 48fc7489-4da6-3fc1-b2fb-55a92be69aab | -12.98993 | -47.26987 | 2025-10-19 04:34:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| bf733cc5-1b15-340d-802b-505b09e3165a | -16.81097 | -42.82978 | 2025-10-19 04:34:00 | NOAA-20 | CRISTÁLIA | MINAS GERAIS | Brasil | 3120300 | 31 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 7ed52536-ce0f-3e9b-9081-919682632f13 | -16.77607 | -42.77018 | 2025-10-19 04:34:00 | NOAA-20 | CRISTÁLIA | MINAS GERAIS | Brasil | 3120300 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 19a708a4-9be0-3d7d-8e74-331572815ce4 | -15.44627 | -45.91739 | 2025-10-19 04:34:00 | NOAA-20 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 0d524bd2-31a6-3441-a12c-80c0c1c771eb | -12.98767 | -47.28495 | 2025-10-19 04:34:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 6f96165f-b3bf-306b-ab2f-35c1ffcbbe28 | -13.02552 | -46.95912 | 2025-10-19 04:34:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| cf0e862a-eabe-31a8-9f91-7d7441888228 | -15.78512 | -43.25587 | 2025-10-19 04:34:00 | NOAA-20 | NOVA PORTEIRINHA | MINAS GERAIS | Brasil | 3145059 | 31 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 48f7afaa-faed-3519-8359-bbd1a09e0f3e | -16.97882 | -41.15402 | 2025-10-19 04:34:00 | NOAA-20 | JOAÍMA | MINAS GERAIS | Brasil | 3136009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| b05f9bb9-7801-3b26-b989-babfa5f65c15 | -13.04113 | -47.27837 | 2025-10-19 04:34:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 6b1bafd0-df82-366f-8924-c270f9411f09 | -15.4469 | -45.91282 | 2025-10-19 04:34:00 | NOAA-20 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 4a1afc29-0538-3327-8d2b-498c78fa9640 | -14.28184 | -42.33389 | 2025-10-19 04:34:00 | NOAA-20 | IBIASSUCÊ | BAHIA | Brasil | 2912004 | 29 | 33 | nan | nan | nan | Caatinga | 5.0 |
| be4dc46f-8013-3ba6-aac5-618f99a887de | -12.98365 | -47.26501 | 2025-10-19 04:34:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 27e04386-eb10-3864-bb0f-bd34a5242a24 | -15.18931 | -43.57019 | 2025-10-19 04:34:00 | NOAA-20 | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 6cf29865-c5d4-36ef-a0d6-0a58ee1d8b2b | -10.93314 | -60.93764 | 2025-10-19 04:34:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| c51eaf3d-1fc7-3f3f-b850-ec07f67c6810 | -16.75574 | -42.7824 | 2025-10-19 04:34:00 | NOAA-20 | CRISTÁLIA | MINAS GERAIS | Brasil | 3120300 | 31 | 33 | nan | nan | nan | Cerrado | 33.6 |
| ca857d1f-6a17-38cd-ada4-26a5934040a1 | -15.01408 | -40.45985 | 2025-10-19 04:34:00 | NOAA-20 | CAATIBA | BAHIA | Brasil | 2904803 | 29 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 1cbcff73-38d2-3062-b27e-8cb57d188ec3 | -12.98538 | -47.27687 | 2025-10-19 04:34:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 164a8da4-9f8c-3aeb-bfcf-dc715b186d03 | -16.78195 | -42.76067 | 2025-10-19 04:34:00 | NOAA-20 | CRISTÁLIA | MINAS GERAIS | Brasil | 3120300 | 31 | 33 | nan | nan | nan | Cerrado | 3.5 |
| ce7d2292-d6c9-3305-9aed-96d2eab06181 | -13.90198 | -45.53483 | 2025-10-19 04:34:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 354a4f26-5678-3368-a127-2e0a3cf81834 | -15.43266 | -45.84261 | 2025-10-19 04:34:00 | NOAA-20 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 1e22026d-c40f-3d50-ad1a-27d044c96c7d | -16.14429 | -41.15318 | 2025-10-19 04:34:00 | NOAA-20 | JEQUITINHONHA | MINAS GERAIS | Brasil | 3135803 | 31 | 33 | nan | nan | nan | Mata Atlântica | 6.6 |
| f00d932b-70f1-35ae-b2f9-39c7308317c6 | -16.82145 | -41.80119 | 2025-10-19 04:34:00 | NOAA-20 | ARAÇUAÍ | MINAS GERAIS | Brasil | 3103405 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.6 |
| 9c45c24f-7c84-398e-9f5a-dc8a1eaeec39 | -15.79713 | -43.65356 | 2025-10-19 04:34:00 | NOAA-20 | SÃO JOÃO DA PONTE | MINAS GERAIS | Brasil | 3162401 | 31 | 33 | nan | nan | nan | Cerrado | 3.5 |
| c31d6222-1bbd-32d5-862b-7bab7239e09c | -14.23393 | -51.42467 | 2025-10-19 04:34:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 508c8710-44bd-3a7c-a28e-1cb2ac2e3467 | -16.76959 | -42.78461 | 2025-10-19 04:34:00 | NOAA-20 | CRISTÁLIA | MINAS GERAIS | Brasil | 3120300 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| c5f29ddb-31d1-329f-a952-8a0f489a458c | -15.6895 | -42.5891 | 2025-10-19 04:34:00 | NOAA-20 | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Cerrado | 2.9 |
| a6f4b3ec-fd2e-3f7f-9e8f-da8e47d5e12b | -10.9342 | -60.93235 | 2025-10-19 04:34:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 8e2b548e-bd21-38a0-9e8b-8f3199201d57 | -13.53473 | -43.00682 | 2025-10-19 04:34:00 | NOAA-20 | RIACHO DE SANTANA | BAHIA | Brasil | 2926400 | 29 | 33 | nan | nan | nan | Caatinga | 22.8 |
| 020b3e76-08cf-3c93-b6f3-4a5582242bfd | -15.25486 | -43.59101 | 2025-10-19 04:34:00 | NOAA-20 | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d068beae-1e0e-30a0-800d-e93db2b32f60 | -13.61139 | -43.96764 | 2025-10-19 04:34:00 | NOAA-20 | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 6d156df8-2ca0-31d7-8040-ade4a6df8aa9 | -13.18806 | -46.44102 | 2025-10-19 04:34:00 | NOAA-20 | DIVINÓPOLIS DE GOIÁS | GOIÁS | Brasil | 5208301 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 4d2336e3-ff7f-3483-b8a8-5f31b2455f2b | -15.51042 | -41.54053 | 2025-10-19 04:34:00 | NOAA-20 | NINHEIRA | MINAS GERAIS | Brasil | 3144656 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| f881867e-a781-30b2-9210-212a2c14fd6e | -14.30014 | -44.01733 | 2025-10-19 04:34:00 | NOAA-20 | JUVENÍLIA | MINAS GERAIS | Brasil | 3136959 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 6afa506f-6b7e-3e7a-9f4a-7d3d875e89ba | -13.18101 | -46.43981 | 2025-10-19 04:34:00 | NOAA-20 | DIVINÓPOLIS DE GOIÁS | GOIÁS | Brasil | 5208301 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| dd6992a7-5064-33ca-8120-88ae07ec0354 | -14.13509 | -44.68849 | 2025-10-19 04:34:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 4cf02e84-c07a-3da9-8422-519e45c74a8e | -14.28248 | -42.32897 | 2025-10-19 04:34:00 | NOAA-20 | IBIASSUCÊ | BAHIA | Brasil | 2912004 | 29 | 33 | nan | nan | nan | Caatinga | 3.3 |
| ec275db2-9866-3c29-8664-d00dbddf506c | -14.30426 | -44.01793 | 2025-10-19 04:34:00 | NOAA-20 | JUVENÍLIA | MINAS GERAIS | Brasil | 3136959 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c332157a-2e87-3ca5-a594-437a245caefa | -15.78562 | -43.25183 | 2025-10-19 04:34:00 | NOAA-20 | NOVA PORTEIRINHA | MINAS GERAIS | Brasil | 3145059 | 31 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 329223a8-8735-3406-8be0-c005f2f6d682 | -14.18817 | -44.79761 | 2025-10-19 04:34:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 60f4a700-797c-3921-8f00-2a1b208cec74 | -12.98651 | -47.26933 | 2025-10-19 04:34:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 90741391-6b2b-3c47-bc43-7f6c76b36ab7 | -13.84229 | -43.72913 | 2025-10-19 04:34:00 | NOAA-20 | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| e07f4e26-4b08-3383-83a2-14783d08a89c | -14.47069 | -43.34606 | 2025-10-19 04:34:00 | NOAA-20 | PALMAS DE MONTE ALTO | BAHIA | Brasil | 2923407 | 29 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 263e4539-7da5-3d7e-8d0b-75f327bc9546 | -16.14395 | -41.15627 | 2025-10-19 04:34:00 | NOAA-20 | JEQUITINHONHA | MINAS GERAIS | Brasil | 3135803 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.0 |
| 553418a4-9de5-38ce-a37e-87234e3c5bc3 | -14.2271 | -51.42348 | 2025-10-19 04:34:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 10.5 |
| c7a5c602-26f2-32bd-a8a0-710eed262e65 | -13.18747 | -46.44505 | 2025-10-19 04:34:00 | NOAA-20 | DIVINÓPOLIS DE GOIÁS | GOIÁS | Brasil | 5208301 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| fcd57c55-2c68-31bd-97ee-aa1dd2fe1d5c | -13.01973 | -46.95039 | 2025-10-19 04:34:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c52a374c-aca2-3a7e-ab27-5fdb2d26f935 | -15.77848 | -41.33995 | 2025-10-19 04:34:00 | NOAA-20 | DIVISA ALEGRE | MINAS GERAIS | Brasil | 3122355 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| eed68ed5-c43f-3a5d-8df3-3790b6955641 | -16.81159 | -42.82484 | 2025-10-19 04:34:00 | NOAA-20 | CRISTÁLIA | MINAS GERAIS | Brasil | 3120300 | 31 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 735d09db-f678-3129-93e6-873d8461b3e6 | -16.97813 | -41.15995 | 2025-10-19 04:34:00 | NOAA-20 | JOAÍMA | MINAS GERAIS | Brasil | 3136009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.9 |
| 57173844-51b7-36e8-823f-55e15c121bbd | -13.89954 | -45.52509 | 2025-10-19 04:34:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 88485fdf-7b52-3823-8a4f-6407f8792df8 | -16.7702 | -42.77964 | 2025-10-19 04:34:00 | NOAA-20 | CRISTÁLIA | MINAS GERAIS | Brasil | 3120300 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 78f04b7d-0823-31be-82df-221a8136edaf | -13.18454 | -46.44043 | 2025-10-19 04:34:00 | NOAA-20 | DIVINÓPOLIS DE GOIÁS | GOIÁS | Brasil | 5208301 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 04ba7a70-43c0-30f4-8740-18994493af16 | -16.81033 | -41.00338 | 2025-10-19 04:34:00 | NOAA-20 | JOAÍMA | MINAS GERAIS | Brasil | 3136009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 8bd0afe5-b0fe-3e3f-bf52-d5ef9c3ef3b6 | -15.52821 | -45.3448 | 2025-10-19 04:34:00 | NOAA-20 | CHAPADA GAÚCHA | MINAS GERAIS | Brasil | 3116159 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 3e82dead-d7aa-3307-a566-20a9a77bc969 | -14.18833 | -44.7953 | 2025-10-19 04:34:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| db4b3b84-901c-351e-ad73-906754c542ad | -15.7896 | -43.64394 | 2025-10-19 04:34:00 | NOAA-20 | CAPITÃO ENÉAS | MINAS GERAIS | Brasil | 3112703 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 1ca276a8-1eb8-362d-af8b-f6b839c6e5e0 | -16.80971 | -41.0024 | 2025-10-19 04:34:00 | NOAA-20 | JOAÍMA | MINAS GERAIS | Brasil | 3136009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| dc076e12-932d-3a55-a7ae-21f35fee46c5 | -13.86543 | -45.46088 | 2025-10-19 04:34:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 6a63a397-a79e-354d-98e4-76841285a59e | -15.79768 | -43.64935 | 2025-10-19 04:34:00 | NOAA-20 | SÃO JOÃO DA PONTE | MINAS GERAIS | Brasil | 3162401 | 31 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 3c81b34d-314f-3cdc-b83a-07ce4e6eba13 | -16.76036 | -42.78312 | 2025-10-19 04:34:00 | NOAA-20 | CRISTÁLIA | MINAS GERAIS | Brasil | 3120300 | 31 | 33 | nan | nan | nan | Cerrado | 19.2 |
| c08f1c96-24e0-3586-b1b7-b82750ac4a6b | -16.78381 | -42.82164 | 2025-10-19 04:34:00 | NOAA-20 | CRISTÁLIA | MINAS GERAIS | Brasil | 3120300 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b1ef742b-2206-3462-9889-50af71187881 | -15.78674 | -43.24997 | 2025-10-19 04:34:00 | NOAA-20 | NOVA PORTEIRINHA | MINAS GERAIS | Brasil | 3145059 | 31 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 5cd2d8fa-42e7-3d53-9dbb-81c7423868f6 | -15.3249 | -41.74041 | 2025-10-19 04:34:00 | NOAA-20 | NINHEIRA | MINAS GERAIS | Brasil | 3144656 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| f04041d9-0caf-3a07-8281-6b438f2d6adc | -13.9879 | -44.09281 | 2025-10-19 04:34:00 | NOAA-20 | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| cf31a51a-903b-3857-85c9-3961909031b1 | -15.79014 | -43.63971 | 2025-10-19 04:34:00 | NOAA-20 | CAPITÃO ENÉAS | MINAS GERAIS | Brasil | 3112703 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| bf0ab6e8-2050-3e13-9c6e-1739fac1e739 | -13.02957 | -46.95559 | 2025-10-19 04:34:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 4c650505-d733-344a-b7b7-e577b4c35f99 | -13.02261 | -46.95486 | 2025-10-19 04:34:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| fd4c4181-6c44-374b-a62c-80137c8aa533 | -12.99334 | -47.27041 | 2025-10-19 04:34:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| ddd89e17-e93c-360e-ad76-a4a2d06f89f8 | -12.9888 | -47.27742 | 2025-10-19 04:34:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 21076b5e-6c18-3888-9bee-5c706dd6df11 | -16.14683 | -41.15234 | 2025-10-19 04:34:00 | NOAA-20 | JEQUITINHONHA | MINAS GERAIS | Brasil | 3135803 | 31 | 33 | nan | nan | nan | Mata Atlântica | 6.3 |
| a792ebc3-bc60-3261-b64c-d90077981663 | -16.78134 | -42.76565 | 2025-10-19 04:34:00 | NOAA-20 | CRISTÁLIA | MINAS GERAIS | Brasil | 3120300 | 31 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 06733519-e88e-34c1-bc2d-c68184f8accb | -14.13903 | -44.68904 | 2025-10-19 04:34:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d0b58d0a-b09b-3a33-8a32-a393a0c4cb38 | -14.90168 | -44.11048 | 2025-10-19 04:34:00 | NOAA-20 | SÃO JOÃO DAS MISSÕES | MINAS GERAIS | Brasil | 3162450 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| d9d40a44-0acc-3a33-b935-6de2b191e0af | -13.0474 | -47.25998 | 2025-10-19 04:34:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |


[Clique aqui para ver as próximas entradas](README53.md)
