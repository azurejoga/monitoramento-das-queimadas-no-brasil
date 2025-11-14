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

## Dados Diários - Página 53

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| f61f7123-740d-3038-9ade-7ed42fdc479f | -8.6623 | -45.4834 | 2025-11-14 13:40:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 83.0 |
| 1078e144-c5e4-3764-8d9a-0ed75899e3c8 | -6.1608 | -48.0289 | 2025-11-14 13:40:00 | GOES-19 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 135.7 |
| 53c6b034-eb77-3905-8eaf-10f80904516c | -3.4656 | -41.3283 | 2025-11-14 13:40:00 | GOES-19 | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 91.1 |
| 6dcc21ed-935f-30c0-8daf-046b735aeab5 | -4.6034 | -47.2713 | 2025-11-14 13:40:00 | GOES-19 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 73.6 |
| 8b977c7d-eea8-3962-8fa3-80b7344f29f3 | -7.454 | -42.5728 | 2025-11-14 13:40:00 | GOES-19 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 134.6 |
| dbba2564-5b99-3f11-8bc1-2fe0fa67d77f | -6.5609 | -47.1034 | 2025-11-14 13:40:00 | GOES-19 | SÃO JOÃO DO PARAÍSO | MARANHÃO | Brasil | 2111052 | 21 | 33 | nan | nan | nan | Cerrado | 63.7 |
| 9685d549-7490-34b8-95d3-59c72c41c5cf | -6.0714 | -41.5581 | 2025-11-14 13:40:00 | GOES-19 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 66.9 |
| a0ab94b3-7906-3ef6-9b2e-ca60398988e2 | -5.5447 | -43.678 | 2025-11-14 13:40:00 | GOES-19 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 107.9 |
| 18657288-c4ec-3e34-8732-0abb70b92858 | -5.0156 | -44.3366 | 2025-11-14 13:40:00 | GOES-19 | DOM PEDRO | MARANHÃO | Brasil | 2103802 | 21 | 33 | nan | nan | nan | Cerrado | 75.5 |
| 95221d7b-5afc-3adf-bc76-d9dd84030c92 | -3.9709 | -44.2823 | 2025-11-14 13:40:00 | GOES-19 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 110.5 |
| 2b344202-6352-3323-a939-63f338b27ae6 | -6.0711 | -41.5821 | 2025-11-14 13:40:00 | GOES-19 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 154.6 |
| f69ce9f9-ab7e-32d2-a6e3-b71edc5f2872 | -2.0257 | -47.3239 | 2025-11-14 13:40:00 | GOES-19 | IRITUIA | PARÁ | Brasil | 1503507 | 15 | 33 | nan | nan | nan | Amazônia | 120.0 |
| 37f9eb45-0046-3a2a-923f-91f237c9949e | -4.6744 | -45.0409 | 2025-11-14 13:50:00 | GOES-19 | LAGO DO JUNCO | MARANHÃO | Brasil | 2105807 | 21 | 33 | nan | nan | nan | Cerrado | 65.2 |
| c0a3be4c-8c01-3241-b0a2-2b3b6289cf3b | -1.6063 | -53.2075 | 2025-11-14 13:50:00 | GOES-19 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 133.6 |
| 0f5f275b-32f4-37b6-b800-7e6f62fbe3be | -2.0257 | -47.3239 | 2025-11-14 13:50:00 | GOES-19 | IRITUIA | PARÁ | Brasil | 1503507 | 15 | 33 | nan | nan | nan | Amazônia | 79.4 |
| c047f716-d7c1-3373-813b-f037aa59dddb | -7.454 | -42.5728 | 2025-11-14 13:50:00 | GOES-19 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 130.4 |
| a3b02449-81bd-3ff6-a082-c0d2efea25eb | -9.0214 | -45.4445 | 2025-11-14 13:50:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 97.8 |
| 6cceedb2-d1d7-3615-a97c-be8cd8c6236a | -9.0403 | -45.4424 | 2025-11-14 13:50:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 65.2 |
| 9a47bf09-3cd7-308c-98a5-0343d4664a53 | -4.2717 | -46.8268 | 2025-11-14 13:50:00 | GOES-19 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 103.9 |
| 82f7471e-ed36-3de3-a09a-ab5ad4e9c41d | -7.492 | -42.5452 | 2025-11-14 13:50:00 | GOES-19 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 107.7 |
| c4fe2864-f5e3-3810-b556-33d3d38f9504 | -5.5447 | -43.678 | 2025-11-14 13:50:00 | GOES-19 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 247.8 |
| 84548a92-9c4d-364f-9744-e45d0e82010b | -3.9709 | -44.2823 | 2025-11-14 13:50:00 | GOES-19 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 107.5 |
| 135af0af-1da6-3694-9edc-3813747b508f | -6.5609 | -47.1034 | 2025-11-14 13:50:00 | GOES-19 | SÃO JOÃO DO PARAÍSO | MARANHÃO | Brasil | 2111052 | 21 | 33 | nan | nan | nan | Cerrado | 78.5 |
| 6b9eb000-58b1-333c-99cf-34fe50e2c032 | -7.4728 | -42.5709 | 2025-11-14 14:00:00 | GOES-19 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 134.2 |
| 68076cbe-b6f3-3cd3-975d-410300d7df46 | -4.2715 | -46.8488 | 2025-11-14 14:00:00 | GOES-19 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 272.6 |
| d97fb85e-8de6-330a-bf8e-c234b020ea3e | -3.31 | -42.4083 | 2025-11-14 14:00:00 | GOES-19 | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Cerrado | 80.8 |
| 91f80aa3-2fa3-3067-aa44-f815fa4fff02 | -8.5609 | -46.0363 | 2025-11-14 14:00:00 | GOES-19 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 77.3 |
| ea2e6e63-6a5a-3af3-8bbe-5b06f655b7e8 | -8.6623 | -45.4834 | 2025-11-14 14:00:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 57.9 |
| 9823483a-b348-371f-b49c-dcb1ac4963b9 | -4.2717 | -46.8268 | 2025-11-14 14:00:00 | GOES-19 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 160.5 |
| b08882e5-65ab-3141-8cbf-89df1e67980d | -2.0257 | -47.3239 | 2025-11-14 14:00:00 | GOES-19 | IRITUIA | PARÁ | Brasil | 1503507 | 15 | 33 | nan | nan | nan | Amazônia | 95.8 |
| 17447203-d72e-3261-9292-30d62311c109 | -6.0711 | -41.5821 | 2025-11-14 14:00:00 | GOES-19 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 70.8 |
| 2bfb5b13-4870-3962-a010-0df3d6e02eb3 | -3.9709 | -44.2823 | 2025-11-14 14:00:00 | GOES-19 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 116.3 |
| 5f8f4349-cdef-3e4e-9a1e-74cea19f1d0e | -3.9961 | -43.2418 | 2025-11-14 14:00:00 | GOES-19 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 105.3 |
| dee48e1c-935f-35f5-bf45-9fbc0f910218 | -6.5609 | -47.1034 | 2025-11-14 14:00:00 | GOES-19 | SÃO JOÃO DO PARAÍSO | MARANHÃO | Brasil | 2111052 | 21 | 33 | nan | nan | nan | Cerrado | 59.6 |
| 0a7dd098-1045-3a02-bf97-81ccaa86b9b9 | -5.3442 | -43.0402 | 2025-11-14 14:00:00 | GOES-19 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 77.4 |
| 41708a2a-5013-3948-b78f-f3269a2e1c80 | -3.4212 | -42.5682 | 2025-11-14 14:00:00 | GOES-19 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 163.4 |
| dcebb59c-6c43-3a92-ace7-ee4b2c788091 | -6.2765 | -41.7322 | 2025-11-14 14:10:00 | GOES-19 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 108.4 |
| 1da7c55b-33c0-310d-9f9d-649ae408da22 | -4.6744 | -45.0409 | 2025-11-14 14:10:00 | GOES-19 | LAGO DO JUNCO | MARANHÃO | Brasil | 2105807 | 21 | 33 | nan | nan | nan | Cerrado | 86.5 |
| f61ca31c-1958-3220-80b8-01094e350e68 | -6.1608 | -48.0289 | 2025-11-14 14:10:00 | GOES-19 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 239.2 |
| 695dfe8a-1a15-3952-90b6-6cd3c96e2888 | -6.5609 | -47.1034 | 2025-11-14 14:10:00 | GOES-19 | SÃO JOÃO DO PARAÍSO | MARANHÃO | Brasil | 2111052 | 21 | 33 | nan | nan | nan | Cerrado | 83.0 |
| 49059520-a67e-3b8d-b196-105460799900 | -8.6623 | -45.4834 | 2025-11-14 14:10:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 166.0 |
| 6c456092-1a40-37c9-98a8-1dee1d36f281 | -9.9564 | -44.9459 | 2025-11-14 14:10:00 | GOES-19 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 122.7 |
| 375aa723-447e-3db4-9656-2b1c3618fde3 | -2.2039 | -56.935 | 2025-11-14 14:10:00 | GOES-19 | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | 77.5 |
| 0673fff2-4437-3ed8-baa7-ad4b2aeca778 | -3.6494 | -45.1165 | 2025-11-14 14:10:00 | GOES-19 | IGARAPÉ DO MEIO | MARANHÃO | Brasil | 2105153 | 21 | 33 | nan | nan | nan | Amazônia | 72.3 |
| 8d492055-1d8e-3050-b503-caa3de9c228c | -3.1763 | -42.978 | 2025-11-14 14:10:00 | GOES-19 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 126.7 |
| 7bce72d1-f114-319d-bea6-7ed80751862a | -6.5607 | -47.1254 | 2025-11-14 14:10:00 | GOES-19 | SÃO JOÃO DO PARAÍSO | MARANHÃO | Brasil | 2111052 | 21 | 33 | nan | nan | nan | Cerrado | 50.7 |
| 6580f5f9-2b3c-377c-8bcf-42d5cdd6497c | -7.454 | -42.5728 | 2025-11-14 14:10:00 | GOES-19 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 154.0 |
| be91bd44-8a74-376c-a5b4-48d1d336541a | -9.9567 | -44.9228 | 2025-11-14 14:10:00 | GOES-19 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 123.0 |
| fbf8317c-bb2e-3f66-947b-99c1063e2427 | -7.2092 | -39.4303 | 2025-11-14 14:10:00 | GOES-19 | CRATO | CEARÁ | Brasil | 2304202 | 23 | 33 | nan | nan | nan | Caatinga | 71.2 |
| 2e287e38-2bf4-3413-a114-89e05ea09247 | -2.0257 | -47.3239 | 2025-11-14 14:10:00 | GOES-19 | IRITUIA | PARÁ | Brasil | 1503507 | 15 | 33 | nan | nan | nan | Amazônia | 99.3 |
| 607c88ea-816b-3fb5-8d4d-1548cf6014ba | -6.0711 | -41.5821 | 2025-11-14 14:20:00 | GOES-19 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 77.1 |
| 92bc8e8e-01f1-3876-8758-a065b727c30c | -8.6623 | -45.4834 | 2025-11-14 14:20:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 117.4 |
| 3c6ea587-3596-35f0-af84-4f94934e1bc2 | -14.2284 | -43.5496 | 2025-11-14 14:20:00 | GOES-19 | IUIU | BAHIA | Brasil | 2917334 | 29 | 33 | nan | nan | nan | Cerrado | 107.1 |
| ffc96bc4-7293-349f-8752-356978a4677d | -4.6744 | -45.0409 | 2025-11-14 14:20:00 | GOES-19 | LAGO DO JUNCO | MARANHÃO | Brasil | 2105807 | 21 | 33 | nan | nan | nan | Cerrado | 95.8 |
| 10b87cda-9018-3d90-aa7f-4fd707a5cf4f | -3.6494 | -45.1165 | 2025-11-14 14:20:00 | GOES-19 | IGARAPÉ DO MEIO | MARANHÃO | Brasil | 2105153 | 21 | 33 | nan | nan | nan | Amazônia | 101.0 |
| 553baa44-138a-3853-97b0-7d810366cb86 | -11.6118 | -45.0905 | 2025-11-14 14:20:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 73.4 |
| e4e4f66a-c865-36bd-b248-1a9b8450a3c1 | -4.2717 | -46.8268 | 2025-11-14 14:20:00 | GOES-19 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 296.7 |
| 4caaf405-7b09-3b62-a9aa-6128219f91fc | -3.31 | -42.4083 | 2025-11-14 14:20:00 | GOES-19 | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Cerrado | 80.3 |
| 63b7dd74-4aac-33e9-8a72-368dd1fc4a36 | -8.5609 | -46.0363 | 2025-11-14 14:20:00 | GOES-19 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 111.6 |
| ae3ebcb0-7b22-3651-adae-306700489366 | -4.4955 | -43.955 | 2025-11-14 14:20:00 | GOES-19 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 75.9 |
| 10c82730-d6ad-3136-a05c-02a103aef519 | -9.9564 | -44.9459 | 2025-11-14 14:20:00 | GOES-19 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 98.2 |
| 5b529a8f-95a3-354a-8383-c7f51a762e8b | -3.668 | -45.1156 | 2025-11-14 14:20:00 | GOES-19 | IGARAPÉ DO MEIO | MARANHÃO | Brasil | 2105153 | 21 | 33 | nan | nan | nan | Amazônia | 98.9 |
| 6fa218ad-f6fc-3c07-8eb1-5a5ab09d6122 | -5.5447 | -43.678 | 2025-11-14 14:20:00 | GOES-19 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 112.3 |
| bf992df1-8555-3da5-a0d1-07769d55af49 | -8.5609 | -46.0363 | 2025-11-14 14:30:00 | GOES-19 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 126.5 |
| da9421a8-7786-3742-8318-b89dde03740e | -14.2284 | -43.5496 | 2025-11-14 14:30:00 | GOES-19 | IUIU | BAHIA | Brasil | 2917334 | 29 | 33 | nan | nan | nan | Cerrado | 101.1 |
| c9c54657-fcb8-3747-ae35-bf0ea8bbba6e | -3.6494 | -45.1165 | 2025-11-14 14:30:00 | GOES-19 | IGARAPÉ DO MEIO | MARANHÃO | Brasil | 2105153 | 21 | 33 | nan | nan | nan | Amazônia | 147.9 |
| 7680202e-74c8-3eb9-b679-49b40f3b921c | -11.8677 | -49.2195 | 2025-11-14 14:30:00 | GOES-19 | CARIRI DO TOCANTINS | TOCANTINS | Brasil | 1703867 | 17 | 33 | nan | nan | nan | Cerrado | 60.2 |
| c8a891ea-4e0e-3da1-bf63-d336a91c8421 | -8.6623 | -45.4834 | 2025-11-14 14:30:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 62.5 |
| a1e81ea9-f0c5-3e5e-b296-614a46a2e13f | -9.9564 | -44.9459 | 2025-11-14 14:30:00 | GOES-19 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 90.9 |
| cbc7bd27-81f9-3b15-8d9f-418e012c4ce1 | -11.6118 | -45.0905 | 2025-11-14 14:30:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 71.7 |
| 737fae96-3f25-3870-bcf4-e5cd775da5a7 | -3.1576 | -42.9788 | 2025-11-14 14:30:00 | GOES-19 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 97.5 |
| 3fe52747-375f-311b-9613-0f24bc042c61 | -4.6744 | -45.0409 | 2025-11-14 14:30:00 | GOES-19 | LAGO DO JUNCO | MARANHÃO | Brasil | 2105807 | 21 | 33 | nan | nan | nan | Cerrado | 89.0 |
| fe05be82-8771-37fd-ad7b-78ffc130e0b4 | -6.5609 | -47.1034 | 2025-11-14 14:30:00 | GOES-19 | SÃO JOÃO DO PARAÍSO | MARANHÃO | Brasil | 2111052 | 21 | 33 | nan | nan | nan | Cerrado | 71.9 |
| be2f93d1-4d19-35f7-a2bd-ddfc2cef61d5 | -12.4436 | -47.891 | 2025-11-14 14:30:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 58.0 |
| 9d80d34c-c7c3-3b3e-94e3-3da84b5d1941 | -10.117 | -40.8851 | 2025-11-14 14:30:00 | GOES-19 | CAMPO FORMOSO | BAHIA | Brasil | 2906006 | 29 | 33 | nan | nan | nan | Caatinga | 76.5 |
| 60ef707e-3e37-3eee-9a77-e40096cbb537 | -11.8486 | -49.2218 | 2025-11-14 14:30:00 | GOES-19 | CARIRI DO TOCANTINS | TOCANTINS | Brasil | 1703867 | 17 | 33 | nan | nan | nan | Cerrado | 86.6 |
| 303789bd-8aae-3a3b-a796-16820507c292 | -5.5447 | -43.678 | 2025-11-14 14:30:00 | GOES-19 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 91.5 |
| cec86738-25c3-3e41-bc6c-56c9ac256181 | -6.5609 | -47.1034 | 2025-11-14 14:40:00 | GOES-19 | SÃO JOÃO DO PARAÍSO | MARANHÃO | Brasil | 2111052 | 21 | 33 | nan | nan | nan | Cerrado | 85.3 |
| 451d708e-4703-3e07-8d30-c1fe738b3022 | -8.5609 | -46.0363 | 2025-11-14 14:40:00 | GOES-19 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 58.8 |
| b912385a-682b-337c-9bd2-e0c6f14b7ae7 | -7.4731 | -42.5471 | 2025-11-14 14:40:00 | GOES-19 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 83.6 |
| 2528cf7b-9064-3ca7-aa6f-ab894074ae39 | -7.3393 | -46.0176 | 2025-11-14 14:40:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 48.3 |
| 22730844-9a3a-34e4-ac7d-61b25d9b41f9 | -6.2765 | -41.7322 | 2025-11-14 14:40:00 | GOES-19 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 87.8 |
| c089366a-801e-3b15-b496-f204b9f2d2ac | -3.44 | -42.5437 | 2025-11-14 14:40:00 | GOES-19 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 109.7 |
| 6d9381de-9cba-34ec-be19-bb0d26ca3cbb | -11.8677 | -49.2195 | 2025-11-14 14:40:00 | GOES-19 | CARIRI DO TOCANTINS | TOCANTINS | Brasil | 1703867 | 17 | 33 | nan | nan | nan | Cerrado | 63.4 |
| 90573644-ea9d-3a9e-b732-f2755efe0a96 | -11.6118 | -45.0905 | 2025-11-14 14:40:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 103.6 |
| e1cb7caa-8644-3129-ae99-3375c77c3420 | -5.5447 | -43.678 | 2025-11-14 14:40:00 | GOES-19 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 75.3 |
| f57deb36-c4d6-34ef-ac4c-0cce38d92b64 | -4.6744 | -45.0409 | 2025-11-14 14:40:00 | GOES-19 | LAGO DO JUNCO | MARANHÃO | Brasil | 2105807 | 21 | 33 | nan | nan | nan | Cerrado | 77.2 |
| 47f59cb5-8cc6-3912-90d3-ef6c7feaa07f | -12.4436 | -47.891 | 2025-11-14 14:40:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 60.0 |
| 99e46a1d-0b53-39ef-9b06-3f76bada78da | -8.6623 | -45.4834 | 2025-11-14 14:40:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 80.6 |
| 21168c16-1267-38e7-bfc5-1807f534e070 | -10.0978 | -40.8879 | 2025-11-14 14:40:00 | GOES-19 | CAMPO FORMOSO | BAHIA | Brasil | 2906006 | 29 | 33 | nan | nan | nan | Caatinga | 75.9 |
| 107985c5-adc3-3b55-9eb5-5962429f74b2 | -4.5759 | -43.1617 | 2025-11-14 14:40:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 89.7 |
| 70f01ce4-4b28-3e10-b7db-4fb9a7395972 | -7.3581 | -46.0159 | 2025-11-14 14:40:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 39.4 |
| 1d510f00-b080-300a-9653-f2ca549eb4d0 | -14.2284 | -43.5496 | 2025-11-14 14:40:00 | GOES-19 | IUIU | BAHIA | Brasil | 2917334 | 29 | 33 | nan | nan | nan | Cerrado | 119.3 |


