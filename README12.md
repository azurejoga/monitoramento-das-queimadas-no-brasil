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

## Dados Diários - Página 12

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 84095f7f-5d50-301e-b0f2-e9f831c005dc | -5.1831 | -41.14562 | 2026-09-27 03:49:00 | NPP-375D | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 5.8 |
| 7f341b9e-10f9-3c88-a4d6-ad5aa8185aab | -12.6688 | -47.31157 | 2026-09-27 03:49:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 2f93cbca-226d-3679-97c4-a91fcf6d14ff | -15.47152 | -46.15364 | 2026-09-27 03:49:00 | NPP-375D | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 7102c837-89fc-32bf-a05c-97cffbcf18c8 | -13.85275 | -43.99849 | 2026-09-27 03:49:00 | NPP-375D | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 8b5d2746-9f81-3cc7-9493-5b29addfd777 | -14.11734 | -46.33393 | 2026-09-27 03:49:00 | NPP-375D | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 2c5540cc-ee79-341e-aa1a-e40f6b0a8659 | -2.90755 | -45.41889 | 2026-09-27 03:49:00 | NPP-375D | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 0c5260ba-f4a9-31b0-8b31-d60a94a737a2 | -13.33744 | -46.80499 | 2026-09-27 03:49:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 0e232421-9893-32e9-be42-3ca9b9240461 | -2.9297 | -45.50588 | 2026-09-27 03:49:00 | NPP-375D | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 80621247-e03b-375f-bded-adffabcd8fc4 | -14.81957 | -49.26962 | 2026-09-27 03:49:00 | NPP-375D | SÃO LUIZ DO NORTE | GOIÁS | Brasil | 5220157 | 52 | 33 | nan | nan | nan | Cerrado | 7.1 |
| d9b485e4-dbdf-3f4b-ba24-6504ca4d51c6 | -12.4775 | -47.48471 | 2026-09-27 03:49:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 1f1bf13d-eef0-3ace-912e-86760054070b | -13.21128 | -42.22781 | 2026-09-27 03:49:00 | NPP-375D | CATURAMA | BAHIA | Brasil | 2907558 | 29 | 33 | nan | nan | nan | Caatinga | 83.8 |
| d6618762-8a27-3c99-82bc-f9060388f891 | -14.96302 | -47.53628 | 2026-09-27 03:49:00 | NPP-375D | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 295bf725-3a62-320e-8778-2c5928312f53 | -3.91178 | -43.02625 | 2026-09-27 03:49:00 | NPP-375D | BURITI | MARANHÃO | Brasil | 2102200 | 21 | 33 | nan | nan | nan | Cerrado | 5.9 |
| a877900c-d036-38c9-8d34-21e94828f352 | -4.84596 | -42.89249 | 2026-09-27 03:49:00 | NPP-375D | UNIÃO | PIAUÍ | Brasil | 2211100 | 22 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 2ee7cd4c-e2c0-3d18-b741-5d8ebcf0a3f0 | -16.78482 | -39.42674 | 2026-09-27 03:49:00 | NPP-375D | PORTO SEGURO | BAHIA | Brasil | 2925303 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 8795cb0a-1933-3936-812d-1b694870fa0a | -13.21002 | -42.22995 | 2026-09-27 03:49:00 | NPP-375D | CATURAMA | BAHIA | Brasil | 2907558 | 29 | 33 | nan | nan | nan | Caatinga | 41.6 |
| 3f5523d1-3a3d-3dca-966a-c87ef9458fd9 | -2.92863 | -45.51191 | 2026-09-27 03:49:00 | NPP-375D | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 93115819-8e0f-3509-ba6b-06d85589618a | -13.09004 | -47.41398 | 2026-09-27 03:49:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 3089b9a8-543c-3402-94ef-19bb392400b0 | -3.91986 | -43.02183 | 2026-09-27 03:49:00 | NPP-375D | BURITI | MARANHÃO | Brasil | 2102200 | 21 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 0449f50f-c4a9-3426-ba2a-7c5a7f4483ea | -5.50668 | -38.00772 | 2026-09-27 03:49:00 | NPP-375D | ALTO SANTO | CEARÁ | Brasil | 2300705 | 23 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 05761e24-ec1f-3d7d-9867-859de81ba39a | -12.47157 | -47.48591 | 2026-09-27 03:49:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| d8192c01-ae7e-32ca-b0f8-4017e4642c1d | -14.81304 | -43.31049 | 2026-09-27 03:49:00 | NPP-375D | GAMELEIRAS | MINAS GERAIS | Brasil | 3127339 | 31 | 33 | nan | nan | nan | Caatinga | 1.3 |
| e7350b4c-b9e6-3bea-a22c-96611d4f3c68 | -13.44092 | -43.823 | 2026-09-27 03:49:00 | NPP-375D | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 60d5daef-f106-3dfe-b5c6-d8e6d2a9cedf | -13.33037 | -46.80822 | 2026-09-27 03:49:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 10b9162a-74df-31b3-97f1-ad831e27fc82 | -14.95695 | -47.53424 | 2026-09-27 03:49:00 | NPP-375D | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 1ee5c1fb-b22c-3bb2-9b3e-cfc016134751 | -4.28341 | -44.59109 | 2026-09-27 03:49:00 | NPP-375D | SÃO LUÍS GONZAGA DO MARANHÃO | MARANHÃO | Brasil | 2111409 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 3e9ddc1c-0ba5-3669-a0d5-633d7c8a4f7b | -14.50225 | -48.34036 | 2026-09-27 03:49:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 469dfbd5-3625-3dc8-a802-f4944dda4410 | -14.72495 | -45.57716 | 2026-09-27 03:49:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e82cc595-196a-3cae-8d78-809502b8e74b | -12.72491 | -41.80281 | 2026-09-27 03:49:00 | NPP-375D | BONINAL | BAHIA | Brasil | 2904001 | 29 | 33 | nan | nan | nan | Caatinga | 1.7 |
| bcc3f556-e572-3cd2-bbf6-0687042ece09 | -4.2801 | -44.58942 | 2026-09-27 03:49:00 | NPP-375D | SÃO LUÍS GONZAGA DO MARANHÃO | MARANHÃO | Brasil | 2111409 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 4b00b09f-ec01-3ddd-b0ab-0fc7415fb3e5 | -11.34448 | -41.85022 | 2026-09-27 03:49:00 | NPP-375D | IRECÊ | BAHIA | Brasil | 2914604 | 29 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 879153a6-9ddd-3788-9525-351f0691862e | -4.8466 | -42.8888 | 2026-09-27 03:49:00 | NPP-375D | UNIÃO | PIAUÍ | Brasil | 2211100 | 22 | 33 | nan | nan | nan | Cerrado | 3.1 |
| b6293b8a-3ad6-33bc-8afd-4b0ccd0a229e | -14.49697 | -48.33307 | 2026-09-27 03:49:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 0e623992-9e32-3c5b-ac9c-a8834fe4f33f | -4.74391 | -43.47742 | 2026-09-27 03:49:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| cb874fb6-5348-3775-b7a1-dacb5d1ff072 | -11.9431 | -50.5058 | 2026-09-27 03:50:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 69.3 |
| ca8ef977-e36e-3fa7-8a47-40a64513229f | -3.1953 | -51.039 | 2026-09-27 03:50:00 | GOES-19 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 47.8 |
| f2c6106d-37f4-3f47-a6de-8f49d80f4133 | -12.2639 | -50.7034 | 2026-09-27 03:50:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 66.9 |
| 536fd53d-c8d8-3867-8532-2d284b573ed5 | -11.8097 | -50.5214 | 2026-09-27 03:50:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 58.1 |
| 9aa5c870-cb38-319f-8273-fbcc92243a93 | -12.0369 | -50.6019 | 2026-09-27 03:50:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 89.7 |
| b052a222-5551-3005-b352-df2135c1bda5 | -11.8856 | -50.534 | 2026-09-27 03:50:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 67.0 |
| f0401b4a-3f65-3fe9-84e8-465ac4467ded | -11.8859 | -50.5125 | 2026-09-27 03:50:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 100.9 |
| 5b370f4e-c337-33fa-bcfe-a3a42fdde8cb | -7.3999 | -55.6311 | 2026-09-27 03:50:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 42.8 |
| 70f5e677-3373-36bc-8a2c-f1b226e5c592 | -20.68882 | -47.52045 | 2026-09-27 03:51:00 | NPP-375D | RESTINGA | SÃO PAULO | Brasil | 3542701 | 35 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 69ae193e-41f8-3da7-bb5b-568c918f6515 | -20.19429 | -46.20102 | 2026-09-27 03:51:00 | NPP-375D | BAMBUÍ | MINAS GERAIS | Brasil | 3105103 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 2ef1dc5f-4f42-3e1d-bb9d-c682f0cb60e9 | -21.52384 | -45.11047 | 2026-09-27 03:51:00 | NPP-375D | CARMO DA CACHOEIRA | MINAS GERAIS | Brasil | 3113909 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| eba7a562-d3ce-30af-b684-1dbb70d24538 | -20.69136 | -47.52291 | 2026-09-27 03:51:00 | NPP-375D | RESTINGA | SÃO PAULO | Brasil | 3542701 | 35 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 77771749-375e-3dd4-af95-536651504348 | -21.09155 | -49.0615 | 2026-09-27 03:51:00 | NPP-375D | CATIGUÁ | SÃO PAULO | Brasil | 3511201 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 131f5d9a-b2b6-32b4-90e9-84932f9929db | -22.17312 | -42.123 | 2026-09-27 03:51:00 | NPP-375D | TRAJANO DE MORAES | RIO DE JANEIRO | Brasil | 3305901 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 54eac56e-3e3e-3e16-8dcf-fc6731bffdc0 | -19.9078 | -46.89943 | 2026-09-27 03:51:00 | NPP-375D | TAPIRA | MINAS GERAIS | Brasil | 3168101 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| eaee5e9d-26c7-3989-b011-81a7fbb4ab18 | -18.54775 | -43.5836 | 2026-09-27 03:51:00 | NPP-375D | SERRO | MINAS GERAIS | Brasil | 3167103 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| de34f628-2479-3da8-ac91-e749ab80d168 | -19.6397 | -49.68972 | 2026-09-27 03:51:00 | NPP-375D | CAMPINA VERDE | MINAS GERAIS | Brasil | 3111101 | 31 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 595d0817-dc69-3e8e-bfcc-54418b5e556f | -20.68792 | -47.52442 | 2026-09-27 03:51:00 | NPP-375D | RESTINGA | SÃO PAULO | Brasil | 3542701 | 35 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 352165b0-7e97-36d6-908b-308959748ee9 | -17.79203 | -47.15936 | 2026-09-27 03:51:00 | NPP-375D | GUARDA-MOR | MINAS GERAIS | Brasil | 3128600 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| e1f9a7d4-f4d7-323d-b297-af17b8316d6c | -18.46388 | -43.12898 | 2026-09-27 03:51:00 | NPP-375D | SERRA AZUL DE MINAS | MINAS GERAIS | Brasil | 3166501 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 5b4a7ea5-6f02-3cb6-9e09-d764352c9e46 | -17.79115 | -47.16343 | 2026-09-27 03:51:00 | NPP-375D | GUARDA-MOR | MINAS GERAIS | Brasil | 3128600 | 31 | 33 | nan | nan | nan | Cerrado | 3.6 |
| bab117ba-a2f6-3f4d-81a4-ca8443725bd9 | -19.63973 | -49.69155 | 2026-09-27 03:51:00 | NPP-375D | CAMPINA VERDE | MINAS GERAIS | Brasil | 3111101 | 31 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 9acad89a-b2fd-399d-9d72-72b779677b85 | -21.52275 | -45.11446 | 2026-09-27 03:51:00 | NPP-375D | CARMO DA CACHOEIRA | MINAS GERAIS | Brasil | 3113909 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.5 |
| f092cea2-419c-3ddb-aba0-90c5f88d1010 | -21.52269 | -45.11589 | 2026-09-27 03:51:00 | NPP-375D | CARMO DA CACHOEIRA | MINAS GERAIS | Brasil | 3113909 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.4 |
| 8e6aed08-75f7-3153-99dd-36b78594b83a | -17.79022 | -47.16769 | 2026-09-27 03:51:00 | NPP-375D | GUARDA-MOR | MINAS GERAIS | Brasil | 3128600 | 31 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 96230945-95c6-3fb9-b718-dd9b9d96672b | -19.63835 | -49.69535 | 2026-09-27 03:51:00 | NPP-375D | CAMPINA VERDE | MINAS GERAIS | Brasil | 3111101 | 31 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 5c264eec-ff8b-36a6-9fb8-ebf883c1358d | -20.0412 | -40.74681 | 2026-09-27 03:51:00 | NPP-375D | SANTA MARIA DE JETIBÁ | ESPÍRITO SANTO | Brasil | 3204559 | 32 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| d62907af-ca87-3d08-ba35-8db135405fbc | -23.0047 | -48.61608 | 2026-09-27 03:51:00 | NPP-375D | BOTUCATU | SÃO PAULO | Brasil | 3507506 | 35 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 3691211e-7e29-3b19-843a-1ec51418a204 | -20.8543 | -49.06726 | 2026-09-27 03:51:00 | NPP-375D | TABAPUÃ | SÃO PAULO | Brasil | 3552601 | 35 | 33 | nan | nan | nan | Mata Atlântica | 5.1 |
| eade9ac3-4f31-3f17-b22f-b32d2962747f | -20.82187 | -44.98908 | 2026-09-27 03:51:00 | NPP-375D | SANTO ANTÔNIO DO AMPARO | MINAS GERAIS | Brasil | 3159902 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| a4577e59-6dab-3f32-9ef3-57a8b5afbbe5 | -18.46499 | -43.13158 | 2026-09-27 03:51:00 | NPP-375D | SERRA AZUL DE MINAS | MINAS GERAIS | Brasil | 3166501 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 69ee18ed-10dc-3053-9030-3cc626dd899b | -22.99906 | -48.61456 | 2026-09-27 03:51:00 | NPP-375D | BOTUCATU | SÃO PAULO | Brasil | 3507506 | 35 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ab4f75fb-33c8-3a75-8b33-c61cdcdbe0fb | -18.01824 | -47.63879 | 2026-09-27 03:51:00 | NPP-375D | CATALÃO | GOIÁS | Brasil | 5205109 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| fad33c78-7758-3065-9a64-81edeb3dce40 | -19.63842 | -49.69717 | 2026-09-27 03:51:00 | NPP-375D | CAMPINA VERDE | MINAS GERAIS | Brasil | 3111101 | 31 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 1935dd67-cf70-37f3-a782-60d4b5ac985b | -21.09039 | -49.06654 | 2026-09-27 03:51:00 | NPP-375D | CATIGUÁ | SÃO PAULO | Brasil | 3511201 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 98dca913-787c-3f6e-ab4c-b606c2fc7795 | -18.55232 | -43.58445 | 2026-09-27 03:51:00 | NPP-375D | PRESIDENTE KUBITSCHEK | MINAS GERAIS | Brasil | 3153301 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| b2040dab-af76-3d3e-af14-5d389ff825c3 | -17.78927 | -47.17204 | 2026-09-27 03:51:00 | NPP-375D | GUARDA-MOR | MINAS GERAIS | Brasil | 3128600 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| f9b0885a-485e-341e-81ba-c1787a1d77c9 | -18.02404 | -47.64059 | 2026-09-27 03:51:00 | NPP-375D | CATALÃO | GOIÁS | Brasil | 5205109 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 23ababa3-4645-38f7-bb8a-9355b5deaed2 | -18.7994 | -48.04638 | 2026-09-27 03:51:00 | NPP-375D | ARAGUARI | MINAS GERAIS | Brasil | 3103504 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 76895e9f-f7f3-3cf5-8ba4-b0c0e2edc1e7 | -18.79353 | -48.04461 | 2026-09-27 03:51:00 | NPP-375D | ARAGUARI | MINAS GERAIS | Brasil | 3103504 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 5f3b6c7a-93b7-3f1a-ae8d-a8e570f1e3fa | -29.55142 | -55.53259 | 2026-09-27 03:55:00 | NPP-375D | MANOEL VIANA | RIO GRANDE DO SUL | Brasil | 4311759 | 43 | 33 | nan | nan | nan | Pampa | 2.8 |
| 1ba5bb4a-df4b-3a5d-9ba5-1a8077c2de4e | -29.55076 | -55.52779 | 2026-09-27 03:55:00 | NPP-375D | MANOEL VIANA | RIO GRANDE DO SUL | Brasil | 4311759 | 43 | 33 | nan | nan | nan | Pampa | 3.0 |
| 974ee629-0734-3557-b80e-c3c395d32b20 | -6.1485 | -47.2871 | 2026-09-27 04:00:00 | GOES-19 | CAMPESTRE DO MARANHÃO | MARANHÃO | Brasil | 2102556 | 21 | 33 | nan | nan | nan | Cerrado | 126.7 |
| 1b8e36d9-20a2-3950-8bd5-d54aff74855c | -11.9431 | -50.5058 | 2026-09-27 04:00:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 78.9 |
| 7872bda3-b6e2-3849-a135-c89081f7ef2a | -11.905 | -50.5103 | 2026-09-27 04:00:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 54.1 |
| 6a158d6a-4671-3df6-b890-2fbd39f8f4b1 | -11.8859 | -50.5125 | 2026-09-27 04:00:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 82.1 |
| a69341ec-7e0d-36f2-9f49-d3153c089236 | -6.1672 | -47.2858 | 2026-09-27 04:00:00 | GOES-19 | CAMPESTRE DO MARANHÃO | MARANHÃO | Brasil | 2102556 | 21 | 33 | nan | nan | nan | Cerrado | 73.6 |
| adbfbf8a-04c5-3d25-bd5d-96ccb59bc8fb | -6.1487 | -47.2651 | 2026-09-27 04:00:00 | GOES-19 | CAMPESTRE DO MARANHÃO | MARANHÃO | Brasil | 2102556 | 21 | 33 | nan | nan | nan | Cerrado | 60.0 |
| 2b82cb12-15af-3000-9890-4e98f0a44e0b | -11.924 | -50.5081 | 2026-09-27 04:00:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 58.9 |
| 4a6f91b2-c1cc-33ed-8de8-cac537fa0170 | -3.46514 | -39.58456 | 2026-09-27 04:06:00 | NOAA-20 | ITAPIPOCA | CEARÁ | Brasil | 2306405 | 23 | 33 | nan | nan | nan | Caatinga | 1.5 |
| f52bf646-00ca-33bb-b298-2d7cc847cb8d | -3.48392 | -39.61571 | 2026-09-27 04:06:00 | NOAA-20 | ITAPIPOCA | CEARÁ | Brasil | 2306405 | 23 | 33 | nan | nan | nan | Caatinga | 2.1 |
| d8dd3870-de15-33a6-bfea-c0ca21aac45e | -1.86191 | -47.98306 | 2026-09-27 04:06:00 | NOAA-20 | CONCÓRDIA DO PARÁ | PARÁ | Brasil | 1502756 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 1718899a-4e35-362c-8b1e-0d52df4f3348 | -2.73894 | -49.46761 | 2026-09-27 04:06:00 | NOAA-20 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 1d50c4ab-89de-341c-8548-4694a9b891de | -1.86273 | -47.97864 | 2026-09-27 04:06:00 | NOAA-20 | CONCÓRDIA DO PARÁ | PARÁ | Brasil | 1502756 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b47e5403-74ed-3a0b-9c5a-cc259b33dafa | 1.96737 | -50.90554 | 2026-09-27 04:06:00 | NOAA-20 | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 4.6 |
| d2f58d6d-bff5-3dd5-9fa8-c6080096b836 | -1.85719 | -47.97903 | 2026-09-27 04:06:00 | NOAA-20 | CONCÓRDIA DO PARÁ | PARÁ | Brasil | 1502756 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 47358637-ed87-318d-b1ce-a5f108d26655 | -2.44511 | -49.22894 | 2026-09-27 04:06:00 | NOAA-20 | MOCAJUBA | PARÁ | Brasil | 1504604 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 6e97a495-4e41-36fc-a989-57d56535a948 | -1.86246 | -47.9798 | 2026-09-27 04:06:00 | NOAA-20 | CONCÓRDIA DO PARÁ | PARÁ | Brasil | 1502756 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 0e537008-4857-3358-becf-1e1e6258c85f | -3.2639 | -46.62104 | 2026-09-27 04:06:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 7e9069d3-b370-3af5-bf16-24e60f6c78f2 | -1.85665 | -47.98226 | 2026-09-27 04:06:00 | NOAA-20 | CONCÓRDIA DO PARÁ | PARÁ | Brasil | 1502756 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 54acc921-d4c0-39f6-9ee0-59d6f1a095aa | -2.92396 | -45.50813 | 2026-09-27 04:06:00 | NOAA-20 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 498182eb-0180-3bf1-bfc7-856ec82a5958 | -0.51303 | -49.13076 | 2026-09-27 04:06:00 | NOAA-20 | CACHOEIRA DO ARARI | PARÁ | Brasil | 1502004 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| b2d0e8f4-eb49-3e11-bd74-0cc83fdbd8d7 | -2.90938 | -45.42558 | 2026-09-27 04:06:00 | NOAA-20 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 3.9 |
| a2fde04b-2f8b-3d57-9638-e054e1c41028 | -2.90572 | -45.4207 | 2026-09-27 04:06:00 | NOAA-20 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| caed42cd-7f39-3965-b728-b8e9f798661f | 0.70072 | -51.44137 | 2026-09-27 04:06:00 | NOAA-20 | PORTO GRANDE | AMAPÁ | Brasil | 1600535 | 16 | 33 | nan | nan | nan | Amazônia | 2.8 |
| d60c7a6b-21d2-3bb9-bfb6-52bfc22e1fe9 | -0.5046 | -49.14603 | 2026-09-27 04:06:00 | NOAA-20 | CACHOEIRA DO ARARI | PARÁ | Brasil | 1502004 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |


[Clique aqui para ver as próximas entradas](README13.md)
