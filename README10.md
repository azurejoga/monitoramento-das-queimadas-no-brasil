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

## Dados Diários - Página 10

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 4643dc1e-1338-395a-9833-14b9a12ca19e | -1.2247 | -51.747501 | 2024-11-11 00:51:00 | METOP-C | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a72bf721-224c-32a7-afe0-c8ef6f461a6c | -1.3551 | -52.540298 | 2024-11-11 00:51:00 | METOP-C | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d07b2ad8-c23a-3b8d-8c82-18ee70c73e33 | -1.55 | -51.861 | 2024-11-11 00:51:00 | METOP-C | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 90541c7c-ffe3-3606-b8d7-a3c68d0c8c0e | -0.0426 | -50.778 | 2024-11-11 00:51:00 | METOP-C | AFUÁ | PARÁ | Brasil | 1500305 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| cf4603c3-5e6f-3414-97d0-ca2655c25339 | -1.2097 | -53.661598 | 2024-11-11 00:51:00 | METOP-C | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 489baaa3-f167-3630-95cb-86d798009080 | -3.0298 | -48.046001 | 2024-11-11 00:51:00 | METOP-C | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2f5e1a5d-90e0-3d06-a322-b74be76650e5 | -2.1117 | -46.105202 | 2024-11-11 00:51:00 | METOP-C | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| de3e7c6e-f170-3c40-911a-295adcdb4136 | -1.1735 | -53.909 | 2024-11-11 00:51:00 | METOP-C | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a593c26c-8720-35bf-a9d4-8a13e61cabe3 | -2.2366 | -53.7789 | 2024-11-11 00:51:00 | METOP-C | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a63c125c-7cbd-348e-8c93-a8d300039d5b | -2.2823 | -53.753601 | 2024-11-11 00:51:00 | METOP-C | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c31bc0be-4981-32e5-ad1d-fd73cf5fa6e9 | -2.442 | -47.6474 | 2024-11-11 00:51:00 | METOP-C | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| fe7615b3-a126-35ec-bc06-051d4045ba8c | -1.56 | -51.994701 | 2024-11-11 00:51:00 | METOP-C | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 25912560-3e14-3dfc-a398-546d6ea5acf2 | -1.3368 | -51.426998 | 2024-11-11 00:51:00 | METOP-C | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1d8c7a39-8ace-3661-a48e-5740a36f6f52 | -2.5401 | -53.980202 | 2024-11-11 00:51:00 | METOP-C | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1f7fe23a-6463-3eeb-97f1-55f41b08fcfc | -3.2292 | -50.505001 | 2024-11-11 00:51:00 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 33d302bd-43bf-3981-85c5-9f6580d5dfd2 | -2.8448 | -54.0061 | 2024-11-11 00:51:00 | METOP-C | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e1ddb8d2-f69c-33d1-bc49-d51dc9a34279 | -2.1895 | -48.376598 | 2024-11-11 00:51:00 | METOP-C | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d9dec366-cc29-312f-bdaa-4fd9cb8fa023 | -4.0259 | -46.975498 | 2024-11-11 00:51:00 | METOP-C | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 3e560602-a1a2-3275-ad8e-9b416fe1b211 | -2.1263 | -53.2509 | 2024-11-11 00:51:00 | METOP-C | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6bbc7740-a5a5-3a63-88d9-2b8fa1ed5e41 | -3.033 | -50.3256 | 2024-11-11 00:51:00 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f07c2792-ebe8-3306-91ec-4a373d81743e | -1.5774 | -53.736599 | 2024-11-11 00:51:00 | METOP-C | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2e6fdc2b-b016-3e2c-ab47-3779b98f4499 | -2.7384 | -49.364101 | 2024-11-11 00:51:00 | METOP-C | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c0d4a562-e422-39fc-805c-bb2d0371d0a3 | -4.1131 | -49.1087 | 2024-11-11 00:51:00 | METOP-C | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b36406d3-4a7a-3e53-a26f-518a160f3e6a | -2.5991 | -54.193901 | 2024-11-11 00:51:00 | METOP-C | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| dfeb481d-1b9b-305d-a0e1-cdb257373fc3 | -2.4187 | -51.960098 | 2024-11-11 00:51:00 | METOP-C | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8389cc18-22fe-3b09-8bba-ffb5bd40d7f4 | -3.0898 | -53.905102 | 2024-11-11 00:51:00 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2467eccb-6be6-3dd8-ae05-099fff75200c | -3.2342 | -50.302799 | 2024-11-11 00:51:00 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e6f0b83c-d0d9-37f1-9a2f-abad45331fc8 | -2.7348 | -49.348701 | 2024-11-11 00:51:00 | METOP-C | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| bb65a54b-a7eb-3139-b248-2db173636f0e | -2.4622 | -53.683399 | 2024-11-11 00:51:00 | METOP-C | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 378c2a6d-f996-3745-8cef-3c7c017c7f5b | -2.418 | -53.670502 | 2024-11-11 00:51:00 | METOP-C | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8c178c37-85da-3a5e-bf2f-dc2aa28dc99d | -17.5861 | -57.3997 | 2024-11-11 00:51:00 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 3fc6d431-dfd3-3971-afc1-bd1609042563 | -2.248 | -53.738499 | 2024-11-11 00:51:00 | METOP-C | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0f421a8d-2b71-3c07-aef2-eea7e233e7c2 | -0.9546 | -52.458199 | 2024-11-11 00:51:00 | METOP-C | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 726ca408-9bac-3f7f-82d3-dc531d174799 | -2.7464 | -49.354198 | 2024-11-11 00:51:00 | METOP-C | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 12cd91ca-85cd-34d8-839e-1d0d4e1ff2e1 | -2.9246 | -51.467602 | 2024-11-11 00:51:00 | METOP-C | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 43af4bc1-534d-38e9-a1b4-df0388c65064 | -2.209 | -48.3722 | 2024-11-11 00:51:00 | METOP-C | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8f351ba6-de7d-34e8-9d43-8f431a78cc17 | 0.1728 | -51.097 | 2024-11-11 00:51:00 | METOP-C | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | nan |
| 8bab26ee-67e6-3586-af45-bc6ea8d543de | -3.5962 | -44.561401 | 2024-11-11 00:51:00 | METOP-C | MIRANDA DO NORTE | MARANHÃO | Brasil | 2106755 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| c21f6b92-2807-3535-ad89-f298438a6a0c | -1.3434 | -51.411098 | 2024-11-11 00:51:00 | METOP-C | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2d16b8ef-e62f-31e0-89bd-0002fa1f14c0 | -1.4908 | -51.738201 | 2024-11-11 00:51:00 | METOP-C | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 75d27d31-0d9e-3d38-90b1-b9c783583e55 | -2.454 | -53.692799 | 2024-11-11 00:51:00 | METOP-C | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| eb46f998-da99-3932-aac6-0cd0c78894ea | -2.9668 | -53.862499 | 2024-11-11 00:51:00 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| df265e2a-3b0a-3804-a983-a58268d94f0d | -3.0968 | -54.299198 | 2024-11-11 00:51:00 | METOP-C | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ba931604-4a5f-3448-9f5b-7e768764edd8 | -3.012 | -53.2463 | 2024-11-11 00:51:00 | METOP-C | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4cdd404d-65c7-39f9-aa6b-0f928d3a0c78 | -3.2388 | -50.1889 | 2024-11-11 00:51:00 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 068433fb-0b5d-3017-a003-b8626817d9ee | -3.5703 | -52.304699 | 2024-11-11 00:51:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| fe961c39-84ed-31bc-9a77-1d39211f042f | -3.5589 | -52.299999 | 2024-11-11 00:51:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e055eec0-8415-3dd0-bcb9-f2be929f48c3 | -2.4658 | -50.415798 | 2024-11-11 00:51:00 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 52fe7573-25c1-3868-bd75-5bbb8a974aa9 | -2.5924 | -51.728199 | 2024-11-11 00:51:00 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 47649c16-96ed-324c-89da-79891e1b36be | -2.3017 | -48.460701 | 2024-11-11 00:51:00 | METOP-C | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 85d6ebfe-e9e0-39e8-a6bc-b9aecdeaab58 | -2.4779 | -53.978401 | 2024-11-11 00:51:00 | METOP-C | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0ef44e82-719d-3106-b07f-6c7569394062 | -4.1113 | -49.101002 | 2024-11-11 00:51:00 | METOP-C | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3b5d4e65-20fa-3f46-a430-2f2102a0cee2 | -1.5615 | -51.282501 | 2024-11-11 00:51:00 | METOP-C | MELGAÇO | PARÁ | Brasil | 1504505 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8b93429d-7310-3323-9b35-15bde6980ffb | -1.2149 | -51.749699 | 2024-11-11 00:51:00 | METOP-C | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f0d99abc-61ec-3e13-af33-86d6059e00a7 | -2.3984 | -49.855999 | 2024-11-11 00:51:00 | METOP-C | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5ac68b05-41a6-3838-8b35-15798a8d7554 | -2.0587 | -53.4062 | 2024-11-11 00:51:00 | METOP-C | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f932cf85-ecd5-33d6-81aa-68b446b31370 | -2.7634 | -49.3829 | 2024-11-11 00:51:00 | METOP-C | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 86ee1a4c-3319-35d9-a207-2a5d27dafec8 | -2.3906 | -53.866798 | 2024-11-11 00:51:00 | METOP-C | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2c811392-1ef5-3ab5-ba6f-a03b21dd83be | -2.953 | -48.026001 | 2024-11-11 00:51:00 | METOP-C | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| fc907728-3d3a-38b1-a21a-4b12f5c10d04 | -1.6112 | -52.3974 | 2024-11-11 00:51:00 | METOP-C | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 04a84069-b6d3-3ff4-b674-1368a305c851 | -0.9757 | -52.460602 | 2024-11-11 00:51:00 | METOP-C | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8d7d3295-b16f-3735-b88a-6193e1ea7119 | -1.8669 | -54.191502 | 2024-11-11 00:51:00 | METOP-C | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b9e059b9-f1e6-3c21-b759-859b1d8d6a57 | -2.7758 | -49.347599 | 2024-11-11 00:51:00 | METOP-C | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ff4ce3ca-bf3d-3a22-b409-1a7be750753a | -17.6359 | -57.509998 | 2024-11-11 00:51:00 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 58a02709-0493-3f71-b6e5-ccc2e4aa9275 | -2.8694 | -49.439701 | 2024-11-11 00:51:00 | METOP-C | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d49bd430-b5b9-3855-881e-e377a796d7f0 | -4.1245 | -43.598701 | 2024-11-11 00:51:00 | METOP-C | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 2240c172-761d-3474-8570-b4ab2e55c169 | -3.5176 | -49.966599 | 2024-11-11 00:51:00 | METOP-C | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4636c8c4-acf6-37d1-b775-f9b7e3e942ed | -3.0779 | -49.360199 | 2024-11-11 00:51:00 | METOP-C | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9b6f45ef-33b4-3fee-9a5c-f1a907558a0d | -0.8379 | -52.534199 | 2024-11-11 00:51:00 | METOP-C | LARANJAL DO JARI | AMAPÁ | Brasil | 1600279 | 16 | 33 | nan | nan | nan | Amazônia | nan |
| 160fc1ed-44bd-37be-a799-373605389865 | -3.1016 | -53.323399 | 2024-11-11 00:51:00 | METOP-C | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b137f005-46f4-32cc-ac46-de1b835c3f2d | -3.0846 | -49.566898 | 2024-11-11 00:51:00 | METOP-C | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e0230646-b267-34b5-a350-f12590f6cb82 | -3.2379 | -46.299599 | 2024-11-11 00:51:00 | METOP-C | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 0ced1f87-b318-3e8c-83c0-a4c945724a79 | -17.599199 | -57.417 | 2024-11-11 00:51:00 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 44f2717f-afba-3ac2-804e-13b0fde1f01c | -2.2369 | -50.720798 | 2024-11-11 00:51:00 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1464dc15-e6f0-3aca-a055-e086063ad5b0 | -2.9228 | -49.492001 | 2024-11-11 00:51:00 | METOP-C | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b9821864-75ae-306a-bc9b-1ef4a3bc17e4 | -3.8452 | -55.9739 | 2024-11-11 00:51:00 | METOP-C | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| aaf1ae8c-0c8e-3361-ae2d-4a673f750ca1 | -1.3921 | -51.982201 | 2024-11-11 00:51:00 | METOP-C | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3d3de235-907a-3122-adbd-d47091414036 | -2.3846 | -49.395302 | 2024-11-11 00:51:00 | METOP-C | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 88f49368-0768-3a33-b116-3b8a3acc71a4 | -2.835 | -54.008202 | 2024-11-11 00:51:00 | METOP-C | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| fb0d74d6-26f3-3d61-bf02-ae27e8e3bd57 | -3.3106 | -50.142502 | 2024-11-11 00:51:00 | METOP-C | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d43a5207-300d-361a-a26b-265fc1e306ed | -3.027 | -45.842899 | 2024-11-11 00:51:00 | METOP-C | ARAGUANÃ | MARANHÃO | Brasil | 2100873 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| dc005451-f774-3afe-a493-769de6cc85c6 | -2.8137 | -54.0051 | 2024-11-11 00:51:00 | METOP-C | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7918511b-5be3-3a2f-918a-4256e95cdffb | 1.5569 | -56.024601 | 2024-11-11 00:51:00 | METOP-C | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 25ab3623-5f13-3bc2-b3cb-27c7f06898ea | -2.211 | -48.380901 | 2024-11-11 00:51:00 | METOP-C | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 363b6040-2114-3517-8e25-0867c0c1d8e9 | -3.0236 | -54.203201 | 2024-11-11 00:51:00 | METOP-C | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 718eb414-ad7c-38fd-8972-2f62b5d5ede3 | -3.325 | -52.5397 | 2024-11-11 00:51:00 | METOP-C | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d82d9fa9-dfe4-32d0-82ee-5a3ea9a88763 | -17.2395 | -57.4846 | 2024-11-11 00:51:00 | METOP-C | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 910e9ae4-a694-3d5e-a86c-50c4024b2284 | -17.587299 | -57.519001 | 2024-11-11 00:51:00 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 8fdce568-ac3a-310c-804e-3065837db124 | -3.4058 | -50.2864 | 2024-11-11 00:51:00 | METOP-C | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 60d40cba-b62a-35b5-bfda-0a1b3b0355b0 | -2.693 | -49.836399 | 2024-11-11 00:51:00 | METOP-C | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d60142c9-84bf-36a5-aa69-2babaf5c7958 | -2.979 | -45.249802 | 2024-11-11 00:51:00 | METOP-C | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 6fe0fe1a-a1cc-3283-8f54-26a58614c4a2 | -0.1448 | -51.4025 | 2024-11-11 00:51:00 | METOP-C | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | nan |
| a298cb39-f22f-3123-b6b1-c0fd6624c4b2 | -2.1785 | -49.084301 | 2024-11-11 00:51:00 | METOP-C | IGARAPÉ-MIRI | PARÁ | Brasil | 1503309 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 27ba18e0-ee9f-3025-be66-14966c09d74a | -3.3582 | -53.4091 | 2024-11-11 00:51:00 | METOP-C | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 93bc37e3-9dd8-36be-9b9a-127cf8800ca3 | -2.243 | -53.6716 | 2024-11-11 00:51:00 | METOP-C | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c0ce0eed-fdad-348a-a23a-3a7f50f96dfb | -1.6096 | -52.390701 | 2024-11-11 00:51:00 | METOP-C | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1715599b-e969-3a08-80a4-fcc7ce27bbe6 | -2.8986 | -49.254398 | 2024-11-11 00:51:00 | METOP-C | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5984de50-45b3-3778-9350-4f96f048c29f | -0.9644 | -52.456001 | 2024-11-11 00:51:00 | METOP-C | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 19b48da8-1257-3491-b326-e62b7fe33a6e | -2.2447 | -53.769501 | 2024-11-11 00:51:00 | METOP-C | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1db151e1-6177-39e4-80ba-a460eb9f3dfe | -3.1051 | -53.700901 | 2024-11-11 00:51:00 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |


[Clique aqui para ver as próximas entradas](README11.md)
