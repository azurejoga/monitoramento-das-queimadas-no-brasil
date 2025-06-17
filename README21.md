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

## Dados Diários - Página 21

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 03283e75-e034-374d-9d6b-7f6d60eab516 | -10.2782 | -60.53635 | 2025-06-17 04:57:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d6d7e46a-d4c0-3618-bb29-74a072c8ec23 | -14.82342 | -48.45142 | 2025-06-17 04:57:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 20c4e0b9-94ec-3752-8d3f-d6f05ae28e23 | -14.85182 | -52.28632 | 2025-06-17 04:57:00 | NOAA-20 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 1a25beca-7e02-3ba7-8d44-e61f6fcae584 | -9.88652 | -47.80988 | 2025-06-17 04:57:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 5a349117-f171-30cd-9c29-d111dccf0cfd | -12.22254 | -55.52223 | 2025-06-17 04:57:00 | NOAA-20 | VERA | MATO GROSSO | Brasil | 5108501 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| db196f0c-21f4-3b0c-a42f-51721fd9c0bc | -12.5092 | -58.34908 | 2025-06-17 04:57:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ae201f45-c765-3920-b9f4-5a6967ef1905 | -11.88314 | -54.67295 | 2025-06-17 04:57:00 | NOAA-20 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 2a5772d0-ea84-38db-bff4-091878891dd9 | -13.44402 | -56.85288 | 2025-06-17 04:57:00 | NOAA-20 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 4a5ad0f1-04ed-3863-8f25-5529c55afa9d | -10.17123 | -52.62002 | 2025-06-17 04:57:00 | NOAA-20 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| cf87b189-263c-3a68-a3ed-40bfafc08151 | -11.02643 | -44.64494 | 2025-06-17 04:57:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 9204661b-749b-3b2b-8264-d5947e1453ab | -10.29895 | -57.13964 | 2025-06-17 04:57:00 | NOAA-20 | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| dce4ce79-6d3c-3944-9f7a-8cc2a447173c | -9.95084 | -54.17598 | 2025-06-17 04:57:00 | NOAA-20 | MATUPÁ | MATO GROSSO | Brasil | 5105606 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 41ba4058-ef2b-37b8-b158-0df6ae62ba74 | -10.28364 | -60.52959 | 2025-06-17 04:57:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| b07bcc61-8580-3749-a0f0-f99f31f960bb | -9.45877 | -58.2153 | 2025-06-17 04:57:00 | NOAA-20 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| cc5370c5-f6d7-32ce-a8c6-fb261c11c439 | -11.14111 | -53.93718 | 2025-06-17 04:57:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 9.8 |
| 3e5c4b2e-e7db-334b-b83e-95818525eb65 | -10.66974 | -56.62887 | 2025-06-17 04:57:00 | NOAA-20 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 3db682eb-e9f0-3170-b91d-003ba4bca23e | -18.643 | -53.3162 | 2025-06-17 04:59:00 | NOAA-20 | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 0.8 |
| b62025c3-0d8e-3035-9219-d869e0bed578 | -17.4393 | -52.93585 | 2025-06-17 04:59:00 | NOAA-20 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e8980960-1472-3f68-a70f-77e3a0af4d0d | -21.4243 | -48.64463 | 2025-06-17 04:59:00 | NOAA-20 | TAQUARITINGA | SÃO PAULO | Brasil | 3553708 | 35 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 969b4806-c9d1-39f1-b3a2-4761e71d44b2 | -17.43785 | -52.93335 | 2025-06-17 04:59:00 | NOAA-20 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a917a83a-15af-3e41-929c-57b2929aa5f0 | -19.00829 | -52.08786 | 2025-06-17 04:59:00 | NOAA-20 | CASSILÂNDIA | MATO GROSSO DO SUL | Brasil | 5002902 | 50 | 33 | nan | nan | nan | Cerrado | 3.6 |
| c48f7ee2-3607-39a7-a8e6-4153fd82303c | -20.65516 | -54.87157 | 2025-06-17 04:59:00 | NOAA-20 | TERENOS | MATO GROSSO DO SUL | Brasil | 5008008 | 50 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 91b32c2d-7e24-3d15-85e0-f049d67c2dee | -22.77419 | -49.31223 | 2025-06-17 04:59:00 | NOAA-20 | ÁGUAS DE SANTA BÁRBARA | SÃO PAULO | Brasil | 3500550 | 35 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 158da600-01a1-378f-b06e-6599c3c604ac | -20.92114 | -49.09907 | 2025-06-17 04:59:00 | NOAA-20 | TABAPUÃ | SÃO PAULO | Brasil | 3552601 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 467b68b3-2e24-3bcf-977c-b2786ca7df3a | -20.55394 | -54.12397 | 2025-06-17 04:59:00 | NOAA-20 | RIBAS DO RIO PARDO | MATO GROSSO DO SUL | Brasil | 5007109 | 50 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 874bbc4c-58e8-3d09-862c-f30b4a36767c | -17.43992 | -52.93129 | 2025-06-17 04:59:00 | NOAA-20 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 5.4 |
| b4c74373-f892-350f-8f56-834faf7d7619 | -20.55455 | -54.11951 | 2025-06-17 04:59:00 | NOAA-20 | RIBAS DO RIO PARDO | MATO GROSSO DO SUL | Brasil | 5007109 | 50 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e94a922a-db09-39d6-bea1-f8d6a0d73842 | -22.77354 | -49.31849 | 2025-06-17 04:59:00 | NOAA-20 | ÁGUAS DE SANTA BÁRBARA | SÃO PAULO | Brasil | 3500550 | 35 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 1f3e3fd5-6530-3c36-bc6e-f802b21026d9 | -20.92175 | -49.09324 | 2025-06-17 04:59:00 | NOAA-20 | TABAPUÃ | SÃO PAULO | Brasil | 3552601 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.1 |
| 7b11951e-82df-3ca6-b17b-b6e427dc810a | -20.01019 | -44.18541 | 2025-06-17 04:59:00 | NOAA-20 | BETIM | MINAS GERAIS | Brasil | 3106705 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.0 |
| b09bb322-aa04-31ee-8fc2-9d7817c215b5 | -21.42463 | -48.64151 | 2025-06-17 04:59:00 | NOAA-20 | TAQUARITINGA | SÃO PAULO | Brasil | 3553708 | 35 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ebc401c0-ee6b-3550-87e9-70ec7420e6cb | -22.76853 | -49.31794 | 2025-06-17 04:59:00 | NOAA-20 | ÁGUAS DE SANTA BÁRBARA | SÃO PAULO | Brasil | 3500550 | 35 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 1b3cfa8e-bbf7-392e-ad41-16e1dbcecd3b | -22.53772 | -48.81224 | 2025-06-17 04:59:00 | NOAA-20 | MACATUBA | SÃO PAULO | Brasil | 3528007 | 35 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 7e8d7506-8661-3605-bca7-1fd67f4600b6 | -21.61589 | -57.57199 | 2025-06-17 04:59:00 | NOAA-20 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 0.6 |
| e329e4ea-e580-3204-bc2f-cad8781ee3a3 | -20.92033 | -49.09818 | 2025-06-17 04:59:00 | NOAA-20 | TABAPUÃ | SÃO PAULO | Brasil | 3552601 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| 84932561-1a68-315b-977b-0575681e6881 | -20.9253 | -49.09867 | 2025-06-17 04:59:00 | NOAA-20 | TABAPUÃ | SÃO PAULO | Brasil | 3552601 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| eac46094-89fa-387f-a65f-f680612f3dd1 | -20.23441 | -46.74162 | 2025-06-17 04:59:00 | NOAA-20 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| fede582a-4ae8-3d7e-92e1-7c32d46a4736 | -20.24043 | -46.73919 | 2025-06-17 04:59:00 | NOAA-20 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 2a59ce29-edfd-3465-b051-74fa8e549c58 | -20.00804 | -44.18084 | 2025-06-17 04:59:00 | NOAA-20 | BETIM | MINAS GERAIS | Brasil | 3106705 | 31 | 33 | nan | nan | nan | Mata Atlântica | 7.0 |
| 0f55fa20-b9c1-3901-8d8f-713945a75b48 | -22.76917 | -49.3117 | 2025-06-17 04:59:00 | NOAA-20 | ÁGUAS DE SANTA BÁRBARA | SÃO PAULO | Brasil | 3500550 | 35 | 33 | nan | nan | nan | Cerrado | 2.7 |
| f9cc9c69-fa17-3b6f-be04-286fc2ef1b5d | -19.02286 | -57.62171 | 2025-06-17 04:59:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.2 |
| bc014d58-d689-38dc-b487-aac8fe880b4d | -20.2401 | -46.74266 | 2025-06-17 04:59:00 | NOAA-20 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a499dbf6-aa87-3d29-b7c8-8c71f41c0c4e | -19.70059 | -47.02063 | 2025-06-17 04:59:00 | NOAA-20 | ARAXÁ | MINAS GERAIS | Brasil | 3104007 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 587b070b-d1d9-3133-9fe2-d0353dce628a | -18.32256 | -49.88394 | 2025-06-17 04:59:00 | NOAA-20 | ITUMBIARA | GOIÁS | Brasil | 5211503 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b6e12e63-495f-3674-8c88-5bca48f5c14c | -17.44364 | -52.93182 | 2025-06-17 04:59:00 | NOAA-20 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 776d89be-da1e-3bbc-bba1-9058b110598f | -20.706 | -54.89233 | 2025-06-17 04:59:00 | NOAA-20 | TERENOS | MATO GROSSO DO SUL | Brasil | 5008008 | 50 | 33 | nan | nan | nan | Cerrado | 0.4 |
| d1c9237b-6d8d-3969-b322-74b20ff6e564 | -19.70099 | -47.01669 | 2025-06-17 04:59:00 | NOAA-20 | ARAXÁ | MINAS GERAIS | Brasil | 3104007 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| fd82d23a-de3c-3b8e-a0a1-546013b8dc29 | -19.00501 | -52.08193 | 2025-06-17 04:59:00 | NOAA-20 | CASSILÂNDIA | MATO GROSSO DO SUL | Brasil | 5002902 | 50 | 33 | nan | nan | nan | Cerrado | 3.6 |
| f5bb2734-c856-3b90-b05f-f7ab858b9e14 | -21.61647 | -57.56829 | 2025-06-17 04:59:00 | NOAA-20 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 595196c7-c1db-3b30-af29-13df88a7eb42 | -20.01073 | -44.17916 | 2025-06-17 04:59:00 | NOAA-20 | BETIM | MINAS GERAIS | Brasil | 3106705 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.0 |
| fd00d152-081a-3ad3-9e11-0e3486482315 | -19.00432 | -52.08724 | 2025-06-17 04:59:00 | NOAA-20 | CASSILÂNDIA | MATO GROSSO DO SUL | Brasil | 5002902 | 50 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 6d88e35f-6824-3926-9cc6-75f5798523cd | -7.2605 | -44.6421 | 2025-06-17 05:20:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 73.5 |
| d5cdf380-5a79-35e3-969e-754ab2dfc5ae | -7.2605 | -44.6421 | 2025-06-17 05:30:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 74.4 |
| ad97b4ee-949f-3b00-b17f-9d70066fedc2 | -3.99886 | -43.23837 | 2025-06-17 05:31:00 | AQUA_M-M | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 6.3 |
| bd4db06d-704e-351f-b790-8d1e4c5df0b1 | -7.23953 | -43.0791 | 2025-06-17 05:31:00 | AQUA_M-M | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 6.6 |
| 6ae224be-42ae-33d8-9ac0-afde79e2e238 | -7.27076 | -44.64017 | 2025-06-17 05:31:00 | AQUA_M-M | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 203cb7f3-7c0d-3b1a-9ab2-c45e7610ad43 | -7.11135 | -47.84323 | 2025-06-17 05:31:00 | AQUA_M-M | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 8.6 |
| 43a1de03-fe3a-3b90-bdd7-ce1ecc18dbcd | -6.12053 | -42.52689 | 2025-06-17 05:31:00 | AQUA_M-M | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 14.1 |
| 1d8c77b3-7139-323d-adea-cacd2c5da65b | -7.23072 | -43.0778 | 2025-06-17 05:31:00 | AQUA_M-M | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 4.3 |
| 0bb5259c-2b0f-347a-98fd-bafc717b9f32 | -8.06532 | -43.11237 | 2025-06-17 05:31:00 | AQUA_M-M | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 26.0 |
| 1fee8fb0-8961-3034-a55a-bddfb979736a | -7.26039 | -44.64803 | 2025-06-17 05:31:00 | AQUA_M-M | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 46.9 |
| dcf7c786-6af5-3e41-87b0-f2cb83945810 | -7.23821 | -43.08793 | 2025-06-17 05:31:00 | AQUA_M-M | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 10.0 |
| 55c4420e-176c-3e0d-a8cc-0a523eb4e786 | -7.24702 | -43.08923 | 2025-06-17 05:31:00 | AQUA_M-M | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 15.2 |
| d11e37f9-e79d-3ad6-8edd-2890f44aba33 | -7.2618 | -44.63886 | 2025-06-17 05:31:00 | AQUA_M-M | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 50.6 |
| f1427d6d-eb47-3c41-9f57-fc9ffe10b41f | -6.48686 | -42.8497 | 2025-06-17 05:31:00 | AQUA_M-M | AMARANTE | PIAUÍ | Brasil | 2200509 | 22 | 33 | nan | nan | nan | Caatinga | 7.0 |
| 40f14970-117b-3768-9fb8-b482c1e7d92c | -6.48819 | -42.84088 | 2025-06-17 05:31:00 | AQUA_M-M | AMARANTE | PIAUÍ | Brasil | 2200509 | 22 | 33 | nan | nan | nan | Caatinga | 4.6 |
| 8f3a09b4-53b2-350a-835f-e311365ac72a | -8.07547 | -43.10478 | 2025-06-17 05:31:00 | AQUA_M-M | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 34.3 |
| 99c281c1-bf09-3d3c-8539-3704f1d9cf16 | -6.12185 | -42.51802 | 2025-06-17 05:31:00 | AQUA_M-M | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 6.5 |
| 9a4cd116-dbcd-32e7-bd8e-d2d615dac88d | -5.07352 | -43.72207 | 2025-06-17 05:31:00 | AQUA_M-M | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 6.1 |
| c9166dd9-d241-3c13-935b-bf5bdb96a824 | -8.07414 | -43.11367 | 2025-06-17 05:31:00 | AQUA_M-M | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 40.7 |
| e57de071-9d71-38b5-be02-7dbf116310a3 | -5.56908 | -45.19437 | 2025-06-17 05:31:00 | AQUA_M-M | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 513a5c1e-9966-36c2-80a6-127e6b6f8012 | -7.17911 | -43.60153 | 2025-06-17 05:31:00 | AQUA_M-M | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 8.2 |
| e1a70d57-4390-3b4d-b26c-b913252c6541 | -8.06664 | -43.10349 | 2025-06-17 05:31:00 | AQUA_M-M | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 15.1 |
| 3e497d71-2d5e-3811-9d73-c30577900a27 | -6.29027 | -44.22833 | 2025-06-17 05:31:00 | AQUA_M-M | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 10.6 |
| da223614-82c6-385a-9d0f-56dcbaf1b869 | -6.66964 | -43.18299 | 2025-06-17 05:31:00 | AQUA_M-M | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Caatinga | 8.1 |
| 2770e592-2934-3a30-95f4-00a573195ba7 | -5.56756 | -45.20431 | 2025-06-17 05:31:00 | AQUA_M-M | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 6.8 |
| abfcb9b8-c33d-3941-a124-ace0962bd28f | -7.54268 | -45.64226 | 2025-06-17 05:31:00 | AQUA_M-M | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 81a435c3-699a-3001-8af5-c5a1f80b5b89 | -13.46194 | -46.26748 | 2025-06-17 05:33:00 | AQUA_M-M | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 4ec3b3a9-a7e0-33b2-8594-6749199e4ae9 | -13.46044 | -46.27699 | 2025-06-17 05:33:00 | AQUA_M-M | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 162c4b07-4894-3180-a96e-85af3ea15164 | -14.85762 | -45.1293 | 2025-06-17 05:33:00 | AQUA_M-M | BONITO DE MINAS | MINAS GERAIS | Brasil | 3108255 | 31 | 33 | nan | nan | nan | Cerrado | 6.8 |
| e8a02b83-9510-3f30-9fe3-e1474b688f01 | -10.83203 | -46.94731 | 2025-06-17 05:33:00 | AQUA_M-M | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 7.7 |
| ed3c0f1a-0280-39ce-a047-4247bbf1ba47 | -9.41105 | -48.41507 | 2025-06-17 05:33:00 | AQUA_M-M | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 16.8 |
| 5dc78446-7192-34b3-a603-916c981fa337 | -11.14014 | -53.92941 | 2025-06-17 05:33:00 | AQUA_M-M | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 41.8 |
| 2f92b60a-552b-3cc3-9ee5-dc58a6031861 | -8.96335 | -47.96843 | 2025-06-17 05:33:00 | AQUA_M-M | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 8.7 |
| d3fbfeb4-ff0d-3e0c-9685-2364a433b53c | -9.39704 | -48.4202 | 2025-06-17 05:33:00 | AQUA_M-M | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 10.3 |
| 686d6740-313e-314f-ba3a-9b97b12e5bdb | -9.40795 | -48.42197 | 2025-06-17 05:33:00 | AQUA_M-M | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 12.4 |
| 85e650d0-3b7e-3e2b-9f96-efce4c058bfa | -9.41017 | -48.40809 | 2025-06-17 05:33:00 | AQUA_M-M | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 17.1 |
| f5ab2e6d-745e-3e40-ac03-092bbfaa2293 | -20.0117 | -44.17479 | 2025-06-17 05:38:00 | AQUA_M-M | BETIM | MINAS GERAIS | Brasil | 3106705 | 31 | 33 | nan | nan | nan | Mata Atlântica | 9.7 |
| 7a12817b-550a-3b95-a138-6e9dc4c32a56 | -7.2605 | -44.6421 | 2025-06-17 05:40:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 78.1 |
| 3a933287-1678-3fe7-800c-5e12922aff17 | -7.72541 | -55.13659 | 2025-06-17 05:48:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 57e7ae8c-f5de-3572-a3c4-ccf58f6ca662 | -7.98374 | -55.29938 | 2025-06-17 05:48:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 08100bd9-b347-37bc-91f0-a49575985034 | -7.98441 | -55.2939 | 2025-06-17 05:48:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| be2b412c-162b-36f5-bbfd-ba3a15cc789d | -7.72472 | -55.142 | 2025-06-17 05:48:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| e3fc8c54-dc56-3f78-915e-7367bb84307e | -7.98194 | -55.30046 | 2025-06-17 05:48:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| b0a908b2-ca83-3a70-a089-62e49f1ff8d6 | -7.98265 | -55.29499 | 2025-06-17 05:48:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 924df6dd-1118-3865-a348-b57b8bbeb6b8 | -7.2605 | -44.6421 | 2025-06-17 05:50:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 71.0 |
| eaed7194-c3e7-3d57-b159-a7dc3bfd5dee | -10.29987 | -60.53228 | 2025-06-17 05:50:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 63e78e88-6487-36b3-8345-3861658b40b0 | -10.29688 | -57.14122 | 2025-06-17 05:50:00 | NOAA-21 | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 9e3e2387-a108-3c8b-b8a1-32098087a98a | -10.52193 | -59.39021 | 2025-06-17 05:50:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c3d82884-fed0-374f-9a91-42c82afbf007 | -9.46437 | -57.85144 | 2025-06-17 05:50:00 | NOAA-21 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 7.6 |


[Clique aqui para ver as próximas entradas](README22.md)
