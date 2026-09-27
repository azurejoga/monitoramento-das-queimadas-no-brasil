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

## Dados Diários - Página 28

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 0f191357-c5c2-33ad-9d3f-494383fabc8a | -8.34552 | -44.16461 | 2026-09-27 04:51:00 | NOAA-21 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| b4130ab0-be0c-3998-9ed6-ecf49b23e73a | -5.17852 | -46.11794 | 2026-09-27 04:51:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e412ad9b-7b13-3d58-b45b-92eb392fd4e0 | -4.47555 | -55.42756 | 2026-09-27 04:51:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 7ee52854-5bf8-3e04-b934-4f8cfeede328 | -3.45333 | -49.8189 | 2026-09-27 04:51:00 | NOAA-21 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 5fa97415-d62b-34eb-b10b-e28f02def814 | -4.54749 | -54.97472 | 2026-09-27 04:51:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 614271f0-d7f8-3847-8f43-3b5907147ea0 | -3.20262 | -51.03311 | 2026-09-27 04:51:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 11.5 |
| 18b529d2-45f8-3eda-965d-3b19d9c0f789 | -2.7971 | -57.69825 | 2026-09-27 04:51:00 | NOAA-21 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| caf135ae-898e-3c7e-86e2-b9ed7b1cbd1a | -2.92434 | -57.6622 | 2026-09-27 04:51:00 | NOAA-21 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 432a8034-d760-3044-b21d-f55b45a64a35 | -2.79352 | -57.69371 | 2026-09-27 04:51:00 | NOAA-21 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| b658e28b-31c8-301d-acc5-3b1352a9d2d4 | -7.70064 | -54.76063 | 2026-09-27 04:51:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 7c86b029-9a0b-3301-b24b-816d2d73c6ee | -3.87463 | -52.2885 | 2026-09-27 04:51:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 12376f69-2536-3c99-ae78-2b3802d0bad4 | -7.68886 | -54.74754 | 2026-09-27 04:51:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| e5401d43-5acc-3238-9e99-835d9ae1a3e4 | -4.49392 | -54.95048 | 2026-09-27 04:51:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 17.2 |
| d152975d-4731-3bb8-aa00-b92b3cd96c17 | -7.69387 | -54.75956 | 2026-09-27 04:51:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 6f9beec2-86c6-3fc7-af12-76ddebd5024d | -4.50506 | -54.94814 | 2026-09-27 04:51:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 001e4755-f5fc-370a-adc8-d1ec7a9db7d4 | -8.34811 | -44.18519 | 2026-09-27 04:51:00 | NOAA-21 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 15.7 |
| 08aa683a-98d7-3f60-8a04-84e9aa008e8c | -6.93043 | -42.86491 | 2026-09-27 04:51:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 60e796d4-48c8-30cc-ab0c-c51b8d27a9a7 | -8.09218 | -54.74486 | 2026-09-27 04:51:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 011bdce1-e9e3-3f58-b13f-efb02da58117 | -4.84108 | -42.89728 | 2026-09-27 04:51:00 | NOAA-21 | UNIÃO | PIAUÍ | Brasil | 2211100 | 22 | 33 | nan | nan | nan | Cerrado | 19.9 |
| feec4ddc-00fc-3f6a-9662-588c8bbeb17d | -1.84266 | -54.71729 | 2026-09-27 04:51:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 11.2 |
| 612f680e-c658-3258-b329-4dc85cef1125 | -4.54336 | -54.97812 | 2026-09-27 04:51:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 98cb71cb-7938-353a-95c1-74b6c6087743 | -4.58406 | -54.92485 | 2026-09-27 04:51:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| cf0bf306-f508-3194-8a22-b45f5b429584 | -2.44558 | -49.22773 | 2026-09-27 04:51:00 | NOAA-21 | MOCAJUBA | PARÁ | Brasil | 1504604 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 250659f1-e681-391e-9aec-0176f18bc4ea | -6.31191 | -43.33736 | 2026-09-27 04:51:00 | NOAA-21 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| ffd79732-80f7-3ab7-b275-2f6992ce72db | -6.8401 | -43.51005 | 2026-09-27 04:51:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 5e563401-1367-33c5-9620-4907a507897e | -6.02213 | -53.89018 | 2026-09-27 04:51:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a727fc3d-3792-3684-b512-8b70b507ffe9 | -7.35569 | -42.07738 | 2026-09-27 04:51:00 | NOAA-21 | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| bc2c5795-6a7b-3a06-ada3-bb567264ec5c | -5.01715 | -49.94099 | 2026-09-27 04:51:00 | NOAA-21 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 7ccfa873-e7a0-3995-8c6c-3717a9ea5829 | -2.79227 | -57.70148 | 2026-09-27 04:51:00 | NOAA-21 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 3.5 |
| afce30f1-7551-3e99-8358-c8ee95857dd9 | -8.03337 | -54.89633 | 2026-09-27 04:51:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| eb56d14b-2922-35c1-a02a-bce2d80d9160 | -9.27969 | -45.7887 | 2026-09-27 04:51:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 6f7113c4-0f6c-3ff5-8e13-fd390c3249e0 | -6.86611 | -59.87552 | 2026-09-27 04:51:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 5662606a-efa8-3b81-b553-131f9d69c8c1 | -3.0754 | -58.41247 | 2026-09-27 04:51:00 | NOAA-21 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6f8c90e4-90c2-3b31-8269-54a64691a5a4 | -9.93944 | -49.37107 | 2026-09-27 04:51:00 | NOAA-21 | DIVINÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1707108 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 4a137f7a-c24f-369e-9f70-7d271b32bb69 | -8.37417 | -44.14554 | 2026-09-27 04:51:00 | NOAA-21 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| ded9c9ea-fb07-3b10-a86c-bc6cea93a9ef | -4.46773 | -55.43054 | 2026-09-27 04:51:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 928d4999-1ff7-3877-8431-faf45fe159c7 | -2.06861 | -56.87422 | 2026-09-27 04:51:00 | NOAA-21 | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 0721edca-d903-3b89-80a1-c254394dc3e7 | -3.01225 | -54.20303 | 2026-09-27 04:51:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 24fc02eb-97c8-3ce3-89f0-a7bc40dcc252 | -4.17861 | -53.66863 | 2026-09-27 04:51:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 0dd79b2a-fde4-32c9-8bf3-7a9399335d97 | -7.191 | -46.50977 | 2026-09-27 04:51:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 0f29239e-f840-3b9e-a542-b2a5c245fd7f | -7.36842 | -42.1204 | 2026-09-27 04:51:00 | NOAA-21 | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 3.2 |
| 414c966a-c937-3a12-a722-bd5bf9fa36fe | -2.15429 | -51.9758 | 2026-09-27 04:51:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 70822ce8-1a1b-3612-ac7e-510661e47e00 | -4.55086 | -55.52265 | 2026-09-27 04:51:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 1edec778-8f97-30de-a7af-31b9464f6846 | -7.27444 | -55.57584 | 2026-09-27 04:51:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 45c38718-5a0b-30ef-b911-3eea406187eb | -2.8332 | -50.47525 | 2026-09-27 04:51:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 0d9c05e7-8323-33cd-81b8-71ee11d9d11d | -3.70189 | -54.19408 | 2026-09-27 04:51:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c6a7486e-0dab-35c4-a92c-0d32e902b591 | -2.97526 | -54.14744 | 2026-09-27 04:51:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 15d8f859-e97e-3715-9da3-3be2e1a1dee6 | -2.36624 | -50.34479 | 2026-09-27 04:51:00 | NOAA-21 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| fa7013a2-8b00-3d03-8534-9b8958c5fb2c | -6.05045 | -53.60257 | 2026-09-27 04:51:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| d8553607-85a7-3d69-a26b-e24c4f29efd0 | -4.53985 | -54.97759 | 2026-09-27 04:51:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| fde44e54-b900-3035-a46b-e881ab84e396 | -2.88187 | -54.07202 | 2026-09-27 04:51:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 44f25d4b-ac62-39d4-865e-27299836d022 | -2.84575 | -53.98996 | 2026-09-27 04:51:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1a7dc596-5d58-3e1e-8dec-ed8254d72c5c | -6.92718 | -42.86626 | 2026-09-27 04:51:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 01fa0dff-f2a4-3bb9-8c4c-c82e25ccbd6e | -2.92022 | -54.18543 | 2026-09-27 04:51:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b150e131-1d7a-34b6-b4b6-39a9168fdaa0 | -3.96199 | -48.1155 | 2026-09-27 04:51:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| ed34dae7-bea6-3a27-8fca-23da499a6eb8 | -2.06168 | -56.86584 | 2026-09-27 04:51:00 | NOAA-21 | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 5cc4990d-5863-306b-8f50-adecfe80733d | -3.01254 | -51.53387 | 2026-09-27 04:51:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 86775da2-13e5-3a1d-a4e2-04fc1302a758 | -4.29469 | -55.24224 | 2026-09-27 04:51:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a050069f-7e7d-3a79-b627-935a93141102 | -8.36539 | -44.17153 | 2026-09-27 04:51:00 | NOAA-21 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 158.1 |
| e765f2e1-bfe3-37c2-a6ff-ba19049da2c7 | -10.11904 | -45.12887 | 2026-09-27 04:51:00 | NOAA-21 | SÃO GONÇALO DO GURGUÉIA | PIAUÍ | Brasil | 2209757 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 56e5ee99-d92b-3fd9-bdf9-24ac36a75ff0 | -3.10355 | -49.3552 | 2026-09-27 04:51:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 473f9ab8-cbaf-3248-8ba0-ee45210a197c | -3.42619 | -50.42801 | 2026-09-27 04:51:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d74a92d7-e627-3344-9835-d09b4f2018b5 | -7.34039 | -42.07949 | 2026-09-27 04:51:00 | NOAA-21 | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| adda137b-dda9-39cd-b7a8-440d93f3712a | -2.5685 | -57.37369 | 2026-09-27 04:51:00 | NOAA-21 | PARINTINS | AMAZONAS | Brasil | 1303403 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| a5b5e0df-a09b-3ae5-a176-723b6012adfc | -5.74311 | -45.0603 | 2026-09-27 04:51:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 9161d035-44f3-3d99-b6b2-51dfab878ba7 | -5.57935 | -47.41503 | 2026-09-27 04:51:00 | NOAA-21 | DAVINÓPOLIS | MARANHÃO | Brasil | 2103752 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ece1e463-9946-3067-b028-a598c0ebd82f | -6.13889 | -53.06165 | 2026-09-27 04:51:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| bdd7683a-3d21-3fa0-8d1f-940e4a4a9a43 | -3.87516 | -52.28506 | 2026-09-27 04:51:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 30e92493-4ba5-3f7a-9eaa-40f8c29dc134 | -2.4503 | -49.22038 | 2026-09-27 04:51:00 | NOAA-21 | MOCAJUBA | PARÁ | Brasil | 1504604 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 31dd03e8-30bc-38a4-bbab-97b28d7e3bd4 | -3.71403 | -54.64938 | 2026-09-27 04:51:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c36ff446-e118-3841-b1a5-69cb34b86ae2 | -3.71813 | -54.64604 | 2026-09-27 04:51:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 89978fd9-ac9a-3e69-9403-5c6ce4ea89ae | -4.57357 | -54.92323 | 2026-09-27 04:51:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 82b28983-31fa-30d4-8f04-b5cbd373265b | -4.26009 | -51.05489 | 2026-09-27 04:51:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 90624d9b-6da0-3b98-8a2d-332f8ffd2147 | -3.01046 | -54.21436 | 2026-09-27 04:51:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 932469c5-c3a4-3470-89f9-f80906b26f5f | -2.94639 | -57.7132 | 2026-09-27 04:51:00 | NOAA-21 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| c53aa909-6524-3d66-8b95-101e427eba64 | -7.36899 | -42.11599 | 2026-09-27 04:51:00 | NOAA-21 | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 3.2 |
| 51e4215a-381b-3513-92a2-0718624c405c | -3.07168 | -54.4024 | 2026-09-27 04:51:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 3278f9fa-f071-36e4-bf86-390f5c2f3d02 | -2.58361 | -48.43963 | 2026-09-27 04:51:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| a432de60-3d91-3706-b64b-e74f3e90e8f0 | -2.99077 | -50.47321 | 2026-09-27 04:51:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 793fd55b-6a9e-3c90-94f0-f5d890e0e913 | -3.42959 | -50.33891 | 2026-09-27 04:51:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| adc3e56d-4737-314e-be29-40d4d4745524 | -6.07459 | -53.40628 | 2026-09-27 04:51:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 209d1347-6109-34f3-9ad2-bfb1af327a2f | -6.15727 | -47.13149 | 2026-09-27 04:51:00 | NOAA-21 | CAMPESTRE DO MARANHÃO | MARANHÃO | Brasil | 2102556 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| a8e16548-47df-3466-8d35-d954bfd29cf2 | -3.26708 | -50.14169 | 2026-09-27 04:51:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 85c46a78-56a8-384b-957a-7e2c57e28233 | -4.28567 | -55.25317 | 2026-09-27 04:51:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 7f50ad65-83cc-31c9-a006-b3547b7389af | -8.32396 | -49.97391 | 2026-09-27 04:51:00 | NOAA-21 | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6a3a3ca1-9d64-3853-a71b-b276ca28ffa8 | -4.52872 | -54.97979 | 2026-09-27 04:51:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 70fda15a-6f21-3963-b9aa-a2421dbea3cd | -8.35078 | -44.15923 | 2026-09-27 04:51:00 | NOAA-21 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 62.0 |
| 5920c45a-8b68-3976-834d-81a0d88619b2 | -4.29342 | -55.25031 | 2026-09-27 04:51:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 5da63a87-8a15-3bca-b575-bf2357b65b1c | -5.17496 | -46.0841 | 2026-09-27 04:51:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7bcb6ef4-1d3e-3341-a381-b0a8dab10ffa | -8.35428 | -44.1795 | 2026-09-27 04:51:00 | NOAA-21 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 83.6 |
| 91fea75b-9dcf-3876-a513-cdf1de97676b | -6.31289 | -43.34296 | 2026-09-27 04:51:00 | NOAA-21 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| bbce25ed-738d-3b72-9957-b921883a556c | -4.28678 | -48.5614 | 2026-09-27 04:51:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 5fc2502c-a098-33b1-a0bf-d374d0db41d1 | -4.56757 | -55.05766 | 2026-09-27 04:51:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 8f26f3db-292d-3e04-ac31-895a10d177b5 | -3.43299 | -50.33945 | 2026-09-27 04:51:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 812a4d57-7c21-3528-b3c6-2401b93ae38a | -6.8416 | -43.5127 | 2026-09-27 04:51:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| e2f9473e-153c-3766-8745-52f0ba0d51e6 | -8.35263 | -44.15211 | 2026-09-27 04:51:00 | NOAA-21 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 7.9 |
| b0e701cb-c051-314f-9e61-eb41bcef3c7f | -1.81775 | -55.32434 | 2026-09-27 04:51:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| f7a4fb1d-ae14-3a80-afb9-c9263a448b4f | -8.49846 | -54.77684 | 2026-09-27 04:51:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 6c7cd1c6-2c38-3c8c-9ff1-61772771f5ce | -3.19487 | -51.03909 | 2026-09-27 04:51:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 8d7b08bc-5eba-3b1f-a4d3-c7c99d6c98a5 | -3.45195 | -50.08128 | 2026-09-27 04:51:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |


[Clique aqui para ver as próximas entradas](README29.md)
