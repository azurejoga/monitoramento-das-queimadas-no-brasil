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

## Dados Diários - Página 199

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| de5b3084-91ee-3b74-87b4-29826f633646 | -9.6879 | -58.10563 | 2026-10-08 05:44:00 | NOAA-20 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 9e142c6a-f959-3970-bfea-197f454576bb | -8.76024 | -67.70457 | 2026-10-08 05:44:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c5adbc1f-4cc2-333b-8d1b-2d8790b113f4 | -8.54788 | -67.02598 | 2026-10-08 05:44:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 5a03fa02-9aa2-3689-b1a2-06adb6c9f500 | -11.94228 | -62.382 | 2026-10-08 05:44:00 | NOAA-20 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 01818f67-4714-364a-b8e2-1bbee40eb63d | -9.20511 | -66.08854 | 2026-10-08 05:44:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 71fc075c-655b-3528-9a9c-74258adc907a | -9.04018 | -65.93481 | 2026-10-08 05:44:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 30b2cc25-a013-30ae-97f5-b65f2c1dfc40 | -8.55192 | -67.02601 | 2026-10-08 05:44:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 797dbdde-f46c-3e67-9cbd-33f00169c078 | -8.60065 | -67.30271 | 2026-10-08 05:44:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 837ccffb-b5d4-3bf4-9c27-a4956070dc6c | -11.75285 | -61.05827 | 2026-10-08 05:44:00 | NOAA-20 | PIMENTA BUENO | RONDÔNIA | Brasil | 1100189 | 11 | 33 | nan | nan | nan | Amazônia | 3.8 |
| b14775d8-e6c5-3970-8332-a39af27d9952 | -8.47548 | -63.93442 | 2026-10-08 05:44:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| be5d044e-6a45-357f-ab11-76220c810cf6 | -10.36628 | -61.2188 | 2026-10-08 05:44:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 49d2e1ce-d964-3401-9be0-599c908c87ce | -9.58185 | -65.24834 | 2026-10-08 05:44:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 66dae3af-6d30-3cc7-870e-1358670ca3d3 | -10.05585 | -62.4591 | 2026-10-08 05:44:00 | NOAA-20 | THEOBROMA | RONDÔNIA | Brasil | 1101609 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 5705f2f0-92f1-321c-a461-5bfc062a9410 | -10.4173 | -60.653 | 2026-10-08 05:44:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| cfa186af-9e8a-390f-a3c6-ea3e844a6799 | -8.84946 | -66.80428 | 2026-10-08 05:44:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 299afb64-8b8b-33d5-9fda-6ffdace85aae | -13.80037 | -52.79339 | 2026-10-08 05:44:00 | NOAA-20 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 84fa9f4c-3449-3862-a380-870e380b28ad | -10.23296 | -58.21755 | 2026-10-08 05:44:00 | NOAA-20 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 06f92ebe-0a0f-3960-88db-2af20309c8f9 | -10.32331 | -64.51552 | 2026-10-08 05:44:00 | NOAA-20 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ef9fd55e-3a5e-35e6-afb4-d8d81f66bf05 | -9.13821 | -65.30271 | 2026-10-08 05:44:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 81aa145d-d972-327f-91c6-42860f633f65 | -9.34631 | -65.46336 | 2026-10-08 05:44:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e4e2141e-3cbb-3c5e-8a5d-d32c3c5d4712 | -10.05238 | -62.45856 | 2026-10-08 05:44:00 | NOAA-20 | THEOBROMA | RONDÔNIA | Brasil | 1101609 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 359983cf-e39c-348e-913b-0a9c2bf0092d | -8.76859 | -61.38475 | 2026-10-08 05:44:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 31d069e7-dac5-36e2-9278-2cf5d2a0fba8 | -9.14046 | -65.28862 | 2026-10-08 05:44:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 7b3a458b-8c29-36de-8cbc-0852e5a4a07d | -8.62483 | -67.02197 | 2026-10-08 05:44:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 26.2 |
| 9d1d6fb5-1ce3-3ad5-aa30-b693b84c6661 | -8.59642 | -67.30618 | 2026-10-08 05:44:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 9506cf47-7aa2-330e-816b-373d4db95977 | -9.07819 | -65.48508 | 2026-10-08 05:44:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 7d47d0cc-563b-3147-8f18-c9bab8f9e1e1 | -9.3477 | -64.7124 | 2026-10-08 05:44:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2e97b943-f73f-3d98-9a76-0d69a1f775d1 | -9.47577 | -64.35471 | 2026-10-08 05:44:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| ea28ae03-395b-35c0-8949-2c970c43d106 | -9.47632 | -64.35122 | 2026-10-08 05:44:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 5bdb9c8d-92de-3aad-a5d2-c0c571c5eff6 | -9.48792 | -64.36379 | 2026-10-08 05:44:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3014a311-715f-3bf5-9441-a581b8998bb6 | -8.96947 | -65.4417 | 2026-10-08 05:44:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| de6bf273-b568-3ffe-b26c-42ce33339d43 | -10.49693 | -67.8845 | 2026-10-08 05:44:00 | NOAA-20 | CAPIXABA | ACRE | Brasil | 1200179 | 12 | 33 | nan | nan | nan | Amazônia | 1.1 |
| de0ce6b8-ead2-3e48-8bba-112a1c3b55e6 | -8.06219 | -55.29998 | 2026-10-08 05:44:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b73aa383-7b22-3da6-a714-4c0c10db6eb0 | -8.08373 | -55.29961 | 2026-10-08 05:44:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3e579fe5-637e-3d85-bc64-b0d3d0cf8d03 | -9.11311 | -65.35287 | 2026-10-08 05:44:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2fed4f95-ad33-35cf-99d7-64a33457784b | -8.61364 | -67.02418 | 2026-10-08 05:44:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 21.4 |
| d6923874-4c67-311c-ae3e-b640d6ab58bc | -8.54091 | -66.98005 | 2026-10-08 05:44:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 2e777a80-82e2-3934-af75-fea9e9dc06bc | -9.51776 | -67.10683 | 2026-10-08 05:44:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0069a0a2-d0ae-320b-bf2e-46e29165a79d | -9.36823 | -55.973 | 2026-10-08 05:44:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 70325ae1-a6ef-321e-816f-d14547a54470 | -9.17125 | -66.93975 | 2026-10-08 05:44:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 5f74e7cc-7363-3a60-bf91-39c55ef004f6 | -9.6885 | -58.1012 | 2026-10-08 05:44:00 | NOAA-20 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 0fa65747-8210-3cf8-b16c-43e62c64788f | -8.6204 | -67.005 | 2026-10-08 05:44:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| dba074cc-c777-37b7-8e47-64f8dee4376f | -8.25336 | -62.94004 | 2026-10-08 05:44:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 44f91c71-789a-32a9-9404-9c0cafc1759f | -9.24339 | -64.36372 | 2026-10-08 05:44:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1ded24a2-a49d-3f8b-9215-2fc87429e1b2 | -8.64936 | -67.18014 | 2026-10-08 05:44:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 494f67fb-a207-3dd7-a0e1-bd3d3188dc38 | -8.6148 | -67.06104 | 2026-10-08 05:44:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| aabf14fa-1149-3802-885d-9334b0676e3b | -8.06833 | -55.29432 | 2026-10-08 05:44:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 252ef451-aa9f-3167-bf8b-5e072522590c | -11.75278 | -61.06076 | 2026-10-08 05:44:00 | NOAA-20 | PIMENTA BUENO | RONDÔNIA | Brasil | 1100189 | 11 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 336cb7c4-5252-32ef-a47c-3aab9a349632 | -8.52926 | -67.05147 | 2026-10-08 05:44:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8e572d33-d000-31dc-bfdd-335d878c9ec7 | -9.59835 | -61.8213 | 2026-10-08 05:44:00 | NOAA-20 | VALE DO ANARI | RONDÔNIA | Brasil | 1101757 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| bad8b136-61e8-3c5e-845d-45504dfa66d3 | -9.14154 | -65.30325 | 2026-10-08 05:44:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 39355373-2de1-3a8f-98e5-b5c2077cd2bd | -8.08242 | -55.3093 | 2026-10-08 05:44:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b5ba7150-4311-3dc0-aa2b-c154ffa06976 | -9.68709 | -65.01392 | 2026-10-08 05:44:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e62f8186-db8b-3262-a9f0-7b7246e5e862 | -9.22534 | -67.27195 | 2026-10-08 05:44:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 40599928-d041-3505-a6fa-f62c6f828549 | -12.20433 | -57.12695 | 2026-10-08 05:44:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 47b44578-d80c-3cfe-985e-16cf48ecca18 | -11.74831 | -61.06485 | 2026-10-08 05:44:00 | NOAA-20 | PIMENTA BUENO | RONDÔNIA | Brasil | 1100189 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b99d9c1b-719e-3a62-baa4-e48030640a39 | -8.6178 | -67.02081 | 2026-10-08 05:44:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 18.3 |
| a4ece1a7-18ce-3a63-9fea-f78b603ec418 | -9.49178 | -64.36083 | 2026-10-08 05:44:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4796499a-de47-30b9-a74e-834e99821be0 | -8.07889 | -55.29572 | 2026-10-08 05:44:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 62602d9a-c284-3690-828a-f89a9b9c78a0 | -10.62006 | -60.48452 | 2026-10-08 05:44:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 78734e2a-73e9-3ca4-9434-c1b829168a17 | -8.33986 | -62.84989 | 2026-10-08 05:44:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 541102bc-b61b-36d1-9008-b1fbce9a19b2 | -9.58517 | -65.24888 | 2026-10-08 05:44:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ba52811b-daa5-34e5-bd3c-8957ee832b14 | -8.76069 | -66.92178 | 2026-10-08 05:44:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 361dfb81-7da3-3fbb-a16c-1842a5b3dfbd | -10.36129 | -56.44085 | 2026-10-08 05:44:00 | NOAA-20 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 8d82450a-9d32-3cdd-a187-082127c8dffd | -9.20452 | -66.09218 | 2026-10-08 05:44:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 435b83c4-37b3-3610-81ff-58a5763d78b9 | -7.89533 | -63.71373 | 2026-10-08 05:44:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 9d67d139-50f0-3297-a7a7-11ef14370661 | -11.75347 | -61.05609 | 2026-10-08 05:44:00 | NOAA-20 | PIMENTA BUENO | RONDÔNIA | Brasil | 1100189 | 11 | 33 | nan | nan | nan | Amazônia | 2.4 |
| c03df34d-774d-30c8-9b9d-97d0871ba64e | -9.05087 | -65.93284 | 2026-10-08 05:44:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 8933bbe4-72cd-3386-9ea4-de46e18a3354 | -9.44584 | -65.43965 | 2026-10-08 05:44:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.4 |
| ea4d7320-760b-31cd-839a-e7a0a6b851a1 | -8.59286 | -67.30557 | 2026-10-08 05:44:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 89e1627b-e156-3888-9ea6-5296755deb00 | -9.49619 | -64.3544 | 2026-10-08 05:44:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 134c5f94-ea6b-3fe5-94a3-9d180171c349 | -8.65004 | -67.17612 | 2026-10-08 05:44:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 11.8 |
| b1a3f96a-5998-3647-842a-0403d974fd8e | -11.75219 | -61.06294 | 2026-10-08 05:44:00 | NOAA-20 | PIMENTA BUENO | RONDÔNIA | Brasil | 1100189 | 11 | 33 | nan | nan | nan | Amazônia | 2.7 |
| c1637d25-0485-38e5-965c-9ed4c3b713b9 | -8.53325 | -66.98283 | 2026-10-08 05:44:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 64860539-2bdf-3b58-a9c2-03ea02129510 | -8.75938 | -67.70604 | 2026-10-08 05:44:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6d5da56c-cdd8-3df2-92cd-ddd29eb41565 | -8.60082 | -63.06788 | 2026-10-08 05:44:00 | NOAA-20 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 63c5fdd2-901b-37d2-92f3-96e6e791737a | -9.58866 | -66.12823 | 2026-10-08 05:44:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 3fc182fb-d695-32bc-8173-554692e5f51b | -10.49335 | -67.88389 | 2026-10-08 05:44:00 | NOAA-20 | CAPIXABA | ACRE | Brasil | 1200179 | 12 | 33 | nan | nan | nan | Amazônia | 0.5 |
| af98da2c-039d-34f5-80a1-7ca3e7fafba4 | -8.59077 | -66.9878 | 2026-10-08 05:44:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 39fac81a-9de7-3361-8525-dcf5364e420f | -8.07845 | -55.29896 | 2026-10-08 05:44:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c0ff26e8-1ced-3faa-948d-74853b6c48e9 | -8.07273 | -55.30149 | 2026-10-08 05:44:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 329b01dc-ba0b-3580-a942-34c3eccd1b11 | -9.20173 | -66.08798 | 2026-10-08 05:44:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a5605db5-317f-34da-b172-975aa5d191f2 | -8.61299 | -67.02813 | 2026-10-08 05:44:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 43b72285-8edf-3239-93cc-ebf15c9add37 | -9.08007 | -67.38173 | 2026-10-08 05:44:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a7acdb1b-5547-34dc-8553-29b1b61d475c | -8.62704 | -67.0305 | 2026-10-08 05:44:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 17.6 |
| e08b4ed5-2a4d-331e-861a-103bd80acedf | -9.09922 | -65.35423 | 2026-10-08 05:44:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 138b8863-079e-3c45-985c-0481ebc8a105 | -10.85571 | -59.11359 | 2026-10-08 05:44:00 | NOAA-20 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0b503390-7e25-3e2c-b02f-1ad054811e89 | -8.9591 | -65.94382 | 2026-10-08 05:44:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 5bbd63b6-0445-3d9f-86e0-674582a7ed79 | -8.59565 | -67.04559 | 2026-10-08 05:44:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b1aac460-c5ef-3968-a5f5-3b2681c35ebf | -9.37335 | -55.9738 | 2026-10-08 05:44:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 1b0e3893-8269-3897-a4a4-cb40330f5dda | -8.96247 | -65.94437 | 2026-10-08 05:44:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 57da447b-486a-35d3-b5c1-d63fc78e93b9 | -9.49837 | -66.71991 | 2026-10-08 05:44:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 209db83e-c391-39fd-ac33-7f205ea38aab | -7.45461 | -63.55849 | 2026-10-08 05:44:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 2d0daafe-e276-371c-83f6-7dc3da5e0e31 | -9.47743 | -64.36568 | 2026-10-08 05:44:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| bebc0dcf-236e-3c1d-a70f-9c78c53daf97 | -9.08389 | -59.47986 | 2026-10-08 05:44:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 77569e1e-1be0-3ead-a5de-5c172e65caf1 | -8.08682 | -55.3164 | 2026-10-08 05:44:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3f50b8dc-160c-3cfe-9d45-f4ae02cb726f | -8.54774 | -67.0294 | 2026-10-08 05:44:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 83b8d39c-dca0-3066-98af-19aa1a066172 | -8.06263 | -55.29674 | 2026-10-08 05:44:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| eb6eaa48-7d0f-36c3-b2d3-a942dae9a117 | -9.11587 | -65.35695 | 2026-10-08 05:44:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| cb5cb0d4-054e-34c4-bdee-aa9589eb2144 | -8.06789 | -55.29754 | 2026-10-08 05:44:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |


[Clique aqui para ver as próximas entradas](README200.md)
