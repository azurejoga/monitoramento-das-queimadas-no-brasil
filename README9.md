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

## Dados Diários - Página 9

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 91a5a146-0ab0-3d74-9683-108e5855e772 | -10.76282 | -46.94584 | 2026-05-30 04:55:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 9d43c1e5-b0d3-3b0e-a63e-b95a43bb35da | -10.19124 | -49.10669 | 2026-05-30 04:55:00 | NOAA-20 | CHAPADA DE AREIA | TOCANTINS | Brasil | 1704600 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 14c24e6a-d02e-3806-a0a3-34b59565662d | -11.58947 | -47.45387 | 2026-05-30 04:55:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 5.6 |
| a5f5cc2e-ad73-31cd-9545-adf5cbec7503 | -9.46251 | -57.84871 | 2026-05-30 04:55:00 | NOAA-20 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 369f869e-c733-3989-9f5e-3f4719692c2b | -10.77997 | -48.54373 | 2026-05-30 04:55:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| c04560d1-b2ab-395a-913d-80436f6b58ea | -12.80402 | -54.86971 | 2026-05-30 04:55:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 64441e03-19b2-378d-bbef-55d11178c27b | -10.77258 | -46.97438 | 2026-05-30 04:55:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| b361d9c6-48a8-33cf-b92e-54c9cc9cc0ef | -10.73136 | -49.02166 | 2026-05-30 04:55:00 | NOAA-20 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| b62de541-99d6-38ca-b2a0-402ced5a031f | -9.76549 | -48.7526 | 2026-05-30 04:55:00 | NOAA-20 | BARROLÂNDIA | TOCANTINS | Brasil | 1703107 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 4501a1dd-4ed8-353f-a741-b6cdcaf75490 | -11.58444 | -47.4579 | 2026-05-30 04:55:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 5.6 |
| c0489abc-efe7-39c8-ba70-e4e9fef91f55 | -10.7673 | -46.94646 | 2026-05-30 04:55:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 894207cd-a56f-32be-accd-bf65ad7d064d | -10.06012 | -49.11701 | 2026-05-30 04:55:00 | NOAA-20 | MONTE SANTO DO TOCANTINS | TOCANTINS | Brasil | 1713700 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| fdf8b861-3e9b-3551-8d3a-cb9af29073dc | -14.13163 | -58.93402 | 2026-05-30 04:55:00 | NOAA-20 | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 274fcae6-c926-3aa2-b0d7-20fcb515724a | -14.06324 | -53.37018 | 2026-05-30 04:55:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 6fa6cb5e-61c0-39c7-aa47-7abadb0be5af | -10.80253 | -46.95579 | 2026-05-30 04:55:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| cf7d68ca-a2c4-31d0-b3b0-c539ef2c57b7 | -10.57478 | -48.02498 | 2026-05-30 04:55:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 92c480a4-55bd-3b87-beb5-c77d31b7f808 | -11.59643 | -47.43915 | 2026-05-30 04:55:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| f811e75f-4fab-3de1-8ff4-e314d8aefb48 | -8.72643 | -47.84125 | 2026-05-30 04:55:00 | NOAA-20 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| e9cb68a5-9e1d-3b2f-a941-df4d8697b568 | -10.8436 | -46.9418 | 2026-05-30 04:55:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 23.2 |
| 37893e63-d988-33ae-b798-37ebd255aef5 | -10.62844 | -48.32634 | 2026-05-30 04:55:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 1bcba791-a81a-335b-8fb7-c62c91dde54c | -10.78387 | -46.92572 | 2026-05-30 04:55:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 033d8d81-b5cb-3c12-8228-af83bf53fd81 | -14.1364 | -58.92962 | 2026-05-30 04:55:00 | NOAA-20 | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b8940bab-1791-37d2-83a1-f7232c0ab670 | -15.58179 | -46.81133 | 2026-05-30 04:55:00 | NOAA-20 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 90d42b47-12e2-32ff-ae37-981a5b1cc2b1 | -10.73048 | -49.0242 | 2026-05-30 04:55:00 | NOAA-20 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| cd7ec425-9ce9-35f2-9ed8-7ada6314fb1f | -9.36608 | -48.41548 | 2026-05-30 04:55:00 | NOAA-20 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c01263a9-76d4-30f8-b553-2fef5bf5098c | -8.408 | -49.60386 | 2026-05-30 04:55:00 | NOAA-20 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 152d6218-abe6-3532-a6fa-fa216dfc62c9 | -10.79746 | -46.95943 | 2026-05-30 04:55:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 534b00d5-59be-3e7a-a947-7b450c3d6468 | -9.45862 | -57.84803 | 2026-05-30 04:55:00 | NOAA-20 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 36bc205d-83c0-3b0d-a76d-f612d5c4be87 | -11.76085 | -47.05971 | 2026-05-30 04:55:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 89a4c4f5-b1d4-35a3-a001-8b82ac180519 | -10.77503 | -46.9566 | 2026-05-30 04:55:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c38dddd1-bd5a-3ea1-9f55-4aa7c1ee4f16 | -12.68042 | -54.58314 | 2026-05-30 04:55:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 087b3ff2-ceec-3d39-9ae4-7d33d4786da3 | -12.6843 | -54.58015 | 2026-05-30 04:55:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 0edec3f7-2311-3dd8-8332-ad89d5b6aea0 | -9.45003 | -51.8283 | 2026-05-30 04:55:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2352cdaa-b384-336a-a241-ac9f7e29fcc5 | -11.6284 | -56.86181 | 2026-05-30 04:55:00 | NOAA-20 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 96610509-7787-3d3d-8745-1de7ed1c653e | -10.80145 | -46.94955 | 2026-05-30 04:55:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b1df3a47-936f-3baa-8ba0-c148cfd8aaea | -10.80375 | -46.94704 | 2026-05-30 04:55:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 7f911015-e1af-3ad7-bb9c-b3a86a762322 | -10.83889 | -46.90881 | 2026-05-30 04:55:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 87394d25-b52c-3388-802a-ec6061049bd6 | -12.8046 | -54.86614 | 2026-05-30 04:55:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| add94a92-ae81-3ad7-895e-9c7b16f083d4 | -11.75894 | -47.07355 | 2026-05-30 04:55:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| ab8ea529-d93b-3b22-be99-93895c787689 | -9.247 | -60.33535 | 2026-05-30 04:55:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b33ba42c-6ac7-3746-8f9a-15b39bc82471 | -10.77442 | -46.96105 | 2026-05-30 04:55:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 9fbb3061-bcb9-3089-a68b-c5af242f6f1b | -10.84607 | -46.92348 | 2026-05-30 04:55:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 4.8 |
| a825abf7-d004-331d-9190-f40a08772627 | -11.59567 | -47.44141 | 2026-05-30 04:55:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 3e57ffd2-aaed-39bd-a0f5-afed41df4a9d | -9.45059 | -51.82468 | 2026-05-30 04:55:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 53b5824a-e8f5-3ad4-9cb0-0fae7b795406 | -10.96948 | -48.31871 | 2026-05-30 04:55:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 3839a1e6-584d-3a63-8469-06012e443f39 | -9.80129 | -48.92142 | 2026-05-30 04:55:00 | NOAA-20 | BARROLÂNDIA | TOCANTINS | Brasil | 1703107 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 4988ee14-c1d1-3f4b-8bb4-93c6a11e931d | -10.76343 | -46.94139 | 2026-05-30 04:55:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| b8077072-dc70-378e-afe7-9689c0b50e7e | -15.30743 | -47.3806 | 2026-05-30 04:55:00 | NOAA-20 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 64c43449-1c5e-36f9-bf4e-a719c0987539 | -9.17586 | -48.62356 | 2026-05-30 04:55:00 | NOAA-20 | FORTALEZA DO TABOCÃO | TOCANTINS | Brasil | 1708254 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 368ebf64-9efa-3836-8ceb-7e5804a3d39b | -10.63532 | -49.72977 | 2026-05-30 04:55:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| fd661109-759a-3a77-b59d-0c8772c8ba0c | -10.57424 | -48.02888 | 2026-05-30 04:55:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 0.2 |
| 5010320d-16b6-3f2b-bef9-7ec547150b4d | -10.14076 | -48.07577 | 2026-05-30 04:55:00 | NOAA-20 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 4cfa4591-039c-3f73-9170-a4409d95e979 | -9.44722 | -51.82416 | 2026-05-30 04:55:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 476b283d-17e3-3a64-9789-e4e80edc80ca | -11.80243 | -57.00985 | 2026-05-30 04:55:00 | NOAA-20 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 8e0f7f06-12ea-3aa0-850b-ed29b99c2cff | -11.54154 | -46.42994 | 2026-05-30 04:55:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 1a25e4bf-5885-3f53-9d34-4262593fd87f | -11.63128 | -56.8666 | 2026-05-30 04:55:00 | NOAA-20 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 5.4 |
| c72213f7-7a83-303e-b29b-3d4d2f971075 | -10.63819 | -49.72735 | 2026-05-30 04:55:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| fe271059-c7e8-3510-bfec-52c2817c4d57 | -10.77034 | -46.92432 | 2026-05-30 04:55:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 33cae34c-d580-3905-9c73-b4bbe89c010a | -10.77319 | -46.96995 | 2026-05-30 04:55:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| b2c84b26-cd72-398d-b79b-090ce86a1187 | -10.77952 | -46.95715 | 2026-05-30 04:55:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| cfab143f-b704-39bb-b831-b26ee54ebeb9 | -10.80204 | -46.94512 | 2026-05-30 04:55:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 80210fe6-6dd9-34e9-90a6-8c2a5e8f6819 | -11.16357 | -46.78537 | 2026-05-30 04:55:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| fef202d0-51c4-3999-b1c5-437accf5e70d | -11.54217 | -46.42512 | 2026-05-30 04:55:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 4fd949ef-edce-3ccb-927a-af35693584a8 | -10.63302 | -48.32327 | 2026-05-30 04:55:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 61e7f6ce-2da0-354d-a75a-3e8dcd4e2f07 | -12.52213 | -57.21376 | 2026-05-30 04:55:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 7efe7140-7367-3003-b2da-efec5f9da546 | -10.75735 | -46.98571 | 2026-05-30 04:55:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e1cc2900-1df3-3282-b94b-af3f6f2107bc | -10.7738 | -46.9655 | 2026-05-30 04:55:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 6e9cb22e-19e2-36a1-8300-d25fc0f17017 | -11.59068 | -47.44516 | 2026-05-30 04:55:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 636597dd-bb01-3b67-b33a-58ba4b3fcc03 | -9.4013 | -48.45244 | 2026-05-30 04:55:00 | NOAA-20 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 4cf7a3f3-2444-3535-8945-ef71fae2f58d | -8.40736 | -49.60818 | 2026-05-30 04:55:00 | NOAA-20 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| dc01e6f0-18a1-3a86-8179-7dfb67bdafcf | -9.92671 | -48.68693 | 2026-05-30 04:55:00 | NOAA-20 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 10.7 |
| 6c20bb69-6abd-39d1-8213-273c698d8d32 | -10.76466 | -46.93241 | 2026-05-30 04:55:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 0dad36a4-78a5-3627-8039-59fe5dd1cc92 | -10.03872 | -52.10007 | 2026-05-30 04:55:00 | NOAA-20 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ea3212c9-fefb-338e-8fdd-d923ece3d1e5 | -11.5851 | -47.45321 | 2026-05-30 04:55:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 3e9dcf4d-884d-3d4c-8f17-623448c000e3 | -10.84241 | -46.95064 | 2026-05-30 04:55:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 16.8 |
| 4dc7c51c-2d4c-3ca9-831a-dcde840059a7 | -8.72751 | -47.83389 | 2026-05-30 04:55:00 | NOAA-20 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 1f3a92f6-8e7e-3261-a581-572b5c69b36f | -9.44665 | -51.82777 | 2026-05-30 04:55:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5f3e7f3b-4873-3ba7-aa5b-3758d755c3d8 | -9.37276 | -50.54707 | 2026-05-30 04:55:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2204a527-3ead-3e27-a705-b526aaece9f5 | -10.77093 | -46.91999 | 2026-05-30 04:55:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 770d62b8-7f1c-301e-ba98-266462c9130e | -12.00449 | -45.35727 | 2026-05-30 04:55:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 9e0a99bf-3fbd-390e-b150-3a126d54fd7f | -10.78076 | -46.94817 | 2026-05-30 04:55:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 4df4dec6-9721-3f40-b2e7-ba7532e0937b | -9.18126 | -49.36731 | 2026-05-30 04:55:00 | NOAA-20 | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ada2710b-98bc-3525-846c-5ebae4c62ee4 | -11.76669 | -47.06281 | 2026-05-30 04:55:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| fd4082d2-1c98-3b80-b5a0-f58fa98e8516 | -9.24785 | -60.33064 | 2026-05-30 04:55:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 92ea47ef-8dca-3d09-8bb0-c56e2cfe8b60 | -11.60082 | -47.43974 | 2026-05-30 04:55:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 1a350e3f-68ed-3ac3-b649-e917220ef639 | -11.99654 | -47.76584 | 2026-05-30 04:55:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 40b87b57-4c60-3258-ad5e-9a226066fb63 | -10.75919 | -46.97234 | 2026-05-30 04:55:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 871f17f2-3da2-3492-98ea-2796afd39b22 | -11.80315 | -57.00561 | 2026-05-30 04:55:00 | NOAA-20 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 50f13c01-e361-3fbb-98be-dc4b6b17199f | -11.90668 | -43.83064 | 2026-05-30 04:55:00 | NOAA-20 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f487b506-6793-3d59-889f-eaac19b2ef15 | -10.50338 | -48.09753 | 2026-05-30 04:55:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ac099b6e-58be-33eb-bf48-6a096ee3782c | -10.81583 | -46.89346 | 2026-05-30 04:55:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 29c344c9-560a-31c5-b3b5-e5ebd6b6f66d | -9.45216 | -51.82433 | 2026-05-30 04:55:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 6.8 |
| a8880b2a-f574-3d07-aaba-28a437dc9383 | -14.05655 | -53.3691 | 2026-05-30 04:55:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 2c5d16a6-1e85-3f84-82b1-992b0c959db6 | -11.5857 | -47.44888 | 2026-05-30 04:55:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 8.3 |
| eb609829-6c96-3acf-8335-f92e28d7d78d | -10.76976 | -46.92857 | 2026-05-30 04:55:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 60d9faa6-4cf7-37c6-8992-f6f2e7d54e1b | -10.76569 | -46.99128 | 2026-05-30 04:55:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 82151442-5c93-374e-95c4-7a9bd10030b1 | -10.81194 | -46.88846 | 2026-05-30 04:55:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| effda474-9f73-36ef-a7b7-04be4292ff00 | -11.6291 | -56.85765 | 2026-05-30 04:55:00 | NOAA-20 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 27033b81-22c4-34fa-9962-048a558e5d2c | -10.79237 | -46.96318 | 2026-05-30 04:55:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| aa212c20-765e-3704-b75e-ebffe8e57979 | -10.7663 | -46.98685 | 2026-05-30 04:55:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |


[Clique aqui para ver as próximas entradas](README10.md)
