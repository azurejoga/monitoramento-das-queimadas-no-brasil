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

## Dados Diários - Página 59

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 136abb8f-4fbf-3314-9dc7-a7a681f961be | -12.5147 | -63.3014 | 2024-10-20 13:26:18 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 97.6 |
| fd588441-6d62-3a53-ba0b-733f5389ba1f | -12.5338 | -63.2812 | 2024-10-20 13:26:18 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 74.8 |
| dec91020-2dd2-379f-9209-fb5579a02f5b | -12.5336 | -63.3003 | 2024-10-20 13:26:18 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 76.5 |
| c6442fe9-0c7f-3fd6-8090-e7cf73a96959 | -1.0976 | -49.1915 | 2024-10-20 13:35:12 | GOES-16 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 98.6 |
| 8e9015c5-8d89-3344-91b3-caa4e1aef7aa | -1.1348 | -49.0421 | 2024-10-20 13:35:13 | GOES-16 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 62.4 |
| 0095d827-952e-3051-ad78-10690211b63b | -1.5874 | -53.5111 | 2024-10-20 13:35:15 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 66.1 |
| e52b1264-07b2-3e44-a6d0-2baee719ccfa | -12.5338 | -63.2812 | 2024-10-20 13:36:18 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 78.2 |
| 82429449-b837-325b-8a4f-dd67c1e365a8 | -12.5336 | -63.3003 | 2024-10-20 13:36:18 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 81.5 |
| 67b43909-2564-3adf-a4ff-e565c98737b3 | -12.5147 | -63.3014 | 2024-10-20 13:36:18 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 97.1 |
| 91718ec7-09fa-30f2-952f-19bcc0aaf89c | -1.0792 | -49.1917 | 2024-10-20 13:45:12 | GOES-16 | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | 60.1 |
| c2e91ed9-ee5f-30f6-9949-e3274e848210 | -1.5875 | -53.4909 | 2024-10-20 13:45:15 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 62.2 |
| 231d3891-5bc7-3555-9b94-9807d1f41604 | -2.7773 | -49.3067 | 2024-10-20 13:45:22 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 106.8 |
| 1535d240-3c68-3901-a853-ea341c0ca80b | -12.5336 | -63.3003 | 2024-10-20 13:46:18 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 85.8 |
| d2c21da1-9746-34a9-8686-c62eab95cdd6 | -12.5339 | -63.262 | 2024-10-20 13:46:18 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 66.4 |
| 198bceb0-1c1b-3e3e-b8a8-a0db10595a29 | -12.5338 | -63.2812 | 2024-10-20 13:46:18 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 82.9 |
| 90d5a087-d7f1-34d4-9856-dfdba5a367bc | -12.5147 | -63.3014 | 2024-10-20 13:46:18 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 100.4 |
| 2586f626-a91a-3ecb-a908-0803e154da18 | -2.5543 | -49.7154 | 2024-10-20 13:55:21 | GOES-16 | MOCAJUBA | PARÁ | Brasil | 1504604 | 15 | 33 | nan | nan | nan | Amazônia | 61.0 |
| b1e32327-9de8-393f-9aef-352cb004bbe1 | -12.5336 | -63.3003 | 2024-10-20 13:56:18 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 85.6 |
| 8d620da6-684e-369b-85b6-4782412b7eeb | -12.5147 | -63.3014 | 2024-10-20 13:56:18 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 108.7 |
| 41a88d48-7104-33af-9f16-5233c12b4fa9 | 2.2186 | -50.9393 | 2024-10-20 14:04:54 | GOES-16 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 65.8 |
| 87c5815d-80e5-3d0e-b699-45eb69a29ad3 | 2.2185 | -50.9601 | 2024-10-20 14:04:54 | GOES-16 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 61.2 |
| 47bba733-db31-3a39-a2fe-5752fc30f4e2 | 1.1318 | -51.0398 | 2024-10-20 14:05:00 | GOES-16 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 127.3 |
| bebcd593-9c5c-325f-8003-9d247637cc52 | -2.5543 | -49.7154 | 2024-10-20 14:05:21 | GOES-16 | MOCAJUBA | PARÁ | Brasil | 1504604 | 15 | 33 | nan | nan | nan | Amazônia | 63.1 |
| 1b8abc73-9e9b-32be-af40-aa338ef386af | -2.5358 | -49.7159 | 2024-10-20 14:05:21 | GOES-16 | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 60.3 |
| 5fab6a9d-bad2-3cef-8ba8-55a0fd33e89e | -12.5147 | -63.3014 | 2024-10-20 14:06:18 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 102.5 |
| 11d05803-57aa-3aee-800e-5d6bf4099786 | -12.5336 | -63.3003 | 2024-10-20 14:06:19 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 87.5 |
| bd4c55fb-defa-3b20-8f99-997232890017 | 1.1318 | -51.0398 | 2024-10-20 14:15:00 | GOES-16 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 79.6 |
| efe7bdf4-5a03-36da-8b69-16e34ffcfa70 | -2.5358 | -49.7159 | 2024-10-20 14:15:21 | GOES-16 | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 62.4 |
| 9724b842-13f1-38f4-a361-8f139d54a9ea | -2.5176 | -49.6529 | 2024-10-20 14:15:21 | GOES-16 | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 62.3 |
| ccfbcb73-6c87-3da5-b0d7-87faac6ed9ad | -2.8371 | -53.3463 | 2024-10-20 14:15:22 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 57.9 |
| 8207778f-e14e-3f0f-adab-a8ba673d8859 | -3.2756 | -54.1418 | 2024-10-20 14:15:25 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 63.7 |
| e83ccf5f-4633-325f-b959-b28036b85305 | -12.5147 | -63.3014 | 2024-10-20 14:16:18 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 106.3 |
| e3c6451a-4df7-36f9-8870-11459b498d8b | -1.165 | -53.6571 | 2024-10-20 14:25:13 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 58.4 |
| 4756a85c-a0ff-3d49-8ec6-49442abd151e | -2.1486 | -49.577 | 2024-10-20 14:25:18 | GOES-16 | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 58.4 |
| 298c7aec-c185-31af-b007-2446cd72b7d4 | -2.8372 | -53.3261 | 2024-10-20 14:25:22 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 70.2 |
| 2f3698b6-7485-3bee-bd67-6189abc60289 | -3.2756 | -54.1418 | 2024-10-20 14:25:25 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 65.2 |
| 8538e848-cc52-312a-a01b-fb37daf97c16 | -3.2755 | -54.1619 | 2024-10-20 14:25:25 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 90.4 |
| 3323be8b-9a09-3612-8ef3-063e831992f7 | -12.496 | -63.2832 | 2024-10-20 14:26:18 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 63.4 |
| 93c7874c-61ea-31b2-ba1e-82f568ff9b4e | -17.8447 | -57.4401 | 2024-10-20 14:26:47 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 68.4 |
| 7cfe9ace-3f6b-3452-b39f-749cb178b6f3 | -0.84 | -48.6394 | 2024-10-20 14:35:11 | GOES-16 | SALVATERRA | PARÁ | Brasil | 1506302 | 15 | 33 | nan | nan | nan | Amazônia | 65.3 |
| df7c4e82-2864-3e8d-b5ef-bd991b28a169 | -1.165 | -53.6571 | 2024-10-20 14:35:13 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 85.4 |
| 437bc176-1bf3-300d-81eb-77a2706c4a50 | -1.5351 | -51.9642 | 2024-10-20 14:35:15 | GOES-16 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 65.5 |
| ad68ca22-4b94-30c8-ade6-249b4296f390 | -2.1486 | -49.577 | 2024-10-20 14:35:18 | GOES-16 | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 60.6 |
| 2586ff57-c610-372a-837c-2aff4ebca1bf | -2.8371 | -53.3463 | 2024-10-20 14:35:22 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 67.7 |
| 749dbbb8-3096-395e-bdf5-06c36fb0e675 | -3.2755 | -54.1619 | 2024-10-20 14:35:25 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 84.2 |
| 06d33027-323a-3811-a44f-5b7e17509307 | -3.2756 | -54.1418 | 2024-10-20 14:35:25 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 64.4 |
| 26efa8da-bf0b-3f04-ae54-793bbed410d2 | -12.4958 | -63.3024 | 2024-10-20 14:36:18 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 66.5 |
| 65fde11b-863f-3347-8b33-b3cf37aa3db9 | -12.496 | -63.2832 | 2024-10-20 14:36:18 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 66.8 |
| 18ad7164-ddb9-31aa-8737-622f5e15814a | -17.8052 | -57.4449 | 2024-10-20 14:36:46 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 73.7 |
| d8ceefe8-70c5-383e-8e49-bc8c4457422e | -17.845 | -57.4195 | 2024-10-20 14:36:47 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 59.7 |
| c4c771b3-c269-35b1-9d69-cd7b8b6bfc26 | 2.2186 | -50.9393 | 2024-10-20 14:44:53 | GOES-16 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 66.4 |
| fa483e93-a88e-389c-8ba2-603e42af0936 | 1.1318 | -51.0398 | 2024-10-20 14:45:00 | GOES-16 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 91.6 |
| 07a76bb8-0166-31de-9021-95f2a9b48792 | -0.84 | -48.6394 | 2024-10-20 14:45:11 | GOES-16 | SALVATERRA | PARÁ | Brasil | 1506302 | 15 | 33 | nan | nan | nan | Amazônia | 67.0 |
| 30e32df9-941c-36d8-8522-7661ad82e9ec | -1.165 | -53.6571 | 2024-10-20 14:45:13 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 95.5 |
| 75493c19-752c-3e6f-ba70-c849bd9194ac | -1.5351 | -51.9642 | 2024-10-20 14:45:15 | GOES-16 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 68.8 |
| 6c60e7f8-eeca-3179-b1c7-eb89551971c5 | -1.5535 | -51.9639 | 2024-10-20 14:45:15 | GOES-16 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 65.8 |
| f151310c-d59b-346d-a2f0-39b0ecad188b | -2.0933 | -49.557 | 2024-10-20 14:45:18 | GOES-16 | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 59.0 |
| 2010926a-532b-375c-a1ca-665373362745 | -2.1486 | -49.577 | 2024-10-20 14:45:18 | GOES-16 | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 62.0 |
| 6c2c37b5-20f5-30b0-9b80-f498c6ff2cd2 | -2.8372 | -53.3261 | 2024-10-20 14:45:22 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 192.9 |
| 9578f9ad-ce07-34d2-ba56-83234a5aa573 | -2.768 | -51.9607 | 2024-10-20 14:45:22 | GOES-16 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 74.1 |
| f9f72ab0-2115-35c3-9425-9b11e70d832d | -2.8371 | -53.3463 | 2024-10-20 14:45:22 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 141.6 |
| 4321a84f-992b-3673-bf9d-284430d3f806 | -3.2755 | -54.1619 | 2024-10-20 14:45:25 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 87.0 |
| 0de29a63-d831-30ab-9a5c-d59051ab91de | -3.2756 | -54.1418 | 2024-10-20 14:45:25 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 57.9 |
| 928f7913-4e7a-355b-8044-05f3532433a9 | -12.4413 | -63.0372 | 2024-10-20 14:46:17 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 62.1 |
| bb18a925-57c1-3f6e-a156-62479ccd176d | -12.46 | -63.0553 | 2024-10-20 14:46:17 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 93.3 |
| 56593370-c97c-30f0-99e4-c68e6de4e093 | -12.4958 | -63.3024 | 2024-10-20 14:46:18 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 66.6 |
| 56ec0ab8-0b04-34a2-9428-bdbab0204474 | -12.496 | -63.2832 | 2024-10-20 14:46:18 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 66.5 |
| f1181ebe-4441-3d56-aa82-e7414727af4d | -13.0323 | -62.4831 | 2024-10-20 14:46:21 | GOES-16 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 68.4 |
| 05dc52d0-3377-3c7b-b3c9-dc19c5031071 | -17.8052 | -57.4449 | 2024-10-20 14:46:46 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 84.1 |
| f88e19e2-649b-39a2-a0d0-21644182f346 | -17.8447 | -57.4401 | 2024-10-20 14:46:47 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 76.8 |


