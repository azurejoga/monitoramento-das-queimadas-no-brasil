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

## Dados Diários - Página 89

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 90c02d34-02ee-3bb4-a64e-057c8c12ffcf | -9.64302 | -64.95892 | 2024-10-13 05:04:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 87ea17ce-3b7f-38a4-8814-fef3e2eb0e02 | -9.63904 | -64.9519 | 2024-10-13 05:04:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| b8ec7eb5-95f3-3618-95b2-aa14c9c5f040 | -9.63848 | -64.95493 | 2024-10-13 05:04:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| ee7619b0-3f15-3ffb-b126-a1919c4e1914 | -9.63792 | -64.95796 | 2024-10-13 05:04:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| d1723d50-297a-3e2d-b654-348297ba4679 | -9.35974 | -65.74537 | 2024-10-13 05:04:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 96c50e33-d947-3c15-926e-6eae239f6cc7 | -9.35913 | -65.74876 | 2024-10-13 05:04:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| df23e9b5-e9b0-3fba-9f35-3f566fae914d | -9.35666 | -65.74118 | 2024-10-13 05:04:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 03531c1c-84b8-375f-8244-d9be329af2c9 | -9.35603 | -65.74453 | 2024-10-13 05:04:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e6b98942-29ac-378b-8ed4-877f9edcaefb | -9.35539 | -65.74792 | 2024-10-13 05:04:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 996d5d03-b428-33fd-a541-516365297074 | -9.35495 | -65.74098 | 2024-10-13 05:04:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 3d683efb-47f0-31a2-afd6-6f1c3ca464b0 | -9.35434 | -65.74435 | 2024-10-13 05:04:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 3413756a-34fa-33d0-b025-7d804639a15a | -9.35062 | -65.74356 | 2024-10-13 05:04:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 60c07288-b71e-3edc-8c67-8b4bf8a450f4 | -11.72719 | -64.97182 | 2024-10-13 05:04:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 8.8 |
| d8fd17dd-9a9b-3795-af9c-4b4f9f34dda5 | -11.72614 | -64.9775 | 2024-10-13 05:04:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 62895576-e3e6-3cf2-b5ed-93acd1f53d9c | -11.7233 | -64.96536 | 2024-10-13 05:04:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 9e4322b4-353d-3677-aaec-829b73d32a91 | -11.72225 | -64.97099 | 2024-10-13 05:04:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 4.2 |
| d6dac89c-8abc-36fc-b89d-73321152e160 | -11.72121 | -64.97659 | 2024-10-13 05:04:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 5d63f1fb-ebf6-365f-b345-6ed3fd6a1711 | -10.90093 | -65.09904 | 2024-10-13 05:04:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 8115926d-af15-327d-bc67-0d3dc637c44f | -10.90036 | -65.1021 | 2024-10-13 05:04:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 76e15c48-b1a1-3fb1-8bf0-701fa8f490bd | -10.89978 | -65.10519 | 2024-10-13 05:04:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e4668e74-b8b5-35b9-a23e-af393d725788 | -10.89633 | -65.09579 | 2024-10-13 05:04:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 24b1c1ab-b265-3754-94b4-d63743b70f5e | -10.89416 | -65.10732 | 2024-10-13 05:04:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 937c10aa-d80d-3dcc-bf78-933a253e29cb | -10.46296 | -69.69682 | 2024-10-13 05:04:00 | NPP-375D | ASSIS BRASIL | ACRE | Brasil | 1200054 | 12 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 924fb10a-9f03-3c0a-9f53-08c07d569db3 | -10.45619 | -69.69553 | 2024-10-13 05:04:00 | NPP-375D | ASSIS BRASIL | ACRE | Brasil | 1200054 | 12 | 33 | nan | nan | nan | Amazônia | 1.9 |
| ef0bede3-6d02-34af-b4db-d47d7da32f9d | -10.40195 | -69.1408 | 2024-10-13 05:04:00 | NPP-375D | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 3f242ad9-5404-3435-bda2-2a0feb719bba | -10.39956 | -69.14468 | 2024-10-13 05:04:00 | NPP-375D | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 134b67c9-1e7f-3d63-b11e-2ee949a77f07 | -1.0626 | -47.9269 | 2024-10-13 05:05:11 | GOES-16 | CASTANHAL | PARÁ | Brasil | 1502400 | 15 | 33 | nan | nan | nan | Amazônia | 44.7 |
| 71338a91-8be7-3887-b104-89f3bb6b851d | -3.0956 | -53.0559 | 2024-10-13 05:05:23 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 51.0 |
| db3e2a93-910d-3db4-bfcd-590306abdc4b | -3.0957 | -53.0355 | 2024-10-13 05:05:23 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 100.9 |
| 312a12ac-dc93-351e-8d91-31ace5f12db2 | -3.114 | -53.0554 | 2024-10-13 05:05:23 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 47.9 |
| 1a05b079-a2bb-3b73-9d81-28bc1277fe6a | -3.1141 | -53.0351 | 2024-10-13 05:05:23 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 74.6 |
| a8951070-6a52-3277-880c-83c5c4e3addf | -18.22791 | -56.47561 | 2024-10-13 05:06:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.7 |
| 0ef5f339-ad07-3d0f-96b0-fb1141229a2c | -15.40035 | -56.23977 | 2024-10-13 05:06:00 | NPP-375D | VÁRZEA GRANDE | MATO GROSSO | Brasil | 5108402 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 462d3fb1-9a70-3002-a9cd-588f8f346f19 | -17.73257 | -56.27313 | 2024-10-13 05:06:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.3 |
| cff1805a-c9f5-3d86-b4ec-6e23e7e71552 | -17.7297 | -56.26867 | 2024-10-13 05:06:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.9 |
| babd4caf-fb11-3caf-a00d-7a71a3e66c67 | -17.72913 | -56.27258 | 2024-10-13 05:06:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.3 |
| 96a00fbc-b142-34ba-bf73-a3cce53c8756 | -17.72569 | -56.27203 | 2024-10-13 05:06:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.8 |
| ee944792-e9dd-3403-805a-95336a0f4f58 | -17.72281 | -56.26757 | 2024-10-13 05:06:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.1 |
| 77f86614-87a5-3b23-a56d-3c80447c3738 | -17.72224 | -56.27147 | 2024-10-13 05:06:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.8 |
| a2274385-ee74-30e7-a804-94df8a228372 | -17.6833 | -56.321 | 2024-10-13 05:06:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 6.3 |
| d767dd8f-c2cc-3692-a97e-ae86538ba54f | -17.65544 | -56.25382 | 2024-10-13 05:06:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 7.2 |
| 3735c9b6-164f-3533-94cd-b73c5e3fa3bf | -18.23365 | -56.50834 | 2024-10-13 05:06:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.1 |
| 1f0bef58-a440-3e3b-8152-3c08a1aa0f68 | -18.23308 | -56.51222 | 2024-10-13 05:06:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.1 |
| 6ac3fc07-07e7-3a6b-b665-fade5c16c9b1 | -18.23306 | -56.48838 | 2024-10-13 05:06:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 6.3 |
| 710ed85c-c3ed-3005-862d-f83a0c10d7de | -18.2325 | -56.5161 | 2024-10-13 05:06:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.1 |
| 6be5ab07-741d-39f1-a404-2ac968a063e4 | -18.2325 | -56.49226 | 2024-10-13 05:06:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.2 |
| 629c370f-bb09-3974-badb-1a9f2e38c2b1 | -18.23021 | -56.50779 | 2024-10-13 05:06:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.9 |
| 1899b495-76d6-3f25-999a-23382aa511f2 | -18.2302 | -56.48394 | 2024-10-13 05:06:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 6.3 |
| 7c4f8f51-baf3-3600-874a-03df638d9f73 | -18.22964 | -56.51167 | 2024-10-13 05:06:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.9 |
| 725678a6-4f0b-31aa-ab66-6a475eeda355 | -18.22963 | -56.48783 | 2024-10-13 05:06:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 6.3 |
| 2a9924ef-e9a7-3a93-bccc-637223b49b9e | -18.22907 | -56.51554 | 2024-10-13 05:06:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.5 |
| f62cf2ec-cd46-3adb-bfe3-d576cd277801 | -18.22906 | -56.49171 | 2024-10-13 05:06:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.2 |
| e2582ae5-0360-3340-ade8-c3c52346b8bd | -18.22848 | -56.47173 | 2024-10-13 05:06:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.5 |
| d22fd106-fe67-3e36-9c82-15cd261f9031 | -18.22734 | -56.4795 | 2024-10-13 05:06:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.7 |
| cf4c21a8-cc7c-389d-b04a-54977580ccb3 | -18.22677 | -56.48339 | 2024-10-13 05:06:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.1 |
| dc03acfd-d4cf-318e-b185-d7da225db7c4 | -18.2262 | -56.48727 | 2024-10-13 05:06:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.1 |
| a20f32e1-a1b6-37d3-bae9-b39100949fd9 | -18.22561 | -56.46729 | 2024-10-13 05:06:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.5 |
| 4e43a3b9-ef81-39b5-a962-4152e5309112 | -18.22506 | -56.49504 | 2024-10-13 05:06:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 6.7 |
| de90e7d8-d47d-342d-8034-d2f2e2213b92 | -18.22504 | -56.47117 | 2024-10-13 05:06:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.5 |
| 5af41b90-4d25-376d-a425-bc5a8ba03ad7 | -18.22449 | -56.49892 | 2024-10-13 05:06:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.6 |
| 87bc1c90-c8c4-3caf-9e23-d1a1d0b1d61f | -18.22447 | -56.47506 | 2024-10-13 05:06:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.7 |
| 4ce59e3e-d269-3b8b-938b-881c22d556e4 | -18.2239 | -56.47894 | 2024-10-13 05:06:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.7 |
| 7c294085-a545-3420-9c50-a73f9cdde6cc | -18.22388 | -56.45506 | 2024-10-13 05:06:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.2 |
| 556bab52-dacf-32f0-8136-a774856cfb4e | -18.22333 | -56.48283 | 2024-10-13 05:06:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.1 |
| debb6264-1574-3713-8ec7-0d6dcaa2d6f0 | -18.22332 | -56.45895 | 2024-10-13 05:06:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.5 |
| 3934f8ba-9370-3dff-9f32-a6b1ac23c401 | -18.22276 | -56.48672 | 2024-10-13 05:06:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.1 |
| da342c6d-8ce7-30e9-8c7b-0c4023645b24 | -18.22274 | -56.46284 | 2024-10-13 05:06:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.5 |
| 8423ad99-0bf8-3456-81f9-49f8f32114b7 | -18.22222 | -56.53824 | 2024-10-13 05:06:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.2 |
| c8ed4647-b647-3f1f-b215-490ca9d140de | -18.22219 | -56.4906 | 2024-10-13 05:06:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 6.7 |
| 0f5b39c2-5a45-337a-ba10-1303a6b75458 | -18.22218 | -56.46673 | 2024-10-13 05:06:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.8 |
| a9538fbe-3b95-3960-b569-bbbee8362762 | -18.22213 | -56.41885 | 2024-10-13 05:06:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.4 |
| 1a83c247-abae-3b9e-98c1-4fdb2ad242a8 | -18.22166 | -56.56586 | 2024-10-13 05:06:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.9 |
| 747cc366-14de-3867-98de-0b119a6b025b | -18.22165 | -56.54211 | 2024-10-13 05:06:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.2 |
| 4f08ba0f-e5b5-3b7d-a376-72935dd66ae6 | -18.22163 | -56.49448 | 2024-10-13 05:06:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 6.7 |
| 97e074aa-e250-3bb5-8e16-a9c95d756be3 | -18.22159 | -56.44671 | 2024-10-13 05:06:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.5 |
| cdf2fb4d-42a0-3a57-843c-2631b0d51ebe | -18.22156 | -56.42276 | 2024-10-13 05:06:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.4 |
| 7a6f06f6-e3ae-3eb3-9b87-b80c462d53c0 | -18.22109 | -56.56973 | 2024-10-13 05:06:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.9 |
| ae259fd4-c1d4-3f7c-89d1-bdb382177576 | -18.22108 | -56.54597 | 2024-10-13 05:06:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.9 |
| bdc373e9-c6b5-38a8-87f8-8687a9599b78 | -18.22102 | -56.45061 | 2024-10-13 05:06:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.2 |
| 95983610-da41-3393-891b-81234f55b5c8 | -18.22051 | -56.54984 | 2024-10-13 05:06:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.9 |
| c5eeb0cc-f5a4-3bc3-8ec2-100b7cef9750 | -18.22045 | -56.4545 | 2024-10-13 05:06:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.2 |
| 65cd7bb0-76dc-3514-ae1f-c087951a9ee8 | -18.2199 | -56.48228 | 2024-10-13 05:06:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.8 |
| 2de4b24b-7f2a-3d72-ba46-2ec8ab99afdb | -18.21988 | -56.45839 | 2024-10-13 05:06:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.5 |
| fc17274f-1451-3dd2-bd67-203c16bb9fa8 | -18.21985 | -56.43446 | 2024-10-13 05:06:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.1 |
| 6a47a5ce-a707-3371-a343-9311020b4c95 | -18.21936 | -56.53381 | 2024-10-13 05:06:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.8 |
| b3dcbe35-1bc3-3bba-9532-bfba7dafb068 | -18.21933 | -56.48616 | 2024-10-13 05:06:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.8 |
| fdb4dd2d-a3c3-349e-b689-fdd8562a756d | -18.21928 | -56.43836 | 2024-10-13 05:06:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.1 |
| b3ec374d-b853-3f8d-90f7-d8bed9352625 | -18.21881 | -56.56144 | 2024-10-13 05:06:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.9 |
| 8d1c6b45-41ad-3a5b-bac9-356b86122e16 | -18.21879 | -56.53768 | 2024-10-13 05:06:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.2 |
| f22b12c0-3d16-3142-97f7-079fcac525bc | -18.21876 | -56.49004 | 2024-10-13 05:06:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.7 |
| 4c1a04d8-830a-3a40-b101-073f04d7edc2 | -18.21872 | -56.44226 | 2024-10-13 05:06:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.8 |
| 128a281c-62ee-305e-b56c-31aa2ef8a4e0 | -18.21869 | -56.4183 | 2024-10-13 05:06:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.4 |
| 2142409a-0cc1-3bdd-9f5d-24e4cf0e49e5 | -18.21824 | -56.56531 | 2024-10-13 05:06:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.9 |
| 7c03fe55-8b07-3157-8c86-6f467de4812c | -18.21823 | -56.54155 | 2024-10-13 05:06:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.2 |
| 014af0ea-b655-32f0-9822-21cdb647dc52 | -18.21819 | -56.49393 | 2024-10-13 05:06:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.7 |
| 1ab719ba-b718-3123-bf1f-746aa6251718 | -18.21815 | -56.44616 | 2024-10-13 05:06:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.8 |
| c5daf1ec-af3c-348f-958a-ae00f1814666 | -18.21812 | -56.42221 | 2024-10-13 05:06:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.4 |
| 183c7e8c-dd4c-3e16-866f-046e8c84d72b | -18.21767 | -56.56917 | 2024-10-13 05:06:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.9 |
| 8f26a509-dfae-3e86-ace6-f2b20812c9ba | -18.21766 | -56.54542 | 2024-10-13 05:06:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.6 |
| 3b6c9107-702c-3f4f-b2c4-45ece75e050e | -18.21758 | -56.45005 | 2024-10-13 05:06:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.3 |


[Clique aqui para ver as próximas entradas](README90.md)
