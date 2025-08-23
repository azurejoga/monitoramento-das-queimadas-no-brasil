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

## Dados Diários - Página 31

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| a056a1b6-6539-383e-8568-43b9192c4d48 | -22.53239 | -44.35408 | 2025-08-23 04:04:00 | NOAA-20 | RESENDE | RIO DE JANEIRO | Brasil | 3304201 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 6de926e2-6fbf-3e19-96fc-1d4b00201dfc | -17.59519 | -46.56242 | 2025-08-23 04:04:00 | NOAA-20 | LAGOA GRANDE | MINAS GERAIS | Brasil | 3137536 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 8b211092-4a66-30c1-af39-18e7e10a3eb9 | -16.42461 | -48.89959 | 2025-08-23 04:04:00 | NOAA-20 | LEOPOLDO DE BULHÕES | GOIÁS | Brasil | 5212303 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 94a5333c-28f8-3835-b778-a564e99dbe39 | -17.59601 | -46.55775 | 2025-08-23 04:04:00 | NOAA-20 | LAGOA GRANDE | MINAS GERAIS | Brasil | 3137536 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 34f1e19a-7b00-364b-a906-c7fe164a98f3 | -17.50315 | -48.02344 | 2025-08-23 04:04:00 | NOAA-20 | IPAMERI | GOIÁS | Brasil | 5210109 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 37c20fc3-60f6-3fef-a1b9-c31e585b306b | -21.96278 | -45.59275 | 2025-08-23 04:04:00 | NOAA-20 | SÃO GONÇALO DO SAPUCAÍ | MINAS GERAIS | Brasil | 3162005 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.5 |
| caa1d36d-dd4b-3d32-aa5d-5c6bf59b243e | -20.29524 | -42.04913 | 2025-08-23 04:04:00 | NOAA-20 | MANHUAÇU | MINAS GERAIS | Brasil | 3139409 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 44503783-e5df-3132-9ba0-e035975d8616 | -22.05482 | -46.04365 | 2025-08-23 04:04:00 | NOAA-20 | CONGONHAL | MINAS GERAIS | Brasil | 3117900 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 05d95dc2-4501-374a-a37b-f9bdeae1ad38 | -17.27048 | -46.77211 | 2025-08-23 04:04:00 | NOAA-20 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 1ec19f4f-c6cd-3304-ae8c-325bf1b9b33e | -22.83503 | -45.18659 | 2025-08-23 04:04:00 | NOAA-20 | GUARATINGUETÁ | SÃO PAULO | Brasil | 3518404 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| c640a9b6-bb67-3eca-8dde-01f594fc5e8a | -17.59311 | -46.55235 | 2025-08-23 04:04:00 | NOAA-20 | LAGOA GRANDE | MINAS GERAIS | Brasil | 3137536 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| c1ef5b7e-6fa2-3edf-b269-29729a601d4c | -18.2507 | -45.57156 | 2025-08-23 04:04:00 | NOAA-20 | SÃO GONÇALO DO ABAETÉ | MINAS GERAIS | Brasil | 3161700 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 850ae512-4e00-34b5-b981-61c8c93c5199 | -20.39253 | -45.44625 | 2025-08-23 04:04:00 | NOAA-20 | FORMIGA | MINAS GERAIS | Brasil | 3126109 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 61c8db4d-4744-330d-9646-946734e72a1c | -22.54118 | -43.59246 | 2025-08-23 04:04:00 | NOAA-20 | ENGENHEIRO PAULO DE FRONTIN | RIO DE JANEIRO | Brasil | 3301801 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| f198af6c-4e6a-39a4-af3f-0ceaed49789c | -20.43909 | -42.12342 | 2025-08-23 04:04:00 | NOAA-20 | LUISBURGO | MINAS GERAIS | Brasil | 3138674 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| f9dc5441-1f23-3b53-af15-3039ca82732f | -22.63412 | -47.43713 | 2025-08-23 04:04:00 | NOAA-20 | LIMEIRA | SÃO PAULO | Brasil | 3526902 | 35 | 33 | nan | nan | nan | Cerrado | 0.9 |
| ce6772de-61db-3842-98e4-9ba526aac88d | -19.42378 | -47.22035 | 2025-08-23 04:04:00 | NOAA-20 | PERDIZES | MINAS GERAIS | Brasil | 3149804 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 776157b8-f991-3326-893d-585a5233916b | -16.41642 | -49.15405 | 2025-08-23 04:04:00 | NOAA-20 | NERÓPOLIS | GOIÁS | Brasil | 5214507 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 8b9c2b87-435c-38b5-84c9-4e5dccbdefc2 | -18.91907 | -47.77423 | 2025-08-23 04:04:00 | NOAA-20 | INDIANÓPOLIS | MINAS GERAIS | Brasil | 3130705 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 06b89170-d064-3cc1-a115-3569c01afb8f | -17.60715 | -46.69413 | 2025-08-23 04:04:00 | NOAA-20 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 5c20dc3b-f84e-3774-8a7a-2af7dbd00550 | -15.22455 | -53.85613 | 2025-08-23 04:04:00 | NOAA-20 | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 12.9 |
| bbd3e68c-95aa-350d-8abf-753bbfc92f31 | -16.40307 | -49.17527 | 2025-08-23 04:04:00 | NOAA-20 | NERÓPOLIS | GOIÁS | Brasil | 5214507 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| cc94e8b5-82a8-34a4-87e7-a74e76a0743e | -20.2923 | -46.65304 | 2025-08-23 04:04:00 | NOAA-20 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b6126830-c18b-3e9c-b5fc-345cbe26123f | -17.27322 | -46.77399 | 2025-08-23 04:04:00 | NOAA-20 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| db63487b-1493-3158-828b-814e27952c32 | -22.62965 | -47.44098 | 2025-08-23 04:04:00 | NOAA-20 | LIMEIRA | SÃO PAULO | Brasil | 3526902 | 35 | 33 | nan | nan | nan | Cerrado | 11.2 |
| 3160ca1c-42ff-3be3-b9eb-847002a08fdd | -22.09586 | -45.0291 | 2025-08-23 04:04:00 | NOAA-20 | SÃO LOURENÇO | MINAS GERAIS | Brasil | 3163706 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 595b3acf-689c-3506-9ed9-be15a6989e56 | -20.08416 | -46.12098 | 2025-08-23 04:04:00 | NOAA-20 | BAMBUÍ | MINAS GERAIS | Brasil | 3105103 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| be169ac6-28aa-34be-9c05-d4fc4bb11123 | -22.53397 | -43.72547 | 2025-08-23 04:04:00 | NOAA-20 | MENDES | RIO DE JANEIRO | Brasil | 3302809 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 483f9383-a9ad-377d-98f8-0c240a000b99 | -22.15371 | -44.59346 | 2025-08-23 04:04:00 | NOAA-20 | AIURUOCA | MINAS GERAIS | Brasil | 3101201 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 5b3f87bd-0d46-39ac-afa0-064f1111b438 | -15.06339 | -56.3949 | 2025-08-23 04:04:00 | NOAA-20 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e49d82b3-955c-3409-9c22-7a2154a3bcee | -14.66919 | -54.92086 | 2025-08-23 04:04:00 | NOAA-20 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 4.4 |
| f311974f-8d01-3fc9-900d-56c48290c48c | -18.86236 | -49.47034 | 2025-08-23 04:04:00 | NOAA-20 | ITUIUTABA | MINAS GERAIS | Brasil | 3134202 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.4 |
| 9d4c5e99-08a9-3117-aa4e-d90dce93bd0d | -15.01787 | -54.89186 | 2025-08-23 04:04:00 | NOAA-20 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 2872cd81-b82c-3a50-b16c-b02668051be0 | -14.66545 | -54.92823 | 2025-08-23 04:04:00 | NOAA-20 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 478312e0-6c86-395e-8e96-46f95e002792 | -17.66306 | -46.68531 | 2025-08-23 04:04:00 | NOAA-20 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| a7287877-7743-339f-9f56-7f057ded26dc | -22.90421 | -46.39059 | 2025-08-23 04:04:00 | NOAA-20 | VARGEM | SÃO PAULO | Brasil | 3556354 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| e1c64b59-1221-3653-b42f-7d82c1d74b82 | -17.60937 | -46.70164 | 2025-08-23 04:04:00 | NOAA-20 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 56c5776e-ba6b-3038-87db-d56b485e18ea | -18.27962 | -45.57267 | 2025-08-23 04:04:00 | NOAA-20 | SÃO GONÇALO DO ABAETÉ | MINAS GERAIS | Brasil | 3161700 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| e781fb75-72a4-318b-902d-e00cd31a0ad4 | -20.09137 | -47.74688 | 2025-08-23 04:04:00 | NOAA-20 | IGARAPAVA | SÃO PAULO | Brasil | 3520103 | 35 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 3c0d205d-6246-3823-be66-b49b6d45879c | -19.69525 | -47.96657 | 2025-08-23 04:04:00 | NOAA-20 | UBERABA | MINAS GERAIS | Brasil | 3170107 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 7aa3e29e-ea70-3ca7-ac9e-9d56dcccdefc | -21.9587 | -45.59607 | 2025-08-23 04:04:00 | NOAA-20 | SÃO GONÇALO DO SAPUCAÍ | MINAS GERAIS | Brasil | 3162005 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 3cd92196-c531-37b7-8fe2-720ce869805b | -20.28755 | -46.63767 | 2025-08-23 04:04:00 | NOAA-20 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 2e91538d-ad91-3fd2-82b1-d9de8d55bd49 | -22.05137 | -46.04296 | 2025-08-23 04:04:00 | NOAA-20 | CONGONHAL | MINAS GERAIS | Brasil | 3117900 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 5e6b5a4c-ca74-36d5-a314-cdb474a229f1 | -20.46102 | -42.02282 | 2025-08-23 04:04:00 | NOAA-20 | LUISBURGO | MINAS GERAIS | Brasil | 3138674 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| 45c5223b-121f-380e-adf6-34abbde7ae65 | -17.26188 | -46.77164 | 2025-08-23 04:04:00 | NOAA-20 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 8.2 |
| 88d02504-06b0-373f-bbb5-c9fb69768d79 | -20.35378 | -46.51473 | 2025-08-23 04:04:00 | NOAA-20 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 5b3aab4c-0ba5-31c2-bb09-19aacd75b004 | -21.90006 | -48.16834 | 2025-08-23 04:04:00 | NOAA-20 | ARARAQUARA | SÃO PAULO | Brasil | 3503208 | 35 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 89414771-3460-3e2a-ad5d-41b97332e2e0 | -21.9081 | -47.24952 | 2025-08-23 04:04:00 | NOAA-20 | SANTA CRUZ DAS PALMEIRAS | SÃO PAULO | Brasil | 3546306 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 4e25b0f1-b4eb-3467-9aed-c77759dc85a3 | -22.82368 | -45.19242 | 2025-08-23 04:04:00 | NOAA-20 | GUARATINGUETÁ | SÃO PAULO | Brasil | 3518404 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 2ebf8184-d854-3fd3-aa9f-9b8bf912739e | -15.22244 | -53.86584 | 2025-08-23 04:04:00 | NOAA-20 | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 8.5 |
| fcb87982-21d4-35cc-a3ec-b1cee94a8deb | -18.75203 | -46.69012 | 2025-08-23 04:04:00 | NOAA-20 | PATOS DE MINAS | MINAS GERAIS | Brasil | 3148004 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| d54356fe-f03e-32d1-a1aa-0896f89f5285 | -17.59808 | -46.56784 | 2025-08-23 04:04:00 | NOAA-20 | LAGOA GRANDE | MINAS GERAIS | Brasil | 3137536 | 31 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 95882ad8-1ed5-37c2-9af5-db1a6125c8dd | -15.33963 | -49.75566 | 2025-08-23 04:04:00 | NOAA-20 | CARMO DO RIO VERDE | GOIÁS | Brasil | 5205000 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 8629b681-8377-36a9-988a-7af5910cd09d | -22.47345 | -44.27882 | 2025-08-23 04:04:00 | NOAA-20 | BARRA MANSA | RIO DE JANEIRO | Brasil | 3300407 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| f7c3c458-249d-35d9-bda7-8e3284725b01 | -19.05234 | -47.70863 | 2025-08-23 04:04:00 | NOAA-20 | NOVA PONTE | MINAS GERAIS | Brasil | 3145000 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 3540c297-1563-3fb6-804f-6661e3fb1a38 | -17.70165 | -48.51807 | 2025-08-23 04:04:00 | NOAA-20 | CALDAS NOVAS | GOIÁS | Brasil | 5204508 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 8eb5b281-d918-3138-9bca-ac4f7f7ec3ad | -19.95903 | -47.51407 | 2025-08-23 04:04:00 | NOAA-20 | CONQUISTA | MINAS GERAIS | Brasil | 3118205 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| d1e8bc67-58eb-36e3-aaab-9a350069444d | -22.77101 | -43.68642 | 2025-08-23 04:04:00 | NOAA-20 | SEROPÉDICA | RIO DE JANEIRO | Brasil | 3305554 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| f4468e74-d6c0-36f0-b5f7-ebfbff8ca503 | -19.95607 | -47.50872 | 2025-08-23 04:04:00 | NOAA-20 | CONQUISTA | MINAS GERAIS | Brasil | 3118205 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| e02ad437-483f-3789-bc39-32ba5e35af24 | -18.27682 | -45.56783 | 2025-08-23 04:04:00 | NOAA-20 | SÃO GONÇALO DO ABAETÉ | MINAS GERAIS | Brasil | 3161700 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 3e66a32c-6d20-3454-9a60-885b57b80f5d | -21.95598 | -45.59138 | 2025-08-23 04:04:00 | NOAA-20 | SÃO GONÇALO DO SAPUCAÍ | MINAS GERAIS | Brasil | 3162005 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| f47051a5-f7da-303c-b0fc-4ff1fe5ee4d7 | -17.57594 | -48.7449 | 2025-08-23 04:04:00 | NOAA-20 | CALDAS NOVAS | GOIÁS | Brasil | 5204508 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 4f1ec34c-892a-3d97-87eb-c56104f065ff | -14.60828 | -54.7982 | 2025-08-23 04:04:00 | NOAA-20 | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 2640104c-9a98-31ac-b68a-1131378cc70c | -18.0514 | -42.95252 | 2025-08-23 04:04:00 | NOAA-20 | ITAMARANDIBA | MINAS GERAIS | Brasil | 3132503 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| dc6541fb-5996-3e1c-b47e-51c432ce4e93 | -20.35445 | -46.53209 | 2025-08-23 04:04:00 | NOAA-20 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| a8e47d4c-95f8-330f-8598-bf4505a4ed1e | -22.19101 | -44.55378 | 2025-08-23 04:04:00 | NOAA-20 | BOCAINA DE MINAS | MINAS GERAIS | Brasil | 3107208 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| 02f14dc8-327e-3900-8f5b-0d1f86aabb34 | -22.7716 | -43.68268 | 2025-08-23 04:04:00 | NOAA-20 | SEROPÉDICA | RIO DE JANEIRO | Brasil | 3305554 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 05768481-ff1e-35b1-b61e-882653d2dcaa | -20.35647 | -46.54184 | 2025-08-23 04:04:00 | NOAA-20 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 392d63ce-3e6b-3336-96b7-c9e522a28f9d | -20.09617 | -47.7641 | 2025-08-23 04:04:00 | NOAA-20 | IGARAPAVA | SÃO PAULO | Brasil | 3520103 | 35 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b01a8704-fc73-30c1-9771-24c713bae2a5 | -20.11252 | -47.78353 | 2025-08-23 04:04:00 | NOAA-20 | ARAMINA | SÃO PAULO | Brasil | 3503000 | 35 | 33 | nan | nan | nan | Cerrado | 1.8 |
| bd7ebe74-56c3-3446-8d54-3e4efcb63f05 | -22.55638 | -49.76424 | 2025-08-23 04:04:00 | NOAA-20 | SÃO PEDRO DO TURVO | SÃO PAULO | Brasil | 3550506 | 35 | 33 | nan | nan | nan | Cerrado | 0.5 |
| ad8e4bce-8935-3dda-a071-e8679b7c1193 | -22.63329 | -47.44175 | 2025-08-23 04:04:00 | NOAA-20 | LIMEIRA | SÃO PAULO | Brasil | 3526902 | 35 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 2864766e-c43b-3e10-96e9-944d8c75565e | -22.66312 | -46.9145 | 2025-08-23 04:04:00 | NOAA-20 | SANTO ANTÔNIO DE POSSE | SÃO PAULO | Brasil | 3548005 | 35 | 33 | nan | nan | nan | Mata Atlântica | 7.1 |
| 855b96d4-aa7d-3166-a474-9aec2ad59c12 | -21.67633 | -49.05576 | 2025-08-23 04:04:00 | NOAA-20 | BORBOREMA | SÃO PAULO | Brasil | 3507407 | 35 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 3a8fcf1d-4387-3e8e-a95c-102ea911f3ac | -22.53339 | -43.7292 | 2025-08-23 04:04:00 | NOAA-20 | MENDES | RIO DE JANEIRO | Brasil | 3302809 | 33 | 33 | nan | nan | nan | Mata Atlântica | 4.2 |
| a65a529a-c7ce-387b-9d3e-b051b2b40aac | -17.40096 | -44.25209 | 2025-08-23 04:04:00 | NOAA-20 | FRANCISCO DUMONT | MINAS GERAIS | Brasil | 3126604 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e380b0ab-04c4-3b43-b1bf-b78405a2eb26 | -14.42375 | -53.34179 | 2025-08-23 04:04:00 | NOAA-20 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 1317e77d-e67b-30c9-b925-ded37f1d7130 | -14.46655 | -55.94845 | 2025-08-23 04:04:00 | NOAA-20 | NOBRES | MATO GROSSO | Brasil | 5105903 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| e9a437cc-8caf-3a2a-b809-da5274b173c1 | -22.42396 | -44.50121 | 2025-08-23 04:04:00 | NOAA-20 | RESENDE | RIO DE JANEIRO | Brasil | 3304201 | 33 | 33 | nan | nan | nan | Mata Atlântica | 3.5 |
| 262b72f0-8cb8-34f1-9229-eb526de8df1c | -17.6109 | -46.69484 | 2025-08-23 04:04:00 | NOAA-20 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| feb1194d-b1a5-3965-918f-95f7f2b7769e | -22.42064 | -44.50056 | 2025-08-23 04:04:00 | NOAA-20 | RESENDE | RIO DE JANEIRO | Brasil | 3304201 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 1d438585-74ce-3902-b0a7-c293ad30df1e | -20.01196 | -46.4299 | 2025-08-23 04:04:00 | NOAA-20 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 856a4264-84a1-33f1-a003-78620bc67fce | -17.26292 | -46.77053 | 2025-08-23 04:04:00 | NOAA-20 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 9.9 |
| 25521cfa-ecfd-3ca6-8261-d9872e8d64c1 | -20.44579 | -42.1246 | 2025-08-23 04:04:00 | NOAA-20 | LUISBURGO | MINAS GERAIS | Brasil | 3138674 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.3 |
| c3add0e3-eb3a-36bd-b419-c4991aa6fc2a | -17.26963 | -46.77696 | 2025-08-23 04:04:00 | NOAA-20 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 92d71bb8-4137-3bbc-9a73-6ae1005b5a98 | -22.31378 | -48.72768 | 2025-08-23 04:04:00 | NOAA-20 | ITAPUÍ | SÃO PAULO | Brasil | 3522901 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 66b260e3-d892-3295-8d5d-ec0b7d17cf09 | -22.6305 | -47.43635 | 2025-08-23 04:04:00 | NOAA-20 | LIMEIRA | SÃO PAULO | Brasil | 3526902 | 35 | 33 | nan | nan | nan | Cerrado | 11.2 |
| e6ef3fe2-9d52-3c22-ac0a-17600735c2df | -21.96142 | -45.60074 | 2025-08-23 04:04:00 | NOAA-20 | SÃO GONÇALO DO SAPUCAÍ | MINAS GERAIS | Brasil | 3162005 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 55a09635-0e2d-37b7-b5a1-419b72a3f970 | -17.39821 | -44.24768 | 2025-08-23 04:04:00 | NOAA-20 | FRANCISCO DUMONT | MINAS GERAIS | Brasil | 3126604 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| a6cba44e-36dc-3d71-8e31-8a92a64275ec | -15.21634 | -53.86444 | 2025-08-23 04:04:00 | NOAA-20 | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 8.5 |
| f72fd608-51c5-3e01-b4c0-7b49b52251ce | -17.58112 | -46.55482 | 2025-08-23 04:04:00 | NOAA-20 | LAGOA GRANDE | MINAS GERAIS | Brasil | 3137536 | 31 | 33 | nan | nan | nan | Cerrado | 16.5 |
| 928702de-6ea7-399f-b589-e9d95ddaeab6 | -16.42028 | -48.89851 | 2025-08-23 04:04:00 | NOAA-20 | LEOPOLDO DE BULHÕES | GOIÁS | Brasil | 5212303 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 844dc54b-793d-3179-846e-0e0bd7f03d47 | -20.08564 | -47.75647 | 2025-08-23 04:04:00 | NOAA-20 | IGARAPAVA | SÃO PAULO | Brasil | 3520103 | 35 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f2ff8db2-ac68-31ba-b6c5-7b1cc9600b52 | -21.617 | -41.57499 | 2025-08-23 04:04:00 | NOAA-20 | SÃO FIDÉLIS | RIO DE JANEIRO | Brasil | 3304805 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 705da3f8-d748-3f3c-8e30-369b90bd5a95 | -21.90001 | -47.25256 | 2025-08-23 04:04:00 | NOAA-20 | SANTA CRUZ DAS PALMEIRAS | SÃO PAULO | Brasil | 3546306 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| af423807-45f3-3865-811c-b70e6f11140b | -17.04455 | -47.13952 | 2025-08-23 04:04:00 | NOAA-20 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 5a1224e7-80ee-31a5-84cb-cf1925e121fd | -15.05473 | -56.40036 | 2025-08-23 04:04:00 | NOAA-20 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 6371c56f-424a-3a8d-a0bd-9f9cfc7e7a29 | -17.69221 | -48.4989 | 2025-08-23 04:04:00 | NOAA-20 | CALDAS NOVAS | GOIÁS | Brasil | 5204508 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 0762e4e5-4db2-3215-b195-d6f61879a0d6 | -17.57166 | -48.74418 | 2025-08-23 04:04:00 | NOAA-20 | CALDAS NOVAS | GOIÁS | Brasil | 5204508 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 84e4d208-2869-3ad7-b78a-2c25c151f1f6 | -19.97503 | -47.51249 | 2025-08-23 04:04:00 | NOAA-20 | CONQUISTA | MINAS GERAIS | Brasil | 3118205 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |


[Clique aqui para ver as próximas entradas](README32.md)
