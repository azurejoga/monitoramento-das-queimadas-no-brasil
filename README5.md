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
| d601806f-9e19-32b5-a8bc-20610302125d | -21.07271 | -56.3951 | 2025-01-23 06:03:00 | AQUA_M-M | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 4ebba9cd-919c-30de-b050-96c1bfd21fcb | 2.17526 | -61.82141 | 2025-01-23 06:03:00 | NOAA-21 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 286f9219-ab4f-3f63-b1f6-4cbc2594fea0 | 3.61668 | -61.64997 | 2025-01-23 06:03:00 | NOAA-21 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 87cfff0a-99e1-346a-83dd-95f63cf3300f | 3.62061 | -61.64388 | 2025-01-23 06:03:00 | NOAA-21 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 0234b455-596e-379a-99de-73e05fa2458c | 3.51219 | -60.70921 | 2025-01-23 06:03:00 | NOAA-21 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c3a834e8-e860-309b-bb32-e34d8ae4d020 | 2.18135 | -61.85943 | 2025-01-23 06:03:00 | NOAA-21 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5987176c-65b5-3391-92e7-d4ce96d0f551 | 2.17438 | -61.81592 | 2025-01-23 06:03:00 | NOAA-21 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 3.0 |
| c074cc9e-eb4f-37ae-baf6-65585c769a7e | 1.05942 | -59.90083 | 2025-01-23 06:05:00 | NOAA-21 | SÃO JOÃO DA BALIZA | RORAIMA | Brasil | 1400506 | 14 | 33 | nan | nan | nan | Amazônia | 4.0 |
| f2d0f23b-9317-3fc4-ba57-cee597bccf51 | 1.05667 | -59.90134 | 2025-01-23 06:05:00 | NOAA-21 | SÃO JOÃO DA BALIZA | RORAIMA | Brasil | 1400506 | 14 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 7092caea-c570-3000-a8bd-326d6a0a93d4 | -15.73 | -45.95 | 2025-01-23 12:00:00 | MSG-03 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 99ce7a55-d6f6-387d-8a1b-70c6a15c9c57 | -15.83 | -43.46 | 2025-01-23 12:00:00 | MSG-03 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| a80bb025-eca0-380e-a841-fef476a7fdd9 | -4.54259 | -38.02962 | 2025-01-23 12:04:00 | TERRA_M-T | BEBERIBE | CEARÁ | Brasil | 2302206 | 23 | 33 | nan | nan | nan | Caatinga | 5.8 |
| ee48dde2-7210-3a37-9f7f-364c5bf0c81d | -8.6624 | -37.57833 | 2025-01-23 12:04:00 | TERRA_M-T | IBIMIRIM | PERNAMBUCO | Brasil | 2606606 | 26 | 33 | nan | nan | nan | Caatinga | 9.5 |
| 40fd4163-7f32-356f-bb0f-d1a80f8eb838 | -9.5276 | -40.66088 | 2025-01-23 12:04:00 | TERRA_M-T | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 8.5 |
| 5a9385b5-9f57-32f3-a36a-03c8fe463652 | -11.88107 | -37.77878 | 2025-01-23 12:04:00 | TERRA_M-T | ESPLANADA | BAHIA | Brasil | 2910602 | 29 | 33 | nan | nan | nan | Mata Atlântica | 11.5 |
| c376c164-e877-3630-9d37-a39da60d8a94 | -9.90356 | -37.05131 | 2025-01-23 12:04:00 | TERRA_M-T | TRAIPU | ALAGOAS | Brasil | 2709202 | 27 | 33 | nan | nan | nan | Mata Atlântica | 10.7 |
| d94ba335-0169-3ccf-9b54-6bdafdd69f0b | -9.60457 | -36.83531 | 2025-01-23 12:04:00 | TERRA_M-T | CRAÍBAS | ALAGOAS | Brasil | 2702355 | 27 | 33 | nan | nan | nan | Caatinga | 14.5 |
| a7e9b17b-e488-34b2-b272-eed3696b4419 | -9.60869 | -36.83089 | 2025-01-23 12:04:00 | TERRA_M-T | CRAÍBAS | ALAGOAS | Brasil | 2702355 | 27 | 33 | nan | nan | nan | Caatinga | 9.0 |
| b54eef69-b3b9-314b-bf76-ef7b5f3cb254 | -9.81031 | -36.98957 | 2025-01-23 12:04:00 | TERRA_M-T | TRAIPU | ALAGOAS | Brasil | 2709202 | 27 | 33 | nan | nan | nan | Caatinga | 11.2 |
| dcb37f6a-71b2-3ee4-95e1-0b34d3848e92 | -11.20195 | -38.03888 | 2025-01-23 12:04:00 | TERRA_M-T | ITAPICURU | BAHIA | Brasil | 2916500 | 29 | 33 | nan | nan | nan | Caatinga | 11.4 |
| 78bc04d8-bf7f-3611-9c18-5b739506ca61 | -12.68006 | -38.80088 | 2025-01-23 12:04:00 | TERRA_M-T | SANTO AMARO | BAHIA | Brasil | 2928604 | 29 | 33 | nan | nan | nan | Mata Atlântica | 6.2 |
| 39e21e41-6ac1-36ab-babf-9e9be9da4a51 | -11.50074 | -39.70905 | 2025-01-23 12:04:00 | TERRA_M-T | GAVIÃO | BAHIA | Brasil | 2911253 | 29 | 33 | nan | nan | nan | Caatinga | 6.8 |
| 00ee9ec3-8e3d-38b7-87c0-9553d40ee959 | -12.17682 | -38.77965 | 2025-01-23 12:04:00 | TERRA_M-T | CORAÇÃO DE MARIA | BAHIA | Brasil | 2908903 | 29 | 33 | nan | nan | nan | Mata Atlântica | 13.5 |
| 9e3e2a0f-9e0f-3e70-b576-6cb1b4e65546 | -11.4759 | -40.83398 | 2025-01-23 12:04:00 | TERRA_M-T | MORRO DO CHAPÉU | BAHIA | Brasil | 2921708 | 29 | 33 | nan | nan | nan | Caatinga | 5.6 |
| dc063321-bc5f-3d2d-9dca-9769d7247e9e | -8.84554 | -36.71852 | 2025-01-23 12:04:00 | TERRA_M-T | PARANATAMA | PERNAMBUCO | Brasil | 2610301 | 26 | 33 | nan | nan | nan | Caatinga | 16.1 |
| d68fe57e-1d76-3676-9974-bb5e961b7387 | -11.47709 | -38.04529 | 2025-01-23 12:04:00 | TERRA_M-T | RIO REAL | BAHIA | Brasil | 2927002 | 29 | 33 | nan | nan | nan | Caatinga | 19.0 |
| c1d24f99-50c6-3693-aa6a-8504e3435725 | -5.91738 | -37.89671 | 2025-01-23 12:04:00 | TERRA_M-T | APODI | RIO GRANDE DO NORTE | Brasil | 2401008 | 24 | 33 | nan | nan | nan | Caatinga | 10.9 |
| df3575ca-0da6-3f2c-b221-552ba9e232f2 | -9.86883 | -37.1634 | 2025-01-23 12:04:00 | TERRA_M-T | BELO MONTE | ALAGOAS | Brasil | 2700904 | 27 | 33 | nan | nan | nan | Caatinga | 11.8 |
| 18226ca2-4327-3eab-b51a-80244018a15a | -11.49944 | -39.71804 | 2025-01-23 12:04:00 | TERRA_M-T | GAVIÃO | BAHIA | Brasil | 2911253 | 29 | 33 | nan | nan | nan | Caatinga | 7.4 |
| acb9d755-ce29-313e-937a-5814b443e19a | -9.90211 | -37.06192 | 2025-01-23 12:04:00 | TERRA_M-T | TRAIPU | ALAGOAS | Brasil | 2709202 | 27 | 33 | nan | nan | nan | Mata Atlântica | 16.2 |
| 2c58ddd6-4a5b-387e-89cd-cd4bd034a99e | -8.90514 | -37.41305 | 2025-01-23 12:04:00 | TERRA_M-T | ITAÍBA | PERNAMBUCO | Brasil | 2607505 | 26 | 33 | nan | nan | nan | Caatinga | 5.8 |
| 63ef772f-a077-334e-b9d3-c43dd2a93c1b | -9.80429 | -37.49609 | 2025-01-23 12:04:00 | TERRA_M-T | PORTO DA FOLHA | SERGIPE | Brasil | 2805604 | 28 | 33 | nan | nan | nan | Caatinga | 8.1 |
| cd1960eb-8d9e-39fc-949e-e698fea103f4 | -9.53662 | -40.6622 | 2025-01-23 12:04:00 | TERRA_M-T | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 5.0 |
| a642fc6d-b9c8-3ae8-a846-512d91f3e83b | -18.85562 | -39.91513 | 2025-01-23 12:06:00 | TERRA_M-T | SÃO MATEUS | ESPÍRITO SANTO | Brasil | 3204906 | 32 | 33 | nan | nan | nan | Mata Atlântica | 6.7 |
| f1d2c38b-b0a3-3826-afa9-3681a826762e | -15.9317 | -39.30895 | 2025-01-23 12:06:00 | TERRA_M-T | BELMONTE | BAHIA | Brasil | 2903409 | 29 | 33 | nan | nan | nan | Mata Atlântica | 9.1 |
| ee829c17-2bfc-32ad-af4b-6dda48f48aef | -17.83566 | -40.04681 | 2025-01-23 12:06:00 | TERRA_M-T | IBIRAPUÃ | BAHIA | Brasil | 2912806 | 29 | 33 | nan | nan | nan | Mata Atlântica | 9.5 |
| 59a4cb44-4676-35a8-ac1c-3282d83856b0 | -14.10236 | -41.65691 | 2025-01-23 12:06:00 | TERRA_M-T | BRUMADO | BAHIA | Brasil | 2904605 | 29 | 33 | nan | nan | nan | Caatinga | 7.0 |
| c132b3ef-a301-3eda-981e-9465207f219e | -16.20868 | -39.43682 | 2025-01-23 12:06:00 | TERRA_M-T | EUNÁPOLIS | BAHIA | Brasil | 2910727 | 29 | 33 | nan | nan | nan | Mata Atlântica | 16.5 |
| 49eb54ef-0d97-3b32-9c88-d21e389acd83 | -17.4162 | -40.21738 | 2025-01-23 12:06:00 | TERRA_M-T | MEDEIROS NETO | BAHIA | Brasil | 2921104 | 29 | 33 | nan | nan | nan | Mata Atlântica | 310.0 |
| 037e4a1d-2c13-34e5-9539-1b81a5d9a0ed | -12.59663 | -44.10138 | 2025-01-23 12:06:00 | TERRA_M-T | TABOCAS DO BREJO VELHO | BAHIA | Brasil | 2930907 | 29 | 33 | nan | nan | nan | Cerrado | 12.5 |
| feaf8834-6006-3a73-a16c-3aeba602f7c7 | -22.67714 | -42.84893 | 2025-01-23 12:08:00 | TERRA_M-T | ITABORAÍ | RIO DE JANEIRO | Brasil | 3301900 | 33 | 33 | nan | nan | nan | Mata Atlântica | 13.4 |
| 95ea5d27-b781-3f94-9742-e7e4fe0e6af4 | -22.67572 | -42.85855 | 2025-01-23 12:08:00 | TERRA_M-T | ITABORAÍ | RIO DE JANEIRO | Brasil | 3301900 | 33 | 33 | nan | nan | nan | Mata Atlântica | 10.0 |


