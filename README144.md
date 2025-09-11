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

## Dados Diários - Página 144

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 48e5498a-4741-3f3d-ad18-c54552bad5c0 | -14.4461 | -53.2755 | 2025-09-11 13:50:00 | GOES-19 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 82.1 |
| 656c9c52-65ea-3344-b8b6-a9061ae395e8 | -14.5125 | -53.9367 | 2025-09-11 13:50:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 87.6 |
| 0748cc78-706c-322f-91be-063d81ca28aa | -11.7786 | -46.5047 | 2025-09-11 13:50:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 360.1 |
| 4e27d2a9-fa55-3a31-9c0f-5425b7707d37 | -8.1837 | -46.0965 | 2025-09-11 13:50:00 | GOES-19 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 74.0 |
| 4192c031-5b72-3d34-99ea-962ded518b99 | -9.0942 | -47.076 | 2025-09-11 13:50:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 98.3 |
| c18f96e5-7c7f-3084-9399-9347ea7dc2db | -7.8708 | -45.5181 | 2025-09-11 13:50:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 135.1 |
| 3f2bf38d-9015-3535-8428-dc406d17654c | -15.801 | -52.2472 | 2025-09-11 13:50:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 113.3 |
| 8c60dfad-a541-3538-a599-a58fbcc9f42c | -11.779 | -46.4821 | 2025-09-11 13:50:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 176.5 |
| f29a7a81-337c-391a-834e-5c8050a3ed8c | -9.1514 | -47.0257 | 2025-09-11 14:00:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 77.0 |
| b76d3a2b-7cb5-3094-a901-efcad9d71ff2 | -9.9398 | -46.064 | 2025-09-11 14:00:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 529.6 |
| e32371c5-e4cc-3d0d-87d8-ade7c566c493 | -10.6606 | -48.6218 | 2025-09-11 14:00:00 | GOES-19 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 93.3 |
| 455b6ccc-4cd6-3dae-a207-9b634b0ff5c3 | -9.0745 | -45.7109 | 2025-09-11 14:00:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 105.4 |
| fd1a0193-0514-32b7-b322-63bb04ee829c | -15.1759 | -52.4199 | 2025-09-11 14:00:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 131.5 |
| 29f6c2bf-8a9a-3ceb-9de5-f0fb3e844c9f | -6.5038 | -45.2539 | 2025-09-11 14:00:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 98.9 |
| 76cbf2c9-75da-3245-a859-22a0831f24d4 | -9.0358 | -45.783 | 2025-09-11 14:00:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 79.1 |
| c70545b5-7e5e-3bd9-bc76-95a9aff73cfe | -13.6009 | -47.656 | 2025-09-11 14:00:00 | GOES-19 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 68.7 |
| 6e5fb955-46c6-3fb6-a24f-3f7e26536eb1 | -15.1012 | -50.1687 | 2025-09-11 14:00:00 | GOES-19 | ARAGUAPAZ | GOIÁS | Brasil | 5202155 | 52 | 33 | nan | nan | nan | Cerrado | 109.1 |
| a07b3b84-859f-3f48-b603-79684953783a | -11.1685 | -45.3144 | 2025-09-11 14:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 162.2 |
| 6161c0f5-5f4d-3753-bc6e-818072dc5521 | -11.7399 | -46.5326 | 2025-09-11 14:00:00 | GOES-19 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 198.9 |
| 8ff4d165-3651-3037-a296-94aeeeff2189 | -7.8708 | -45.5181 | 2025-09-11 14:00:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 110.6 |
| 1509a019-ed1f-39b9-9a3a-0ced9cc278c0 | -7.4161 | -45.8536 | 2025-09-11 14:00:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 176.4 |
| 33df144b-f416-3533-ba2a-6cd332a52131 | -10.203 | -46.213 | 2025-09-11 14:00:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 85.7 |
| 989c1190-45b6-3ee2-a33a-cba1ec80e218 | -11.1689 | -45.2914 | 2025-09-11 14:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 100.0 |
| 6d5d3e60-05af-322d-9ec0-004194934fa6 | -6.2228 | -43.3226 | 2025-09-11 14:00:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 106.5 |
| 2c0d5160-7bf2-3c51-b263-293d4ddbb169 | -10.8789 | -45.5368 | 2025-09-11 14:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 98.7 |
| 4b9de32f-9ca5-36be-bdac-8acb38360c1d | -11.1 | -48.4172 | 2025-09-11 14:00:00 | GOES-19 | IPUEIRAS | TOCANTINS | Brasil | 1709807 | 17 | 33 | nan | nan | nan | Cerrado | 86.6 |
| 0b7b27a2-f8ff-36ee-afd9-a62bb0fbd255 | -15.801 | -52.2472 | 2025-09-11 14:00:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 103.1 |
| 29649282-4e5b-3a66-ab24-4ccf76339989 | -6.3735 | -45.1736 | 2025-09-11 14:00:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 59.4 |
| 2f8321d7-f994-3bb9-8041-4071a23ffd27 | -11.7211 | -46.5127 | 2025-09-11 14:00:00 | GOES-19 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 284.8 |
| 9a2e8f0d-c2a9-34d7-8f49-2afe9cc3ec64 | -6.3801 | -44.4893 | 2025-09-11 14:00:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 61.9 |
| 03c06e29-5f91-379f-84fa-e154b78e72f7 | -14.3074 | -54.7492 | 2025-09-11 14:00:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 152.6 |
| 5452272e-c7c7-3630-b389-561a17b29355 | -6.4848 | -45.2781 | 2025-09-11 14:00:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 117.8 |
| c5fa5dd6-d9e4-3572-9889-e23f4bb76c20 | -8.9365 | -46.1545 | 2025-09-11 14:00:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 76.7 |
| 12d96eb6-06af-3e71-99c2-67eb6a64f2b1 | -9.0976 | -49.8408 | 2025-09-11 14:00:00 | GOES-19 | CASEARA | TOCANTINS | Brasil | 1703909 | 17 | 33 | nan | nan | nan | Cerrado | 121.3 |
| 6f2db672-5b8e-3735-8ab4-85223fc91b8e | -13.2798 | -51.7312 | 2025-09-11 14:00:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 149.6 |
| 049341f4-b145-3b09-b321-24a5bc5e5603 | -15.5628 | -54.7453 | 2025-09-11 14:00:00 | GOES-19 | DOM AQUINO | MATO GROSSO | Brasil | 5103601 | 51 | 33 | nan | nan | nan | Cerrado | 75.4 |
| 93a98fad-27e4-3b38-b9d4-a914835367ec | -9.0262 | -49.5261 | 2025-09-11 14:00:00 | GOES-19 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 94.8 |
| 491301df-d455-3fb3-8f6e-d9fc081ebe81 | -10.6796 | -48.6196 | 2025-09-11 14:00:00 | GOES-19 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 214.0 |
| d0ab9730-8da4-3733-836a-0edbc8e2ef45 | -11.4836 | -43.6875 | 2025-09-11 14:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 110.0 |
| fa7aca7a-48c9-384d-bd82-6a115eefa1ae | -10.5671 | -47.2442 | 2025-09-11 14:00:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 145.9 |
| 6dd09a28-034c-329b-acdc-33123708172f | -6.6149 | -45.3807 | 2025-09-11 14:00:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 90.0 |
| 9ce4bd23-a53f-387f-bde1-61cc5d0e3a1a | -11.4845 | -43.6402 | 2025-09-11 14:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 150.7 |
| 2c0843dc-31b9-37f5-a04c-f13c37a8d36b | -9.7445 | -47.8468 | 2025-09-11 14:00:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 118.1 |
| a6c99859-ebfa-3ff9-bea9-fa546e619813 | -9.7634 | -47.8447 | 2025-09-11 14:00:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 124.7 |
| cf454f91-4a97-3c21-b320-4856f3151852 | -8.9752 | -46.0829 | 2025-09-11 14:00:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 161.6 |
| e645fb0e-76f9-3431-b850-5a25f9c22b69 | -5.9193 | -45.7492 | 2025-09-11 14:00:00 | GOES-19 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 58.1 |
| 0f360e2a-1bb2-3c91-b6d5-70d3acb7fbd5 | -6.4833 | -41.7613 | 2025-09-11 14:00:00 | GOES-19 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 92.4 |
| c081052c-eaac-3f52-a423-ea0eb9599c1e | -15.6929 | -47.0354 | 2025-09-11 14:00:00 | GOES-19 | CABECEIRAS | GOIÁS | Brasil | 5204003 | 52 | 33 | nan | nan | nan | Cerrado | 102.6 |
| 0d639b68-7e4a-327e-92e0-da712a7262d3 | -6.8374 | -45.6108 | 2025-09-11 14:00:00 | GOES-19 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 67.2 |
| d8e99cd2-6bb4-3ad7-8a8e-415a62548887 | -6.2226 | -43.3459 | 2025-09-11 14:00:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 112.7 |
| c2139478-cc2f-3801-b1e6-cfbd65beaf58 | -15.1021 | -50.1249 | 2025-09-11 14:00:00 | GOES-19 | ARAGUAPAZ | GOIÁS | Brasil | 5202155 | 52 | 33 | nan | nan | nan | Cerrado | 109.2 |
| 7b052a58-eed7-3799-b7a6-2cfcd276b3c3 | -15.1557 | -52.4652 | 2025-09-11 14:00:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 70.0 |
| 1f6c3631-234a-34d8-87ba-0c62467b4ed5 | -8.1837 | -46.0965 | 2025-09-11 14:00:00 | GOES-19 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 72.3 |
| 01aa9a97-5e30-33b5-8645-1218821bcc55 | -11.2834 | -46.4365 | 2025-09-11 14:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 78.7 |
| 32df80ed-f458-3c74-acd1-b8fa7abf9487 | -6.8525 | -47.8707 | 2025-09-11 14:00:00 | GOES-19 | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | 69.7 |
| fe5791c6-8009-38ec-b2bb-971f96a9a302 | -8.1101 | -49.2634 | 2025-09-11 14:00:00 | GOES-19 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 90.3 |
| 47c209c5-3740-3aa7-aad6-124c5c0b7ff6 | -15.1374 | -52.4039 | 2025-09-11 14:00:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 94.9 |
| 7f63afa4-74a2-3e65-aa90-794dd652e6fb | -15.1016 | -50.1468 | 2025-09-11 14:00:00 | GOES-19 | ARAGUAPAZ | GOIÁS | Brasil | 5202155 | 52 | 33 | nan | nan | nan | Cerrado | 204.2 |
| e901d478-71f3-3649-b501-4ed86c319e0d | -10.7557 | -46.0987 | 2025-09-11 14:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 603.8 |
| 0bc3d6ba-c8f9-39ec-9d6f-ecca4f8acda8 | -13.2599 | -51.7761 | 2025-09-11 14:00:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 112.6 |
| f8051113-8f64-33e4-aef4-46d97c55f86a | -9.9004 | -51.8811 | 2025-09-11 14:00:00 | GOES-19 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 64.6 |
| 7d1e8ffa-584a-357a-9a63-31d137ce0b32 | -10.6793 | -48.6415 | 2025-09-11 14:00:00 | GOES-19 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 223.4 |
| c83cccc7-2733-35bd-945a-b4814038ba2a | -10.8594 | -45.5622 | 2025-09-11 14:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 175.2 |
| 136514b1-1e10-360c-8d8c-3e4837e475c6 | -11.484 | -43.6639 | 2025-09-11 14:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 113.8 |
| 187e046a-7d42-3fcf-82db-6a4f80bc13da | -12.9292 | -54.7538 | 2025-09-11 14:00:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 96.2 |
| ee3d361b-329e-340a-b3b6-1996aa282d7e | -6.5962 | -45.3822 | 2025-09-11 14:00:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 76.4 |
| 1d9bcd4a-43f3-3886-a5c8-2b1b1a877525 | -4.553 | -43.7439 | 2025-09-11 14:00:00 | GOES-19 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 77.7 |
| b2304cf7-e02f-3fa0-8fd3-fda3d728fa6a | -10.7362 | -46.1238 | 2025-09-11 14:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 132.7 |
| 30757b0c-5b62-3ea7-92d3-cda5f51d0c80 | -7.4159 | -45.8761 | 2025-09-11 14:00:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 158.2 |
| e11bfa04-bfcc-3215-9a73-54618356e0a3 | -6.485 | -45.2554 | 2025-09-11 14:00:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 89.3 |
| 230c309c-b44f-39e6-b534-1b13d0d41353 | -8.8758 | -49.5399 | 2025-09-11 14:00:00 | GOES-19 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 120.1 |
| 7abe6f02-9de9-35c6-b12a-c74f1db07b79 | -6.3158 | -43.4081 | 2025-09-11 14:00:00 | GOES-19 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 89.4 |
| 95b63a4a-551d-322a-9fba-9ae7da26d74b | -9.0979 | -49.8194 | 2025-09-11 14:00:00 | GOES-19 | CASEARA | TOCANTINS | Brasil | 1703909 | 17 | 33 | nan | nan | nan | Cerrado | 99.3 |
| 3dc30fb4-849e-37bf-a1ba-bc5679040357 | -14.3071 | -54.7699 | 2025-09-11 14:00:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 122.4 |
| 1e4e1fa8-a1ee-397e-8bba-af1120579f95 | -11.4849 | -43.6166 | 2025-09-11 14:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 96.4 |
| d5fd2ce3-bd64-3b5b-a089-017d8e1afc26 | -6.4836 | -41.7373 | 2025-09-11 14:00:00 | GOES-19 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 112.3 |
| 568d2a6b-0b6a-3e45-a53b-d8922f02eb1c | -6.3226 | -53.4553 | 2025-09-11 14:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 83.0 |
| e36e3d3f-0517-3d80-a9ba-2c6cadbf2410 | -15.1211 | -50.1438 | 2025-09-11 14:00:00 | GOES-19 | ARAGUAPAZ | GOIÁS | Brasil | 5202155 | 52 | 33 | nan | nan | nan | Cerrado | 93.3 |
| 05810491-2ce7-3058-bf50-8d777e6aff0f | -15.6536 | -47.0425 | 2025-09-11 14:00:00 | GOES-19 | CABECEIRAS | GOIÁS | Brasil | 5204003 | 52 | 33 | nan | nan | nan | Cerrado | 94.5 |
| 296deb7e-ea1a-386b-89cb-b1ac6c5c84b9 | -16.6335 | -49.7683 | 2025-09-11 14:00:00 | GOES-19 | NAZÁRIO | GOIÁS | Brasil | 5214408 | 52 | 33 | nan | nan | nan | Cerrado | 88.0 |
| e1afa43f-2acc-3814-af25-08b0a224a88d | -6.4364 | -44.4847 | 2025-09-11 14:00:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 88.7 |
| 9a914ae4-32b2-3252-9ca4-8629ccd1f00c | -11.0959 | -51.3443 | 2025-09-11 14:00:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 213.4 |
| ea496b60-9e5a-3757-8d2b-54f697e97e12 | -11.779 | -46.4821 | 2025-09-11 14:00:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 194.3 |
| 9a307974-365c-3a1c-b8ea-438e85705f65 | -15.1367 | -52.4466 | 2025-09-11 14:00:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 116.7 |
| 99cfecbb-7bbc-3186-bc2a-d6cfeec81a57 | -15.8014 | -52.2258 | 2025-09-11 14:00:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 84.7 |
| 1b3cc014-a877-3e14-b510-f9d3eeb5894e | -10.859 | -45.5851 | 2025-09-11 14:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 142.0 |
| 5271ab2c-20c9-32b9-99da-6e8da49023f2 | -14.6652 | -44.0617 | 2025-09-11 14:00:00 | GOES-19 | MANGA | MINAS GERAIS | Brasil | 3139300 | 31 | 33 | nan | nan | nan | Caatinga | 108.1 |
| eea57cbc-6841-3791-a54c-7eac1e93d467 | -15.1371 | -52.4252 | 2025-09-11 14:00:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 139.9 |
| 473b4218-b31c-3a5c-889e-b193f6e823f4 | -10.7366 | -46.1011 | 2025-09-11 14:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 242.1 |
| 9b097439-27aa-3612-9670-ef7db6d8758f | -6.684 | -44.1189 | 2025-09-11 14:00:00 | GOES-19 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 79.8 |
| 59ace573-1484-3c7d-a067-3dc9a95adc0f | -15.1215 | -50.1219 | 2025-09-11 14:00:00 | GOES-19 | ARAGUAPAZ | GOIÁS | Brasil | 5202155 | 52 | 33 | nan | nan | nan | Cerrado | 77.5 |
| 7c356deb-cf61-3f1a-b051-a67a92ff9a3a | -9.4801 | -46.4545 | 2025-09-11 14:00:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 106.4 |
| 011a24e4-c771-34e3-af47-018fda32c4d6 | -11.7112 | -48.2757 | 2025-09-11 14:00:00 | GOES-19 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 240.4 |
| 0c3bcd8c-9cdb-30f4-9838-2992c1e07cfd | -15.6732 | -47.0389 | 2025-09-11 14:00:00 | GOES-19 | CABECEIRAS | GOIÁS | Brasil | 5204003 | 52 | 33 | nan | nan | nan | Cerrado | 234.7 |
| 6dc31efc-6d76-3b34-9baa-6d3e500f9fc3 | -8.1103 | -49.2419 | 2025-09-11 14:00:00 | GOES-19 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 102.8 |
| dc31c280-7a6d-385f-ac55-a149f56ab8a1 | -11.7115 | -48.2536 | 2025-09-11 14:00:00 | GOES-19 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 211.2 |
| f411bf84-f5b4-38b3-ac4d-ee255c00ebb6 | -14.6658 | -44.0379 | 2025-09-11 14:00:00 | GOES-19 | MANGA | MINAS GERAIS | Brasil | 3139300 | 31 | 33 | nan | nan | nan | Caatinga | 149.1 |
| 7d348525-fc09-3aff-899e-dd60798f362a | -15.1561 | -52.4439 | 2025-09-11 14:00:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 95.3 |
| 504071de-94fc-3a1d-8aed-4d4e9e2e4217 | -19.9994 | -47.6271 | 2025-09-11 14:00:00 | GOES-19 | CONQUISTA | MINAS GERAIS | Brasil | 3118205 | 31 | 33 | nan | nan | nan | Cerrado | 148.4 |
| c06104c3-cc94-3aed-82ac-b78fd1e76643 | -15.8006 | -52.2687 | 2025-09-11 14:00:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 218.4 |


[Clique aqui para ver as próximas entradas](README145.md)
