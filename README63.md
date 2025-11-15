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

## Dados Diários - Página 63

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 9d3ea343-1611-3ef2-89a8-7c3f4be14858 | -6.0849 | -48.1859 | 2025-11-15 14:00:00 | GOES-19 | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Amazônia | 65.6 |
| b34e5adb-8862-32f8-b6e1-7a2e35e52f25 | -7.4517 | -42.7624 | 2025-11-15 14:00:00 | GOES-19 | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 199.7 |
| 211812dd-d03d-3403-968f-a9f32627b9e9 | -7.442 | -45.2184 | 2025-11-15 14:00:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 124.4 |
| c166b099-8bb9-31ee-81f9-5dc149387aca | -5.5127 | -40.9765 | 2025-11-15 14:00:00 | GOES-19 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 211.2 |
| c1745f1a-0aa9-3706-8328-7a0a9ad6d872 | -5.2701 | -47.6496 | 2025-11-15 14:00:00 | GOES-19 | IMPERATRIZ | MARANHÃO | Brasil | 2105302 | 21 | 33 | nan | nan | nan | Amazônia | 75.6 |
| b025b3fe-63db-3f74-aeeb-9f18b64312c8 | -8.6623 | -45.4834 | 2025-11-15 14:00:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 107.0 |
| 40e7f6a6-24c4-3067-895c-69a33f6a56c6 | -6.0496 | -45.8072 | 2025-11-15 14:10:00 | GOES-19 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 75.2 |
| 5de4801a-03b5-3b1e-a9e7-24b784f69aa4 | -3.4209 | -42.6153 | 2025-11-15 14:10:00 | GOES-19 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 124.6 |
| a006d3e1-38a8-32fa-867e-fbb3876b3774 | -5.4753 | -40.9553 | 2025-11-15 14:10:00 | GOES-19 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 190.8 |
| b21754f6-38cb-3c2a-becd-f9228cd69e2b | -3.59 | -42.4421 | 2025-11-15 14:10:00 | GOES-19 | JOCA MARQUES | PIAUÍ | Brasil | 2205458 | 22 | 33 | nan | nan | nan | Caatinga | 177.8 |
| 789b1f44-356d-310a-bef0-59e3cf391934 | -9.9377 | -44.9252 | 2025-11-15 14:10:00 | GOES-19 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 103.6 |
| 14caa3b3-f3d7-3835-a8d8-18bf66b8aeed | -3.971 | -44.2594 | 2025-11-15 14:10:00 | GOES-19 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 81.1 |
| 5170f4e5-487d-302b-b84e-df2a7bc462e3 | -9.1247 | -49.1511 | 2025-11-15 14:10:00 | GOES-19 | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | 138.4 |
| 817a21f2-d421-3d9b-97db-490cdce7b8f9 | -4.0067 | -47.6711 | 2025-11-15 14:10:00 | GOES-19 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 84.2 |
| 59a6e2d0-5099-3b8b-9384-335a067ff189 | -7.442 | -45.2184 | 2025-11-15 14:10:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 123.5 |
| eecfe36f-97ab-31a9-b540-6ff8da3f0067 | -9.7305 | -48.8966 | 2025-11-15 14:10:00 | GOES-19 | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 73.0 |
| 1bcb385a-9c82-300e-a4da-ba9f24e3f126 | -6.0309 | -45.8085 | 2025-11-15 14:10:00 | GOES-19 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 101.5 |
| e4f09c0d-4b70-34e6-8bec-deb3e0145a30 | -7.4417 | -45.2411 | 2025-11-15 14:10:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 63.6 |
| 231b2af2-3169-3880-8c3f-9dccb1f2ba42 | -8.5795 | -46.0568 | 2025-11-15 14:10:00 | GOES-19 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 131.9 |
| d01f55c6-261b-396e-a31f-caf6b4045aba | -5.4942 | -40.9537 | 2025-11-15 14:10:00 | GOES-19 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 132.5 |
| 834f76e3-b5a7-39b9-970d-177c24f766c6 | -3.2439 | -40.8074 | 2025-11-15 14:10:00 | GOES-19 | URUOCA | CEARÁ | Brasil | 2313906 | 23 | 33 | nan | nan | nan | Caatinga | 143.9 |
| 4f0d3b3c-b67d-30fa-8559-15a331c60350 | -6.411 | -41.4793 | 2025-11-15 14:10:00 | GOES-19 | LAGOA DO SÍTIO | PIAUÍ | Brasil | 2205599 | 22 | 33 | nan | nan | nan | Caatinga | 79.2 |
| 772509c9-8a87-3797-9278-15e27d3a5ccf | -7.3868 | -48.6545 | 2025-11-15 14:10:00 | GOES-19 | ARAGUAÍNA | TOCANTINS | Brasil | 1702109 | 17 | 33 | nan | nan | nan | Amazônia | 67.3 |
| cd13f0b7-adfd-3cd0-a50b-9e93e76a9504 | -10.3232 | -44.576 | 2025-11-15 14:10:00 | GOES-19 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 129.8 |
| 7af8503f-a91a-3a1f-b85e-4bd8392a240f | -3.4212 | -42.5682 | 2025-11-15 14:10:00 | GOES-19 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 82.8 |
| 56dc8b0d-acc3-352e-aea5-35598232dbd0 | -11.9171 | -46.2362 | 2025-11-15 14:10:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 138.0 |
| 2df929f0-d4e0-3209-b403-1d420220fb55 | -8.1778 | -45.0332 | 2025-11-15 14:10:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 224.2 |
| 268113ab-c4ac-3a2d-8090-5dc28cb3fe15 | -5.6433 | -41.0872 | 2025-11-15 14:10:00 | GOES-19 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 89.1 |
| 61a531bd-d138-3de5-b6c4-3007d0abed8f | -5.5125 | -41.0008 | 2025-11-15 14:10:00 | GOES-19 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 110.2 |
| 31004f48-5d7f-3969-b376-a2975a3eaf79 | -7.7681 | -37.4158 | 2025-11-15 14:10:00 | GOES-19 | INGAZEIRA | PERNAMBUCO | Brasil | 2607109 | 26 | 33 | nan | nan | nan | Caatinga | 244.5 |
| 3e39ec4c-68aa-3ddb-8fa0-c8288d5530bd | -6.1233 | -48.0532 | 2025-11-15 14:10:00 | GOES-19 | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 185.2 |
| a248cb29-4121-34fc-82cd-95072670ff12 | -4.6609 | -39.4419 | 2025-11-15 14:10:00 | GOES-19 | ITATIRA | CEARÁ | Brasil | 2306603 | 23 | 33 | nan | nan | nan | Caatinga | 104.7 |
| c06e2b90-38a1-31f2-931d-fea67e2e9723 | -6.1421 | -48.0302 | 2025-11-15 14:10:00 | GOES-19 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 212.1 |
| 3403ea26-a585-3933-9c6a-176047fccf6a | -8.1967 | -45.0312 | 2025-11-15 14:10:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 117.4 |
| b03416ca-66d9-3623-ac06-7a9e70aa9a34 | -9.8542 | -44.1729 | 2025-11-15 14:10:00 | GOES-19 | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 82.2 |
| c52edc71-5a96-38e2-9ff6-44de1e66152f | -11.9363 | -46.2335 | 2025-11-15 14:10:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 174.3 |
| 9e876800-b85b-3661-a05d-40de2fc8bb47 | -3.5667 | -43.2402 | 2025-11-15 14:10:00 | GOES-19 | MATA ROMA | MARANHÃO | Brasil | 2106409 | 21 | 33 | nan | nan | nan | Cerrado | 74.1 |
| 242b9fe6-7319-3e0f-af40-dcc36cbb8233 | -5.4751 | -40.9796 | 2025-11-15 14:10:00 | GOES-19 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 247.3 |
| dfbe0383-c229-301e-9416-98e0b8b7b908 | -8.6808 | -45.5041 | 2025-11-15 14:10:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 138.7 |
| b0f976a0-a52c-340f-aac7-1ccebf715156 | -7.094 | -42.7272 | 2025-11-15 14:10:00 | GOES-19 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 87.9 |
| e432878e-01e4-36c5-8b94-733568f92220 | -7.2567 | -40.1725 | 2025-11-15 14:10:00 | GOES-19 | ARARIPE | CEARÁ | Brasil | 2301307 | 23 | 33 | nan | nan | nan | Caatinga | 100.4 |
| ca7e0b40-a920-3813-823e-0e022cc6fe02 | -4.8125 | -41.6084 | 2025-11-15 14:10:00 | GOES-19 | JUAZEIRO DO PIAUÍ | PIAUÍ | Brasil | 2205516 | 22 | 33 | nan | nan | nan | Caatinga | 127.4 |
| ec2d781a-9d25-3986-b345-98ee7a9e228f | -8.662 | -45.5061 | 2025-11-15 14:10:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 126.9 |
| dc7026ee-98d2-32fd-bd82-b9a19bb61d8c | -5.5316 | -40.975 | 2025-11-15 14:10:00 | GOES-19 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 126.1 |
| fdae0dc0-791b-34ba-83fe-a5ed9e4a1385 | -11.9175 | -46.2135 | 2025-11-15 14:10:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 150.5 |
| 2ec7f541-5abb-3e36-bd7b-a7c134a57999 | -7.4517 | -42.7624 | 2025-11-15 14:10:00 | GOES-19 | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 167.3 |
| 2573dec2-8649-3f88-990d-49fd8b75066f | -3.2117 | -43.3494 | 2025-11-15 14:10:00 | GOES-19 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 76.5 |
| 4cc303e5-78b5-3a3d-92d8-4bab8de77b23 | -5.4939 | -40.9781 | 2025-11-15 14:10:00 | GOES-19 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 170.7 |
| a31ebb94-8c4c-34df-ad73-de75f63abdd9 | -3.6835 | -42.4374 | 2025-11-15 14:10:00 | GOES-19 | LUZILÂNDIA | PIAUÍ | Brasil | 2205805 | 22 | 33 | nan | nan | nan | Caatinga | 113.0 |
| fabbdd88-ed20-3c35-bb3c-b08be5c8a593 | -8.159 | -45.0351 | 2025-11-15 14:10:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 122.7 |
| 6683a01b-13f5-30ee-92a3-f696f010dbd5 | -8.7355 | -45.657 | 2025-11-15 14:10:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 90.3 |
| 14392ee8-be0f-3cde-a88e-8936b4ce1f1a | -8.5604 | -46.0813 | 2025-11-15 14:10:00 | GOES-19 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 192.8 |
| 5df57836-e4be-30a4-a181-307f2733402f | -8.5607 | -46.0588 | 2025-11-15 14:10:00 | GOES-19 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 211.0 |
| d1199593-5af0-3f07-94df-b1f40caf395e | -11.9175 | -46.2135 | 2025-11-15 14:20:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 127.9 |
| a1a097a7-ca62-3d3c-8218-c7814b954506 | -10.5652 | -44.9134 | 2025-11-15 14:20:00 | GOES-19 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 150.3 |
| 34a089b6-e859-31e3-bddf-6b7530763ce8 | -12.3917 | -47.5643 | 2025-11-15 14:20:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 204.5 |
| 37104911-8369-3af5-a525-72144de86aa4 | -8.662 | -45.5061 | 2025-11-15 14:20:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 283.7 |
| 75c7e5de-fb8d-3eab-8e65-39d7a376a22b | -3.6835 | -42.4374 | 2025-11-15 14:20:00 | GOES-19 | LUZILÂNDIA | PIAUÍ | Brasil | 2205805 | 22 | 33 | nan | nan | nan | Caatinga | 85.7 |
| e1c678f6-26af-38bc-ab89-3aee79d6a3de | -4.7342 | -47.1547 | 2025-11-15 14:20:00 | GOES-19 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 56.8 |
| 1ccb3c56-db48-31b4-a6a4-f89101caced9 | -11.9363 | -46.2335 | 2025-11-15 14:20:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 346.3 |
| 9f2fc2e2-a1a4-34ff-b32f-ced023d09843 | -6.0309 | -45.8085 | 2025-11-15 14:20:00 | GOES-19 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 67.9 |
| 8157a12a-2c5c-3ad7-81d7-4f77b1fffb71 | -12.4109 | -47.5616 | 2025-11-15 14:20:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 151.9 |
| da86a28d-c908-3472-a726-860fc59ae5fe | -10.3037 | -44.6017 | 2025-11-15 14:20:00 | GOES-19 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 146.2 |
| 9966778f-8749-3648-a3cc-ecbccc500628 | -6.1608 | -48.0289 | 2025-11-15 14:20:00 | GOES-19 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 59.0 |
| 52e004fa-9fa7-3467-83c6-dda5fa768994 | -7.4417 | -45.2411 | 2025-11-15 14:20:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 76.3 |
| c013f099-2cbd-3d2f-b4f3-629d3d075711 | -11.4977 | -48.5223 | 2025-11-15 14:20:00 | GOES-19 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 75.3 |
| d5fe3854-665f-3b35-84d9-f2f0d2f189b3 | -8.5795 | -46.0568 | 2025-11-15 14:20:00 | GOES-19 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 154.3 |
| d9b14265-c3ac-3605-a76f-f73d5e605d1e | -1.3008 | -49.0613 | 2025-11-15 14:20:00 | GOES-19 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 64.1 |
| e98bfd8f-2774-3353-b91b-5bc52b395b02 | -9.736 | -45.7487 | 2025-11-15 14:20:00 | GOES-19 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 135.7 |
| 5c22d01d-7c27-319f-8f4f-6cb6086c04fe | -11.7208 | -48.8669 | 2025-11-15 14:20:00 | GOES-19 | GURUPI | TOCANTINS | Brasil | 1709500 | 17 | 33 | nan | nan | nan | Cerrado | 183.8 |
| e3eb1f80-19b3-30a2-bb29-6862ff51a696 | -7.7681 | -37.4158 | 2025-11-15 14:20:00 | GOES-19 | INGAZEIRA | PERNAMBUCO | Brasil | 2607109 | 26 | 33 | nan | nan | nan | Caatinga | 141.9 |
| 0eb190f5-1d99-32a2-abc2-5b8f292fa940 | -8.6808 | -45.5041 | 2025-11-15 14:20:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 323.0 |
| aa4e7c8c-4805-3aa8-aeed-3011b68dd409 | -12.3914 | -47.5867 | 2025-11-15 14:20:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 180.5 |
| 59456425-66b7-357e-9171-d535ad4c3454 | -12.8534 | -46.4392 | 2025-11-15 14:20:00 | GOES-19 | COMBINADO | TOCANTINS | Brasil | 1705557 | 17 | 33 | nan | nan | nan | Cerrado | 111.5 |
| c3e6adc9-b7e6-3704-a1df-fb64111eeb5f | -9.1247 | -49.1511 | 2025-11-15 14:20:00 | GOES-19 | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | 91.8 |
| cd0941d3-9151-3440-bf15-ac9e63e8c35a | -8.6811 | -45.4814 | 2025-11-15 14:20:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 109.8 |
| 95d8f2d8-2ee4-3539-9533-74f093a3546f | -8.1778 | -45.0332 | 2025-11-15 14:20:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 203.5 |
| bccf31d2-6fe7-347b-be39-2741ce2bcd48 | -6.1421 | -48.0302 | 2025-11-15 14:20:00 | GOES-19 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 300.0 |
| 31b32048-0644-3a6e-8738-41383e773da7 | -7.3868 | -48.6545 | 2025-11-15 14:20:00 | GOES-19 | ARAGUAÍNA | TOCANTINS | Brasil | 1702109 | 17 | 33 | nan | nan | nan | Amazônia | 65.1 |
| 5b407d4a-ee4e-37ab-b8c5-bcc3d4e3962e | -3.971 | -44.2594 | 2025-11-15 14:20:00 | GOES-19 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 86.1 |
| f1509636-d6c7-3147-a9b8-80efac287581 | -10.5461 | -44.9159 | 2025-11-15 14:20:00 | GOES-19 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 150.3 |
| c17879fd-8fdf-38c0-8274-597d4ea36bc5 | -7.3504 | -43.3604 | 2025-11-15 14:20:00 | GOES-19 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 122.0 |
| acf50957-c8a4-385d-b057-014a6d1e808e | -6.1233 | -48.0532 | 2025-11-15 14:20:00 | GOES-19 | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 399.6 |
| 97e91440-fd60-31e4-9dd1-0705335458ed | -3.9983 | -42.8912 | 2025-11-15 14:20:00 | GOES-19 | BURITI | MARANHÃO | Brasil | 2102200 | 21 | 33 | nan | nan | nan | Caatinga | 73.9 |
| 01b4db6b-4ae2-3158-839b-dd7ffbaf83de | -6.411 | -41.4793 | 2025-11-15 14:20:00 | GOES-19 | LAGOA DO SÍTIO | PIAUÍ | Brasil | 2205599 | 22 | 33 | nan | nan | nan | Caatinga | 92.1 |
| d6a1c714-0e7a-3b62-83bb-e9d46af79dfe | -8.5607 | -46.0588 | 2025-11-15 14:20:00 | GOES-19 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 226.2 |
| b2a5b9ac-a24e-3342-a794-7711a73dff6e | -10.3232 | -44.576 | 2025-11-15 14:20:00 | GOES-19 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 290.9 |
| a287c8f3-4809-3312-bd86-0cd9201363cb | -11.7094 | -48.386 | 2025-11-15 14:20:00 | GOES-19 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 252.8 |
| 6cc7b197-0302-3824-ae41-afd28b4794aa | -8.159 | -45.0351 | 2025-11-15 14:20:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 112.6 |
| 5b67c81f-827a-3783-a7f4-fd2315c80c5d | -7.2567 | -40.1725 | 2025-11-15 14:20:00 | GOES-19 | ARARIPE | CEARÁ | Brasil | 2301307 | 23 | 33 | nan | nan | nan | Caatinga | 82.9 |
| f2268589-4f23-38fc-8bea-10c9cfc010b6 | -10.3228 | -44.5992 | 2025-11-15 14:20:00 | GOES-19 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 627.9 |
| b6a06b87-ae6b-3d85-bbbd-c50b9ff68076 | -7.4517 | -42.7624 | 2025-11-15 14:20:00 | GOES-19 | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 165.3 |
| 63469c88-a191-3467-b8f8-f77308a53b8c | -10.5457 | -44.939 | 2025-11-15 14:20:00 | GOES-19 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 145.1 |
| 968c3dfe-4950-3f66-ae50-e64e2e3d9bb7 | -8.1967 | -45.0312 | 2025-11-15 14:20:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 120.7 |
| cb2872a3-f760-3654-b225-4fa01161f6c4 | -5.2701 | -47.6496 | 2025-11-15 14:20:00 | GOES-19 | IMPERATRIZ | MARANHÃO | Brasil | 2105302 | 21 | 33 | nan | nan | nan | Amazônia | 105.8 |
| 75ed18a8-8689-33b5-94c8-c27ae308ef82 | -8.5604 | -46.0813 | 2025-11-15 14:20:00 | GOES-19 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 246.0 |
| 6248caaa-387c-3c2a-8881-4e72ff033dc9 | -12.4106 | -47.584 | 2025-11-15 14:20:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 118.6 |
| 823f7d08-720f-34ef-8e0f-55c49396a02c | -11.3265 | -48.5214 | 2025-11-15 14:20:00 | GOES-19 | BREJINHO DE NAZARÉ | TOCANTINS | Brasil | 1703701 | 17 | 33 | nan | nan | nan | Cerrado | 55.1 |
| 09b0fdd1-8168-334a-941d-5a0694eed0e1 | -6.0892 | -41.6527 | 2025-11-15 14:20:00 | GOES-19 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 99.8 |
| dbba398f-12ed-35c1-96ac-5cad93bb10bd | -12.6741 | -46.7831 | 2025-11-15 14:20:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 194.8 |


[Clique aqui para ver as próximas entradas](README64.md)
