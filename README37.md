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

## Dados Diários - Página 37

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 623aac8b-ed37-3b47-bc3d-613c730a3e96 | -8.69366 | -69.96579 | 2026-09-25 06:08:00 | NPP-375D | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.4 |
| dee8851a-c7e9-3adc-aa95-9d954db17f37 | -10.17247 | -67.18958 | 2026-09-25 06:08:00 | NPP-375D | PLÁCIDO DE CASTRO | ACRE | Brasil | 1200385 | 12 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 03faa72f-9fca-3851-b11f-a992f558b7df | -9.75991 | -66.11523 | 2026-09-25 06:08:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3a7ff5ed-3edd-3413-a3bb-96fe45985a80 | -9.02763 | -60.52002 | 2026-09-25 06:08:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 12acd611-9ea4-33d0-a0ad-5b0e72da0400 | -9.54854 | -65.98782 | 2026-09-25 06:08:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 51b01477-ac1a-3f13-8bc1-eccc5844745c | -10.98131 | -58.95676 | 2026-09-25 06:08:00 | NPP-375D | CASTANHEIRA | MATO GROSSO | Brasil | 5102850 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a980ce55-f5a3-30fa-b8dd-9435353e07f0 | -9.46631 | -67.0733 | 2026-09-25 06:08:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8d355741-7078-3b75-82fa-eb4b6c4e4acf | -9.02221 | -60.55946 | 2026-09-25 06:08:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d2219fa7-bb7a-3751-9f9a-f93154aa297f | -9.06671 | -65.6993 | 2026-09-25 06:08:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 5962070e-1dac-3cff-8ec0-7cf53ca68cbc | -8.31453 | -70.53894 | 2026-09-25 06:08:00 | NPP-375D | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 80e1378e-5174-3cbd-a67b-a3cb7eeaa0a4 | -10.56655 | -59.48513 | 2026-09-25 06:08:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1c0b73d6-d472-317f-929f-849bec0d3c0a | -8.0374 | -61.31573 | 2026-09-25 06:08:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 9af3f2b7-b654-3b2e-b0a7-53e6d1f933ba | -7.66678 | -67.07524 | 2026-09-25 06:08:00 | NPP-375D | PAUINI | AMAZONAS | Brasil | 1303502 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ccca42d6-af3c-3559-bbb5-929ab314969d | -9.93442 | -60.71841 | 2026-09-25 06:08:00 | NPP-375D | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a0ba8676-7dc7-3349-a490-be9754dee166 | -8.64192 | -66.8578 | 2026-09-25 06:08:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 7d0575cf-f97b-38a3-baab-f657b717fc63 | -6.95262 | -71.78797 | 2026-09-25 06:08:00 | NPP-375D | IPIXUNA | AMAZONAS | Brasil | 1301803 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 53e3f9fa-ee1b-3659-b8ef-79cff46d234c | -8.61658 | -70.03738 | 2026-09-25 06:08:00 | NPP-375D | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c5c55702-e805-3e79-8ebe-5aebe9794017 | -9.06815 | -65.69717 | 2026-09-25 06:08:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 83d780e0-65a1-3ddd-a7b8-8d0071293378 | -10.21828 | -59.40403 | 2026-09-25 06:08:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 12df1403-c18b-3803-b797-be0ed7472e87 | -8.26987 | -70.80993 | 2026-09-25 06:08:00 | NPP-375D | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 883c3322-3cec-37cf-95ce-817075fdef84 | -9.16387 | -67.67788 | 2026-09-25 06:08:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7cf332fe-88f5-3e33-a5e6-9ff4f62ff87a | -10.5683 | -69.32598 | 2026-09-25 06:08:00 | NPP-375D | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 95563a70-0d8c-373d-876c-2c14a4d15533 | -11.56516 | -61.24097 | 2026-09-25 06:08:00 | NPP-375D | PIMENTA BUENO | RONDÔNIA | Brasil | 1100189 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 109f6a78-070e-3604-8a18-7f805dfcbbaa | -9.52196 | -67.75502 | 2026-09-25 06:08:00 | NPP-375D | PORTO ACRE | ACRE | Brasil | 1200807 | 12 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 46bbe104-01f3-39f9-b596-1e88c76afe62 | -9.37974 | -66.50843 | 2026-09-25 06:08:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 501bf44c-9e55-3c0f-9713-a91f046d67e7 | -9.50208 | -64.75237 | 2026-09-25 06:08:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6a1e7785-ed13-3eac-9d3b-8cf86564452b | -9.14707 | -59.47613 | 2026-09-25 06:08:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 7d2e090e-e461-356b-ad2b-077a73127a6a | -8.91564 | -72.80737 | 2026-09-25 06:08:00 | NPP-375D | MARECHAL THAUMATURGO | ACRE | Brasil | 1200351 | 12 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e3395357-0d0f-3f75-909c-828c9d04be72 | -9.06607 | -65.70367 | 2026-09-25 06:08:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 37b6551b-187f-384b-af86-6f26e6e8b264 | -9.14802 | -59.46896 | 2026-09-25 06:08:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0b9a0a9a-3dd3-32d4-9910-e8bc9a09c71c | -10.14246 | -69.02721 | 2026-09-25 06:08:00 | NPP-375D | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 9f21b2ce-b0c7-37c0-8d19-d65484b87229 | -9.08525 | -61.43282 | 2026-09-25 06:08:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 08b17deb-d6dd-3411-bfe5-417085e00805 | -7.94384 | -63.49873 | 2026-09-25 06:08:00 | NPP-375D | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| cbfe6944-17c5-3409-b65b-03f796b8abfe | -7.94025 | -63.49442 | 2026-09-25 06:08:00 | NPP-375D | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c9d906a0-a8da-36ee-812e-cd101b311593 | -10.44873 | -69.29624 | 2026-09-25 06:08:00 | NPP-375D | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 6a990d99-e64b-3b5c-96ef-7f7cff6fec16 | -7.58449 | -69.89332 | 2026-09-25 06:08:00 | NPP-375D | ENVIRA | AMAZONAS | Brasil | 1301506 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| c0a8a3c3-a6c1-3dff-a336-6108989df381 | -7.25441 | -72.41214 | 2026-09-25 06:08:00 | NPP-375D | GUAJARÁ | AMAZONAS | Brasil | 1301654 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2bd331b0-9425-3618-86c8-ca16300e0062 | -8.32612 | -72.84398 | 2026-09-25 06:08:00 | NPP-375D | PORTO WALTER | ACRE | Brasil | 1200393 | 12 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 8c3f6e9f-5b5a-3bee-9fd9-3bdb88c336a4 | -8.63787 | -66.86108 | 2026-09-25 06:08:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 4fd38e2b-9679-3fa5-8397-0df697fe14b8 | -9.57375 | -66.48659 | 2026-09-25 06:08:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 9031d3db-1ac5-36c8-bfe4-6501ab38836d | -8.26828 | -70.80663 | 2026-09-25 06:08:00 | NPP-375D | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 11ea69aa-1d0b-3ca1-a661-7aaa33f58a26 | -12.14775 | -61.17123 | 2026-09-25 06:08:00 | NPP-375D | PIMENTA BUENO | RONDÔNIA | Brasil | 1100189 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 079cc5fd-ebaa-3029-a818-eca6248a30ae | -9.0229 | -60.51637 | 2026-09-25 06:08:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 17d54c3e-6ad0-38c2-bc30-b2a69d0e7fc2 | -7.73059 | -66.9101 | 2026-09-25 06:08:00 | NPP-375D | PAUINI | AMAZONAS | Brasil | 1303502 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c4f17b78-a6e0-3478-bdf7-211588df6221 | -7.58785 | -69.89387 | 2026-09-25 06:08:00 | NPP-375D | ENVIRA | AMAZONAS | Brasil | 1301506 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 43e73776-2193-3ae5-a5ed-9bd80c0c2616 | -8.26544 | -70.80231 | 2026-09-25 06:08:00 | NPP-375D | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 182a8f63-51f6-31d8-8712-c865fafb6501 | -9.5872 | -60.5216 | 2026-09-25 06:08:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| caf44556-0fb4-32ca-95c0-689549d77fce | -10.56367 | -59.48307 | 2026-09-25 06:08:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d46203e0-cf64-3d98-81d1-06818c660708 | -8.38817 | -71.0737 | 2026-09-25 06:08:00 | NPP-375D | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ffc75e08-26eb-38fc-abe3-f019f070325c | -8.26643 | -70.80936 | 2026-09-25 06:08:00 | NPP-375D | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 39685f9f-772b-37d1-b82f-781716f83268 | -9.37908 | -66.50704 | 2026-09-25 06:08:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4b226524-105f-3017-bac1-b9ac1287fe4e | -9.15811 | -59.4777 | 2026-09-25 06:08:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 6ed53884-416c-3754-9f7d-cfa55beb1548 | -8.26705 | -70.80562 | 2026-09-25 06:08:00 | NPP-375D | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d7b817df-9072-3040-b51a-55cca2b0fc6e | -9.76083 | -66.1144 | 2026-09-25 06:08:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8f93415d-4e0b-37c1-8a2f-9f0d6a70be4e | -9.67259 | -66.83179 | 2026-09-25 06:08:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6dec27ba-4112-36e5-a6e1-bfb1e0448cd7 | -9.08379 | -61.44345 | 2026-09-25 06:08:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 05ce6fa0-1702-3535-8c5c-3589f67d18ab | -10.14626 | -68.80779 | 2026-09-25 06:08:00 | NPP-375D | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 9b8e8f15-9007-3ee5-8bc6-16a2d8b0b1b4 | -8.90001 | -71.34079 | 2026-09-25 06:08:00 | NPP-375D | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0942c215-c807-308d-bf71-f7cc36f3e727 | -9.38035 | -66.50443 | 2026-09-25 06:08:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 169870fe-b7a8-30b4-b5a0-a17be305a794 | -9.15354 | -59.46977 | 2026-09-25 06:08:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| d365dc1f-a0b4-3da7-aa3c-cd2a8a66d585 | -8.78231 | -66.59854 | 2026-09-25 06:08:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f152a4c5-7f4b-3623-8ebd-f94d7e761135 | -9.15306 | -59.47337 | 2026-09-25 06:08:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 3719cad7-01ca-3694-8528-416b48928b42 | -9.14754 | -59.47257 | 2026-09-25 06:08:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| affee4ba-b240-3415-b031-c57126ba1b63 | -9.02263 | -60.55644 | 2026-09-25 06:08:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ca9f69f5-028b-3612-adc3-6351389ced54 | -10.5632 | -59.48688 | 2026-09-25 06:08:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5c242b11-fc7b-36ba-a9bf-d1fbb775c0aa | -9.38615 | -66.50816 | 2026-09-25 06:08:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 65f9c179-5b3e-3c19-bedc-15874bef2002 | -8.38754 | -71.0775 | 2026-09-25 06:08:00 | NPP-375D | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ea6a47a6-6d22-31ff-8b16-3b5502f4ad7a | -9.16034 | -59.41872 | 2026-09-25 06:08:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 1b3ae0ea-e12b-3880-a53a-04bf1b287ccc | -9.55581 | -65.9889 | 2026-09-25 06:08:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 2eff91d5-bf73-3017-ac7f-3de88982a3a4 | -9.23856 | -65.74958 | 2026-09-25 06:08:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 42e360af-a931-3c2b-9080-93e43e3c5494 | -9.21185 | -60.46239 | 2026-09-25 06:08:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c49c3840-b1e7-33c1-a4ea-01b064a72c56 | -8.63846 | -66.85728 | 2026-09-25 06:08:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 37ef60d4-f913-3b66-8ea0-d937c7426d13 | -9.2998 | -62.30568 | 2026-09-25 06:08:00 | NPP-375D | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 1a36ec52-d09a-32a6-8694-51f0ae38658e | -9.93483 | -60.71534 | 2026-09-25 06:08:00 | NPP-375D | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 73e4652a-08dd-36db-be7c-742106d1546f | -9.55218 | -65.98836 | 2026-09-25 06:08:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 6ab6074b-88d2-3343-8a49-778356c059c5 | -8.84182 | -70.86355 | 2026-09-25 06:08:00 | NPP-375D | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 0.7 |
| b9165ef1-be89-3e20-8ee2-76374cc42b94 | -7.67034 | -67.14292 | 2026-09-25 06:08:00 | NPP-375D | PAUINI | AMAZONAS | Brasil | 1303502 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| cf20218d-fdd2-314b-8ea4-4e7f5d14f8c2 | -9.20751 | -60.45546 | 2026-09-25 06:08:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| bacb9469-4c9d-36bb-b087-6790d7be8de8 | -9.54918 | -65.9836 | 2026-09-25 06:08:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 028d0fc7-dd2f-30b5-9db7-b473b424c1ef | -8.58101 | -69.9514 | 2026-09-25 06:08:00 | NPP-375D | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 0.5 |
| f310549d-ea5f-3dff-b009-7a7afd369149 | -10.95155 | -58.96399 | 2026-09-25 06:08:00 | NPP-375D | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| c73592a9-f0e3-3198-a016-9b8d9df7eb17 | -9.02208 | -60.52237 | 2026-09-25 06:08:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4d83ad7a-0e03-36f9-83da-4ff0ff866e08 | -7.94438 | -63.49504 | 2026-09-25 06:08:00 | NPP-375D | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| fed45aa8-ea0e-3bc8-8270-b1d8cfadba82 | -8.02652 | -71.36225 | 2026-09-25 06:08:00 | NPP-375D | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 1.1 |
| cf04b5eb-3191-3f59-bd2c-c6ac2d975689 | -8.02587 | -71.36622 | 2026-09-25 06:08:00 | NPP-375D | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 1c5e7f76-3f9c-3657-ad27-19755fd9e745 | -9.35822 | -60.3657 | 2026-09-25 06:08:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2ef01a8a-8633-315d-821a-ed30a5fdbd48 | -9.15164 | -59.48402 | 2026-09-25 06:08:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0a82f5c1-7d55-315a-9223-1e2bf4841b63 | -7.70717 | -71.98637 | 2026-09-25 06:08:00 | NPP-375D | CRUZEIRO DO SUL | ACRE | Brasil | 1200203 | 12 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a1f313fb-5403-3044-bfe7-a18f5c5109b2 | -9.06449 | -65.69655 | 2026-09-25 06:08:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 32df1029-b682-3ce1-aa0e-8ae165fa3409 | -8.59092 | -69.9969 | 2026-09-25 06:08:00 | NPP-375D | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 48bcef6b-15d6-358a-99e2-d06ddf48dcf8 | -8.03668 | -61.32084 | 2026-09-25 06:08:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 45d6cc49-8ca8-3d57-b80d-d47e0fbd36f4 | -7.93971 | -63.49812 | 2026-09-25 06:08:00 | NPP-375D | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 624aefef-f287-3555-8c14-de4fd5136fa7 | -8.89937 | -71.34465 | 2026-09-25 06:08:00 | NPP-375D | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b632d5d0-a245-34a3-8a7e-73884e40d2c7 | -7.6019 | -69.89246 | 2026-09-25 06:08:00 | NPP-375D | ENVIRA | AMAZONAS | Brasil | 1301506 | 13 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 2a178d31-250f-32f2-b5d8-e9dc49d200e9 | -8.61264 | -70.0404 | 2026-09-25 06:08:00 | NPP-375D | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.3 |
| da436b19-575c-3110-8c8e-3bb0fa364cd9 | -8.26925 | -70.81367 | 2026-09-25 06:08:00 | NPP-375D | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 5891ca86-e185-38cd-b839-493a0c80a4cb | -7.66978 | -67.14658 | 2026-09-25 06:08:00 | NPP-375D | PAUINI | AMAZONAS | Brasil | 1303502 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 4d10f081-50a2-3d76-90d4-7d746f9711c6 | -9.0268 | -60.52612 | 2026-09-25 06:08:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e0088d73-8698-3d99-a013-bb35481b1b9e | -9.35864 | -60.3626 | 2026-09-25 06:08:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 0a6bb8dc-e881-3e7b-bbab-234c27841d92 | -10.61382 | -69.2324 | 2026-09-25 06:08:00 | NPP-375D | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 0.6 |


[Clique aqui para ver as próximas entradas](README38.md)
