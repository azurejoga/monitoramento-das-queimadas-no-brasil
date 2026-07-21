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

## Dados Diários - Página 16

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 860cae11-6841-3365-951e-b3c8faf63d91 | -13.3028 | -45.1278 | 2026-07-21 06:00:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 153.5 |
| 8df8fc5e-d9be-30e4-b645-3477ab06fbde | -18.5476 | -56.8135 | 2026-07-21 06:00:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 117.7 |
| 1f32986e-9d4e-3824-8d29-68569c387490 | -13.3221 | -45.1246 | 2026-07-21 06:00:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 66.7 |
| 6d3dffab-331c-355b-8bce-d2f3556d74e1 | -9.10036 | -71.27077 | 2026-07-21 06:08:00 | NOAA-21 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 0.7 |
| cbabb456-26c2-33d0-a2d9-2a1a5bf06da6 | -9.10227 | -59.4095 | 2026-07-21 06:08:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 03e107f9-591b-3c03-9507-7fee870845a6 | -10.47087 | -62.45104 | 2026-07-21 06:08:00 | NOAA-21 | JARU | RONDÔNIA | Brasil | 1100114 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 2532eb56-3a83-3f1f-bd26-ee3c97442a01 | -9.103 | -59.40349 | 2026-07-21 06:08:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 03fde464-7494-36ba-a28d-d2ff7a8904f7 | -10.01461 | -65.0541 | 2026-07-21 06:08:00 | NOAA-21 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 34dbc0b1-0b2c-35f3-9677-b2460b608119 | -10.46862 | -62.44819 | 2026-07-21 06:08:00 | NOAA-21 | JARU | RONDÔNIA | Brasil | 1100114 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3d490800-f4f7-37c0-ba84-e5495b59a736 | -10.01933 | -65.05472 | 2026-07-21 06:08:00 | NOAA-21 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ca5f6d9b-d57b-3f7e-8dfd-455207d6e680 | -9.10091 | -71.26724 | 2026-07-21 06:08:00 | NOAA-21 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 27465ca3-b487-3e71-bad9-f7ff43b28fb5 | -9.64279 | -67.06567 | 2026-07-21 06:08:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 17d3d093-1e4c-30ce-ba7b-4dbbff8cf056 | -10.46814 | -62.45214 | 2026-07-21 06:08:00 | NOAA-21 | JARU | RONDÔNIA | Brasil | 1100114 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 55276c3e-4250-3e3b-b7d6-e62cfa1a9aed | -13.3032 | -45.1045 | 2026-07-21 06:10:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 58.2 |
| 59aa429d-3baf-30ad-b1cf-56df4a55eba0 | -18.5476 | -56.8135 | 2026-07-21 06:10:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 95.8 |
| 2f28309c-352c-3f10-b9ca-bce17cedce7c | -18.5671 | -56.8317 | 2026-07-21 06:10:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 61.0 |
| 9e377fe0-36bf-3c6a-9757-604631058d48 | -13.3028 | -45.1278 | 2026-07-21 06:10:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 117.8 |
| 0e1e36ea-784c-3307-89d7-91b956e268f0 | -13.3221 | -45.1246 | 2026-07-21 06:10:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 93.9 |
| e6cf7c24-145f-3e3a-b57f-ed58ecc95974 | -18.5472 | -56.8343 | 2026-07-21 06:10:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 68.6 |
| dff7164b-61fd-3a17-9fac-58dfa6c873aa | -18.5675 | -56.8109 | 2026-07-21 06:10:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 72.9 |
| 3e87a98e-efd0-3aaf-86aa-cc195b856237 | -13.3226 | -45.1013 | 2026-07-21 06:10:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 36.4 |
| c2090a9b-7a4c-3604-9e43-e9eb3d09baa8 | -13.3028 | -45.1278 | 2026-07-21 06:20:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 118.9 |
| a2a816fe-cc4c-3180-a839-caf0e6c65e74 | -7.6375 | -49.7507 | 2026-07-21 06:20:00 | GOES-19 | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 50.0 |
| 12b3d7e7-3c94-3165-8080-89e691bad77e | -13.3221 | -45.1246 | 2026-07-21 06:20:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 60.5 |
| a64f928e-a952-349b-9fd7-501472314763 | -18.5476 | -56.8135 | 2026-07-21 06:20:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 92.4 |
| 4dc11a8a-f8d9-3342-b69b-e2f11f9f261f | -13.3032 | -45.1045 | 2026-07-21 06:20:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 80.3 |
| 08e6d0f4-22ee-3b54-8e0f-95b3e40a1a3d | -18.5472 | -56.8343 | 2026-07-21 06:20:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 80.2 |
| 7d8f13f3-a4e8-3d34-b3d9-9941797d5216 | -13.3221 | -45.1246 | 2026-07-21 06:30:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 58.8 |
| 1b785032-89fc-3e72-84d7-3b65217df179 | -13.3226 | -45.1013 | 2026-07-21 06:30:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 39.0 |
| 1fa8af93-c6ff-35c7-ab8e-905f65a2a109 | -13.3028 | -45.1278 | 2026-07-21 06:30:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 127.8 |
| c8780a90-fb74-3d36-a736-7337664b1a60 | -13.3032 | -45.1045 | 2026-07-21 06:30:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 93.8 |
| 505c60da-3ab6-38ce-8e23-183d21d9f982 | -18.5472 | -56.8343 | 2026-07-21 06:30:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 83.7 |
| 99f6c986-635f-364d-8e60-cdf8fabdd679 | -18.5476 | -56.8135 | 2026-07-21 06:30:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 101.1 |
| bbc5bc1d-85f2-3894-a0f3-3616706ab609 | -18.5476 | -56.8135 | 2026-07-21 06:40:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 107.4 |
| 70b9b498-1f60-3282-be2f-fe6b08d0324e | -13.3032 | -45.1045 | 2026-07-21 06:40:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 99.3 |
| 3942cd27-ed4e-3423-a7b6-8fc797b16ea3 | -13.3226 | -45.1013 | 2026-07-21 06:40:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 37.2 |
| 1732b927-863e-33dc-ae6a-5b62feeeb887 | -13.3221 | -45.1246 | 2026-07-21 06:40:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 57.7 |
| f22bed3e-4400-39d6-9073-e7241b9a1665 | -18.5472 | -56.8343 | 2026-07-21 06:40:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 69.9 |
| d4d654e0-d338-3026-8205-e6d2f2a7b84e | -13.3028 | -45.1278 | 2026-07-21 06:40:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 132.1 |
| e25e51db-462e-3a80-a8c0-f319b6f20f31 | -18.5476 | -56.8135 | 2026-07-21 06:50:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 91.3 |
| 510f4618-73c5-3135-839a-7d1454c0cbcd | -13.3028 | -45.1278 | 2026-07-21 06:50:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 125.0 |
| 3b06df4f-e002-3dd1-92e8-1149f6ce355e | -13.3221 | -45.1246 | 2026-07-21 06:50:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 65.4 |
| 35922d0d-3412-36d9-b47b-f8cee140b74c | -18.5472 | -56.8343 | 2026-07-21 06:50:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 60.6 |
| ed88bac0-16aa-3087-93d3-41b4123f5815 | -13.3032 | -45.1045 | 2026-07-21 06:50:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 96.7 |
| ac1a3fe9-4e36-31eb-a95e-00560260c887 | -13.3032 | -45.1045 | 2026-07-21 07:00:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 108.2 |
| e6f88a71-c817-3c25-9d15-2c05e7a1708f | -13.3221 | -45.1246 | 2026-07-21 07:00:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 69.1 |
| 3aea7642-37bb-3c30-9948-efa4a006499e | -13.3226 | -45.1013 | 2026-07-21 07:00:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 64.3 |
| bca1c719-2e0e-31e8-b690-8a1bb34ff348 | -13.3028 | -45.1278 | 2026-07-21 07:00:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 106.0 |
| 351049e6-a9b5-3b2b-8afd-c0b617358557 | -13.3226 | -45.1013 | 2026-07-21 07:10:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 45.7 |
| 161c5790-b22b-352c-9562-7ad42d32579d | -18.5472 | -56.8343 | 2026-07-21 07:10:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 55.1 |
| 0546a157-b213-39d8-b295-320e04a95357 | -13.3028 | -45.1278 | 2026-07-21 07:10:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 89.2 |
| 9a7b8c09-19af-30bf-b46d-ddd22ddd0db1 | -13.3221 | -45.1246 | 2026-07-21 07:10:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 60.7 |
| f78981b5-ff06-3ff7-a41b-2e190a4c076a | -18.5476 | -56.8135 | 2026-07-21 07:10:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 75.8 |
| 62c2ca2f-1283-33d3-93cd-ed3980e3f880 | -13.3032 | -45.1045 | 2026-07-21 07:10:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 92.1 |
| 424e252e-c7fe-3ede-9489-b1ddff14add7 | -18.5675 | -56.8109 | 2026-07-21 07:10:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 49.6 |
| dfd2651e-d35c-38f3-9bc1-6e520d981a6d | -13.3032 | -45.1045 | 2026-07-21 07:20:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 70.0 |
| 6cc9dc30-0b8c-31e2-9c91-2103b34b6273 | -13.3028 | -45.1278 | 2026-07-21 07:20:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 72.8 |
| 23a0bc36-3cb2-32ba-bbe6-5019ee37dc51 | -13.3221 | -45.1246 | 2026-07-21 07:20:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 48.5 |
| df69652f-4e55-3538-a746-63a30b0ce52d | -13.3028 | -45.1278 | 2026-07-21 07:30:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 59.0 |
| 8822c17f-9392-3f91-8928-20f38abd3963 | -18.5675 | -56.8109 | 2026-07-21 07:30:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 56.2 |
| 34943e39-56ae-309c-bc34-5b070907ddc2 | -18.5472 | -56.8343 | 2026-07-21 07:30:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 55.1 |
| 8de30796-491d-3ab7-b118-bf20b8906a26 | -18.5476 | -56.8135 | 2026-07-21 07:30:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 66.5 |
| fed89c9e-52ef-30e0-932f-9fddc77d379c | -13.3032 | -45.1045 | 2026-07-21 07:30:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 58.8 |
| 12787479-c506-3ec2-a7cc-24112d7749ea | -13.3221 | -45.1246 | 2026-07-21 07:30:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 41.7 |
| 4fc7d126-0986-3923-9550-cfe125bbf3fb | -18.5472 | -56.8343 | 2026-07-21 07:40:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 73.0 |
| 816bbbf4-25b7-3798-af29-1bbe8e3c8c9c | -13.3032 | -45.1045 | 2026-07-21 07:40:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 44.4 |
| c8eea290-a3dd-36e2-b860-a021d0dd88be | -13.3028 | -45.1278 | 2026-07-21 07:40:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 53.4 |
| 69016630-e89e-3b7c-9931-643da35eeab6 | -18.5476 | -56.8135 | 2026-07-21 07:40:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 82.8 |
| 479d2252-91c0-374e-98eb-dac6d485ec84 | -18.5476 | -56.8135 | 2026-07-21 07:50:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 82.3 |
| b485078b-727d-337b-9679-8698b6245013 | -18.5472 | -56.8343 | 2026-07-21 07:50:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 65.3 |
| 41aeca23-bdb0-3e1b-9c51-ad47cdfd8129 | -13.3221 | -45.1246 | 2026-07-21 07:50:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 40.7 |
| 2a60396d-8804-3b16-9e3d-5fe79be9feb6 | -13.3028 | -45.1278 | 2026-07-21 07:50:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 55.0 |
| 4c6fc760-8025-3234-8bea-fa2634f8716d | -13.3028 | -45.1278 | 2026-07-21 08:00:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 58.8 |
| 486a9eaa-bc65-3482-a553-358b49927f2d | -18.5476 | -56.8135 | 2026-07-21 08:00:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 70.9 |
| 428657ad-fa97-3693-838d-4a44bd09ef6c | -18.5472 | -56.8343 | 2026-07-21 08:00:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 64.8 |
| be263fd0-6182-3eca-89b3-02f5123e4346 | -13.3032 | -45.1045 | 2026-07-21 08:00:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 38.6 |
| 1702193a-31d4-345d-a86a-65fc989b9622 | -13.3028 | -45.1278 | 2026-07-21 08:10:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 42.4 |
| c1b300a5-9e1f-3592-be01-9f4f172f298b | -18.5476 | -56.8135 | 2026-07-21 08:10:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 59.8 |
| 59a757a2-72e3-31ac-b9ce-521016f640b6 | -18.5472 | -56.8343 | 2026-07-21 08:10:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 58.1 |
| 52427bdd-c470-361e-a541-558f4d23c636 | -18.5476 | -56.8135 | 2026-07-21 08:20:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 76.1 |
| aea5789b-b410-3ac9-91d5-4d23b6eeb1a3 | -18.5472 | -56.8343 | 2026-07-21 08:20:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 56.6 |
| 509d3ef1-3654-3774-8971-49a35898e795 | -13.3028 | -45.1278 | 2026-07-21 08:20:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 43.4 |
| 73c6b74a-07a5-3e2c-af09-213b662f9e04 | -18.5476 | -56.8135 | 2026-07-21 08:30:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 65.8 |
| e3e5dfe9-1184-3549-9e46-cfaf8994c8f4 | -18.5472 | -56.8343 | 2026-07-21 08:30:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 59.4 |
| bb27bce8-8f2c-3848-a3d1-9af2097f16fe | -18.5476 | -56.8135 | 2026-07-21 09:10:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 54.5 |
| 800e24d2-0f52-36d1-9b08-5a74eab23c04 | -18.5476 | -56.8135 | 2026-07-21 09:30:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 61.7 |
| e6e07846-78d6-3859-a75a-660b310b0db2 | -6.03857 | -43.87093 | 2026-07-21 11:42:00 | TERRA_M-M | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 12.2 |
| aa8b3e4a-cb6d-3bb2-840d-953058fa798d | -9.05631 | -44.8464 | 2026-07-21 11:42:00 | TERRA_M-M | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 18.0 |
| cbf9bbf8-32eb-3dc5-ba19-22088c851feb | -9.05505 | -44.85537 | 2026-07-21 11:42:00 | TERRA_M-M | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 5.8 |
| dcaa1c9d-2ab2-3c48-9f06-693701a25a73 | -8.85821 | -46.73193 | 2026-07-21 11:42:00 | TERRA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 69.7 |
| 4fd63c8b-1614-3417-a925-8adac590a895 | -6.21414 | -46.8871 | 2026-07-21 11:42:00 | TERRA_M-M | PORTO FRANCO | MARANHÃO | Brasil | 2109007 | 21 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 3a25a180-f5a1-3629-b84a-7f478c6c342b | -8.85954 | -46.72276 | 2026-07-21 11:42:00 | TERRA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 98.2 |
| 0fd15bf4-b42b-3af3-9b34-4b4b3529dc43 | -7.26592 | -44.90786 | 2026-07-21 11:42:00 | TERRA_M-M | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 35.0 |
| 46d3f8d3-e983-3de5-bb1f-5e559ea93436 | -6.0488 | -43.86308 | 2026-07-21 11:42:00 | TERRA_M-M | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 7.7 |
| c84df99d-d3bc-310d-812f-2639375cc678 | -7.83425 | -47.10555 | 2026-07-21 11:42:00 | TERRA_M-M | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 8.1 |
| cf7f158b-0337-396c-9305-3483bae6ae76 | -6.54118 | -43.10977 | 2026-07-21 11:42:00 | TERRA_M-M | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 5.9 |
| a7e8bd6d-4f6e-331e-8de5-d1364e46179f | -6.92499 | -47.83102 | 2026-07-21 11:42:00 | TERRA_M-M | WANDERLÂNDIA | TOCANTINS | Brasil | 1722081 | 17 | 33 | nan | nan | nan | Cerrado | 15.3 |
| 3387ce3c-4cbf-3fe8-a97d-f41a4bac7fc4 | -7.98573 | -44.19186 | 2026-07-21 11:42:00 | TERRA_M-M | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 12.8 |
| ebdcc854-5363-3c4f-a223-06d81868cf57 | -7.26466 | -44.91668 | 2026-07-21 11:42:00 | TERRA_M-M | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 10.5 |
| 2c8e8eff-d5fc-3f46-a0b6-4d6daf704173 | -7.97677 | -44.19062 | 2026-07-21 11:42:00 | TERRA_M-M | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 5.4 |


[Clique aqui para ver as próximas entradas](README17.md)
