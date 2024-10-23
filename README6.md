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

## Dados Diários - Página 6

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 617657de-e167-3ff0-b509-d8722cb6048d | -3.64868 | -44.33749 | 2024-10-23 00:48:00 | TERRA_M-M | CANTANHEDE | MARANHÃO | Brasil | 2102705 | 21 | 33 | nan | nan | nan | Cerrado | 5.7 |
| dc69b020-7b8a-37ec-9e4b-fb55e2c87f5f | -3.64726 | -44.32748 | 2024-10-23 00:48:00 | TERRA_M-M | CANTANHEDE | MARANHÃO | Brasil | 2102705 | 21 | 33 | nan | nan | nan | Cerrado | 8.4 |
| 7217ab0a-2e09-3e00-bf3d-6e81215a6ecb | -3.56608 | -49.93743 | 2024-10-23 00:48:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 89b09d11-37f4-3131-8681-6980e56c3988 | -3.56449 | -49.92556 | 2024-10-23 00:48:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 12.3 |
| 8720a1f7-1c85-3873-97b3-456a08b756a3 | -3.56396 | -53.77417 | 2024-10-23 00:48:00 | TERRA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 16.3 |
| 8a2ad0d3-8c49-3a44-9e78-c5d225c2ad2f | -3.5608 | -53.75053 | 2024-10-23 00:48:00 | TERRA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 29.4 |
| d7fd1d43-0e54-3106-9eb9-b50c05fa9ca3 | -3.54588 | -49.93454 | 2024-10-23 00:48:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 17.6 |
| 9be8017e-58bc-3330-804c-5daca3a4d7d4 | -3.54401 | -54.76466 | 2024-10-23 00:48:00 | TERRA_M-M | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 33.3 |
| 9c5058f9-a1d3-3a95-9e05-1889cc8f5d59 | -3.54076 | -54.74221 | 2024-10-23 00:48:00 | TERRA_M-M | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 133.8 |
| ead65e27-d6b8-370f-9615-f9cd7d6a3fdb | -3.54045 | -54.73687 | 2024-10-23 00:48:00 | TERRA_M-M | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 134.5 |
| f93e1dfa-51c9-366c-99f6-c9038c59c56d | -3.51586 | -52.82803 | 2024-10-23 00:48:00 | TERRA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 17.0 |
| d2d27212-f937-32e1-bee4-6a94d6319a0a | -3.51149 | -50.29572 | 2024-10-23 00:48:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 5318a1f0-ca89-3b72-a65b-741cd2184f04 | -3.50985 | -50.28341 | 2024-10-23 00:48:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 8.9 |
| fdecf305-349e-37ab-8c64-64e5d9750553 | -3.50347 | -50.28997 | 2024-10-23 00:48:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 13.8 |
| ee6d0729-8b9f-3063-b4e3-31c4a7844d45 | -3.49487 | -54.15667 | 2024-10-23 00:48:00 | TERRA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 34.9 |
| 3f536bb2-c31c-30ff-94bf-b8f33b10afbf | -3.49097 | -54.16275 | 2024-10-23 00:48:00 | TERRA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 26.0 |
| 71e829e6-a9b1-368a-bba8-8c5343825857 | -3.48749 | -54.13762 | 2024-10-23 00:48:00 | TERRA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 14.8 |
| 61d0a8ca-f607-3470-8d7e-cefafdc083e9 | -3.46747 | -52.86012 | 2024-10-23 00:48:00 | TERRA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 10.1 |
| ce8a5665-393d-3c11-a9c5-654dda8e7580 | -3.46183 | -47.67486 | 2024-10-23 00:48:00 | TERRA_M-M | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 7.6 |
| f4c80206-d7ef-3a3e-8894-2bbdcf24bc1f | -3.44868 | -49.82327 | 2024-10-23 00:48:00 | TERRA_M-M | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| a7f0582f-d6e1-33b7-929b-9cb20921193a | -3.4459 | -50.41253 | 2024-10-23 00:48:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 11.2 |
| 474b8b8c-fe85-3487-a1c8-56789f89b6b1 | -3.42047 | -45.52459 | 2024-10-23 00:48:00 | TERRA_M-M | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 4.2 |
| c3c3d3bd-07e0-3817-89ec-66af59ec0b8a | -3.40521 | -44.50223 | 2024-10-23 00:48:00 | TERRA_M-M | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 4d483080-87de-39cb-8f96-119f8d3aad13 | -3.40008 | -44.15823 | 2024-10-23 00:48:00 | TERRA_M-M | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 25.7 |
| eb7d6131-24a0-33c3-9cf1-f1724f0ac4db | -3.35346 | -50.32996 | 2024-10-23 00:48:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 12.4 |
| b3be2a63-105c-359c-ab0f-e35bb9450305 | -3.35177 | -50.31737 | 2024-10-23 00:48:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 26.8 |
| db519982-df20-3eb7-a3e1-6e1bdba6367e | -3.34002 | -49.0135 | 2024-10-23 00:48:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 11.4 |
| 610bbefc-799e-37df-9219-2b3e053d420e | -3.33617 | -49.01989 | 2024-10-23 00:48:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 10.7 |
| bd5e9ce7-b7f2-319a-afc2-c5ff5dfc2535 | -3.33473 | -49.0096 | 2024-10-23 00:48:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 16.6 |
| 0f20c3ed-1638-32d3-8933-e60dd1523b5c | -3.32828 | -46.11512 | 2024-10-23 00:48:00 | TERRA_M-M | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 5.7 |
| e9833ef9-3ae8-3b68-8185-4beae3494e22 | -3.31289 | -47.19873 | 2024-10-23 00:48:00 | TERRA_M-M | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 39299123-a69e-3065-989b-f6dcce2294b6 | -3.31166 | -47.18985 | 2024-10-23 00:48:00 | TERRA_M-M | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 18.5 |
| f93c90d2-5a65-3236-acbe-40e19a6cc192 | -3.30724 | -47.028 | 2024-10-23 00:48:00 | TERRA_M-M | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 25.7 |
| f5036d9e-d42d-3e85-bb43-c3108ef84868 | -3.30602 | -47.01918 | 2024-10-23 00:48:00 | TERRA_M-M | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 28.4 |
| 594e2f4f-608e-38ee-9640-3b848aa2c3de | -3.3028 | -47.1911 | 2024-10-23 00:48:00 | TERRA_M-M | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 83c109a9-c881-3d0b-b767-a2cbb2690c8a | -3.30231 | -44.15321 | 2024-10-23 00:48:00 | TERRA_M-M | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Amazônia | 47.5 |
| 20c19c00-3d3f-32ca-b709-8178c9ef742c | -3.29839 | -47.02925 | 2024-10-23 00:48:00 | TERRA_M-M | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 10.3 |
| 6e120351-c5c3-3084-81f6-45d5dd89b5a2 | -3.28572 | -46.082 | 2024-10-23 00:48:00 | TERRA_M-M | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 42.2 |
| 4b8818d7-3878-399e-a0f1-81a07ec9f984 | -3.27957 | -51.40545 | 2024-10-23 00:48:00 | TERRA_M-M | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 14.2 |
| 3e40061e-ba63-3a9e-9cfa-528c822f8b7b | -3.26453 | -49.1354 | 2024-10-23 00:48:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 4067083e-adaa-337e-9731-11a920dbd50f | -3.25983 | -50.16141 | 2024-10-23 00:48:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 81fab9ad-5fc3-3748-8982-944aa79dea63 | -3.25819 | -50.14936 | 2024-10-23 00:48:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 7.8 |
| 29132349-5051-3e95-99c9-24fcca8626ce | -3.25287 | -50.18695 | 2024-10-23 00:48:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 28.2 |
| 93794511-74a7-3c2f-a0be-406ba44aba63 | -3.25123 | -50.17491 | 2024-10-23 00:48:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 23.5 |
| cb0385e8-7952-30de-852b-d62ab3d8f2c9 | -3.24261 | -50.18838 | 2024-10-23 00:48:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 26.1 |
| 6936d40d-1a3c-391a-b932-1f9de2ecafca | -3.24098 | -50.17633 | 2024-10-23 00:48:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 29.3 |
| c895e214-23e2-369c-ac0a-841117364bce | -3.23756 | -44.41689 | 2024-10-23 00:48:00 | TERRA_M-M | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Amazônia | 36.9 |
| cbc49b18-36c3-3304-b3b9-f1a51491b075 | -3.23571 | -49.6062 | 2024-10-23 00:48:00 | TERRA_M-M | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| a8a8eeb9-a0c9-3701-b940-26edc4569f11 | -3.23423 | -49.59512 | 2024-10-23 00:48:00 | TERRA_M-M | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 8.4 |
| 5779c566-a83f-3e23-a4f7-c76fd09c6f9d | -3.23342 | -49.60094 | 2024-10-23 00:48:00 | TERRA_M-M | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 10.7 |
| fcc1fb75-f2c7-36cc-befc-f23611082d0d | -3.22809 | -49.11506 | 2024-10-23 00:48:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 9.2 |
| 084731aa-9d5f-35c7-a41b-e91969c955cb | -3.22098 | -46.21463 | 2024-10-23 00:48:00 | TERRA_M-M | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 8.2 |
| dd5db70b-800f-375c-b7f5-857084acff7b | -3.21977 | -46.52897 | 2024-10-23 00:48:00 | TERRA_M-M | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 747bf5cb-7128-35dd-9e40-1ed43dbfb1d8 | -3.20757 | -50.29893 | 2024-10-23 00:48:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 8.5 |
| 61268975-780c-32a9-ae43-08104b944d52 | -3.17117 | -48.37634 | 2024-10-23 00:48:00 | TERRA_M-M | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 7.9 |
| dff67655-bd6b-3d14-9b54-e54347bf1234 | -3.16584 | -50.38026 | 2024-10-23 00:48:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 9.0 |
| cb926128-7f2a-37e0-9abe-e355a99f3724 | -3.11845 | -46.65663 | 2024-10-23 00:48:00 | TERRA_M-M | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 19.0 |
| 5205a91a-81e6-3ada-9dd5-2bfbad8952a5 | -3.11316 | -45.30689 | 2024-10-23 00:48:00 | TERRA_M-M | VIANA | MARANHÃO | Brasil | 2112803 | 21 | 33 | nan | nan | nan | Amazônia | 139.6 |
| 17cadb31-a6c1-3bdf-aa6e-d0484da40e59 | -3.11185 | -45.29765 | 2024-10-23 00:48:00 | TERRA_M-M | VIANA | MARANHÃO | Brasil | 2112803 | 21 | 33 | nan | nan | nan | Amazônia | 14.5 |
| 9d48aa8c-2651-3489-8954-a6d4a4df0fd0 | -3.11099 | -54.1623 | 2024-10-23 00:48:00 | TERRA_M-M | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 66.8 |
| 70b7577e-b4fa-3099-bd82-4fd5faa0ef28 | -3.10451 | -54.18278 | 2024-10-23 00:48:00 | TERRA_M-M | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 48.9 |
| cdbe2319-b60d-3fba-8140-5e1be592be42 | -3.10138 | -54.15858 | 2024-10-23 00:48:00 | TERRA_M-M | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 172.3 |
| 1b5c48ae-4034-3d77-b9c2-124480efd50b | -3.09688 | -54.16408 | 2024-10-23 00:48:00 | TERRA_M-M | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 111.2 |
| 04025fd3-4f64-3fb7-aead-b14ee9aba43c | -3.09432 | -45.63248 | 2024-10-23 00:48:00 | TERRA_M-M | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 12.2 |
| 9d665ae6-39ed-38c9-99b7-cd93566dc680 | -3.09359 | -54.14 | 2024-10-23 00:48:00 | TERRA_M-M | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 21.4 |
| 35a35b5f-43f3-305a-a8e4-97d7461e87df | -3.09305 | -45.62344 | 2024-10-23 00:48:00 | TERRA_M-M | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 38.7 |
| 8a224a85-9aec-30a4-991e-5cdb3d0bf0ab | -3.09076 | -45.94077 | 2024-10-23 00:48:00 | TERRA_M-M | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 342a02f4-518b-395e-84df-bfdd01cd9871 | -3.08952 | -45.93187 | 2024-10-23 00:48:00 | TERRA_M-M | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 5d63fccb-b63f-396b-85f7-1f378742016c | -3.07656 | -53.26403 | 2024-10-23 00:48:00 | TERRA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 16.3 |
| 425aa86a-a2d3-3dd2-86ab-f27c4388355a | -3.07627 | -53.24953 | 2024-10-23 00:48:00 | TERRA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 35.9 |
| dd33f520-9527-314c-98b5-6597eda4e584 | -3.07389 | -53.24353 | 2024-10-23 00:48:00 | TERRA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 30.9 |
| 3bd67abf-4d99-3bda-ae85-801026b23ebb | -3.07374 | -50.50717 | 2024-10-23 00:48:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 15.1 |
| b675abd6-4bc8-3e52-816a-69868cd651c8 | -3.06321 | -53.25136 | 2024-10-23 00:48:00 | TERRA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 12.2 |
| d038a6a2-6b41-3cca-a0be-70d9a7719478 | -3.00263 | -48.08519 | 2024-10-23 00:48:00 | TERRA_M-M | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| f5e2e384-72e6-398a-95f9-5455e979e801 | -2.9639 | -48.00556 | 2024-10-23 00:48:00 | TERRA_M-M | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 22.8 |
| d5181d80-58b0-30c4-a905-d17c1f71cd3e | -2.96338 | -50.52821 | 2024-10-23 00:48:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 11.9 |
| 56c56d83-a3d3-38e7-b893-3e7b7dfdb9d6 | -2.95291 | -50.52965 | 2024-10-23 00:48:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 17.4 |
| 2ed1ef43-5008-32d5-90f3-5c8d13c74434 | -2.95118 | -50.51705 | 2024-10-23 00:48:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 11.7 |
| c36f2ecb-5090-3334-80ae-eb4c8d3f6cf9 | -2.87018 | -49.40369 | 2024-10-23 00:48:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 222700b5-eac6-3760-99ee-f939a9b87874 | -2.86777 | -49.45853 | 2024-10-23 00:48:00 | TERRA_M-M | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 10.4 |
| a5a0c08f-2d71-3868-a0fb-bbb44682df3d | -2.84866 | -49.5553 | 2024-10-23 00:48:00 | TERRA_M-M | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 41f507aa-fed1-3f83-8db8-ac1f82d737e8 | -2.84713 | -49.54439 | 2024-10-23 00:48:00 | TERRA_M-M | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 18.9 |
| aca54add-c8af-355f-9259-58760a1805d6 | -2.82526 | -50.50243 | 2024-10-23 00:48:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 8.4 |
| 8904d771-9047-3ded-932b-97353b89e843 | -2.82359 | -50.49002 | 2024-10-23 00:48:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 8.3 |
| f920d695-9c24-378a-825b-1279afeba332 | -2.80729 | -49.61666 | 2024-10-23 00:48:00 | TERRA_M-M | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| d24c2815-2369-3918-b844-b281f707801e | -2.8043 | -49.59476 | 2024-10-23 00:48:00 | TERRA_M-M | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 8.7 |
| d1d295e2-6336-3fa8-a904-c0489e8f27c6 | -2.8028 | -49.58384 | 2024-10-23 00:48:00 | TERRA_M-M | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 18.6 |
| 067e79e1-2484-3fd3-95cb-97283403c70b | -2.79451 | -49.59613 | 2024-10-23 00:48:00 | TERRA_M-M | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 14.5 |
| 3084b248-a66f-3b60-932a-f9eddb005ea6 | -2.79302 | -49.58519 | 2024-10-23 00:48:00 | TERRA_M-M | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 23.8 |
| adacf277-3936-3c04-8694-78cd7908f373 | -2.77394 | -45.97706 | 2024-10-23 00:48:00 | TERRA_M-M | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | 8.3 |
| 5c98e2c3-3d2d-3076-9508-a79b04d9d061 | -2.76505 | -45.97833 | 2024-10-23 00:48:00 | TERRA_M-M | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | 11.1 |
| 05260a39-9707-365e-ac30-ff707eb6ab76 | -2.76475 | -49.30542 | 2024-10-23 00:48:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 30.7 |
| cd08aefd-7b98-3a92-9479-6df87b74f005 | -2.75802 | -49.32785 | 2024-10-23 00:48:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 9.5 |
| cb7f659e-43c9-3fd8-b125-cbadbb06ddd3 | -2.75658 | -49.31728 | 2024-10-23 00:48:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 27.2 |
| 78ec6a7c-fd62-3c27-ad94-a7c7d98bddf7 | -2.7564 | -54.03887 | 2024-10-23 00:48:00 | TERRA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 54.8 |
| 6f3e61fc-c906-33ab-8dc6-0381af2e8306 | -2.75514 | -49.30676 | 2024-10-23 00:48:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 20.8 |
| 93cf38af-67d5-3313-9adc-0e8f2fc4f4bb | -2.74843 | -54.03446 | 2024-10-23 00:48:00 | TERRA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 50.1 |
| 480a4020-a054-314e-a502-1e9ae176cc45 | -2.74697 | -49.31867 | 2024-10-23 00:48:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 8.5 |
| 75c0999e-d2a1-3691-a044-22e0f236f12a | -2.69513 | -49.04761 | 2024-10-23 00:48:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| b2e8eb8c-04d7-3f8b-a2de-75f52fb5b9e0 | -2.68481 | -49.32282 | 2024-10-23 00:48:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 9.2 |


[Clique aqui para ver as próximas entradas](README7.md)
