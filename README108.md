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

## Dados Diários - Página 108

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| b1e9b718-de26-3a06-9ff9-c7305b765308 | -5.90476 | -57.73357 | 2025-09-03 06:52:00 | AQUA_M-M | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 145.8 |
| 5346d546-40c2-3a33-b365-d1cb29f49aa4 | -12.63805 | -56.99472 | 2025-09-03 06:54:00 | AQUA_M-M | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 17.8 |
| 34264c33-dfba-3522-a3c6-769458e5df25 | -14.32805 | -60.33253 | 2025-09-03 06:54:00 | AQUA_M-M | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 11.8 |
| 6a293610-1fd9-3eca-981d-266c7183ef22 | -12.93764 | -56.95835 | 2025-09-03 06:54:00 | AQUA_M-M | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 30.1 |
| b5cd9504-9050-3598-bd18-832dcc5ad9c5 | -12.90864 | -56.93203 | 2025-09-03 06:54:00 | AQUA_M-M | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 12.8 |
| 218553e3-b0cc-3b69-a91b-266483407580 | -14.33318 | -60.33973 | 2025-09-03 06:54:00 | AQUA_M-M | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 14.6 |
| ecc20eec-9b5c-34f2-bbb1-ea77bb029a80 | -12.94171 | -56.95355 | 2025-09-03 06:54:00 | AQUA_M-M | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 39.6 |
| 7f4a2671-03f2-3d17-b9f2-93f7c01d47a3 | -12.93953 | -56.97006 | 2025-09-03 06:54:00 | AQUA_M-M | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 14.8 |
| 9f6f1df5-57e0-3d10-a80d-77fede163512 | -12.92349 | -57.00141 | 2025-09-03 06:54:00 | AQUA_M-M | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 14.3 |
| b8321d9f-67cf-3a49-b7c5-6a3da6a8e921 | -14.32648 | -60.34352 | 2025-09-03 06:54:00 | AQUA_M-M | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 8.6 |
| b086306a-38ab-35b3-93c8-29f0cd78f048 | -7.7039 | -48.7371 | 2025-09-03 07:00:00 | GOES-19 | BANDEIRANTES DO TOCANTINS | TOCANTINS | Brasil | 1703057 | 17 | 33 | nan | nan | nan | Amazônia | 119.5 |
| 7c0dbc7f-0381-3ff8-8680-61742e763fc0 | -7.7226 | -48.7355 | 2025-09-03 07:00:00 | GOES-19 | BANDEIRANTES DO TOCANTINS | TOCANTINS | Brasil | 1703057 | 17 | 33 | nan | nan | nan | Amazônia | 72.5 |
| 936eb52f-a561-3f54-8884-5d64099b6422 | -7.6849 | -48.7602 | 2025-09-03 07:00:00 | GOES-19 | ARAPOEMA | TOCANTINS | Brasil | 1702307 | 17 | 33 | nan | nan | nan | Amazônia | 69.7 |
| 6c0f368c-6145-32d9-a992-18df281318a1 | -7.6851 | -48.7386 | 2025-09-03 07:00:00 | GOES-19 | BANDEIRANTES DO TOCANTINS | TOCANTINS | Brasil | 1703057 | 17 | 33 | nan | nan | nan | Amazônia | 69.6 |
| 3ed65b9e-d0d1-34fa-85fc-d0323fe977a9 | -7.7036 | -48.7587 | 2025-09-03 07:00:00 | GOES-19 | ARAPOEMA | TOCANTINS | Brasil | 1702307 | 17 | 33 | nan | nan | nan | Amazônia | 89.2 |
| 8fff3c92-785b-3720-923c-aaf338709002 | -7.7226 | -48.7355 | 2025-09-03 07:10:00 | GOES-19 | BANDEIRANTES DO TOCANTINS | TOCANTINS | Brasil | 1703057 | 17 | 33 | nan | nan | nan | Amazônia | 62.6 |
| f31b4644-50d5-37c9-a860-cce9811fefb0 | -7.5291 | -61.3444 | 2025-09-03 07:10:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 50.4 |
| 0b35e117-bccb-3e9e-98ad-dddbde8051ab | -7.6849 | -48.7602 | 2025-09-03 07:10:00 | GOES-19 | ARAPOEMA | TOCANTINS | Brasil | 1702307 | 17 | 33 | nan | nan | nan | Amazônia | 71.8 |
| 6a05da9a-bb3f-3a2f-9ef9-e6e58c8f48ba | -7.7036 | -48.7587 | 2025-09-03 07:10:00 | GOES-19 | ARAPOEMA | TOCANTINS | Brasil | 1702307 | 17 | 33 | nan | nan | nan | Amazônia | 95.2 |
| e9d230f6-b923-39ef-9406-459e6cff0365 | -7.6851 | -48.7386 | 2025-09-03 07:10:00 | GOES-19 | BANDEIRANTES DO TOCANTINS | TOCANTINS | Brasil | 1703057 | 17 | 33 | nan | nan | nan | Amazônia | 68.7 |
| 3c0b1845-bf42-36b9-b78c-31d99a1e17ef | -7.5476 | -61.3437 | 2025-09-03 07:10:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 57.5 |
| 9726192a-401d-324f-b4c6-1aff86eab9e4 | -7.7039 | -48.7371 | 2025-09-03 07:10:00 | GOES-19 | BANDEIRANTES DO TOCANTINS | TOCANTINS | Brasil | 1703057 | 17 | 33 | nan | nan | nan | Amazônia | 134.6 |
| ea81e70c-e7fe-3fa8-8aa0-e2bfba3bc15a | -7.5477 | -61.3247 | 2025-09-03 07:10:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 46.4 |
| 1fbc72d3-a958-36a0-b2d6-39fd2836b4a7 | -7.5477 | -61.3247 | 2025-09-03 07:20:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 49.3 |
| 7b3ae0fd-ad69-3642-8a7e-d64f1c4e8172 | -7.5476 | -61.3437 | 2025-09-03 07:20:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 52.2 |
| aad584a6-5f45-34b5-955b-54f281533100 | -11.5774 | -52.157 | 2025-09-03 07:20:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 142.7 |
| 124dbb1f-5bf7-3122-acc4-abfc076d773d | -11.5966 | -52.134 | 2025-09-03 07:20:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 838.9 |
| 2457462f-64a9-3010-9ee5-65a46a673e1b | -7.7226 | -48.7355 | 2025-09-03 07:20:00 | GOES-19 | BANDEIRANTES DO TOCANTINS | TOCANTINS | Brasil | 1703057 | 17 | 33 | nan | nan | nan | Amazônia | 68.6 |
| 35fe9444-831a-3942-89fa-c40d80888203 | -7.7036 | -48.7587 | 2025-09-03 07:20:00 | GOES-19 | ARAPOEMA | TOCANTINS | Brasil | 1702307 | 17 | 33 | nan | nan | nan | Amazônia | 82.8 |
| b4677960-de5f-32c8-a27a-00aeeade1b1d | -7.6851 | -48.7386 | 2025-09-03 07:20:00 | GOES-19 | BANDEIRANTES DO TOCANTINS | TOCANTINS | Brasil | 1703057 | 17 | 33 | nan | nan | nan | Amazônia | 68.7 |
| c821dede-be58-3407-8ff5-888cf2b5ec6a | -11.5969 | -52.113 | 2025-09-03 07:20:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 313.2 |
| a483950a-66e1-3ec9-a5d9-181c2d305bca | -11.5779 | -52.115 | 2025-09-03 07:20:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 212.7 |
| a597478b-e82c-3738-bef4-932c68d616cb | -11.5776 | -52.136 | 2025-09-03 07:20:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 505.0 |
| 1762265d-8708-3279-b35c-842f90bf8bbd | -11.5963 | -52.155 | 2025-09-03 07:20:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 234.1 |
| d54b7835-bbee-3979-bc2f-16a49bfa23a7 | -7.6849 | -48.7602 | 2025-09-03 07:20:00 | GOES-19 | ARAPOEMA | TOCANTINS | Brasil | 1702307 | 17 | 33 | nan | nan | nan | Amazônia | 65.4 |
| 159d50a6-8096-353e-a098-fd5d87d53a15 | -7.5291 | -61.3444 | 2025-09-03 07:20:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 43.4 |
| d51d4b75-cbe8-336a-8bc3-7e88ac7e9f6a | -7.7039 | -48.7371 | 2025-09-03 07:20:00 | GOES-19 | BANDEIRANTES DO TOCANTINS | TOCANTINS | Brasil | 1703057 | 17 | 33 | nan | nan | nan | Amazônia | 121.3 |
| 3d6d70e3-d83e-3cd7-a640-a9eb6b6b26ee | -7.8975 | -46.4594 | 2025-09-03 07:20:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 79.6 |
| 9771b92b-6c12-32e4-9b99-ba5657a30a0d | -7.6849 | -48.7602 | 2025-09-03 07:30:00 | GOES-19 | ARAPOEMA | TOCANTINS | Brasil | 1702307 | 17 | 33 | nan | nan | nan | Amazônia | 70.7 |
| 5a2b957b-1a27-3017-b7a8-63eb4a199db8 | -8.0608 | -45.3636 | 2025-09-03 07:30:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 62.4 |
| 369c923f-d465-38f9-85cb-6f0c8c508af3 | -7.7226 | -48.7355 | 2025-09-03 07:30:00 | GOES-19 | BANDEIRANTES DO TOCANTINS | TOCANTINS | Brasil | 1703057 | 17 | 33 | nan | nan | nan | Amazônia | 80.2 |
| b86b305f-7cfd-3844-8d73-92fa15f75adc | -7.5476 | -61.3437 | 2025-09-03 07:30:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 66.1 |
| be8f992e-6d1a-3f25-a967-0f3714e8e2cf | -7.5477 | -61.3247 | 2025-09-03 07:30:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 56.3 |
| fdd164b1-c602-3cd4-932e-8d3464731cd3 | -7.7039 | -48.7371 | 2025-09-03 07:30:00 | GOES-19 | BANDEIRANTES DO TOCANTINS | TOCANTINS | Brasil | 1703057 | 17 | 33 | nan | nan | nan | Amazônia | 106.9 |
| bbd4ad1b-0c27-3fce-9da9-8b5f8e04bce3 | -7.7036 | -48.7587 | 2025-09-03 07:30:00 | GOES-19 | ARAPOEMA | TOCANTINS | Brasil | 1702307 | 17 | 33 | nan | nan | nan | Amazônia | 74.6 |
| 547e50c5-4853-30dc-8ca2-57270094c821 | -7.6851 | -48.7386 | 2025-09-03 07:30:00 | GOES-19 | BANDEIRANTES DO TOCANTINS | TOCANTINS | Brasil | 1703057 | 17 | 33 | nan | nan | nan | Amazônia | 82.8 |
| 4d57c36d-12f4-3c0d-aa6e-206787fc4c9e | -7.8975 | -46.4594 | 2025-09-03 07:40:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 68.7 |
| bbbfe908-2f8b-3996-b75f-f19a7e257268 | -7.8977 | -46.4371 | 2025-09-03 07:40:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 64.4 |
| 2d2bcf7f-355d-3c63-be37-0542ef53449f | -15.1576 | -52.3586 | 2025-09-03 07:40:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 58.4 |
| 490ebc2a-6d2a-3786-81aa-ab01769618ef | -7.7036 | -48.7587 | 2025-09-03 07:40:00 | GOES-19 | ARAPOEMA | TOCANTINS | Brasil | 1702307 | 17 | 33 | nan | nan | nan | Amazônia | 66.9 |
| d69904df-5c21-36e2-9105-b44e47ad449d | -7.7226 | -48.7355 | 2025-09-03 07:40:00 | GOES-19 | BANDEIRANTES DO TOCANTINS | TOCANTINS | Brasil | 1703057 | 17 | 33 | nan | nan | nan | Amazônia | 77.9 |
| 42c13152-d878-3c3a-8d74-f9ff7958a4b8 | -7.5477 | -61.3247 | 2025-09-03 07:40:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 55.1 |
| 80f2156d-bca1-31a7-ad03-40a03f87efc9 | -7.6851 | -48.7386 | 2025-09-03 07:40:00 | GOES-19 | BANDEIRANTES DO TOCANTINS | TOCANTINS | Brasil | 1703057 | 17 | 33 | nan | nan | nan | Amazônia | 77.5 |
| 25ea011e-b01f-35b8-9a8b-23b84c83d143 | -7.7039 | -48.7371 | 2025-09-03 07:40:00 | GOES-19 | BANDEIRANTES DO TOCANTINS | TOCANTINS | Brasil | 1703057 | 17 | 33 | nan | nan | nan | Amazônia | 107.1 |
| 50b205c4-a687-31d9-b42b-0bcaa0c582b3 | -7.5476 | -61.3437 | 2025-09-03 07:40:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 62.0 |
| c46361e3-b97d-3139-ae32-76abba14b910 | -7.5477 | -61.3247 | 2025-09-03 07:50:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 54.8 |
| c7bc8825-a7de-3c38-a766-6b5ef32dd73e | -7.7039 | -48.7371 | 2025-09-03 07:50:00 | GOES-19 | BANDEIRANTES DO TOCANTINS | TOCANTINS | Brasil | 1703057 | 17 | 33 | nan | nan | nan | Amazônia | 113.8 |
| 2d25c065-f68c-3c3d-8530-099ed36e5650 | -7.5476 | -61.3437 | 2025-09-03 07:50:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 62.1 |
| a81907be-d792-3282-9e1c-57f761bbe689 | -7.7226 | -48.7355 | 2025-09-03 07:50:00 | GOES-19 | BANDEIRANTES DO TOCANTINS | TOCANTINS | Brasil | 1703057 | 17 | 33 | nan | nan | nan | Amazônia | 100.9 |
| b400bf5f-276a-31d6-ba3e-373e7d320a92 | -7.6851 | -48.7386 | 2025-09-03 07:50:00 | GOES-19 | BANDEIRANTES DO TOCANTINS | TOCANTINS | Brasil | 1703057 | 17 | 33 | nan | nan | nan | Amazônia | 81.5 |
| 0341dd16-008c-3add-a5ac-43b92ae73dc9 | -7.6849 | -48.7602 | 2025-09-03 07:50:00 | GOES-19 | ARAPOEMA | TOCANTINS | Brasil | 1702307 | 17 | 33 | nan | nan | nan | Amazônia | 76.7 |
| f25b8e5b-7804-3193-9e33-87cd9d6a45da | -17.4431 | -47.2044 | 2025-09-03 07:50:00 | GOES-19 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 46.2 |
| fb73a4a6-f2fb-3f3d-a3f0-8d4f970edec3 | -7.7036 | -48.7587 | 2025-09-03 07:50:00 | GOES-19 | ARAPOEMA | TOCANTINS | Brasil | 1702307 | 17 | 33 | nan | nan | nan | Amazônia | 99.6 |
| 9973176a-55e8-33d9-b30c-44989a92f968 | -7.5476 | -61.3437 | 2025-09-03 08:00:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 60.2 |
| b76197fe-2fdc-3b28-bdb7-d572c305b82a | -7.7226 | -48.7355 | 2025-09-03 08:00:00 | GOES-19 | BANDEIRANTES DO TOCANTINS | TOCANTINS | Brasil | 1703057 | 17 | 33 | nan | nan | nan | Amazônia | 110.6 |
| a8708a4e-22e4-3939-a03c-2f29ee985c94 | -6.8367 | -45.6784 | 2025-09-03 08:00:00 | GOES-19 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 63.4 |
| caa3f0f2-bff0-35cb-b767-f95e09c6edcd | -7.7039 | -48.7371 | 2025-09-03 08:00:00 | GOES-19 | BANDEIRANTES DO TOCANTINS | TOCANTINS | Brasil | 1703057 | 17 | 33 | nan | nan | nan | Amazônia | 107.2 |
| d1ac6295-91d0-3239-b3c8-bda6f0eeb4fc | -7.6851 | -48.7386 | 2025-09-03 08:00:00 | GOES-19 | BANDEIRANTES DO TOCANTINS | TOCANTINS | Brasil | 1703057 | 17 | 33 | nan | nan | nan | Amazônia | 62.8 |
| 5c08c2cb-fa32-39dc-99cd-1530565bf721 | -7.8975 | -46.4594 | 2025-09-03 08:00:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 62.5 |
| 0a44ad10-1798-380a-b00a-52b0ef12e272 | -7.7036 | -48.7587 | 2025-09-03 08:00:00 | GOES-19 | ARAPOEMA | TOCANTINS | Brasil | 1702307 | 17 | 33 | nan | nan | nan | Amazônia | 78.9 |
| 1aa0598e-ccf6-36fe-85f2-b911b0c093c6 | -7.7226 | -48.7355 | 2025-09-03 08:10:00 | GOES-19 | BANDEIRANTES DO TOCANTINS | TOCANTINS | Brasil | 1703057 | 17 | 33 | nan | nan | nan | Amazônia | 134.9 |
| f3cd53b0-7a51-37aa-b0e8-177f56154115 | -7.6851 | -48.7386 | 2025-09-03 08:10:00 | GOES-19 | BANDEIRANTES DO TOCANTINS | TOCANTINS | Brasil | 1703057 | 17 | 33 | nan | nan | nan | Amazônia | 61.0 |
| e043792a-e05c-30dd-92bb-f72a77c4e99a | -7.7039 | -48.7371 | 2025-09-03 08:10:00 | GOES-19 | BANDEIRANTES DO TOCANTINS | TOCANTINS | Brasil | 1703057 | 17 | 33 | nan | nan | nan | Amazônia | 83.7 |
| 0d19a498-cd94-3a23-8ec9-d9ff8edb8a64 | -7.7036 | -48.7587 | 2025-09-03 08:10:00 | GOES-19 | ARAPOEMA | TOCANTINS | Brasil | 1702307 | 17 | 33 | nan | nan | nan | Amazônia | 68.2 |
| 0973d70e-bb33-3b39-971c-8b039535deea | -7.6849 | -48.7602 | 2025-09-03 08:10:00 | GOES-19 | ARAPOEMA | TOCANTINS | Brasil | 1702307 | 17 | 33 | nan | nan | nan | Amazônia | 56.1 |
| ee0ef44c-82d2-3379-a4d4-056a83ccb54d | -7.7224 | -48.7572 | 2025-09-03 08:10:00 | GOES-19 | BANDEIRANTES DO TOCANTINS | TOCANTINS | Brasil | 1703057 | 17 | 33 | nan | nan | nan | Amazônia | 85.1 |
| f2b6aef9-0dee-3c2a-9915-079cd00ecb89 | -7.5476 | -61.3437 | 2025-09-03 08:10:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 59.6 |
| 486a8018-6e92-3e62-97f1-fccf3599772c | -10.0932 | -54.7667 | 2025-09-03 08:20:00 | GOES-19 | MATUPÁ | MATO GROSSO | Brasil | 5105606 | 51 | 33 | nan | nan | nan | Amazônia | 35.5 |
| 38f54c25-0e17-34ea-aa97-9c489dd97ae6 | -7.6851 | -48.7386 | 2025-09-03 08:20:00 | GOES-19 | BANDEIRANTES DO TOCANTINS | TOCANTINS | Brasil | 1703057 | 17 | 33 | nan | nan | nan | Amazônia | 63.4 |
| 1b7f9e27-07b5-3351-aeab-4e47d04f080d | -11.5779 | -52.115 | 2025-09-03 08:20:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 325.4 |
| ca6dff32-6e9d-3b95-b975-877aabea2eda | -11.5776 | -52.136 | 2025-09-03 08:20:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 778.3 |
| ce44be0e-9c2a-3f1f-8d5a-646118c41356 | -7.7039 | -48.7371 | 2025-09-03 08:20:00 | GOES-19 | BANDEIRANTES DO TOCANTINS | TOCANTINS | Brasil | 1703057 | 17 | 33 | nan | nan | nan | Amazônia | 93.9 |
| 482f785c-753f-3281-9f3f-42ee0e6bbaf9 | -7.7224 | -48.7572 | 2025-09-03 08:20:00 | GOES-19 | BANDEIRANTES DO TOCANTINS | TOCANTINS | Brasil | 1703057 | 17 | 33 | nan | nan | nan | Amazônia | 148.4 |
| a9d8aede-a15d-389a-8fc4-968a80afd9cf | -7.7036 | -48.7587 | 2025-09-03 08:20:00 | GOES-19 | ARAPOEMA | TOCANTINS | Brasil | 1702307 | 17 | 33 | nan | nan | nan | Amazônia | 80.7 |
| 24ce7826-0d3f-366f-a189-9e4771a4ea59 | -11.5774 | -52.157 | 2025-09-03 08:20:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 221.9 |
| 7e637281-6618-3c6b-afc0-d38dede251ec | -11.5963 | -52.155 | 2025-09-03 08:20:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 126.8 |
| 02499e33-e3b5-367f-9941-a2274f6dc947 | -7.7226 | -48.7355 | 2025-09-03 08:20:00 | GOES-19 | BANDEIRANTES DO TOCANTINS | TOCANTINS | Brasil | 1703057 | 17 | 33 | nan | nan | nan | Amazônia | 197.7 |
| 4a6290b6-79df-3572-93a3-8595dd6c1e6a | -11.5966 | -52.134 | 2025-09-03 08:20:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 384.4 |
| dc24cf65-56b9-3704-90d2-d4ce7ad20d4c | -11.5969 | -52.113 | 2025-09-03 08:20:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 203.6 |
| b1474412-5235-3cad-8e6a-f6c767bf5f78 | -11.5779 | -52.115 | 2025-09-03 08:30:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 222.2 |
| a0648dfe-266b-307d-8e18-ff4690db7396 | -7.7224 | -48.7572 | 2025-09-03 08:30:00 | GOES-19 | BANDEIRANTES DO TOCANTINS | TOCANTINS | Brasil | 1703057 | 17 | 33 | nan | nan | nan | Amazônia | 140.7 |
| d62bd224-5090-3b74-8755-3f78426a43db | -11.5776 | -52.136 | 2025-09-03 08:30:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 552.9 |
| 6f5cd502-9155-373a-8db9-9fd8f1b78360 | -7.7039 | -48.7371 | 2025-09-03 08:30:00 | GOES-19 | BANDEIRANTES DO TOCANTINS | TOCANTINS | Brasil | 1703057 | 17 | 33 | nan | nan | nan | Amazônia | 83.6 |
| 2bf64760-e6a7-325e-abf8-6cbbdbb06256 | -11.5963 | -52.155 | 2025-09-03 08:30:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 80.8 |
| 4bf481b0-680c-3abc-a20a-198f08c0a4e3 | -7.7036 | -48.7587 | 2025-09-03 08:30:00 | GOES-19 | ARAPOEMA | TOCANTINS | Brasil | 1702307 | 17 | 33 | nan | nan | nan | Amazônia | 76.1 |
| 74316a47-e0fe-3ec8-86ef-03c9e63cd49e | -11.5966 | -52.134 | 2025-09-03 08:30:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 279.8 |
| 0a84c739-b96f-3928-bc19-27e2b311aec9 | -11.5774 | -52.157 | 2025-09-03 08:30:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 126.5 |
| 9d7caf2c-f603-3731-9231-9fd24d99ac1e | -10.0932 | -54.7667 | 2025-09-03 08:30:00 | GOES-19 | MATUPÁ | MATO GROSSO | Brasil | 5105606 | 51 | 33 | nan | nan | nan | Amazônia | 45.0 |
| 9dba59ae-8605-3d73-9eab-2f7ba219aaf3 | -7.6851 | -48.7386 | 2025-09-03 08:30:00 | GOES-19 | BANDEIRANTES DO TOCANTINS | TOCANTINS | Brasil | 1703057 | 17 | 33 | nan | nan | nan | Amazônia | 61.1 |
| cae0c85d-73c6-3797-9216-cb4c7b9ccd9f | -7.7226 | -48.7355 | 2025-09-03 08:30:00 | GOES-19 | BANDEIRANTES DO TOCANTINS | TOCANTINS | Brasil | 1703057 | 17 | 33 | nan | nan | nan | Amazônia | 163.3 |


[Clique aqui para ver as próximas entradas](README109.md)
