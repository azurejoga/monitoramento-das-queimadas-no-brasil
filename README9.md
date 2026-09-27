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

## Dados Diários - Página 9

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 2224dfb5-bd84-3edf-ad6c-0f5c0ba3a7d9 | -8.0373 | -54.8926 | 2026-09-27 03:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 49.0 |
| 19212eae-38d7-39b5-83ec-58972c994dfe | -11.9622 | -50.5036 | 2026-09-27 03:00:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 165.7 |
| 35a03858-c290-3f33-8362-6c27a0565e7f | -11.9809 | -50.5228 | 2026-09-27 03:00:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 73.2 |
| c7966b2c-53f4-3948-94b5-ca96ce83c3c1 | -12.3082 | -50.3119 | 2026-09-27 03:00:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 76.1 |
| 7bc9b2ff-1cf7-30da-83db-1f5e0461a0e6 | -7.3999 | -55.6311 | 2026-09-27 03:00:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 63.8 |
| b7954a63-03cf-3ad0-a901-a9ede0f95872 | -11.9619 | -50.5251 | 2026-09-27 03:00:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 188.0 |
| 1c9558c5-9d72-33af-8afd-2ca0c5088a4d | -11.8097 | -50.5214 | 2026-09-27 03:10:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 75.2 |
| 914dda71-2817-3d7d-844d-c0fb0c14763a | -11.924 | -50.5081 | 2026-09-27 03:10:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 66.5 |
| 2e910a16-9cac-3a53-86d1-85a765bb0dbc | -7.3814 | -55.6321 | 2026-09-27 03:10:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 43.4 |
| 7e0ccfc6-7d61-3e30-a690-c46f3823def5 | -7.3999 | -55.6311 | 2026-09-27 03:10:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 62.2 |
| cf1ea482-b0e0-3dd8-bd92-66c06ed53eb5 | -11.9428 | -50.5273 | 2026-09-27 03:10:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 77.6 |
| a8d6400e-b821-3904-a4f1-59d226c3d035 | -7.3998 | -55.6511 | 2026-09-27 03:10:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 51.6 |
| 141ba3bf-887f-3b0d-8c3e-563144426d74 | -3.1953 | -51.039 | 2026-09-27 03:10:00 | GOES-19 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 58.8 |
| eacb5785-f7dd-3da6-a5a5-08312262e1ad | -11.9619 | -50.5251 | 2026-09-27 03:10:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 97.4 |
| 09f12503-2c8c-3ba5-97dc-70098964208c | -11.9622 | -50.5036 | 2026-09-27 03:10:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 123.6 |
| 26f1173f-529e-3b90-9306-5497bdc49a95 | -12.3273 | -50.3096 | 2026-09-27 03:10:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 68.8 |
| fb03fecb-c4b3-399c-897e-8ced9af9b7eb | -11.9431 | -50.5058 | 2026-09-27 03:10:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 107.4 |
| 318a37b6-19a6-3937-921c-2f05cfe435ee | -12.3082 | -50.3119 | 2026-09-27 03:10:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 90.4 |
| 6a093c62-509a-3a3e-bc5f-9d4c33bc08c5 | -5.50729 | -38.00599 | 2026-09-27 03:10:00 | NOAA-21 | ALTO SANTO | CEARÁ | Brasil | 2300705 | 23 | 33 | nan | nan | nan | Caatinga | 2.1 |
| a9284fcd-1f0f-3b19-9b0e-5b8be79c7dad | -5.5056 | -38.0042 | 2026-09-27 03:10:00 | NOAA-21 | ALTO SANTO | CEARÁ | Brasil | 2300705 | 23 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 23ffeddc-c7d3-3150-910e-32a7686e8172 | -5.51151 | -38.00515 | 2026-09-27 03:10:00 | NOAA-21 | ALTO SANTO | CEARÁ | Brasil | 2300705 | 23 | 33 | nan | nan | nan | Caatinga | 1.2 |
| a207f84e-4b81-3dac-8cbc-524e9329ae1b | -10.22535 | -36.33492 | 2026-09-27 03:13:00 | NOAA-21 | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| 2346cd56-d5c3-3410-b828-7bee974e1cfa | -8.3 | -44.15 | 2026-09-27 03:15:00 | MSG-03 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 60e66060-234d-31a0-abaa-aec55302ebd0 | -11.94 | -50.5 | 2026-09-27 03:15:00 | MSG-03 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| a7cd8a11-7b1e-32ee-a91c-b3c69e37b312 | -8.3 | -44.19 | 2026-09-27 03:15:00 | MSG-03 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 1111fa5c-3414-3cb0-8dd4-4af4112a2e14 | -8.33 | -44.2 | 2026-09-27 03:15:00 | MSG-03 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 6f5368ac-015a-3755-92a5-daa8e2750aa5 | -8.33 | -44.15 | 2026-09-27 03:15:00 | MSG-03 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 4ef829c3-84e0-3a13-975a-44404be2db24 | -8.33 | -44.11 | 2026-09-27 03:15:00 | MSG-03 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| e901f3ac-25f8-3fa8-87da-44773d7cb68e | -8.36 | -44.16 | 2026-09-27 03:15:00 | MSG-03 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 75d70547-865c-3c87-8fc4-e483e31d832f | -8.33 | -44.24 | 2026-09-27 03:15:00 | MSG-03 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 32509ae6-f690-36d9-a1ba-32a6e12e23f0 | -8.36 | -44.2 | 2026-09-27 03:15:00 | MSG-03 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| f07973ee-9276-305f-a663-5ae3431cc089 | -8.36 | -44.25 | 2026-09-27 03:15:00 | MSG-03 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 699d60a0-eb65-3352-9f8f-1b0d147c4c1c | -8.36 | -44.29 | 2026-09-27 03:15:00 | MSG-03 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 9905b8c1-c70a-31b9-b25e-394c5451e1d6 | -8.33 | -44.29 | 2026-09-27 03:15:00 | MSG-03 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 44d0785f-b374-30f5-bb21-c20a91ad20c2 | -16.5919 | -41.84218 | 2026-09-27 03:15:00 | NOAA-21 | ITINGA | MINAS GERAIS | Brasil | 3134004 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.9 |
| c62f564b-43cb-3baa-8b9d-0ed2f9e62bd0 | -15.33822 | -42.90955 | 2026-09-27 03:15:00 | NOAA-21 | MATO VERDE | MINAS GERAIS | Brasil | 3141009 | 31 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 992455e7-c476-3293-aa8d-31c081662987 | -15.60677 | -41.35172 | 2026-09-27 03:15:00 | NOAA-21 | ÁGUAS VERMELHAS | MINAS GERAIS | Brasil | 3101003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.7 |
| 0202e6f6-1af3-3ea9-baec-2a0f5462ba24 | -14.06845 | -41.93562 | 2026-09-27 03:15:00 | NOAA-21 | BRUMADO | BAHIA | Brasil | 2904605 | 29 | 33 | nan | nan | nan | Caatinga | 8.7 |
| a66edd66-0918-3918-ab59-e698e15cbcba | -15.33459 | -42.90705 | 2026-09-27 03:15:00 | NOAA-21 | MATO VERDE | MINAS GERAIS | Brasil | 3141009 | 31 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 441bfb5b-df8a-39cc-9232-86830324bcdd | -13.21213 | -42.23027 | 2026-09-27 03:15:00 | NOAA-21 | CATURAMA | BAHIA | Brasil | 2907558 | 29 | 33 | nan | nan | nan | Caatinga | 6.6 |
| afb67e96-115d-3c64-a1e0-927b01b99e7d | -13.21595 | -42.22726 | 2026-09-27 03:15:00 | NOAA-21 | CATURAMA | BAHIA | Brasil | 2907558 | 29 | 33 | nan | nan | nan | Caatinga | 2.5 |
| c44df479-b247-3526-9562-b582a5e04d20 | -13.20963 | -42.22421 | 2026-09-27 03:15:00 | NOAA-21 | CATURAMA | BAHIA | Brasil | 2907558 | 29 | 33 | nan | nan | nan | Caatinga | 3.5 |
| 48b2de48-e328-3e47-97b3-064c18a0d139 | -21.52227 | -45.11364 | 2026-09-27 03:17:00 | NOAA-21 | CARMO DA CACHOEIRA | MINAS GERAIS | Brasil | 3113909 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.7 |
| 446eb5da-ffdb-3c2e-835b-f5622cda33b7 | -20.11477 | -43.59343 | 2026-09-27 03:17:00 | NOAA-21 | SANTA BÁRBARA | MINAS GERAIS | Brasil | 3157203 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.6 |
| 85e9c286-4f9d-300d-bda8-7ff5767fea13 | -11.9431 | -50.5058 | 2026-09-27 03:20:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 163.2 |
| d484915a-97de-3310-a23d-a09fa1ca4faf | -3.1953 | -51.039 | 2026-09-27 03:20:00 | GOES-19 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 59.4 |
| 2b77a28a-6a70-33d9-8cea-8ab1838ab980 | -11.8097 | -50.5214 | 2026-09-27 03:20:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 65.2 |
| 1b17eeb0-8a1d-3c8d-9dfa-ec3b3ff2fd33 | -7.3998 | -55.6511 | 2026-09-27 03:20:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 54.7 |
| d099fc7a-81a8-39a0-9833-5fbbbfea30d4 | -12.2834 | -50.6797 | 2026-09-27 03:20:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 69.3 |
| 37695b54-d977-3edf-95cc-38fe768e951f | -11.9428 | -50.5273 | 2026-09-27 03:20:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 99.9 |
| 7b950997-8e26-38ee-941f-71b074f01828 | -11.9622 | -50.5036 | 2026-09-27 03:20:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 112.9 |
| 17e6adee-f916-320c-9598-b09824632588 | -11.924 | -50.5081 | 2026-09-27 03:20:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 70.5 |
| 93bece52-4da6-3007-aa7c-5a3bd1c6b5f3 | -11.8669 | -50.5147 | 2026-09-27 03:20:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 66.5 |
| 198dc116-4085-3de3-8d4b-412cc5f6a8a9 | -12.283 | -50.7011 | 2026-09-27 03:20:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 106.8 |
| b898c493-3881-397a-b901-a7764fd8b34e | -7.3999 | -55.6311 | 2026-09-27 03:20:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 75.1 |
| feda813b-2cb2-3682-91eb-61b2b89be39e | -7.3814 | -55.6321 | 2026-09-27 03:20:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 61.7 |
| 0f1abf84-ef59-368f-a032-2f3880380cf4 | -12.2643 | -50.682 | 2026-09-27 03:20:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 84.3 |
| 5db28c3d-b70f-376e-966d-2bf796ec46c6 | -11.8856 | -50.534 | 2026-09-27 03:20:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 66.7 |
| da53d014-c3e6-3a08-828a-8c04cade096d | -7.3812 | -55.6521 | 2026-09-27 03:20:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 45.1 |
| 8661128e-b5c5-3549-aebe-c41cea1c25fd | -11.9619 | -50.5251 | 2026-09-27 03:20:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 79.6 |
| 2c60614f-e75f-3192-be39-daf759f8eb8d | -11.8859 | -50.5125 | 2026-09-27 03:20:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 78.0 |
| b5d73d0d-c082-3413-9d66-5965f9603edd | -12.2639 | -50.7034 | 2026-09-27 03:20:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 152.6 |
| b1ced2dc-f76d-3809-81a5-45377c52679d | -11.9431 | -50.5058 | 2026-09-27 03:30:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 92.6 |
| 27ee9c13-ba69-332a-9e8f-6036310f52d4 | -12.283 | -50.7011 | 2026-09-27 03:30:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 84.2 |
| 648c00f7-9d79-39f5-8ab3-1ca8f90e622d | -12.2639 | -50.7034 | 2026-09-27 03:30:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 107.3 |
| dd806c57-a08e-3d62-a7f8-1637763c30b1 | -3.1953 | -51.039 | 2026-09-27 03:30:00 | GOES-19 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 47.1 |
| 40b3ce12-b016-396a-8554-0651bad4bbbf | -11.9428 | -50.5273 | 2026-09-27 03:30:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 74.4 |
| 20dbd7e8-7e24-3cd2-8a32-c94af80a1dd6 | -11.8669 | -50.5147 | 2026-09-27 03:30:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 71.1 |
| 2ee8082f-e86f-3390-9366-b87b2801e2e0 | -11.9622 | -50.5036 | 2026-09-27 03:30:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 71.7 |
| 776e620a-3fa8-390f-9c54-cfa7249c4b2b | -7.3998 | -55.6511 | 2026-09-27 03:30:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 45.5 |
| 571652da-81c1-3a0a-a4a6-907b5b5cef13 | -11.8097 | -50.5214 | 2026-09-27 03:30:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 96.8 |
| eb810eaf-7e28-39d5-865b-57acedaa4756 | -7.3999 | -55.6311 | 2026-09-27 03:30:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 50.2 |
| 98a32e4e-9c33-3708-a9a3-5feb17681d82 | -7.3814 | -55.6321 | 2026-09-27 03:30:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 44.0 |
| fc560185-ec57-3a44-abea-1a9bc55e1880 | -11.8856 | -50.534 | 2026-09-27 03:30:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 79.8 |
| 156406ab-506c-3fdb-8f47-99d9d1e99616 | -11.8859 | -50.5125 | 2026-09-27 03:30:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 89.1 |
| 21bf1254-2e4a-3606-a774-78285e1b9de5 | -7.3812 | -55.6521 | 2026-09-27 03:40:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 40.9 |
| 8a832417-ab69-3d68-983d-0665171a9311 | -7.3999 | -55.6311 | 2026-09-27 03:40:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 52.8 |
| b41a960c-8bc4-36fe-8875-481827b85355 | -11.9431 | -50.5058 | 2026-09-27 03:40:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 86.6 |
| 1a15baf5-daef-382c-b5cf-88e4ca42cebc | -12.0369 | -50.6019 | 2026-09-27 03:40:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 126.0 |
| c4d5f560-27fd-35d5-9705-e40b6470bee9 | -7.3998 | -55.6511 | 2026-09-27 03:40:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 49.5 |
| f0af906f-d5c7-38ad-ae24-e489c73daaed | -11.8097 | -50.5214 | 2026-09-27 03:40:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 77.6 |
| 741f4c75-a5a4-33ba-ab39-4cec070f9991 | -11.8859 | -50.5125 | 2026-09-27 03:40:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 88.8 |
| 7a0d0430-e5ea-3f1f-96d7-7bde454ccb86 | -7.3814 | -55.6321 | 2026-09-27 03:40:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 44.5 |
| f8ef3a07-b45e-33d0-a804-3ecc3f8f9331 | -11.8856 | -50.534 | 2026-09-27 03:40:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 73.4 |
| 68511240-439b-3176-a355-ef8e6f9d02d9 | -8.33353 | -44.16866 | 2026-09-27 03:47:00 | NPP-375D | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 17f43dda-f558-34a5-b265-97ce42cf6f4c | -6.82212 | -39.32721 | 2026-09-27 03:47:00 | NPP-375D | VÁRZEA ALEGRE | CEARÁ | Brasil | 2314003 | 23 | 33 | nan | nan | nan | Caatinga | 3.7 |
| cbc4aa10-4cf5-3b3b-adc5-e8e9b19eceb8 | -7.35839 | -42.10363 | 2026-09-27 03:47:00 | NPP-375D | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| bf19ed06-91ec-3135-a5ff-e0f7c4161a59 | -8.34957 | -44.18642 | 2026-09-27 03:47:00 | NPP-375D | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 141.2 |
| fc79fb6b-c65a-3a6d-87ee-d7f00122bafb | -7.37302 | -42.10916 | 2026-09-27 03:47:00 | NPP-375D | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 4920eac4-e1ce-38fd-9ec5-acdc8d45007a | -8.34534 | -44.17758 | 2026-09-27 03:47:00 | NPP-375D | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 4.7 |
| ab78b080-15a2-3fcd-bb4e-5db8b33ceef0 | -6.83561 | -43.52051 | 2026-09-27 03:47:00 | NPP-375D | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| eaaf9011-9df9-3ba0-ae77-1f1cb184a10e | -8.35528 | -44.18734 | 2026-09-27 03:47:00 | NPP-375D | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 141.2 |
| 5ea362d4-0463-3c7a-8215-e291b43950f7 | -5.73803 | -45.02438 | 2026-09-27 03:47:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 9e8668e1-f39f-32fb-ae1e-8b88c7aaf501 | -7.36591 | -42.11996 | 2026-09-27 03:47:00 | NPP-375D | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| f229e3b4-8bce-3a9d-8584-e7c13d7a5e2c | -7.34186 | -42.0796 | 2026-09-27 03:47:00 | NPP-375D | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| ff1dc920-ffed-3f9c-8f50-ad3664830b46 | -6.93217 | -41.61334 | 2026-09-27 03:47:00 | NPP-375D | PICOS | PIAUÍ | Brasil | 2208007 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| af257ebf-9730-3206-a4f2-d14cfa7dd550 | -6.83546 | -43.56925 | 2026-09-27 03:47:00 | NPP-375D | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 7c4da712-9d24-3197-afc4-3ea777ce3a11 | -8.36035 | -44.16023 | 2026-09-27 03:47:00 | NPP-375D | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 81.4 |
| 53b411fc-88b2-328a-bf5c-336ea4c41455 | -6.84188 | -43.51768 | 2026-09-27 03:47:00 | NPP-375D | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 467d6630-6c8e-3d36-adae-10169d8b396f | -5.17549 | -46.1168 | 2026-09-27 03:47:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |


[Clique aqui para ver as próximas entradas](README10.md)
