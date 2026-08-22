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

## Dados Diários - Página 57

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 84c1cf44-8b44-3f02-b49d-70d0ed7ada19 | -6.85989 | -59.43248 | 2026-08-22 05:23:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b5b30659-2cb4-3efc-ab7c-4f329db181d8 | -6.94303 | -60.08431 | 2026-08-22 05:23:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| d5c556bd-a098-3d08-bd47-d28f78e8ed0f | -7.6049 | -60.96091 | 2026-08-22 05:23:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| bfa07852-3bde-3fa7-87e6-7ab69772910b | -8.59331 | -54.73812 | 2026-08-22 05:23:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a458dbd3-a48b-3d92-b4a3-e44e93622940 | -6.93987 | -52.7825 | 2026-08-22 05:23:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 0b309082-f859-3663-9ef7-a2274a42d59d | -6.08958 | -57.71843 | 2026-08-22 05:23:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 0d12f3df-afcd-37fe-b25c-7a6abf6ae265 | -6.75888 | -58.67424 | 2026-08-22 05:23:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 9eb8b6d2-5933-37e3-988c-a5052441ac26 | -6.7727 | -58.67284 | 2026-08-22 05:23:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| f4e9c2a1-7cf2-3825-b4ee-9adba7d7092d | -6.77325 | -58.66936 | 2026-08-22 05:23:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 5726bb2c-32b7-3e98-a694-ea30eaa2021e | -6.81247 | -59.41075 | 2026-08-22 05:23:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 88983f17-de53-3459-b43a-6c47f38cec5d | -8.52341 | -54.81135 | 2026-08-22 05:23:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 11.8 |
| 6f84e742-e25a-32a3-9685-0ea321989c38 | -7.0141 | -59.59578 | 2026-08-22 05:23:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 85ff288c-f42f-3b59-8cc1-dd55a0f32192 | -4.17877 | -48.57925 | 2026-08-22 05:23:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c184eb26-0fe5-3edc-b434-48012a10b568 | -6.65452 | -56.3449 | 2026-08-22 05:23:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| fa7b7cd7-64cb-33dd-bbce-9bf125fbdde9 | -7.68124 | -46.16537 | 2026-08-22 05:23:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 26853b25-cf2f-355b-89ca-1c861df6e886 | -4.17933 | -48.57531 | 2026-08-22 05:23:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 09b6357d-bb5c-3b37-9e63-633bba80b935 | -6.78683 | -58.6465 | 2026-08-22 05:23:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 8eb0d64c-9718-33bb-9002-dc81102b3017 | -6.35861 | -58.34699 | 2026-08-22 05:23:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 4558cde3-84e7-3b8a-b8b9-2926eae348bb | -7.60105 | -60.94167 | 2026-08-22 05:23:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 7402d1ea-b521-3ff7-bacf-f2a0fd2706ff | -6.38375 | -54.95845 | 2026-08-22 05:23:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 409fb49e-45e7-3dc6-9668-0155fd1eee41 | -6.02787 | -57.68333 | 2026-08-22 05:23:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 233c296b-f966-385d-927f-56cdc1aef662 | -13.82228 | -53.99693 | 2026-08-22 05:23:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| faab8c27-5a4e-30f6-b5f3-037128554418 | -6.11464 | -53.07543 | 2026-08-22 05:23:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 12c62235-ce20-34a9-825e-3e86ab765236 | -6.5517 | -56.25947 | 2026-08-22 05:23:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| cb0048bf-eb8d-3fbc-802e-5cf4ce9c9e50 | -14.56328 | -53.0493 | 2026-08-22 05:23:00 | NOAA-20 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 3f1ccebd-dcf1-3ad3-befb-4cb83c881ad3 | -8.52098 | -55.32199 | 2026-08-22 05:23:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 0537dc22-c686-357c-af43-5f2089cf1ba4 | -7.50145 | -60.0768 | 2026-08-22 05:23:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 944b42aa-2c74-3e44-8c50-c435622bc966 | -6.88808 | -59.40509 | 2026-08-22 05:23:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 738aa826-221f-3b77-9705-9ae1ebd61417 | -6.17121 | -55.4444 | 2026-08-22 05:23:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 67ba2167-6664-3d22-916b-6150bc3f4f43 | -4.17716 | -48.57607 | 2026-08-22 05:23:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| cd53779e-cc68-331a-b015-d88a355a1b45 | -6.56821 | -58.97849 | 2026-08-22 05:23:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a192db64-5941-34e5-95cd-c8bb7c47e47b | -6.1238 | -59.89543 | 2026-08-22 05:23:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| feeb3c9b-df01-3da6-bca8-7c40b64f955e | -7.59883 | -60.82632 | 2026-08-22 05:23:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| ea1f3fd6-9791-38ca-8ad3-cee58ea5ab93 | -7.37239 | -59.94876 | 2026-08-22 05:23:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 971d267c-a191-375c-8ca5-2c2a44c32d8d | -6.11264 | -53.07376 | 2026-08-22 05:23:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ef8c8834-2e8b-3cfc-a255-2a968e11502e | -7.09814 | -61.08246 | 2026-08-22 05:23:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a1c4ad2c-7377-3027-b8a4-da774bc6504f | -6.13211 | -59.90751 | 2026-08-22 05:23:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6b1e996b-81f4-3c08-9c02-8654021b6799 | -6.22751 | -55.48713 | 2026-08-22 05:23:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| b970d95e-1ae5-3446-a562-0117c65522a6 | -14.38577 | -51.79634 | 2026-08-22 05:23:00 | NOAA-20 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 13.8 |
| 34b4ec66-a9ed-36f7-96a5-37f66bda19ee | -6.81853 | -59.41526 | 2026-08-22 05:23:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 53eb6e91-92cb-3249-b323-59fc11aa4563 | -6.86273 | -59.02868 | 2026-08-22 05:23:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 890b9167-8c06-3072-bfcc-b3911e6c591c | -5.99658 | -57.81765 | 2026-08-22 05:23:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 0ef0dcfa-1514-3222-9f7a-c0d67edcf169 | -8.53077 | -54.84403 | 2026-08-22 05:23:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 8.0 |
| faf7892b-a765-3582-ad94-3dbf84a6ee46 | -5.79767 | -57.54467 | 2026-08-22 05:23:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| f26c3df5-00c0-31c0-995f-6bd6f0f137cd | -7.43491 | -59.79112 | 2026-08-22 05:23:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 64eccc06-9dcb-3530-80cb-106314bf91b7 | -6.81468 | -59.4182 | 2026-08-22 05:23:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 20ffcd69-b936-3018-94a3-a8f1671989de | -4.12159 | -49.44442 | 2026-08-22 05:23:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 222e23d9-9946-30b2-b565-f8b2f53b250e | -6.1002 | -57.69437 | 2026-08-22 05:23:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 14a888ed-5e6f-3ed0-9c2f-e108569af799 | -6.00663 | -57.79731 | 2026-08-22 05:23:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| bcfe1b2f-5eb8-3956-8224-fe042e8cb5c5 | -14.00063 | -53.67341 | 2026-08-22 05:23:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 9d82bcba-3858-3480-9526-de3654d36281 | -6.94368 | -59.31106 | 2026-08-22 05:23:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| da4522b6-2db8-3e02-8df8-1b2e733605fc | -6.60997 | -56.35074 | 2026-08-22 05:23:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d2002fbd-c868-3fca-af75-610722908b31 | -6.53769 | -58.52565 | 2026-08-22 05:23:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 4.1 |
| b31308ec-c2d6-34eb-8b19-0c7d14b96be9 | -7.68814 | -46.16646 | 2026-08-22 05:23:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| bd504e4f-d983-35c3-8885-e46812f58d82 | -12.82502 | -48.45827 | 2026-08-22 05:23:00 | NOAA-20 | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 3d36f95d-d63d-3eb0-8daa-8daac6b66267 | -6.61051 | -56.3713 | 2026-08-22 05:23:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5a978985-d986-3b9a-ae9b-e9d025ae1945 | -6.24491 | -55.42196 | 2026-08-22 05:23:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d586e16b-3d03-33b4-88da-aaf674f36f12 | -8.02863 | -54.02473 | 2026-08-22 05:23:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| e6fd0eab-f7fe-32c3-a51a-b24dd8fe74be | -6.8966 | -55.71099 | 2026-08-22 05:23:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 98666399-4b0e-3b48-8d86-4d31b8759e9b | -6.06712 | -57.7076 | 2026-08-22 05:23:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 424a6ec9-857b-3a5a-8bde-75300f704cda | -12.93887 | -56.62635 | 2026-08-22 05:23:00 | NOAA-20 | NOVA MUTUM | MATO GROSSO | Brasil | 5106224 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| a23a7b66-d858-3bdb-bd87-10364e1d0947 | -6.88976 | -59.43727 | 2026-08-22 05:23:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| eab2bde7-cb02-3305-9f7e-9f0a1ccf2e91 | -7.02015 | -59.55775 | 2026-08-22 05:23:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| add2ab03-cd8e-3ab8-8627-33a22d512b22 | -6.9676 | -59.05236 | 2026-08-22 05:23:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 80b9fe8d-3e90-3ba3-bd56-dbf875d80303 | -8.61484 | -54.7304 | 2026-08-22 05:23:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| bcba4e00-3591-3e5d-b9c2-7e903e61b6e5 | -6.85549 | -59.43887 | 2026-08-22 05:23:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 088c54a7-6919-3c8a-9857-2951d0d82692 | -6.82087 | -59.67842 | 2026-08-22 05:23:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 866b1f90-d0b7-379b-ba78-8d5c56d37125 | -6.44495 | -60.07648 | 2026-08-22 05:23:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 88e10738-1306-37ff-9b27-9f3d1b9f35ce | -6.09327 | -59.91571 | 2026-08-22 05:23:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 230fe11f-7d42-39c2-b03d-f155f380c7ae | -8.0316 | -54.01762 | 2026-08-22 05:23:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| b5cb6cd8-8d08-3abd-b86a-20c61d990de8 | -6.76275 | -58.67128 | 2026-08-22 05:23:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 9fb41862-21c0-39f8-936b-c031bc868f72 | -13.99009 | -53.68168 | 2026-08-22 05:23:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 9d955b56-e7ee-3b62-9276-732cb16ae607 | -6.77103 | -58.66187 | 2026-08-22 05:23:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 771b80a6-323e-37e7-aca2-ea8f785d210a | -6.2617 | -62.52882 | 2026-08-22 05:23:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| fc93a5fe-df44-3d4e-91f3-9e9a6576a005 | -4.42514 | -55.44425 | 2026-08-22 05:23:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| dec0f485-b038-38d9-8a89-f2794191790b | -5.79712 | -57.54827 | 2026-08-22 05:23:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| e9cb39eb-beda-375e-b8d4-c141b5531f25 | -7.08352 | -55.45356 | 2026-08-22 05:23:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b9ff10c4-c8a2-3a6b-b315-804654668524 | -6.80035 | -59.42302 | 2026-08-22 05:23:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 13.2 |
| 76e708a5-cc3c-3507-a9d7-8a7cf610a04b | -6.09291 | -57.69691 | 2026-08-22 05:23:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 431775d3-c4a3-3a0a-a9e3-5ae41f8e57f9 | -6.76883 | -58.6758 | 2026-08-22 05:23:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| c804c7f4-cbec-345b-ba6b-d7f4815522ab | -8.52605 | -54.84853 | 2026-08-22 05:23:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 08b9924c-5998-3565-b7f2-f7c610c59f0e | -8.99124 | -50.73963 | 2026-08-22 05:23:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 889ddcf5-33e7-3b62-b477-1d82a0e80917 | -6.10833 | -53.07312 | 2026-08-22 05:23:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1e2a86ce-0f5f-352d-8b14-31014e4553e9 | -6.82515 | -59.41631 | 2026-08-22 05:23:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 7.4 |
| 8a40146d-d590-3e4c-8dcd-ad16d3a0be6a | -13.99199 | -53.66727 | 2026-08-22 05:23:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 23c540f2-b3e3-356d-ae20-f0a221830b0f | -6.1299 | -59.89999 | 2026-08-22 05:23:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 08864cd2-fe3f-330f-9442-d2bd6dc584cd | -6.76839 | -59.7733 | 2026-08-22 05:23:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 36213282-ad73-340a-ac49-98f60f443fa6 | -6.8505 | -59.40615 | 2026-08-22 05:23:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 18ff02fe-6df6-3c38-88f3-528e30d14f63 | -7.44567 | -59.99977 | 2026-08-22 05:23:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ae1c26ab-9b17-36e9-bf8b-0906406f51c8 | -6.1199 | -59.91993 | 2026-08-22 05:23:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| de8cab2a-d26c-351c-ae1d-9e0920d5e81a | -6.22937 | -55.42424 | 2026-08-22 05:23:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 5d86034a-2df1-37b4-89b8-16aa9c885108 | -7.48485 | -55.32888 | 2026-08-22 05:23:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9b526578-2894-3cd7-9a9e-280defa5325c | -11.16418 | -54.01184 | 2026-08-22 05:23:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 8ff53c29-082c-3453-9f3d-024891eef387 | -6.8257 | -59.41285 | 2026-08-22 05:23:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 7.4 |
| c7de06cc-ad7b-383a-abbe-e279e9f4ff17 | -7.5943 | -60.94058 | 2026-08-22 05:23:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e19d9c0a-b512-3103-b678-d04a44253918 | -4.0584 | -49.10926 | 2026-08-22 05:23:00 | NOAA-20 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| e4135e51-2586-34ce-a99e-b7fa82d3d801 | -14.39067 | -51.80036 | 2026-08-22 05:23:00 | NOAA-20 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 13.8 |
| 23b48351-77a6-3247-b79c-0dd4f1d755ca | -5.91033 | -61.29429 | 2026-08-22 05:23:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8926a6ba-5bd7-3c21-b5a2-76012a001f37 | -6.80076 | -59.0114 | 2026-08-22 05:23:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 03cc4cbd-4743-314e-8b55-bf142f2617a2 | -5.96339 | -51.95926 | 2026-08-22 05:23:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |


[Clique aqui para ver as próximas entradas](README58.md)
