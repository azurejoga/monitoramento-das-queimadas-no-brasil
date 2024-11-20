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

## Dados Diários - Página 66

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 365d9c94-9593-30b6-ba7f-60ff66d4fe53 | -2.13738 | -48.56727 | 2024-11-20 05:14:00 | NOAA-20 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 15.8 |
| d377af07-4869-3280-8d1c-8f652e800abf | -2.56178 | -54.07415 | 2024-11-20 05:14:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 256c96e9-1d8f-34fe-afbd-677843850685 | -3.13842 | -49.12976 | 2024-11-20 05:14:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| e5458fc4-6779-377f-a356-8f4537207703 | -1.43778 | -53.37975 | 2024-11-20 05:14:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7cfe1854-9770-3fc3-94e0-340e38bde971 | -6.24257 | -47.27457 | 2024-11-20 05:14:00 | NOAA-20 | CAMPESTRE DO MARANHÃO | MARANHÃO | Brasil | 2102556 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 00160430-1a99-39ea-96f9-04a949984f7c | -1.64461 | -52.60514 | 2024-11-20 05:14:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| cb074429-7be3-3f19-aa98-308906dea2c8 | -1.10969 | -51.75485 | 2024-11-20 05:14:00 | NOAA-20 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 8376609b-4dd6-3f85-86c3-67b6e0097cde | -3.2814 | -53.83253 | 2024-11-20 05:14:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 6f95ce80-e645-3080-a5c2-0fa2f51fa554 | -6.2468 | -47.27296 | 2024-11-20 05:14:00 | NOAA-20 | CAMPESTRE DO MARANHÃO | MARANHÃO | Brasil | 2102556 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 9ae13cc6-1e66-3cb4-835f-fee8ea7c7b43 | -1.24281 | -51.75142 | 2024-11-20 05:14:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d243d109-5686-3775-a297-653e493a4bc8 | -1.06139 | -52.39425 | 2024-11-20 05:14:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ecd2b1d1-aace-3386-9aa8-2722d53fb670 | -2.74184 | -54.11197 | 2024-11-20 05:14:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 44867cdb-af60-3058-9b1f-6188d4f3618e | -3.18515 | -54.3238 | 2024-11-20 05:14:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 3dacb558-f455-389f-8358-b436660d116f | -1.14926 | -53.51397 | 2024-11-20 05:14:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 3d0eb632-4c82-3ab7-864b-b1e1e1cabb56 | -3.77346 | -52.00538 | 2024-11-20 05:14:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 02e73b63-eb1e-33eb-9f78-39316a6ef4b6 | -4.94063 | -50.6481 | 2024-11-20 05:14:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4cb2cf23-1191-3318-8848-fc9b0b404693 | -1.95689 | -53.31832 | 2024-11-20 05:14:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8ac8e2a6-3e04-3a37-aea1-c168e19757cb | -4.44313 | -46.58714 | 2024-11-20 05:14:00 | NOAA-20 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 15.2 |
| 4a23128f-694b-37a0-af82-baa7d7907c9d | -3.66901 | -54.27419 | 2024-11-20 05:14:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| c55ba3df-bd2f-3171-88bb-bab866b83652 | -2.79747 | -51.7967 | 2024-11-20 05:14:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| e87d6007-d6af-3328-b5fc-a010dec3d2bb | -3.76282 | -52.13889 | 2024-11-20 05:14:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| c22e1955-03fd-394c-97bc-1e096b4b6358 | -0.07978 | -51.46885 | 2024-11-20 05:14:00 | NOAA-20 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a2fd495f-ee8e-3fa1-a9a4-dfa3b63692ef | -1.13396 | -53.666 | 2024-11-20 05:14:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 60945478-6259-3104-8684-408b15b4c8c8 | -2.8994 | -53.05529 | 2024-11-20 05:14:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| eb967852-f8fa-30f6-8e4a-84271bb8d884 | -6.24952 | -47.2706 | 2024-11-20 05:14:00 | NOAA-20 | CAMPESTRE DO MARANHÃO | MARANHÃO | Brasil | 2102556 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| d7d5d650-7c50-352c-8633-57055c557f8a | -2.12727 | -48.53143 | 2024-11-20 05:14:00 | NOAA-20 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 71851e23-41ba-3ed4-8644-aa5f1d27ed91 | -2.62098 | -54.26685 | 2024-11-20 05:14:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ee5abdcf-8e4d-3832-95f8-9860c14f1994 | -1.27985 | -55.68126 | 2024-11-20 05:14:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 7f35514f-6d9d-3bf7-b333-b05722f6897b | -4.13663 | -47.73464 | 2024-11-20 05:14:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| bb65d97c-2c09-30b7-bda3-0a4ada432fd5 | -2.79371 | -51.79187 | 2024-11-20 05:14:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| e959d441-c3e2-35b9-af72-ad01c13a6cf4 | -2.70949 | -53.17672 | 2024-11-20 05:14:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| f2ad6573-1b43-31d2-a851-63d6579e3ac6 | -3.04001 | -49.46791 | 2024-11-20 05:14:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 804be9e1-6c93-3178-b161-9a1dd0160544 | -3.18211 | -54.31868 | 2024-11-20 05:14:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 5d607ffa-cebb-3fc8-92fd-0114e9c5fea1 | -2.62942 | -54.28645 | 2024-11-20 05:14:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 1d62829a-8839-3584-90ee-6f05faa42eb3 | -1.66135 | -52.65966 | 2024-11-20 05:14:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a1fa7c4d-e4d6-38f1-b1fd-84f17dd5fee4 | -1.78998 | -53.61262 | 2024-11-20 05:14:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| dd5cf49e-c2a0-39a8-9c82-1cd2f264d606 | -1.68489 | -55.02885 | 2024-11-20 05:14:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 97e80461-0bc5-361a-a9d3-455322d3b9b4 | -1.10761 | -51.75698 | 2024-11-20 05:14:00 | NOAA-20 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 5b7036b1-0423-3feb-af5f-b5b4f29b59cf | -0.77856 | -51.75948 | 2024-11-20 05:14:00 | NOAA-20 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f6aa89bc-263a-306e-8a60-904ca3bae52d | -2.21524 | -48.77472 | 2024-11-20 05:14:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c8a2def2-4a21-32fb-aaaf-1e4fb09805ad | -3.52925 | -54.68201 | 2024-11-20 05:14:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 35879581-32ca-31e6-ab16-73568bc47c24 | -1.2237 | -51.79013 | 2024-11-20 05:14:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 8d043653-7e52-34d0-9125-5b1db5f3c749 | -1.20347 | -51.76334 | 2024-11-20 05:14:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 5c822206-52a4-380f-929c-128569186b72 | -2.9294 | -48.33517 | 2024-11-20 05:14:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 124acbc8-098d-37f1-8f80-1974931caf49 | -2.05901 | -53.43723 | 2024-11-20 05:14:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| dc0032b8-c686-3db7-957d-4873234186d9 | -1.60365 | -52.24748 | 2024-11-20 05:14:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 0cd5f042-da19-3d67-b79f-ced96d7c6b52 | -4.44951 | -46.58811 | 2024-11-20 05:14:00 | NOAA-20 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 15.2 |
| 4a73a95a-1d01-3be9-b48f-3be69147e784 | -2.81679 | -54.02898 | 2024-11-20 05:14:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 91e0cda6-0c1f-3d1d-acee-97cf545e700a | -2.26619 | -45.4592 | 2024-11-20 05:14:00 | NOAA-20 | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9a227127-3e90-3c9a-81b6-4d3d881d41ba | -1.2262 | -51.74473 | 2024-11-20 05:14:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 1b8c907d-b2a3-3f08-8ca6-3c5183a31d81 | -2.0198 | -52.41067 | 2024-11-20 05:14:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 2e2ba67a-9017-3d65-bf0c-1fed0b120611 | -1.81779 | -52.69798 | 2024-11-20 05:14:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 102230ca-f389-3c03-8697-5e12e61b52b1 | -6.36338 | -55.36453 | 2024-11-20 05:14:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d6427f22-11b3-37b7-81ea-687b72e7242a | -1.66494 | -54.90345 | 2024-11-20 05:14:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 530b3fd3-d0a2-3cfd-9e84-a589888652f3 | -1.33531 | -52.24429 | 2024-11-20 05:14:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 7316bdf1-c965-309f-ad33-94bb71dcec79 | -1.43704 | -53.38457 | 2024-11-20 05:14:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| fd068ef6-a11e-3636-b588-5030af233aa1 | -1.54718 | -51.11185 | 2024-11-20 05:14:00 | NOAA-20 | MELGAÇO | PARÁ | Brasil | 1504505 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c1043f86-c03e-334b-8f6e-804d7881dc2f | -1.62959 | -52.62143 | 2024-11-20 05:14:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e307d48d-2199-32d4-97d2-a7faf2bcf075 | -1.04482 | -53.51489 | 2024-11-20 05:14:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b16984e3-a3a9-3fb4-9d8c-8d0c17c92c83 | -0.03069 | -51.11456 | 2024-11-20 05:14:00 | NOAA-20 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3ef9110e-a336-323a-84a7-9dc065cf6c95 | -3.66139 | -54.32461 | 2024-11-20 05:14:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 770d183a-365c-3bc3-8824-f143960bc4e7 | -0.94511 | -51.72252 | 2024-11-20 05:14:00 | NOAA-20 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 2.5 |
| b687f920-787e-3999-8444-dbcf3686d787 | -3.51603 | -53.79946 | 2024-11-20 05:14:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 4ed411fe-01f6-32e2-b9d9-6821ad66ac02 | -1.60359 | -52.41398 | 2024-11-20 05:14:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 938bd2b7-0065-3341-9361-b5c5fee7fd7d | -1.30257 | -52.26257 | 2024-11-20 05:14:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 31e2b7d9-b51b-3667-939c-dde47db52a86 | -1.33173 | -52.23988 | 2024-11-20 05:14:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 915372b3-86a6-30a8-9a5d-f3c69c73ddb1 | -2.70892 | -51.99776 | 2024-11-20 05:14:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| c2e1d45b-3b46-3fd2-b394-98e82a341bc5 | -3.05227 | -54.40636 | 2024-11-20 05:14:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 21a01331-5efe-3f31-9232-7512f3a303fc | -1.34843 | -55.73764 | 2024-11-20 05:14:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 21c7cf13-0de1-3e8b-98f2-009ebf65eece | -3.45637 | -53.30103 | 2024-11-20 05:14:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 9c13835c-b2dc-3975-bc03-3d059e86e534 | -2.57558 | -48.39382 | 2024-11-20 05:14:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 22cec5b4-032a-393c-9dd3-e37b99ca8af4 | -2.91505 | -53.06125 | 2024-11-20 05:14:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 488fc448-ba43-38c4-9383-425ccd352837 | -4.38605 | -47.76032 | 2024-11-20 05:14:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| f3c545ab-00c4-3dea-bd17-25d62bccb7b4 | -2.84669 | -54.0073 | 2024-11-20 05:14:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 11b4587f-b010-3013-952f-76fc1d09fefe | -1.27233 | -52.12495 | 2024-11-20 05:14:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 6b552ec4-b1c6-3610-b46b-ad351f6c6b14 | -1.25753 | -51.77037 | 2024-11-20 05:14:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 08c70a26-75ce-37ad-b135-158d869c71f1 | -1.86118 | -47.8278 | 2024-11-20 05:14:00 | NOAA-20 | SÃO DOMINGOS DO CAPIM | PARÁ | Brasil | 1507201 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 1148804c-8d84-3463-ab1b-02f6e2bf0f7f | -1.99574 | -46.61063 | 2024-11-20 05:14:00 | NOAA-20 | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| b5d69f0d-33b2-3774-89a1-9ac78925e9bd | -0.94082 | -51.72186 | 2024-11-20 05:14:00 | NOAA-20 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 2.5 |
| dc18dbff-bd6a-39a7-9673-7c865e830405 | -1.20906 | -51.75584 | 2024-11-20 05:14:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2b378093-ead6-39bd-a5fc-2fb38f5ed5cf | -3.56173 | -45.01571 | 2024-11-20 05:14:00 | NOAA-20 | VITÓRIA DO MEARIM | MARANHÃO | Brasil | 2112902 | 21 | 33 | nan | nan | nan | Amazônia | 21.6 |
| 0fceff01-805d-3934-9bb1-2a294c9bfcd9 | -1.29477 | -52.23029 | 2024-11-20 05:14:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 00b761aa-f483-305e-8178-c52d1892ee78 | -3.80697 | -47.79897 | 2024-11-20 05:14:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| cd46e015-7ff3-3d01-9b08-060434b313e1 | -1.68428 | -55.03286 | 2024-11-20 05:14:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 5387aca4-301a-3da9-9baa-57839aa2bcae | -1.374 | -52.08093 | 2024-11-20 05:14:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 86d955b3-77c0-39e1-b00c-f4d269c37c02 | -1.14961 | -53.52158 | 2024-11-20 05:14:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| a87cf7eb-0aec-302c-9313-accf7e2d1ceb | -1.24294 | -53.36644 | 2024-11-20 05:14:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 2cde92ee-a21c-35c8-9e9b-c62b59ace162 | -4.06465 | -46.85083 | 2024-11-20 05:14:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 75c48040-65c7-3c51-9ee2-a83401aabeac | -2.20314 | -53.70665 | 2024-11-20 05:14:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| de150ffb-c962-3992-94d9-0140f7537a0b | -2.13139 | -48.53415 | 2024-11-20 05:14:00 | NOAA-20 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0ed0d1e1-d944-35ad-bcad-5c73ab187482 | -2.05586 | -53.4317 | 2024-11-20 05:14:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| f899b43b-2de5-3eeb-851e-242dbe9657f8 | -1.7049 | -52.48652 | 2024-11-20 05:14:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 7de13b77-f033-3c77-b417-721b08d55006 | -2.53778 | -54.30154 | 2024-11-20 05:14:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d35e1659-5621-3375-a6cb-22e29f8ffe0d | -1.47301 | -53.48382 | 2024-11-20 05:14:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 48c8684c-6c8e-31ec-b8e1-6fd578981351 | -4.00338 | -54.34103 | 2024-11-20 05:14:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| acfc3243-5170-3967-a5ca-05627d9af7d1 | -5.38099 | -50.47548 | 2024-11-20 05:14:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 113283da-a174-3929-85a2-94bec1426a73 | -4.44242 | -46.59227 | 2024-11-20 05:14:00 | NOAA-20 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 12.8 |
| c055397e-c70d-36f1-a792-0c218ab8f266 | -2.71963 | -49.34949 | 2024-11-20 05:14:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 4b366937-bbeb-3c55-bc54-65d11eed53fe | -2.89591 | -53.05103 | 2024-11-20 05:14:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 54502df5-6da0-3a59-8c3b-155b2527b7db | -1.64283 | -52.67159 | 2024-11-20 05:14:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |


[Clique aqui para ver as próximas entradas](README67.md)
