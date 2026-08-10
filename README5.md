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

## Dados Diários - Página 5

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| b9043647-be59-3463-b364-415bc5fabb72 | -20.04523 | -43.76387 | 2026-08-10 03:51:00 | NPP-375D | RIO ACIMA | MINAS GERAIS | Brasil | 3154804 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 037cb3f6-b7c1-3249-a2da-29555ab0369c | -22.22733 | -43.02795 | 2026-08-10 03:51:00 | NPP-375D | PETRÓPOLIS | RIO DE JANEIRO | Brasil | 3303906 | 33 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| ec89e799-f1cd-33a7-9aa5-4338407ff23d | -20.36826 | -42.91198 | 2026-08-10 03:51:00 | NPP-375D | PONTE NOVA | MINAS GERAIS | Brasil | 3152105 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| b0a77655-349d-3e95-981f-7e9ba33f9439 | -20.04424 | -43.76886 | 2026-08-10 03:51:00 | NPP-375D | RIO ACIMA | MINAS GERAIS | Brasil | 3154804 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 5b1e80ea-f649-332b-9e22-5ca06c0410b2 | -19.7167 | -49.13372 | 2026-08-10 03:51:00 | NPP-375D | COMENDADOR GOMES | MINAS GERAIS | Brasil | 3116902 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| a999c365-7a87-3a84-800f-0a6c36cfb429 | -20.0486 | -43.7701 | 2026-08-10 03:51:00 | NPP-375D | RIO ACIMA | MINAS GERAIS | Brasil | 3154804 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 827af338-dbf0-32cd-bb5f-00f188a5445a | -22.2233 | -43.02696 | 2026-08-10 03:51:00 | NPP-375D | PETRÓPOLIS | RIO DE JANEIRO | Brasil | 3303906 | 33 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| 1b7e682f-9803-3f98-b2d4-812032880278 | -20.04759 | -43.77521 | 2026-08-10 03:51:00 | NPP-375D | RIO ACIMA | MINAS GERAIS | Brasil | 3154804 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| afde2ed0-e91a-3c02-aa46-5e4fe3466cb0 | -20.37794 | -41.60913 | 2026-08-10 03:51:00 | NPP-375D | IRUPI | ESPÍRITO SANTO | Brasil | 3202652 | 32 | 33 | nan | nan | nan | Mata Atlântica | 3.0 |
| 020ea1be-b015-31a2-8c58-84120d1f634c | -20.50269 | -43.62908 | 2026-08-10 03:51:00 | NPP-375D | OURO BRANCO | MINAS GERAIS | Brasil | 3145901 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 8e042880-6297-31a9-b7af-6e6ac9441dae | -22.22396 | -43.02361 | 2026-08-10 03:51:00 | NPP-375D | PETRÓPOLIS | RIO DE JANEIRO | Brasil | 3303906 | 33 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| 4c359f5c-9b84-3a59-bce9-2a6178789d89 | -20.50161 | -42.38441 | 2026-08-10 03:51:00 | NPP-375D | PEDRA BONITA | MINAS GERAIS | Brasil | 3148756 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.8 |
| c721e743-bb38-33df-8188-7702d2c06391 | -18.8153 | -49.64716 | 2026-08-10 03:51:00 | NPP-375D | ITUIUTABA | MINAS GERAIS | Brasil | 3134202 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.5 |
| 990c6f00-ec41-3d7d-adf1-d1992d772960 | -20.5045 | -43.64276 | 2026-08-10 03:51:00 | NPP-375D | OURO BRANCO | MINAS GERAIS | Brasil | 3145901 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.3 |
| afa6d93d-d813-3135-a0a1-0d3b9760c235 | -20.50013 | -43.64198 | 2026-08-10 03:51:00 | NPP-375D | OURO BRANCO | MINAS GERAIS | Brasil | 3145901 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 1763ddea-6b17-3333-b3c4-dd19c0c9c4d9 | -22.22056 | -43.01936 | 2026-08-10 03:51:00 | NPP-375D | PETRÓPOLIS | RIO DE JANEIRO | Brasil | 3303906 | 33 | 33 | nan | nan | nan | Mata Atlântica | 3.5 |
| db757734-454a-3bb4-b1af-8d601f4d681c | -20.39741 | -42.82639 | 2026-08-10 03:51:00 | NPP-375D | PONTE NOVA | MINAS GERAIS | Brasil | 3152105 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 874ec695-90fb-32f1-ac27-e6f04320777a | -21.32043 | -43.78178 | 2026-08-10 03:51:00 | NPP-375D | ANTÔNIO CARLOS | MINAS GERAIS | Brasil | 3102902 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 60f1f6d9-e6a9-35ae-8f5f-fa9b928f9ba5 | -20.50099 | -43.63767 | 2026-08-10 03:51:00 | NPP-375D | OURO BRANCO | MINAS GERAIS | Brasil | 3145901 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| ab98798f-fdf7-3bb9-8950-beba0e87c078 | -19.71564 | -49.12982 | 2026-08-10 03:51:00 | NPP-375D | COMENDADOR GOMES | MINAS GERAIS | Brasil | 3116902 | 31 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 0fe04180-8fb5-3a87-b4a8-c45bb1688e4a | -20.0408 | -43.76304 | 2026-08-10 03:51:00 | NPP-375D | RIO ACIMA | MINAS GERAIS | Brasil | 3154804 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 62b76f2f-1673-30c7-b4d5-9a2cda970cfe | -20.37243 | -42.91282 | 2026-08-10 03:51:00 | NPP-375D | PONTE NOVA | MINAS GERAIS | Brasil | 3152105 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| fde984e1-f7bb-3741-99fe-ba5be950835b | -20.75469 | -44.73081 | 2026-08-10 03:51:00 | NPP-375D | OLIVEIRA | MINAS GERAIS | Brasil | 3145604 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 229716e7-040e-3da1-9ab4-7fcfbf09a88a | -20.37319 | -42.90879 | 2026-08-10 03:51:00 | NPP-375D | PONTE NOVA | MINAS GERAIS | Brasil | 3152105 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| ee2a7519-2901-3fd4-b933-8a97491ab263 | -20.50184 | -43.63335 | 2026-08-10 03:51:00 | NPP-375D | OURO BRANCO | MINAS GERAIS | Brasil | 3145901 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| a5b8a06c-8022-3599-ba2a-8c23c3000aef | -20.50533 | -43.63855 | 2026-08-10 03:51:00 | NPP-375D | OURO BRANCO | MINAS GERAIS | Brasil | 3145901 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.3 |
| d9c70d17-8e01-3f8e-b84f-7e0d69beeb1c | -19.1814 | -47.18742 | 2026-08-10 03:51:00 | NPP-375D | PERDIZES | MINAS GERAIS | Brasil | 3149804 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| eb585ddc-4d24-33e7-831f-612d2b7c3af7 | -18.81932 | -49.65406 | 2026-08-10 03:51:00 | NPP-375D | ITUIUTABA | MINAS GERAIS | Brasil | 3134202 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.0 |
| 46aa7126-71e2-3681-8d3e-b6dc1bc1513d | -19.17588 | -47.18601 | 2026-08-10 03:51:00 | NPP-375D | PERDIZES | MINAS GERAIS | Brasil | 3149804 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 458071dd-fb6c-368c-80da-93eb6bd18caf | -19.84277 | -44.98866 | 2026-08-10 03:51:00 | NPP-375D | NOVA SERRANA | MINAS GERAIS | Brasil | 3145208 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 7c77b4ed-df80-374f-b3a8-e74a4302ab5b | -23.02108 | -46.67836 | 2026-08-10 03:51:00 | NPP-375D | ATIBAIA | SÃO PAULO | Brasil | 3504107 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| f666176a-a901-31c9-b930-de52ea5f03a4 | -20.02019 | -45.46407 | 2026-08-10 03:51:00 | NPP-375D | LAGOA DA PRATA | MINAS GERAIS | Brasil | 3137205 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 69036153-b7d5-3f0c-951b-69b27422dd45 | -18.81573 | -49.64052 | 2026-08-10 03:51:00 | NPP-375D | ITUIUTABA | MINAS GERAIS | Brasil | 3134202 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.2 |
| 3c0ce422-6b54-3ac5-8857-df885813e8d5 | -18.81669 | -49.64114 | 2026-08-10 03:51:00 | NPP-375D | ITUIUTABA | MINAS GERAIS | Brasil | 3134202 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.9 |
| 7898435a-cf6b-32b6-8ce4-3dbc5f4f20e9 | -19.84167 | -44.99408 | 2026-08-10 03:51:00 | NPP-375D | NOVA SERRANA | MINAS GERAIS | Brasil | 3145208 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| baeb5346-075b-32b6-91b0-11639126cec4 | -19.71791 | -49.12841 | 2026-08-10 03:51:00 | NPP-375D | COMENDADOR GOMES | MINAS GERAIS | Brasil | 3116902 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| bd84de82-9d96-3372-b5de-012ae5fa2467 | -20.39327 | -42.82555 | 2026-08-10 03:51:00 | NPP-375D | PONTE NOVA | MINAS GERAIS | Brasil | 3152105 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| 7bee80e2-98d5-3d3a-b2f3-4d862b1f821e | -20.3947 | -42.82605 | 2026-08-10 03:51:00 | NPP-375D | PONTE NOVA | MINAS GERAIS | Brasil | 3152105 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.8 |
| 9ece68fb-6fba-3527-81b0-569d9548fb2f | -20.37408 | -41.60841 | 2026-08-10 03:51:00 | NPP-375D | IRUPI | ESPÍRITO SANTO | Brasil | 3202652 | 32 | 33 | nan | nan | nan | Mata Atlântica | 3.0 |
| de295db3-3be3-3672-83fb-1dd8abbc1f98 | -20.52015 | -42.30941 | 2026-08-10 03:51:00 | NPP-375D | SANTA MARGARIDA | MINAS GERAIS | Brasil | 3157906 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.6 |
| 06c5f269-0e12-335f-ac5d-01030f352ddb | -18.81394 | -49.65305 | 2026-08-10 03:51:00 | NPP-375D | ITUIUTABA | MINAS GERAIS | Brasil | 3134202 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.5 |
| b2e3838f-32bc-33d1-8c0e-a1e7138bd858 | -20.52083 | -42.30586 | 2026-08-10 03:51:00 | NPP-375D | SANTA MARGARIDA | MINAS GERAIS | Brasil | 3157906 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.6 |
| 766f727d-3e0d-35c5-a180-8af8665a0f84 | -22.21987 | -43.02289 | 2026-08-10 03:51:00 | NPP-375D | PETRÓPOLIS | RIO DE JANEIRO | Brasil | 3303906 | 33 | 33 | nan | nan | nan | Mata Atlântica | 4.1 |
| 3d922c37-ab41-3c3e-ab46-958d2d9c2921 | -18.81429 | -49.64654 | 2026-08-10 03:51:00 | NPP-375D | ITUIUTABA | MINAS GERAIS | Brasil | 3134202 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.2 |
| 63d3158c-622e-3a31-8ea4-baefb2480a48 | -8.96 | -60.5358 | 2026-08-10 04:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 50.4 |
| 23fd8076-6c86-3fec-a4cc-f176a5b4b6a4 | -8.9598 | -60.555 | 2026-08-10 04:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 52.9 |
| ace78ac0-1d7b-3f95-8dfa-c97c2a344aeb | -8.8854 | -60.5778 | 2026-08-10 04:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 62.0 |
| a4185629-ccd7-34fb-8404-fef4747afe64 | -8.9039 | -60.5769 | 2026-08-10 04:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 53.9 |
| 76b9caea-20da-37cc-acb1-363c9639f5b4 | -3.49013 | -50.05159 | 2026-08-10 04:06:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 9.5 |
| 271d37b9-c6d3-3f07-a856-a80692b4b32b | -4.45215 | -47.91446 | 2026-08-10 04:06:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| b892c571-5bd2-30fd-9e10-324dd800b426 | -3.48429 | -50.05046 | 2026-08-10 04:06:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 3dab2b5f-972e-3d25-b1b4-115d7c68ade9 | -7.35998 | -42.89213 | 2026-08-10 04:06:00 | NOAA-20 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| cc75a917-90d1-3868-87a3-a09a6fe8cba5 | -7.31015 | -35.12868 | 2026-08-10 04:06:00 | NOAA-20 | PEDRAS DE FOGO | PARAÍBA | Brasil | 2511202 | 25 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 4ea54485-0000-3dbb-ba6a-7f8f0c3eab29 | -3.95791 | -48.12939 | 2026-08-10 04:06:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b9deef05-5b30-3af0-b966-ffc2c2c0a30c | -4.74498 | -40.43483 | 2026-08-10 04:06:00 | NOAA-20 | TAMBORIL | CEARÁ | Brasil | 2313203 | 23 | 33 | nan | nan | nan | Caatinga | 3.2 |
| a822624a-4a0e-3cf2-b49c-e3c3e2357734 | -6.0667 | -42.51366 | 2026-08-10 04:06:00 | NOAA-20 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 3.9 |
| 7f3021ec-669f-3b16-b906-a91c87e3fe24 | -3.75794 | -51.60975 | 2026-08-10 04:06:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| f6b10a2c-34f7-3c10-9d0f-50d25d13663e | -6.98517 | -39.50225 | 2026-08-10 04:06:00 | NOAA-20 | FARIAS BRITO | CEARÁ | Brasil | 2304301 | 23 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 1a8d190f-4327-3d71-b955-a964e3dbded0 | -7.61261 | -42.76453 | 2026-08-10 04:06:00 | NOAA-20 | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 3.5 |
| 0523f31e-8efe-3711-9050-b402945084c7 | -6.95386 | -42.00314 | 2026-08-10 04:06:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| e3c1e02c-d598-3a19-97c4-62167100871c | -4.93081 | -37.42598 | 2026-08-10 04:06:00 | NOAA-20 | MOSSORÓ | RIO GRANDE DO NORTE | Brasil | 2408003 | 24 | 33 | nan | nan | nan | Caatinga | 3.5 |
| dff67ca5-43e8-367f-98c8-662cb412510d | -6.96647 | -41.48499 | 2026-08-10 04:06:00 | NOAA-20 | SANTANA DO PIAUÍ | PIAUÍ | Brasil | 2209351 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 04aaf250-b661-3212-9334-bd84008ce29b | -7.61957 | -42.76567 | 2026-08-10 04:06:00 | NOAA-20 | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 3.9 |
| 1bc30221-f357-3ae5-aeb8-f864e199e64d | -7.17493 | -42.34672 | 2026-08-10 04:06:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 9322a6c6-0527-3445-87ba-579a217ed05d | -6.46638 | -47.85043 | 2026-08-10 04:06:00 | NOAA-20 | ANGICO | TOCANTINS | Brasil | 1701051 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| d4802e34-88a0-302e-a2f2-bab784f19d90 | -3.4894 | -50.05574 | 2026-08-10 04:06:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 11.2 |
| abd70843-4ec7-392e-b4bb-3b612bda2c8f | -6.90146 | -41.9343 | 2026-08-10 04:06:00 | NOAA-20 | SÃO JOÃO DA VARJOTA | PIAUÍ | Brasil | 2209955 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| f9cd1fbb-8094-319a-81df-42dbb973ac44 | -6.98462 | -39.50574 | 2026-08-10 04:06:00 | NOAA-20 | FARIAS BRITO | CEARÁ | Brasil | 2304301 | 23 | 33 | nan | nan | nan | Caatinga | 1.4 |
| a5b42380-534d-3cd4-871c-e54ccd68bb96 | -6.46061 | -47.85497 | 2026-08-10 04:06:00 | NOAA-20 | ANGICO | TOCANTINS | Brasil | 1701051 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 6c1512d2-1598-3122-9cf3-f169b77f2469 | -7.61735 | -42.75734 | 2026-08-10 04:06:00 | NOAA-20 | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 860206fb-564a-3858-a300-dea206183278 | -3.2674 | -49.53483 | 2026-08-10 04:06:00 | NOAA-20 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 91cbc32e-900b-34c8-a290-87c81e4047cc | -7.61798 | -42.75348 | 2026-08-10 04:06:00 | NOAA-20 | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 376e0ea4-2f8e-3112-9475-e6494c439c82 | -7.00132 | -42.03374 | 2026-08-10 04:06:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 50b6a1ec-d32b-382f-b1e0-1da9c5380345 | -7.08683 | -42.26414 | 2026-08-10 04:06:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| df048e6c-55ba-36c1-b9f8-9bb300eb5e04 | -7.38707 | -42.88046 | 2026-08-10 04:06:00 | NOAA-20 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 3b51ea4e-052c-36dc-9b7f-64173e10bbb8 | -6.64902 | -49.61624 | 2026-08-10 04:06:00 | NOAA-20 | SAPUCAIA | PARÁ | Brasil | 1507755 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| cecd9af4-493b-3a6c-9ae2-a15b92660ad7 | -6.46209 | -47.85375 | 2026-08-10 04:06:00 | NOAA-20 | ANGICO | TOCANTINS | Brasil | 1701051 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 8c0c4b4c-2294-30f3-8781-5139cd01425a | -2.37883 | -48.2294 | 2026-08-10 04:06:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ff4aa055-b07a-39ec-9d87-eb96c46103a4 | -6.96368 | -41.48092 | 2026-08-10 04:06:00 | NOAA-20 | SANTANA DO PIAUÍ | PIAUÍ | Brasil | 2209351 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| c81f246f-9add-36ab-92dc-57f094223bf6 | -7.61324 | -42.76065 | 2026-08-10 04:06:00 | NOAA-20 | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 18899a47-ca1d-3635-9630-6b2ab61a3f9f | -6.95697 | -41.47986 | 2026-08-10 04:06:00 | NOAA-20 | SANTANA DO PIAUÍ | PIAUÍ | Brasil | 2209351 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 3cdda11a-a8e4-30ae-86bc-73bfcfd955df | -5.7301 | -49.13709 | 2026-08-10 04:06:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| b014a59b-9864-33a5-a637-d1975962adc1 | -2.37936 | -48.22612 | 2026-08-10 04:06:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 32f33a54-fd46-3265-b863-639e3a7ed757 | -7.3877 | -42.87655 | 2026-08-10 04:06:00 | NOAA-20 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| d02f5fc3-7c7b-3cf0-b68b-66d195d16d6b | -6.96704 | -41.48143 | 2026-08-10 04:06:00 | NOAA-20 | SANTANA DO PIAUÍ | PIAUÍ | Brasil | 2209351 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 892afbfc-d171-3306-8825-d5b56de4a34b | -7.44682 | -43.20453 | 2026-08-10 04:06:00 | NOAA-20 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 54729277-a6a2-3af7-9ec1-e66cce8041aa | -5.61228 | -37.53046 | 2026-08-10 04:06:00 | NOAA-20 | CARAÚBAS | RIO GRANDE DO NORTE | Brasil | 2402303 | 24 | 33 | nan | nan | nan | Caatinga | 0.6 |
| ae51a067-9479-36fb-b344-624984ba2157 | -6.90205 | -41.93061 | 2026-08-10 04:06:00 | NOAA-20 | SÃO JOÃO DA VARJOTA | PIAUÍ | Brasil | 2209955 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| b64737c8-dd53-37f9-96d2-ba8f218f824a | -7.40481 | -39.79362 | 2026-08-10 04:06:00 | NOAA-20 | EXU | PERNAMBUCO | Brasil | 2605301 | 26 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 678b5ef6-129e-3ce7-a141-f7d081b93572 | -5.73068 | -49.13379 | 2026-08-10 04:06:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| aa33ae2b-8fff-371e-a11d-61cc6a76276a | -3.49056 | -50.05785 | 2026-08-10 04:06:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 89fd636c-a570-371f-b5ce-f520cca8a220 | -7.35648 | -42.89157 | 2026-08-10 04:06:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| e35a0521-0c74-38cf-b4c4-1738155fa358 | -3.96306 | -48.13011 | 2026-08-10 04:06:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| eb5f5c04-9f1a-300c-aeda-258cd0a045a0 | -4.43798 | -40.65448 | 2026-08-10 04:06:00 | NOAA-20 | IPU | CEARÁ | Brasil | 2305803 | 23 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 8391f0f1-27e5-31e8-a291-2031f9b1fa46 | -4.33221 | -40.18809 | 2026-08-10 04:06:00 | NOAA-20 | SANTA QUITÉRIA | CEARÁ | Brasil | 2312205 | 23 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 26a8b7e1-3a73-3542-92c4-375e0eb17c80 | -7.62146 | -42.75404 | 2026-08-10 04:06:00 | NOAA-20 | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 45b3f8f4-8910-3e89-98d7-6ffc56e265ac | -4.55066 | -38.39091 | 2026-08-10 04:06:00 | NOAA-20 | OCARA | CEARÁ | Brasil | 2309458 | 23 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 9323001f-8cad-3cb0-8604-b201d6c2e2f8 | -7.10149 | -43.78126 | 2026-08-10 04:06:00 | NOAA-20 | MARCOS PARENTE | PIAUÍ | Brasil | 2206001 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 1df98966-7791-38c8-8126-89b3623ab25d | -6.64964 | -49.61275 | 2026-08-10 04:06:00 | NOAA-20 | SAPUCAIA | PARÁ | Brasil | 1507755 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 9cc1340c-3262-3f09-8581-835867a9769f | -7.61672 | -42.76122 | 2026-08-10 04:06:00 | NOAA-20 | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |


[Clique aqui para ver as próximas entradas](README6.md)
