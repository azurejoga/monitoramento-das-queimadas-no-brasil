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

## Dados Diários - Página 97

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 8229b98e-28c6-31a5-997a-89076cb3c1ef | -9.56479 | -66.05533 | 2026-09-21 05:42:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 85732579-20fa-3054-b4c8-aa9518e22683 | -9.11771 | -60.94761 | 2026-09-21 05:42:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 517091d1-9297-32bd-9211-075686c3e1e1 | -6.73931 | -59.41883 | 2026-09-21 05:42:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 23aa66e5-cfc6-39e8-9360-ead5fb6a9204 | -10.37963 | -48.90623 | 2026-09-21 05:42:00 | NPP-375D | PUGMIL | TOCANTINS | Brasil | 1718451 | 17 | 33 | nan | nan | nan | Cerrado | 6.0 |
| e528088f-613d-32c2-b915-b3aad470a46b | -10.21096 | -53.91572 | 2026-09-21 05:42:00 | NPP-375D | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5798414f-0456-3ccd-a34f-4886d3f5dde1 | -9.70939 | -65.08819 | 2026-09-21 05:42:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3a60833b-4eba-31f7-9094-bc4f8d710575 | -5.84149 | -53.51706 | 2026-09-21 05:42:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0bfe6dac-f3d9-3262-9ef3-e6809f798255 | -5.38432 | -55.90144 | 2026-09-21 05:42:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 59cee803-0299-336c-be50-bc3f0a6f3cad | -11.35497 | -51.43045 | 2026-09-21 05:42:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f3d8b89d-9d5b-3da1-af3d-b3903373306d | -9.55005 | -66.00936 | 2026-09-21 05:42:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 3d681084-df23-3a4b-93fd-54b6f3615b97 | -8.24681 | -61.36775 | 2026-09-21 05:42:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 776e1f10-8716-3fe4-99ef-7bf16f941b43 | -7.32384 | -55.21358 | 2026-09-21 05:42:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 7f0c83d7-9826-3100-b8a8-0d793c3b3586 | -7.24842 | -55.60674 | 2026-09-21 05:42:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 02ca205e-c379-3b3f-a87d-1ee38e0ddcf4 | -6.45083 | -59.96864 | 2026-09-21 05:42:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 3.4 |
| ac21242b-b17a-35dd-b856-c3e2d3f3cafd | -6.44678 | -59.9719 | 2026-09-21 05:42:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 3.4 |
| e71c5e44-11db-30c1-94a4-01eb655107de | -10.41922 | -51.86846 | 2026-09-21 05:42:00 | NPP-375D | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 14.2 |
| b3b866a1-faa5-3ed1-bb71-fb4862d0de86 | -6.9915 | -61.3481 | 2026-09-21 05:42:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 3.7 |
| f5563b8a-a1cb-3631-bafd-8a7b4035243e | -10.81111 | -50.77012 | 2026-09-21 05:42:00 | NPP-375D | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 2aebc7af-aa63-3bbd-9150-846d57285389 | -8.18309 | -54.77298 | 2026-09-21 05:42:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 883ced6e-634f-30a1-b19a-30101cb949de | -10.96486 | -57.19571 | 2026-09-21 05:42:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 6d6fb5d4-1c7e-31e4-bf98-4b9b672030da | -9.18423 | -60.76583 | 2026-09-21 05:42:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e437f64c-dc07-37e9-bc3f-2cfcd5901507 | -9.28387 | -60.6366 | 2026-09-21 05:42:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 07889294-b7a3-3d3c-ab79-3da96426727a | -6.73316 | -55.0966 | 2026-09-21 05:42:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 1fb28819-b288-3cbd-9fc5-be42529afff7 | -6.1192 | -57.75594 | 2026-09-21 05:42:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 107d285b-784e-30e8-a7af-e5e1f0c03dfb | -6.9642 | -71.76235 | 2026-09-21 05:42:00 | NPP-375D | IPIXUNA | AMAZONAS | Brasil | 1301803 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ff0581fa-2ec3-3b78-91e2-1e7fe962f800 | -7.5736 | -57.66093 | 2026-09-21 05:42:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 11ed2ed1-7444-363d-9ec8-c758ebc0166d | -10.09237 | -50.2536 | 2026-09-21 05:42:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 43497618-20f6-35af-89bc-afa27ca59592 | -7.32848 | -55.21442 | 2026-09-21 05:42:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 5357e633-3649-394a-a03a-28769dfc3bb7 | -9.68033 | -54.33495 | 2026-09-21 05:42:00 | NPP-375D | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 9531a3ed-fa4b-3f7e-94b2-bf1f59d04b2e | -8.87593 | -64.24197 | 2026-09-21 05:42:00 | NPP-375D | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| dcba66ef-7d0f-34e0-9948-1e0bcd959164 | -11.10669 | -54.01469 | 2026-09-21 05:42:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| bb70bcfb-aac2-3f25-ad2d-4e3a4c362dc4 | -8.79866 | -60.80005 | 2026-09-21 05:42:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a96cbce3-080c-3795-b429-35a7028f2972 | -6.07546 | -57.62467 | 2026-09-21 05:42:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 3c8affeb-432d-3e2f-ae77-80e40e61c2b1 | -10.58259 | -57.48129 | 2026-09-21 05:42:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 29f4692a-ea62-3f49-8a4e-39e4f99d3768 | -10.47552 | -50.27352 | 2026-09-21 05:42:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 5.7 |
| dd371c8b-d77a-33e4-87c2-b64f2080fd41 | -9.03025 | -60.3593 | 2026-09-21 05:42:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7c2c7102-3162-36aa-8d84-a38c497dcc85 | -6.30577 | -60.01382 | 2026-09-21 05:42:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 67256871-807d-3d5f-963d-4e58167cd0ed | -6.28885 | -57.74528 | 2026-09-21 05:42:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 446f7168-2775-3fc1-8de9-843882bf61d9 | -6.73187 | -55.07181 | 2026-09-21 05:42:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| bf4f9e99-b7bd-39e5-97ea-2f68903c95db | -9.54876 | -66.0395 | 2026-09-21 05:42:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.5 |
| f36abcc4-e66a-3ce8-a1cd-49b3f9cdfec9 | -5.83975 | -53.52914 | 2026-09-21 05:42:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 31845d9e-a873-331d-89ae-875bb5781533 | -9.67914 | -54.34375 | 2026-09-21 05:42:00 | NPP-375D | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 9da2c685-49f2-368a-91ff-e0bc901ec559 | -5.76169 | -57.58646 | 2026-09-21 05:42:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| a2a47033-325f-32d0-bc7d-a045ec298c95 | -5.37064 | -56.05183 | 2026-09-21 05:42:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8f3b4a9f-7192-3d5b-9189-a52cf0f0c859 | -5.97504 | -52.19678 | 2026-09-21 05:42:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 221e911d-f087-3a57-bdc1-149628147330 | -7.33319 | -55.21487 | 2026-09-21 05:42:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 6e6e0b28-8a16-36a2-9d59-a1f12073c31e | -10.90417 | -53.97878 | 2026-09-21 05:42:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 886ac53c-86f7-3381-84ca-11a3be932ec4 | -11.02648 | -54.14328 | 2026-09-21 05:42:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| be323c94-bbe7-37da-9873-ded4379ecc70 | -6.23022 | -55.93429 | 2026-09-21 05:42:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 44ca8f13-ae6b-37ae-9a31-0822b24a4e4f | -8.92152 | -50.83992 | 2026-09-21 05:42:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 669178d8-654a-3aea-bdd8-3472a1dafc8d | -5.87632 | -53.63612 | 2026-09-21 05:42:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| e6e3ae64-190e-31a5-9637-dbf670777b65 | -8.90467 | -62.34401 | 2026-09-21 05:42:00 | NPP-375D | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 80e71c5d-7f10-3f2b-b6af-a0be49d1e48e | -10.22916 | -57.82682 | 2026-09-21 05:42:00 | NPP-375D | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| cabd0a9d-8dd8-388b-8300-261c3dd770e9 | -10.96376 | -57.20375 | 2026-09-21 05:42:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 43908655-8f0c-3df7-8af7-162c8dd8f894 | -9.73815 | -54.81127 | 2026-09-21 05:42:00 | NPP-375D | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| b71e88c3-51b4-3d84-948a-87046e8acb94 | -9.56256 | -66.04625 | 2026-09-21 05:42:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 303ce165-2e9a-3847-bb8c-641d79f503cf | -5.26098 | -55.92101 | 2026-09-21 05:42:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 6b733329-6fd5-3763-a673-4b76129c90b4 | -10.79074 | -50.77324 | 2026-09-21 05:42:00 | NPP-375D | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 4.4 |
| e9eabfff-83fd-3088-a8a3-72a4b2aa2780 | -5.86697 | -60.16225 | 2026-09-21 05:42:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 63a90d30-0671-3e18-b40a-238fab088212 | -5.85176 | -53.51851 | 2026-09-21 05:42:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| cc6bb3a0-4398-3e01-83bf-6fc003467e37 | -6.73383 | -55.09186 | 2026-09-21 05:42:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 242c68c9-1338-3b14-b2f9-253ed81fd0fc | -7.11556 | -48.4382 | 2026-09-21 05:42:00 | NPP-375D | CARMOLÂNDIA | TOCANTINS | Brasil | 1703883 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 17720164-e3be-3d94-84c2-4450f850d860 | -10.82873 | -50.78931 | 2026-09-21 05:42:00 | NPP-375D | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 4.3 |
| fc81b252-21e5-32d6-a391-777e4c9b0d27 | -5.73243 | -53.45716 | 2026-09-21 05:42:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f13e4e0f-e7f9-3308-89fc-578db120de19 | -6.13226 | -59.957 | 2026-09-21 05:42:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 579ffd4d-caa8-305d-80b0-771092970136 | -5.82226 | -53.50487 | 2026-09-21 05:42:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 47960da9-95e5-3924-8338-9d306dd75437 | -5.203 | -56.07663 | 2026-09-21 05:42:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6d07a2a4-7a64-359a-9252-e697b65a83b4 | -10.81768 | -50.77096 | 2026-09-21 05:42:00 | NPP-375D | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 3f02558b-f420-3862-a452-8a0e8129fea2 | -6.10896 | -55.66813 | 2026-09-21 05:42:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 789bea39-d8b3-3b8f-a373-f69fba873d7d | -11.12405 | -54.00695 | 2026-09-21 05:42:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| ab2694fd-7fc5-3c45-a150-483930460f80 | -10.8836 | -54.09523 | 2026-09-21 05:42:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| c35719f3-05c6-3cd7-95a3-b74890feb4cf | -6.37822 | -60.01668 | 2026-09-21 05:42:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| beaac72b-7ff9-3a03-93e0-fee4a958a0cd | -6.12532 | -59.95596 | 2026-09-21 05:42:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 73b29f69-40bb-3eb5-b317-1843c77a26ae | -8.24288 | -61.37082 | 2026-09-21 05:42:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 83658dbd-df1b-3dc1-96c3-ad4b7e339135 | -8.07923 | -55.33875 | 2026-09-21 05:42:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| aa24d7c8-778e-3069-b81c-a9fd5555e9eb | -6.30585 | -57.73795 | 2026-09-21 05:42:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| ef9e6910-f810-3cbf-bba7-3b8dc164c2e8 | -8.16668 | -54.764 | 2026-09-21 05:42:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 0e7ccb6d-9797-3c71-85a4-c8b12f9e5ff1 | -10.70258 | -54.17091 | 2026-09-21 05:42:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 359803a4-2324-32aa-b6d0-d1f4983f7897 | -10.85148 | -50.1567 | 2026-09-21 05:42:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 5fe4e2b8-51f7-3336-b1fd-85e54603b651 | -8.85773 | -68.50992 | 2026-09-21 05:42:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 19ba51b6-551c-3916-966e-1b91290932fc | -11.35804 | -51.42674 | 2026-09-21 05:42:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 8eae8875-3405-3cc4-aa82-5bd375a08b73 | -9.03196 | -61.66188 | 2026-09-21 05:42:00 | NPP-375D | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4aaca84e-6589-3e95-878d-eeaf007569b8 | -5.85875 | -57.55283 | 2026-09-21 05:42:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 28e6e2d5-9d37-3826-968c-d5d5ef633b9c | -6.69566 | -60.01302 | 2026-09-21 05:42:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 23e3e45e-9f61-3921-aa68-fc2e605b54ec | -6.24497 | -53.30879 | 2026-09-21 05:42:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 65bc2a05-c762-3f6f-a5f2-b1c7902fb899 | -10.69824 | -50.76715 | 2026-09-21 05:42:00 | NPP-375D | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 3fe66ab1-3824-362c-b22d-30da2f1e0fac | -7.32453 | -55.2088 | 2026-09-21 05:42:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 5bfd9412-09f9-35d0-93ec-b287dfb14102 | -10.76047 | -50.80333 | 2026-09-21 05:42:00 | NPP-375D | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 8acbf8b7-1f4e-3985-bea8-3bb3cf2398c2 | -11.04449 | -54.16206 | 2026-09-21 05:42:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| d2de97bf-0b46-3434-9d80-439a245a8c01 | -6.14237 | -55.71029 | 2026-09-21 05:42:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 82dd7b70-fbdd-38bf-8d9f-09af70606fa2 | -7.32228 | -55.61049 | 2026-09-21 05:42:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e61802d1-f976-3503-9ad9-715edbd5b79e | -6.43444 | -59.97483 | 2026-09-21 05:42:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a2c9307e-f689-3bf4-aa26-008efdf0dd84 | -6.83035 | -55.53138 | 2026-09-21 05:42:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 8.3 |
| 567b7c9a-75ba-3d20-adba-ea161c6fef5f | -6.12308 | -57.75652 | 2026-09-21 05:42:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 56a63f4c-75ab-3c4f-95f8-48a5b79ba134 | -10.86025 | -54.10876 | 2026-09-21 05:42:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 9e22ad26-6547-3b88-b0ac-06a42563047b | -10.22262 | -59.40164 | 2026-09-21 05:42:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 6e6a0028-9a8a-3c3a-93bb-a1e79d9bb3e7 | -5.8321 | -53.50942 | 2026-09-21 05:42:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2f07de88-2aa2-30b9-b2a7-09283131d975 | -7.58499 | -57.69395 | 2026-09-21 05:42:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 4e7ceab5-826c-3a4f-b7a8-93e530d3715d | -10.37876 | -48.91364 | 2026-09-21 05:42:00 | NPP-375D | PUGMIL | TOCANTINS | Brasil | 1718451 | 17 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 785a2288-0846-337e-9951-d7dfee81fc3d | -10.47192 | -50.27962 | 2026-09-21 05:42:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 5.0 |


[Clique aqui para ver as próximas entradas](README98.md)
