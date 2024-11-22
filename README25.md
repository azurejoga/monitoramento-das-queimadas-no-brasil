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

## Dados Diários - Página 25

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| d78ab99f-47e8-3e9b-9fc0-95dba30cd451 | -2.00951 | -54.51934 | 2024-11-22 04:12:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 2af8fc1d-59e0-3a1f-9901-0b118f357159 | -1.6655 | -46.93521 | 2024-11-22 04:12:00 | NPP-375D | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 243f0791-e254-3c42-b510-15b8b9bf2988 | -3.44022 | -42.54696 | 2024-11-22 04:12:00 | NPP-375D | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| dbbac423-7bff-32dd-855f-d580cd077173 | -4.39964 | -44.12361 | 2024-11-22 04:12:00 | NPP-375D | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 1593ba98-0ee8-390b-bbe0-bcd36f1ff7e2 | -5.93464 | -43.7862 | 2024-11-22 04:12:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 4319202b-8b71-30aa-8bb4-b45e7f1ca551 | -1.96588 | -48.38766 | 2024-11-22 04:12:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| c02fed2e-550c-33f1-a7c2-d6f64d613273 | -3.83318 | -52.2571 | 2024-11-22 04:12:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 362becce-e9f8-30bb-8665-93cec11b4bc9 | -3.11073 | -54.28558 | 2024-11-22 04:12:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| f921e6fd-0e96-3b43-b447-a544e852683a | -2.28519 | -47.91563 | 2024-11-22 04:12:00 | NPP-375D | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 85ea20e6-6860-3a53-821f-ac8e3a97dc12 | -5.062 | -44.21971 | 2024-11-22 04:12:00 | NPP-375D | GOVERNADOR ARCHER | MARANHÃO | Brasil | 2104503 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 186e1ce4-5c21-3902-8506-718b84f8a259 | -3.51409 | -50.81171 | 2024-11-22 04:12:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 33b6486e-38be-3331-b594-4f3462f77cf3 | -4.70516 | -48.2977 | 2024-11-22 04:12:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| cb6200dd-f087-33fd-85b1-2b6db8ad11e9 | -2.76443 | -52.11414 | 2024-11-22 04:12:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| eaaa8ba7-5671-38cc-ad48-d8e9bebb9eae | -6.11851 | -42.51415 | 2024-11-22 04:12:00 | NPP-375D | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 8aad02ea-056b-3ef8-9be5-6283f3016c17 | -1.17985 | -51.9353 | 2024-11-22 04:12:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 03652d81-cc3d-340b-9880-61aac2f5ab6c | -6.02798 | -46.10717 | 2024-11-22 04:12:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 8559949c-928d-33be-839c-77b135f87310 | -3.8034 | -46.60147 | 2024-11-22 04:12:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 3.8 |
| ad758857-94be-3c93-8656-b25477ef6cad | -3.13947 | -41.22486 | 2024-11-22 04:12:00 | NPP-375D | CHAVAL | CEARÁ | Brasil | 2303907 | 23 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 0c4bb88c-2c24-3632-9ad1-d5925dcb7476 | -3.46434 | -45.90783 | 2024-11-22 04:12:00 | NPP-375D | GOVERNADOR NEWTON BELLO | MARANHÃO | Brasil | 2104651 | 21 | 33 | nan | nan | nan | Amazônia | 18.1 |
| 11fc1262-a979-36dd-a5aa-0c48865c55cb | -2.79012 | -45.94852 | 2024-11-22 04:12:00 | NPP-375D | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 9b92b885-afbc-3dcc-8f13-2dc2018de4fb | -4.12075 | -43.87637 | 2024-11-22 04:12:00 | NPP-375D | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| e3ed5836-bedb-3b08-bdbd-cbc384f168ef | -2.78932 | -51.41199 | 2024-11-22 04:12:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b8945c7e-4ab5-3f80-800e-0ab06eeb3fc6 | -1.12418 | -53.4073 | 2024-11-22 04:12:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| ed491cd7-0627-30b2-a63f-399f99a5b356 | -3.02239 | -45.14257 | 2024-11-22 04:12:00 | NPP-375D | MATINHA | MARANHÃO | Brasil | 2106508 | 21 | 33 | nan | nan | nan | Amazônia | 8.0 |
| 13d8405a-840c-3e44-bf5c-eb91a139480b | -1.1939 | -51.95811 | 2024-11-22 04:12:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 13941a13-58e1-3edd-9311-5ccb262f9283 | -3.2859 | -53.84192 | 2024-11-22 04:12:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 18d78b6a-3e84-30b7-acb4-c5f18287c833 | -1.73082 | -52.71748 | 2024-11-22 04:12:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 3bb20da1-99c3-365b-902c-b36ce8c58ec9 | -2.93174 | -48.055 | 2024-11-22 04:12:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 385c06a2-b350-3631-9101-e9d72b9bd0df | -1.71358 | -52.48425 | 2024-11-22 04:12:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 0478e8f1-8cc1-3b7e-b45d-ec8d254c7fb8 | -4.70213 | -48.29314 | 2024-11-22 04:12:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 97aae464-37eb-36d5-82b2-7a32d6f67956 | -2.69838 | -46.25402 | 2024-11-22 04:12:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 71e47006-008d-3d7f-a8ed-c06fbaa1e484 | -1.44547 | -53.39273 | 2024-11-22 04:12:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 62f9a628-735f-3f6f-8b30-a9ddcbd72bdc | -3.88743 | -46.66854 | 2024-11-22 04:12:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f03f8fc5-34c5-338b-b0b6-00682fd0612a | -1.19578 | -51.94623 | 2024-11-22 04:12:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 60ed9fc5-27fe-3af6-88a0-75aca40f364f | -5.01093 | -41.95939 | 2024-11-22 04:12:00 | NPP-375D | JATOBÁ DO PIAUÍ | PIAUÍ | Brasil | 2205276 | 22 | 33 | nan | nan | nan | Caatinga | 4.6 |
| 37eec8f0-eb62-372d-8075-b56d86b5d507 | -1.0732 | -53.36333 | 2024-11-22 04:12:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 751756bf-a40b-3267-bc77-0dc774e73630 | -1.72777 | -52.70956 | 2024-11-22 04:12:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| d118e03f-fa93-364e-972f-87b01a302a3c | -1.78955 | -53.63712 | 2024-11-22 04:12:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 762d22c1-30b0-3d98-b1b9-0c61367d718f | -6.62655 | -42.38316 | 2024-11-22 04:12:00 | NPP-375D | ARRAIAL | PIAUÍ | Brasil | 2201002 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| fea573c0-48fa-3067-9834-9a03ccd5d04f | -4.7015 | -48.29703 | 2024-11-22 04:12:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e293b35c-267a-3034-b26e-2f464b3b65c1 | -3.0037 | -51.30868 | 2024-11-22 04:12:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 27f23efa-96da-32de-ac3d-7f07841bd60e | -1.2741 | -52.98486 | 2024-11-22 04:12:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| fa12cecd-ddec-31cf-a5df-9056380be18a | -4.70157 | -48.29319 | 2024-11-22 04:12:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ec3f0e33-8891-3606-a28f-3971f8633c6c | -4.70081 | -46.07628 | 2024-11-22 04:12:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| fa44548b-3a90-3619-8733-76d035842155 | -6.8415 | -44.38566 | 2024-11-22 04:12:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| b6b9e51f-8974-3017-bf3a-2d5540c33b76 | -3.68839 | -50.21896 | 2024-11-22 04:12:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| bf7f5f77-350c-357f-970f-dea9991ccbee | -3.83833 | -41.56636 | 2024-11-22 04:12:00 | NPP-375D | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| d31445fa-fa95-31b5-9c03-2abd1626fd91 | -1.11321 | -53.39518 | 2024-11-22 04:12:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| b19c433e-df07-394a-9642-5fcae2ebd168 | -4.40022 | -44.11994 | 2024-11-22 04:12:00 | NPP-375D | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 9bf1c915-2584-38c0-aa92-dc1ae1523087 | -4.57819 | -48.02388 | 2024-11-22 04:12:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 97d21cdd-53d6-3583-b757-e8d6aa479c4e | -1.94539 | -49.52398 | 2024-11-22 04:12:00 | NPP-375D | LIMOEIRO DO AJURU | PARÁ | Brasil | 1504000 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 747049dc-9a5a-31b8-96ad-a4af7ffb1404 | -4.44246 | -50.69812 | 2024-11-22 04:12:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2f1c165b-f3d3-39b7-a991-84baa4b6245b | -2.41168 | -46.06693 | 2024-11-22 04:12:00 | NPP-375D | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 7c28d5ca-67cc-3f1e-a0a4-22a177cef518 | -4.78882 | -45.62287 | 2024-11-22 04:12:00 | NPP-375D | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2d9e3945-d460-301c-80b4-531996ce537d | -2.28105 | -46.55821 | 2024-11-22 04:12:00 | NPP-375D | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 8981a6f3-913f-33af-8180-7c2956bdacd7 | -2.68614 | -46.25688 | 2024-11-22 04:12:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 3a20d973-7833-32e0-b511-92cbf68fe347 | -1.21515 | -51.97395 | 2024-11-22 04:12:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 0a26fc3f-9118-3ea5-b835-8e9b4a2f59c5 | -5.04093 | -44.17594 | 2024-11-22 04:12:00 | NPP-375D | GOVERNADOR ARCHER | MARANHÃO | Brasil | 2104503 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f304c04b-093f-3e79-a105-9bf498df1b12 | -4.06162 | -46.41854 | 2024-11-22 04:12:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3e9bf301-3a69-3f16-b2cf-b3db2e20d058 | -4.70575 | -48.29768 | 2024-11-22 04:12:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 071a8cbb-bce5-330e-bdba-d29a43c1d6f2 | -2.35605 | -48.55669 | 2024-11-22 04:12:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 7.4 |
| 71d1aebe-5f8d-324c-be44-9e2a65ac4751 | -1.19037 | -51.94545 | 2024-11-22 04:12:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| b615c5ae-3207-35fe-8b08-303beff43c03 | -3.25055 | -54.24203 | 2024-11-22 04:12:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 45077536-a6d9-3204-9ac6-4fcef4015cc1 | -2.93624 | -40.86707 | 2024-11-22 04:12:00 | NPP-375D | CAMOCIM | CEARÁ | Brasil | 2302602 | 23 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 36f63dab-28d1-3a80-85e3-14c4d0213396 | -5.09207 | -45.9402 | 2024-11-22 04:12:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 94dea534-9a59-33eb-9a11-d364adb092ce | -0.26539 | -51.57001 | 2024-11-22 04:12:00 | NPP-375D | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 52b02266-1b6d-34c9-9028-9ad8a7eda023 | -1.62125 | -52.6007 | 2024-11-22 04:12:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 2cefd5c4-de13-33fd-8873-7bb4d3b56e63 | -3.57479 | -54.52024 | 2024-11-22 04:12:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 358f7908-7767-3dcc-9478-ad057a442146 | -2.70221 | -46.25464 | 2024-11-22 04:12:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 78e1a500-1ec9-3b15-95e6-cb07f93f3072 | -2.68997 | -46.25749 | 2024-11-22 04:12:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 6aec0826-287a-3ac7-9022-b68bcdf5a81d | -3.57324 | -54.68441 | 2024-11-22 04:12:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 6f7cea23-f0fe-39ed-9482-0e29355c4852 | -4.13603 | -54.66118 | 2024-11-22 04:12:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| d93ca094-6e59-3d99-8bdc-e47159339e87 | -2.54423 | -46.20953 | 2024-11-22 04:12:00 | NPP-375D | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 215a0957-8875-3fd4-bb97-37e0aac4721f | -3.22192 | -54.25465 | 2024-11-22 04:12:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 10.5 |
| 2838277e-1f58-32e7-b1b1-aab13f3b837a | -2.19566 | -53.65035 | 2024-11-22 04:12:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e6a73f5a-6504-3682-8a34-7f309644e0b5 | -1.20988 | -51.96893 | 2024-11-22 04:12:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 894785bf-31a5-3df6-9c9c-6d427180f44d | -2.78392 | -51.41111 | 2024-11-22 04:12:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| afec8b14-d1a7-308b-9a4a-b8e9c971fbc2 | -5.50652 | -45.48524 | 2024-11-22 04:12:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 2fee99bd-72d6-397f-ba46-92429a4572dc | -2.43564 | -46.54152 | 2024-11-22 04:12:00 | NPP-375D | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b4f50adb-c170-375b-8d0d-e07d5b8c2820 | -3.47176 | -45.90905 | 2024-11-22 04:12:00 | NPP-375D | GOVERNADOR NEWTON BELLO | MARANHÃO | Brasil | 2104651 | 21 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 3214ff5f-dae1-36a3-8bb9-b2b4da3053ec | -2.21991 | -53.73708 | 2024-11-22 04:12:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| ba18de29-8f19-31eb-9dd6-0d93cb5a9bfd | -2.1577 | -53.7958 | 2024-11-22 04:12:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 8cd1880b-d67e-3c61-b80c-bf75c17ef2f8 | -2.8413 | -46.68092 | 2024-11-22 04:12:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 15886925-e4c2-3ca2-aa64-1c1d5588ea52 | -4.12131 | -43.87278 | 2024-11-22 04:12:00 | NPP-375D | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| ccd7a163-6671-357c-a733-5f42f9918b6b | -3.51372 | -54.69042 | 2024-11-22 04:12:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| ccb52ab2-3e15-3058-a69f-b875bde8de0b | -3.64879 | -41.91106 | 2024-11-22 04:12:00 | NPP-375D | CARAÚBAS DO PIAUÍ | PIAUÍ | Brasil | 2202539 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 1170218d-53d1-36f6-bc32-46bd424d265e | -2.70217 | -46.23059 | 2024-11-22 04:12:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4177611b-ccd3-3120-9e11-7be678f3c469 | -1.27487 | -52.9802 | 2024-11-22 04:12:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 013682c2-d95c-3680-aaad-20941ff7d6f5 | -3.25646 | -54.25011 | 2024-11-22 04:12:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 5f4b3e73-0cf1-3926-a45f-147bd136a673 | -0.05358 | -51.23246 | 2024-11-22 04:12:00 | NPP-375D | SANTANA | AMAPÁ | Brasil | 1600600 | 16 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 2fefafd0-0a5d-30b1-9593-ea4452222912 | -3.06676 | -53.28899 | 2024-11-22 04:12:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7bf65d0a-195a-38d8-a370-8861dd72cc69 | -5.9285 | -43.78163 | 2024-11-22 04:12:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 0a264ed4-180e-34e6-9f15-3f0b3a9d19d6 | -4.42886 | -46.58964 | 2024-11-22 04:12:00 | NPP-375D | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 3.2 |
| f909b5a4-151d-3666-a09f-d3bd93c5bc94 | -4.21223 | -50.6953 | 2024-11-22 04:12:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 85562821-7a10-3f9f-9303-a4a6d923168e | -0.30934 | -51.5495 | 2024-11-22 04:12:00 | NPP-375D | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2cd760cd-faa4-3f49-9e1b-d0784f625599 | -2.69812 | -46.08744 | 2024-11-22 04:12:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 66d116ff-8ed7-3ee7-9814-5e0f16a11633 | -3.2758 | -53.82561 | 2024-11-22 04:12:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 89a0a06f-f99a-388a-ae8e-cd90c363f7a4 | -3.50419 | -53.81131 | 2024-11-22 04:12:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| ea17b4ae-5a38-36c3-a7a4-48546fd39fdb | -2.21194 | -52.22879 | 2024-11-22 04:12:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 09df0c52-686d-337e-b714-4cd67957103c | -2.72842 | -46.09228 | 2024-11-22 04:12:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |


[Clique aqui para ver as próximas entradas](README26.md)
