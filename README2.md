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

## Dados Diários - Página 2

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 3e1e0f0e-c05a-3aac-9f10-38d6f611ed50 | -8.2293 | -43.9459 | 2025-10-19 00:10:00 | GOES-19 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 34.2 |
| f86ff595-4e2b-3d40-a18d-dbb7d19f6027 | -8.2476 | -43.9903 | 2025-10-19 00:10:00 | GOES-19 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 66.6 |
| ea1188ed-9da5-302d-a9ae-539ca89b0f7c | -5.1138 | -46.138 | 2025-10-19 00:10:00 | GOES-19 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 135.2 |
| b59ab270-8e4d-31ae-9d68-2c4750c5d407 | -12.5072 | -45.4173 | 2025-10-19 00:10:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 68.4 |
| 16a37948-61fe-3947-afb8-f396940f9c81 | -17.8578 | -40.1263 | 2025-10-19 00:10:00 | GOES-19 | MUCURI | BAHIA | Brasil | 2922003 | 29 | 33 | nan | nan | nan | Mata Atlântica | 71.3 |
| 6ac35d82-0e85-3366-9599-2f22ea01db01 | -5.5525 | -44.9395 | 2025-10-19 00:10:00 | GOES-19 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 57.0 |
| 252777ee-b002-3388-af41-1b12eadb0e5d | -7.6238 | -60.9212 | 2025-10-19 00:10:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 80.3 |
| 9818660f-5e18-3d4c-9c67-373e3642d026 | -13.2214 | -44.3711 | 2025-10-19 00:10:00 | GOES-19 | SANTA MARIA DA VITÓRIA | BAHIA | Brasil | 2928109 | 29 | 33 | nan | nan | nan | Cerrado | 58.1 |
| 0e43bc32-8991-3388-bd97-ad253b19c88d | -5.5524 | -44.9622 | 2025-10-19 00:10:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 66.1 |
| bcaf3801-3ef1-3b5a-b833-28a89bdcf8f8 | -5.3665 | -47.2063 | 2025-10-19 00:10:00 | GOES-19 | SENADOR LA ROCQUE | MARANHÃO | Brasil | 2111763 | 21 | 33 | nan | nan | nan | Amazônia | 59.1 |
| f5f91a4c-b713-3122-8f28-46105eb90ef5 | -2.9128 | -52.7146 | 2025-10-19 00:10:00 | GOES-19 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 69.8 |
| 7c35c9a2-a65d-36f4-a34f-78121fd482f7 | -12.2465 | -49.3896 | 2025-10-19 00:10:00 | GOES-19 | FIGUEIRÓPOLIS | TOCANTINS | Brasil | 1707652 | 17 | 33 | nan | nan | nan | Cerrado | 74.8 |
| 1698adcb-d78d-3647-95d6-da421e36605f | -8.4534 | -44.1303 | 2025-10-19 00:10:00 | GOES-19 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 116.6 |
| 3779bf05-3882-315c-b5c5-6fb36cb2d912 | -4.248 | -44.6787 | 2025-10-19 00:10:00 | GOES-19 | BACABAL | MARANHÃO | Brasil | 2101202 | 21 | 33 | nan | nan | nan | Cerrado | 57.1 |
| 82e3d1b3-4915-33ba-b59d-dd1490448ae0 | -4.1851 | -45.7877 | 2025-10-19 00:10:00 | GOES-19 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 77.5 |
| fe9b172e-9b31-3298-b1d0-6b68c84e1255 | -5.8913 | -44.6875 | 2025-10-19 00:10:00 | GOES-19 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 90.4 |
| 4016a84d-2dcd-3cbc-b63a-c2aefdec4c31 | -2.7026 | -49.5422 | 2025-10-19 00:10:00 | GOES-19 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 69.7 |
| 4a14eb8b-ff7e-3a3a-bcb3-50f8c7754de8 | -5.2898 | -45.0934 | 2025-10-19 00:10:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 63.1 |
| 5b6c121c-a264-3da7-9762-8ac7a43c8fe4 | -11.78 | -47.5583 | 2025-10-19 00:10:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 83.0 |
| bdc7043b-bc5d-3077-9d4c-b821f2b0a7db | -12.2274 | -49.392 | 2025-10-19 00:10:00 | GOES-19 | FIGUEIRÓPOLIS | TOCANTINS | Brasil | 1707652 | 17 | 33 | nan | nan | nan | Cerrado | 72.3 |
| 912da802-9b4a-38eb-ad69-8fa15d5fb582 | -5.6472 | -44.7964 | 2025-10-19 00:20:00 | GOES-19 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 68.2 |
| a5abf6ff-5067-3e19-a1cd-af6d0b2b6aa7 | -4.28 | -45.4913 | 2025-10-19 00:20:00 | GOES-19 | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 107.0 |
| 2366a25a-b79b-359e-b118-96e9f6650344 | -10.5518 | -43.3998 | 2025-10-19 00:20:00 | GOES-19 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 253.6 |
| bdf3de10-9719-3199-b759-425a01b861a1 | -5.2899 | -45.0707 | 2025-10-19 00:20:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 59.1 |
| e85e9c7b-8108-37ca-9bdb-62476577c6e9 | -10.5522 | -43.3761 | 2025-10-19 00:20:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 320.1 |
| 19321758-a599-31b4-9b84-1a1e746e8930 | -12.2465 | -49.3896 | 2025-10-19 00:20:00 | GOES-19 | FIGUEIRÓPOLIS | TOCANTINS | Brasil | 1707652 | 17 | 33 | nan | nan | nan | Cerrado | 80.3 |
| e5d6260b-b5bf-3ee1-95cc-24a010b7b760 | -4.8642 | -44.5976 | 2025-10-19 00:20:00 | GOES-19 | SANTO ANTÔNIO DOS LOPES | MARANHÃO | Brasil | 2110302 | 21 | 33 | nan | nan | nan | Cerrado | 103.7 |
| fd243be2-c239-34ed-abd9-df265ccf4b7a | -2.9128 | -52.7146 | 2025-10-19 00:20:00 | GOES-19 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 83.3 |
| 16cb3de2-59a3-3940-b92f-32702825c8ae | -5.3084 | -45.0921 | 2025-10-19 00:20:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 66.3 |
| a9c2753f-472b-3edf-914f-143c45a41b5d | -11.6109 | -44.0678 | 2025-10-19 00:20:00 | GOES-19 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 44.3 |
| a45c8e92-d0e9-3caf-8003-6eeb17745799 | -4.248 | -44.6787 | 2025-10-19 00:20:00 | GOES-19 | BACABAL | MARANHÃO | Brasil | 2101202 | 21 | 33 | nan | nan | nan | Cerrado | 59.8 |
| d6b43b70-a022-3b84-9261-1f299cbe4813 | -4.2802 | -45.4688 | 2025-10-19 00:20:00 | GOES-19 | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 102.8 |
| f0ea1163-eaee-3209-8daa-ba00d5c43885 | -5.6283 | -44.8205 | 2025-10-19 00:20:00 | GOES-19 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 67.0 |
| 2620dbc2-3ba9-3847-9842-bfda81ba2741 | -5.1139 | -46.1157 | 2025-10-19 00:20:00 | GOES-19 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 57.6 |
| 2bfc216a-5be2-3744-b4fd-f7d0895bd9f8 | -10.8891 | -46.0814 | 2025-10-19 00:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 77.9 |
| 3af7eff9-7024-39a8-bf32-6d1623b7e4ed | -5.0951 | -46.1391 | 2025-10-19 00:20:00 | GOES-19 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 144.0 |
| 9d48ba9f-79a0-3186-9c60-8f23ff9a9dd2 | -4.9141 | -45.4107 | 2025-10-19 00:20:00 | GOES-19 | LAGOA GRANDE DO MARANHÃO | MARANHÃO | Brasil | 2105963 | 21 | 33 | nan | nan | nan | Cerrado | 56.5 |
| d075dd44-a37c-3ffe-b9c4-1618baef5688 | 1.7297 | -56.0203 | 2025-10-19 00:20:00 | GOES-19 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 74.6 |
| bad1d6d9-20cb-3ab2-8942-bfb9a1cdadb5 | -5.0953 | -46.1168 | 2025-10-19 00:20:00 | GOES-19 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 83.1 |
| 8c189c74-c414-3383-adc2-8146122c8b9d | -11.6301 | -44.0649 | 2025-10-19 00:20:00 | GOES-19 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 42.2 |
| 37a2e78c-6e21-3baf-b96a-6dbf68e807fe | -8.2476 | -43.9903 | 2025-10-19 00:20:00 | GOES-19 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 76.2 |
| 44b145d1-e7a4-3413-9154-0f4901c8c8d4 | -11.78 | -47.5583 | 2025-10-19 00:20:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 69.9 |
| 1559eb9e-8576-343d-b117-407222068688 | -4.8455 | -44.5988 | 2025-10-19 00:20:00 | GOES-19 | SANTO ANTÔNIO DOS LOPES | MARANHÃO | Brasil | 2110302 | 21 | 33 | nan | nan | nan | Cerrado | 57.2 |
| c5297033-fc5e-33e1-9bd3-6c5fff98ba53 | -13.2209 | -44.3947 | 2025-10-19 00:20:00 | GOES-19 | SANTA MARIA DA VITÓRIA | BAHIA | Brasil | 2928109 | 29 | 33 | nan | nan | nan | Cerrado | 72.5 |
| 72ec010b-47da-32f4-8386-1e04b7b3cb32 | -2.9127 | -52.735 | 2025-10-19 00:20:00 | GOES-19 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 71.2 |
| eadce480-e8d7-3c14-bd2f-51b89cac717b | 1.7481 | -55.9413 | 2025-10-19 00:20:00 | GOES-19 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 94.5 |
| 7d0edc39-84f8-34dc-a07a-b02a7dc9fcf2 | -11.6489 | -44.0854 | 2025-10-19 00:20:00 | GOES-19 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 62.6 |
| 4027771a-3397-30c3-a9d2-89beb2b84ed0 | -4.2987 | -45.4903 | 2025-10-19 00:20:00 | GOES-19 | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 91.4 |
| 5bb85604-df83-34e8-bf6c-eafa382354d9 | -14.4759 | -45.5751 | 2025-10-19 00:20:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 80.3 |
| f93d11d5-ea82-3835-882b-f0d8115857e1 | -13.2214 | -44.3711 | 2025-10-19 00:20:00 | GOES-19 | SANTA MARIA DA VITÓRIA | BAHIA | Brasil | 2928109 | 29 | 33 | nan | nan | nan | Cerrado | 54.5 |
| 11fcc56d-9ad4-36bf-8fc8-c491031e2fb0 | -8.6219 | -40.2058 | 2025-10-19 00:20:00 | GOES-19 | LAGOA GRANDE | PERNAMBUCO | Brasil | 2608750 | 26 | 33 | nan | nan | nan | Caatinga | 79.5 |
| 1b20344a-cc65-3bf0-bd87-c1a85ff4feb7 | 1.7298 | -55.9809 | 2025-10-19 00:20:00 | GOES-19 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 84.6 |
| 66ce7689-cf9e-397d-94a5-523586db68c3 | -5.1138 | -46.138 | 2025-10-19 00:20:00 | GOES-19 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 97.7 |
| e02598c8-5e5c-3d44-a6a9-8083ec5b312a | 1.7297 | -56.0006 | 2025-10-19 00:20:00 | GOES-19 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 79.7 |
| 95a82f8a-262e-333e-b2fd-a2217018c16a | -2.684 | -49.5639 | 2025-10-19 00:20:00 | GOES-19 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 53.9 |
| ad30de81-b658-3e57-be50-3a04a0d95e5d | -5.647 | -44.8192 | 2025-10-19 00:20:00 | GOES-19 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 75.8 |
| 587c27a6-a5ba-3df5-a378-2bde135588b3 | -4.2988 | -45.4678 | 2025-10-19 00:20:00 | GOES-19 | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 87.1 |
| 287c22eb-2445-3635-ae0b-a3214692530a | -12.4682 | -45.4463 | 2025-10-19 00:20:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 93.0 |
| 47a6b000-1359-3e9a-9f69-932fc64d1528 | -8.6223 | -40.1809 | 2025-10-19 00:20:00 | GOES-19 | LAGOA GRANDE | PERNAMBUCO | Brasil | 2608750 | 26 | 33 | nan | nan | nan | Caatinga | 131.2 |
| 1af8959b-8181-3ac0-8795-37bed8a341cc | -5.3105 | -44.8423 | 2025-10-19 00:20:00 | GOES-19 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 89.9 |
| 477163dd-f2c2-3686-91e4-900e77147879 | -5.3086 | -45.0695 | 2025-10-19 00:20:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 74.3 |
| 6c309e8c-73b4-3841-ae77-e3cab9d14dd9 | -2.7026 | -49.5422 | 2025-10-19 00:20:00 | GOES-19 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 77.2 |
| 87fdf991-4a51-3309-b13c-1a5d1948eae6 | -7.6238 | -60.9212 | 2025-10-19 00:20:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 83.0 |
| 084f43bb-b30b-329f-bc3f-51a5db925787 | 1.7481 | -55.9807 | 2025-10-19 00:20:00 | GOES-19 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 76.6 |
| 9a0b0896-6760-3e31-8889-6b4bf9d21815 | 1.7481 | -55.961 | 2025-10-19 00:20:00 | GOES-19 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 127.8 |
| b057fa09-643d-35e4-9ad7-687a72f22c7a | -8.2287 | -43.9924 | 2025-10-19 00:20:00 | GOES-19 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 35.2 |
| 7185aa15-0635-3ef4-b4b0-f754f0ef3464 | -12.2274 | -49.392 | 2025-10-19 00:20:00 | GOES-19 | FIGUEIRÓPOLIS | TOCANTINS | Brasil | 1707652 | 17 | 33 | nan | nan | nan | Cerrado | 82.7 |
| bf6b5ee4-f11e-3803-b98f-be3efb361738 | -8.4345 | -44.1324 | 2025-10-19 00:20:00 | GOES-19 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 262.6 |
| a3a1c040-0530-38dc-9b50-6c2a6dcc87d1 | -5.5524 | -44.9622 | 2025-10-19 00:20:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 60.7 |
| e6375dd6-b980-3f5f-af02-7d2f47acbda7 | -5.6285 | -44.7977 | 2025-10-19 00:20:00 | GOES-19 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 60.7 |
| b99d8b4e-a0ab-3c85-8a55-39366263c2d2 | -8.4342 | -44.1556 | 2025-10-19 00:20:00 | GOES-19 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 249.8 |
| 78d6c475-5a0f-315d-8fa4-c24bfcfa1550 | -5.3291 | -44.8411 | 2025-10-19 00:20:00 | GOES-19 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 59.7 |
| a7c4338e-b3ab-39da-a20f-9f8ad453d57d | -11.6297 | -44.0884 | 2025-10-19 00:20:00 | GOES-19 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 48.0 |
| 4c3f3d06-1507-3a89-adef-eef2a16f1fbc | -10.2422 | -44.8866 | 2025-10-19 00:20:00 | GOES-19 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 102.6 |
| 2415f6cb-56af-3403-aa2e-2b5ea36fcb9d | -2.6841 | -49.5427 | 2025-10-19 00:20:00 | GOES-19 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 104.6 |
| dde652d0-e0f9-3ec8-a613-ed273fa3841d | -12.4686 | -45.4232 | 2025-10-19 00:20:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 96.3 |
| 93315ed5-885f-3829-9110-7380cf5ee557 | -10.571 | -43.3971 | 2025-10-19 00:20:00 | GOES-19 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 300.9 |
| 4dc5d7b2-de30-3376-a5e1-9683d012b5fa | -9.1174 | -65.359 | 2025-10-19 00:20:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 62.9 |
| 633c426b-e4d3-349f-8269-9dd95e161093 | -8.2101 | -43.9712 | 2025-10-19 00:20:00 | GOES-19 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 26.7 |
| 72e69e34-94d7-39b3-81ad-d931816ae321 | -10.5714 | -43.3734 | 2025-10-19 00:20:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 345.6 |
| e2619071-3a3a-3bd7-814f-386b1067fa84 | -13.2209 | -44.3947 | 2025-10-19 00:30:00 | GOES-19 | SANTA MARIA DA VITÓRIA | BAHIA | Brasil | 2928109 | 29 | 33 | nan | nan | nan | Cerrado | 58.2 |
| 98b43722-21ab-3ba3-868a-119ff3108ffd | -11.6301 | -44.0649 | 2025-10-19 00:30:00 | GOES-19 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 51.1 |
| 92199d85-c391-3f81-b1db-4e1c308c8db5 | -5.3291 | -44.8411 | 2025-10-19 00:30:00 | GOES-19 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 55.3 |
| 9bd7da6b-6fe9-3cbe-8ccb-cbce078c1e41 | -10.5522 | -43.3761 | 2025-10-19 00:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 237.6 |
| 6b8b95a1-af52-37a0-bd80-51296343733b | -4.2988 | -45.4678 | 2025-10-19 00:30:00 | GOES-19 | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 60.0 |
| f325f204-d06e-3e35-902b-718c98bd15a2 | -11.6297 | -44.0884 | 2025-10-19 00:30:00 | GOES-19 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 51.0 |
| 567dd3a6-948c-3e2a-979f-e5eb4e89bb1f | -2.684 | -49.5639 | 2025-10-19 00:30:00 | GOES-19 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 58.5 |
| f4fbc7d0-63ec-3e22-8c58-d839f2cf58b1 | -2.9127 | -52.735 | 2025-10-19 00:30:00 | GOES-19 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 73.5 |
| a69d53a8-74f1-39f2-a8ab-5f4dcc409e9b | -8.2473 | -44.0136 | 2025-10-19 00:30:00 | GOES-19 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 35.4 |
| e5449f9c-082f-3594-bf4b-82f0e9472b79 | -8.6223 | -40.1809 | 2025-10-19 00:30:00 | GOES-19 | LAGOA GRANDE | PERNAMBUCO | Brasil | 2608750 | 26 | 33 | nan | nan | nan | Caatinga | 97.9 |
| 58c301c2-1d0e-34e6-a636-fb7b9c6a6865 | -4.2987 | -45.4903 | 2025-10-19 00:30:00 | GOES-19 | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 88.1 |
| e8ff8914-5da4-3876-ad8a-4558c75c4c6d | -4.2802 | -45.4688 | 2025-10-19 00:30:00 | GOES-19 | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 92.9 |
| 9c538d53-42b0-3188-a64c-74751aefe042 | -10.571 | -43.3971 | 2025-10-19 00:30:00 | GOES-19 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 72.4 |
| c55bcd2c-e14c-33a3-a288-84e1314893a4 | -5.6285 | -44.7977 | 2025-10-19 00:30:00 | GOES-19 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 69.3 |
| 2a2f6bfc-e286-36d2-9875-4cfcbadae2a8 | -5.6472 | -44.7964 | 2025-10-19 00:30:00 | GOES-19 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 71.8 |
| 7fd6ab47-f1e4-3bb9-93f7-4d1f2c336626 | -5.3086 | -45.0695 | 2025-10-19 00:30:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 83.6 |
| deb3e9bb-f1a7-3a6f-ae1c-91e21e32cb36 | -2.9128 | -52.7146 | 2025-10-19 00:30:00 | GOES-19 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 84.9 |
| df362529-27ae-339a-abb9-c9e2c73af9c0 | -5.3105 | -44.8423 | 2025-10-19 00:30:00 | GOES-19 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 69.4 |
| cc801f57-eedd-3cca-aeaf-7afadfcd5d2c | -10.5714 | -43.3734 | 2025-10-19 00:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 105.3 |
| 4c428061-bb7f-3ef4-8188-d15ee39a490e | -2.7026 | -49.5422 | 2025-10-19 00:30:00 | GOES-19 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 59.9 |


[Clique aqui para ver as próximas entradas](README3.md)
