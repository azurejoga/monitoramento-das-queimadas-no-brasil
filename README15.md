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

## Dados Diários - Página 15

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| ff7b4345-6f1c-3474-8bf5-221f792a528f | -7.5666 | -63.84 | 2025-08-29 01:21:00 | METOP-B | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| d013fa85-149d-3160-b05a-e4545346b34f | -11.3771 | -63.2775 | 2025-08-29 01:21:00 | METOP-B | SÃO MIGUEL DO GUAPORÉ | RONDÔNIA | Brasil | 1100320 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 38c043ed-a97e-32ad-ab10-605088d34b71 | -9.0171 | -65.701797 | 2025-08-29 01:21:00 | METOP-B | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 5a8ec6ed-9a4c-31e5-9c5d-1d20f78fd7a6 | -9.5599 | -65.6894 | 2025-08-29 01:21:00 | METOP-B | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| fc519744-4189-33bc-8e4e-cf760f9fc2a5 | -10.8624 | -60.7994 | 2025-08-29 01:21:00 | METOP-B | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| fb0215d2-4afa-3385-bd18-6924e331d126 | -9.2272 | -60.867699 | 2025-08-29 01:21:00 | METOP-B | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| bb6d04ac-c67c-35b7-8dc3-4162f0edbefb | -10.9404 | -63.624001 | 2025-08-29 01:21:00 | METOP-B | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 13a69b36-d1c7-344e-9673-8aaf2d335ce9 | -10.8721 | -60.797001 | 2025-08-29 01:21:00 | METOP-B | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| e1503f1f-6863-382f-a20a-f5cc00f29c4d | -8.1228 | -61.213699 | 2025-08-29 01:21:00 | METOP-B | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 011b7ba2-f3ec-38d9-aa42-d280c298179c | -8.294 | -61.4151 | 2025-08-29 01:21:00 | METOP-B | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| c6e8a372-126d-3573-a620-1be87d6ed809 | -9.2249 | -60.8578 | 2025-08-29 01:21:00 | METOP-B | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| f3b53901-9fe5-3cef-b779-bd2dd5b54867 | -12.2295 | -64.221802 | 2025-08-29 01:21:00 | METOP-B | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| ed07817b-f097-368d-9ef9-79baae2828b5 | -9.1528 | -59.563599 | 2025-08-29 01:21:00 | METOP-B | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 510f7144-3e87-38b7-abd3-923401c3923f | -9.1723 | -59.5588 | 2025-08-29 01:21:00 | METOP-B | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 3d99d87d-df9f-3af5-ad82-ba2163ffd77b | -9.1584 | -60.925598 | 2025-08-29 01:21:00 | METOP-B | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| fcfc39b9-f6f5-3c69-b8fe-b21c70e5a40b | -14.2544 | -58.502602 | 2025-08-29 01:21:00 | METOP-B | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 51d6441c-f5df-3b71-8f7a-f0db79272c54 | -9.5501 | -65.691597 | 2025-08-29 01:21:00 | METOP-B | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 94114752-9746-320e-a0eb-1e066321ac17 | -9.4508 | -60.549099 | 2025-08-29 01:21:00 | METOP-B | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 9d0300fe-31ef-36cb-8d74-264991ada461 | -10.3784 | -57.8274 | 2025-08-29 01:21:00 | METOP-B | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| a36dd14c-e325-3e68-a4c2-43d97f5e6ac9 | -9.1888 | -65.779602 | 2025-08-29 01:21:00 | METOP-B | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| a4ce30a7-e868-36a7-b028-b875a096888a | -9.1171 | -65.781097 | 2025-08-29 01:21:00 | METOP-B | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 809b189a-cfa0-3fdc-85d0-4d828a2a994b | -8.8871 | -60.7384 | 2025-08-29 01:21:00 | METOP-B | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| cc9ad8f1-c920-355c-98fd-7d3ae3106ec5 | -9.1352 | -65.769798 | 2025-08-29 01:21:00 | METOP-B | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| ebd1a5c6-154f-3631-bcbb-d7acba16083d | -9.8095 | -61.192001 | 2025-08-29 01:21:00 | METOP-B | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| a73de141-2162-3c7a-9e55-03821430d675 | -14.3383 | -53.325199 | 2025-08-29 01:21:00 | METOP-B | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| f62bc979-c8e6-3f3d-8c02-12b1df840f62 | -8.2495 | -61.445301 | 2025-08-29 01:21:00 | METOP-B | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| e0c3d405-8c03-3157-878f-05519adef2e6 | -9.1367 | -65.776703 | 2025-08-29 01:21:00 | METOP-B | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 3b6e6254-7b71-30b7-9f46-1013183ef5e3 | -9.1315 | -65.799698 | 2025-08-29 01:21:00 | METOP-B | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 2ebd39fd-5af5-3d08-9ffd-e91479ffeb43 | -14.2738 | -58.497501 | 2025-08-29 01:21:00 | METOP-B | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| aedd6704-54e8-3e2a-ad6f-3e02ccc2f29b | -8.7052 | -69.409698 | 2025-08-29 01:21:00 | METOP-B | MANOEL URBANO | ACRE | Brasil | 1200344 | 12 | 33 | nan | nan | nan | Amazônia | nan |
| 07e64979-50e0-3622-8442-e14d07985118 | -10.3821 | -57.842201 | 2025-08-29 01:21:00 | METOP-B | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 8551bac7-b648-3cea-bed1-eea8bd07b4c7 | -9.7358 | -64.908203 | 2025-08-29 01:21:00 | METOP-B | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| b9d9da6b-1ec7-3164-b5f6-c071d14b163f | -3.7643 | -54.835701 | 2025-08-29 01:21:00 | METOP-B | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8a0704c2-43d9-320d-af6b-1e71cf57ad88 | -7.6063 | -63.338501 | 2025-08-29 01:21:00 | METOP-B | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| d74fce22-24b3-3bf7-9ae6-51e10599ffad | -8.9698 | -65.952202 | 2025-08-29 01:21:00 | METOP-B | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 9cebf979-2f29-395d-8212-9d2b35006423 | -7.087 | -63.053101 | 2025-08-29 01:21:00 | METOP-B | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| ac692149-ecc9-3ee6-8fdb-899f62958429 | -14.3217 | -53.302502 | 2025-08-29 01:21:00 | METOP-B | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 997b3fd3-8291-34ee-814d-c7e37260638a | -9.7934 | -64.248497 | 2025-08-29 01:21:00 | METOP-B | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 87aadb8f-aa76-30af-959b-2bba899ea4fb | -9.1496 | -65.788399 | 2025-08-29 01:21:00 | METOP-B | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 81cc58e4-88a9-3350-bc4e-f031cb1d3f28 | -9.1768 | -60.785599 | 2025-08-29 01:21:00 | METOP-B | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 5f52745c-788c-3319-8318-242848a7427d | -10.1881 | -68.148003 | 2025-08-29 01:21:00 | METOP-B | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | nan |
| eeae16b1-14bb-3805-aba8-ac1ca35d901b | -8.9385 | -64.160301 | 2025-08-29 01:21:00 | METOP-B | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| a0fdfbc8-6aad-3f01-a373-8da94484432c | -9.1557 | -59.5755 | 2025-08-29 01:21:00 | METOP-B | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 8206f378-d149-327e-a21e-78920cae0e0a | -9.0254 | -65.692802 | 2025-08-29 01:21:00 | METOP-B | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| b2ee11cb-0b3c-3f11-a314-5f16c5832ca8 | -9.7721 | -64.245903 | 2025-08-29 01:21:00 | METOP-B | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| b2dcd705-de3b-36f7-b977-5db44b2f0f3a | -8.1807 | -61.372101 | 2025-08-29 01:21:00 | METOP-B | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 25765c19-c9bc-3f7f-a501-8512ed901ecc | -19.151899 | -57.784801 | 2025-08-29 01:21:00 | METOP-B | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 6eeb11e7-3c07-3f24-8c90-2463a28078ac | -8.903 | -69.424698 | 2025-08-29 01:21:00 | METOP-B | MANOEL URBANO | ACRE | Brasil | 1200344 | 12 | 33 | nan | nan | nan | Amazônia | nan |
| 3fa55016-e936-3ad4-a437-8fcce2ad6a79 | -28.7071 | -55.575298 | 2025-08-29 01:21:00 | METOP-B | SÃO BORJA | RIO GRANDE DO SUL | Brasil | 4318002 | 43 | 33 | nan | nan | nan | Pampa | nan |
| 5d4fd8a0-139f-3124-b734-a51298c05bb1 | -8.8895 | -60.7486 | 2025-08-29 01:21:00 | METOP-B | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 6ef2493d-37c4-3a7c-bd65-847c707a1b8b | -10.8646 | -60.8088 | 2025-08-29 01:21:00 | METOP-B | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 1fe9bc0e-db58-3704-af1e-101c4d8f840d | -8.1785 | -61.362598 | 2025-08-29 01:21:00 | METOP-B | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| ca449c58-c627-3747-92df-91bf6e7738ea | -9.7342 | -64.901299 | 2025-08-29 01:21:00 | METOP-B | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| b6107d17-5f06-31df-8505-b4897546c9ef | -10.4658 | -57.93 | 2025-08-29 01:21:00 | METOP-B | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 96743a40-c908-3af3-889f-f8b93bf91b86 | -9.4752 | -60.5648 | 2025-08-29 01:21:00 | METOP-B | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 8589710e-f724-329f-890b-1d178e884dec | -8.3015 | -61.403301 | 2025-08-29 01:21:00 | METOP-B | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 2dc50e45-2589-3a7b-8e98-6903220d29f3 | -9.0269 | -65.699699 | 2025-08-29 01:21:00 | METOP-B | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 37f0d29a-cac5-3d11-8a77-c81f613cf76f | -9.5485 | -65.684601 | 2025-08-29 01:21:00 | METOP-B | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 8b4fd71a-1aca-38a1-80dd-c0268427aa80 | -9.1285 | -65.785896 | 2025-08-29 01:21:00 | METOP-B | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 84442be1-2f22-3fae-9fe3-80cd281dc715 | -8.6942 | -62.466702 | 2025-08-29 01:21:00 | METOP-B | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| e59dacda-7b5e-324c-8443-093b9df92e61 | -9.1692 | -65.783997 | 2025-08-29 01:21:00 | METOP-B | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| ccf772ca-f967-3ee9-85b2-e1096b9fd854 | -9.8929 | -64.690002 | 2025-08-29 01:21:00 | METOP-B | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 954e401a-5b33-36ba-a60d-24f387a8e7f5 | -9.8133 | -67.835098 | 2025-08-29 01:21:00 | METOP-B | BUJARI | ACRE | Brasil | 1200138 | 12 | 33 | nan | nan | nan | Amazônia | nan |
| 2dccf330-daf2-3c1c-ae8d-973eb6579694 | -9.6636 | -64.953697 | 2025-08-29 01:21:00 | METOP-B | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 1fb5a0d6-2153-37aa-ac90-ce814dbe90b9 | -8.5479 | -70.743698 | 2025-08-29 01:21:00 | METOP-B | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | nan |
| 03cf2304-221b-33d8-946c-47af28593c32 | -16.288 | -53.608299 | 2025-08-29 01:21:00 | METOP-B | GUIRATINGA | MATO GROSSO | Brasil | 5104203 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 253f5400-7557-313b-9354-89b0b4b90fa1 | -9.7852 | -64.257698 | 2025-08-29 01:21:00 | METOP-B | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 4c1d30dc-04c8-3fb7-9b58-8fd906438a9b | -9.1784 | -59.456001 | 2025-08-29 01:21:00 | METOP-B | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| a5a569b1-8b65-3e29-81c9-18d5d4a5ef42 | -28.745399 | -55.645599 | 2025-08-29 01:21:00 | METOP-B | SÃO BORJA | RIO GRANDE DO SUL | Brasil | 4318002 | 43 | 33 | nan | nan | nan | Pampa | nan |
| 46e81da2-f1d6-3b9e-9ac4-fa6cf8ae9619 | -10.371 | -57.797699 | 2025-08-29 01:21:00 | METOP-B | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| ca4e77d7-3829-3c62-8724-0aa8399a50e4 | -16.2784 | -53.611198 | 2025-08-29 01:21:00 | METOP-B | GUIRATINGA | MATO GROSSO | Brasil | 5104203 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 1969b3d4-ecdd-3378-84f1-97c909f6c951 | -9.2152 | -60.8601 | 2025-08-29 01:21:00 | METOP-B | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| aed704df-addf-3f75-8742-a49e9f42af93 | -9.6796 | -64.979301 | 2025-08-29 01:21:00 | METOP-B | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 04d7de03-3a98-34dd-a1ab-eff2aaafd455 | -6.5358 | -43.9237 | 2025-08-29 01:30:00 | GOES-19 | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 85.9 |
| 59cbbe71-3428-32ea-b637-b09570b166df | -9.462 | -60.549 | 2025-08-29 01:30:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 112.1 |
| c00ed39b-e5db-3ccb-8646-afa859e4988e | -13.558 | -46.8745 | 2025-08-29 01:30:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 89.2 |
| 46bf5036-5e19-32b9-b7ec-aa9dda213b61 | -6.9684 | -59.3169 | 2025-08-29 01:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 59.3 |
| 0deb11be-b5c8-3018-a591-b4eae49014de | -6.9867 | -59.3354 | 2025-08-29 01:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 98.0 |
| 433b111d-90bd-312d-a38e-a01196dd0971 | -5.6081 | -45.0038 | 2025-08-29 01:30:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 222.6 |
| e996ec02-f0ac-3c6e-89f7-69f5fa830d44 | -13.1837 | -45.2865 | 2025-08-29 01:30:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 155.5 |
| 02c8b39e-361f-3cf2-a2d2-b37b0609c76a | -13.0151 | -56.9184 | 2025-08-29 01:30:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 32.9 |
| e300ebd0-4d53-3caa-b5bd-d8e8869e85a3 | -5.6266 | -45.0252 | 2025-08-29 01:30:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 52.7 |
| 6e2be766-4b82-33c6-b7b1-5f0c469f4e5e | -13.2036 | -45.2601 | 2025-08-29 01:30:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 53.4 |
| c1f23ae3-67af-327f-bd0d-33f809c3b22b | -10.3812 | -57.8245 | 2025-08-29 01:30:00 | GOES-19 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 62.0 |
| c67d8211-1695-3409-aa79-90e59bf4e8e1 | -13.5386 | -46.8775 | 2025-08-29 01:30:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 98.9 |
| 6eb949a2-6683-37fc-baf0-5b70d12f12b8 | -8.1944 | -61.3747 | 2025-08-29 01:30:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 60.5 |
| c9c86959-6735-3aa3-a85e-b7b9b1a90f2f | -10.4551 | -57.9378 | 2025-08-29 01:30:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 60.0 |
| bed8a6d3-fa47-3739-b13c-759396685678 | -9.4263 | -47.6384 | 2025-08-29 01:30:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 85.3 |
| 04ea4229-f9d8-3440-8442-f304359920f3 | -6.1674 | -47.2638 | 2025-08-29 01:30:00 | GOES-19 | CAMPESTRE DO MARANHÃO | MARANHÃO | Brasil | 2102556 | 21 | 33 | nan | nan | nan | Cerrado | 54.6 |
| 4dc2d627-16af-3ad3-9bb4-cd938c32084c | -9.2178 | -60.8689 | 2025-08-29 01:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 78.3 |
| 6aacd7c8-ee71-30b1-87ab-6ce36bdf5867 | -9.7916 | -64.2461 | 2025-08-29 01:30:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 140.4 |
| a87b8319-34ca-3829-9880-0754efe37be5 | -6.9869 | -59.3161 | 2025-08-29 01:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 49.5 |
| 1e1a7df5-c194-3e98-bf89-bdafee4322ab | -8.1758 | -61.3755 | 2025-08-29 01:30:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 83.1 |
| 689451a5-a83b-3aea-96ad-e8703795600e | -9.7728 | -64.2657 | 2025-08-29 01:30:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 97.9 |
| 3d759a4f-04e8-3c65-974d-880883e83c6e | -10.8608 | -60.7998 | 2025-08-29 01:30:00 | GOES-19 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 70.5 |
| f51b53b7-cb4b-3a88-8633-de41097313df | -9.426 | -47.6605 | 2025-08-29 01:30:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 47.6 |
| 4786e283-bf1b-3155-99eb-30cf843d3260 | -6.5546 | -43.9221 | 2025-08-29 01:30:00 | GOES-19 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 131.1 |
| 5ae97a90-403e-30ac-9d55-2faf772fdaea | -7.0569 | -44.3623 | 2025-08-29 01:30:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 81.9 |
| 7362fd41-9c2c-3e7c-9e6c-d61d90926c2e | -17.3442 | -42.6333 | 2025-08-29 01:30:00 | GOES-19 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 55.1 |
| 987e7cf2-5226-345f-86f3-4c468db5520f | -3.4254 | -49.0517 | 2025-08-29 01:30:00 | GOES-19 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 70.3 |


[Clique aqui para ver as próximas entradas](README16.md)
