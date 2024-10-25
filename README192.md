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

## Dados Diários - Página 192

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 49d10f84-ad1e-3214-9dd2-6a773972b739 | -19.5461 | -56.7192 | 2024-10-25 18:26:54 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 86.3 |
| 0f27a134-c3b9-32dd-bc97-d9970f92ffac | -19.5862 | -56.7136 | 2024-10-25 18:26:55 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 121.9 |
| 6f9eb131-6855-340d-86a9-a53690b085f2 | -19.626 | -56.7289 | 2024-10-25 18:26:55 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 103.4 |
| 1a0917e4-4ccc-3e49-8214-7771d9715be1 | -19.6063 | -56.7108 | 2024-10-25 18:26:55 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 113.9 |
| 81cae4de-61b1-3231-930e-1c3953cf283a | -19.6075 | -56.6478 | 2024-10-25 18:26:55 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 149.7 |
| 34bef796-b671-3f6d-82f2-fa4d24c53c43 | -19.587 | -56.6716 | 2024-10-25 18:26:55 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 133.0 |
| 63b0878c-2dbc-32c7-b4c5-937805d8accd | -19.5666 | -56.6954 | 2024-10-25 18:26:55 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 104.3 |
| 64b58477-a4a8-3772-a20c-d287f7554b87 | -19.6079 | -56.6267 | 2024-10-25 18:26:55 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 124.0 |
| 481b9283-f426-33b9-8665-bdc619f7cd6d | -19.5866 | -56.6926 | 2024-10-25 18:26:55 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 208.8 |
| bcdc05e6-a425-3775-a154-27cbbae54088 | -20.1877 | -57.8626 | 2024-10-25 18:26:58 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 54.4 |
| 05c15003-4210-30b5-88f0-ecf938426cf7 | -1.0368 | -53.5171 | 2024-10-25 18:35:11 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 151.0 |
| 7322b240-05db-3df5-b33e-4b7b24a5b5a8 | -1.382 | -55.847 | 2024-10-25 18:35:13 | GOES-16 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 203.2 |
| 36fb6212-6766-3591-8250-59ebfc374480 | -1.3637 | -55.8472 | 2024-10-25 18:35:13 | GOES-16 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 68.2 |
| da36ccec-9e0e-3497-b9bb-2b6f732fecde | -1.4004 | -55.8468 | 2024-10-25 18:35:13 | GOES-16 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 103.0 |
| 01135937-9d2c-383f-a7a7-d9db936f4946 | -1.4918 | -55.9443 | 2024-10-25 18:35:14 | GOES-16 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 50.3 |
| 675e3e0a-e6fd-3349-8bf0-52338806417e | -2.1829 | -50.502 | 2024-10-25 18:35:18 | GOES-16 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 58.5 |
| b3478f6f-bab6-3624-a76d-783fc7f6edde | -2.3516 | -49.5935 | 2024-10-25 18:35:18 | GOES-16 | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 63.7 |
| fbfd5c41-9ba6-3831-8431-84584d696cd8 | -2.425 | -49.7398 | 2024-10-25 18:35:19 | GOES-16 | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 55.3 |
| 01f54059-2de3-3559-80c3-3f7c7c414c36 | -2.6473 | -49.5013 | 2024-10-25 18:35:20 | GOES-16 | MOCAJUBA | PARÁ | Brasil | 1504604 | 15 | 33 | nan | nan | nan | Amazônia | 70.9 |
| 9ef52360-9a9a-3f71-ae2c-af8083b40af6 | -2.6473 | -49.5225 | 2024-10-25 18:35:20 | GOES-16 | MOCAJUBA | PARÁ | Brasil | 1504604 | 15 | 33 | nan | nan | nan | Amazônia | 69.3 |
| 51951aeb-76ea-3a35-9534-b5738a41c961 | -2.6658 | -49.5008 | 2024-10-25 18:35:20 | GOES-16 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 82.6 |
| a2514daf-dbac-32e3-996b-31911f0b5284 | -3.1281 | -54.266 | 2024-10-25 18:35:23 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 63.0 |
| b8907d31-ff54-3a7c-aa7c-b605aea4937a | -3.1882 | -44.3182 | 2024-10-25 18:35:23 | GOES-16 | SANTA RITA | MARANHÃO | Brasil | 2110203 | 21 | 33 | nan | nan | nan | Amazônia | 69.6 |
| b9bec772-a3e2-3ed8-b23c-8a2389b2811c | -3.0932 | -53.7239 | 2024-10-25 18:35:23 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 98.6 |
| 1dd2157e-3ac8-323a-9d51-cc050081c7ba | -3.3306 | -54.1805 | 2024-10-25 18:35:24 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 48.1 |
| 03bfd67f-b487-3a5e-bc84-5fd795cf4e75 | -3.3041 | -43.5078 | 2024-10-25 18:35:24 | GOES-16 | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 97.2 |
| feea6119-b7c6-3d8e-9976-d2c3cff42a19 | -3.2357 | -50.1805 | 2024-10-25 18:35:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 165.1 |
| ed008758-c4c7-3dbf-940f-d6b20a07eef6 | -3.4951 | -54.4366 | 2024-10-25 18:35:25 | GOES-16 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 233.4 |
| 57b475e7-cf8d-33eb-9c63-76db774c8f40 | -3.5978 | -44.3462 | 2024-10-25 18:35:25 | GOES-16 | CANTANHEDE | MARANHÃO | Brasil | 2102705 | 21 | 33 | nan | nan | nan | Cerrado | 108.5 |
| 1666d8ad-6c87-3327-b72c-6d54d3a0c6e1 | -3.5792 | -44.347 | 2024-10-25 18:35:25 | GOES-16 | CANTANHEDE | MARANHÃO | Brasil | 2102705 | 21 | 33 | nan | nan | nan | Cerrado | 76.9 |
| 34eeb4c1-daf6-3a5f-93db-e7ced7fa8bc9 | -3.597 | -44.4832 | 2024-10-25 18:35:25 | GOES-16 | MATÕES DO NORTE | MARANHÃO | Brasil | 2106631 | 21 | 33 | nan | nan | nan | Cerrado | 64.4 |
| bbad3eee-d46a-3aed-8900-61e6d24a4010 | -3.4767 | -54.4371 | 2024-10-25 18:35:25 | GOES-16 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 86.4 |
| 09350c25-ed12-3610-b07d-6cd79fcb0f67 | -3.756 | -42.8102 | 2024-10-25 18:35:26 | GOES-16 | BREJO | MARANHÃO | Brasil | 2102101 | 21 | 33 | nan | nan | nan | Cerrado | 179.4 |
| 2c346b50-5640-39b8-877e-84c611913a5c | -3.7373 | -42.8112 | 2024-10-25 18:35:26 | GOES-16 | BREJO | MARANHÃO | Brasil | 2102101 | 21 | 33 | nan | nan | nan | Cerrado | 107.2 |
| b35e27a7-ea28-39d7-97e9-adfe0286cc84 | -3.6473 | -45.4994 | 2024-10-25 18:35:26 | GOES-16 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 74.7 |
| fc988458-e0b4-37e5-bc2f-c7dd65efdef2 | -3.8144 | -48.9729 | 2024-10-25 18:35:27 | GOES-16 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 86.3 |
| a619fe0b-888c-3fad-ade6-c355279956ea | -3.8416 | -44.0824 | 2024-10-25 18:35:27 | GOES-16 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 72.0 |
| 1e2950c9-01ff-3bf1-8dfa-e05d58338f5c | -4.029 | -43.9348 | 2024-10-25 18:35:28 | GOES-16 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 74.1 |
| 9646ca6e-9995-3384-badd-02b1426a4aa6 | -3.9462 | -52.2538 | 2024-10-25 18:35:28 | GOES-16 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 74.2 |
| c7dd9d4d-85ec-362f-828d-762c456fbc38 | -4.5772 | -45.61 | 2024-10-25 18:35:31 | GOES-16 | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Cerrado | 59.1 |
| 21c19477-6b0a-37df-8e24-0ef880ebe9f8 | -4.5769 | -45.6549 | 2024-10-25 18:35:31 | GOES-16 | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Amazônia | 66.1 |
| 44379712-fdd9-3f06-ac16-149560d16d3a | -4.7445 | -45.6679 | 2024-10-25 18:35:32 | GOES-16 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 105.7 |
| 08490b7b-d452-3ef7-9c40-7aaac18f1729 | -4.7428 | -45.9143 | 2024-10-25 18:35:32 | GOES-16 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 79.1 |
| aa13d06e-b020-3bc2-8f6f-f73ada6a0217 | -4.8493 | -44.0947 | 2024-10-25 18:35:33 | GOES-16 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 58.7 |
| 9380bf3c-9683-3744-9335-76634aa9b935 | -5.1129 | -43.8471 | 2024-10-25 18:35:34 | GOES-16 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 69.2 |
| 4aacc89d-4ae3-30c8-a6c7-03127d47b623 | -5.3553 | -46.2344 | 2024-10-25 18:35:35 | GOES-16 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Amazônia | 81.3 |
| e443f5ed-b0cc-3efc-85f4-cf882b583232 | -5.3987 | -41.107 | 2024-10-25 18:35:35 | GOES-16 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 107.6 |
| c96e055b-0a6e-3def-86e2-5df6ebec7c51 | -5.5234 | -39.8465 | 2024-10-25 18:35:36 | GOES-16 | PEDRA BRANCA | CEARÁ | Brasil | 2310506 | 23 | 33 | nan | nan | nan | Caatinga | 109.4 |
| b3dee3c0-3669-37cf-a377-d8df61b1d739 | -5.7014 | -45.0199 | 2024-10-25 18:35:37 | GOES-16 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 61.3 |
| 69997aa0-a854-301b-8595-5ca6e7f4ae5f | -5.8016 | -44.2591 | 2024-10-25 18:35:38 | GOES-16 | JATOBÁ | MARANHÃO | Brasil | 2105450 | 21 | 33 | nan | nan | nan | Cerrado | 179.5 |
| 1020f80b-5f1e-3374-93c4-3c359e99e09b | -5.9394 | -47.7607 | 2024-10-25 18:35:39 | GOES-16 | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 44.1 |
| ed530702-f0ea-3f84-b9d8-a56e6e75abf6 | -6.2742 | -47.8471 | 2024-10-25 18:35:41 | GOES-16 | NAZARÉ | TOCANTINS | Brasil | 1714302 | 17 | 33 | nan | nan | nan | Cerrado | 76.0 |
| 37ae126e-ac58-3264-b1d1-1bcb0bb06706 | -6.2744 | -47.8253 | 2024-10-25 18:35:41 | GOES-16 | NAZARÉ | TOCANTINS | Brasil | 1714302 | 17 | 33 | nan | nan | nan | Cerrado | 241.3 |
| db9d8c99-6954-3530-9600-c570567ffe21 | -6.4991 | -42.0471 | 2024-10-25 18:35:42 | GOES-16 | NOVO ORIENTE DO PIAUÍ | PIAUÍ | Brasil | 2206902 | 22 | 33 | nan | nan | nan | Caatinga | 44.7 |
| 033748b6-b233-3f46-9d2f-251b08739070 | -6.7045 | -43.9554 | 2024-10-25 18:35:43 | GOES-16 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 157.6 |
| de6afd59-15ac-386a-8ca6-4a8cdfd5421d | -6.8927 | -38.987 | 2024-10-25 18:35:44 | GOES-16 | AURORA | CEARÁ | Brasil | 2301703 | 23 | 33 | nan | nan | nan | Caatinga | 166.4 |
| fc08dd4d-bdeb-3cdd-afbc-0bb00b48d0df | -7.097 | -39.3174 | 2024-10-25 18:35:45 | GOES-16 | CARIRIAÇU | CEARÁ | Brasil | 2303204 | 23 | 33 | nan | nan | nan | Caatinga | 94.5 |
| 0d4bf781-470d-39e8-a88a-466284af2f45 | -7.0135 | -46.7143 | 2024-10-25 18:35:45 | GOES-16 | FEIRA NOVA DO MARANHÃO | MARANHÃO | Brasil | 2104073 | 21 | 33 | nan | nan | nan | Cerrado | 61.7 |
| 854dae9b-aded-3d80-8e2a-239cc2479e2f | -6.9527 | -47.1834 | 2024-10-25 18:35:45 | GOES-16 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 70.2 |
| 5be62caf-ea01-308d-97d2-76d46015459f | -6.9952 | -46.6714 | 2024-10-25 18:35:45 | GOES-16 | FEIRA NOVA DO MARANHÃO | MARANHÃO | Brasil | 2104073 | 21 | 33 | nan | nan | nan | Cerrado | 180.4 |
| ada76376-4ec0-3067-bc08-d683f0971c0a | -7.1625 | -46.7908 | 2024-10-25 18:35:46 | GOES-16 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 53.9 |
| 9a3a73fe-266b-3718-95e7-31d35490f1d2 | -7.2946 | -44.9589 | 2024-10-25 18:35:46 | GOES-16 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 66.9 |
| 9c804322-c055-3a7e-8548-2be7a977067e | -7.2943 | -44.9817 | 2024-10-25 18:35:46 | GOES-16 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 62.5 |
| 07692464-94c7-3f18-aa9d-3740d87b4605 | -7.2267 | -44.3007 | 2024-10-25 18:35:46 | GOES-16 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 308.5 |
| 2f7f6655-f0f2-327c-acc1-0df93a434d31 | -7.2073 | -47.9087 | 2024-10-25 18:35:46 | GOES-16 | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 80.0 |
| a5774873-a77c-3a15-bc7b-ed014d341085 | -7.1203 | -49.1699 | 2024-10-25 18:35:46 | GOES-16 | SANTA FÉ DO ARAGUAIA | TOCANTINS | Brasil | 1718865 | 17 | 33 | nan | nan | nan | Amazônia | 64.6 |
| 15661ee9-9879-3643-88f0-46c2a997a8a8 | -7.2456 | -44.2989 | 2024-10-25 18:35:46 | GOES-16 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 105.6 |
| 702a2b1d-c2eb-336c-9cf5-82e7e63a209b | -7.3266 | -47.2192 | 2024-10-25 18:35:47 | GOES-16 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 54.7 |
| e7bf5900-d6ca-33e4-9e0c-76ff409ad081 | -7.5289 | -45.8434 | 2024-10-25 18:35:48 | GOES-16 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 88.4 |
| 099fc329-dbe0-3e07-97aa-07b88555bc59 | -7.7068 | -46.7217 | 2024-10-25 18:35:49 | GOES-16 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 48.2 |
| a6097ad6-4b87-36af-ac9f-bc350aa1a593 | -7.8727 | -45.3593 | 2024-10-25 18:35:50 | GOES-16 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 77.0 |
| ed26ceed-1d04-328e-865a-1b1884b97ec6 | -9.2024 | -43.3429 | 2024-10-25 18:35:57 | GOES-16 | CARACOL | PIAUÍ | Brasil | 2202505 | 22 | 33 | nan | nan | nan | Caatinga | 161.9 |
| 666577ad-8db9-3975-9431-4f5348d79e3e | -9.4699 | -43.215 | 2024-10-25 18:35:58 | GOES-16 | CAMPO ALEGRE DE LOURDES | BAHIA | Brasil | 2905909 | 29 | 33 | nan | nan | nan | Caatinga | 121.8 |
| 6df6f23c-5528-3efa-8619-388dacba1dcb | -9.3076 | -45.2527 | 2024-10-25 18:35:58 | GOES-16 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 60.8 |
| 87e5948b-248a-3ba7-8fbb-7e90166e829d | -9.9215 | -44.7431 | 2024-10-25 18:36:01 | GOES-16 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 114.7 |
| cf1ae092-c7db-3dd3-a55b-d2da3d39225d | -9.9954 | -48.8473 | 2024-10-25 18:36:02 | GOES-16 | BARROLÂNDIA | TOCANTINS | Brasil | 1703107 | 17 | 33 | nan | nan | nan | Cerrado | 112.8 |
| 57f708a0-36bb-39dd-9323-0e5034bae3dc | -10.3657 | -44.292 | 2024-10-25 18:36:03 | GOES-16 | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 91.9 |
| 53853669-b3eb-35c1-b644-0f72281e38bf | -10.6249 | -55.9757 | 2024-10-25 18:36:06 | GOES-16 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 118.4 |
| 00b8f476-bfc4-3163-890d-43b595d0c8da | -11.9028 | -43.8348 | 2024-10-25 18:36:12 | GOES-16 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 110.9 |
| 93f245c4-78ce-33aa-a0c3-b21162b7d83e | -12.9254 | -42.7827 | 2024-10-25 18:36:17 | GOES-16 | MACAÚBAS | BAHIA | Brasil | 2919801 | 29 | 33 | nan | nan | nan | Caatinga | 98.1 |
| c6176b45-a4bf-3dd2-9343-a7a1b38659c7 | -13.7544 | -42.9918 | 2024-10-25 18:36:22 | GOES-16 | MATINA | BAHIA | Brasil | 2921054 | 29 | 33 | nan | nan | nan | Caatinga | 113.4 |
| a55209b7-70e4-3174-9ecf-0f2abec67f99 | -13.9457 | -41.4166 | 2024-10-25 18:36:23 | GOES-16 | ITUAÇU | BAHIA | Brasil | 2917201 | 29 | 33 | nan | nan | nan | Caatinga | 78.8 |
| 0520fab3-b2c3-3d85-8c20-46f0523477b2 | -14.4169 | -42.1331 | 2024-10-25 18:36:25 | GOES-16 | RIO DO ANTÔNIO | BAHIA | Brasil | 2926806 | 29 | 33 | nan | nan | nan | Caatinga | 91.3 |
| d48e8492-9c80-3e1f-b21a-3d786c221e04 | -17.7634 | -57.5937 | 2024-10-25 18:36:45 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 196.9 |
| ac4d4883-3814-39dc-aebe-b657c299f04c | -17.7637 | -57.5732 | 2024-10-25 18:36:45 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 145.0 |
| 287b5264-771e-3d94-999e-e0dd46d57aad | -17.764 | -57.5526 | 2024-10-25 18:36:45 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 138.6 |
| 5bbcfafb-a501-3193-843c-3f72a01458d1 | -19.5272 | -56.6591 | 2024-10-25 18:36:54 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 130.0 |
| d62c4ccd-33ef-3d3f-8b7e-091251312126 | -19.7061 | -56.7386 | 2024-10-25 18:36:55 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 85.0 |
| 482cf957-7f0d-3156-a42a-bb1600f26c59 | -19.7266 | -56.7147 | 2024-10-25 18:36:55 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 89.3 |
| c74f7907-58aa-3a71-adcd-ad5f8f766005 | -19.6453 | -56.7681 | 2024-10-25 18:36:55 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 114.2 |
| 66a4f484-dcc9-3799-b1a6-bdcdb8067a4c | -19.6245 | -56.8129 | 2024-10-25 18:36:55 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 92.0 |
| 16904804-37de-3991-baa5-666d920b885d | -19.587 | -56.6716 | 2024-10-25 18:36:55 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 135.5 |
| f1e242ce-4517-38e5-b796-5bbbb6577006 | -19.6655 | -56.7653 | 2024-10-25 18:36:55 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 91.0 |
| 261ad63a-3eed-37eb-bb21-ecf9b3803bb6 | -1.1834 | -53.6771 | 2024-10-25 18:45:12 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 66.7 |
| dd4f54d6-6915-3ee5-9094-df264e66ec54 | -1.2762 | -52.9275 | 2024-10-25 18:45:12 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 56.4 |
| d9598a36-5c84-3d36-897c-72b52de2346a | -1.382 | -55.847 | 2024-10-25 18:45:13 | GOES-16 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 186.8 |
| f47a0c9c-46fb-309d-8cde-a33e6ae4e78d | -1.3637 | -55.8472 | 2024-10-25 18:45:13 | GOES-16 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 64.3 |
| cbcfedd6-db0a-35ea-8c80-b620620d5a5a | -1.4004 | -55.8468 | 2024-10-25 18:45:13 | GOES-16 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 97.5 |
| 76337c88-03ae-3a2a-87ad-de51b5adda5c | -2.023 | -55.8981 | 2024-10-25 18:45:17 | GOES-16 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 63.7 |
| 09a8fe57-c1de-30e3-bbf1-f3b6cf7aa37a | -2.0484 | -52.6926 | 2024-10-25 18:45:17 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 94.6 |


[Clique aqui para ver as próximas entradas](README193.md)
