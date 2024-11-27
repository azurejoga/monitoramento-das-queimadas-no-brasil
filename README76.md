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

## Dados Diários - Página 76

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| a00c2c41-5db1-3fd8-aebf-f11e17f82bfd | -2.83028 | -54.10416 | 2024-11-27 05:35:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| df5fb72b-ce2c-3b7d-8cfd-e773a5ae4fbe | -2.5978 | -54.25739 | 2024-11-27 05:35:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 2a866b1e-4db9-3dcc-8e8b-0e759fa3c79b | -3.68817 | -50.23055 | 2024-11-27 05:35:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 2126a07b-b229-3750-a422-76dabb62e81c | -3.10492 | -53.24942 | 2024-11-27 05:35:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 9.8 |
| 068b1639-bab0-3345-a1d4-c0fc2edc91dc | -1.35447 | -54.63438 | 2024-11-27 05:35:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 47616f40-5e68-3760-8182-1ab9f082edd1 | -2.94086 | -54.79162 | 2024-11-27 05:35:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| ba99e3a9-d6cd-3713-8193-c5dd33b35b61 | -3.1082 | -53.10705 | 2024-11-27 05:35:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| bfabfa6f-1756-39b8-abde-f4f773af9787 | -1.35449 | -54.634 | 2024-11-27 05:35:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c3382033-4854-3568-8114-bde4101f6154 | -3.49661 | -53.80983 | 2024-11-27 05:35:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d834945e-5ff6-3159-90ab-bd0802d60d26 | -2.10282 | -53.35358 | 2024-11-27 05:35:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 6ffa9a32-9479-3eb8-88b7-6604807d0c3d | -1.76351 | -53.62049 | 2024-11-27 05:35:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| aff041e8-2971-38d8-b626-f3b543f9188b | -3.49711 | -53.8065 | 2024-11-27 05:35:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| cecd60c7-117d-3243-80a9-6e538f7bfe09 | -2.80462 | -54.13044 | 2024-11-27 05:35:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 9ba03545-2293-3225-b11f-140d12459c24 | -1.79921 | -52.74625 | 2024-11-27 05:35:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 88b24017-40e5-321e-ba6c-9bcdd334b0c6 | -2.61573 | -52.53516 | 2024-11-27 05:35:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c2e2cf84-2bdc-3a83-a839-bb37a6b02801 | -3.50207 | -53.81076 | 2024-11-27 05:35:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b161bbaa-50bf-3e07-bc33-92b5b84c0329 | -2.80937 | -52.91536 | 2024-11-27 05:35:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 1bc96f8c-520b-3483-aa90-ea05e680057d | -2.81082 | -53.02597 | 2024-11-27 05:35:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a2d74517-fa4b-3b3b-927a-fdc7f8f72f9a | -3.28682 | -51.11576 | 2024-11-27 05:35:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 4141a3e5-727c-3195-94e6-5ced8d44538a | -2.90047 | -54.17259 | 2024-11-27 05:35:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| fa459c48-90da-35b0-8670-c4d378e757bd | -3.23649 | -50.67886 | 2024-11-27 05:35:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 0cab9163-7772-3b9a-b570-cd1e975cc4fe | -3.70861 | -51.8031 | 2024-11-27 05:35:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| d6316f88-661b-3bd5-9a6b-6d8bf115e624 | -1.80493 | -52.74717 | 2024-11-27 05:35:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 4ac0473d-8878-364b-b364-5d181267a7c6 | -3.6 | -50.35631 | 2024-11-27 05:35:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 44118899-f134-3f40-aaca-445057e4737c | -2.18529 | -53.78189 | 2024-11-27 05:35:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 12.9 |
| 5f50d385-25cd-34b4-9b7c-477ab3e65ffd | -3.09789 | -50.35655 | 2024-11-27 05:35:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| b2e5f911-4407-3635-8ad0-229eab5a15c8 | -1.67887 | -52.44105 | 2024-11-27 05:35:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 49cf61c7-01d4-30ef-8e8e-20298bc00ab9 | -1.98701 | -53.29613 | 2024-11-27 05:35:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| ec791324-e7af-3e49-a774-ee9dc7fb68d3 | -1.2754 | -54.54705 | 2024-11-27 05:35:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 93bce709-18d7-31cd-b772-253b0d9848d0 | -1.48806 | -52.52238 | 2024-11-27 05:35:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 86eb3bff-9c92-32ef-94d8-f33a178642d3 | -2.76845 | -52.90419 | 2024-11-27 05:35:00 | NOAA-21 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1d3f79ac-ef4e-379f-8399-71254b91a662 | -3.28713 | -51.11778 | 2024-11-27 05:35:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| ffedc2ca-30a3-3912-b671-ade116f5d074 | -3.09817 | -53.25622 | 2024-11-27 05:35:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 32.3 |
| 375aa2c6-096e-33a4-9cfa-0e3a7992fe4f | 0.64699 | -50.82862 | 2024-11-27 05:35:00 | NOAA-21 | ITAUBAL | AMAPÁ | Brasil | 1600253 | 16 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 96f64665-faef-3d18-a359-1ef95f48238e | -1.35991 | -54.63223 | 2024-11-27 05:35:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 8132f92f-507e-3c41-9f78-5c80617379dc | -2.60799 | -53.97307 | 2024-11-27 05:35:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| f8efe40b-a38c-351d-85f2-df33c8c8ac67 | -2.79854 | -52.90906 | 2024-11-27 05:35:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| f8852a33-37b9-357e-b596-6582dfd03710 | -2.23304 | -53.68505 | 2024-11-27 05:35:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 0e2c6393-4b9e-3662-aedd-8147809865c9 | -3.51397 | -50.31257 | 2024-11-27 05:35:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| ae263d3c-0cbe-3924-a11b-2e6d43932211 | -3.11504 | -53.25908 | 2024-11-27 05:35:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 80beac4a-59be-3296-805d-05dec0f85939 | -2.80413 | -54.13369 | 2024-11-27 05:35:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 148ca9f3-1285-3452-bba3-9863e7c748fc | -3.11561 | -53.25519 | 2024-11-27 05:35:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| c7c7d2c4-ebc5-3099-97c3-ec1582844c0f | -1.78897 | -52.73652 | 2024-11-27 05:35:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 0f7e9361-9aef-31e5-8182-1761c341e591 | -3.71079 | -51.80281 | 2024-11-27 05:35:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| a95ae496-0ca8-3438-8663-df142e31b634 | -3.72185 | -50.18859 | 2024-11-27 05:35:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 94fcfd27-ab35-344a-9d53-747719d4cf4c | -2.80894 | -54.13771 | 2024-11-27 05:35:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 5491bdab-d43f-39b3-92dd-b7f391d619c0 | -3.37962 | -50.11832 | 2024-11-27 05:35:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 5ab21325-a053-3bd9-a3a0-89f5e9a697e3 | -3.27222 | -50.61912 | 2024-11-27 05:35:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 9b28b8b4-4f49-34dd-bb27-1c0301bc6e61 | -2.83258 | -54.12466 | 2024-11-27 05:35:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 12.2 |
| c4439daf-a262-3af0-a372-fa538f4002d7 | -1.78837 | -52.74048 | 2024-11-27 05:35:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 559f7d26-bc70-38cf-8d62-c6d3d5ebca70 | -2.94133 | -54.78852 | 2024-11-27 05:35:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 78765f07-c9ec-34b7-8a37-17b005a72977 | -1.76788 | -53.62815 | 2024-11-27 05:35:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 52e0ed04-e9e4-33c7-b7d0-19ed53c3a68b | -2.24384 | -53.6262 | 2024-11-27 05:35:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| d0e65f87-bb15-3764-992e-ca0ec3ee1441 | -1.67819 | -52.4425 | 2024-11-27 05:35:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 7178fc53-1464-33aa-a90f-883276d84fd7 | -3.10267 | -53.26485 | 2024-11-27 05:35:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| af9a4d81-acc1-3613-9544-bebabfcb2303 | -3.45317 | -50.29114 | 2024-11-27 05:35:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 9752581e-ac8b-3010-a706-d9a1c1623175 | -1.6788 | -52.43837 | 2024-11-27 05:35:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 2fcd19d0-a351-354a-ace3-be2d9c18b2af | -2.97891 | -51.57715 | 2024-11-27 05:35:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 87a8e2e7-c794-3c17-8ed9-e4eec6a0b8ee | -2.09677 | -53.35635 | 2024-11-27 05:35:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| bbff3265-60dc-371f-97d5-5c3081eb1f91 | -3.06313 | -53.21908 | 2024-11-27 05:35:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 32249747-00c2-3cf8-ba94-ae53721b4bff | -3.69595 | -50.22499 | 2024-11-27 05:35:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 10.6 |
| 4ede14b3-1a3f-3ce6-bf78-228515301465 | -1.7684 | -53.62471 | 2024-11-27 05:35:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 48164be3-ee53-3d3d-abc3-87f9bcf2c107 | -2.17069 | -54.62887 | 2024-11-27 05:35:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| a35b6616-bec3-3c32-842c-439835337c7b | -2.73343 | -54.1361 | 2024-11-27 05:35:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 39d9f49e-2761-34b3-91e7-f0b55da283f8 | -2.59923 | -54.20935 | 2024-11-27 05:35:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 45e8ba3e-83f5-3397-9f5f-a4488b800b74 | -3.72877 | -50.18943 | 2024-11-27 05:35:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 0f98618f-7986-3b41-8572-d8335c772666 | -2.43844 | -53.89083 | 2024-11-27 05:35:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e73bd216-60b9-365c-a73f-b16634d0d1ad | -3.08912 | -54.12939 | 2024-11-27 05:35:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| e071f3d8-1da2-3f3f-afcc-2277e09b57ad | -1.34993 | -54.63039 | 2024-11-27 05:35:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 3dbd3903-edf6-3251-8e45-13b32ad1589b | -1.45359 | -52.59533 | 2024-11-27 05:35:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| cc3bd26d-70f5-3a19-b22a-3fe6bc804136 | -3.25225 | -50.61578 | 2024-11-27 05:35:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 8345c836-2186-3fe3-a143-67fd344a0268 | -2.94017 | -54.78811 | 2024-11-27 05:35:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 728ef530-b7ce-3893-bbe3-2f900e935066 | -2.69943 | -51.98433 | 2024-11-27 05:35:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 76e0af47-0f0a-3744-b927-9785aca41487 | -1.98752 | -53.29575 | 2024-11-27 05:35:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| a5f795bf-ac01-333e-b844-f2c7627d264e | -2.83745 | -54.12266 | 2024-11-27 05:35:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 15.4 |
| 1ca0a770-a039-3f73-a72f-74d2640f6d03 | -1.78325 | -52.73561 | 2024-11-27 05:35:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 0821be22-407f-39a6-b4dc-c61cbc88b8ef | -3.10323 | -53.26105 | 2024-11-27 05:35:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 14.7 |
| 16f7a310-a797-32f5-a200-cfaf5aa8310d | -2.79796 | -52.91306 | 2024-11-27 05:35:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| d1fcb5d0-af34-30c3-ab97-a1dd7739ed00 | -3.41005 | -53.20052 | 2024-11-27 05:35:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c52a0b88-feb7-325b-ac27-bcbca4af2ea6 | -2.24152 | -53.62942 | 2024-11-27 05:35:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2af0a34c-bbef-3399-81ff-75fffc055d7d | -2.83358 | -54.11811 | 2024-11-27 05:35:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| c18360d9-3409-3473-bcb0-fdb9ecb30d8c | -1.68817 | -52.61527 | 2024-11-27 05:35:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 85c152a7-5771-33db-9cc3-dc3e35c71aa9 | -1.66815 | -52.71011 | 2024-11-27 05:35:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 7b1a007e-f0a0-379e-8683-c1e105532003 | -3.3792 | -50.11738 | 2024-11-27 05:35:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| ddc621bb-cd48-3d78-a55d-e95f35ae8556 | -2.18146 | -53.77076 | 2024-11-27 05:35:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| d374a9d7-ada0-3203-bf0b-f8c5f4fcd5cf | -2.61057 | -54.24326 | 2024-11-27 05:35:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 131ed508-8608-3974-bb8b-7daa89cb7f16 | -1.79468 | -52.73744 | 2024-11-27 05:35:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| f9a1697a-279b-3709-aae3-ae65c0a28e12 | -3.31416 | -53.75169 | 2024-11-27 05:35:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f4d63e02-ee85-30ed-9af4-4900885647f2 | -2.10228 | -53.35723 | 2024-11-27 05:35:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| b7556701-7f11-3957-863c-3aadd33182dd | -2.83793 | -54.11937 | 2024-11-27 05:35:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 90a52b1c-ba52-3262-9551-cda82679c1af | -2.77552 | -52.90586 | 2024-11-27 05:35:00 | NOAA-21 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 13b0dc99-1990-30fd-a7ba-35e04fb95359 | -2.60215 | -53.9756 | 2024-11-27 05:35:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| eadb113f-6082-3fa3-86df-711348a6586b | -2.24927 | -53.62709 | 2024-11-27 05:35:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 45a287ab-3b95-3fb9-ab13-9c4b5d5e8c82 | -2.82923 | -54.10453 | 2024-11-27 05:35:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 1f339767-9598-3d5f-b602-46528ad92350 | -2.59783 | -53.96808 | 2024-11-27 05:35:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 1eda87a0-459a-331c-ad98-ed9101347e77 | -2.81738 | -54.76036 | 2024-11-27 05:35:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3e9d413c-62dd-3866-990d-e69555743f7e | -1.65714 | -55.23757 | 2024-11-27 05:35:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c7b471c5-7710-34cb-a37b-ae12b858c9c0 | -3.30746 | -53.75215 | 2024-11-27 05:35:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 6e30d7d8-c3c3-337d-b7e0-5760a1868321 | -3.7211 | -51.80497 | 2024-11-27 05:35:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 4562236f-5133-35a4-95bc-ab8f167ffe64 | -3.23903 | -50.67974 | 2024-11-27 05:35:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |


[Clique aqui para ver as próximas entradas](README77.md)
