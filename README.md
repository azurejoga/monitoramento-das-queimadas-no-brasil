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

## Dados Diários - Página 1

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 52b43355-88a0-3d97-a6ba-b75e21f0b154 | -3.7255 | -41.6748 | 2024-11-15 00:00:00 | GOES-16 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 96.3 |
| 124227c8-e5c7-3437-9633-acee095d1f20 | -15.3025 | -56.5268 | 2024-11-15 00:00:00 | GOES-16 | JANGADA | MATO GROSSO | Brasil | 5104906 | 51 | 33 | nan | nan | nan | Cerrado | 74.6 |
| 97e7a24d-3102-3b71-bc87-49e9eb8c3713 | -2.3233 | -46.8786 | 2024-11-15 00:00:00 | GOES-16 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 126.0 |
| 5e4bca11-d133-3a5f-b948-e308d1e83ebb | -3.7068 | -41.6758 | 2024-11-15 00:00:00 | GOES-16 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 101.7 |
| ea247210-5857-3ab5-89a2-90725784fcb1 | -3.0882 | -45.791 | 2024-11-15 00:00:00 | GOES-16 | ARAGUANÃ | MARANHÃO | Brasil | 2100873 | 21 | 33 | nan | nan | nan | Amazônia | 114.6 |
| 016b8187-14ae-3b2f-b5b2-7d1a7a829bec | -2.3419 | -46.8781 | 2024-11-15 00:00:00 | GOES-16 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 88.0 |
| 20053385-db60-33ee-85df-3490ec7b94cb | -2.8535 | -53.9714 | 2024-11-15 00:00:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 68.1 |
| 3e8084f1-b2ec-3bcb-ac77-18972dcc1645 | -17.2347 | -57.4721 | 2024-11-15 00:00:00 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 88.1 |
| 1a96cfdc-bae4-3914-8b2b-27b39aad0d89 | 1.0765 | -51.1441 | 2024-11-15 00:00:00 | GOES-16 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 90.4 |
| d915cd70-89fd-32d9-a8f3-8c2ed3de52e2 | -17.5879 | -57.4917 | 2024-11-15 00:00:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 61.8 |
| 4ae51509-f1c5-3282-a340-b4c0d42db058 | -2.3408 | -47.2069 | 2024-11-15 00:00:00 | GOES-16 | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | 63.4 |
| 62a36646-25fe-3cd7-a83c-39e7e8ee12a7 | -2.3407 | -47.2288 | 2024-11-15 00:00:00 | GOES-16 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 61.0 |
| eb3c3d3f-5abc-3199-8361-b3c591989ffa | -1.9198 | -45.4683 | 2024-11-15 00:00:00 | GOES-16 | TURIAÇU | MARANHÃO | Brasil | 2112407 | 21 | 33 | nan | nan | nan | Amazônia | 97.2 |
| ddc91815-8ca8-32d9-83ac-baae78146616 | -1.9198 | -45.4459 | 2024-11-15 00:00:00 | GOES-16 | TURIAÇU | MARANHÃO | Brasil | 2112407 | 21 | 33 | nan | nan | nan | Amazônia | 125.2 |
| 59b69161-da55-3cdf-b227-871497dec025 | -2.8534 | -53.9915 | 2024-11-15 00:00:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 54.3 |
| f5d25288-ffe8-3f01-a553-c575d1c334df | -1.9013 | -45.4463 | 2024-11-15 00:00:00 | GOES-16 | TURIAÇU | MARANHÃO | Brasil | 2112407 | 21 | 33 | nan | nan | nan | Amazônia | 108.8 |
| 99be99e4-a44a-320c-a691-ee51bac28a9e | -17.7048 | -57.5597 | 2024-11-15 00:00:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 57.5 |
| 95fa617f-7656-32b4-9a9e-69016185b85a | -17.274 | -57.4675 | 2024-11-15 00:00:00 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 64.8 |
| 2246e197-a2c4-386c-8a28-79069bb0de43 | -3.0883 | -45.7687 | 2024-11-15 00:00:00 | GOES-16 | ARAGUANÃ | MARANHÃO | Brasil | 2100873 | 21 | 33 | nan | nan | nan | Amazônia | 126.1 |
| a9e21699-2e09-3078-b00d-c7dacc912a46 | -17.7052 | -57.5392 | 2024-11-15 00:00:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 59.2 |
| f8cda83f-685f-3a62-8c6c-1be55341c1c5 | -2.641 | -46.1849 | 2024-11-15 00:00:00 | GOES-16 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 92.4 |
| ce654197-6cfb-338a-967b-abcaad8828ae | -17.2543 | -57.4698 | 2024-11-15 00:00:00 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 174.1 |
| 80bd810b-2fe5-3c80-9af6-83968f73ad1b | 1.0764 | -51.1648 | 2024-11-15 00:00:00 | GOES-16 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 103.1 |
| 0cb1020e-b51e-38ee-a418-5a8aae2c2582 | -2.9825 | -53.8677 | 2024-11-15 00:00:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 57.4 |
| 861ab603-9d05-375c-8ade-205c6d04f155 | -2.6596 | -46.1843 | 2024-11-15 00:00:00 | GOES-16 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 122.0 |
| 019b276c-d304-34b8-8b76-9365096cd436 | -17.235 | -57.4516 | 2024-11-15 00:00:00 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 99.9 |
| 447f317a-6edb-33a6-aafa-acc1361dfab5 | -3.8054 | -43.9002 | 2024-11-15 00:00:00 | GOES-16 | VARGEM GRANDE | MARANHÃO | Brasil | 2112704 | 21 | 33 | nan | nan | nan | Cerrado | 79.5 |
| 5a3e9c6e-9b1d-3198-8ab7-5b1f24aacbaf | -3.7066 | -41.6997 | 2024-11-15 00:00:00 | GOES-16 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 145.9 |
| 8a0379f3-73c5-3f68-bda1-3a1e59f0a0f5 | -1.9161 | -46.7567 | 2024-11-15 00:00:00 | GOES-16 | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 104.0 |
| 8fffd511-7c31-30ac-a595-d9555067e673 | -1.9012 | -45.4687 | 2024-11-15 00:00:00 | GOES-16 | TURIAÇU | MARANHÃO | Brasil | 2112407 | 21 | 33 | nan | nan | nan | Amazônia | 88.6 |
| 451b8e44-5e46-3262-8cd2-f4c43f6d5339 | -3.7254 | -41.6987 | 2024-11-15 00:00:00 | GOES-16 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 138.4 |
| ef719ff1-e867-3ecf-8bd0-58fb34835d88 | -17.5882 | -57.4711 | 2024-11-15 00:00:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 104.6 |
| 08429752-0a90-3bfc-bb9a-c3fcc668b721 | -17.5885 | -57.4506 | 2024-11-15 00:00:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 56.1 |
| c48e0029-100d-3634-a978-59d138439703 | -17.2547 | -57.4493 | 2024-11-15 00:00:00 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 141.2 |
| 9457055d-962e-35ec-a852-b610f8e1ab6a | -17.6079 | -57.4688 | 2024-11-15 00:00:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 60.7 |
| 052ffcfb-9215-330a-8799-c888008650e6 | -2.9825 | -53.8476 | 2024-11-15 00:00:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 53.8 |
| d6e9f3af-9b77-389b-b139-68251b06f42a | -3.7867 | -43.9011 | 2024-11-15 00:00:00 | GOES-16 | VARGEM GRANDE | MARANHÃO | Brasil | 2112704 | 21 | 33 | nan | nan | nan | Cerrado | 106.1 |
| 6088ad8c-99a6-3486-a147-dcc5e3aef7ae | -1.9161 | -46.7787 | 2024-11-15 00:00:00 | GOES-16 | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 112.7 |
| 15dbdaab-eafb-3d57-ae3c-e140f137c607 | -2.3234 | -46.8567 | 2024-11-15 00:00:00 | GOES-16 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 103.1 |
| c5d2efba-283c-3df5-8118-bb49a1db4ec6 | -17.57 | -57.57 | 2024-11-15 00:00:00 | MSG-03 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| b8367665-c11a-37ab-9e33-99bfb5787143 | -3.3029 | -46.059601 | 2024-11-15 00:08:00 | METOP-B | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 258066de-5ee3-31d4-b1ab-1a39494c1f09 | -2.1199 | -46.4799 | 2024-11-15 00:08:00 | METOP-B | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f393b440-75cb-3e87-9312-6e44e77b136c | -6.162 | -41.146099 | 2024-11-15 00:08:00 | METOP-B | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 2244fe59-1692-3c85-b1d5-1bbb26b03d13 | -2.6429 | -46.147999 | 2024-11-15 00:08:00 | METOP-B | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 1560b68d-73c7-3e8f-bbe4-4295f31bafc5 | -10.72 | -40.5168 | 2024-11-15 00:08:00 | METOP-B | MIRANGABA | BAHIA | Brasil | 2921401 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| 841651bb-aacd-3248-9f4b-d085ffa8e5ca | -3.5896 | -47.339298 | 2024-11-15 00:08:00 | METOP-B | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 73fcb001-f576-32b6-ba07-440537ef729d | -3.8809 | -43.1492 | 2024-11-15 00:08:00 | METOP-B | BURITI | MARANHÃO | Brasil | 2102200 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 7b37f939-4fc2-354b-b0d5-cdea7fbbb0d1 | -3.1744 | -45.077499 | 2024-11-15 00:08:00 | METOP-B | VIANA | MARANHÃO | Brasil | 2112803 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| c79fca0b-fe27-3e24-93cb-f8e219f12725 | -2.1215 | -46.486801 | 2024-11-15 00:08:00 | METOP-B | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ffdf74f4-a3e4-384d-aa70-b867755f0712 | -2.0813 | -46.5826 | 2024-11-15 00:08:00 | METOP-B | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 45cf57a5-8194-3406-a0d2-c559828224ba | -2.2875 | -47.914101 | 2024-11-15 00:08:00 | METOP-B | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3f26b990-d2b5-380e-8af6-74d3c755eb5d | -2.8569 | -45.405899 | 2024-11-15 00:08:00 | METOP-B | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 45b1be82-24a9-398d-a874-b8888ce9b7d5 | -1.7066 | -46.154099 | 2024-11-15 00:08:00 | METOP-B | BOA VISTA DO GURUPI | MARANHÃO | Brasil | 2101970 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 6114d1d6-6454-37b3-a1ec-888a9a27326d | -2.6444 | -46.1548 | 2024-11-15 00:08:00 | METOP-B | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| c8d1e703-6c15-3fde-8a0e-b3a357a1ec71 | -1.9236 | -45.562801 | 2024-11-15 00:08:00 | METOP-B | TURIAÇU | MARANHÃO | Brasil | 2112407 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| c61e28da-2cfd-3813-8221-a78d1e74efff | -6.1522 | -41.148399 | 2024-11-15 00:08:00 | METOP-B | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 3f03485d-e7df-365d-bfb0-2ac57fc21166 | -2.618 | -46.174999 | 2024-11-15 00:08:00 | METOP-B | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 829ff863-b8d4-3901-8342-2dacd50bbcd7 | -1.9058 | -45.438 | 2024-11-15 00:08:00 | METOP-B | TURIAÇU | MARANHÃO | Brasil | 2112407 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 7e7f21e5-f52c-342c-b4b9-2f9d06ab7b09 | -2.6408 | -46.184399 | 2024-11-15 00:08:00 | METOP-B | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 7f62340f-daff-387b-99dd-078a84a7732b | -3.8791 | -43.141701 | 2024-11-15 00:08:00 | METOP-B | BURITI | MARANHÃO | Brasil | 2102200 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| f00753a0-88ee-396d-9eb8-740476f39d80 | -2.6506 | -46.182201 | 2024-11-15 00:08:00 | METOP-B | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 7de41ee0-470a-37aa-bba1-cdd5a548e9f0 | -2.9047 | -46.855099 | 2024-11-15 00:08:00 | METOP-B | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 73c9a622-9abe-364a-8edc-665cb06ff892 | -4.2138 | -45.620602 | 2024-11-15 00:08:00 | METOP-B | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 4a812290-d465-3f57-9f7d-3768a3a92e6d | -2.6588 | -46.173199 | 2024-11-15 00:08:00 | METOP-B | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 58f67e84-4855-312a-9714-b0fc41e7b206 | -2.8554 | -45.399101 | 2024-11-15 00:08:00 | METOP-B | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 250e0dff-600d-3db7-b92c-910357d09efc | -1.9073 | -45.444801 | 2024-11-15 00:08:00 | METOP-B | TURIAÇU | MARANHÃO | Brasil | 2112407 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| c192d6f1-49ea-3966-8017-2c9c7f36881d | -2.6521 | -46.189098 | 2024-11-15 00:08:00 | METOP-B | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 16493716-6a5a-3199-87bf-8fa153c911f3 | -2.6573 | -46.166302 | 2024-11-15 00:08:00 | METOP-B | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 0c0af0c5-9aaf-3024-ad79-42daff5d96fc | -4.2107 | -45.606899 | 2024-11-15 00:08:00 | METOP-B | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 51a6b93e-8cfb-37ca-8f03-92f4c92fcf9d | -2.6392 | -46.177601 | 2024-11-15 00:08:00 | METOP-B | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 3bcd35cd-8777-3fc5-9d69-9afe73360411 | -2.6604 | -46.18 | 2024-11-15 00:08:00 | METOP-B | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 977e3057-f435-3b33-9780-5ae3fedb7fe7 | -3.1677 | -45.458599 | 2024-11-15 00:08:00 | METOP-B | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| c28dab5e-c7ff-37d1-b6e4-b0a39cdbffa7 | -2.6377 | -46.1707 | 2024-11-15 00:08:00 | METOP-B | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| edfc6dae-0f4d-38f2-a20d-7e839be87e3d | -1.9645 | -46.5215 | 2024-11-15 00:08:00 | METOP-B | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 187dfae4-7c1a-3144-acba-c64a2664b2f0 | -6.1542 | -41.1572 | 2024-11-15 00:08:00 | METOP-B | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| a301c874-d04c-3e84-b45f-4ed018246701 | -7.4835 | -35.291 | 2024-11-15 00:08:00 | METOP-B | FERREIROS | PERNAMBUCO | Brasil | 2605509 | 26 | 33 | nan | nan | nan | Mata Atlântica | nan |
| cc6541cd-deec-385b-9d13-e6e0a760e43d | -3.097 | -45.968399 | 2024-11-15 00:08:00 | METOP-B | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 9786a50d-1275-3dd8-aeb2-b1be00b1ba7e | -2.3473 | -47.216599 | 2024-11-15 00:08:00 | METOP-B | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ecb5b432-7ac2-343f-a729-3a6c0a55376f | -3.2422 | -46.523102 | 2024-11-15 00:08:00 | METOP-B | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| b06c3800-c2de-384d-929d-ceea981f9978 | -2.3151 | -45.060001 | 2024-11-15 00:08:00 | METOP-B | PINHEIRO | MARANHÃO | Brasil | 2108603 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 6dd29f0a-d994-3769-ab07-8cd13049780b | -3.2437 | -45.384499 | 2024-11-15 00:08:00 | METOP-B | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 63c8f38b-0ea4-33fe-9c91-746b9030fc1b | -2.1437 | -46.402401 | 2024-11-15 00:08:00 | METOP-B | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 16b9354e-2f17-36bc-a81f-ba4729f6a464 | -4.1947 | -44.256802 | 2024-11-15 00:08:00 | METOP-B | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 557a6f00-d4a3-3ce2-908f-386c5c0c43fe | -6.972 | -38.462101 | 2024-11-15 00:08:00 | METOP-B | CAJAZEIRAS | PARAÍBA | Brasil | 2503704 | 25 | 33 | nan | nan | nan | Caatinga | nan |
| aea03df8-ce78-3313-8309-c0a32c258275 | -1.7001 | -45.805302 | 2024-11-15 00:08:00 | METOP-B | CÂNDIDO MENDES | MARANHÃO | Brasil | 2102606 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| d2d2b082-7ba4-3f72-9c8b-663bda45da4d | -1.8999 | -46.463402 | 2024-11-15 00:08:00 | METOP-B | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 68b17ca1-c436-3b5c-a8d7-86866ee5eb30 | -2.649 | -46.1754 | 2024-11-15 00:08:00 | METOP-B | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 7de78744-f124-3b69-9453-959dd7e2a803 | -2.2982 | -46.447701 | 2024-11-15 00:08:00 | METOP-B | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3a71db9f-83fd-3516-96bf-fff4095c7801 | -2.2868 | -46.443001 | 2024-11-15 00:08:00 | METOP-B | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 01ef6748-455e-363a-9098-2a0bc7a0b570 | -2.3135 | -45.0532 | 2024-11-15 00:08:00 | METOP-B | PINHEIRO | MARANHÃO | Brasil | 2108603 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 1ac696cd-e56d-3749-84e1-0fda1ddefe92 | -2.8493 | -46.653702 | 2024-11-15 00:08:00 | METOP-B | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c8720c06-84ea-388d-b6aa-e5fdd9f22d2d | -4.5126 | -44.068298 | 2024-11-15 00:08:00 | METOP-B | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| f48254b0-dcf3-3811-a1f9-b63711479bd8 | -2.3313 | -46.274399 | 2024-11-15 00:08:00 | METOP-B | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 0e75d3b2-e788-33ed-ac34-b869f3aad575 | -6.6399 | -39.1436 | 2024-11-15 00:08:00 | METOP-B | CEDRO | CEARÁ | Brasil | 2303808 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| 25e69aaa-128e-39fb-bc6f-26a635bc76e7 | -1.93 | -46.276798 | 2024-11-15 00:08:00 | METOP-B | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9166ee9b-3e69-3684-8b98-a8d5152c2d3d | -1.9047 | -46.759701 | 2024-11-15 00:08:00 | METOP-B | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 169dfbb2-8939-3f3e-ab01-690515c21c44 | -4.2123 | -45.613701 | 2024-11-15 00:08:00 | METOP-B | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 15baa353-a469-3b8a-b34a-e5535496819e | -2.3283 | -46.856701 | 2024-11-15 00:08:00 | METOP-B | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| fe5f44ea-e062-3fa1-bedd-7cc14c718fc2 | -4.3705 | -42.991299 | 2024-11-15 00:08:00 | METOP-B | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| e3a5d0f7-808b-3077-add5-38613fee9f28 | -2.7146 | -44.776199 | 2024-11-15 00:08:00 | METOP-B | BACURITUBA | MARANHÃO | Brasil | 2101350 | 21 | 33 | nan | nan | nan | Amazônia | nan |


[Clique aqui para ver as próximas entradas](README2.md)
