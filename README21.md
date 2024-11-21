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

## Dados Diários - Página 21

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 005a5e0c-06d0-3187-875d-9e29b97a9a1a | -4.86567 | -42.04024 | 2024-11-21 04:08:00 | NOAA-21 | JATOBÁ DO PIAUÍ | PIAUÍ | Brasil | 2205276 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| d68ae9fb-5782-3374-9eb1-6b12d8c1971c | -3.43061 | -49.2387 | 2024-11-21 04:08:00 | NOAA-21 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 22aab032-b214-3527-9678-487cefb91646 | -3.00281 | -51.30411 | 2024-11-21 04:08:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 6.8 |
| ce98dd78-9c9d-3500-b0bb-039b6fccf765 | -2.66959 | -46.16365 | 2024-11-21 04:08:00 | NOAA-21 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 6167827f-72bf-3156-90b9-12a973b077ef | -5.5797 | -42.604 | 2024-11-21 04:08:00 | NOAA-21 | MONSENHOR GIL | PIAUÍ | Brasil | 2206407 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| c0cf307b-b09b-3ff3-b555-630f994a3033 | -3.27965 | -50.52583 | 2024-11-21 04:08:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 6574a98b-d6dd-3174-88b4-409d862eceff | -2.78752 | -45.94781 | 2024-11-21 04:08:00 | NOAA-21 | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 0397bd69-1cdc-3039-a8c1-542e7b68447e | -3.27338 | -53.0173 | 2024-11-21 04:08:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 4afd94d0-5b44-3921-bbf5-7e61129e8f7f | -5.55536 | -46.19405 | 2024-11-21 04:08:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 9f117755-aff2-3601-bc55-5d6cd48ff0a3 | -3.04221 | -49.47087 | 2024-11-21 04:08:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ece9726b-0800-3b16-8735-a552296e21b8 | -3.46974 | -50.00994 | 2024-11-21 04:08:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 77cc0b5a-8840-3374-8615-e840ebf18c9a | -5.61901 | -39.51924 | 2024-11-21 04:08:00 | NOAA-21 | SENADOR POMPEU | CEARÁ | Brasil | 2312700 | 23 | 33 | nan | nan | nan | Caatinga | 1.7 |
| de078ffa-51e1-3e96-9944-a25f50d7b1be | -3.3401 | -50.49898 | 2024-11-21 04:08:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 6c4b636f-d2db-3a76-8ae1-8a0bc8b2f9ab | -1.72731 | -52.70705 | 2024-11-21 04:08:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| e050f1fb-a108-3f97-8624-70cb693899cf | -3.10268 | -49.45277 | 2024-11-21 04:08:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 35e05ccf-e2d5-3267-80e3-8fedced62178 | -2.24629 | -46.85582 | 2024-11-21 04:08:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7d10da19-9222-3866-802a-f0d692d18ab3 | -3.40992 | -49.17887 | 2024-11-21 04:08:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 633b7f3a-1d00-3588-87a9-87cfcc75ea5b | -5.03874 | -44.83067 | 2024-11-21 04:08:00 | NOAA-21 | JOSELÂNDIA | MARANHÃO | Brasil | 2105609 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 833ed8d1-f781-3a1a-bbe6-449aa727006b | -2.96072 | -51.41412 | 2024-11-21 04:08:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 398a7596-23f7-3823-9e9e-0b5a824a196a | -1.6442 | -52.61324 | 2024-11-21 04:08:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| c92c96b9-8c4a-36fe-acd1-1eabb48d1556 | -3.80896 | -42.54745 | 2024-11-21 04:08:00 | NOAA-21 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 0e531166-9baa-3610-b312-0fb6c9c5ee90 | -2.63925 | -46.2225 | 2024-11-21 04:08:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d4cf8df4-769a-3f6b-ba41-718b1c910ae4 | -3.74891 | -47.35899 | 2024-11-21 04:08:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| f5e832bd-4b66-380a-a930-39cf05bd90f0 | -5.87899 | -43.88076 | 2024-11-21 04:08:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| ca19f22a-01da-3070-af52-9dedf4f0e20e | -2.16459 | -46.39855 | 2024-11-21 04:08:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| fbd4b431-0ea6-3724-bfa1-3f4ad8c96e6c | -3.99806 | -46.39119 | 2024-11-21 04:08:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| afa7731b-f889-3783-b985-6664a0b6cea2 | -3.19241 | -54.32809 | 2024-11-21 04:08:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 73b5c80e-0dde-3d5f-b800-34184d36e380 | -0.29948 | -51.60887 | 2024-11-21 04:08:00 | NOAA-21 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 24649d51-9eae-3029-8cdd-67c3af3ab4b5 | -2.67319 | -51.88695 | 2024-11-21 04:08:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 17b3aaf8-b6eb-35e0-9e7f-817b56d58ecc | -3.46548 | -54.55946 | 2024-11-21 04:08:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 932e8886-61db-3f56-ad36-504d6682c88b | -3.81268 | -52.34992 | 2024-11-21 04:08:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 28f47cf2-d1b2-3e4d-823c-94a96d5ecf0b | -2.82693 | -46.67882 | 2024-11-21 04:08:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 9df9432c-383f-37bd-a105-750c738b9f92 | -2.84319 | -46.68533 | 2024-11-21 04:08:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 11a45a93-2154-3ce8-888f-dce6f6d7de7c | -3.27524 | -50.57913 | 2024-11-21 04:08:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e65c933f-7d12-317d-b075-d487fbd5c7f3 | -3.26037 | -50.39708 | 2024-11-21 04:08:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 4df04974-30a2-3c61-86bd-8e05bc339404 | -2.6161 | -51.80681 | 2024-11-21 04:08:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e95c8fff-a87e-304a-ae32-7fb47ec301cc | -2.70062 | -46.22838 | 2024-11-21 04:08:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 22161c00-63c5-3def-a520-26e67b983b4e | -4.25109 | -49.1866 | 2024-11-21 04:08:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 49a2b60a-6deb-3d5c-937c-49856f9dff49 | -5.60824 | -46.28696 | 2024-11-21 04:08:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 0ac91f03-9fa8-38e3-aa75-9971dbb93ae6 | -3.53652 | -51.61009 | 2024-11-21 04:08:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| ce9b3889-4d35-34ec-a865-da3a6a8ef6ee | -3.75822 | -52.4064 | 2024-11-21 04:08:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 7.6 |
| 2c533cf5-0761-3ba0-a977-0f065ae0c29d | -4.48499 | -44.75333 | 2024-11-21 04:08:00 | NOAA-21 | IGARAPÉ GRANDE | MARANHÃO | Brasil | 2105203 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 1405d0d9-f59b-3cba-9c94-f60e6747daf6 | -4.18772 | -43.93916 | 2024-11-21 04:08:00 | NOAA-21 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 884d5f87-e9b5-324e-b907-2b5e43ac056c | -2.70002 | -46.23204 | 2024-11-21 04:08:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| d701c9a7-5c09-3d44-be99-35abb6ade12e | -3.77083 | -50.70035 | 2024-11-21 04:08:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 5aa27a59-8ad3-3c03-b799-7c9dcc9e8af2 | -5.55162 | -46.3902 | 2024-11-21 04:08:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 76e5ed43-542f-3d5b-a558-d172924626dc | -1.25626 | -51.76303 | 2024-11-21 04:08:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| c307f1c2-d91e-32f7-a31d-3be8236895da | -5.10964 | -43.17254 | 2024-11-21 04:08:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 7.4 |
| c80fead6-73b2-3f87-9e74-61672c0e61f2 | -4.79135 | -44.43007 | 2024-11-21 04:08:00 | NOAA-21 | SANTO ANTÔNIO DOS LOPES | MARANHÃO | Brasil | 2110302 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| bdbcfa32-a9e5-3edb-a763-d62eb85efce6 | -1.39479 | -53.57701 | 2024-11-21 04:08:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| e9602349-e986-3bfc-9527-dbea3b59fe68 | -6.37938 | -44.74883 | 2024-11-21 04:08:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 91cda65b-63be-3993-a0a1-beeab89b9f3d | -4.48201 | -44.7485 | 2024-11-21 04:08:00 | NOAA-21 | IGARAPÉ GRANDE | MARANHÃO | Brasil | 2105203 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 049e1255-4d4a-327b-a52c-e3ba91ac8328 | -2.67248 | -48.28521 | 2024-11-21 04:08:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 3e94665d-f379-37b2-bf94-544ccbeb99b7 | -6.56028 | -41.97137 | 2024-11-21 04:08:00 | NOAA-21 | NOVO ORIENTE DO PIAUÍ | PIAUÍ | Brasil | 2206902 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| edde37e6-449d-3de3-8b56-6b3330f642e2 | -4.16631 | -46.82032 | 2024-11-21 04:08:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| b36b3a2c-6eb3-3845-a6cf-8be8dfbaa409 | -3.54252 | -51.43523 | 2024-11-21 04:08:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 30bcad94-c309-354f-ba39-6a10905d8c70 | -2.46098 | -47.0319 | 2024-11-21 04:08:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 2732bb1f-51a3-3e11-b189-b3ff2169ffca | -3.30684 | -50.36604 | 2024-11-21 04:08:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| bffb8cfc-bca5-3209-8414-66c8314dd1ca | -3.18625 | -48.57591 | 2024-11-21 04:08:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 5713a582-7dc0-3294-a0af-a9f2d0f31bf4 | 0.75512 | -50.2442 | 2024-11-21 04:08:00 | NOAA-21 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 00b7d94f-c6bd-33f1-a70c-ba18fa7141bf | -3.50449 | -48.22211 | 2024-11-21 04:08:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 521c2c1f-b7d7-3b3e-9841-6c5e030a08ce | -3.96478 | -46.72544 | 2024-11-21 04:08:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 7036c3b6-bf1e-315e-aaf5-b57f83e07678 | -3.54444 | -50.53109 | 2024-11-21 04:08:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 5e50c0ba-b59c-34d1-9bc9-2206e47add42 | -4.38447 | -47.77704 | 2024-11-21 04:08:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 0051b6c1-2048-3e0f-be3e-4b108b54d8f9 | -2.18416 | -52.13675 | 2024-11-21 04:08:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 8eb508c1-bfe9-3301-a1a2-6a90f0d30de4 | -5.55887 | -46.39575 | 2024-11-21 04:08:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 2b6f5327-963b-3c66-b97d-e06a4c749ddd | -5.94923 | -44.2435 | 2024-11-21 04:08:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 16.0 |
| d41e088f-9837-39c7-b2f8-8f01024877bb | -3.13943 | -41.22364 | 2024-11-21 04:08:00 | NOAA-21 | CHAVAL | CEARÁ | Brasil | 2303907 | 23 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 421c1f7c-140e-3e6d-9094-51d89ec06e15 | -4.95429 | -47.80194 | 2024-11-21 04:08:00 | NOAA-21 | CIDELÂNDIA | MARANHÃO | Brasil | 2103257 | 21 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 4d6512ce-f6a1-3190-ab3a-7b61aa2d4c32 | 0.75573 | -50.24807 | 2024-11-21 04:08:00 | NOAA-21 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 1.9 |
| a519e07f-633a-3b81-a761-82599651a8e5 | -4.24696 | -46.12164 | 2024-11-21 04:08:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 10.9 |
| 9c00b9fa-8b9e-3d56-a39d-28b67e41f308 | -3.54872 | -50.27592 | 2024-11-21 04:08:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 78ea8d5b-e70f-3b5a-95b9-12c0a4960e13 | -3.55381 | -50.24594 | 2024-11-21 04:08:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 789b10fb-f73b-3934-9cc9-b2e83f84e947 | -5.65984 | -43.35995 | 2024-11-21 04:08:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 9b188303-aacd-3b5c-8ba0-2373fc06bad1 | -3.32585 | -50.2542 | 2024-11-21 04:08:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 16ab72eb-5f49-368b-b310-992c72745e5e | -3.81819 | -52.34838 | 2024-11-21 04:08:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| a0d8b8a9-cb29-37bc-a76a-87c21b23de49 | -2.65204 | -46.14225 | 2024-11-21 04:08:00 | NOAA-21 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| be7adba4-62af-3e3c-b073-6ba235fbfa1d | -1.72974 | -52.70122 | 2024-11-21 04:08:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| fad48cc1-8c8b-35d1-8d75-b6d3b64670c9 | -2.47711 | -48.19573 | 2024-11-21 04:08:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 01f8dab6-558c-32a7-98d0-ef950a203a5f | -0.94164 | -51.72324 | 2024-11-21 04:08:00 | NOAA-21 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 1.9 |
| c09269df-aa8c-3709-bf9d-b84ffc9385cd | -1.60208 | -46.87027 | 2024-11-21 04:08:00 | NOAA-21 | SANTA LUZIA DO PARÁ | PARÁ | Brasil | 1506559 | 15 | 33 | nan | nan | nan | Amazônia | 12.7 |
| 71a43116-4467-3c9a-b5e2-46d1e2110f52 | -2.75962 | -52.12314 | 2024-11-21 04:08:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 7.8 |
| c3a1174e-754d-3ad0-a5e1-443826133fb1 | -4.62948 | -49.54484 | 2024-11-21 04:08:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 2fe31c07-920f-3155-89e8-2f5a79d27b30 | -2.20954 | -53.71536 | 2024-11-21 04:08:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 74f52688-f470-35e0-9162-e8d8cc567c84 | -4.4885 | -47.10651 | 2024-11-21 04:08:00 | NOAA-21 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 3dd5af47-0d70-3fc3-a333-b58b33150712 | -3.91013 | -45.08988 | 2024-11-21 04:08:00 | NOAA-21 | PIO XII | MARANHÃO | Brasil | 2108702 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6f23055f-41b2-31e0-b32e-4a6f96c53208 | -6.07402 | -41.03106 | 2024-11-21 04:08:00 | NOAA-21 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 8a1b6527-170c-3a39-a271-405ed3797f0b | -6.98259 | -40.30045 | 2024-11-21 04:08:00 | NOAA-21 | CAMPOS SALES | CEARÁ | Brasil | 2302701 | 23 | 33 | nan | nan | nan | Caatinga | 1.2 |
| c35a777e-f256-3a66-b26d-37b4b5e1a357 | -5.27746 | -45.44691 | 2024-11-21 04:08:00 | NOAA-21 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| bdea85ec-8d4d-3552-9b38-e496d3259111 | -4.818 | -45.75961 | 2024-11-21 04:08:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 8b05a61c-97fe-3623-a7d2-6af4646e7a49 | -3.29388 | -53.86369 | 2024-11-21 04:08:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 14200d47-b53e-3e07-bf39-8eb4b6e8497e | -4.00575 | -43.25094 | 2024-11-21 04:08:00 | NOAA-21 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 33e5d237-7d6b-3d85-984e-3a61b3ba5736 | -5.95272 | -44.46782 | 2024-11-21 04:08:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 91638493-ea78-3c87-a17e-6f7efe6bb16a | -3.26953 | -50.61837 | 2024-11-21 04:08:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 41a76c32-80da-3b69-9f9f-357f734578c9 | -6.21008 | -46.22816 | 2024-11-21 04:08:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 5c47d408-23f4-308d-b28d-4eb5c0b629a1 | -4.59973 | -47.0356 | 2024-11-21 04:08:00 | NOAA-21 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| be255b5d-ab5d-3dda-b658-7bc5d7b796f8 | -4.47835 | -44.74793 | 2024-11-21 04:08:00 | NOAA-21 | IGARAPÉ GRANDE | MARANHÃO | Brasil | 2105203 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 09725ade-b201-3cd1-aa4b-3780eda3eacd | -4.13502 | -47.73211 | 2024-11-21 04:08:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| edf9ee33-bb52-3d01-a89b-56b4d452ca9d | -4.38818 | -47.75504 | 2024-11-21 04:08:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 68970acf-90e3-326d-aa0d-7d2b6e563ce5 | -5.73708 | -44.27579 | 2024-11-21 04:08:00 | NOAA-21 | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |


[Clique aqui para ver as próximas entradas](README22.md)
