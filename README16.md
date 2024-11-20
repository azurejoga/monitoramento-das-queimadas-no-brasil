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
| cfd003bb-1f59-3e4d-aab2-a27b2f77d04a | -11.1109 | -54.6204 | 2024-11-20 02:00:00 | GOES-16 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 102.3 |
| c46b9473-2ae1-3863-824e-2d1650321f95 | -4.459 | -46.5966 | 2024-11-20 02:10:00 | GOES-16 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 49.8 |
| 2e86387f-86f6-3ff7-816e-794b00c3a9e8 | -3.8206 | -47.7879 | 2024-11-20 02:10:00 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 36.6 |
| c3a1e02a-b869-3248-b7e2-973bb93b66fd | -2.7033 | -49.3513 | 2024-11-20 02:10:00 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 35.4 |
| 613c3aa0-0d2d-3402-9347-db70f90a4060 | -3.8205 | -47.8096 | 2024-11-20 02:10:00 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 36.8 |
| b83506cd-7c06-3f68-aafe-27cc99bbbe93 | -3.2014 | -54.3243 | 2024-11-20 02:10:00 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 75.6 |
| addf2a3d-fb42-369d-95e8-530a93fc389e | -2.93 | -53.0601 | 2024-11-20 02:10:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 52.9 |
| 5a450080-7bf0-3c3f-9afe-88697003d88b | -4.4405 | -46.5754 | 2024-11-20 02:10:00 | GOES-16 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 45.0 |
| 1b594207-f322-3c70-860f-80e556866012 | -2.9116 | -53.0606 | 2024-11-20 02:10:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 65.3 |
| 32b9d870-4932-368e-be37-a77970dd4e1f | -5.9742 | -48.063 | 2024-11-20 02:10:00 | GOES-16 | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 62.6 |
| 4dd42355-14c9-34d1-9ad5-74738a4d9baf | -2.7402 | -49.3502 | 2024-11-20 02:10:00 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 54.4 |
| 179fc847-fca6-3088-a518-29f8491ba4d8 | -4.4592 | -46.5745 | 2024-11-20 02:10:00 | GOES-16 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 52.3 |
| c5468aec-dfb2-3323-9d51-b967c1edbe39 | -1.2017 | -53.6769 | 2024-11-20 02:10:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 81.0 |
| fb2ef98f-7076-39dc-9bc4-387d7b3480d2 | -4.4404 | -46.5975 | 2024-11-20 02:10:00 | GOES-16 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 45.9 |
| 4119c04a-8d7f-3b91-84e1-12d4f69deeb4 | -5.9556 | -48.0642 | 2024-11-20 02:10:00 | GOES-16 | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 74.5 |
| 8f37263e-2079-3ace-b9b5-bc1e7e9cdaf7 | -4.3959 | -47.7618 | 2024-11-20 02:10:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 50.0 |
| 1c766cc1-3972-33f0-b20b-f11b41f4da99 | -3.802 | -47.8104 | 2024-11-20 02:10:00 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 40.4 |
| 18228564-26ea-30be-8024-ceb6ba0d547e | -2.7218 | -49.3295 | 2024-11-20 02:10:00 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 74.1 |
| caf5d2c3-26e6-34c8-84db-ecf3504f959d | -4.3774 | -47.7627 | 2024-11-20 02:10:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 42.6 |
| 0b640088-a542-3417-b4dc-3fd89c4ef30a | -2.9969 | -45.436 | 2024-11-20 02:10:00 | GOES-16 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 67.1 |
| 93b35d68-c7ac-3834-8ce3-434f4c67c6ae | -2.7217 | -49.3508 | 2024-11-20 02:10:00 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 143.5 |
| bc51477a-2f30-3d59-9e07-e0b49fe3f4ac | -5.9556 | -48.0642 | 2024-11-20 02:20:00 | GOES-16 | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 113.0 |
| 67d65dea-a088-3dfc-836e-54806b3f0155 | -14.8449 | -53.6661 | 2024-11-20 02:20:00 | GOES-16 | SANTO ANTÔNIO DO LESTE | MATO GROSSO | Brasil | 5107792 | 51 | 33 | nan | nan | nan | Cerrado | 55.3 |
| 8f2d78d9-1202-340e-aa11-30ce708e97d1 | -4.1594 | -43.9739 | 2024-11-20 02:20:00 | GOES-16 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 127.4 |
| af5db673-5d43-39d3-bbfe-5804683d6aa1 | -4.4592 | -46.5745 | 2024-11-20 02:20:00 | GOES-16 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 59.6 |
| e6cb5b99-c236-3948-ace6-fd9a24beb1d3 | -4.459 | -46.5966 | 2024-11-20 02:20:00 | GOES-16 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 45.9 |
| 5fbb91a9-c84d-32ef-94f1-e1c98e351d6d | -4.4405 | -46.5754 | 2024-11-20 02:20:00 | GOES-16 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 47.3 |
| 96a4b174-fcd5-33ca-8cda-91225e4d822a | -2.75 | -51.8377 | 2024-11-20 02:20:00 | GOES-16 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 40.7 |
| 3a2dce68-0119-3a66-9036-0c8c142cc4ec | -3.2014 | -54.3243 | 2024-11-20 02:20:00 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 65.2 |
| c3bf517a-ceae-3632-a4c6-930b0065ca13 | -2.7501 | -51.8171 | 2024-11-20 02:20:00 | GOES-16 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 36.8 |
| cdef328b-799d-3141-88c5-f0f88f9ccb94 | -1.2017 | -53.6769 | 2024-11-20 02:20:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 83.9 |
| 7c8bda4e-1a7c-3d67-bf0a-1f80429b2e7d | -1.4603 | -52.6812 | 2024-11-20 02:20:00 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 59.6 |
| 381eb6b8-a4ec-3b1c-9eec-107fce834b44 | -4.1407 | -43.9749 | 2024-11-20 02:20:00 | GOES-16 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 82.6 |
| 944c09f3-46ef-339e-882f-cf82fab1f933 | -23.2896 | -51.406 | 2024-11-20 02:20:00 | GOES-16 | ROLÂNDIA | PARANÁ | Brasil | 4122404 | 41 | 33 | nan | nan | nan | Mata Atlântica | 71.5 |
| 59fd8fb6-dbcf-37cf-beed-0210be540f64 | -5.9742 | -48.063 | 2024-11-20 02:20:00 | GOES-16 | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 75.5 |
| 81b0c594-ecd1-3654-b2aa-9d436faa1254 | -4.4592 | -46.5745 | 2024-11-20 02:30:00 | GOES-16 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 39.6 |
| ad9dd6ef-4da2-33df-9545-5beeff5b2878 | -12.938 | -57.0057 | 2024-11-20 02:30:00 | GOES-16 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 58.9 |
| 1eb9da02-1c8b-353f-8850-4827c6cad924 | -3.802 | -47.8104 | 2024-11-20 02:30:00 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 45.7 |
| e7092311-74db-3d16-9525-ec99b3b58a76 | -3.8205 | -47.8096 | 2024-11-20 02:30:00 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 68.2 |
| b23dabd1-005f-329c-88ef-fb8463054d63 | -4.4404 | -46.5975 | 2024-11-20 02:30:00 | GOES-16 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 57.1 |
| 88671eee-6fbc-3954-83e3-1a0b29879139 | -3.2014 | -54.3243 | 2024-11-20 02:30:00 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 50.6 |
| 26d31ae3-a18c-3a6b-9edc-94500fb6b7d3 | -1.4603 | -52.6812 | 2024-11-20 02:30:00 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 60.3 |
| 468baea5-9036-3c55-b9d6-07c458ba636c | -4.4405 | -46.5754 | 2024-11-20 02:30:00 | GOES-16 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 57.9 |
| 76605ceb-336e-3229-ba10-2de2ea749504 | -1.2017 | -53.6769 | 2024-11-20 02:30:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 94.1 |
| bfae29b1-9b1c-3db4-b460-de51bd3a1db5 | -2.6212 | -51.8203 | 2024-11-20 02:30:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 36.4 |
| b9b1402c-fc18-3cb5-a83e-aa512ccfc8aa | -4.1594 | -43.9739 | 2024-11-20 02:30:00 | GOES-16 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 75.2 |
| fb424a2c-9a88-3048-a3a0-1705487958f1 | -4.3959 | -47.7618 | 2024-11-20 02:30:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 46.9 |
| dd3fa68a-140f-3bbf-b92a-ded603a3507a | -5.9742 | -48.063 | 2024-11-20 02:30:00 | GOES-16 | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 91.5 |
| b6861287-b0ea-308f-81d7-51a7e6dd5092 | -3.8206 | -47.7879 | 2024-11-20 02:30:00 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 62.2 |
| e8b2bdd5-cb2b-3049-9322-a1191b5d1aeb | -2.7217 | -49.3508 | 2024-11-20 02:30:00 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 36.5 |
| f9caadcc-812a-38d8-858b-feeb353d1a43 | -5.9556 | -48.0642 | 2024-11-20 02:30:00 | GOES-16 | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 97.0 |
| 2cbe3fab-887a-3e0b-b325-118024d1d679 | -2.6212 | -51.7997 | 2024-11-20 02:30:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 99.2 |
| ade39194-cea8-3a3a-910c-7c2c49827d52 | -12.9377 | -57.0258 | 2024-11-20 02:30:00 | GOES-16 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 56.0 |
| 2bf5172c-5cb6-34ec-bed0-1cc30e68fbff | -3.8021 | -47.7887 | 2024-11-20 02:30:00 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 40.5 |
| 5fb43a4e-5d61-3a3c-b714-a736b3f4b78b | -2.6397 | -51.7992 | 2024-11-20 02:40:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 36.6 |
| 0411ed7a-6fc2-3e98-875c-324e2596e550 | -4.4592 | -46.5745 | 2024-11-20 02:40:00 | GOES-16 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 62.6 |
| 3457e27c-e620-3f4a-a53d-6365ffb3830a | -3.2014 | -54.3243 | 2024-11-20 02:40:00 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 61.1 |
| b5ca40c5-94e0-3452-80fb-5c36b12195cb | -5.9554 | -48.086 | 2024-11-20 02:40:00 | GOES-16 | ARAGUATINS | TOCANTINS | Brasil | 1702208 | 17 | 33 | nan | nan | nan | Cerrado | 56.7 |
| cc885d37-ac30-3930-b7f1-d05b1ea7e5a6 | -1.2017 | -53.6769 | 2024-11-20 02:40:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 85.1 |
| 7a7df94f-e0a8-3c88-8472-889f6f3fa6a0 | -2.7501 | -51.8171 | 2024-11-20 02:40:00 | GOES-16 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 37.4 |
| 8e14befe-067f-3bca-adfa-620c3210e1f7 | -2.75 | -51.8377 | 2024-11-20 02:40:00 | GOES-16 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 37.0 |
| 33f32ed2-d36b-38ea-b6c8-8efb89a37c04 | -4.3774 | -47.7627 | 2024-11-20 02:40:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 48.8 |
| b898a545-7ba8-3e30-ba2c-39723b986d6c | -2.6212 | -51.8203 | 2024-11-20 02:40:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 36.6 |
| df6cffd2-3e18-3ea9-8919-a4298ccb2bfa | -2.7217 | -49.3508 | 2024-11-20 02:40:00 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 66.9 |
| 9682719c-2da8-3bfa-9b84-edba0cd3cf03 | -5.9742 | -48.063 | 2024-11-20 02:40:00 | GOES-16 | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 100.8 |
| cd82556e-7d01-3ba9-820b-024475bad51c | -4.4405 | -46.5754 | 2024-11-20 02:40:00 | GOES-16 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 49.3 |
| c6a83346-de99-3810-a878-2a34f20a8d30 | -4.459 | -46.5966 | 2024-11-20 02:40:00 | GOES-16 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 50.1 |
| 8a6bc3df-dd52-3a8f-9d20-93a48b1274a5 | -2.6212 | -51.7997 | 2024-11-20 02:40:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 66.0 |
| 6a0c457f-bfbb-3b43-9e66-6abce56eeed6 | -4.4404 | -46.5975 | 2024-11-20 02:40:00 | GOES-16 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 43.9 |
| e3c4b294-9836-3ab8-938b-c1045da7d844 | -5.9556 | -48.0642 | 2024-11-20 02:40:00 | GOES-16 | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 133.3 |
| a4bb1df9-836d-32c5-8b82-3f310b8053f9 | -2.7218 | -49.3295 | 2024-11-20 02:40:00 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 44.0 |
| 0b240174-ef6a-33d3-8dc2-b86782ec7e8a | -7.59275 | -34.93882 | 2024-11-20 02:49:00 | NOAA-21 | GOIANA | PERNAMBUCO | Brasil | 2606200 | 26 | 33 | nan | nan | nan | Mata Atlântica | 5.3 |
| 76b0215e-37d1-39cd-b284-b68ebfee3e77 | -7.59148 | -34.94551 | 2024-11-20 02:49:00 | NOAA-21 | GOIANA | PERNAMBUCO | Brasil | 2606200 | 26 | 33 | nan | nan | nan | Mata Atlântica | 5.3 |
| 2e738cf0-d6ee-321a-8ecf-d71ac108270c | -5.9556 | -48.0642 | 2024-11-20 02:50:00 | GOES-16 | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 127.9 |
| 9d71af60-544c-3700-a2f9-cdf615754e3d | -11.1106 | -54.6408 | 2024-11-20 02:50:00 | GOES-16 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 52.2 |
| bd06f329-c3fa-34f6-ba10-2be2ef4c3680 | -4.459 | -46.5966 | 2024-11-20 02:50:00 | GOES-16 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 39.1 |
| b39dbe5b-8663-3466-8801-ff5aa4083307 | -2.6212 | -51.8203 | 2024-11-20 02:50:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 36.4 |
| e2dd6c1a-cc50-3e31-b58f-5a5f49a0e45e | -4.4404 | -46.5975 | 2024-11-20 02:50:00 | GOES-16 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 51.3 |
| a82a0b84-cb3d-3b31-a1cd-af536e77f972 | -11.1109 | -54.6204 | 2024-11-20 02:50:00 | GOES-16 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 63.7 |
| 4564cd39-e043-3a98-87e7-4d760208a4a5 | -2.6212 | -51.7997 | 2024-11-20 02:50:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 83.7 |
| df7ef190-dc06-39cc-a474-4b5dde1deebe | -4.4405 | -46.5754 | 2024-11-20 02:50:00 | GOES-16 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 52.9 |
| 907b7e3b-e467-3702-92ab-2845db3ad813 | -2.7217 | -49.3508 | 2024-11-20 02:50:00 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 48.6 |
| a1174c1e-009c-3fae-ada5-8820397c5e2b | -1.2017 | -53.6769 | 2024-11-20 02:50:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 89.0 |
| 6d9f3a2c-5c85-36f0-a82a-b6e0a87de558 | -2.75 | -51.8377 | 2024-11-20 02:50:00 | GOES-16 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 45.6 |
| 2a57cfeb-4a31-3c44-9dca-6d20235fdb36 | -3.2014 | -54.3243 | 2024-11-20 02:50:00 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 57.4 |
| 730f259a-e7f6-3483-a5d2-97f9deb64041 | -5.9742 | -48.063 | 2024-11-20 02:50:00 | GOES-16 | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 106.0 |
| e0ae89a8-1c69-3dca-b2c9-ca80603cdf42 | -4.4592 | -46.5745 | 2024-11-20 02:50:00 | GOES-16 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 41.2 |
| 1be8f2ef-7c7e-3569-9498-f69e58d1df59 | -2.7501 | -51.8171 | 2024-11-20 02:50:00 | GOES-16 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 41.4 |
| 96014be8-becc-38fa-acf7-2a89894fb5a6 | -5.9742 | -48.063 | 2024-11-20 03:00:00 | GOES-16 | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 99.9 |
| af183bbb-6199-3862-b85d-d910f42dda61 | -11.0917 | -54.6425 | 2024-11-20 03:00:00 | GOES-16 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 61.9 |
| ae666b71-5f01-3e4d-b188-03547fb31d45 | -5.9556 | -48.0642 | 2024-11-20 03:00:00 | GOES-16 | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 128.1 |
| 42714663-13d3-302a-a9d5-fceb39e80d7a | -2.75 | -51.8377 | 2024-11-20 03:00:00 | GOES-16 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 50.3 |
| a24f10c1-204b-3671-ae62-5a4c25248e34 | -11.1106 | -54.6408 | 2024-11-20 03:00:00 | GOES-16 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 71.3 |
| 05ca893b-77ad-3f35-a896-add16a07c6fe | -5.9557 | -48.0425 | 2024-11-20 03:00:00 | GOES-16 | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 55.9 |
| 58e23025-75b3-302f-be4e-6b2d32e48696 | -11.092 | -54.6221 | 2024-11-20 03:00:00 | GOES-16 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 81.5 |
| 4ec6c5b2-214a-307d-9b74-d88517c4a237 | -4.459 | -46.5966 | 2024-11-20 03:00:00 | GOES-16 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 41.9 |
| f8e3e715-0373-3bb3-84b5-115bd4de12a3 | -4.4592 | -46.5745 | 2024-11-20 03:00:00 | GOES-16 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 40.8 |
| 9fce2d81-390f-3fdc-8f69-4be8c29843df | -4.5614 | -48.0141 | 2024-11-20 03:00:00 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 45.0 |
| 25a638c1-4ac2-3c4c-a956-80605954383b | -4.4404 | -46.5975 | 2024-11-20 03:00:00 | GOES-16 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 59.9 |
| 27e6f378-d8f7-3aec-809e-705b76bcf339 | -2.3371 | -54.783 | 2024-11-20 03:00:00 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 44.5 |


[Clique aqui para ver as próximas entradas](README17.md)
