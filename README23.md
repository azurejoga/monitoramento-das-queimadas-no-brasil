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

## Dados Diários - Página 23

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 71a73c74-1ec3-3d3a-b9b8-8effab9cd2af | -21.04573 | -54.54793 | 2025-07-10 04:29:00 | NOAA-20 | SIDROLÂNDIA | MATO GROSSO DO SUL | Brasil | 5007901 | 50 | 33 | nan | nan | nan | Cerrado | 0.9 |
| d7473af7-4efd-3447-9c73-d84d1c225b4f | -21.44011 | -54.57422 | 2025-07-10 04:29:00 | NOAA-20 | NOVA ALVORADA DO SUL | MATO GROSSO DO SUL | Brasil | 5006002 | 50 | 33 | nan | nan | nan | Cerrado | 1.6 |
| cb4bd93b-f17d-3b16-8d85-e89850639296 | -19.39616 | -54.46495 | 2025-07-10 04:29:00 | NOAA-20 | SÃO GABRIEL DO OESTE | MATO GROSSO DO SUL | Brasil | 5007695 | 50 | 33 | nan | nan | nan | Cerrado | 0.6 |
| f6f9cfaf-c4e5-36b7-a3f6-aa354ff777b9 | -21.77399 | -52.75964 | 2025-07-10 04:29:00 | NOAA-20 | BATAGUASSU | MATO GROSSO DO SUL | Brasil | 5001904 | 50 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 62f83d94-50ca-336a-a973-07d9a2d2113f | -20.86158 | -55.29547 | 2025-07-10 04:29:00 | NOAA-20 | DOIS IRMÃOS DO BURITI | MATO GROSSO DO SUL | Brasil | 5003488 | 50 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 721c0859-8d86-344f-a223-73baa8b2d2b7 | -20.07832 | -45.81672 | 2025-07-10 04:29:00 | NOAA-20 | IGUATAMA | MINAS GERAIS | Brasil | 3130309 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| ca2d5973-4d3d-35ce-84d7-a9a5f49ffe58 | -21.9583 | -56.07453 | 2025-07-10 04:29:00 | NOAA-20 | PONTA PORÃ | MATO GROSSO DO SUL | Brasil | 5006606 | 50 | 33 | nan | nan | nan | Cerrado | 0.8 |
| c4f51eb1-cadd-31e3-81fd-dfe747e03fad | -21.76413 | -48.12339 | 2025-07-10 04:29:00 | NOAA-20 | ARARAQUARA | SÃO PAULO | Brasil | 3503208 | 35 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 1cdbe85b-c15b-310b-810b-4ea41e4fb5a6 | -22.24431 | -49.61087 | 2025-07-10 04:29:00 | NOAA-20 | GARÇA | SÃO PAULO | Brasil | 3516705 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.7 |
| 2800a4c9-000b-3baf-8962-ea287565780b | -25.19195 | -49.32716 | 2025-07-10 04:29:00 | NOAA-20 | RIO BRANCO DO SUL | PARANÁ | Brasil | 4122206 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 90e8071d-8307-3b3a-a2eb-dff1acef7bff | -21.35045 | -48.62291 | 2025-07-10 04:29:00 | NOAA-20 | CÂNDIDO RODRIGUES | SÃO PAULO | Brasil | 3510104 | 35 | 33 | nan | nan | nan | Mata Atlântica | 5.5 |
| 7192b5d7-cf73-3469-aa9c-2262105687c6 | -22.34887 | -48.23571 | 2025-07-10 04:29:00 | NOAA-20 | BROTAS | SÃO PAULO | Brasil | 3507902 | 35 | 33 | nan | nan | nan | Cerrado | 0.5 |
| f2d57bbc-7804-32ee-9c88-73e8f61ef19c | -21.96244 | -56.07547 | 2025-07-10 04:29:00 | NOAA-20 | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 5d922791-f7f7-3aea-b382-755578485bfe | -18.64635 | -55.72047 | 2025-07-10 04:29:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.7 |
| 4e9e1d8a-a3c7-351a-997a-e0801d35c452 | -21.76364 | -48.1263 | 2025-07-10 04:29:00 | NOAA-20 | ARARAQUARA | SÃO PAULO | Brasil | 3503208 | 35 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 4afda98b-9d6e-3d45-b672-ad8619d1d059 | -10.5776 | -49.1316 | 2025-07-10 04:30:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 89.2 |
| 97fc4219-b276-350f-9809-73bce35c100d | -10.5773 | -49.1533 | 2025-07-10 04:30:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 88.4 |
| ec5b3376-de32-3067-a2c2-2838d40d1779 | -10.6675 | -49.4679 | 2025-07-10 04:30:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 78.8 |
| fac40d90-07d9-317f-a9a4-097d0ad1e85a | -27.21667 | -50.66345 | 2025-07-10 04:32:00 | NOAA-20 | CURITIBANOS | SANTA CATARINA | Brasil | 4204806 | 42 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 9b579abf-45db-3dae-a4c9-4c963076b5d6 | -26.18346 | -50.58279 | 2025-07-10 04:32:00 | NOAA-20 | CANOINHAS | SANTA CATARINA | Brasil | 4203808 | 42 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| c596799c-e436-38ec-af62-b0570b10aaff | -10.5776 | -49.1316 | 2025-07-10 04:40:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 104.8 |
| 721348db-e892-380e-9bb9-ae95f86c1eb1 | -8.5028 | -43.2614 | 2025-07-10 04:40:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 87.6 |
| 97c9b79d-582b-3cd6-aab5-7a04fb3e14ba | -10.5773 | -49.1533 | 2025-07-10 04:40:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 89.7 |
| 5d4b9c39-1e4f-3bcb-b59f-4adedc269774 | -6.9914 | -43.4882 | 2025-07-10 04:40:00 | GOES-19 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 71.1 |
| 55fc684b-0069-3278-8849-74ab736250fa | -8.5025 | -43.285 | 2025-07-10 04:40:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 241.9 |
| e765c061-7602-3e9a-8508-4fed2835b77d | -8.5211 | -43.3063 | 2025-07-10 04:40:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Cerrado | 82.6 |
| 26979e30-63c0-36bf-891b-50c7e77af6be | -10.6675 | -49.4679 | 2025-07-10 04:40:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 69.7 |
| 79b4800f-2b02-39bd-b62f-8dffd1d945ee | -8.5018 | -43.332 | 2025-07-10 04:40:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 95.9 |
| c98285e2-8a65-3150-af9e-73dfc86a0a89 | -8.5022 | -43.3085 | 2025-07-10 04:40:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 259.9 |
| 258cbe1a-d9af-3732-a2e9-463e33a5d102 | -10.6675 | -49.4679 | 2025-07-10 04:50:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 64.5 |
| dfa9ff53-7160-3d22-af8d-d1963a2803a2 | -10.5773 | -49.1533 | 2025-07-10 04:50:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 88.4 |
| 2e7ddc43-e2f4-30e3-9370-9392c2e38127 | -10.5776 | -49.1316 | 2025-07-10 04:50:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 87.6 |
| 0504aa67-ee86-3432-9758-30c6b640ca8b | -8.5025 | -43.285 | 2025-07-10 05:00:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 236.3 |
| fc3233d1-59b2-3fac-898a-5d22eba5b105 | -8.5214 | -43.2828 | 2025-07-10 05:00:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 62.9 |
| 11644c28-63bf-3ff6-b3b5-777781dfdd6a | -10.5776 | -49.1316 | 2025-07-10 05:00:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 89.5 |
| d56ac387-5e48-337b-a307-a09eecc142c9 | -8.5211 | -43.3063 | 2025-07-10 05:00:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Cerrado | 86.3 |
| 038ecc70-c020-387d-a943-e0de162f9f12 | -10.5773 | -49.1533 | 2025-07-10 05:00:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 85.2 |
| e547c23a-a304-3360-8f8b-98b30f83ff00 | -8.5022 | -43.3085 | 2025-07-10 05:00:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 289.8 |
| 445f7446-fe1a-308f-bde7-654763dd2c88 | -8.5018 | -43.332 | 2025-07-10 05:00:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 98.8 |
| c0c28af1-fe2e-33d8-b537-c167aac0d933 | -8.5028 | -43.2614 | 2025-07-10 05:00:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 74.8 |
| 99026219-b1dd-3115-bb64-e0f91f63dc5f | -8.5214 | -43.2828 | 2025-07-10 05:10:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 63.2 |
| 624aa9c5-e4c0-3abe-a443-3e02ea5d285a | -10.5773 | -49.1533 | 2025-07-10 05:10:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 80.2 |
| 1ce00166-cc93-3938-96fa-771f18fbcbe7 | -8.5018 | -43.332 | 2025-07-10 05:10:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 105.3 |
| b7656f38-4f1f-33b7-89b8-316fab09fcb1 | -8.5025 | -43.285 | 2025-07-10 05:10:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 218.8 |
| ccb61423-9c55-3e8d-ac25-44b5d376806f | -8.5022 | -43.3085 | 2025-07-10 05:10:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 273.6 |
| 5453987f-eb83-3a5f-b198-2af851ecdc1b | -8.5028 | -43.2614 | 2025-07-10 05:10:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 75.0 |
| 7472c777-61e0-3868-b2ae-a312c9801564 | -8.5211 | -43.3063 | 2025-07-10 05:10:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Cerrado | 90.0 |
| 027a0a63-4d08-349b-901d-99fac88c068e | -10.5776 | -49.1316 | 2025-07-10 05:10:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 96.0 |
| ee701578-0bd9-3ba6-8f7b-9d8f6d81f52c | -5.03305 | -47.96718 | 2025-07-10 05:16:00 | NOAA-21 | CIDELÂNDIA | MARANHÃO | Brasil | 2103257 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f11b8c20-856f-3de0-bcb1-95fa0c1af416 | -3.74743 | -47.11907 | 2025-07-10 05:16:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| e7a01b0d-a531-3fd8-b16c-4cde7b219507 | -3.74573 | -47.12622 | 2025-07-10 05:16:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 8d29b1fa-c44d-3c21-ae46-46197a5dd440 | -3.74639 | -47.12149 | 2025-07-10 05:16:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 570578e5-d3a7-3169-a848-5961c6c2a7de | -3.74705 | -47.11668 | 2025-07-10 05:16:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 37a54877-fabb-3bc8-a168-f450ab85587d | -3.7529 | -47.12488 | 2025-07-10 05:16:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 5f9153eb-c95e-3948-bca8-551800bb6f55 | -4.22292 | -47.21085 | 2025-07-10 05:16:00 | NOAA-21 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 0ce63342-d8b6-3a27-92ef-25c8ed63e42d | -2.75223 | -54.06576 | 2025-07-10 05:16:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 32df5aee-03e6-3497-ab0a-48d4439d8f2c | -6.67442 | -46.30192 | 2025-07-10 05:16:00 | NOAA-21 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| e6f11dea-b2e3-3aef-bb89-de82ef36a762 | -5.02959 | -47.97011 | 2025-07-10 05:16:00 | NOAA-21 | CIDELÂNDIA | MARANHÃO | Brasil | 2103257 | 21 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 9b63fe73-4526-32b2-8789-34f21d0c8714 | -3.51421 | -47.21429 | 2025-07-10 05:16:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 309b084a-5d4d-312e-bad8-cc697dd8911a | -3.74674 | -47.12383 | 2025-07-10 05:16:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| f8f5333f-cc72-313d-822d-541c3a45cade | -6.17507 | -48.05121 | 2025-07-10 05:16:00 | NOAA-21 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 5b33fddd-c404-3484-ba3e-5b97057079f9 | -4.22911 | -47.2117 | 2025-07-10 05:16:00 | NOAA-21 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 7.9 |
| a5c50eb9-5f5f-35a0-956e-80b1af0d95b4 | -2.53343 | -53.95745 | 2025-07-10 05:16:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| e08b828a-0da4-3f67-9341-9c8269f14bd4 | -3.75358 | -47.1202 | 2025-07-10 05:16:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 1236c7bb-88d9-3694-bbda-96e399d649e7 | -6.68117 | -46.3029 | 2025-07-10 05:16:00 | NOAA-21 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 45d7417c-e1ea-3a76-ac36-786ad67e2d69 | -4.13126 | -54.89701 | 2025-07-10 05:16:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 6e211931-284f-3f8c-b88e-abd41b28b267 | -7.01318 | -49.81934 | 2025-07-10 05:16:00 | NOAA-21 | XINGUARA | PARÁ | Brasil | 1508407 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| f3b679eb-4424-3215-8cfc-11cf31be81ec | -3.75254 | -47.1226 | 2025-07-10 05:16:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| d8a0388a-4d91-3e15-9c7a-5321c14f0d4a | -4.12861 | -54.89899 | 2025-07-10 05:16:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e67eae49-d91f-3e56-b42f-60b6cf2b9616 | -3.75189 | -47.12728 | 2025-07-10 05:16:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| d52b56ea-e195-3f9f-a97f-aae6c346db1a | -5.03248 | -47.97137 | 2025-07-10 05:16:00 | NOAA-21 | CIDELÂNDIA | MARANHÃO | Brasil | 2103257 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 899fa630-12aa-3474-a66c-450e0f71f924 | -12.56474 | -52.21661 | 2025-07-10 05:18:00 | NOAA-21 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7660249f-da8a-30a6-8b4e-65ea5929b547 | -11.8321 | -48.21369 | 2025-07-10 05:18:00 | NOAA-21 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 8f04edff-3f7c-37b1-bfe5-be9d0a96e037 | -6.62872 | -56.27937 | 2025-07-10 05:18:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| c53294fb-8a7d-39de-89cf-59fb37d0fdf4 | -13.38196 | -47.88971 | 2025-07-10 05:18:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 1a6c2900-bcb4-36c3-b815-20cd93b35d3f | -10.66076 | -49.46597 | 2025-07-10 05:18:00 | NOAA-21 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 11.6 |
| 0d0949fa-18e1-36c3-bb18-114e4de68716 | -6.62934 | -56.27531 | 2025-07-10 05:18:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 0e550566-1e13-3254-967e-f25d9b13064f | -9.71776 | -62.16248 | 2025-07-10 05:18:00 | NOAA-21 | VALE DO ANARI | RONDÔNIA | Brasil | 1101757 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| dd5de6ba-ccbf-3a71-8b6b-8bd554e0fa57 | -11.33012 | -51.44843 | 2025-07-10 05:18:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ead3d95d-772a-380e-a760-b8d1b546888d | -10.13264 | -57.7803 | 2025-07-10 05:18:00 | NOAA-21 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c903e956-b9c9-3078-aa5b-c07f956590c6 | -10.09644 | -60.4957 | 2025-07-10 05:18:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| eecc8ee2-a2a1-30c5-ac56-cead306697f9 | -10.29749 | -57.12994 | 2025-07-10 05:18:00 | NOAA-21 | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 94a1bbe7-98ee-367a-a89d-66c14248cc4e | -11.87709 | -58.7199 | 2025-07-10 05:18:00 | NOAA-21 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 5335c54d-f229-3d14-be90-b56690827627 | -7.95401 | -49.65181 | 2025-07-10 05:18:00 | NOAA-21 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 54803613-7cb5-30b3-8e48-a6e2800cc537 | -11.36516 | -48.70444 | 2025-07-10 05:18:00 | NOAA-21 | ALIANÇA DO TOCANTINS | TOCANTINS | Brasil | 1700350 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 8bc82bb3-0eb7-3b45-8ff9-320453e9d935 | -9.02163 | -61.23409 | 2025-07-10 05:18:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 1ccdbe2e-9a57-3344-8b5a-f6189ef216ce | -13.28845 | -49.15862 | 2025-07-10 05:18:00 | NOAA-21 | PORANGATU | GOIÁS | Brasil | 5218003 | 52 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 68dd4a81-bf67-3499-b2bc-b3db79c99ed4 | -10.57541 | -49.14999 | 2025-07-10 05:18:00 | NOAA-21 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 20.1 |
| 1a41d10a-6f71-3623-9c0a-aa241ed6bc79 | -9.02222 | -61.23045 | 2025-07-10 05:18:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 33f7aea6-70e7-304e-b50f-f1adcc39cac0 | -8.86419 | -47.94991 | 2025-07-10 05:18:00 | NOAA-21 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| fad8db2e-6161-3434-a6f3-ce7ad5c3be09 | -8.51797 | -54.7704 | 2025-07-10 05:18:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 138b6327-a0af-3e9f-892e-2175cd3bba66 | -7.91649 | -61.54668 | 2025-07-10 05:18:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 981a038a-b36f-3207-a881-c41e02d5ced1 | -10.57167 | -49.13098 | 2025-07-10 05:18:00 | NOAA-21 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 20440aa0-85ef-39af-b5b9-e8d8f45a4be7 | -13.16141 | -47.28656 | 2025-07-10 05:18:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 679bc1e5-b3c3-36d9-8b63-a30b1d1ae98d | -10.5722 | -49.12666 | 2025-07-10 05:18:00 | NOAA-21 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 6.0 |
| e355a313-ac92-36e3-adae-40394e810536 | -13.1626 | -47.2755 | 2025-07-10 05:18:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 32cd7000-98f2-3308-a46b-f7ab2f2a3817 | -13.38274 | -47.88186 | 2025-07-10 05:18:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 6d67c05a-d2ce-3f4d-a069-28f993703acb | -13.16193 | -47.28502 | 2025-07-10 05:18:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 6.4 |
| fe4bf019-332b-3a8b-929e-e25a0dddbb6b | -11.87765 | -58.71621 | 2025-07-10 05:18:00 | NOAA-21 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 0e08def5-0d89-30eb-bcdd-4b649070fbd7 | -10.57002 | -49.14454 | 2025-07-10 05:18:00 | NOAA-21 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 22.1 |


[Clique aqui para ver as próximas entradas](README24.md)
