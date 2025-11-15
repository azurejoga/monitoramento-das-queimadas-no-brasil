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

## Dados Diários - Página 24

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 8c6f1b99-6466-3c59-ba0d-a2cedd67d326 | -2.4355 | -48.05027 | 2025-11-15 04:04:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 98eb2604-6f10-3bc5-a5b5-20ab6c16bf43 | -5.52817 | -41.77057 | 2025-11-15 04:04:00 | NPP-375D | SÃO JOÃO DA SERRA | PIAUÍ | Brasil | 2209906 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| a4b4269a-89d6-30e9-b336-d30bcd52e090 | -6.00015 | -45.3974 | 2025-11-15 04:04:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 63228b2e-a76f-331d-9e02-8b5203b2ba56 | -1.67979 | -46.92165 | 2025-11-15 04:04:00 | NPP-375D | SANTA LUZIA DO PARÁ | PARÁ | Brasil | 1506559 | 15 | 33 | nan | nan | nan | Amazônia | 8.1 |
| ec815462-eee5-354f-9010-9c4cfea9b1d9 | -4.35997 | -47.57782 | 2025-11-15 04:04:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 58b4a27d-0a01-3fe8-8803-366bff75756c | -6.65272 | -43.51377 | 2025-11-15 04:04:00 | NPP-375D | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 1276ba4d-285f-31d3-9b79-146aa0f8823f | -5.51027 | -40.54931 | 2025-11-15 04:04:00 | NPP-375D | INDEPENDÊNCIA | CEARÁ | Brasil | 2305605 | 23 | 33 | nan | nan | nan | Caatinga | 2.2 |
| ce3391b9-78de-3885-ac61-338a1b8ff86b | -7.34476 | -46.01117 | 2025-11-15 04:04:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| abc29a89-9807-356f-b295-e588633ead47 | -6.10074 | -41.62018 | 2025-11-15 04:04:00 | NPP-375D | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| a7992dd9-ee99-33fe-90bc-051ad4030dec | -4.30349 | -45.88776 | 2025-11-15 04:04:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 69e54c84-4486-3576-b15d-90c9ca746dd2 | -6.73514 | -42.96448 | 2025-11-15 04:04:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 40b58b52-7d0d-3cc3-b503-59081a9bb357 | -6.58286 | -47.5337 | 2025-11-15 04:04:00 | NPP-375D | PALMEIRAS DO TOCANTINS | TOCANTINS | Brasil | 1713809 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 572b96ba-941a-3761-afc1-63f6b2dd88e5 | -7.65455 | -41.30046 | 2025-11-15 04:04:00 | NPP-375D | PATOS DO PIAUÍ | PIAUÍ | Brasil | 2207777 | 22 | 33 | nan | nan | nan | Caatinga | 3.2 |
| 42540543-39c2-3ab9-8835-50589155a881 | -4.27297 | -46.83785 | 2025-11-15 04:04:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 7a7c5266-64cf-3100-8004-876946d44f8b | -3.76235 | -45.08428 | 2025-11-15 04:04:00 | NPP-375D | PIO XII | MARANHÃO | Brasil | 2108702 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3eea71b2-a742-3fad-b913-7f54d5d6b3a7 | -7.65731 | -40.02755 | 2025-11-15 04:04:00 | NPP-375D | BODOCÓ | PERNAMBUCO | Brasil | 2602001 | 26 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 1996329e-0653-3fa5-8f5f-09741e47d000 | -2.51885 | -47.8063 | 2025-11-15 04:04:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 498429d6-c159-335b-8831-ef4937327cf3 | -5.3861 | -44.84343 | 2025-11-15 04:04:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 8c7966e6-2ad3-3320-8df9-a345d4af8a2d | -7.10527 | -42.73264 | 2025-11-15 04:04:00 | NPP-375D | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 41dc5c64-8669-38e1-81a6-29b6fce6ee77 | -5.05516 | -44.68241 | 2025-11-15 04:04:00 | NPP-375D | JOSELÂNDIA | MARANHÃO | Brasil | 2105609 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 803daafc-3746-3788-b00a-5b5ac013f05a | -4.40118 | -44.07947 | 2025-11-15 04:04:00 | NPP-375D | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 42d7edf3-8799-3111-81fe-6c15f8632179 | -7.45409 | -42.76286 | 2025-11-15 04:04:00 | NPP-375D | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 2a544acc-13f1-332f-bc99-152866d02d20 | -4.58054 | -43.40249 | 2025-11-15 04:04:00 | NPP-375D | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 4684e082-808e-30bf-a2fb-05d567bc9fa6 | -4.42745 | -47.60096 | 2025-11-15 04:04:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d5795a8f-1e76-33d4-b04b-180e58036724 | -4.5407 | -43.21798 | 2025-11-15 04:04:00 | NPP-375D | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 19.1 |
| 8a67ae25-3d7b-3332-b48f-654687296ce1 | -7.33138 | -40.37462 | 2025-11-15 04:04:00 | NPP-375D | SALITRE | CEARÁ | Brasil | 2311959 | 23 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 0a7be502-1957-3a03-b8b4-a43e6dfad6b1 | -5.7486 | -42.72437 | 2025-11-15 04:04:00 | NPP-375D | AGRICOLÂNDIA | PIAUÍ | Brasil | 2200103 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 22d3580f-46bd-3596-b4d2-e911feeeee13 | -3.00867 | -49.43173 | 2025-11-15 04:04:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ef47f37b-cef9-3835-ae3d-d2cbbaa6de4d | -6.7329 | -42.95568 | 2025-11-15 04:04:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| fca1fe6b-4934-38c4-b9d1-7421fbb98b68 | -4.38775 | -50.42891 | 2025-11-15 04:04:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e5db25e8-5318-3270-8138-3b74a4139d5c | -4.10558 | -48.01143 | 2025-11-15 04:04:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| b9674142-53b6-33c0-8be9-f6a58e565900 | -5.89335 | -42.74759 | 2025-11-15 04:04:00 | NPP-375D | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| fd02a321-0ade-3dce-b7d7-e419f66aa29d | -4.32922 | -47.57761 | 2025-11-15 04:04:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b816c7b9-735c-351c-8336-513932ce5c75 | -5.72075 | -42.91533 | 2025-11-15 04:04:00 | NPP-375D | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| f3e7179e-8170-3512-8290-8e29fd1ff622 | -3.76358 | -47.74411 | 2025-11-15 04:04:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 8394f0c5-f392-3c89-833b-8c052203e82d | -5.51965 | -40.974 | 2025-11-15 04:04:00 | NPP-375D | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 4.1 |
| b4cd522a-a8be-33d1-b617-445900f17a84 | -3.89513 | -43.81907 | 2025-11-15 04:04:00 | NPP-375D | VARGEM GRANDE | MARANHÃO | Brasil | 2112704 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| dfc3873f-724f-3a19-8d41-3ab36237f6c5 | -3.28196 | -51.5447 | 2025-11-15 04:04:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| d369ca12-13d6-3931-9a66-f4915226238a | -3.22005 | -45.48466 | 2025-11-15 04:04:00 | NPP-375D | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | 3.4 |
| fbe68596-c267-38af-b909-325f32f6c30b | -7.4416 | -42.77294 | 2025-11-15 04:04:00 | NPP-375D | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 23824a1b-4e51-334f-a26c-77a5074599ab | -6.36069 | -35.21286 | 2025-11-15 04:04:00 | NPP-375D | CANGUARETAMA | RIO GRANDE DO NORTE | Brasil | 2402204 | 24 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 33af3144-a0a7-3095-95b4-590a40b1e371 | -6.81825 | -48.824 | 2025-11-15 04:04:00 | NPP-375D | ARAGOMINAS | TOCANTINS | Brasil | 1701309 | 17 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 4ad3eb50-0f00-33c3-8b87-12aabf7a4a3d | -5.42656 | -40.6657 | 2025-11-15 04:04:00 | NPP-375D | CRATEÚS | CEARÁ | Brasil | 2304103 | 23 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 95d2bd4b-73d5-36f2-9ea7-1b3432e8d228 | -6.27473 | -41.75381 | 2025-11-15 04:04:00 | NPP-375D | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 1a91cc8e-621e-380f-896e-19c5f03d7718 | -6.72282 | -42.94983 | 2025-11-15 04:04:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 4.7 |
| ff4d400c-a797-31e0-a0b3-cb6f70126661 | -3.65349 | -44.79899 | 2025-11-15 04:04:00 | NPP-375D | VITÓRIA DO MEARIM | MARANHÃO | Brasil | 2112902 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 68a63fa5-3a3c-315b-b690-1c91e7d000ce | -5.42612 | -42.58552 | 2025-11-15 04:04:00 | NPP-375D | LAGOA DO PIAUÍ | PIAUÍ | Brasil | 2205581 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 4f140a06-f2d1-31c4-b510-fc05fee8e717 | -5.62197 | -42.81114 | 2025-11-15 04:04:00 | NPP-375D | CURRALINHOS | PIAUÍ | Brasil | 2203255 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 51559eac-48d7-3507-9f89-79f79f7b9806 | -2.79362 | -52.97662 | 2025-11-15 04:04:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 438c1deb-57d1-3227-9acb-11bc3c4c142b | -4.17496 | -50.42408 | 2025-11-15 04:04:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 893229ca-1f6b-3f05-b7d5-674253d40c68 | -6.01783 | -41.95974 | 2025-11-15 04:04:00 | NPP-375D | SANTA CRUZ DOS MILAGRES | PIAUÍ | Brasil | 2209153 | 22 | 33 | nan | nan | nan | Caatinga | 4.4 |
| 98240a91-af65-3f93-8346-b7299074ead0 | -7.42988 | -45.2268 | 2025-11-15 04:04:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 5b83ee80-7e29-3574-ad7c-4fcf909077ec | -7.08186 | -41.58116 | 2025-11-15 04:04:00 | NPP-375D | PICOS | PIAUÍ | Brasil | 2208007 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 18704588-15ab-3023-97db-c73c19b06c9b | -2.8692 | -51.4721 | 2025-11-15 04:04:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d517ac71-2f04-321f-a91a-6bca1ac54a68 | -5.12933 | -44.88707 | 2025-11-15 04:04:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 780237d7-9e44-3825-aefe-51a343a01d39 | -4.19516 | -45.45293 | 2025-11-15 04:04:00 | NPP-375D | ALTAMIRA DO MARANHÃO | MARANHÃO | Brasil | 2100402 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| bf88923d-8b5f-3f08-913b-5d52f6e08943 | -4.43354 | -43.66151 | 2025-11-15 04:04:00 | NPP-375D | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 0351037d-dbf9-39ec-bb4f-af329ffa4d6f | -6.09288 | -41.60372 | 2025-11-15 04:04:00 | NPP-375D | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 389382d6-a5fd-3e55-a18c-dbdbfd73ee95 | -3.26543 | -50.09167 | 2025-11-15 04:04:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 657ed4d5-f534-304c-81d0-0ba78c4b5bd6 | -5.7281 | -42.36513 | 2025-11-15 04:04:00 | NPP-375D | PASSAGEM FRANCA DO PIAUÍ | PIAUÍ | Brasil | 2207751 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 73de2f1e-c30c-3bd4-ab02-8f1971dfaf84 | -5.89172 | -42.27011 | 2025-11-15 04:04:00 | NPP-375D | SÃO MIGUEL DA BAIXA GRANDE | PIAUÍ | Brasil | 2210383 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| b38adc93-b3c2-39ee-a092-05bbb56eed00 | -7.71251 | -35.98122 | 2025-11-15 04:04:00 | NPP-375D | SANTA CECÍLIA | PARAÍBA | Brasil | 2513158 | 25 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 14472b4a-d9ad-33a4-8793-41d8511db825 | -3.26799 | -43.61333 | 2025-11-15 04:04:00 | NPP-375D | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| aa4e725d-ad83-3a10-a8f9-3e3ba72407c9 | -3.12566 | -45.17929 | 2025-11-15 04:04:00 | NPP-375D | VIANA | MARANHÃO | Brasil | 2112803 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| d44e235a-798a-325d-9ffa-27aefef52d1b | -2.15354 | -48.29082 | 2025-11-15 04:04:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| b19ae3eb-142e-3c2e-991a-01717773be3f | -4.42347 | -43.39561 | 2025-11-15 04:04:00 | NPP-375D | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 49f9ab83-951a-35e9-ab3c-8ee3bc71981c | -4.94986 | -37.3889 | 2025-11-15 04:04:00 | NPP-375D | MOSSORÓ | RIO GRANDE DO NORTE | Brasil | 2408003 | 24 | 33 | nan | nan | nan | Caatinga | 0.8 |
| e4e417c3-5485-31e4-a4cd-afbe07b96dfa | -5.08925 | -43.28898 | 2025-11-15 04:04:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 9a8569d2-cb66-3428-ad53-70077d78b0af | -4.59705 | -44.31621 | 2025-11-15 04:04:00 | NPP-375D | CAPINZAL DO NORTE | MARANHÃO | Brasil | 2102754 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 4f562fad-7235-3f11-9940-584a21ef3836 | -4.10733 | -50.05737 | 2025-11-15 04:04:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| bd41eb75-28ad-3528-9ddf-532d7b42a6c7 | -5.65835 | -41.08775 | 2025-11-15 04:04:00 | NPP-375D | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 7.7 |
| 6d0d2874-d44e-35b3-b13e-e49543da3163 | -7.10846 | -39.08076 | 2025-11-15 04:04:00 | NPP-375D | AURORA | CEARÁ | Brasil | 2301703 | 23 | 33 | nan | nan | nan | Caatinga | 3.1 |
| 08762d46-4414-3315-9d36-47fa6efe0896 | -6.16026 | -48.04362 | 2025-11-15 04:04:00 | NPP-375D | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 13bc5c4b-559f-35f2-9f30-163c1827e871 | -11.32498 | -48.50879 | 2025-11-15 04:06:00 | NPP-375D | BREJINHO DE NAZARÉ | TOCANTINS | Brasil | 1703701 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 1ff44658-a693-3123-b1b4-9e8404f0cc83 | -12.75897 | -43.64761 | 2025-11-15 04:06:00 | NPP-375D | SERRA DOURADA | BAHIA | Brasil | 2930303 | 29 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 47de07af-d99a-34a4-9b5d-8f37c8f14172 | -11.9178 | -46.1943 | 2025-11-15 04:06:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 01cc0183-5773-352a-88d9-0d8f69f10013 | -12.38853 | -48.10575 | 2025-11-15 04:06:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 396a2485-e85e-375a-b46f-0e55bf598fe4 | -11.71185 | -44.44257 | 2025-11-15 04:06:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 1d403571-9d15-3a7c-bbbb-2724218ae3f8 | -9.7549 | -43.97083 | 2025-11-15 04:06:00 | NPP-375D | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ef7c8121-01c7-3be0-812d-e093aedf9b6e | -7.66887 | -47.20302 | 2025-11-15 04:06:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 69b85b4f-d407-3713-8ae4-8990ffa5ff78 | -11.7921 | -47.40789 | 2025-11-15 04:06:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 7e9dc2f4-6307-3929-8810-a2e8e0df9767 | -8.20527 | -43.56406 | 2025-11-15 04:06:00 | NPP-375D | COLÔNIA DO GURGUÉIA | PIAUÍ | Brasil | 2202752 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 1f4fcd03-e1c5-3d77-9195-bbbde81135eb | -9.00616 | -44.18022 | 2025-11-15 04:06:00 | NPP-375D | SANTA LUZ | PIAUÍ | Brasil | 2209302 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 33448257-ea4a-319a-9443-e5d3e6223877 | -12.78575 | -46.75088 | 2025-11-15 04:06:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 4907e16d-62e3-331c-a1eb-b53a94d1ecd8 | -7.87488 | -48.41391 | 2025-11-15 04:06:00 | NPP-375D | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 0b9ba844-5818-3ced-b7f8-96647e08379f | -7.70816 | -49.3868 | 2025-11-15 04:06:00 | NPP-375D | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| a266519c-bac7-3519-8fff-bc64f2f7972f | -12.66114 | -46.74804 | 2025-11-15 04:06:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 1505b422-1f1a-30f2-bf01-472c9a513a99 | -8.31958 | -45.40395 | 2025-11-15 04:06:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b1db1d94-a45d-3b6b-a248-e22fe9998c27 | -12.84676 | -46.43197 | 2025-11-15 04:06:00 | NPP-375D | COMBINADO | TOCANTINS | Brasil | 1705557 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| baf4f39c-5233-3812-9f6d-3cde0e320498 | -13.48851 | -46.71475 | 2025-11-15 04:06:00 | NPP-375D | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 538e6364-b178-3ff4-a834-7254919a5a35 | -9.44528 | -46.97078 | 2025-11-15 04:06:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 02680def-9adc-32bf-bdac-c3f706719e16 | -9.02634 | -46.8894 | 2025-11-15 04:06:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 7a91e802-0a2d-395b-86ea-eacdbfb96566 | -8.46068 | -45.14383 | 2025-11-15 04:06:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 53872b71-fb53-34c2-a404-843743825a45 | -12.23744 | -49.39363 | 2025-11-15 04:06:00 | NPP-375D | FIGUEIRÓPOLIS | TOCANTINS | Brasil | 1707652 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 1d809fb4-7749-3829-9e25-dfe936d01f19 | -10.70527 | -44.51864 | 2025-11-15 04:06:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 88ee47e4-97e2-3771-a7f7-3e697ad1f979 | -12.65039 | -43.25233 | 2025-11-15 04:06:00 | NPP-375D | SÍTIO DO MATO | BAHIA | Brasil | 2930758 | 29 | 33 | nan | nan | nan | Cerrado | 3.8 |
| f63cc978-904c-3d32-808b-fc8e1ada4678 | -9.26252 | -45.1979 | 2025-11-15 04:06:00 | NPP-375D | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| e94a0c82-9bc3-34df-a955-67ba33867474 | -9.85481 | -44.17482 | 2025-11-15 04:06:00 | NPP-375D | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 249fb933-36cf-3a28-95df-839396da38d0 | -10.62763 | -44.58492 | 2025-11-15 04:06:00 | NPP-375D | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 303452f2-3f12-3d54-95c9-3ae6f638ee35 | -12.40289 | -48.11058 | 2025-11-15 04:06:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |


[Clique aqui para ver as próximas entradas](README25.md)
