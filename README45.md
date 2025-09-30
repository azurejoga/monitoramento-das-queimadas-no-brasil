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

## Dados Diários - Página 45

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 1b82d4d4-81bd-3154-bb37-47081fed6c23 | -21.04191 | -45.68572 | 2025-09-30 03:51:00 | NOAA-20 | BOA ESPERANÇA | MINAS GERAIS | Brasil | 3107109 | 31 | 33 | nan | nan | nan | Cerrado | 4.5 |
| b2310cf8-8284-32bb-8e8a-7b55440bcbbc | -21.40878 | -43.89629 | 2025-09-30 03:51:00 | NOAA-20 | IBERTIOGA | MINAS GERAIS | Brasil | 3129400 | 31 | 33 | nan | nan | nan | Mata Atlântica | 7.2 |
| 7d3f88c1-df85-38ab-8c52-6e9e7ed7fbfb | -21.21751 | -44.06519 | 2025-09-30 03:51:00 | NOAA-20 | SÃO JOÃO DEL REI | MINAS GERAIS | Brasil | 3162500 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.3 |
| a79ad85e-4380-3f22-8ce2-49b7c5ce7d12 | -20.61723 | -46.18175 | 2025-09-30 03:51:00 | NOAA-20 | CAPITÓLIO | MINAS GERAIS | Brasil | 3112802 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 49681d93-b133-3129-9675-c671513a1b59 | -20.42183 | -43.35879 | 2025-09-30 03:51:00 | NOAA-20 | MARIANA | MINAS GERAIS | Brasil | 3140001 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| e5675499-7c01-33cd-a548-8e6f6ff7c25a | -22.58506 | -46.79567 | 2025-09-30 03:51:00 | NOAA-20 | AMPARO | SÃO PAULO | Brasil | 3501905 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| b1025b2d-c1c5-30a4-8d11-083ae8c58eaf | -20.91186 | -46.39357 | 2025-09-30 03:51:00 | NOAA-20 | ALPINÓPOLIS | MINAS GERAIS | Brasil | 3101904 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| ec99d08c-5ee9-3fb3-b5b9-53b45073c814 | -23.56161 | -47.55526 | 2025-09-30 03:51:00 | NOAA-20 | SOROCABA | SÃO PAULO | Brasil | 3552205 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.7 |
| 0d47fbc2-2b36-363f-b6a4-90d88dc80132 | -20.23026 | -41.34333 | 2025-09-30 03:51:00 | NOAA-20 | BREJETUBA | ESPÍRITO SANTO | Brasil | 3201159 | 32 | 33 | nan | nan | nan | Mata Atlântica | 4.6 |
| d355cfaa-0885-3c18-a5a7-40c5e1f1d995 | -19.86165 | -44.55657 | 2025-09-30 03:51:00 | NOAA-20 | PARÁ DE MINAS | MINAS GERAIS | Brasil | 3147105 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 94384687-d3a9-31ba-948b-008c01dc9248 | -21.4135 | -45.69874 | 2025-09-30 03:51:00 | NOAA-20 | CAMPOS GERAIS | MINAS GERAIS | Brasil | 3111606 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| f3c75f8b-4d42-360e-9164-475638fc5f81 | -21.04115 | -45.68964 | 2025-09-30 03:51:00 | NOAA-20 | BOA ESPERANÇA | MINAS GERAIS | Brasil | 3107109 | 31 | 33 | nan | nan | nan | Cerrado | 4.5 |
| f0c24111-4202-3055-98f7-6f378e433ac1 | -23.15512 | -45.72947 | 2025-09-30 03:51:00 | NOAA-20 | CAÇAPAVA | SÃO PAULO | Brasil | 3508504 | 35 | 33 | nan | nan | nan | Mata Atlântica | 4.1 |
| 2da4a3f8-0ffa-35ba-97a3-022d292e8ddb | -21.32092 | -42.87461 | 2025-09-30 03:51:00 | NOAA-20 | ASTOLFO DUTRA | MINAS GERAIS | Brasil | 3104601 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.9 |
| 8a964451-02f7-3127-b5d6-c7bde723be33 | -20.046 | -41.3303 | 2025-09-30 03:51:00 | NOAA-20 | MUTUM | MINAS GERAIS | Brasil | 3144003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| f40759e7-e793-3078-a365-b51584725363 | -19.85017 | -43.80846 | 2025-09-30 03:51:00 | NOAA-20 | SABARÁ | MINAS GERAIS | Brasil | 3156700 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.2 |
| f30d5d0d-948e-387b-b9fc-0a77ffb438cb | -23.22469 | -49.41521 | 2025-09-30 03:51:00 | NOAA-20 | PIRAJU | SÃO PAULO | Brasil | 3538808 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| c0d5ae6b-a3d9-392d-b864-838a4b129571 | -19.71406 | -45.88638 | 2025-09-30 03:51:00 | NOAA-20 | LUZ | MINAS GERAIS | Brasil | 3138807 | 31 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 703ea969-d989-39c2-ba3f-a553e8b16ee4 | -22.06668 | -45.64399 | 2025-09-30 03:51:00 | NOAA-20 | CAREAÇU | MINAS GERAIS | Brasil | 3113602 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 6c710abb-b159-3bef-8f1e-f2a3a85a669c | -20.61321 | -46.06791 | 2025-09-30 03:51:00 | NOAA-20 | CAPITÓLIO | MINAS GERAIS | Brasil | 3112802 | 31 | 33 | nan | nan | nan | Cerrado | 5.6 |
| d4675d01-5c08-39e5-bd88-9051a7bc8c24 | -19.86923 | -42.59454 | 2025-09-30 03:51:00 | NOAA-20 | DIONÍSIO | MINAS GERAIS | Brasil | 3121803 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.9 |
| d51d02c8-f04e-3aaf-b5e9-10770015cf5e | -19.86454 | -44.56265 | 2025-09-30 03:51:00 | NOAA-20 | PARÁ DE MINAS | MINAS GERAIS | Brasil | 3147105 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.3 |
| 063d3ec4-c16a-3b6b-8550-0ed830dd9edf | -23.32804 | -46.86554 | 2025-09-30 03:51:00 | NOAA-20 | CAJAMAR | SÃO PAULO | Brasil | 3509205 | 35 | 33 | nan | nan | nan | Mata Atlântica | 4.6 |
| 9d83ca45-2fb2-3262-8fbd-1f2b588a57cb | -22.76286 | -45.78588 | 2025-09-30 03:51:00 | NOAA-20 | SAPUCAÍ-MIRIM | MINAS GERAIS | Brasil | 3165404 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| ccddbbcd-a913-3b63-985f-8950701ca757 | -21.89405 | -45.75417 | 2025-09-30 03:51:00 | NOAA-20 | TURVOLÂNDIA | MINAS GERAIS | Brasil | 3169802 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 361d41ed-2b18-3214-abef-66cdedbe03fb | -20.74321 | -47.14223 | 2025-09-30 03:51:00 | NOAA-20 | SÃO TOMÁS DE AQUINO | MINAS GERAIS | Brasil | 3165107 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 93bd331f-d429-3a29-a913-44d5789f7fe0 | -23.15408 | -45.73491 | 2025-09-30 03:51:00 | NOAA-20 | CAÇAPAVA | SÃO PAULO | Brasil | 3508504 | 35 | 33 | nan | nan | nan | Mata Atlântica | 4.1 |
| 250e47ff-d69b-3793-a012-7655c7479e93 | -19.94482 | -41.64433 | 2025-09-30 03:51:00 | NOAA-20 | CONCEIÇÃO DE IPANEMA | MINAS GERAIS | Brasil | 3117405 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| 680f99aa-1aff-3ea4-8afe-aead2b03f5c1 | -22.51438 | -44.60857 | 2025-09-30 03:51:00 | NOAA-20 | ITATIAIA | RIO DE JANEIRO | Brasil | 3302254 | 33 | 33 | nan | nan | nan | Mata Atlântica | 27.7 |
| ffecd1e4-8865-394c-b87f-7d4efb6c76f6 | -19.52616 | -43.902 | 2025-09-30 03:51:00 | NOAA-20 | JABOTICATUBAS | MINAS GERAIS | Brasil | 3134608 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 07b326ca-cca3-3d30-9ace-cada8362dc1c | -20.05969 | -46.79487 | 2025-09-30 03:51:00 | NOAA-20 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| cec73779-490e-397b-9415-af4df0328f82 | -19.85679 | -43.81461 | 2025-09-30 03:51:00 | NOAA-20 | SABARÁ | MINAS GERAIS | Brasil | 3156700 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| 50218af3-2884-316f-8eb5-6c34605cf730 | -23.46561 | -47.75555 | 2025-09-30 03:51:00 | NOAA-20 | CAPELA DO ALTO | SÃO PAULO | Brasil | 3510302 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| c9fa7b3f-0e32-3af4-ba54-5b2b631535cb | -20.04407 | -41.97268 | 2025-09-30 03:51:00 | NOAA-20 | SANTANA DO MANHUAÇU | MINAS GERAIS | Brasil | 3158904 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 4194c4e7-a9ee-351d-a5a7-1faac69806cc | -21.31755 | -46.7546 | 2025-09-30 03:51:00 | NOAA-20 | GUAXUPÉ | MINAS GERAIS | Brasil | 3128709 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| c46f4899-bc39-3a6c-b831-f1a22e252a56 | -22.51904 | -44.60421 | 2025-09-30 03:51:00 | NOAA-20 | ITATIAIA | RIO DE JANEIRO | Brasil | 3302254 | 33 | 33 | nan | nan | nan | Mata Atlântica | 27.7 |
| 471f1909-15bd-3ab4-8153-003466829d9c | -21.26175 | -43.85494 | 2025-09-30 03:51:00 | NOAA-20 | BARBACENA | MINAS GERAIS | Brasil | 3105608 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 415d288b-0c88-3418-b287-bc5e43f41f5e | -19.22577 | -45.81784 | 2025-09-30 03:51:00 | NOAA-20 | SÃO GOTARDO | MINAS GERAIS | Brasil | 3162104 | 31 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 3a19613c-edda-3594-9b6d-c44d97c754b2 | -19.58654 | -43.86927 | 2025-09-30 03:51:00 | NOAA-20 | LAGOA SANTA | MINAS GERAIS | Brasil | 3137601 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 564bf9e2-6948-3085-b10e-4529bc1e5a30 | -21.04267 | -45.6818 | 2025-09-30 03:51:00 | NOAA-20 | BOA ESPERANÇA | MINAS GERAIS | Brasil | 3107109 | 31 | 33 | nan | nan | nan | Cerrado | 3.6 |
| e7c54431-46b2-3447-84ce-6c2dab64a6ab | -20.61808 | -46.17744 | 2025-09-30 03:51:00 | NOAA-20 | CAPITÓLIO | MINAS GERAIS | Brasil | 3112802 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| cfa3fe55-9a60-3ee3-8f16-0a967f10d108 | -19.84934 | -43.81317 | 2025-09-30 03:51:00 | NOAA-20 | SABARÁ | MINAS GERAIS | Brasil | 3156700 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.2 |
| 7a347d12-9c31-325e-b6cb-5569ed904f45 | -23.16007 | -45.72489 | 2025-09-30 03:51:00 | NOAA-20 | CAÇAPAVA | SÃO PAULO | Brasil | 3508504 | 35 | 33 | nan | nan | nan | Mata Atlântica | 4.6 |
| 8705037f-afc6-382f-9fbf-697ba193c2e1 | -20.60824 | -46.07111 | 2025-09-30 03:51:00 | NOAA-20 | CAPITÓLIO | MINAS GERAIS | Brasil | 3112802 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 683a4b82-0235-37ef-8ceb-65cd99436af7 | -20.55882 | -46.28246 | 2025-09-30 03:51:00 | NOAA-20 | CAPITÓLIO | MINAS GERAIS | Brasil | 3112802 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 2bfc2591-46cb-36e1-b8bd-d38195f87c4c | -20.6156 | -46.19004 | 2025-09-30 03:51:00 | NOAA-20 | CAPITÓLIO | MINAS GERAIS | Brasil | 3112802 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 13111e6a-f84c-3e54-93b7-bd8653864ad0 | -20.73037 | -45.27131 | 2025-09-30 03:51:00 | NOAA-20 | CANDEIAS | MINAS GERAIS | Brasil | 3112000 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 46bc06a6-9e97-3e0a-9e72-5a2399112cf8 | -19.85466 | -43.8106 | 2025-09-30 03:51:00 | NOAA-20 | SABARÁ | MINAS GERAIS | Brasil | 3156700 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.0 |
| 6783739d-fec5-3846-bb25-3c9413bbd4c3 | -22.93178 | -42.4309 | 2025-09-30 03:51:00 | NOAA-20 | SAQUAREMA | RIO DE JANEIRO | Brasil | 3305505 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| e3315577-1e79-373d-9879-b0624315f629 | -19.85307 | -43.81382 | 2025-09-30 03:51:00 | NOAA-20 | SABARÁ | MINAS GERAIS | Brasil | 3156700 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| b070d670-7062-39a1-85de-e2032e91a938 | -20.39882 | -43.67923 | 2025-09-30 03:51:00 | NOAA-20 | OURO PRETO | MINAS GERAIS | Brasil | 3146107 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.7 |
| c0b8be43-497c-3ac9-8906-d85ecb551b39 | -22.71358 | -43.34939 | 2025-09-30 03:51:00 | NOAA-20 | BELFORD ROXO | RIO DE JANEIRO | Brasil | 3300456 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| a828b03d-c9e8-3bc5-99b7-2a14a2ffe19b | -19.69729 | -43.68779 | 2025-09-30 03:51:00 | NOAA-20 | TAQUARAÇU DE MINAS | MINAS GERAIS | Brasil | 3168309 | 31 | 33 | nan | nan | nan | Cerrado | 3.3 |
| a727d671-c7c4-3040-bb85-d80bee97af5e | -23.12182 | -48.84027 | 2025-09-30 03:51:00 | NOAA-20 | AVARÉ | SÃO PAULO | Brasil | 3504503 | 35 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b1f37a01-ee5a-3f58-989a-b5b16889ca4d | -20.02151 | -41.43627 | 2025-09-30 03:51:00 | NOAA-20 | MUTUM | MINAS GERAIS | Brasil | 3144003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| a2376937-7b49-3892-aa00-80503b9cddbb | -23.12174 | -48.84085 | 2025-09-30 03:51:00 | NOAA-20 | AVARÉ | SÃO PAULO | Brasil | 3504503 | 35 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 640cac74-8ddc-3d16-92ea-499cf06fd845 | -20.18865 | -49.1222 | 2025-09-30 03:51:00 | NOAA-20 | FRONTEIRA | MINAS GERAIS | Brasil | 3127008 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e3074635-5452-3f0f-a868-f68cf83ee218 | -20.42305 | -46.17021 | 2025-09-30 03:51:00 | NOAA-20 | PIUMHI | MINAS GERAIS | Brasil | 3151503 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| b7921563-2876-390b-ae00-03badc018d7a | -19.98012 | -41.91184 | 2025-09-30 03:51:00 | NOAA-20 | SIMONÉSIA | MINAS GERAIS | Brasil | 3167608 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 39f204dc-b3d4-347a-98fb-033ccd914678 | -21.62297 | -44.06606 | 2025-09-30 03:51:00 | NOAA-20 | SANTANA DO GARAMBÉU | MINAS GERAIS | Brasil | 3158706 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 06765473-5f78-38b8-9364-75e2ef4cd6d9 | -22.33193 | -49.48051 | 2025-09-30 03:51:00 | NOAA-20 | FERNÃO | SÃO PAULO | Brasil | 3515657 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 09710ce6-3424-333e-826d-143c80fa927a | -20.61967 | -46.19164 | 2025-09-30 03:51:00 | NOAA-20 | CAPITÓLIO | MINAS GERAIS | Brasil | 3112802 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 96e9e0a5-7cb3-3233-8531-8b4dd73e8fe9 | -23.46639 | -47.75851 | 2025-09-30 03:51:00 | NOAA-20 | CAPELA DO ALTO | SÃO PAULO | Brasil | 3510302 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| b6dada63-4093-3915-a706-8ce5ac93f9cd | -20.39147 | -43.67786 | 2025-09-30 03:51:00 | NOAA-20 | OURO PRETO | MINAS GERAIS | Brasil | 3146107 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| b1ce4475-c751-31b4-8d3d-89382f9c2e45 | -21.61562 | -44.06453 | 2025-09-30 03:51:00 | NOAA-20 | SANTANA DO GARAMBÉU | MINAS GERAIS | Brasil | 3158706 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| f4aa086d-4cec-3924-9d0b-811d00827e37 | -22.8444 | -45.44743 | 2025-09-30 03:51:00 | NOAA-20 | PINDAMONHANGABA | SÃO PAULO | Brasil | 3538006 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 3a542794-23d6-38b2-8ab5-704818edd46a | -21.33135 | -46.7302 | 2025-09-30 03:51:00 | NOAA-20 | GUAXUPÉ | MINAS GERAIS | Brasil | 3128709 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| ea891d06-af28-3990-8a7a-3a08073f41ea | -21.31368 | -44.18682 | 2025-09-30 03:51:00 | NOAA-20 | SÃO JOÃO DEL REI | MINAS GERAIS | Brasil | 3162500 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 85245728-db2a-383c-8a57-c8d9c4f78397 | -21.38419 | -43.71961 | 2025-09-30 03:51:00 | NOAA-20 | ANTÔNIO CARLOS | MINAS GERAIS | Brasil | 3102902 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 9f40880a-0098-322c-86bd-5970005a3fd9 | -22.5219 | -44.60977 | 2025-09-30 03:51:00 | NOAA-20 | ITATIAIA | RIO DE JANEIRO | Brasil | 3302254 | 33 | 33 | nan | nan | nan | Mata Atlântica | 11.5 |
| 85bcb335-b75c-3eef-9670-f36d6cd6b390 | -19.85518 | -42.59173 | 2025-09-30 03:51:00 | NOAA-20 | DIONÍSIO | MINAS GERAIS | Brasil | 3121803 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.6 |
| b11eb42c-c5b0-34f4-95f3-1cbb331a7a52 | -23.19264 | -49.97731 | 2025-09-30 03:51:00 | NOAA-20 | JACAREZINHO | PARANÁ | Brasil | 4111803 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 3263f93c-1824-399a-bb33-a011d9162929 | -19.59935 | -45.89292 | 2025-09-30 03:51:00 | NOAA-20 | ESTRELA DO INDAIÁ | MINAS GERAIS | Brasil | 3124708 | 31 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 866fccba-2537-36fb-a520-94fbf19113a5 | -21.89457 | -45.75352 | 2025-09-30 03:51:00 | NOAA-20 | TURVOLÂNDIA | MINAS GERAIS | Brasil | 3169802 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 1ab78e7b-e27c-3721-b4de-ec06b972e719 | -20.32224 | -41.40261 | 2025-09-30 03:51:00 | NOAA-20 | MUNIZ FREIRE | ESPÍRITO SANTO | Brasil | 3203700 | 32 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| d19aa9cb-0503-3230-bc30-ec3f57f9855a | -19.55233 | -44.24417 | 2025-09-30 03:51:00 | NOAA-20 | SETE LAGOAS | MINAS GERAIS | Brasil | 3167202 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 4447d0ce-6a81-3265-80ef-03481c5a0532 | -20.4281 | -46.16689 | 2025-09-30 03:51:00 | NOAA-20 | PIUMHI | MINAS GERAIS | Brasil | 3151503 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| cde25e64-3a71-3af0-b75e-b07cfa45f677 | -20.04664 | -41.32637 | 2025-09-30 03:51:00 | NOAA-20 | MUTUM | MINAS GERAIS | Brasil | 3144003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 7.5 |
| 86b401de-b6e5-34c0-95ea-0795f42e5150 | -19.4212 | -44.53477 | 2025-09-30 03:51:00 | NOAA-20 | PARAOPEBA | MINAS GERAIS | Brasil | 3147402 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f72a04d7-81ba-394c-b014-aa6dcac9b4ae | -20.06404 | -46.78863 | 2025-09-30 03:51:00 | NOAA-20 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| c3921986-1268-3847-b6a3-9f2129679d32 | -21.32022 | -42.8787 | 2025-09-30 03:51:00 | NOAA-20 | ASTOLFO DUTRA | MINAS GERAIS | Brasil | 3104601 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.9 |
| bac9d7d5-871c-3acb-8fe5-20925434126a | -20.95829 | -46.29209 | 2025-09-30 03:51:00 | NOAA-20 | CARMO DO RIO CLARO | MINAS GERAIS | Brasil | 3114402 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 0b28a744-e8f8-3070-8ccc-72623f19e492 | -20.99542 | -47.02242 | 2025-09-30 03:51:00 | NOAA-20 | SÃO SEBASTIÃO DO PARAÍSO | MINAS GERAIS | Brasil | 3164704 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b44f9ab6-371b-3257-be16-cb8cfd07ad7a | -19.70981 | -45.88568 | 2025-09-30 03:51:00 | NOAA-20 | LUZ | MINAS GERAIS | Brasil | 3138807 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 44f10cde-b238-3f04-9816-3071a72bd1fc | -19.86119 | -43.81709 | 2025-09-30 03:51:00 | NOAA-20 | SABARÁ | MINAS GERAIS | Brasil | 3156700 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| 7f530d85-9a2f-3210-9e0d-cffeff566f73 | -19.94188 | -43.66811 | 2025-09-30 03:51:00 | NOAA-20 | CAETÉ | MINAS GERAIS | Brasil | 3110004 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 5f2bf4b0-eaf4-3864-93d2-37f88aea5f3a | -19.66865 | -44.98248 | 2025-09-30 03:51:00 | NOAA-20 | LEANDRO FERREIRA | MINAS GERAIS | Brasil | 3138302 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| ef34719b-c9b8-342a-8342-30eb5269a5c2 | -22.90123 | -51.19069 | 2025-09-30 03:51:00 | NOAA-20 | ALVORADA DO SUL | PARANÁ | Brasil | 4100806 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 79d1e748-fa20-32da-b51f-a844a13a156c | -19.85943 | -42.58826 | 2025-09-30 03:51:00 | NOAA-20 | DIONÍSIO | MINAS GERAIS | Brasil | 3121803 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.6 |
| 90cbb7a5-a539-3802-8547-06ca264f4f6f | -20.61146 | -46.1887 | 2025-09-30 03:51:00 | NOAA-20 | CAPITÓLIO | MINAS GERAIS | Brasil | 3112802 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b2e45ca2-5c5a-347d-9be2-9c83dce9ae9c | -19.6017 | -43.82799 | 2025-09-30 03:51:00 | NOAA-20 | LAGOA SANTA | MINAS GERAIS | Brasil | 3137601 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 468b33b3-7eaf-335d-b5cf-7e17c2df9d95 | -20.29699 | -42.28247 | 2025-09-30 03:51:00 | NOAA-20 | MATIPÓ | MINAS GERAIS | Brasil | 3140902 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 8c128102-706b-3c2a-92df-e16e8f8cbbd2 | -19.86294 | -42.58897 | 2025-09-30 03:51:00 | NOAA-20 | DIONÍSIO | MINAS GERAIS | Brasil | 3121803 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 77f53d9f-d33b-36a0-a70b-1b170bb1b0ba | -22.33618 | -49.48532 | 2025-09-30 03:51:00 | NOAA-20 | FERNÃO | SÃO PAULO | Brasil | 3515657 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| c6c383a0-8920-3571-8502-32c67f596c9a | -20.60901 | -46.0671 | 2025-09-30 03:51:00 | NOAA-20 | CAPITÓLIO | MINAS GERAIS | Brasil | 3112802 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 8544b161-5495-300c-8a7b-616391ac7941 | -20.74068 | -47.14568 | 2025-09-30 03:51:00 | NOAA-20 | SÃO TOMÁS DE AQUINO | MINAS GERAIS | Brasil | 3165107 | 31 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 127cbe9f-4f85-3e8f-b3fd-bee3017a83aa | -21.32184 | -46.75564 | 2025-09-30 03:51:00 | NOAA-20 | GUAXUPÉ | MINAS GERAIS | Brasil | 3128709 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 3d38fb33-39f4-3a23-abf0-c27736e26b34 | -22.33055 | -49.48167 | 2025-09-30 03:51:00 | NOAA-20 | FERNÃO | SÃO PAULO | Brasil | 3515657 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 0b00524f-9434-3976-becc-c6f3fc856315 | -19.94641 | -43.66416 | 2025-09-30 03:51:00 | NOAA-20 | CAETÉ | MINAS GERAIS | Brasil | 3110004 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 12bd58cb-1678-37af-bffc-e7d5393e5d54 | -22.90041 | -51.1943 | 2025-09-30 03:51:00 | NOAA-20 | ALVORADA DO SUL | PARANÁ | Brasil | 4100806 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |


[Clique aqui para ver as próximas entradas](README46.md)
