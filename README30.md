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

## Dados Diários - Página 30

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| f5c9f807-4ec5-39bc-a649-196d92f3543a | -3.35617 | -50.17876 | 2024-11-21 04:29:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 6e998201-dfa5-3bcf-bb93-f797695b55d9 | 0.45487 | -50.78913 | 2024-11-21 04:29:00 | NPP-375D | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 2.1 |
| c17c6573-6dd3-332e-adcd-3b2ce675a6e9 | -2.17636 | -52.1276 | 2024-11-21 04:29:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| f2838984-da01-32c4-aa77-eb6e16309d37 | -2.28004 | -48.49062 | 2024-11-21 04:29:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e3e22813-375b-30e5-b16b-2099f9c823c7 | -2.07117 | -48.90433 | 2024-11-21 04:29:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 8ab2583f-2034-32f1-9dd0-310cabff0800 | -2.63726 | -46.20262 | 2024-11-21 04:29:00 | NPP-375D | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 270fa70e-414a-3fc8-bc2b-be5152cc5a26 | -0.81293 | -52.49252 | 2024-11-21 04:29:00 | NPP-375D | LARANJAL DO JARI | AMAPÁ | Brasil | 1600279 | 16 | 33 | nan | nan | nan | Amazônia | 1.8 |
| f3a3d73f-4b17-316b-9e6e-6a51bf859285 | -2.69366 | -46.08293 | 2024-11-21 04:29:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e5d69adb-6b2d-30dd-87cb-7f7e684d731f | -1.73593 | -52.39287 | 2024-11-21 04:29:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 7.3 |
| 8a087f30-31ee-31c3-a7d4-a1da270818d6 | -3.91711 | -42.41621 | 2024-11-21 04:29:00 | NPP-375D | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 51387dd3-449c-3e7e-9d8f-3f1a7a0cd457 | -1.72794 | -53.02499 | 2024-11-21 04:29:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| d9595d68-9a28-3a0b-acfc-1f7aab4836ae | -2.81203 | -54.0218 | 2024-11-21 04:29:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 6ad4447a-b4fd-3326-8546-d133c0eaca49 | -2.07661 | -51.11835 | 2024-11-21 04:29:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 170c7463-c932-3174-b732-e24a9013b1e3 | -2.72058 | -45.16101 | 2024-11-21 04:29:00 | NPP-375D | PINHEIRO | MARANHÃO | Brasil | 2108603 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 624b8496-7dee-3067-9cde-c6ecfb48d66c | -2.69004 | -46.25345 | 2024-11-21 04:29:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 2a909636-4222-3ccb-b70f-3cb33eefbe0e | -0.09788 | -51.42511 | 2024-11-21 04:29:00 | NPP-375D | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 1d15577e-b0bc-3ca1-93a0-1e086fe96c43 | -2.39893 | -49.06332 | 2024-11-21 04:29:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b1865952-a8fd-3cbc-977e-f40bdc60d600 | -2.92446 | -48.32663 | 2024-11-21 04:29:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 4f64b7db-93ce-3e32-a245-2c8b457a1293 | -0.29406 | -51.60489 | 2024-11-21 04:29:00 | NPP-375D | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 3.0 |
| ca41b51b-e878-3009-a966-74eea7f5a4de | -3.39721 | -50.10862 | 2024-11-21 04:29:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 34b6d3e3-f60a-37d2-a9f9-1e11133f1720 | -2.68704 | -46.18538 | 2024-11-21 04:29:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 06067cba-65f6-3bf6-a41f-f7f7cd97cd09 | -0.17553 | -51.62088 | 2024-11-21 04:29:00 | NPP-375D | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f37da9b4-410b-36e0-b5f9-c86924065394 | -2.1428 | -48.76525 | 2024-11-21 04:29:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 72a1261a-3be7-3312-bd5c-45edf8569d0d | -1.7842 | -45.96667 | 2024-11-21 04:29:00 | NPP-375D | AMAPÁ DO MARANHÃO | MARANHÃO | Brasil | 2100550 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a711d8a3-a5ca-3ff4-912b-f270f2b84b1f | -2.55421 | -47.28983 | 2024-11-21 04:29:00 | NPP-375D | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 81f36eae-93e4-3a11-9840-65de339d8adb | -2.66286 | -46.23504 | 2024-11-21 04:29:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3d38f942-04ac-39e8-95f5-e43edf4b51d7 | -3.59399 | -43.63517 | 2024-11-21 04:29:00 | NPP-375D | NINA RODRIGUES | MARANHÃO | Brasil | 2107209 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 165d4083-6716-3888-ad46-b56fb38b4d83 | -1.71109 | -52.38485 | 2024-11-21 04:29:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 8e7dd069-06f9-3795-9b9e-62024978fd94 | -1.25602 | -53.3642 | 2024-11-21 04:29:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 52b3e1b2-db41-3554-9c85-d0d8edb049ef | -1.4277 | -46.01837 | 2024-11-21 04:29:00 | NPP-375D | CARUTAPERA | MARANHÃO | Brasil | 2102903 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 1fe550ee-c60b-38c6-85cb-7f1bd316a913 | -4.15455 | -42.0175 | 2024-11-21 04:29:00 | NPP-375D | BATALHA | PIAUÍ | Brasil | 2201507 | 22 | 33 | nan | nan | nan | Caatinga | 3.6 |
| a657a2cc-5d9b-3f5c-94c3-1c09dd2659a9 | -1.23573 | -46.74374 | 2024-11-21 04:29:00 | NPP-375D | BRAGANÇA | PARÁ | Brasil | 1501709 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 62a5c4bf-30da-3254-afa8-831b5cf7333a | -2.63677 | -46.22745 | 2024-11-21 04:29:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| aa19b214-00d9-37a1-ae8e-0fb0dd363303 | -1.63748 | -52.6079 | 2024-11-21 04:29:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 12fc9bc1-9274-38fe-a60b-05a871726f24 | -1.25546 | -51.7611 | 2024-11-21 04:29:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| f8738d92-d93a-327f-af6d-5d00ab3134b9 | -2.93347 | -48.33541 | 2024-11-21 04:29:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e5a35c11-6acd-3367-9d3c-319ade6dc304 | -4.47916 | -44.75722 | 2024-11-21 04:29:00 | NPP-375D | IGARAPÉ GRANDE | MARANHÃO | Brasil | 2105203 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f55cc65f-8ae7-3479-841b-ee40c0afda1d | -2.82313 | -54.02537 | 2024-11-21 04:29:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| de48b9ca-cddf-331e-9d9a-5b853fd89279 | -2.66715 | -46.16449 | 2024-11-21 04:29:00 | NPP-375D | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 2ac81fd5-4e29-3397-9e33-743c9ecdcabc | -4.25458 | -46.11504 | 2024-11-21 04:29:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 10f74496-b4e9-372b-b6f9-0f9bb504e38e | -2.82445 | -54.09428 | 2024-11-21 04:29:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e155330b-272e-3225-97db-69b8dd3c0e59 | -2.20109 | -53.65966 | 2024-11-21 04:29:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 17.2 |
| 513c19ee-71dd-3119-a063-7052906487ce | -1.61278 | -55.40989 | 2024-11-21 04:29:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f83a8d3d-62ac-3723-9423-541edfeed7ed | -2.16647 | -50.1326 | 2024-11-21 04:29:00 | NPP-375D | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 42da3cab-6590-33ed-996a-88df9ad9921e | -2.67305 | -48.28413 | 2024-11-21 04:29:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 469c527b-4341-3314-a137-10e148854b00 | -2.6988 | -46.21923 | 2024-11-21 04:29:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 141b47a3-47be-3f8a-a36e-c3cd969cebd2 | -1.47816 | -52.51732 | 2024-11-21 04:29:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 60d29102-ee0b-39fa-934c-92365ff926ba | -2.67048 | -46.165 | 2024-11-21 04:29:00 | NPP-375D | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c13d966e-aa08-3f74-b176-6098845ed5b6 | -0.08129 | -51.47799 | 2024-11-21 04:29:00 | NPP-375D | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 19a155b3-5ccb-36fa-ab9a-5973259d624b | -2.78596 | -45.94667 | 2024-11-21 04:29:00 | NPP-375D | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f00d4259-4e82-3288-9655-7cd1ad0d94f3 | -1.4153 | -52.82114 | 2024-11-21 04:29:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 1815202c-4feb-3c47-9df9-4bdf51a17c19 | -1.4332 | -46.00502 | 2024-11-21 04:29:00 | NPP-375D | CARUTAPERA | MARANHÃO | Brasil | 2102903 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| dfaa0bab-fda1-3308-8e12-022f3db2aa0a | -1.78145 | -53.59244 | 2024-11-21 04:29:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 27e653bd-b176-3e7c-856d-f3a64ee4e91d | -2.35829 | -48.91704 | 2024-11-21 04:29:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| dd752511-4b93-3027-89be-2a1b47fec470 | -1.40998 | -52.10947 | 2024-11-21 04:29:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 60c09a1e-715e-3bce-8793-d487a53ed131 | -3.42233 | -50.25354 | 2024-11-21 04:29:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1b5783e1-7a23-38d5-adde-4065f320a984 | -0.94687 | -51.7205 | 2024-11-21 04:29:00 | NPP-375D | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 93369ffd-f7f2-34f9-ac98-896e6031c6ed | -1.75605 | -52.37597 | 2024-11-21 04:29:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 4d38e1ca-a5cf-3690-9290-9c50f3a66873 | -2.90137 | -48.31934 | 2024-11-21 04:29:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 98470115-288c-34fe-95b9-a653c5f2625d | -2.25039 | -49.20559 | 2024-11-21 04:29:00 | NPP-375D | IGARAPÉ-MIRI | PARÁ | Brasil | 1503309 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| ac3018d9-f195-3f7f-944a-498431151218 | -3.30199 | -51.29145 | 2024-11-21 04:29:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| c0c7f70e-df94-3fbe-9a6c-cdea67a9e28e | -1.23815 | -51.74787 | 2024-11-21 04:29:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| e948301f-e301-3676-9b77-b7c5a14ebd42 | -4.48679 | -44.75441 | 2024-11-21 04:29:00 | NPP-375D | IGARAPÉ GRANDE | MARANHÃO | Brasil | 2105203 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c1a5d9ca-eea3-3ce0-ae22-533091031e84 | -1.25255 | -51.7532 | 2024-11-21 04:29:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 347f2458-52b1-3ad9-a810-baa2d90e8a68 | -2.61468 | -49.24904 | 2024-11-21 04:29:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 292908dc-1e5b-33b4-a194-c2c8e06f227d | -0.64495 | -52.33434 | 2024-11-21 04:29:00 | NPP-375D | LARANJAL DO JARI | AMAPÁ | Brasil | 1600279 | 16 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a1bf37e9-03de-3270-ae76-ea544c04b153 | -2.74484 | -51.82603 | 2024-11-21 04:29:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 247c95a7-30b3-342c-9ecc-ec6cb2dc4a42 | -4.47685 | -44.74885 | 2024-11-21 04:29:00 | NPP-375D | IGARAPÉ GRANDE | MARANHÃO | Brasil | 2105203 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 97446dcd-81b8-3da3-99cd-2d935a00a033 | -2.82628 | -46.679 | 2024-11-21 04:29:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| e51a04d4-7f42-3c69-8996-a984a8831155 | -1.25676 | -53.35961 | 2024-11-21 04:29:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 1f3316d8-709b-34c5-86aa-7c2ff2356108 | -4.2556 | -43.8077 | 2024-11-21 04:29:00 | NPP-375D | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 3e41f4a7-9cba-3cb1-8c4a-1fcd595b7bdf | -2.04412 | -48.9623 | 2024-11-21 04:29:00 | NPP-375D | IGARAPÉ-MIRI | PARÁ | Brasil | 1503309 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a6e79736-a7c8-3fee-bb6e-d9ed02fd6c6c | -1.44812 | -52.81325 | 2024-11-21 04:29:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 1f19486c-29ae-3038-b792-ff73e51db486 | -2.69162 | -46.84518 | 2024-11-21 04:29:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1f83b595-504e-391d-8ec3-a25fdd62c513 | -2.65719 | -46.5497 | 2024-11-21 04:29:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 76b5751f-0f2d-38c7-8482-169ea3a9f965 | -2.67103 | -46.16153 | 2024-11-21 04:29:00 | NPP-375D | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 52377176-7e2a-31b4-bdb6-4eb70eff36d0 | -1.48026 | -46.6306 | 2024-11-21 04:29:00 | NPP-375D | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 1725a8b3-1d08-3cc0-9e06-f540ec42f2fc | -2.5718 | -46.55405 | 2024-11-21 04:29:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 1073a103-4f23-38a6-a5b6-9305b01ffbfb | -1.12059 | -46.85303 | 2024-11-21 04:29:00 | NPP-375D | BRAGANÇA | PARÁ | Brasil | 1501709 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 78f99a6d-163b-35ca-b040-bf312307964b | -2.91604 | -48.31427 | 2024-11-21 04:29:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| faca1f4f-d0bb-3ba0-954b-c1705e58563e | -2.68167 | -46.24149 | 2024-11-21 04:29:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 827f48ad-b629-35f2-bc78-4a4cc36470b1 | -4.47976 | -44.75332 | 2024-11-21 04:29:00 | NPP-375D | IGARAPÉ GRANDE | MARANHÃO | Brasil | 2105203 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f42d30c6-0111-3712-8106-3cb467763458 | -4.11124 | -46.90066 | 2024-11-21 04:29:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 7ed01e94-2139-3c78-805d-6d3c444f84d4 | -2.91953 | -46.83821 | 2024-11-21 04:29:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f8d36fb1-ee52-3c6b-b0df-b52227b83092 | -2.45657 | -53.69684 | 2024-11-21 04:29:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| ed367c56-88cc-33c5-a965-1141c9c93942 | -1.98305 | -48.70999 | 2024-11-21 04:29:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 951a4b9a-fc4a-3f08-83e0-fc98379c1c08 | -1.26823 | -51.60902 | 2024-11-21 04:29:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| bd752d69-70c6-3baf-836a-fea3ad89ca86 | -2.07419 | -48.88542 | 2024-11-21 04:29:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| de97ca37-711a-3af2-b5f7-2e0e17284db9 | -3.24748 | -46.43251 | 2024-11-21 04:29:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 39787123-e613-3903-9b47-e32337ec81d3 | -2.71004 | -46.08186 | 2024-11-21 04:29:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 029e19f5-f84b-385d-93b2-cb67c2f59eb9 | -2.38712 | -49.09276 | 2024-11-21 04:29:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 88bf6fae-3044-38b3-9279-15a4f73324e4 | -0.93865 | -51.71921 | 2024-11-21 04:29:00 | NPP-375D | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 8ee1968a-f040-3bd4-8f3d-795ae128dcd7 | -2.40226 | -48.60345 | 2024-11-21 04:29:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| dd49d8bb-2f33-39ae-96a4-114d4bf3b1ff | -3.89008 | -46.62888 | 2024-11-21 04:29:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 698cdff2-3248-38cb-8e90-852230104e40 | -2.27852 | -48.41193 | 2024-11-21 04:29:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 533edcd4-ff30-39db-82a1-2baa36ab0c7b | -2.06497 | -53.43032 | 2024-11-21 04:29:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 2427c8f4-87b8-3884-a734-9e124d4ae13a | -3.79653 | -46.51493 | 2024-11-21 04:29:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 90803fce-4a3b-364c-892e-92d64220b694 | -1.34961 | -55.44498 | 2024-11-21 04:29:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6cf0fe9c-05aa-3ea5-a272-a85251e27dcb | -1.62691 | -52.61876 | 2024-11-21 04:29:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| e3ca3570-2536-3cb3-bd71-bb898143a1bd | -2.26109 | -49.18348 | 2024-11-21 04:29:00 | NPP-375D | IGARAPÉ-MIRI | PARÁ | Brasil | 1503309 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |


[Clique aqui para ver as próximas entradas](README31.md)
