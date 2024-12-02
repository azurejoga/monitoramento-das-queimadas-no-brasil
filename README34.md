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

## Dados Diários - Página 34

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| db6d6951-0cbc-33ce-a6df-0cc3e6d9cfe9 | -1.69745 | -52.64232 | 2024-12-02 04:23:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| e6f347bf-c492-3fcc-92cf-74b6a2a18ad0 | -3.26558 | -45.37189 | 2024-12-02 04:23:00 | NPP-375D | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 48054565-f1cf-32d9-9f1e-bbb4cb499340 | -1.68328 | -46.20479 | 2024-12-02 04:23:00 | NPP-375D | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| f89cb869-43d3-3a42-8f84-37c13733a2f0 | -1.23446 | -51.61635 | 2024-12-02 04:23:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c0800265-fbc7-3b07-8082-161a4cb30b0f | -3.30884 | -46.15037 | 2024-12-02 04:23:00 | NPP-375D | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d00d9e48-fa7c-3059-b5ae-c595cbaf13bf | -1.38844 | -53.55571 | 2024-12-02 04:23:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 05c2aeaf-934a-39ef-803e-3e8f095a012a | -2.64817 | -46.77694 | 2024-12-02 04:23:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 4ac52a3d-b4ff-3fae-9215-4a9d42f1d6ab | -1.37698 | -52.3861 | 2024-12-02 04:23:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f40bd021-dca2-30f8-8274-1ffe03d88602 | -2.56433 | -46.33849 | 2024-12-02 04:23:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 892fe3f7-44e4-3c55-94a5-49d7419ef76d | -2.90202 | -48.58809 | 2024-12-02 04:23:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2e0281ff-5a96-3e59-a1cd-b385bba04b92 | -2.65656 | -46.12341 | 2024-12-02 04:23:00 | NPP-375D | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| aa3f3556-309a-3db6-ab36-ad4f6734630f | -1.94749 | -53.34236 | 2024-12-02 04:23:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 569303e3-0b6f-3762-8a0c-9889281a55a6 | -1.9617 | -46.45417 | 2024-12-02 04:23:00 | NPP-375D | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 361d9b61-054d-3f45-b302-04be900d895d | -2.73146 | -46.24961 | 2024-12-02 04:23:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9f95ee52-d077-3a0d-8544-5186722bb9c4 | -4.05711 | -46.6801 | 2024-12-02 04:25:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| f194cfe3-d91c-359c-8e34-6813d228f50a | -6.92317 | -43.53824 | 2024-12-02 04:25:00 | NPP-375D | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 9fa58735-3400-3783-bca5-77c70f88ff52 | -3.87705 | -46.57942 | 2024-12-02 04:25:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c81da8a5-d8d4-3f69-9adf-be04cfbbe987 | -3.85667 | -50.89785 | 2024-12-02 04:25:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| c3017522-d873-3f0d-afbb-344a5dcee29c | -4.04198 | -46.84058 | 2024-12-02 04:25:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f9a4b73a-2f71-3147-9bdf-13939e6d561c | -3.26685 | -50.21136 | 2024-12-02 04:25:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 099af522-88ae-3d7d-8327-ecd562e8589e | -3.25309 | -53.93149 | 2024-12-02 04:25:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 65454a2e-f4bc-369b-85b9-2516ce487073 | -3.9366 | -47.98331 | 2024-12-02 04:25:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a340993e-be3b-3405-9aa0-7a058e098883 | -3.50775 | -53.8338 | 2024-12-02 04:25:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1f00d9ca-8200-3c7e-912e-e9243377df7a | -4.36261 | -46.26959 | 2024-12-02 04:25:00 | NPP-375D | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 112efae6-5cd2-3a40-b7a9-ef138fa33454 | -2.95178 | -51.79357 | 2024-12-02 04:25:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d11f1f0a-b77a-3590-a758-2ea4807b96c7 | -10.66225 | -44.49832 | 2024-12-02 04:25:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 5.6 |
| c50e97e3-86b3-37cf-97bf-0f6e83f3a6cc | -5.55097 | -50.27243 | 2024-12-02 04:25:00 | NPP-375D | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 97269239-c820-3fb5-a69d-b3e9d49ffe57 | -3.248 | -53.93053 | 2024-12-02 04:25:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 8b019538-76dd-3bf7-b597-da94d6491323 | -8.13514 | -44.48053 | 2024-12-02 04:25:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 17e27b7e-61fc-36d0-86a4-fec7395a8597 | -3.55124 | -51.45678 | 2024-12-02 04:25:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e02dc96e-15f7-39c3-a59e-ec5963ebbf24 | -5.19931 | -43.86544 | 2024-12-02 04:25:00 | NPP-375D | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 2c59ad63-39da-32af-ad1b-1668600bfcd2 | -10.69944 | -44.9735 | 2024-12-02 04:25:00 | NPP-375D | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| efba4075-1b7b-3d20-b484-3d62b0e93e5d | -4.06214 | -46.822 | 2024-12-02 04:25:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b1c83bdf-54ad-30a7-84eb-102624f0cc73 | -4.33688 | -50.40079 | 2024-12-02 04:25:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 315ccfd3-d23b-302e-aa69-d8f2ac168173 | -3.4207 | -54.64035 | 2024-12-02 04:25:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 0.3 |
| abed8b50-2142-3acc-ad51-c0594bf4d023 | -9.18862 | -45.35024 | 2024-12-02 04:25:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 3806ffda-6ae0-3289-802a-d313dc8c1a76 | -4.86085 | -41.31291 | 2024-12-02 04:25:00 | NPP-375D | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| c0f17117-2be0-3db4-87a9-142548933306 | -3.94765 | -48.18342 | 2024-12-02 04:25:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b9f33bc8-7485-35a5-b2dc-a2bd59695696 | -3.98566 | -46.66551 | 2024-12-02 04:25:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 495b169d-4aac-3f89-bee2-0485beb55f29 | -4.42911 | -46.29789 | 2024-12-02 04:25:00 | NPP-375D | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 49e0d847-0d10-3c3b-b30f-ca4f0461d135 | -3.11074 | -53.76234 | 2024-12-02 04:25:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1fc29ac5-57cd-3fb0-a3fc-b07237c65a11 | -8.82969 | -44.78119 | 2024-12-02 04:25:00 | NPP-375D | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 0278fd32-0589-3c56-8b31-70540a31d133 | -3.93359 | -46.39474 | 2024-12-02 04:25:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 28bb18e5-20fd-3826-a0b3-a347da91a597 | -3.53782 | -51.49701 | 2024-12-02 04:25:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 5f434ed8-d0a2-3cd9-ad69-ce88622fe30c | -3.93988 | -46.50011 | 2024-12-02 04:25:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| da5ac3d2-a7ea-386c-b615-6bfad17409ce | -4.47216 | -50.77021 | 2024-12-02 04:25:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 91f6bbd5-60d1-3246-9900-7e33b085e1c1 | -2.82334 | -51.8363 | 2024-12-02 04:25:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 639d6d58-e826-324a-8699-c5ded45c8f41 | -6.45963 | -47.53953 | 2024-12-02 04:25:00 | NPP-375D | AGUIARNÓPOLIS | TOCANTINS | Brasil | 1700301 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 910c7c09-d1b2-3206-ac02-f9f8ce9d40e2 | -4.32341 | -48.09301 | 2024-12-02 04:25:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c6f6d4ba-ec87-3100-865c-abe698d4d38d | -3.62398 | -52.50162 | 2024-12-02 04:25:00 | NPP-375D | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e803b25b-b3ff-33a1-8dc1-dcc9f4bd3c93 | -10.6599 | -44.48971 | 2024-12-02 04:25:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 86d566d5-8918-36c2-8e42-b1a8b256928f | -4.05262 | -46.81684 | 2024-12-02 04:25:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 652ef103-ed4e-39fc-b2cf-469cc0eb5a33 | -4.03461 | -46.93055 | 2024-12-02 04:25:00 | NPP-375D | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 2cc555e3-f33e-3b48-b9cd-90911846ccdd | -4.72319 | -43.25357 | 2024-12-02 04:25:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| b6ced675-65e3-3817-8827-1560bda81cc1 | -3.79272 | -46.69966 | 2024-12-02 04:25:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| c89112b7-95f4-3200-9694-a91aff753a22 | -3.97282 | -46.65986 | 2024-12-02 04:25:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 9dd4c7ce-c95c-3d17-983f-7e02962007f1 | -3.69728 | -47.12053 | 2024-12-02 04:25:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5c8c9911-7ce1-36ee-a56c-0ef05883f2b5 | -5.12376 | -43.20116 | 2024-12-02 04:25:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 7a6abe6c-f866-31aa-ab32-4276288fefa6 | -3.8737 | -46.5789 | 2024-12-02 04:25:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| cde86084-7bbf-3290-b9a6-0b84f3a6769f | -3.87761 | -46.5759 | 2024-12-02 04:25:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 0bc21838-ff67-3ea4-a05e-f0ce9e2b8b0f | -3.10381 | -49.50478 | 2024-12-02 04:25:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 4f7750ce-3d07-334b-909b-0bd6047d8269 | -4.20562 | -50.67274 | 2024-12-02 04:25:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 37d28f1a-1de6-348c-b811-4183db605abb | 1.66047 | -50.77212 | 2024-12-02 04:25:00 | NPP-375D | PRACUÚBA | AMAPÁ | Brasil | 1600550 | 16 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 3629ce86-0920-3ce3-ba46-0f0bb373576c | -3.90136 | -46.65586 | 2024-12-02 04:25:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| cd7c327c-dd78-38aa-b3d1-2c4c819dcfa4 | -4.01261 | -47.00394 | 2024-12-02 04:25:00 | NPP-375D | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f1c968b5-7759-3f54-a3fd-25712221e0ff | -3.94482 | -46.9241 | 2024-12-02 04:25:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 4df0cbce-aab2-34bd-a38c-1c0944ed2e22 | -11.05954 | -45.38148 | 2024-12-02 04:25:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 052de66e-10a8-3c06-ae94-5893d1fa7c4c | -3.85362 | -46.53259 | 2024-12-02 04:25:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 46d212f5-8cee-3804-ba01-76b7f64a0e11 | -3.27038 | -53.63469 | 2024-12-02 04:25:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f7a3a554-2276-3eee-936e-fee90c780a5a | -3.89641 | -46.43533 | 2024-12-02 04:25:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 77fbcddc-54d3-39c7-a6a1-d941f610e346 | -4.04917 | -46.99138 | 2024-12-02 04:25:00 | NPP-375D | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 13dc17e0-53e7-3a6f-ae8d-e56b302658b2 | -3.64391 | -51.10824 | 2024-12-02 04:25:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 49b02b59-de17-3192-a703-6e889f7da032 | -4.84605 | -50.49405 | 2024-12-02 04:25:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 40ef0564-811d-327c-b4a5-18025ba517bf | -3.10005 | -54.04952 | 2024-12-02 04:25:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 07d5b5c6-5ef1-3a8b-bbae-cf351903a4a3 | -3.99402 | -47.27451 | 2024-12-02 04:25:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 5acbadfa-6824-3223-9fe3-570cdac41b3c | -3.2475 | -53.93365 | 2024-12-02 04:25:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f37fbc27-8be8-35d6-9198-37fee4424e09 | -11.6219 | -43.25249 | 2024-12-02 04:25:00 | NPP-375D | MORPARÁ | BAHIA | Brasil | 2921609 | 29 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 62463fb7-c962-3bf1-91f5-7906c26577ec | -3.7001 | -47.12468 | 2024-12-02 04:25:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 9af11d00-6016-33e1-98ac-71779bc81829 | -3.56828 | -52.49954 | 2024-12-02 04:25:00 | NPP-375D | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 88eaf219-9285-3a8a-8b21-467ab571b3b7 | -3.29718 | -53.83846 | 2024-12-02 04:25:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 00e6a10a-d817-3d44-9894-02c3eea1d1bb | -5.48766 | -47.23923 | 2024-12-02 04:25:00 | NPP-375D | SENADOR LA ROCQUE | MARANHÃO | Brasil | 2111763 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 41c8d43e-0d88-369b-b093-e5d90248b421 | -4.0026 | -46.93649 | 2024-12-02 04:25:00 | NPP-375D | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| fef7cc78-2ca7-3563-9f72-e3812a49ab6d | -3.91547 | -43.7136 | 2024-12-02 04:25:00 | NPP-375D | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 740b86cb-e5a2-3e5f-91a9-564b828bd4d7 | -4.4383 | -45.35653 | 2024-12-02 04:25:00 | NPP-375D | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| ab836603-8359-3bfe-9f62-92101e454741 | -3.47513 | -47.68285 | 2024-12-02 04:25:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| d5bba25b-ed20-3438-a79c-842ce95598f5 | -2.95827 | -50.57604 | 2024-12-02 04:25:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ee1afc0c-86ec-38ac-ae80-dc7162657797 | -3.58682 | -50.51815 | 2024-12-02 04:25:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e0c65e32-cb84-33f2-b69b-9d1e7465b077 | -3.72812 | -49.9354 | 2024-12-02 04:25:00 | NPP-375D | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 37ff8849-84eb-3ded-93e6-ad09bac2c497 | -4.20395 | -50.68311 | 2024-12-02 04:25:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f8fb12ae-29af-3998-8a2f-edda09a0bcf2 | -4.5744 | -43.35205 | 2024-12-02 04:25:00 | NPP-375D | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 5fdba317-2802-30cf-b32a-7a713ecf9d10 | -2.72031 | -54.17549 | 2024-12-02 04:25:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 778f92a4-11f8-37d4-a034-9fe1b3594498 | -3.04646 | -49.37788 | 2024-12-02 04:25:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 188b4586-5111-3f5f-8064-7862f40d2e64 | -2.81462 | -53.95724 | 2024-12-02 04:25:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| bb0dfc28-3635-3580-9707-ca34308b5031 | -3.89465 | -46.67642 | 2024-12-02 04:25:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6de5243e-4d2e-3759-afff-1fea39aa59c1 | -4.01599 | -47.00443 | 2024-12-02 04:25:00 | NPP-375D | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 9c1272c5-34f0-3d28-8fe9-27cb0c10ac9c | -2.81813 | -53.05173 | 2024-12-02 04:25:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| e57fd2ff-63ce-3411-90ef-d81df53a8348 | -3.85966 | -47.04648 | 2024-12-02 04:25:00 | NPP-375D | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 31b6291c-e0e1-3855-9733-768aaef3b4c3 | -3.54416 | -50.18326 | 2024-12-02 04:25:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| df2918af-98d1-31c3-94da-d8bf37afa55b | -3.84972 | -46.53558 | 2024-12-02 04:25:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.4 |
| f8eb2531-b72b-330f-8ee3-71e211483f6d | -4.09079 | -44.85283 | 2024-12-02 04:25:00 | NPP-375D | BACABAL | MARANHÃO | Brasil | 2101202 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |


[Clique aqui para ver as próximas entradas](README35.md)
