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

## Dados Diários - Página 1

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| fdf91dbf-eb2c-3a66-9165-0f591c96cabc | -19.0989 | -56.0488 | 2025-02-22 00:00:00 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 79.1 |
| 128eafbf-4c78-36a8-8a9f-24ed8ad1f611 | -19.0785 | -56.0727 | 2025-02-22 00:00:00 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 87.7 |
| a0b8e365-9e02-32de-b489-f94719e2bb63 | -19.0985 | -56.0698 | 2025-02-22 00:00:00 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 113.1 |
| 8ec4b3a4-348a-3ef4-8327-35239f5fafb9 | -19.0785 | -56.0727 | 2025-02-22 00:10:00 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 83.6 |
| 7c3053fb-7fcd-3ca4-81d3-15c26e8feecb | -19.0989 | -56.0488 | 2025-02-22 00:10:00 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 74.7 |
| 453978ff-47fa-3239-973d-8aae27c3bd04 | -19.0985 | -56.0698 | 2025-02-22 00:10:00 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 104.3 |
| 7fd3d5e7-1c41-3e41-86b4-c3e178b7d9ab | -19.0989 | -56.0488 | 2025-02-22 00:20:00 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 66.0 |
| d98cbff1-bb84-3504-b3c9-b50b638084a1 | -19.0985 | -56.0698 | 2025-02-22 00:20:00 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 103.4 |
| 775306c5-0377-3a34-b467-8354e03a961c | -19.0785 | -56.0727 | 2025-02-22 00:20:00 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 78.6 |
| 2b19eca5-dbff-3839-8b67-1faef3ba2cbc | -14.4424 | -45.623699 | 2025-02-22 00:21:00 | METOP-C | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 20abee2c-a357-34ff-af6e-cca396e25958 | -10.2969 | -36.449799 | 2025-02-22 00:21:00 | METOP-C | PENEDO | ALAGOAS | Brasil | 2706703 | 27 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 1953a3e1-0787-3dcf-96d4-002cf00c9e43 | -10.4334 | -44.8876 | 2025-02-22 00:21:00 | METOP-C | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 5318c98f-ac99-3d75-9121-63644e8af2bf | -20.133699 | -45.455502 | 2025-02-22 00:21:00 | METOP-C | SANTO ANTÔNIO DO MONTE | MINAS GERAIS | Brasil | 3160405 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| c96575d3-9236-3773-a8cc-ee9e2534e160 | -12.8267 | -44.995998 | 2025-02-22 00:21:00 | METOP-C | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| dfc92a22-ace9-3927-b30d-bb37dd02e9c1 | -10.3028 | -36.473598 | 2025-02-22 00:21:00 | METOP-C | PENEDO | ALAGOAS | Brasil | 2706703 | 27 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 70b52da5-628a-3b70-8cd5-b3f579030916 | -10.5898 | -44.617001 | 2025-02-22 00:21:00 | METOP-C | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| a925c09f-5bc9-37d2-a73c-cc70476f315d | -12.8347 | -44.9855 | 2025-02-22 00:21:00 | METOP-C | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 111ec1e1-e02d-3e13-bc12-633671543b49 | -7.9031 | -43.5504 | 2025-02-22 00:21:00 | METOP-C | ELISEU MARTINS | PIAUÍ | Brasil | 2203602 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| a4dec691-bcad-3ceb-9e0e-1e4b817ca719 | -12.8231 | -44.979099 | 2025-02-22 00:21:00 | METOP-C | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| fc03e4aa-8b34-3fff-8dd8-d3e706de127c | -9.4517 | -40.326 | 2025-02-22 00:21:00 | METOP-C | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| acc2b99b-adfc-318e-a5f3-20628ee38008 | -10.5782 | -37.981098 | 2025-02-22 00:21:00 | METOP-C | ADUSTINA | BAHIA | Brasil | 2900355 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| 266243fa-4f2b-3513-af26-8059419e4235 | -7.9015 | -43.543499 | 2025-02-22 00:21:00 | METOP-C | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 630935ad-a479-39b4-a2e9-72d8f4843580 | -10.5881 | -44.609299 | 2025-02-22 00:21:00 | METOP-C | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| e40a1f9e-1d72-33c4-9344-8fa40e04a755 | -17.7934 | -40.019001 | 2025-02-22 00:21:00 | METOP-C | IBIRAPUÃ | BAHIA | Brasil | 2912806 | 29 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 80e7cff4-d8d7-3421-9099-d8aaa7d29ffb | -17.795 | -40.026199 | 2025-02-22 00:21:00 | METOP-C | IBIRAPUÃ | BAHIA | Brasil | 2912806 | 29 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 460490e8-c81c-36f4-8896-6d0d2586b95d | -20.1294 | -45.4328 | 2025-02-22 00:21:00 | METOP-C | LAGOA DA PRATA | MINAS GERAIS | Brasil | 3137205 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 95206ab2-1a44-3634-a0c3-c7965f7c283f | -10.5759 | -37.9715 | 2025-02-22 00:21:00 | METOP-C | ADUSTINA | BAHIA | Brasil | 2900355 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| 2e440779-10e0-3a9b-ae61-6fb15916f0eb | -20.1315 | -45.444099 | 2025-02-22 00:21:00 | METOP-C | LAGOA DA PRATA | MINAS GERAIS | Brasil | 3137205 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 86fc7a8e-c2aa-3bde-a381-c1569750f083 | -17.7917 | -40.011799 | 2025-02-22 00:21:00 | METOP-C | IBIRAPUÃ | BAHIA | Brasil | 2912806 | 29 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 902f1889-7a04-3a45-81c9-392237b67f08 | -12.2897 | -44.834301 | 2025-02-22 00:21:00 | METOP-C | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 6f2e2be4-9e16-34f2-b34a-9c493a159aa2 | -12.8365 | -44.9939 | 2025-02-22 00:21:00 | METOP-C | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 81800dec-527a-3f18-a0de-25853d04c6a1 | -10.4913 | -42.4203 | 2025-02-22 00:21:00 | METOP-C | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| 898bf386-797e-304f-adc1-56f31740280c | -12.288 | -44.826099 | 2025-02-22 00:21:00 | METOP-C | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 929d90f2-0a08-3f52-b3c4-8c6db86457da | -14.4444 | -45.633301 | 2025-02-22 00:21:00 | METOP-C | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| a819a62f-6370-3b08-b49e-a8c2878d3c47 | -10.3683 | -44.9184 | 2025-02-22 00:21:00 | METOP-C | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| bf873a1b-6ac9-38fc-8ad3-c22410041b6c | -12.8383 | -45.002399 | 2025-02-22 00:21:00 | METOP-C | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| b35d9c54-19f3-367f-a0a3-68a344608efc | -12.2799 | -44.836399 | 2025-02-22 00:21:00 | METOP-C | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| f128a919-5089-3c74-b3ba-cac2f5b19bb9 | -12.8249 | -44.987598 | 2025-02-22 00:21:00 | METOP-C | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 866c39d5-aa44-3948-8e4d-e5dd567dd554 | -10.2998 | -36.4617 | 2025-02-22 00:21:00 | METOP-C | PENEDO | ALAGOAS | Brasil | 2706703 | 27 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 10f34372-3e0c-3236-bbfd-829d47b2d033 | -12.8481 | -45.000198 | 2025-02-22 00:21:00 | METOP-C | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 1fbc1324-a943-35f7-8ba4-a0bcdbf265a5 | -17.7807 | -40.0182 | 2025-02-22 00:30:00 | GOES-16 | IBIRAPUÃ | BAHIA | Brasil | 2912806 | 29 | 33 | nan | nan | nan | Mata Atlântica | 121.7 |
| 6a9cd68a-d286-325f-a3d8-09999da16f62 | -19.0785 | -56.0727 | 2025-02-22 00:30:00 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 72.8 |
| 1a5f3cb2-e2de-3e3f-b0e7-e0fcdee8652a | -19.0985 | -56.0698 | 2025-02-22 00:30:00 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 93.3 |
| 3633eab8-28a0-3a27-a87e-78519f12a79a | -19.0989 | -56.0488 | 2025-02-22 00:30:00 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 62.4 |
| 595b3da6-6b80-3a85-8f73-d7dc003b34f7 | -19.0785 | -56.0727 | 2025-02-22 00:40:00 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 85.8 |
| 47fe86fc-103f-3ee1-9862-d21b424f22fd | -17.7807 | -40.0182 | 2025-02-22 00:40:00 | GOES-16 | IBIRAPUÃ | BAHIA | Brasil | 2912806 | 29 | 33 | nan | nan | nan | Mata Atlântica | 152.1 |
| dcae40c1-db12-3830-b439-b6dab0736b78 | -19.0985 | -56.0698 | 2025-02-22 00:40:00 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 88.9 |
| 5bc9490c-f741-3f3a-8f15-752e52719208 | -19.0785 | -56.0727 | 2025-02-22 00:50:00 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 77.9 |
| 8aa55a16-5642-3d6f-b32d-b2051540a200 | -19.0985 | -56.0698 | 2025-02-22 00:50:00 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 93.8 |
| 24631391-2a77-3849-974f-7eb0eccdcd19 | -19.0785 | -56.0727 | 2025-02-22 01:00:00 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 75.4 |
| f2cfaa0f-5793-361e-8f77-b8903b0f37f2 | -19.0985 | -56.0698 | 2025-02-22 01:00:00 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 80.9 |
| df8a90f2-1488-3c81-a9e2-07c8388dba85 | -19.095501 | -56.0676 | 2025-02-22 01:06:00 | METOP-B | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| a827e4df-2b38-3b1e-806a-4783b33b7f1b | -19.101999 | -56.050598 | 2025-02-22 01:06:00 | METOP-B | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 440db46f-2382-35ca-a145-c13e11c7093a | -21.080601 | -56.381802 | 2025-02-22 01:06:00 | METOP-B | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| 2ccd0e9e-f416-3edb-9ac6-c35d76363e0c | -12.1646 | -54.977901 | 2025-02-22 01:06:00 | METOP-B | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 271f2f5d-b28a-3204-85f8-e62d0555e306 | -19.0923 | -56.053001 | 2025-02-22 01:06:00 | METOP-B | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 75b51485-43f4-3122-b40b-0a778dee5008 | 4.5589 | -60.7267 | 2025-02-22 01:06:00 | METOP-B | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| 52e38415-9bd4-39e7-ad31-2daf21c251da | -21.079 | -56.374401 | 2025-02-22 01:06:00 | METOP-B | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| a31d9d65-313b-3fea-a984-ad085bf8c534 | -19.103701 | -56.057899 | 2025-02-22 01:06:00 | METOP-B | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 2d051cbf-6667-3aee-aad2-4d6414a4fa38 | -19.093901 | -56.060299 | 2025-02-22 01:06:00 | METOP-B | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| c2c906bd-9940-3ef0-9c6c-2938f2628b62 | -19.105301 | -56.065201 | 2025-02-22 01:06:00 | METOP-B | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| cb01ee37-4aca-388c-a6f9-3d3cd353e1db | -12.1666 | -54.986599 | 2025-02-22 01:06:00 | METOP-B | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| c0e3da96-f178-36d5-8dd2-592bc36cc606 | -20.8592 | -56.404999 | 2025-02-22 01:06:00 | METOP-B | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| 4694d8c3-fcbd-3227-be77-a0aaa3a2408d | 4.5573 | -60.733898 | 2025-02-22 01:06:00 | METOP-B | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| be2875e3-ec47-37a1-92a6-c06645213e8f | 3.1139 | -60.235199 | 2025-02-22 01:06:00 | METOP-B | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| 431d858c-d6ed-39b7-9720-1b937f6ac0e1 | 3.1171 | -60.220699 | 2025-02-22 01:06:00 | METOP-B | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| dc55f85f-5b09-3398-9f1f-7ab99a7b9380 | -19.100401 | -56.043301 | 2025-02-22 01:06:00 | METOP-B | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 693032ed-480e-377a-a6fe-05f16e062cf2 | 3.1155 | -60.228001 | 2025-02-22 01:06:00 | METOP-B | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| ccde1531-22ae-3752-bb3f-19cbe92e3ebb | -19.0985 | -56.0698 | 2025-02-22 01:10:00 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 83.0 |
| 4f1c4aad-157a-347f-a66e-4ceca538e507 | -19.0785 | -56.0727 | 2025-02-22 01:10:00 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 64.7 |
| b9fa2332-5e4f-3f63-8231-eb3b76ccde69 | -19.0785 | -56.0727 | 2025-02-22 01:20:00 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 64.8 |
| ead17d03-64d1-3c4f-8867-efef87828bef | -19.0985 | -56.0698 | 2025-02-22 01:20:00 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 64.1 |
| bb7df495-1e1c-326a-9824-a10e0d6a7588 | -20.84948 | -56.41415 | 2025-02-22 01:26:00 | TERRA_M-M | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 2d1c6068-7286-3bfa-bb10-aa6f99de9799 | -19.09504 | -56.064 | 2025-02-22 01:28:00 | TERRA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 8.6 |
| c09f5555-5f23-3ca6-9876-0910e135866f | -19.0875 | -56.07483 | 2025-02-22 01:28:00 | TERRA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 29.4 |
| b519d680-1740-3de4-a70c-93e5c239007a | -19.49705 | -55.33636 | 2025-02-22 01:28:00 | TERRA_M-M | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 5.4 |
| 50aa0d9d-2dfd-3695-a90b-4be73b362801 | -19.08616 | -56.06543 | 2025-02-22 01:28:00 | TERRA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 37.9 |
| 56535b21-02a6-368c-81da-6dd1208a29ae | -12.15329 | -54.99358 | 2025-02-22 01:30:00 | TERRA_M-M | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 16.4 |
| 95bf2b11-1b8e-3122-ba97-94f69a0a5173 | -12.15359 | -54.99993 | 2025-02-22 01:30:00 | TERRA_M-M | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 15.4 |
| 7f74ba83-41a2-301a-8e5b-ccc22f48ba3a | -12.15187 | -54.98831 | 2025-02-22 01:30:00 | TERRA_M-M | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 72e17b2a-6d5b-360a-bca1-4ba0e207e2f7 | -12.15508 | -55.00515 | 2025-02-22 01:30:00 | TERRA_M-M | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 923abbcf-3b0f-3c0b-acc9-77b28d37ca28 | 3.11604 | -61.27988 | 2025-02-22 01:34:00 | TERRA_M-M | ALTO ALEGRE | RORAIMA | Brasil | 1400050 | 14 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 496262f3-3728-3c6a-b026-0131b0977687 | 4.5636 | -60.74422 | 2025-02-22 01:34:00 | TERRA_M-M | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 1612f503-97fb-30b8-ae14-8b9751ec65a5 | 4.56483 | -60.7352 | 2025-02-22 01:34:00 | TERRA_M-M | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 9.4 |
| d49729ee-e886-3bf5-a1fc-2ca92e14091d | -19.0785 | -56.0727 | 2025-02-22 01:50:00 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 50.7 |
| 32188271-e05e-37ba-912e-d4b795e5ed51 | -5.83179 | -35.5213 | 2025-02-22 03:21:00 | NOAA-21 | IELMO MARINHO | RIO GRANDE DO NORTE | Brasil | 2404606 | 24 | 33 | nan | nan | nan | Caatinga | 1.3 |
| d4e3588b-d5f3-3720-bd03-c3431ec024d7 | -7.47492 | -34.84174 | 2025-02-22 03:23:00 | NOAA-21 | PITIMBU | PARAÍBA | Brasil | 2511905 | 25 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 27467aef-cedc-31ff-97eb-42dc89481404 | -7.46608 | -35.1356 | 2025-02-22 03:23:00 | NOAA-21 | ITAMBÉ | PERNAMBUCO | Brasil | 2607653 | 26 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 3618cf9c-5657-34a1-9ce4-0c398cd4a5ea | -7.4637 | -35.13352 | 2025-02-22 03:23:00 | NOAA-21 | ITAMBÉ | PERNAMBUCO | Brasil | 2607653 | 26 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| d6afff6b-b23b-3c59-9251-a00b74c547bd | -10.57068 | -37.97438 | 2025-02-22 03:23:00 | NOAA-21 | ADUSTINA | BAHIA | Brasil | 2900355 | 29 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 55843871-ead4-3e59-a893-58ab92aeb285 | -10.43126 | -44.89069 | 2025-02-22 03:23:00 | NOAA-21 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 7098809c-981a-31f1-ab34-d5483040cf62 | -10.4302 | -44.8962 | 2025-02-22 03:23:00 | NOAA-21 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| ca9879b6-c136-3fd1-80a3-44a90aada046 | -10.58683 | -44.61489 | 2025-02-22 03:23:00 | NOAA-21 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 10.7 |
| b9271868-a815-39b1-834e-ef4532dcae0f | -10.43151 | -44.88971 | 2025-02-22 03:23:00 | NOAA-21 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| a772aa9f-20fa-3906-80db-e8771b81468d | -7.89517 | -43.54983 | 2025-02-22 03:23:00 | NOAA-21 | ELISEU MARTINS | PIAUÍ | Brasil | 2203602 | 22 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 8c7d282c-a286-381f-86f1-b12dcbbf6a1f | -10.4882 | -42.42234 | 2025-02-22 03:23:00 | NOAA-21 | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 8.2 |
| 4bc77c85-7ad3-3a18-b6db-1ced15b3257a | -10.15946 | -36.47264 | 2025-02-22 03:23:00 | NOAA-21 | PENEDO | ALAGOAS | Brasil | 2706703 | 27 | 33 | nan | nan | nan | Caatinga | 3.3 |
| b9a3b98d-1d45-39ca-9b93-e59d62dac15f | -10.82354 | -37.166 | 2025-02-22 03:23:00 | NOAA-21 | LARANJEIRAS | SERGIPE | Brasil | 2803609 | 28 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| cafb8555-d905-366a-819f-09a54aa91757 | -6.90993 | -35.57516 | 2025-02-22 03:23:00 | NOAA-21 | PILÕES | PARAÍBA | Brasil | 2511608 | 25 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 3c1ba51f-0d2f-33c5-8bfd-dd16d8385fa9 | -10.48535 | -42.421 | 2025-02-22 03:23:00 | NOAA-21 | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 7.4 |


[Clique aqui para ver as próximas entradas](README2.md)
