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

## Dados Diários - Página 34

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| ec44fa33-c4ab-3252-a337-75fd9a63b04e | -9.50565 | -60.56001 | 2025-08-17 05:31:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 40602596-d03f-3480-8f19-f991a54165ff | -9.50335 | -60.55186 | 2025-08-17 05:31:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c6547821-c4d3-30b1-8e1d-e63e8f8fc476 | -5.44607 | -60.12661 | 2025-08-17 05:31:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3efab655-9710-3c99-8b95-444079f91c5c | -9.21499 | -59.64966 | 2025-08-17 05:31:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| bd48e678-9f2a-3cfe-85ad-76907a0e9d94 | -8.98604 | -60.51471 | 2025-08-17 05:31:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 013029bf-605c-3d59-a17e-46d78dc5dc6b | -6.08194 | -59.93776 | 2025-08-17 05:31:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| fa7288c5-7490-3dab-ab62-5c3a26eac41b | -10.67194 | -60.77485 | 2025-08-17 05:31:00 | NPP-375D | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a11da5a2-96a6-3268-8c5e-807f7a93b725 | -8.61761 | -64.05743 | 2025-08-17 05:31:00 | NPP-375D | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 5cd79776-3559-308f-ace8-712887290118 | -8.99528 | -60.50059 | 2025-08-17 05:31:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d718054a-f7d8-37c5-9169-53a0f19b3700 | -8.89777 | -60.74693 | 2025-08-17 05:31:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 38f65185-17ab-3a44-9406-9e833a4c9a9c | -8.98779 | -60.50331 | 2025-08-17 05:31:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 0349422f-c4ae-3c7c-b556-b0cd96232266 | -10.00201 | -65.28905 | 2025-08-17 05:31:00 | NPP-375D | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 368aa957-e853-3886-bb8a-d6f227526bae | -11.3743 | -55.42569 | 2025-08-17 05:31:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 6a2db610-d710-3c04-9120-274c8d167878 | -8.02769 | -72.50017 | 2025-08-17 05:31:00 | NPP-375D | CRUZEIRO DO SUL | ACRE | Brasil | 1200203 | 12 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b6e1b3e5-fc17-3681-8ba4-456327bfbcb8 | -6.07565 | -59.95593 | 2025-08-17 05:31:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 313b4837-0d40-3c97-90c0-b7314ca32f71 | -10.11069 | -57.76204 | 2025-08-17 05:31:00 | NPP-375D | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 119a8d13-263a-3ccd-be4f-d8c429d02d5e | -9.3887 | -60.54679 | 2025-08-17 05:31:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| d227d988-739f-3434-b503-b12d574e0308 | -9.55759 | -63.66566 | 2025-08-17 05:31:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 6c4fff03-46cb-390f-b965-27b7b8cabf7c | -9.19527 | -59.63411 | 2025-08-17 05:31:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 3eea63aa-3620-343a-9314-f62ebb2077e3 | -8.99411 | -60.50818 | 2025-08-17 05:31:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 4e81e4f9-c17a-3cdb-989e-4f01b23a8e9f | -9.886 | -64.27304 | 2025-08-17 05:31:00 | NPP-375D | BURITIS | RONDÔNIA | Brasil | 1100452 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| c0da68f3-aa06-3796-8a2a-86a059c67379 | -9.51549 | -60.542 | 2025-08-17 05:31:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 4d434dd8-1c50-3a3c-bfe9-aee93ba1a81d | -8.97397 | -60.50119 | 2025-08-17 05:31:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.2 |
| b5694e02-d199-3e31-a9e3-9fe21a402a7d | -8.98546 | -60.5185 | 2025-08-17 05:31:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ec502d1a-a97a-3f99-95bf-a842e6083094 | -11.36876 | -55.43044 | 2025-08-17 05:31:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| ae47ffc5-542f-3cc9-83e0-1d1bd813aa38 | -9.39563 | -60.54783 | 2025-08-17 05:31:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 47139d3e-22a1-3f33-91ee-9a6327cd8a52 | -8.986 | -60.53797 | 2025-08-17 05:31:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b7414d8e-07a9-327d-ab8e-1a592b0a2e2f | -6.0705 | -59.96662 | 2025-08-17 05:31:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 38c45116-1277-372a-a793-f4732d0fcd12 | -6.07792 | -59.94101 | 2025-08-17 05:31:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| e96289f7-4d03-3ce4-9554-8a0ad7d5b840 | -9.5097 | -60.55673 | 2025-08-17 05:31:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 88e70c03-69c1-377d-a645-bf47b0aef723 | -8.7996 | -52.07511 | 2025-08-17 05:31:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 0408b416-2f56-3a0c-997e-c21a5cca53db | -9.50972 | -60.5333 | 2025-08-17 05:31:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c6a1615b-a49c-3b3e-ac99-07869552ee68 | -7.428 | -60.5978 | 2025-08-17 05:31:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 752c3c92-6e66-3aec-85c6-030bba1ffc6e | -9.51377 | -60.53 | 2025-08-17 05:31:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 11.0 |
| ae80c6ef-f029-3e59-a539-1744ed72fc45 | -9.2192 | -59.64608 | 2025-08-17 05:31:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ec54331e-467a-3812-9e35-2edde4ec0025 | -8.9924 | -60.49626 | 2025-08-17 05:31:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 16e6c408-1109-3ebd-9241-a83453c0f682 | -8.79774 | -52.07843 | 2025-08-17 05:31:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| f6ac2276-bd49-3013-953d-5e1e62fb2bc1 | -10.35829 | -64.50852 | 2025-08-17 05:31:00 | NPP-375D | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 118e13f8-8858-366d-8829-19758992b968 | -8.99868 | -60.52446 | 2025-08-17 05:31:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| fa84c019-0b6c-304c-8866-d11e6f844659 | -8.98087 | -60.50227 | 2025-08-17 05:31:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 6aa1790a-3205-351c-85fc-1cbefd09336c | -8.99873 | -60.50113 | 2025-08-17 05:31:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 782d31f7-4d4c-33cb-b3d1-b816de18be8f | -7.53223 | -50.5307 | 2025-08-17 05:31:00 | NPP-375D | BANNACH | PARÁ | Brasil | 1501253 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 8e6a832d-ffe5-3481-897f-d39e577f43b1 | -5.45174 | -60.13497 | 2025-08-17 05:31:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4e8792ca-8278-3a9e-b8e7-2572194c0053 | -8.23934 | -61.46965 | 2025-08-17 05:31:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 8.7 |
| 9fc6fed3-ac8c-3d26-8364-91a2af710558 | -8.98775 | -60.52661 | 2025-08-17 05:31:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 61472780-b95f-334a-8029-7c779bff10e2 | -10.31762 | -54.15601 | 2025-08-17 05:31:00 | NPP-375D | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 0daf94d3-b2d2-32f6-9648-495bea8b7a8c | -10.11423 | -57.76624 | 2025-08-17 05:31:00 | NPP-375D | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| cf0c60c2-3778-3f7e-8e5c-fddb48a66f1d | -8.87787 | -68.50873 | 2025-08-17 05:31:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 0e560ec9-ff17-3187-b642-d46f17914c7e | -6.46524 | -55.89795 | 2025-08-17 05:31:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 54bfbcac-193c-368a-902c-747da5a0b352 | -8.87717 | -68.51283 | 2025-08-17 05:31:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c2d6a3df-843b-304c-b023-d9af22e92736 | -9.50739 | -60.54858 | 2025-08-17 05:31:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 5e1a354e-17cf-3266-a017-444596ce346c | -9.38929 | -60.54296 | 2025-08-17 05:31:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| bdab18eb-3c73-38cb-8e4f-3c6ea2591f8d | -8.99353 | -60.51198 | 2025-08-17 05:31:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| f9b0e470-8c25-3d5a-a34c-8688a6a1a7b4 | -6.1359 | -57.93489 | 2025-08-17 05:31:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 7b8903e9-4724-348a-a0c3-b30291004627 | -8.99469 | -60.50438 | 2025-08-17 05:31:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 978069ca-a4a1-3021-b68b-5302f164f31d | -9.88719 | -64.26573 | 2025-08-17 05:31:00 | NPP-375D | BURITIS | RONDÔNIA | Brasil | 1100452 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 42c45ba0-37d7-38f8-861b-e5146d0f8216 | -13.01347 | -56.86184 | 2025-08-17 05:31:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 42f6568a-8eb8-31a8-9b42-022335b4c9bf | -9.18204 | -59.64892 | 2025-08-17 05:31:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 986acd4c-e322-3a41-b12c-02e0bb4e74bf | -6.08251 | -59.93404 | 2025-08-17 05:31:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 706cac2e-c812-3879-a242-34472ce8425e | -10.31203 | -54.15834 | 2025-08-17 05:31:00 | NPP-375D | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f9755323-658c-33cb-b478-3fdd1381c369 | -9.85813 | -65.26289 | 2025-08-17 05:31:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| df89a7a2-fbfe-3a29-8866-2bebfe6fcff8 | -11.35979 | -55.4011 | 2025-08-17 05:31:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| b5cde390-ccfc-3d08-8239-fe6f8fc84283 | -7.50499 | -60.30306 | 2025-08-17 05:31:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8db74d6f-a6bf-3aa4-8fa5-d27c2f33e84e | -8.23654 | -61.46559 | 2025-08-17 05:31:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7030fa4c-1321-3688-9c0f-f980c0e46cae | -5.44834 | -60.13443 | 2025-08-17 05:31:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 12546942-0ddd-321f-bf9b-fe16b50734bc | -9.0016 | -60.50546 | 2025-08-17 05:31:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 56d7387a-1a70-31d0-a902-c66f089d7e02 | -8.97858 | -60.49414 | 2025-08-17 05:31:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 16.4 |
| a4238f6c-abfe-33ca-b430-f9da427f2d61 | -8.9872 | -60.50711 | 2025-08-17 05:31:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4010e2d6-4b9f-3d1c-b6d9-87f2f41d2851 | -8.99236 | -60.5196 | 2025-08-17 05:31:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 9504b0fc-7cce-3368-a203-bdb295ea452b | -8.98658 | -60.53418 | 2025-08-17 05:31:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4b080ab3-8b5c-3d1d-94c2-283056488b6e | -8.99815 | -60.50492 | 2025-08-17 05:31:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| f298485c-f294-3e74-8964-51afea3d180c | -8.98491 | -60.49898 | 2025-08-17 05:31:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 303b9df9-2d44-3136-a0af-cb2f6e44f9f5 | -8.978 | -60.49794 | 2025-08-17 05:31:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 87ddf9ba-3b19-3fe0-a4d8-3b29f58e32f0 | -9.51088 | -60.52565 | 2025-08-17 05:31:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| ff644481-5307-37ba-8dcf-b32663a98ad1 | -6.07163 | -59.95917 | 2025-08-17 05:31:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 39130a9c-a34d-3fd7-8794-408bbfc96881 | -9.19907 | -60.83033 | 2025-08-17 05:31:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c942f33b-258d-390a-8a16-6575bf5af95e | -9.0453 | -67.42664 | 2025-08-17 05:31:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| cba46ee7-4572-3529-a727-35be53a0b0bf | -8.99926 | -60.52068 | 2025-08-17 05:31:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c81873ce-b059-34ca-81a5-f67f67ce6806 | -9.51144 | -60.54528 | 2025-08-17 05:31:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| c31baa3d-bfae-358d-bb0e-6d9d80c510c5 | -9.50219 | -60.55947 | 2025-08-17 05:31:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 7400e58c-44ec-3d41-ae8e-3c61d5043d96 | -8.8001 | -52.07133 | 2025-08-17 05:31:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 70155e66-7164-338e-b61a-7f2cfddb61ef | -9.55873 | -63.65855 | 2025-08-17 05:31:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 6a21e861-01a3-3351-b31c-d606eb34878f | -5.45458 | -60.13914 | 2025-08-17 05:31:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 56ef73f3-97a3-3129-a867-0518c312d0bb | -9.93087 | -60.46482 | 2025-08-17 05:31:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 0cfac1d2-75bf-3309-9a11-8f68c19cfc7a | -8.98549 | -60.49518 | 2025-08-17 05:31:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 0296530e-1166-39b9-a2a6-8b8ebf5492ee | -6.66782 | -58.81687 | 2025-08-17 05:31:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| f449172e-21c6-3449-8c11-9e61923f8136 | -8.99003 | -60.53472 | 2025-08-17 05:31:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a5a64486-8827-318d-a30c-26cbb6c312bd | -13.01405 | -56.85738 | 2025-08-17 05:31:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 96ca696a-10c3-3343-9b36-3d4b19f59637 | -8.99931 | -60.49734 | 2025-08-17 05:31:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 446e6228-46b7-3024-a613-74e1b4feb245 | -9.20591 | -60.8314 | 2025-08-17 05:31:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 70c713a3-821c-3378-a6a2-6f0550036bb3 | -10.11525 | -57.75904 | 2025-08-17 05:31:00 | NPP-375D | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 25028139-d941-33ee-aeeb-d153bccb3318 | -6.46583 | -55.89377 | 2025-08-17 05:31:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0c5ce0c3-f242-3297-b69b-73650589115d | -9.18308 | -59.69114 | 2025-08-17 05:31:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3397cf3d-195f-314d-9c49-97e0c4092a6e | -8.30823 | -55.11008 | 2025-08-17 05:31:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 31b77121-6a31-383f-b602-10fcff975f6a | -6.07909 | -59.95644 | 2025-08-17 05:31:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 847f88e7-2883-34ee-a9fa-9f167b819e5a | -9.97944 | -63.29472 | 2025-08-17 05:31:00 | NPP-375D | ARIQUEMES | RONDÔNIA | Brasil | 1100023 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 940f4d5d-281c-33f2-a228-f2fc5a8285f1 | -10.11372 | -57.76982 | 2025-08-17 05:31:00 | NPP-375D | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| de59cdb6-f971-33f9-b93a-b758ddb0b2d5 | -7.53464 | -50.52689 | 2025-08-17 05:31:00 | NPP-375D | BANNACH | PARÁ | Brasil | 1501253 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f7b0e5ef-89ad-3e42-bf97-161ade9465d3 | -6.07107 | -59.96289 | 2025-08-17 05:31:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| db46a4ad-58a6-37fe-8ee3-739fb7488c3f | -8.81159 | -52.03009 | 2025-08-17 05:31:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |


[Clique aqui para ver as próximas entradas](README35.md)
