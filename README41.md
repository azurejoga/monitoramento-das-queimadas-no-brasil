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

## Dados Diários - Página 41

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 9f031768-9063-3645-b32a-4d117465c91d | -13.326 | -46.8279 | 2025-09-03 03:55:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 67e023d9-03e3-3210-be77-46669d628141 | -12.99742 | -48.11333 | 2025-09-03 03:55:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| abd109f0-fec6-3e12-bec7-fb3b984b842f | -10.05337 | -48.09387 | 2025-09-03 03:55:00 | NOAA-20 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 226b9a41-da25-3b53-bcb8-0b1fdced330b | -9.13403 | -49.64465 | 2025-09-03 03:55:00 | NOAA-20 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 4.7 |
| d3892629-545a-3c85-95a8-914e8959eb3b | -13.31572 | -46.8233 | 2025-09-03 03:55:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 56051969-342f-3dc2-a060-0602f2226752 | -14.81396 | -48.34732 | 2025-09-03 03:55:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| f9905427-0d61-3782-8211-b80d624653dd | -10.00977 | -46.90142 | 2025-09-03 03:55:00 | NOAA-20 | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b0eb040e-7f3c-3882-9f23-3c82c77a36e2 | -13.31509 | -46.82673 | 2025-09-03 03:55:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 07642335-a1d5-3eaf-975a-dd1ccd48c654 | -15.56784 | -48.40887 | 2025-09-03 03:55:00 | NOAA-20 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 10.8 |
| 5cbfd24f-c19f-3430-90d9-a5630e0e52d5 | -11.1165 | -44.65821 | 2025-09-03 03:55:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 178beeea-d4cc-3782-9ec9-08177a9bd3b7 | -11.91981 | -46.66351 | 2025-09-03 03:55:00 | NOAA-20 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 0675d221-af73-377b-9add-7488831993f1 | -11.6138 | -52.14301 | 2025-09-03 03:55:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 400bccc1-b3d2-3e66-b66d-c74f4954dc19 | -15.00652 | -50.05913 | 2025-09-03 03:55:00 | NOAA-20 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 3ee1c88d-186f-3849-ae34-1afedf014435 | -15.55147 | -48.36555 | 2025-09-03 03:55:00 | NOAA-20 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 471059d8-7846-326c-a2f7-79475e9fb117 | -13.20513 | -51.81683 | 2025-09-03 03:55:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| a2340d46-0705-39e5-8655-06714a3be7b7 | -10.54834 | -50.42342 | 2025-09-03 03:55:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 2959c68a-dba8-381b-83f6-d7c12c72fb71 | -9.62961 | -47.04149 | 2025-09-03 03:55:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| eb2599ca-0942-3f01-902f-c351b7a2bfce | -9.63184 | -46.11515 | 2025-09-03 03:55:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d12ceda5-a61a-3061-bbd3-b295e0e39140 | -14.76983 | -48.14107 | 2025-09-03 03:55:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| f13023a0-084a-362d-b05b-11f86ee544a7 | -15.16167 | -52.36376 | 2025-09-03 03:55:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 8c39f91d-a1a6-3497-a899-9be6eb5692ae | -10.49528 | -50.33067 | 2025-09-03 03:55:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 2004050d-2572-3764-a56c-ae2535d15aeb | -13.5252 | -51.80488 | 2025-09-03 03:55:00 | NOAA-20 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 79e58213-c9d1-3efb-8ef3-12af8b100100 | -10.7344 | -44.81497 | 2025-09-03 03:55:00 | NOAA-20 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 3fafe23d-0e32-37df-8758-d2e02aa721de | -13.29279 | -46.82154 | 2025-09-03 03:55:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| cc245964-364a-37b1-abd5-2399f7252872 | -11.91529 | -46.66246 | 2025-09-03 03:55:00 | NOAA-20 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c3f2cde8-17be-3a2f-9c99-394e06ecede8 | -13.50545 | -46.93077 | 2025-09-03 03:55:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 80fe8e85-5477-329a-b58a-5822091df493 | -10.49181 | -50.33352 | 2025-09-03 03:55:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| d2d365c1-ef67-3cb8-a116-22eb0b22cc60 | -11.91439 | -46.66745 | 2025-09-03 03:55:00 | NOAA-20 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 60a44b1b-2093-3a74-9299-1d3ac89dc80c | -11.9395 | -50.60062 | 2025-09-03 03:55:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 0ea44750-3b4b-38e0-bafc-89cf04d08fe2 | -13.49704 | -47.02432 | 2025-09-03 03:55:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 14.0 |
| a7bcbfa1-e1da-370b-9094-eb1b89c85411 | -12.86281 | -48.02787 | 2025-09-03 03:55:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| aa382e83-e6a5-3dc9-88ba-acf1472b1052 | -11.08526 | -45.1237 | 2025-09-03 03:55:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 2bbe876b-7ea9-3f6e-a5f1-bdb460db6cdb | -12.29672 | -50.00778 | 2025-09-03 03:55:00 | NOAA-20 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 8b06dda6-c110-3160-a87b-fec32daca0b3 | -13.31124 | -46.82238 | 2025-09-03 03:55:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 0c58f1a1-8572-3ee1-8b2a-c5dff61dffa5 | -11.85196 | -51.52753 | 2025-09-03 03:55:00 | NOAA-20 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| dbd2cd68-fd01-39b8-90bc-40b1bcae4335 | -9.13243 | -49.6531 | 2025-09-03 03:55:00 | NOAA-20 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 7.4 |
| f375b8e3-b70e-38fc-8985-37e391d7af40 | -14.79017 | -47.51117 | 2025-09-03 03:55:00 | NOAA-20 | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e31891ae-4784-3b39-a143-87ae89d13ebd | -12.01816 | -45.5749 | 2025-09-03 03:55:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| c6190569-63b0-3855-a367-4356b79a4a8e | -11.37787 | -43.61267 | 2025-09-03 03:55:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 3f8d4c49-b03c-311f-9fc1-05747858404f | -11.11862 | -44.66978 | 2025-09-03 03:55:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| df2cd7dd-a93a-350f-9cbb-ab1b32ed362e | -10.55343 | -50.42911 | 2025-09-03 03:55:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 4b27c7b6-85d9-3b53-baf7-a85ea66e323a | -14.81046 | -48.21124 | 2025-09-03 03:55:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 1e3fce7a-5556-3182-8819-333ee6db741e | -10.93739 | -50.76834 | 2025-09-03 03:55:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 3592699e-f362-31ea-8dd8-97811d1e6626 | -12.88253 | -48.03107 | 2025-09-03 03:55:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| fe527e5a-6eea-3d6e-aa21-9144876740a1 | -12.44329 | -48.70979 | 2025-09-03 03:55:00 | NOAA-20 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| de55df36-7627-3afc-af68-40046afd97fb | -14.74015 | -46.97451 | 2025-09-03 03:55:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 54f3a1ee-e2f6-3d61-9860-19667138123f | -15.55572 | -48.39455 | 2025-09-03 03:55:00 | NOAA-20 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 7.4 |
| c8ca526c-9c57-3d02-8d7f-fa024c4c68f5 | -10.737 | -44.79983 | 2025-09-03 03:55:00 | NOAA-20 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 15f71b9d-fdfc-3f77-a124-05b87101532e | -11.60882 | -52.1362 | 2025-09-03 03:55:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 9.0 |
| b4e34b05-663a-3f2b-95f8-31f4035dd052 | -10.11438 | -46.23765 | 2025-09-03 03:55:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| e9021cfe-b3c5-38e9-9d1f-9c4bbc423107 | -14.39758 | -51.71218 | 2025-09-03 03:55:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 14c08b40-ec74-32b8-912d-42601b0360a3 | -11.59815 | -52.12225 | 2025-09-03 03:55:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 6b05bcee-f1a9-39d1-8daf-11ca4df7f987 | -10.48516 | -50.35152 | 2025-09-03 03:55:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 1bbcd327-773c-3a4c-bda5-cada9ef51168 | -11.88565 | -50.62545 | 2025-09-03 03:55:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 9d1d31df-cac2-3b58-b968-2456c4f83d4b | -10.12631 | -46.25012 | 2025-09-03 03:55:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 70e8e348-dc04-3fe8-b858-8ce7aa807065 | -12.4024 | -44.59103 | 2025-09-03 03:55:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 3877d29b-8563-3764-a02a-f71ea8276f12 | -14.34332 | -52.80531 | 2025-09-03 03:55:00 | NOAA-20 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 1ac42ace-a339-353a-af1c-d8a2d9a55cf5 | -15.54662 | -48.36501 | 2025-09-03 03:55:00 | NOAA-20 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |
| c3afe5d0-7f10-3653-89b3-88d93fb0d2c0 | -11.06208 | -52.08321 | 2025-09-03 03:55:00 | NOAA-20 | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 29ec4fd5-3155-3cdd-9862-66e1286cbd21 | -9.70539 | -48.30394 | 2025-09-03 03:55:00 | NOAA-20 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| c0cf6a16-88be-39da-92bd-d2cc0bb1ec0c | -11.60573 | -52.11814 | 2025-09-03 03:55:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 4.2 |
| dc0e6544-ce3e-3c4c-a9a5-98c36dbc8c97 | -13.49749 | -46.81421 | 2025-09-03 03:55:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| dcdb2282-1833-31fe-b3c8-5e526caba3b2 | -13.29596 | -46.93236 | 2025-09-03 03:55:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 2c45f6c6-dc31-39d3-b146-8e220c79a162 | -15.1087 | -48.12556 | 2025-09-03 03:55:00 | NOAA-20 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d6c60c7c-df4b-373c-b97f-45119af50566 | -11.61356 | -52.07943 | 2025-09-03 03:55:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 3.8 |
| c2314fab-2b0f-33d6-96cf-d3dbe90f6f85 | -14.72354 | -46.74818 | 2025-09-03 03:55:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 849f8619-9903-3056-a8a1-a6511413e60b | -14.786 | -48.16022 | 2025-09-03 03:55:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 2e7cd533-b035-3934-a0a9-324021b4ab77 | -15.12282 | -48.1559 | 2025-09-03 03:55:00 | NOAA-20 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| da775d4d-ca8d-385e-993a-bb13254283a6 | -10.1347 | -46.25599 | 2025-09-03 03:55:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 9cf0522e-98b2-32d6-94c4-7af572367fd5 | -14.97147 | -50.20355 | 2025-09-03 03:55:00 | NOAA-20 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| a9d5b76c-6d33-31e4-ae15-09b150868594 | -13.73588 | -46.93674 | 2025-09-03 03:55:00 | NOAA-20 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 6811e58f-172f-369a-8cec-47133673dfde | -14.74099 | -46.97005 | 2025-09-03 03:55:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a16392e1-5fb0-3e64-8ae2-61a18cfb15fb | -11.60596 | -52.08376 | 2025-09-03 03:55:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 040e5979-5b89-3bea-837c-b3827149e683 | -15.11609 | -48.16504 | 2025-09-03 03:55:00 | NOAA-20 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 5d6f4c8b-53fa-3763-a305-c022c7d834b3 | -15.89766 | -48.16573 | 2025-09-03 03:55:00 | NOAA-20 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 9.1 |
| 456eeea3-fa86-324e-ab9d-91df0bb130ee | -15.12446 | -48.17265 | 2025-09-03 03:55:00 | NOAA-20 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 212621b2-286a-393a-ab29-79c95069d28d | -9.76045 | -46.91729 | 2025-09-03 03:55:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 1f9170c5-d67e-32a6-85f1-8f147d900ff1 | -15.59689 | -52.68365 | 2025-09-03 03:55:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 35dd5d5a-5b6f-33a6-a2d0-dcbee0c006ef | -13.72897 | -46.93918 | 2025-09-03 03:55:00 | NOAA-20 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 454f1986-224f-34ee-92ad-d37a69d12966 | -14.40658 | -51.69947 | 2025-09-03 03:55:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| d2dcde0e-5b12-36e5-bc89-e2480a80b64a | -14.55503 | -53.04517 | 2025-09-03 03:55:00 | NOAA-20 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 3.3 |
| eb812f87-c222-3cb0-aeb9-59b3a3810c86 | -10.54154 | -50.42664 | 2025-09-03 03:55:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| f4d88a18-dd9b-3194-a675-3ce6f96f54e3 | -12.8776 | -48.03028 | 2025-09-03 03:55:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 4b3143c4-7024-3a12-97cf-7342a999a8be | -12.41365 | -47.49954 | 2025-09-03 03:55:00 | NOAA-20 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 3479aecb-f7af-3df6-adb5-489931b67fa5 | -11.85423 | -51.41922 | 2025-09-03 03:55:00 | NOAA-20 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| e1836a8a-45b4-3178-b2f7-f053c59fd83c | -10.73093 | -44.81047 | 2025-09-03 03:55:00 | NOAA-20 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 78ef436c-6ba1-3562-b60e-0e3dfb60c825 | -10.48432 | -50.35595 | 2025-09-03 03:55:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 00cc30b4-25c7-33cb-9d33-82530ef00f57 | -11.59057 | -52.12634 | 2025-09-03 03:55:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 30.0 |
| f1769e13-93e1-3bff-ab62-034a68f47e4a | -9.14248 | -49.66365 | 2025-09-03 03:55:00 | NOAA-20 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 78dbac67-f965-3e86-8747-5e8a2109d4d7 | -15.59795 | -52.6787 | 2025-09-03 03:55:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ff71f785-7ff3-35a9-ab65-76193c0619f6 | -14.56461 | -48.05193 | 2025-09-03 03:55:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 8f27d771-95b2-3633-bf9b-68d520cbebc1 | -14.04759 | -44.62405 | 2025-09-03 03:55:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 06c14a9e-1208-31c5-a6ab-621d7aa4fccf | -10.48328 | -50.34554 | 2025-09-03 03:55:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 86eb0ab0-7ee6-33a8-838f-972284d5fed3 | -10.13614 | -46.30131 | 2025-09-03 03:55:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 145f8153-68cb-3638-970e-fb53d86a3f7a | -13.71097 | -46.93592 | 2025-09-03 03:55:00 | NOAA-20 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| c2c7c5b5-75f0-38b4-80f7-240cce4b7119 | -10.91842 | -50.86641 | 2025-09-03 03:55:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 7536111b-81a7-373d-aa56-3ce9fdf4cc68 | -13.29903 | -46.92133 | 2025-09-03 03:55:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 9927745d-9066-372a-9d26-93b1095a8493 | -11.59171 | -52.12073 | 2025-09-03 03:55:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 30.0 |
| 94a82a79-e5be-316b-909e-7099582dd368 | -15.59356 | -52.68607 | 2025-09-03 03:55:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 2c1032a3-bf22-3979-9674-7c044e46d467 | -15.11869 | -48.1767 | 2025-09-03 03:55:00 | NOAA-20 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |


[Clique aqui para ver as próximas entradas](README42.md)
