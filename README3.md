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

## Dados Diários - Página 3

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 7e6a11d3-0f2e-35f9-a2bc-9f60ff226d77 | -6.4889 | -56.2139 | 2025-07-28 02:00:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 41.2 |
| a6328651-d545-321f-8c4c-be05a603567c | -17.3643 | -42.6284 | 2025-07-28 02:10:00 | GOES-19 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 85.8 |
| 9dd47c7b-af25-3e39-a54f-06a2855d98fb | -21.2128 | -48.7167 | 2025-07-28 02:10:00 | GOES-19 | ARIRANHA | SÃO PAULO | Brasil | 3503703 | 35 | 33 | nan | nan | nan | Mata Atlântica | 98.7 |
| 5bb4d410-3809-3896-8b00-9c3abcd73125 | -6.4889 | -56.2139 | 2025-07-28 02:10:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 54.1 |
| 8d34fef9-1191-33e9-a7e5-c8293a82ad6a | -4.1601 | -46.8322 | 2025-07-28 02:10:00 | GOES-19 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 100.4 |
| 721f62c1-b313-3940-a006-0b6d0915a90f | -6.5074 | -56.213 | 2025-07-28 02:10:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 69.8 |
| 9c042630-8a73-3642-a977-6a034b349686 | -21.2122 | -48.74 | 2025-07-28 02:10:00 | GOES-19 | ARIRANHA | SÃO PAULO | Brasil | 3503703 | 35 | 33 | nan | nan | nan | Mata Atlântica | 129.5 |
| 2ec45bd0-fdf2-3fdd-8708-b1b6d7cdbd36 | -4.1789 | -46.8092 | 2025-07-28 02:10:00 | GOES-19 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 71.1 |
| e0533955-ab11-3c0b-958e-f78ce4c9ba2b | -4.1603 | -46.8101 | 2025-07-28 02:10:00 | GOES-19 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 162.6 |
| 3d8b173b-5088-30e8-ae19-51acf3c14cef | -4.1603 | -46.8101 | 2025-07-28 02:20:00 | GOES-19 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 151.4 |
| 3c00ccbb-8f00-31e3-996c-d0f2e1df1477 | -6.4889 | -56.2139 | 2025-07-28 02:20:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 49.6 |
| 31b6bb59-3c80-336d-a469-827a4e4f970a | -4.1601 | -46.8322 | 2025-07-28 02:20:00 | GOES-19 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 121.0 |
| f0c46aeb-1541-3418-9a5c-e2890b2a4fe6 | -6.5074 | -56.213 | 2025-07-28 02:20:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 58.7 |
| 380c378a-0646-3acf-9ff5-5ba7129655f4 | -4.1789 | -46.8092 | 2025-07-28 02:20:00 | GOES-19 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 59.7 |
| 36a3486c-42c8-3d4e-8524-1075fea058a4 | -17.3643 | -42.6284 | 2025-07-28 02:20:00 | GOES-19 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 63.6 |
| 40cbb16b-a910-350d-b631-314f9cde7f67 | -4.1787 | -46.8313 | 2025-07-28 02:20:00 | GOES-19 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 58.5 |
| ec3058ca-addd-3a76-9237-c81e2f188d35 | -4.1789 | -46.8092 | 2025-07-28 02:30:00 | GOES-19 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 75.7 |
| ae52b6b6-11de-3a6b-92a9-9ec07bf85325 | -6.5074 | -56.213 | 2025-07-28 02:30:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 58.2 |
| 1dfffe47-4028-33cf-8f65-7bf95a7c1819 | -17.3643 | -42.6284 | 2025-07-28 02:30:00 | GOES-19 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 62.3 |
| 90de5c69-c6c4-37de-a180-09c511bd4705 | -6.4889 | -56.2139 | 2025-07-28 02:30:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 44.6 |
| adc06407-dd19-301a-bbe1-d7417e5e8ea2 | -4.1603 | -46.8101 | 2025-07-28 02:30:00 | GOES-19 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 223.8 |
| 30f67139-3ec0-39e1-962c-c96a5b595144 | -4.1601 | -46.8322 | 2025-07-28 02:30:00 | GOES-19 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 111.8 |
| 66e15707-a1ac-3dfe-a318-240f44213094 | -4.1601 | -46.8322 | 2025-07-28 02:40:00 | GOES-19 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 159.6 |
| 7e1fe8ec-6374-3ffe-9abb-fcc9dc2c5157 | -17.3643 | -42.6284 | 2025-07-28 02:40:00 | GOES-19 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 52.0 |
| 8ac8bfe0-d3a9-3817-af9e-73e59f77831f | -4.1603 | -46.8101 | 2025-07-28 02:40:00 | GOES-19 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 206.6 |
| 64388b94-c30f-37cf-bb74-2174f80e189e | -6.4889 | -56.2139 | 2025-07-28 02:40:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 52.3 |
| 2e93e402-6e98-3043-8611-404ddb7840e3 | -4.1601 | -46.8322 | 2025-07-28 02:50:00 | GOES-19 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 117.7 |
| 9b0bb024-7403-3748-a911-ecfa1d51a3df | -4.1787 | -46.8313 | 2025-07-28 02:50:00 | GOES-19 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 73.6 |
| 67b8e8c4-2b30-3ae9-aa2d-fd9b37060721 | -6.5074 | -56.213 | 2025-07-28 02:50:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 54.5 |
| 2f0b8cce-ed8a-3c07-982f-177b55a4a755 | -4.1789 | -46.8092 | 2025-07-28 02:50:00 | GOES-19 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 100.8 |
| f81a3165-4479-3b92-a664-58ddf27069be | -4.1603 | -46.8101 | 2025-07-28 02:50:00 | GOES-19 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 172.4 |
| 7a9379b0-7d7b-350c-b72f-f1f58db840c5 | -5.47187 | -36.66994 | 2025-07-28 02:58:00 | NOAA-21 | AFONSO BEZERRA | RIO GRANDE DO NORTE | Brasil | 2400307 | 24 | 33 | nan | nan | nan | Caatinga | 3.9 |
| b47fe9e3-6965-3e2e-8c0a-d11025dc776e | -5.47449 | -36.66898 | 2025-07-28 02:58:00 | NOAA-21 | AFONSO BEZERRA | RIO GRANDE DO NORTE | Brasil | 2400307 | 24 | 33 | nan | nan | nan | Caatinga | 3.5 |
| 5277bc9c-68f8-327b-9b43-8124475eccb7 | -4.1601 | -46.8322 | 2025-07-28 03:00:00 | GOES-19 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 121.3 |
| 42a88e36-92bd-323e-8e2a-25e97f052392 | -6.5074 | -56.213 | 2025-07-28 03:00:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 47.4 |
| 64cfcf4d-1453-39d4-92dd-8d3abdc914d1 | -4.1789 | -46.8092 | 2025-07-28 03:00:00 | GOES-19 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 93.3 |
| 5511b9c9-e439-3c79-800c-e0c3eb8add2c | -4.1603 | -46.8101 | 2025-07-28 03:00:00 | GOES-19 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 145.7 |
| d5bad6c2-30c8-3f03-b570-3070db706e50 | -4.1787 | -46.8313 | 2025-07-28 03:00:00 | GOES-19 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 81.2 |
| 9fb06c0a-d7bd-3053-9069-4d0469cbec96 | -6.4889 | -56.2139 | 2025-07-28 03:10:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 35.9 |
| f04428ea-0a61-3ddd-a4a8-1d39e648a334 | -4.1789 | -46.8092 | 2025-07-28 03:10:00 | GOES-19 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 63.8 |
| fe27b103-b3c6-30a4-8125-45490edb0d74 | -4.1603 | -46.8101 | 2025-07-28 03:10:00 | GOES-19 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 152.7 |
| 8b89c24b-21c9-3194-9d9d-9b6b95adc554 | -6.5074 | -56.213 | 2025-07-28 03:10:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 44.4 |
| 4e83b607-b0bd-3f26-89fb-f41bde3b8bd4 | -4.1601 | -46.8322 | 2025-07-28 03:10:00 | GOES-19 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 111.1 |
| 66020f1e-3c33-37bf-88a4-8ecf5aa4d947 | -6.4889 | -56.2139 | 2025-07-28 03:20:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 38.0 |
| 0a57471e-064a-3267-ae94-47d29cfac36f | -4.1789 | -46.8092 | 2025-07-28 03:20:00 | GOES-19 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 76.0 |
| dcfe79f0-9faf-3137-87e6-f941606829bf | -4.1601 | -46.8322 | 2025-07-28 03:20:00 | GOES-19 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 68.0 |
| 1da5ea60-2b63-34b8-ab8c-d4e57cb56592 | -6.5074 | -56.213 | 2025-07-28 03:20:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 45.7 |
| 917381ba-72f6-3317-b0bf-61ca9fb73b00 | -4.1603 | -46.8101 | 2025-07-28 03:20:00 | GOES-19 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 127.5 |
| 8e6d1df1-4fcc-3ddc-8d45-4e1d33b8ef30 | -4.59862 | -43.30706 | 2025-07-28 03:23:00 | NPP-375D | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 2804cfd7-c87e-34b7-889a-7fb20c38d5a3 | -2.95572 | -41.35987 | 2025-07-28 03:23:00 | NPP-375D | CAJUEIRO DA PRAIA | PIAUÍ | Brasil | 2202083 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 11e3af7e-3bc7-36c1-8a91-f1c64841d20c | -5.87749 | -39.76191 | 2025-07-28 03:23:00 | NPP-375D | MOMBAÇA | CEARÁ | Brasil | 2308500 | 23 | 33 | nan | nan | nan | Caatinga | 1.3 |
| bff8f7ce-e96e-3da0-941a-69e785ee1825 | -2.94939 | -41.3587 | 2025-07-28 03:23:00 | NPP-375D | CAJUEIRO DA PRAIA | PIAUÍ | Brasil | 2202083 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 8d9b03d0-9ff6-3992-9a6d-46c4a2616b08 | -5.47419 | -36.67009 | 2025-07-28 03:23:00 | NPP-375D | AFONSO BEZERRA | RIO GRANDE DO NORTE | Brasil | 2400307 | 24 | 33 | nan | nan | nan | Caatinga | 2.4 |
| bf5da38d-6133-3c8e-a417-1d8539f6ab1c | -5.00156 | -42.29958 | 2025-07-28 03:23:00 | NPP-375D | COIVARAS | PIAUÍ | Brasil | 2202737 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 61116b0f-7f46-3f78-9a89-01bafd8d65a0 | -5.00107 | -42.29725 | 2025-07-28 03:23:00 | NPP-375D | COIVARAS | PIAUÍ | Brasil | 2202737 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| dae6ab1b-ef6c-38d1-a17e-276a18a7d265 | -4.59992 | -43.30684 | 2025-07-28 03:23:00 | NPP-375D | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 80c173d8-8ec5-3052-b696-9aa09ced792f | -4.59879 | -43.3133 | 2025-07-28 03:23:00 | NPP-375D | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 4be58ed2-22ad-37ed-a8c0-525cdc7deb15 | -5.47493 | -36.66571 | 2025-07-28 03:23:00 | NPP-375D | AFONSO BEZERRA | RIO GRANDE DO NORTE | Brasil | 2400307 | 24 | 33 | nan | nan | nan | Caatinga | 2.4 |
| e6fcc6de-cc6a-37f4-bea7-61c918fa6ce3 | -5.87685 | -39.7655 | 2025-07-28 03:23:00 | NPP-375D | MOMBAÇA | CEARÁ | Brasil | 2308500 | 23 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 44610227-dda0-36be-8f02-8456be72a5a4 | -5.00753 | -42.29869 | 2025-07-28 03:23:00 | NPP-375D | COIVARAS | PIAUÍ | Brasil | 2202737 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 50a3dd9c-013d-39b0-bdce-d5d4f1a81d23 | -9.37384 | -40.32083 | 2025-07-28 03:25:00 | NPP-375D | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 1.6 |
| a77d6a27-535d-3a00-ade1-ba2b4ff7e9fd | -10.52013 | -42.55696 | 2025-07-28 03:25:00 | NPP-375D | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 8.9 |
| b6a3969e-9733-30db-af1d-e8bfab4c97a7 | -12.7464 | -44.73989 | 2025-07-28 03:25:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 30f7b1c1-83fe-3c37-8aff-ad48d4d1584a | -7.29416 | -43.07984 | 2025-07-28 03:25:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 4fe1ab82-dd35-3c4c-9cc6-d59dc24aaa7e | -13.29705 | -40.98121 | 2025-07-28 03:25:00 | NPP-375D | IRAMAIA | BAHIA | Brasil | 2914307 | 29 | 33 | nan | nan | nan | Caatinga | 0.5 |
| bd66ab2d-f9df-3e54-8095-f3e8130c9286 | -6.38307 | -43.38235 | 2025-07-28 03:25:00 | NPP-375D | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 5b209319-b3a9-3a2a-9ed4-ad8e9b5826f2 | -12.73979 | -44.73849 | 2025-07-28 03:25:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 0e230af5-a5e7-32f8-b644-0ba23590ec6c | -10.52102 | -42.55246 | 2025-07-28 03:25:00 | NPP-375D | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 6.2 |
| dc8a0e41-1342-30d8-97c5-dd8d52a40150 | -7.6586 | -44.80153 | 2025-07-28 03:25:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 5ebaa484-1248-36d2-879f-9a2968696f78 | -5.86667 | -44.02599 | 2025-07-28 03:25:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| b199fc5f-3b4c-3afc-a3e6-326e48819384 | -6.39181 | -43.37704 | 2025-07-28 03:25:00 | NPP-375D | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 123c3d1c-fef2-35c5-aebf-6660c1824425 | -12.74302 | -44.73858 | 2025-07-28 03:25:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 1479d980-7761-3a71-9a6a-c7fc4068d5de | -5.87376 | -44.02734 | 2025-07-28 03:25:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 150b2f55-2ebb-34b6-9463-b0fb088d37e0 | -7.29562 | -43.0862 | 2025-07-28 03:25:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 0c93e575-5587-3480-9f2c-3e1036b1540a | -6.3898 | -43.38397 | 2025-07-28 03:25:00 | NPP-375D | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 81d02870-6d76-3668-9f95-af7ae52f56b6 | -6.39098 | -43.37746 | 2025-07-28 03:25:00 | NPP-375D | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ba0835c0-abac-3ea9-9c4b-819db55c354d | -6.38384 | -43.38206 | 2025-07-28 03:25:00 | NPP-375D | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 1cf08f95-9945-35a0-92dd-9c18853932bb | -7.2901 | -43.07918 | 2025-07-28 03:25:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 87734634-4791-37cc-87e7-c08def90b987 | -7.29664 | -43.08068 | 2025-07-28 03:25:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 288f9f54-5417-37b0-b11f-4e5b7d2972e0 | -13.29183 | -40.98026 | 2025-07-28 03:25:00 | NPP-375D | IRAMAIA | BAHIA | Brasil | 2914307 | 29 | 33 | nan | nan | nan | Caatinga | 0.8 |
| cabd8cf4-c5f9-3e3f-8fb5-63f79ef93741 | -7.657 | -44.80981 | 2025-07-28 03:25:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| bc34486f-4b91-3008-b056-9d3e349f5aa6 | -9.37446 | -40.31746 | 2025-07-28 03:25:00 | NPP-375D | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 1.6 |
| fada4379-d3ec-3c2e-b2cc-7105587671ea | -14.49526 | -46.549 | 2025-07-28 03:28:00 | NPP-375D | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 71c5b213-3918-3a5b-babd-346dd935636c | -14.98316 | -46.97148 | 2025-07-28 03:28:00 | NPP-375D | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| f54f40fb-86f9-35f0-a27a-f3ce008746b6 | -17.53761 | -43.91931 | 2025-07-28 03:28:00 | NPP-375D | BOCAIÚVA | MINAS GERAIS | Brasil | 3107307 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 47947d60-71d8-3f48-9060-e7d4cbe7f4b4 | -17.3617 | -42.6475 | 2025-07-28 03:28:00 | NPP-375D | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 68696a0f-1579-3ee2-a055-778c35320975 | -13.30418 | -44.18138 | 2025-07-28 03:28:00 | NPP-375D | SANTA MARIA DA VITÓRIA | BAHIA | Brasil | 2928109 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| b5065701-e619-383e-9b8c-43845205f1be | -13.52943 | -46.29024 | 2025-07-28 03:28:00 | NPP-375D | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| e0ba4e95-af6f-3cd0-84de-3b05081278f3 | -17.34975 | -42.64115 | 2025-07-28 03:28:00 | NPP-375D | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ccc8faa4-c613-3efe-a869-9699ebb3ebc8 | -17.36192 | -42.63644 | 2025-07-28 03:28:00 | NPP-375D | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 4.9 |
| a54b2df3-5f2f-3aae-a9d8-d4afd6449539 | -14.48265 | -46.53872 | 2025-07-28 03:28:00 | NPP-375D | SIMOLÂNDIA | GOIÁS | Brasil | 5220686 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 4939f38a-975a-3511-b570-e0b0308b85db | -17.36321 | -42.64042 | 2025-07-28 03:28:00 | NPP-375D | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 9da8cc1f-84e1-3da8-be85-a1fd4471b82d | -17.36119 | -42.63999 | 2025-07-28 03:28:00 | NPP-375D | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 03d30015-c353-3c4a-b055-4fa134e58af1 | -17.3544 | -42.64576 | 2025-07-28 03:28:00 | NPP-375D | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 4b1eea21-63bc-320b-add9-d08a16596a7b | -14.4901 | -46.55007 | 2025-07-28 03:28:00 | NPP-375D | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f8f3728a-c169-3543-ad69-d14669d54bb0 | -19.50779 | -48.48188 | 2025-07-28 03:28:00 | NPP-375D | PRATA | MINAS GERAIS | Brasil | 3152808 | 31 | 33 | nan | nan | nan | Cerrado | 14.6 |
| b517e662-c380-3f06-8be9-e49a693a02c8 | -19.50788 | -48.47483 | 2025-07-28 03:28:00 | NPP-375D | PRATA | MINAS GERAIS | Brasil | 3152808 | 31 | 33 | nan | nan | nan | Cerrado | 5.9 |
| c17e7d4a-3929-3a72-8f00-487b8550ea50 | -17.36246 | -42.64397 | 2025-07-28 03:28:00 | NPP-375D | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 4.7 |
| fbca6655-ca86-3aac-9853-d608095cd3a7 | -17.35974 | -42.64704 | 2025-07-28 03:28:00 | NPP-375D | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 068b5cea-d53c-396d-9e53-31b500b7df08 | -14.49173 | -46.54286 | 2025-07-28 03:28:00 | NPP-375D | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |


[Clique aqui para ver as próximas entradas](README4.md)
