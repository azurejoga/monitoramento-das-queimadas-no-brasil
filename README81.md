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

## Dados Diários - Página 81

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| e23851d2-f927-3682-914d-882695151771 | -8.65881 | -70.02508 | 2026-09-17 06:22:00 | NOAA-21 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.8 |
| f62b0ec0-fc00-30a2-a2a4-7bb9fa6fca17 | -9.34592 | -65.93166 | 2026-09-17 06:22:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 3431ed84-84e4-3734-85eb-f6398acad5d2 | -7.79993 | -66.92089 | 2026-09-17 06:22:00 | NOAA-21 | PAUINI | AMAZONAS | Brasil | 1303502 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 04152eb9-f5c6-3222-a282-a3a0d21764e1 | -9.10968 | -65.93192 | 2026-09-17 06:22:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 3.8 |
| b1a2e7ca-bb1f-3205-8537-78d9cc0e795d | -8.37897 | -71.04673 | 2026-09-17 06:22:00 | NOAA-21 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 3bac4261-8a7b-3438-8320-f1e307859cb6 | -8.76227 | -66.56371 | 2026-09-17 06:22:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 65562a1f-6ca1-30e2-a4de-4b3a6f7bf4c6 | -9.05556 | -65.91669 | 2026-09-17 06:22:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b7de819d-96b2-3e60-96fb-c45367d78bc2 | -9.00352 | -69.40328 | 2026-09-17 06:22:00 | NOAA-21 | MANOEL URBANO | ACRE | Brasil | 1200344 | 12 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 02e2b286-3839-340e-b11c-2460c14e29d1 | -8.91736 | -62.40208 | 2026-09-17 06:22:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 5.3 |
| dce194e1-7f75-3d2c-8b25-235704398694 | -8.37511 | -71.04613 | 2026-09-17 06:22:00 | NOAA-21 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 3b3e1d5d-f5fb-3ec4-b859-a5fe359732ef | -9.10909 | -65.939 | 2026-09-17 06:22:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 6c38fcd7-47a1-3de0-8a5a-b015c62ff903 | -9.10266 | -65.94552 | 2026-09-17 06:22:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| da2edbf0-cb87-3811-ba3b-e83fc4412519 | -9.10773 | -65.94978 | 2026-09-17 06:22:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 832784b4-73e0-3f7f-8e70-c37a74874f03 | -9.4816 | -65.65513 | 2026-09-17 06:22:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6014e4af-e2d0-3662-b1a1-51ddc5026610 | -9.10222 | -65.94905 | 2026-09-17 06:22:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a35da3fb-57b0-3977-b136-ac8274c9a641 | -8.64265 | -66.57864 | 2026-09-17 06:22:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 3.0 |
| fc5f4a58-bb8d-3d42-bcf5-d1c384c688cc | -7.61166 | -67.25175 | 2026-09-17 06:22:00 | NOAA-21 | PAUINI | AMAZONAS | Brasil | 1303502 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 7c2a3729-733d-36bf-a723-ba699d6e1810 | -8.88224 | -62.39597 | 2026-09-17 06:22:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 87f6f053-6671-34c5-9006-70df91bda6d0 | -9.42161 | -65.9083 | 2026-09-17 06:22:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 22405126-7b92-3a1d-bbc8-0d1f25290141 | -8.6514 | -66.59318 | 2026-09-17 06:22:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 9b64d0aa-10b7-3dfe-8c27-a7f40af97f39 | -9.1834 | -66.01816 | 2026-09-17 06:22:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| f1e13579-6cd7-30e3-8df4-2384f11b16cd | -7.80033 | -66.91792 | 2026-09-17 06:22:00 | NOAA-21 | PAUINI | AMAZONAS | Brasil | 1303502 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3a794abd-b627-3193-ba12-b98dbe5c7fa4 | -9.10871 | -65.93915 | 2026-09-17 06:22:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 400000a3-343b-35ab-b43d-29a4cfc66957 | -9.11506 | -65.93606 | 2026-09-17 06:22:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 68d060ce-6d87-33b5-8bdc-6b88ba124d75 | -8.64222 | -66.58189 | 2026-09-17 06:22:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 5.0 |
| e4dcd901-602b-32f8-ad98-c00b294f1bc5 | -8.56326 | -71.45158 | 2026-09-17 06:22:00 | NOAA-21 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7c5a7921-aea8-3dab-8083-7bd080f0e634 | -9.34637 | -65.92813 | 2026-09-17 06:22:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| b7d5d099-d135-3c8c-803d-970a84ac0964 | -8.80324 | -71.29523 | 2026-09-17 06:22:00 | NOAA-21 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 7a9416f3-b5c2-378c-8d75-f87553fc6aad | -9.06107 | -65.91753 | 2026-09-17 06:22:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 2aa99a3b-cefd-3676-af47-d8307eaff907 | -10.29995 | -68.8566 | 2026-09-17 06:22:00 | NOAA-21 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 52ffe07a-8c92-3421-b907-e31f3ffe1d57 | -9.16794 | -66.04642 | 2026-09-17 06:22:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 4efbeadf-fe4d-3cfe-856c-a605a0dd5e30 | -9.06155 | -65.91383 | 2026-09-17 06:22:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c8567891-0b82-3bd9-9dc5-7782445509bb | -9.10224 | -65.94567 | 2026-09-17 06:22:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b70595cc-7bf3-3dd4-9b65-6d5fda0d8118 | -7.60241 | -67.31829 | 2026-09-17 06:22:00 | NOAA-21 | PAUINI | AMAZONAS | Brasil | 1303502 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 091c0316-6cfe-3e54-96bf-a38db719c230 | -8.56329 | -71.45337 | 2026-09-17 06:22:00 | NOAA-21 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 55f3c4d6-c159-3c2e-b71f-8e4f2c448c90 | -9.10177 | -65.9492 | 2026-09-17 06:22:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e301810d-1247-3d4a-8233-97a1d8c72a7f | -9.11 | -65.93177 | 2026-09-17 06:22:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 9efaabe6-f613-3819-b2b1-7c284dba54c7 | -7.60732 | -67.319 | 2026-09-17 06:22:00 | NOAA-21 | PAUINI | AMAZONAS | Brasil | 1303502 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 8d7a75c7-d3dd-3736-a710-b43f9d93c97f | -9.1734 | -66.04726 | 2026-09-17 06:22:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8eb8bc49-0720-30d9-b72c-427497b33dae | -7.79527 | -66.91718 | 2026-09-17 06:22:00 | NOAA-21 | PAUINI | AMAZONAS | Brasil | 1303502 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1d3292c0-7ca4-38ab-85b0-cf76b20f2ce9 | -8.88385 | -62.39086 | 2026-09-17 06:22:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 72f8839f-321c-373a-bb87-74734c7ad4dd | -18.0303 | -50.9385 | 2026-09-17 06:30:00 | GOES-19 | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 194.1 |
| 8ffe40ae-bd45-30b9-b00c-505a6e746e55 | -18.0298 | -50.9606 | 2026-09-17 06:30:00 | GOES-19 | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 171.6 |
| 22ffface-a442-328b-8ecb-27e89e44c87f | -11.8069 | -58.1759 | 2026-09-17 06:30:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 93.1 |
| 1def8313-f871-37c9-8ea7-d0c4ee3c9cab | -11.8069 | -58.1759 | 2026-09-17 06:40:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 76.7 |
| 0804a140-46e7-384f-9a00-f8bd3f1b2ac5 | -18.0303 | -50.9385 | 2026-09-17 06:40:00 | GOES-19 | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 130.6 |
| 8dfb3dd5-1a67-3b33-9223-1016b41a6b38 | -18.0298 | -50.9606 | 2026-09-17 06:40:00 | GOES-19 | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 87.3 |
| 12736e2a-9c5c-3616-84c1-955e3b7b116d | -12.493 | -50.6972 | 2026-09-17 06:40:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 62.5 |
| 451537b4-d9e5-3460-8024-eea14bd4c896 | -18.0502 | -50.935 | 2026-09-17 06:40:00 | GOES-19 | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 55.4 |
| 12176c0e-8872-3743-90a5-f6b4380d95e5 | -12.4738 | -50.6995 | 2026-09-17 06:40:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 79.4 |
| e42ce44d-fb0a-3720-bc48-d016860d1303 | -11.8069 | -58.1759 | 2026-09-17 06:50:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 76.4 |
| c30643fb-5d9a-39c8-9b2f-b1d66d2b35c1 | -18.0303 | -50.9385 | 2026-09-17 06:50:00 | GOES-19 | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 75.8 |
| f156a91c-2a85-3883-8e96-135add225c0a | -18.0298 | -50.9606 | 2026-09-17 06:50:00 | GOES-19 | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 57.5 |
| 93c2f4c5-013f-37d8-a80a-c4603f4e803f | -12.493 | -50.6972 | 2026-09-17 07:00:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 52.3 |
| 2911d282-8ec3-3852-b401-63cdf69c556b | -11.8069 | -58.1759 | 2026-09-17 07:00:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 53.3 |
| f5f8c58f-881a-3345-b022-b43481b23648 | -11.8069 | -58.1759 | 2026-09-17 07:10:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 47.4 |
| 60cd8986-14ba-3e7a-a8f2-6254dbe1adaf | -12.493 | -50.6972 | 2026-09-17 07:10:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 79.1 |
| 4b8b6837-e2a8-35a5-8bc6-bbf91ab0fb29 | -12.37 | -50.87 | 2026-09-17 07:15:00 | MSG-03 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| c50c5044-1e4f-3ea1-9ec1-d14d5db16911 | -12.36 | -50.76 | 2026-09-17 07:15:00 | MSG-03 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| e26055e2-865f-3891-b5c3-490a45c31e37 | -12.4 | -50.82 | 2026-09-17 07:15:00 | MSG-03 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 87021d2a-1b79-38f8-99d0-34d6456afbf8 | -12.37 | -50.81 | 2026-09-17 07:15:00 | MSG-03 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 20d6751c-9f43-311f-a2db-d646163d3887 | -12.4 | -50.88 | 2026-09-17 07:15:00 | MSG-03 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 3839e125-48a1-3833-a8b1-a1deba2f4d58 | -12.5118 | -50.7164 | 2026-09-17 07:20:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 88.6 |
| ee9a98d7-3abb-32df-b001-83ab3306360c | -12.4738 | -50.6995 | 2026-09-17 07:20:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 107.2 |
| 51ed8512-dab4-3b18-ba3b-55a015689a28 | -12.5121 | -50.6949 | 2026-09-17 07:20:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 100.3 |
| e480c886-d54e-31f7-81d5-32f79ab223bf | -12.493 | -50.6972 | 2026-09-17 07:20:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 121.6 |
| 4d96a516-7907-390c-9c2e-90933f3b5fa6 | -12.4738 | -50.6995 | 2026-09-17 07:30:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 79.7 |
| 485bb43a-afb1-326d-a006-2ddd01dba630 | -12.493 | -50.6972 | 2026-09-17 07:30:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 119.9 |
| 5496a7f1-ac18-3981-b798-f940885b83d3 | -3.47326 | -54.69805 | 2026-09-17 07:44:00 | AQUA_M-M | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 20.7 |
| b4bd3a25-e437-385e-97ce-676c431fe2e6 | -1.03901 | -53.727 | 2026-09-17 07:44:00 | AQUA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 20.5 |
| e18ceb21-5ce7-34b9-9d44-6d7ac2339447 | -3.47495 | -54.7158 | 2026-09-17 07:44:00 | AQUA_M-M | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 20.2 |
| 305e87cf-76bf-3243-9f72-d28b96a8f565 | -3.47824 | -54.69329 | 2026-09-17 07:44:00 | AQUA_M-M | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 19.6 |
| 4b0afd78-15f5-32f9-8545-2aaf55640ff2 | -8.87605 | -62.3931 | 2026-09-17 07:46:00 | AQUA_M-M | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 9.4 |
| 1621ae09-33df-37bc-88af-233892743622 | -11.81283 | -58.16463 | 2026-09-17 07:46:00 | AQUA_M-M | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 22.4 |
| cacc73b1-770c-3d4c-948f-67a39a15b10b | -9.28235 | -60.62521 | 2026-09-17 07:46:00 | AQUA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 10.7 |
| 87e1a9e5-f305-3af4-8704-0b30eee679ab | -11.80108 | -58.1632 | 2026-09-17 07:46:00 | AQUA_M-M | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 14.4 |
| 11d2d70a-79fc-3405-9940-94bdc914e819 | -6.93154 | -63.02232 | 2026-09-17 07:46:00 | AQUA_M-M | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 215aad9d-f1f4-37ad-8a52-ba47c16b7d7c | -9.09633 | -60.96654 | 2026-09-17 07:46:00 | AQUA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 48ac303e-1125-362e-8393-9e0c7873c806 | -5.1491 | -55.93816 | 2026-09-17 07:46:00 | AQUA_M-M | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 17.1 |
| 8f2d2fa0-78a0-391e-a4d5-805a6f3c33e6 | -9.38784 | -60.29633 | 2026-09-17 07:46:00 | AQUA_M-M | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 7.3 |
| 37718425-b36a-3ee2-85b7-3da1342f2768 | -8.63784 | -66.57806 | 2026-09-17 07:46:00 | AQUA_M-M | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 6.7 |
| f4ff9f0b-11e5-31dc-9e55-66d820a0695c | -8.48804 | -57.63848 | 2026-09-17 07:46:00 | AQUA_M-M | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 11.1 |
| ecba2345-7f20-3899-b382-7ae94714b351 | -10.39404 | -58.30322 | 2026-09-17 07:46:00 | AQUA_M-M | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 11.4 |
| 01826fe5-b2a4-31a1-aae4-f73eeaaf5a32 | -6.3101 | -62.67053 | 2026-09-17 07:46:00 | AQUA_M-M | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 4.1 |
| caf1d1fe-4877-3264-9107-c6b9588b3c0b | -9.10908 | -65.93156 | 2026-09-17 07:46:00 | AQUA_M-M | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 749d92f3-06eb-3bbd-8c31-83ea0a1fddab | -9.09489 | -60.97639 | 2026-09-17 07:46:00 | AQUA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 7.6 |
| 79ac0d3b-aeb4-311a-bfa1-1aebb4fd3562 | -9.09777 | -60.95668 | 2026-09-17 07:46:00 | AQUA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 15.9 |
| 5eb9f510-aaa8-3707-ac4a-f559215b925d | -6.36009 | -58.28371 | 2026-09-17 07:46:00 | AQUA_M-M | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 6.4 |
| fb083a9a-37de-3a7c-8950-65ae2b564e79 | -9.28088 | -60.63549 | 2026-09-17 07:46:00 | AQUA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 943f2f14-6b84-35e0-816a-1781d775f147 | -9.4101 | -62.70946 | 2026-09-17 07:46:00 | AQUA_M-M | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 6.2 |
| c9e61973-140e-3446-92ef-90b8b39cc83c | -9.56387 | -66.24747 | 2026-09-17 07:46:00 | AQUA_M-M | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 2bcc1819-9ed2-37e8-928a-a98d6ce87631 | -9.10736 | -65.94255 | 2026-09-17 07:46:00 | AQUA_M-M | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 87e9fc01-28d9-34cb-aa28-6fb64ba5bda1 | -11.80893 | -58.16955 | 2026-09-17 07:46:00 | AQUA_M-M | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 46.2 |
| 9946e91f-e8cb-304d-9f3d-2033c80792d7 | -6.37069 | -58.28518 | 2026-09-17 07:46:00 | AQUA_M-M | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 11.2 |
| 4f439e1e-5d92-31e5-8a8c-03e1bd3259cd | -9.28381 | -60.61487 | 2026-09-17 07:46:00 | AQUA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 4b641bca-d9e5-33b2-9739-7e4b69222824 | -5.14726 | -55.93247 | 2026-09-17 07:46:00 | AQUA_M-M | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 16.1 |
| 7d5891e1-c785-37a4-8d09-8fea3c07ac28 | -9.8694 | -48.3814 | 2026-09-17 08:10:00 | GOES-19 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 54.6 |
| 495eba3e-5cf0-3b0c-bf40-2df6faacd333 | -12.37 | -50.87 | 2026-09-17 08:15:00 | MSG-03 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 5fa1a2e2-7987-3db7-8794-dd5d90d068a6 | -12.34 | -50.86 | 2026-09-17 08:15:00 | MSG-03 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| d86563c9-427d-3ec1-a2b9-362c7c6ec7d7 | -12.37 | -50.81 | 2026-09-17 08:15:00 | MSG-03 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | nan |


[Clique aqui para ver as próximas entradas](README82.md)
