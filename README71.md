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

## Dados Diários - Página 71

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| f0b268c6-09bc-3968-8880-c68d7fb5a3c1 | -8.96443 | -65.9281 | 2025-10-27 05:25:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 84f985a4-61e1-3450-a903-c0c13c68fad8 | -11.10003 | -55.56173 | 2025-10-27 05:25:00 | NOAA-20 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6edcdcc0-366a-33ff-bed2-ac8d0e23e7c5 | -8.96865 | -65.90301 | 2025-10-27 05:25:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d0afcefd-be9e-3dc0-a265-e0215291dcff | -9.00061 | -65.92004 | 2025-10-27 05:25:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 84427ca2-a6bd-3aaf-bc29-ea129259675a | -12.04677 | -54.23962 | 2025-10-27 05:25:00 | NOAA-20 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f423882e-f8c4-315e-872f-f4596fd41b78 | -11.09205 | -55.55648 | 2025-10-27 05:25:00 | NOAA-20 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 1218ea76-684c-340f-a742-bd3ad289b6fa | -4.4805 | -43.4237 | 2025-10-27 05:30:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 105.1 |
| 3136df82-9738-3f2a-8fc2-f6224bb908cf | -3.33469 | -42.88068 | 2025-10-27 05:36:00 | AQUA_M-M | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 956534fb-cede-3e2e-85a4-04de598173f9 | -3.60865 | -43.55793 | 2025-10-27 05:36:00 | AQUA_M-M | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 8.1 |
| c10266d8-6230-3b51-b3ec-67178ad2c6b5 | -6.88137 | -43.57481 | 2025-10-27 05:38:00 | AQUA_M-M | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 36.5 |
| dbbf86bb-39b9-3818-a0fb-da7cc085ffc0 | -8.30302 | -46.18079 | 2025-10-27 05:38:00 | AQUA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 14.2 |
| 3eae4384-3e9c-39f6-a4f4-68b0d2d1171d | -10.35534 | -47.1684 | 2025-10-27 05:38:00 | AQUA_M-M | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 28.9 |
| 4e276912-2247-38f9-8a83-d31788e847fa | -8.09177 | -47.05449 | 2025-10-27 05:38:00 | AQUA_M-M | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 13.1 |
| 53f6dbc2-bb39-380e-b3cb-97c56b3f6cab | -7.43924 | -41.87014 | 2025-10-27 05:38:00 | AQUA_M-M | SANTO INÁCIO DO PIAUÍ | PIAUÍ | Brasil | 2209500 | 22 | 33 | nan | nan | nan | Caatinga | 10.6 |
| 751110ba-b7f4-3b01-a622-0647193f3d6c | -6.25298 | -41.83391 | 2025-10-27 05:38:00 | AQUA_M-M | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 5.6 |
| b9a8c040-b8b7-3dc9-8df4-d9b8b8f792c0 | -6.88593 | -45.16145 | 2025-10-27 05:38:00 | AQUA_M-M | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 33.5 |
| 37514d6b-acf5-3d58-911e-94725cdcea55 | -10.31343 | -47.19728 | 2025-10-27 05:38:00 | AQUA_M-M | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 27.0 |
| b5d79ffd-d2ee-34ea-ada3-31d01d99f521 | -4.44637 | -43.65535 | 2025-10-27 05:38:00 | AQUA_M-M | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 31.5 |
| b2095810-fee9-313f-973a-a1a18f30b259 | -6.09535 | -41.77594 | 2025-10-27 05:38:00 | AQUA_M-M | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 5.0 |
| fcf516b7-a02c-3ccf-857c-4afd2ac4768e | -6.44311 | -42.34129 | 2025-10-27 05:38:00 | AQUA_M-M | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 6.1 |
| db97180c-52cc-320e-ab58-837e0e0c408b | -8.02417 | -46.75625 | 2025-10-27 05:38:00 | AQUA_M-M | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 93.8 |
| a8eba585-4525-3dea-81f6-2a46e35097d8 | -10.35245 | -47.18561 | 2025-10-27 05:38:00 | AQUA_M-M | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 22.0 |
| f39b9e5d-a3f7-3a4f-a48d-eb0fc83c035b | -6.43499 | -42.03143 | 2025-10-27 05:38:00 | AQUA_M-M | NOVO ORIENTE DO PIAUÍ | PIAUÍ | Brasil | 2206902 | 22 | 33 | nan | nan | nan | Caatinga | 5.4 |
| 6118b184-4ac1-335d-a6a4-cf2e3eb80839 | -10.74926 | -44.1888 | 2025-10-27 05:38:00 | AQUA_M-M | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 11.5 |
| c49831da-324d-3cf0-8484-ec7ced669722 | -6.25576 | -41.81554 | 2025-10-27 05:38:00 | AQUA_M-M | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 4.5 |
| a5eba1f7-f349-3f41-8173-5e97a1fff56a | -6.8773 | -45.14574 | 2025-10-27 05:38:00 | AQUA_M-M | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 7.7 |
| f3f0aa8e-6903-3595-a73c-427ffec709f7 | -7.82644 | -46.49187 | 2025-10-27 05:38:00 | AQUA_M-M | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 137.6 |
| 74a8a5cd-38e1-3b91-a702-7908c4c5d5f3 | -9.56986 | -46.89025 | 2025-10-27 05:38:00 | AQUA_M-M | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 17.6 |
| 603cc694-e4f2-3bf1-8ed4-769fc4355907 | -7.8211 | -46.49661 | 2025-10-27 05:38:00 | AQUA_M-M | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 58.3 |
| d3bfca6e-edfc-3068-a0a8-6b14fbee38a6 | -4.81027 | -38.64765 | 2025-10-27 05:38:00 | AQUA_M-M | IBARETAMA | CEARÁ | Brasil | 2305266 | 23 | 33 | nan | nan | nan | Caatinga | 9.0 |
| 813f1885-09d9-3512-9790-79e678d1c1bb | -4.48271 | -43.42178 | 2025-10-27 05:38:00 | AQUA_M-M | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 56.3 |
| d7eb163a-9813-30e1-84ff-4e8817644bc2 | -4.47452 | -43.40889 | 2025-10-27 05:38:00 | AQUA_M-M | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 12.0 |
| a608ac4c-2f42-3bf3-9688-a7225fe02bef | -8.09492 | -47.06015 | 2025-10-27 05:38:00 | AQUA_M-M | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 11.5 |
| 506991e8-02ba-3138-826f-b83bd0446ada | -6.63369 | -44.63023 | 2025-10-27 05:38:00 | AQUA_M-M | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 848a87bb-53a8-337f-9754-777ac3f29284 | -9.9857 | -47.17039 | 2025-10-27 05:38:00 | AQUA_M-M | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 20.2 |
| 87a85f15-fcf0-3e2a-951c-51e1652b08dd | -7.82922 | -46.47449 | 2025-10-27 05:38:00 | AQUA_M-M | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 109.4 |
| 65326392-b816-3627-bfde-fd3f5a6a694f | -4.38692 | -43.3083 | 2025-10-27 05:38:00 | AQUA_M-M | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 13.4 |
| 65e36352-135f-3a91-8ae8-84a81e21a87b | -8.02706 | -46.73867 | 2025-10-27 05:38:00 | AQUA_M-M | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 52.1 |
| 04eb440a-82a2-3dc5-a866-5337f63d8bd3 | -7.96956 | -45.45351 | 2025-10-27 05:38:00 | AQUA_M-M | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 8.2 |
| 0226f206-5d27-3853-8e9b-eb521029a8f4 | -7.8534 | -46.44954 | 2025-10-27 05:38:00 | AQUA_M-M | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 25.6 |
| d951e71c-1a41-3970-a9fc-f3b3b8846aab | -6.88306 | -43.56393 | 2025-10-27 05:38:00 | AQUA_M-M | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 20.2 |
| 0e5d343d-d3e8-363c-898b-e4e979deb605 | -6.87503 | -45.15982 | 2025-10-27 05:38:00 | AQUA_M-M | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 33.5 |
| bee11e2f-f77e-36ab-a6f8-4fcf6097e9e2 | -7.06022 | -46.75183 | 2025-10-27 05:38:00 | AQUA_M-M | FEIRA NOVA DO MARANHÃO | MARANHÃO | Brasil | 2104073 | 21 | 33 | nan | nan | nan | Cerrado | 11.1 |
| 179d0cdd-b3fe-3740-9135-80dec5932a17 | -10.74756 | -44.19951 | 2025-10-27 05:38:00 | AQUA_M-M | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 22.9 |
| e5e4f74b-ddf6-3b91-a5a7-200760007025 | -7.82404 | -46.47922 | 2025-10-27 05:38:00 | AQUA_M-M | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 94.0 |
| 362d4116-cebb-353b-baf0-a41b5294ed73 | -6.90049 | -46.13914 | 2025-10-27 05:38:00 | AQUA_M-M | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 12.6 |
| edfb149c-a8ca-3d03-9965-d7d99101830e | -7.24176 | -46.95056 | 2025-10-27 05:38:00 | AQUA_M-M | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 19.7 |
| b640b71a-34a5-3ed8-9d81-0ad181ec9e49 | -8.95426 | -47.18587 | 2025-10-27 05:38:00 | AQUA_M-M | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 12.4 |
| 839545f8-d57b-3a0b-bdce-d85b9d888eba | -7.82288 | -46.43819 | 2025-10-27 05:38:00 | AQUA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 23.9 |
| 4bc91442-2324-39b4-9241-5d2ade3d5989 | -7.95633 | -45.46606 | 2025-10-27 05:38:00 | AQUA_M-M | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 24.5 |
| 4236beb6-50c5-3b1d-a927-abec6b494787 | -7.83587 | -46.48146 | 2025-10-27 05:38:00 | AQUA_M-M | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 27.9 |
| dff5a29e-4c97-3887-a7b7-8c2ea6d00c8f | -8.31713 | -46.16657 | 2025-10-27 05:38:00 | AQUA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 11.8 |
| 912d3286-df87-3ca5-9083-83177f187328 | -7.84012 | -46.40651 | 2025-10-27 05:38:00 | AQUA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 19.2 |
| 4cda436c-a1d6-3cfc-af40-565e30709925 | -9.29862 | -45.23058 | 2025-10-27 05:38:00 | AQUA_M-M | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 8.8 |
| ee6787cc-095b-367a-9701-1cb246bd3389 | -9.26218 | -45.59407 | 2025-10-27 05:38:00 | AQUA_M-M | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 7.3 |
| acde86fe-4e28-3041-9e7f-5f695a1e7fc2 | -4.79953 | -42.75841 | 2025-10-27 05:38:00 | AQUA_M-M | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Cerrado | 7.1 |
| dc4abd33-5366-3d46-a96d-6c3e8ab9de2b | -7.82983 | -46.44485 | 2025-10-27 05:38:00 | AQUA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 30.8 |
| 405fcbff-160d-3c85-bf24-ca6332db0ad7 | -7.84728 | -46.41337 | 2025-10-27 05:38:00 | AQUA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 19.2 |
| d48a27ea-1476-327b-bcf3-2ab3723a1187 | -7.95405 | -45.4802 | 2025-10-27 05:38:00 | AQUA_M-M | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 106.5 |
| 0c92e121-4726-392d-a210-d80f78b1d839 | -4.38514 | -43.31965 | 2025-10-27 05:38:00 | AQUA_M-M | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 53.4 |
| 81b0fe0a-f7a1-3b06-8db9-b0c0f6d1e6da | -9.9827 | -47.18827 | 2025-10-27 05:38:00 | AQUA_M-M | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 18.5 |
| 0c4e79e5-2b35-3671-80f0-5492782c71e8 | -7.42894 | -41.87791 | 2025-10-27 05:38:00 | AQUA_M-M | SANTO INÁCIO DO PIAUÍ | PIAUÍ | Brasil | 2209500 | 22 | 33 | nan | nan | nan | Caatinga | 8.8 |
| 426ac8d6-90c7-32aa-8fc5-f87db683fbcb | -7.43033 | -41.86878 | 2025-10-27 05:38:00 | AQUA_M-M | SANTO INÁCIO DO PIAUÍ | PIAUÍ | Brasil | 2209500 | 22 | 33 | nan | nan | nan | Caatinga | 18.1 |
| 64a27617-aee8-303d-9330-d3313e20fe52 | -6.88819 | -45.14742 | 2025-10-27 05:38:00 | AQUA_M-M | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 36.3 |
| 8446e329-e0cc-396d-8d68-ccb280d16992 | -7.96722 | -45.46815 | 2025-10-27 05:38:00 | AQUA_M-M | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 19.8 |
| 25416157-615d-3fe8-9d47-2ca9e001985c | -7.82557 | -46.4215 | 2025-10-27 05:38:00 | AQUA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 17.1 |
| 082c2b08-a995-3a63-98b7-3a1b9889cf73 | -10.30757 | -47.191 | 2025-10-27 05:38:00 | AQUA_M-M | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 20.3 |
| e0a51d06-f5a3-3530-ad86-3338b2df841a | -5.5923 | -41.31369 | 2025-10-27 05:38:00 | AQUA_M-M | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 8.6 |
| a822719e-3bd6-3695-9a72-8666c9dd9156 | -9.62979 | -46.87098 | 2025-10-27 05:38:00 | AQUA_M-M | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 11.5 |
| 3f0772a6-c657-3d95-b095-3997894ee007 | -7.85057 | -46.46653 | 2025-10-27 05:38:00 | AQUA_M-M | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 29.0 |
| 31972331-fbac-3852-8c7d-705946efdf34 | -9.2558 | -45.56486 | 2025-10-27 05:38:00 | AQUA_M-M | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 985b251b-a3b3-3f2d-9a44-51c18ee87a17 | -7.82696 | -46.4619 | 2025-10-27 05:38:00 | AQUA_M-M | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 57.5 |
| a1964516-30e4-3a05-8072-be3b097fe507 | -7.83298 | -46.49872 | 2025-10-27 05:38:00 | AQUA_M-M | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 20.4 |
| b0141c2d-169f-3b8e-8d35-dc20b259519f | -8.31457 | -46.18236 | 2025-10-27 05:38:00 | AQUA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 11.4 |
| aea39119-2eb1-323b-b0ac-59c14ced897d | -9.63265 | -46.8541 | 2025-10-27 05:38:00 | AQUA_M-M | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 15.1 |
| aafe7b44-73db-3526-a6d5-f7547f7e815f | -6.59481 | -42.67063 | 2025-10-27 05:38:00 | AQUA_M-M | FRANCISCO AYRES | PIAUÍ | Brasil | 2204105 | 22 | 33 | nan | nan | nan | Caatinga | 4.7 |
| 5e52aecb-80d3-31df-a80f-6ee046ae70ed | -4.86861 | -43.25203 | 2025-10-27 05:38:00 | AQUA_M-M | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 6.3 |
| cdd7d3cf-5fe7-33cf-baff-bb5601af6b74 | -4.47273 | -43.42033 | 2025-10-27 05:38:00 | AQUA_M-M | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 119.7 |
| a4fb186e-09c8-3388-986d-4196297d58fe | -7.83202 | -46.45705 | 2025-10-27 05:38:00 | AQUA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 75.7 |
| a05f7154-d53c-3008-96fc-4fbb1909823d | -9.30062 | -45.21815 | 2025-10-27 05:38:00 | AQUA_M-M | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 9.9 |
| 511926ec-44f3-3841-8ffd-a20cd370efb4 | -4.4805 | -43.4237 | 2025-10-27 05:40:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 77.4 |
| 10d10288-aca9-30fb-8a06-3f500777b736 | -4.4618 | -43.4248 | 2025-10-27 05:40:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 49.4 |
| d0fccf28-f328-3894-a115-e7536eebc40b | -4.3879 | -43.3129 | 2025-10-27 05:40:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 31.9 |
| 4ab3fb8b-2c99-3b44-a87d-049e93b38b02 | -11.70856 | -44.43476 | 2025-10-27 05:40:00 | AQUA_M-M | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 28.6 |
| dcd08c66-d687-3a61-b704-e3d1b885a289 | -17.23303 | -46.78494 | 2025-10-27 05:40:00 | AQUA_M-M | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 593769f7-48ab-31e5-85dc-4cca5856f376 | -22.00237 | -43.25482 | 2025-10-27 05:40:00 | AQUA_M-M | SIMÃO PEREIRA | MINAS GERAIS | Brasil | 3167509 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.3 |
| 42e4665e-5fd2-3d56-8a6b-e6155999443a | -17.31565 | -43.65685 | 2025-10-27 05:40:00 | AQUA_M-M | OLHOS-D'ÁGUA | MINAS GERAIS | Brasil | 3145455 | 31 | 33 | nan | nan | nan | Cerrado | 8.9 |
| cb8d998b-a79f-3238-8562-8cc12c833373 | -11.90669 | -43.8289 | 2025-10-27 05:40:00 | AQUA_M-M | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 13.7 |
| eb09a221-3d6e-3ced-8c8f-9903699da048 | -17.32591 | -43.64904 | 2025-10-27 05:40:00 | AQUA_M-M | OLHOS-D'ÁGUA | MINAS GERAIS | Brasil | 3145455 | 31 | 33 | nan | nan | nan | Cerrado | 24.0 |
| 13e7e993-728b-36de-96cf-50c6f95adba9 | -17.31534 | -43.59991 | 2025-10-27 05:40:00 | AQUA_M-M | OLHOS-D'ÁGUA | MINAS GERAIS | Brasil | 3145455 | 31 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 0f4f25e0-79c4-36dd-8076-bd198b758186 | -19.64233 | -45.39119 | 2025-10-27 05:40:00 | AQUA_M-M | BOM DESPACHO | MINAS GERAIS | Brasil | 3107406 | 31 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 24d4b649-0fdb-3634-ba81-8dd7febe40a1 | -17.31707 | -43.64761 | 2025-10-27 05:40:00 | AQUA_M-M | OLHOS-D'ÁGUA | MINAS GERAIS | Brasil | 3145455 | 31 | 33 | nan | nan | nan | Cerrado | 16.3 |
| ca262e0a-7c82-35a9-b874-167d086a9754 | -20.75369 | -43.22345 | 2025-10-27 05:40:00 | AQUA_M-M | PRESIDENTE BERNARDES | MINAS GERAIS | Brasil | 3153103 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.9 |
| e2aa8942-0d78-3f2e-97a3-dcb87a84a77b | -11.90827 | -43.81895 | 2025-10-27 05:40:00 | AQUA_M-M | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 30.8 |
| 7def768b-aba8-3f02-b8da-da18082fd3d7 | -13.23449 | -47.07788 | 2025-10-27 05:40:00 | AQUA_M-M | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 40.5 |
| c31f370c-147a-3cfb-aec6-aea76f74c7bc | -12.08826 | -46.39632 | 2025-10-27 05:40:00 | AQUA_M-M | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 37.0 |
| d764dad7-9865-30e8-8dec-71fdfc0e903a | -21.59043 | -43.48512 | 2025-10-27 05:40:00 | AQUA_M-M | JUIZ DE FORA | MINAS GERAIS | Brasil | 3136702 | 31 | 33 | nan | nan | nan | Mata Atlântica | 7.1 |
| 2325adab-332f-3556-a49c-38a6ff43ca06 | -11.70683 | -44.44548 | 2025-10-27 05:40:00 | AQUA_M-M | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 18.0 |
| 68baa3b0-e7e8-3269-af70-b0ecaafff3d9 | -17.23088 | -46.79746 | 2025-10-27 05:40:00 | AQUA_M-M | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 7.7 |
| c23f2a1b-d301-394e-a1c5-038519653457 | -17.31393 | -43.60912 | 2025-10-27 05:40:00 | AQUA_M-M | OLHOS-D'ÁGUA | MINAS GERAIS | Brasil | 3145455 | 31 | 33 | nan | nan | nan | Cerrado | 5.8 |


[Clique aqui para ver as próximas entradas](README72.md)
