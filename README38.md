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

## Dados Diários - Página 38

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 3e5e4d7e-b2b7-32d5-b957-5e72a9b6c703 | -2.58604 | -53.99244 | 2024-11-13 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 933a83c0-ae43-39df-b766-d0d37e490745 | -3.8565 | -52.38106 | 2024-11-13 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 853c2f16-2a43-35e8-909c-4716a037b124 | -2.13577 | -50.81011 | 2024-11-13 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 98698e03-c71d-3e20-9b2e-9c442af68fe0 | -2.95383 | -54.20908 | 2024-11-13 04:57:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0b04f480-3c5e-3450-8a7e-8729b8884863 | -1.66212 | -52.54425 | 2024-11-13 04:57:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 0b2eba64-0be5-34bc-9569-572b47ec5f75 | -1.48292 | -51.09219 | 2024-11-13 04:57:00 | NOAA-21 | MELGAÇO | PARÁ | Brasil | 1504505 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 60a4d983-a432-3a73-9d4c-b29986b5e041 | -3.73043 | -45.95256 | 2024-11-13 04:57:00 | NOAA-21 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 4c38807b-f60a-30f6-bf0d-eff233fe6675 | -2.11464 | -52.27805 | 2024-11-13 04:57:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 610c17fc-46cc-37eb-b197-d8b7318dcf52 | -4.81573 | -44.48568 | 2024-11-13 04:57:00 | NOAA-21 | SANTO ANTÔNIO DOS LOPES | MARANHÃO | Brasil | 2110302 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| a37a9a4a-bdfb-356d-8d48-9d5b67738bd0 | -3.02679 | -51.09217 | 2024-11-13 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 184e3771-b473-395e-be12-8d2c98b154f7 | -3.75087 | -46.17125 | 2024-11-13 04:57:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 69d7ce6c-65f7-30ee-9dff-c842cf0ab360 | -1.09847 | -53.16863 | 2024-11-13 04:57:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 433962b2-6f9b-3e2f-9b95-276de7e86f3d | -3.03611 | -50.32785 | 2024-11-13 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 70bc80d3-37e7-36a1-a491-ac2f8ee7de8b | -2.9887 | -51.33847 | 2024-11-13 04:57:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e2c9e8cc-9b19-3083-81fd-71b67dfd7010 | -1.34345 | -51.40284 | 2024-11-13 04:57:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 3f891ab8-9d1b-3936-8bdb-ba6287277303 | -3.00679 | -51.44523 | 2024-11-13 04:57:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| f7f4d522-747a-382a-9a33-4c8c6d136da1 | -4.03099 | -48.94902 | 2024-11-13 04:57:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 0272ec26-96ab-3dc9-8164-a3e54c2842de | -1.51525 | -54.98577 | 2024-11-13 04:57:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c50b2327-b89b-38af-b587-e3f9efe4bda1 | -2.69743 | -49.34971 | 2024-11-13 04:57:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 10.3 |
| dc1beca7-b84b-3412-a177-85e7cf7dbd63 | -3.39728 | -52.47155 | 2024-11-13 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 55a76499-e9ce-377f-b0c1-ba2918287e19 | -1.37439 | -51.99032 | 2024-11-13 04:57:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| cfa23135-5039-3ebe-a4bb-10d572d4f290 | -3.2997 | -51.59704 | 2024-11-13 04:57:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 53d8fa4a-fc2c-38b4-acc7-213f3387ffe6 | -1.38456 | -51.56957 | 2024-11-13 04:57:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| ac59b2fd-5bfb-3bda-b90d-8f47ccd7e25a | -1.11103 | -53.0232 | 2024-11-13 04:57:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 42e04210-0554-3285-9399-7189b95f6f0b | -2.4385 | -49.22124 | 2024-11-13 04:57:00 | NOAA-21 | MOCAJUBA | PARÁ | Brasil | 1504604 | 15 | 33 | nan | nan | nan | Amazônia | 7.4 |
| 925bd0af-4b54-3ef7-bc2d-d0954d75c165 | -3.06172 | -50.33503 | 2024-11-13 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| d6685d43-51dd-386a-92cb-552a830af394 | -2.85352 | -53.3483 | 2024-11-13 04:57:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b64b717f-c8e3-3fad-bab9-20c47499ddeb | -2.32429 | -53.75427 | 2024-11-13 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1da19334-caa1-334d-99de-a88edb9d5e54 | -3.269 | -48.75559 | 2024-11-13 04:57:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 5764a9c8-76fa-3daa-a28a-28f9d3b51038 | -3.65683 | -50.2106 | 2024-11-13 04:57:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 21e50a57-bc34-3c42-8752-3887fd17cbfc | -2.46694 | -51.96333 | 2024-11-13 04:57:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b138fa93-e003-3009-858c-61e7a8d9c60b | -3.10409 | -54.29324 | 2024-11-13 04:57:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 416a577f-4541-3450-8d35-a4f1fbfb0f9c | -1.62237 | -52.38487 | 2024-11-13 04:57:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 24e65933-5733-34f0-8ded-914bf81ba100 | -2.75795 | -54.04739 | 2024-11-13 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| d3562494-c911-3330-92a6-c4a8cf92ce51 | -3.7261 | -51.23685 | 2024-11-13 04:57:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c21a2a64-45b7-32b4-81f7-93fb553eb38a | -1.37774 | -51.99083 | 2024-11-13 04:57:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d6077958-6176-3e69-a673-34808fdfc40c | -3.09826 | -50.24058 | 2024-11-13 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| de08acfc-4d37-3f20-8827-c64adf10f4e5 | -3.03349 | -48.08147 | 2024-11-13 04:57:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 9.3 |
| a32d8056-2964-384a-ac9d-f8b43da68dc5 | -2.31712 | -50.66653 | 2024-11-13 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 2e396e3c-5abd-34fe-94aa-19f352f3586b | -2.10262 | -52.33389 | 2024-11-13 04:57:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 6f183dc5-4c6a-323c-99e0-698849fa631c | -1.74385 | -50.48175 | 2024-11-13 04:57:00 | NOAA-21 | BREVES | PARÁ | Brasil | 1501808 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 20df1eb1-6eaa-355a-abc7-8740778f7ccf | -2.95618 | -54.08577 | 2024-11-13 04:57:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b3315566-6344-38ed-b20f-8718cd04d6bf | -2.99953 | -51.03608 | 2024-11-13 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 8.4 |
| 0d8f253b-8edf-3989-bcd2-4a0bcef3d5cc | -3.98302 | -56.23838 | 2024-11-13 04:57:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d9f344e3-f60c-3e32-821a-5b444a8c7fcb | -2.11344 | -50.69471 | 2024-11-13 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 7338c9f2-cdfb-3cbd-a829-101b0bd064b7 | -1.44229 | -52.25296 | 2024-11-13 04:57:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 8b9a9a3b-968b-3549-ba9a-a3908059080b | -1.93279 | -46.28838 | 2024-11-13 04:57:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d2309c00-3abc-3fc4-9610-7020d6ebf7fc | -4.6078 | -48.60868 | 2024-11-13 04:57:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| b1bf96b4-6b12-3d66-91cb-21582387de1a | -2.37579 | -54.42425 | 2024-11-13 04:57:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 2b740322-6e7a-3818-a90d-0b676d63e49b | -3.90844 | -52.24514 | 2024-11-13 04:57:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| d98a3f3b-bf38-34e9-b5ce-5ed52eb8869a | -3.35124 | -48.95388 | 2024-11-13 04:57:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 14.3 |
| 31e55d1e-5ccb-3203-9e34-1ee6e82127e8 | -3.02966 | -50.98039 | 2024-11-13 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9ce01333-5e1f-33c5-a165-646bcb8f006e | -2.93825 | -48.32292 | 2024-11-13 04:57:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 5ef4e2fc-2504-380d-ade6-3f8c70b59831 | -2.24562 | -53.75609 | 2024-11-13 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 4890d73f-50a3-39b0-8cd4-c55416da3967 | -0.36845 | -51.7413 | 2024-11-13 04:57:00 | NOAA-21 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 4116707f-289e-35df-bfdf-a1c55cf17f24 | -3.43048 | -54.53267 | 2024-11-13 04:57:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ea50a164-6d76-3780-b042-1d66d6023828 | -3.08667 | -50.48889 | 2024-11-13 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e2e29bb5-0500-3a41-be52-0f4cb2b0c838 | -2.77448 | -54.04994 | 2024-11-13 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 8f93950c-6fe8-3770-b69d-570565583165 | -1.76805 | -55.61236 | 2024-11-13 04:57:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 647c980f-3bd4-3ec5-a853-757df2a55ac9 | -1.57555 | -53.7989 | 2024-11-13 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| eefc1135-8673-3f2c-b0b4-54f05369ee90 | -3.24805 | -50.31397 | 2024-11-13 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 335b4158-9cc5-3582-b9bc-62e7de5abd07 | -2.46337 | -53.97286 | 2024-11-13 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| e35519b9-ac9d-3cc6-95a0-96aeadda5db9 | -2.45953 | -53.69427 | 2024-11-13 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| d429b3e5-946a-3c33-92e9-e6085fe77c66 | -2.70439 | -45.99281 | 2024-11-13 04:57:00 | NOAA-21 | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6cd7a0c7-30d9-361d-813b-5001c61a423f | -2.63623 | -46.15581 | 2024-11-13 04:57:00 | NOAA-21 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f4aef59b-e98d-3c61-829e-2898ab2ea604 | -3.26494 | -53.69791 | 2024-11-13 04:57:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 72837526-aa3a-36c1-ae09-c7c8bcec8d51 | -2.7861 | -51.40154 | 2024-11-13 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| bc2a99f6-f525-3f17-857d-3a0a73649b88 | -2.82093 | -46.65233 | 2024-11-13 04:57:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 9a92b021-581a-3757-83af-c3e0f51492a4 | -2.56074 | -54.00264 | 2024-11-13 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 5e0da7c6-248e-38a5-b2fa-bd2edde2e0f3 | -2.93664 | -53.22741 | 2024-11-13 04:57:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| d3c93917-43a5-3258-aea5-cc138f700959 | -2.94026 | -54.10096 | 2024-11-13 04:57:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2cbbcd74-075a-3476-a61e-d4d22d9669a3 | -4.06609 | -54.5367 | 2024-11-13 04:57:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 621cc306-082e-3660-b436-42ae933d61d9 | -2.97024 | -53.8661 | 2024-11-13 04:57:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4621a227-fdf4-3184-bcca-2441635119c8 | -2.46457 | -50.12303 | 2024-11-13 04:57:00 | NOAA-21 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 7.6 |
| 130fba74-3045-3437-93ab-15bb7e5297fd | -1.47137 | -52.30459 | 2024-11-13 04:57:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 6866d8a7-1f4e-3fb0-ab9f-8cb79b914531 | -2.34188 | -48.59736 | 2024-11-13 04:57:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4afb4faa-2596-318a-a634-88f07f712007 | -4.39319 | -48.90281 | 2024-11-13 04:57:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 37c87025-e527-3cd6-a92c-54996ed8ad51 | -2.79094 | -51.75565 | 2024-11-13 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 9c7048d3-eae6-3eb0-bc14-1c6e3d74fcda | -2.75174 | -49.35325 | 2024-11-13 04:57:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| cfc24642-47a8-3318-a341-bd1802fc4da5 | -2.9581 | -53.85719 | 2024-11-13 04:57:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 7dcb93bd-2860-3c45-bace-32b7d3adfa36 | -3.86128 | -51.75286 | 2024-11-13 04:57:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 9fc4d7b7-8e3b-37a9-a9f8-4e36eaeaf1ff | -3.66591 | -54.65844 | 2024-11-13 04:57:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a04d1a4d-cdd3-30ca-ba30-3dcc850baf69 | -3.12713 | -59.01731 | 2024-11-13 04:57:00 | NOAA-21 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 41289349-c07d-3fd1-ac8c-a9078ec54a90 | -3.06599 | -50.33134 | 2024-11-13 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 12.0 |
| 0154bc81-ff5f-3348-8ac4-b319e904faa9 | -5.35857 | -43.53167 | 2024-11-13 04:57:00 | NOAA-21 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| bd5a1db7-3bb4-3d12-8b47-5a0f004a1b92 | -4.78039 | -50.55288 | 2024-11-13 04:57:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 74c3d585-a057-3027-b2d4-86d59b3f63a0 | -2.80569 | -54.00185 | 2024-11-13 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 409e5002-cffc-3e04-b9ac-b068e265c36a | -2.84411 | -53.97671 | 2024-11-13 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| afa5b587-b6d8-3018-9b5c-f05ee952b3ec | -2.39214 | -53.66629 | 2024-11-13 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b4c66e00-fa50-3032-9c2c-7838bd2bca22 | -2.40618 | -50.30466 | 2024-11-13 04:57:00 | NOAA-21 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a9702e96-7fa2-3eaa-91d5-a9e17a2a88fc | -3.04506 | -49.71316 | 2024-11-13 04:57:00 | NOAA-21 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 8b60f731-010f-3536-a1a1-22aeacf905e2 | -2.97677 | -45.15926 | 2024-11-13 04:57:00 | NOAA-21 | VIANA | MARANHÃO | Brasil | 2112803 | 21 | 33 | nan | nan | nan | Amazônia | 3.9 |
| d3aa5b4d-9609-35b7-8709-c4ce6468b57b | -2.56397 | -53.98199 | 2024-11-13 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| b26e6972-dc08-31b5-9739-a911b44b68b6 | -1.98199 | -53.13517 | 2024-11-13 04:57:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 02cd1717-29a6-3051-a92f-b6005cd3c220 | -4.65059 | -45.12785 | 2024-11-13 04:57:00 | NOAA-21 | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| bbd5c5fa-0f72-3b1c-8067-3afce816feca | -2.77901 | -50.29643 | 2024-11-13 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 01c7a1ad-236f-3638-b31b-8aac2b122579 | -3.85847 | -51.90857 | 2024-11-13 04:57:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 91d54344-a61c-339f-adde-0ae1516b751d | -2.12404 | -50.69635 | 2024-11-13 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 07463da9-f2ea-30cc-a15d-dc7b2fc5c069 | -2.97354 | -53.86661 | 2024-11-13 04:57:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| da1092b8-091e-3ba7-b523-37bba12226d3 | -3.10561 | -53.9784 | 2024-11-13 04:57:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |


[Clique aqui para ver as próximas entradas](README39.md)
