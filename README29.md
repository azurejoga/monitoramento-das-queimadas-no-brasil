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

## Dados Diários - Página 29

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 9df5de36-e1f3-3e10-a4af-a86703efcfd7 | -5.08344 | -46.17797 | 2024-10-17 04:12:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 594656d2-77c1-3ccd-bc25-158610bc833d | -5.05544 | -45.86524 | 2024-10-17 04:12:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 562fc282-9d24-31bd-a6bf-2ac2e42ed5ad | -5.05478 | -45.8693 | 2024-10-17 04:12:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2a7bbd3d-0cde-3d8e-937a-def710c53a4d | -7.85131 | -46.2548 | 2024-10-17 04:12:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b44d2fc9-44d6-3ab4-8f58-15c5d9611a56 | -7.15158 | -45.43536 | 2024-10-17 04:12:00 | NOAA-20 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 6652f8ae-f3da-3b4a-8b80-9a088e9d9797 | -6.68506 | -46.37844 | 2024-10-17 04:12:00 | NOAA-20 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| c9101327-941b-3033-aef5-8380d8c348a8 | -7.39087 | -45.82883 | 2024-10-17 04:12:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 2f598056-d535-34d4-9777-8b3608839862 | -7.15503 | -45.43594 | 2024-10-17 04:12:00 | NOAA-20 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| a341e0c3-f4da-3335-b85e-e6ae7107fbb4 | -7.05924 | -45.53117 | 2024-10-17 04:12:00 | NOAA-20 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| affbefd9-4617-3485-807c-56127aef4e56 | -8.64217 | -45.61273 | 2024-10-17 04:12:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 3542dc99-4169-39d4-90b4-ac5306b62af9 | -8.71708 | -45.86283 | 2024-10-17 04:12:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| b576dc69-51eb-3774-8e47-15817a8312a1 | -8.41235 | -45.70875 | 2024-10-17 04:12:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| b0f368d4-f74d-3d4b-ac63-02d4453ce698 | -9.28445 | -46.24299 | 2024-10-17 04:12:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 5248221a-64dd-331a-9fed-32cfee5a2962 | -9.05709 | -46.4828 | 2024-10-17 04:12:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 4b7cd22d-8377-33bb-8b91-cac98b0f82fc | -8.21395 | -45.78676 | 2024-10-17 04:12:00 | NOAA-20 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f225c946-f3b6-3c94-889e-ad4d26523cd2 | -8.4089 | -45.70821 | 2024-10-17 04:12:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| adda9237-997d-3797-affb-196629d67656 | -8.6456 | -45.61329 | 2024-10-17 04:12:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 265060b2-0cd6-3412-a3d4-54ff61a3f489 | -8.2898 | -45.9889 | 2024-10-17 04:12:00 | NOAA-20 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| e1f4b628-be73-3d44-a2a5-753c3b75c2cd | -8.28631 | -45.98835 | 2024-10-17 04:12:00 | NOAA-20 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b56d0a8a-0289-3e70-aaab-200ca688afbe | -8.28282 | -45.9878 | 2024-10-17 04:12:00 | NOAA-20 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e8d574d6-9649-33b4-81c8-643bb1c6ef93 | -8.27997 | -45.98335 | 2024-10-17 04:12:00 | NOAA-20 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 41ffb9eb-9206-30e5-9338-54a5f1eed4b2 | -8.27933 | -45.98726 | 2024-10-17 04:12:00 | NOAA-20 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 77053fec-4ba2-3841-a151-daba75e40db6 | -8.27647 | -45.98282 | 2024-10-17 04:12:00 | NOAA-20 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 003c7509-15b7-39c6-8909-e401ac8c79b4 | -8.27298 | -45.9823 | 2024-10-17 04:12:00 | NOAA-20 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d2e441ae-e212-3c0c-b48c-a3ea04570fe4 | -8.21333 | -45.79059 | 2024-10-17 04:12:00 | NOAA-20 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 8af9fe57-5d65-3cb2-a5c3-4c772935f4a7 | -3.31685 | -47.01617 | 2024-10-17 04:12:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 28bfc03d-4194-3946-b0f6-9e145de1e95e | -3.25111 | -46.87597 | 2024-10-17 04:12:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 3a3b3129-6aa0-3de8-931a-83adb27507ef | -3.25032 | -46.88083 | 2024-10-17 04:12:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 5cdc5cd0-e42a-368d-9df0-cc57e9e1b0e4 | -3.24643 | -46.88018 | 2024-10-17 04:12:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 0f5e7529-7492-3e03-af2d-fb23d4831644 | -3.39763 | -47.06189 | 2024-10-17 04:12:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c5331c02-f831-3d91-83f3-b18840840475 | -3.31293 | -47.01554 | 2024-10-17 04:12:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2ba7b5cf-3b9e-3eb2-9796-a67bbd0ec029 | -4.55237 | -46.67107 | 2024-10-17 04:12:00 | NOAA-20 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 9.3 |
| 5037f9ba-8715-3016-b9af-cf69d334f269 | -4.54859 | -46.67052 | 2024-10-17 04:12:00 | NOAA-20 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 3.4 |
| dcbd818d-db6a-36c9-af68-32d137347873 | -4.54824 | -46.67281 | 2024-10-17 04:12:00 | NOAA-20 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 2.8 |
| adbaa4b3-5c50-30d6-beb1-02bfbc9c44f5 | -4.54707 | -46.67966 | 2024-10-17 04:12:00 | NOAA-20 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 29b0f28a-3ce2-32f1-b3b6-1fd82d9f19d4 | -4.84826 | -47.72718 | 2024-10-17 04:12:00 | NOAA-20 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 336b812e-a1f6-31ad-9e20-aa6284a2d39e | -4.72814 | -46.54438 | 2024-10-17 04:12:00 | NOAA-20 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e38acb3d-c906-3eb5-be2d-241ac8cd9f73 | -4.65645 | -46.29264 | 2024-10-17 04:12:00 | NOAA-20 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 38ceaa40-fa51-32bc-8617-402c54bef4bd | -4.55161 | -46.67569 | 2024-10-17 04:12:00 | NOAA-20 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 9.3 |
| 550212d9-8099-3c92-b12b-8cd6f27350d3 | -4.54783 | -46.67509 | 2024-10-17 04:12:00 | NOAA-20 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 3.4 |
| c5e36d5a-8bcd-3775-a217-2b47460c149a | -4.54751 | -46.67737 | 2024-10-17 04:12:00 | NOAA-20 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 2fa38f1e-4b9a-3ce7-b491-45c1c823807c | -4.36199 | -46.81666 | 2024-10-17 04:12:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 7b19f6c2-abb4-3109-b9c6-25553b6df3a4 | -4.36122 | -46.82138 | 2024-10-17 04:12:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 0a496260-36d7-3538-ab43-b87722d6b9b7 | -4.35818 | -46.81598 | 2024-10-17 04:12:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 3.3 |
| d9d12230-74db-3926-a0ff-cd2c0b349c38 | -4.35741 | -46.82073 | 2024-10-17 04:12:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 3.3 |
| fdb4fe19-6a0f-3506-9a10-c869d33251b8 | -4.3536 | -46.82006 | 2024-10-17 04:12:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 6398caad-f5fa-3878-b5f9-b9928b54263f | -4.33814 | -47.31227 | 2024-10-17 04:12:00 | NOAA-20 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 2.5 |
| ec5838af-c2dd-368a-bd1a-cb3f9ca3fe3f | -4.33733 | -47.31737 | 2024-10-17 04:12:00 | NOAA-20 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 2.5 |
| cf9d7e91-0bd3-3df8-9442-9d8b12f4a038 | -4.20547 | -46.4419 | 2024-10-17 04:12:00 | NOAA-20 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 785d610c-a89e-3426-be84-c923ee6f04f3 | -3.95885 | -46.43335 | 2024-10-17 04:12:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d90d2498-8db4-3c2d-990a-1de5db50723b | -3.95439 | -46.43707 | 2024-10-17 04:12:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| fce01eb8-3676-3ae2-8270-edf6c21a1dc7 | -3.93179 | -46.41051 | 2024-10-17 04:12:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a2a97b76-21e6-3f76-a00a-e039c40e942f | -3.93142 | -46.40811 | 2024-10-17 04:12:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 0ffbf803-314d-3d36-a9c3-7bd91008a1e5 | -3.85741 | -46.46091 | 2024-10-17 04:12:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 3d53c3cf-2b90-307e-a98b-04ff0668fef3 | -3.84124 | -46.927 | 2024-10-17 04:12:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 427a8c4c-845d-3058-badd-56ebc65545b2 | -3.82809 | -46.90984 | 2024-10-17 04:12:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a81c53a9-9e05-3be4-91ad-995b9eec6466 | -4.33718 | -47.31452 | 2024-10-17 04:12:00 | NOAA-20 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 6e8e4640-8676-37a3-a4c8-24e45899d4f3 | -4.32109 | -47.7103 | 2024-10-17 04:12:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 072c53f2-fd87-343b-b652-ed19e27d84fd | -4.13204 | -46.3909 | 2024-10-17 04:12:00 | NOAA-20 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6b4ba641-3d81-3fc2-8213-dbc90f28f1a9 | -3.95812 | -46.43784 | 2024-10-17 04:12:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d2229be2-0b0d-32fa-b9a5-762156dc0cbb | -3.95511 | -46.43266 | 2024-10-17 04:12:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 29c8af93-ed34-363a-9130-c38cc6e21381 | -3.93252 | -46.4061 | 2024-10-17 04:12:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c5b97c8b-5868-3d23-8f73-2e60eb78e898 | -3.91374 | -46.44661 | 2024-10-17 04:12:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 0f7ad679-f29f-33e5-be15-a4e5eade3998 | -3.83509 | -46.91577 | 2024-10-17 04:12:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1f1bb1cc-47fd-3d20-a852-47e022f10fd3 | -3.83121 | -46.91517 | 2024-10-17 04:12:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 986f7cc1-fa59-3786-85cf-337186abf727 | -6.295 | -47.02131 | 2024-10-17 04:12:00 | NOAA-20 | SÃO JOÃO DO PARAÍSO | MARANHÃO | Brasil | 2111052 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| d7fd92de-ac77-3d17-9229-6735b71f168d | -6.28672 | -47.02464 | 2024-10-17 04:12:00 | NOAA-20 | SÃO JOÃO DO PARAÍSO | MARANHÃO | Brasil | 2111052 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 4e7f94e8-3413-3875-b861-717eb09720b4 | -5.74956 | -46.50756 | 2024-10-17 04:12:00 | NOAA-20 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 6.0 |
| bf50d358-6ae1-3f13-a256-c53d065b759d | -5.74588 | -46.50697 | 2024-10-17 04:12:00 | NOAA-20 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 6f52953f-c8ea-3631-8694-e60b3d42ca76 | -5.72122 | -47.38677 | 2024-10-17 04:12:00 | NOAA-20 | GOVERNADOR EDISON LOBÃO | MARANHÃO | Brasil | 2104552 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 22ec83e5-bfa2-34b9-8039-4e5654b3e19d | -5.71971 | -47.39029 | 2024-10-17 04:12:00 | NOAA-20 | GOVERNADOR EDISON LOBÃO | MARANHÃO | Brasil | 2104552 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| a8849cf9-fcc9-3f6d-9aba-3e6284df4ced | -3.16417 | -48.37581 | 2024-10-17 04:12:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 32a4d085-21c8-33d6-a3b4-567cbbe8a9bc | -2.94994 | -48.61574 | 2024-10-17 04:12:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 35ab270c-35fd-3af0-b634-8d14e1c280ea | -2.91174 | -48.76459 | 2024-10-17 04:12:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| bb85a040-aa8b-3c8e-82d1-ddc9fe60f74d | -2.90819 | -48.76602 | 2024-10-17 04:12:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b0db8f52-28af-3712-984b-ea4a10df6447 | -2.9073 | -48.76389 | 2024-10-17 04:12:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 37b011ad-f980-3902-88d0-14864709432f | -3.69701 | -47.62361 | 2024-10-17 04:12:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| d23c3d85-debc-30e8-a002-6d86ea649fcd | -3.52216 | -48.06054 | 2024-10-17 04:12:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e378294d-ca89-3616-a019-d886118f64cf | -3.46394 | -47.67229 | 2024-10-17 04:12:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 14.0 |
| 116e1d68-6f00-300f-bddc-1aff7048bfbc | -3.21942 | -48.92335 | 2024-10-17 04:12:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 8.2 |
| e70ff196-3ede-3e07-9fd8-7447f5f07e14 | -3.21495 | -48.92266 | 2024-10-17 04:12:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 11.2 |
| 8f04b0f6-d92b-328c-8c9a-6c90e90dd662 | -3.16481 | -48.37178 | 2024-10-17 04:12:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8b6d1148-0b41-3678-b2de-977cbada07c6 | -3.11244 | -48.12878 | 2024-10-17 04:12:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c428a47f-5345-3673-af07-f937a881cd67 | -3.08285 | -47.78127 | 2024-10-17 04:12:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 74cfd053-3e74-3d61-9346-4bfc0cb83d25 | -4.58123 | -48.03049 | 2024-10-17 04:12:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 5807f93b-f375-3729-9f89-ec9109cbded4 | -4.57712 | -48.02976 | 2024-10-17 04:12:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 778741b4-03c2-34ca-a478-23df9b0f7901 | -4.57076 | -48.01723 | 2024-10-17 04:12:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 17.9 |
| d71b0491-6074-380f-98f7-f0eb1448e04f | -4.46655 | -48.12034 | 2024-10-17 04:12:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e6224ff4-6193-3fa1-af45-4ce3e444fa6f | -5.07255 | -48.28738 | 2024-10-17 04:12:00 | NOAA-20 | SÃO PEDRO DA ÁGUA BRANCA | MARANHÃO | Brasil | 2111532 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d8db686a-d5a6-3e6c-b562-ce6480b10eb5 | -5.07192 | -48.29116 | 2024-10-17 04:12:00 | NOAA-20 | SÃO PEDRO DA ÁGUA BRANCA | MARANHÃO | Brasil | 2111532 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b624c500-e51c-34a6-911a-8080f82a81b3 | -5.06777 | -48.29042 | 2024-10-17 04:12:00 | NOAA-20 | SÃO PEDRO DA ÁGUA BRANCA | MARANHÃO | Brasil | 2111532 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c0d346a5-2889-36eb-babc-960387ca1070 | -5.02268 | -48.03563 | 2024-10-17 04:12:00 | NOAA-20 | VILA NOVA DOS MARTÍRIOS | MARANHÃO | Brasil | 2112852 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| c5d741ef-c6e8-30df-a43c-ad8687984f99 | -4.5765 | -48.03355 | 2024-10-17 04:12:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e8aeb9b4-4213-337e-8663-f7bf0cbdb960 | -4.57486 | -48.01791 | 2024-10-17 04:12:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 17.9 |
| 04a873e7-c076-3929-be3e-868dbe48a317 | -4.47069 | -48.12101 | 2024-10-17 04:12:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 1e372cab-385b-39d0-b3fc-2e7ea6f345ba | -4.46593 | -48.1241 | 2024-10-17 04:12:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 6ae748d6-1930-32c1-8287-b0073bbdde80 | -4.35789 | -48.49314 | 2024-10-17 04:12:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| b8c9a745-3eae-3b90-8c7f-9dc2dffa47a6 | -4.35364 | -48.4924 | 2024-10-17 04:12:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| bff2677d-7efe-374d-866c-2eb51a1c8c44 | -4.32663 | -48.63288 | 2024-10-17 04:12:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| abfdb841-7548-3119-af8a-bac2ef075ff0 | -4.32555 | -48.62772 | 2024-10-17 04:12:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |


[Clique aqui para ver as próximas entradas](README30.md)
