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

## Dados Diários - Página 39

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 693e05a4-539c-3c3e-824f-6305ec6eaafb | -5.3182 | -43.42242 | 2026-09-22 04:02:00 | NOAA-20 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| c4c1a9d6-701e-3b1c-b622-098e304f093a | -9.61148 | -43.94054 | 2026-09-22 04:02:00 | NOAA-20 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 6be53dcf-315a-3f7b-854d-77b6f7f674d6 | -7.41199 | -42.64812 | 2026-09-22 04:02:00 | NOAA-20 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 21093447-38d1-36e8-ba9e-63571e15c84e | -11.42303 | -47.35825 | 2026-09-22 04:02:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 8.7 |
| 3f27c790-35e9-3857-8fec-d0362d834dae | -9.81097 | -48.30289 | 2026-09-22 04:02:00 | NOAA-20 | LAJEADO | TOCANTINS | Brasil | 1712009 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 075dfdd8-953d-3dc2-ae8c-9b42f6805ab1 | -7.59387 | -43.42913 | 2026-09-22 04:02:00 | NOAA-20 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 5c7398f1-c7a6-3cec-9a3b-4059b0354e2b | -7.35264 | -45.35005 | 2026-09-22 04:02:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 786be1dc-136c-35cd-9ab8-596232fe30d6 | -10.86908 | -50.16247 | 2026-09-22 04:02:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 8dc1039d-8a65-375a-87e3-90b6f2406126 | -11.41369 | -46.78602 | 2026-09-22 04:02:00 | NOAA-20 | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 9fe1fa1d-11b4-35c8-8147-0058cdce2d9f | -10.84108 | -50.15245 | 2026-09-22 04:02:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 511d6c70-2b62-3858-8622-d8a93314255d | -8.34923 | -50.75253 | 2026-09-22 04:02:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 88f9cfd2-70e1-3558-826d-4b6fdac542b5 | -8.79275 | -44.28062 | 2026-09-22 04:02:00 | NOAA-20 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 3.3 |
| f319cbf2-b041-34ae-b70a-9e2039eb2f86 | -11.3437 | -43.37158 | 2026-09-22 04:02:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| cfdc712b-d834-335d-bd90-1e886c709846 | -6.5731 | -44.15616 | 2026-09-22 04:02:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 5.5 |
| fb609128-25ca-3205-8fe1-14ad7a73f7b7 | -8.79213 | -44.28424 | 2026-09-22 04:02:00 | NOAA-20 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 93de82d5-63ee-3ac9-b58b-9179d6932993 | -8.32095 | -44.75147 | 2026-09-22 04:02:00 | NOAA-20 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 2c15e8b4-9582-3d01-b291-fb7690192231 | -11.15314 | -51.1108 | 2026-09-22 04:02:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 40a0f00b-32d6-3dea-a093-d4ad6ec5a240 | -6.78088 | -48.66962 | 2026-09-22 04:02:00 | NOAA-20 | ARAGOMINAS | TOCANTINS | Brasil | 1701309 | 17 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 1b053059-173a-33de-86b5-c151a8c62c97 | -12.56668 | -45.97913 | 2026-09-22 04:02:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 1ea4d94f-1573-3fda-9181-4bd59de7c31c | -8.32101 | -44.75044 | 2026-09-22 04:02:00 | NOAA-20 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 9b9b5db6-81f2-34d8-8098-08b4473251a4 | -9.53739 | -45.38966 | 2026-09-22 04:02:00 | NOAA-20 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 694060b7-755b-3d59-b6f2-6d8f3e51b26b | -9.88535 | -48.45508 | 2026-09-22 04:02:00 | NOAA-20 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 68b61328-6a92-3442-a604-41da6f35a25f | -7.42195 | -49.84118 | 2026-09-22 04:02:00 | NOAA-20 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 66379b6d-119b-3841-b003-b5191c95e016 | -11.40543 | -46.77933 | 2026-09-22 04:02:00 | NOAA-20 | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 903df0e0-12ac-3ce0-bb74-5e523477f2eb | -11.44058 | -47.34303 | 2026-09-22 04:02:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 12.2 |
| de2af561-29b1-34fd-b25b-9c352168d853 | -8.81656 | -45.37143 | 2026-09-22 04:02:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 6258ec09-07cb-3395-be76-bd358c8c1f7e | -7.94455 | -45.64484 | 2026-09-22 04:02:00 | NOAA-20 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 295f9281-da71-3eaa-b1d9-83ee3a291da8 | -11.67681 | -43.4656 | 2026-09-22 04:02:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| c7e7886c-4201-3d57-8da3-5505c30ae108 | -5.38989 | -42.9482 | 2026-09-22 04:02:00 | NOAA-20 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Caatinga | 4.0 |
| bfecff5e-b391-3cdc-82db-bdd57934bf6e | -6.93987 | -42.91705 | 2026-09-22 04:02:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| beceffbc-5a18-3ebd-a249-58a7f04102f8 | -5.60908 | -44.8466 | 2026-09-22 04:02:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 5.2 |
| c53c6192-4f96-34fb-b4dc-d905206130d0 | -11.10209 | -48.31475 | 2026-09-22 04:02:00 | NOAA-20 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| fda0d4d8-d141-318f-a69a-8b9af68182bc | -6.58333 | -44.14614 | 2026-09-22 04:02:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| ebf5d80b-642b-3ae7-b0fb-473e98a464f0 | -6.57917 | -44.1454 | 2026-09-22 04:02:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| b5902d96-d869-36a5-aa44-91dea5d46d75 | -11.43485 | -47.32328 | 2026-09-22 04:02:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| b1c01570-cb37-3e4f-8353-a2b9b4f42b70 | -12.02421 | -47.80752 | 2026-09-22 04:02:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 23.2 |
| 67877741-1279-356f-a641-94f801334e6c | -7.82775 | -44.97211 | 2026-09-22 04:02:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 456b295b-9e58-36da-aa8c-a25e8d1077b5 | -8.81223 | -45.37054 | 2026-09-22 04:02:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 70791032-c6cd-33b7-97c3-945e59b755c6 | -5.78535 | -43.76933 | 2026-09-22 04:02:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| e06c492c-f989-340f-abee-d766348756d0 | -12.19732 | -47.04171 | 2026-09-22 04:02:00 | NOAA-20 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |
| c36df36e-9b2b-33e6-b26a-931608cb5b5f | -8.91554 | -50.90498 | 2026-09-22 04:02:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 2449af75-6611-39a5-99a0-2f1447be0ac5 | -7.41939 | -49.85481 | 2026-09-22 04:02:00 | NOAA-20 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| a864b199-e054-376d-8700-6c378bf55490 | -11.32408 | -51.36845 | 2026-09-22 04:02:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 369b143a-21e7-3425-81d5-817985d29c64 | -10.25074 | -45.49103 | 2026-09-22 04:02:00 | NOAA-20 | SÃO GONÇALO DO GURGUÉIA | PIAUÍ | Brasil | 2209757 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 9ad2d783-4939-37cd-86cf-d6fd3ea29307 | -12.02811 | -47.8134 | 2026-09-22 04:02:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 23.2 |
| da7dda37-04df-3e33-b9df-c8bbf93f58df | -11.32529 | -51.35677 | 2026-09-22 04:02:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 4.5 |
| e435cf8f-e13b-3567-8f11-5bc695c727c0 | -11.09356 | -48.33199 | 2026-09-22 04:02:00 | NOAA-20 | IPUEIRAS | TOCANTINS | Brasil | 1709807 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| bd121883-577b-38c6-8edf-577bbec36d8b | -10.84684 | -50.15364 | 2026-09-22 04:02:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 511f3c46-303d-3346-8719-8cfad49d153a | -11.43973 | -47.34771 | 2026-09-22 04:02:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 12.2 |
| f7582bb4-02cc-39b5-ab8a-92e35e346e7a | -5.85263 | -49.7848 | 2026-09-22 04:02:00 | NOAA-20 | CURIONÓPOLIS | PARÁ | Brasil | 1502772 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| bdbedcc3-50da-3eb4-bfbe-ec1ded343459 | -11.41498 | -47.3485 | 2026-09-22 04:02:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 87251f75-4ba8-3f99-afc0-e5f7ebef8349 | -8.33469 | -47.53329 | 2026-09-22 04:02:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ca035bee-da9a-34b8-be80-db21eacb0813 | -6.57727 | -44.15688 | 2026-09-22 04:02:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 5.5 |
| d18dcf23-50be-3eee-a274-d5eb4a7dbd9f | -11.44714 | -47.3363 | 2026-09-22 04:02:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 6d0673f0-1cdc-3a71-a17b-7fb4b9f2315a | -6.54783 | -45.57101 | 2026-09-22 04:02:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 7d40ac6a-ea9d-3ec6-b152-39887aecee6e | -9.89687 | -48.48112 | 2026-09-22 04:02:00 | NOAA-20 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| ffeb1aae-8ecd-3d52-a091-527ef2884b0f | -12.13712 | -47.3918 | 2026-09-22 04:02:00 | NOAA-20 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| f3cdc257-c96a-3e44-b966-2fed9580561c | -5.78264 | -43.76894 | 2026-09-22 04:02:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 105d3fb6-f611-313f-951a-ff184b4932a4 | -5.76022 | -45.08086 | 2026-09-22 04:02:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| a9e8d52e-b50a-387e-88dc-200a5f94ed4f | -6.47656 | -42.76917 | 2026-09-22 04:02:00 | NOAA-20 | AMARANTE | PIAUÍ | Brasil | 2200509 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 899b98c0-46bb-38bf-81b4-90ae370734ea | -5.83057 | -43.85318 | 2026-09-22 04:02:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| d12e62d2-d7d4-3bfa-b7b5-caa1e76bfdad | -8.13613 | -46.82775 | 2026-09-22 04:02:00 | NOAA-20 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| e1b0bbd6-faf5-3df4-9509-d8194433f75f | -9.9759 | -50.25785 | 2026-09-22 04:02:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 2a237dba-e576-3b4e-ab8a-25f01a481c62 | -6.97647 | -42.58363 | 2026-09-22 04:02:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 74c6d23b-c848-38af-8f77-486d285f0f25 | -7.54418 | -47.32407 | 2026-09-22 04:02:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| eee878ec-0d17-3b14-8afe-6959f0ccc3ce | -9.72379 | -47.77122 | 2026-09-22 04:02:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 9f6983e5-b2e4-39c8-89b0-91ea9c0ab026 | -5.75494 | -45.08474 | 2026-09-22 04:02:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 37.6 |
| d9bfd954-9507-3bad-b556-722265143b71 | -10.90585 | -47.38069 | 2026-09-22 04:02:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 941f9c27-029c-35a7-a71a-e8fd538c277a | -7.08053 | -42.07536 | 2026-09-22 04:02:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| d27d7bfb-1966-3c3b-ba31-b937a0f38f10 | -11.15002 | -42.83604 | 2026-09-22 04:02:00 | NOAA-20 | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 1.7 |
| bba8ca5c-d375-3c8e-a645-c34e7263c44c | -12.5653 | -45.96209 | 2026-09-22 04:02:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 13.7 |
| 4d56d553-c3f4-3c34-85e1-7a3d2c05ebeb | -5.75793 | -45.09458 | 2026-09-22 04:02:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 9.9 |
| 2d3e5d4d-9190-3697-ae2f-b41fffb87761 | -9.72485 | -47.76537 | 2026-09-22 04:02:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 3bb4b9d7-925e-370b-b442-078413c95451 | -7.42113 | -49.84557 | 2026-09-22 04:02:00 | NOAA-20 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 46a7b5fd-6167-3339-b5c3-7208a57f3bda | -10.3793 | -48.91268 | 2026-09-22 04:02:00 | NOAA-20 | PUGMIL | TOCANTINS | Brasil | 1718451 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| e98aa100-89f1-3ecc-874f-ed6ec61a1aeb | -10.1239 | -45.5459 | 2026-09-22 04:02:00 | NOAA-20 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 247b92ef-9c84-35ad-a032-44cbb5d87fa0 | -6.97773 | -42.13091 | 2026-09-22 04:02:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| d53f9717-df7a-3f55-b6b0-ac26f12193e5 | -8.7915 | -44.28788 | 2026-09-22 04:02:00 | NOAA-20 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 834cfe46-0457-3fb5-ac07-1e5345208af4 | -8.48338 | -44.74104 | 2026-09-22 04:02:00 | NOAA-20 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 70c7dd7b-88fa-31c4-bdc0-b7adb1433b69 | -11.14366 | -42.84477 | 2026-09-22 04:02:00 | NOAA-20 | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 2.4 |
| cfda234c-8f6f-384b-849f-27d8b6c9e33f | -6.61559 | -45.8975 | 2026-09-22 04:02:00 | NOAA-20 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 876ba0e6-dc2d-3788-9f28-bb44a14aa1eb | -19.40785 | -46.41241 | 2026-09-22 04:04:00 | NOAA-20 | IBIÁ | MINAS GERAIS | Brasil | 3129509 | 31 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 82ff6b5b-e5d8-3e5c-989d-5800d59793bf | -11.31374 | -54.05255 | 2026-09-22 04:04:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 9.2 |
| abaa21c7-1b1b-3c11-b65c-529e8581e01c | -15.26367 | -47.59912 | 2026-09-22 04:04:00 | NOAA-20 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 8e82d25e-f22d-302b-b682-9619c528feba | -13.92824 | -48.57493 | 2026-09-22 04:04:00 | NOAA-20 | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 7a1d386e-cab8-3577-8e64-957745ca8019 | -16.04802 | -49.98428 | 2026-09-22 04:04:00 | NOAA-20 | ITABERAÍ | GOIÁS | Brasil | 5210406 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e3cfc72e-09ed-3a10-a223-910dc06f6379 | -14.91642 | -45.14469 | 2026-09-22 04:04:00 | NOAA-20 | BONITO DE MINAS | MINAS GERAIS | Brasil | 3108255 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| ea1daf72-0d1c-3eac-abbe-ea2c4eb4f3e9 | -15.44389 | -48.44035 | 2026-09-22 04:04:00 | NOAA-20 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 4618b028-998e-3e83-8f9d-e333ab2336d5 | -18.88262 | -46.8467 | 2026-09-22 04:04:00 | NOAA-20 | PATROCÍNIO | MINAS GERAIS | Brasil | 3148103 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| e81511d1-a67d-33ba-b35b-25bff707d116 | -11.3209 | -54.05415 | 2026-09-22 04:04:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 9.2 |
| d3d6c43d-ea88-3474-a413-5bd066f8ff82 | -16.19557 | -42.80944 | 2026-09-22 04:04:00 | NOAA-20 | GRÃO MOGOL | MINAS GERAIS | Brasil | 3127800 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| e60de5fb-8a23-3f9d-bd04-a77383c43110 | -17.35758 | -41.19556 | 2026-09-22 04:04:00 | NOAA-20 | NOVO ORIENTE DE MINAS | MINAS GERAIS | Brasil | 3145356 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| 3bb1d683-48c0-3380-929d-483e7790073f | -12.39223 | -47.0596 | 2026-09-22 04:04:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 7.7 |
| eb7649bf-c119-3b7b-ae8b-8eec4aaaaf17 | -12.98974 | -44.80315 | 2026-09-22 04:04:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 8267f063-fc86-36aa-9011-779fa87c711a | -15.35573 | -48.10545 | 2026-09-22 04:04:00 | NOAA-20 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 9112691f-d8f4-33a5-a50c-26c4d6ecf292 | -18.73785 | -46.94739 | 2026-09-22 04:04:00 | NOAA-20 | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 23.3 |
| d4dca21d-0edc-3606-ac98-600c04548f20 | -15.23578 | -42.77396 | 2026-09-22 04:04:00 | NOAA-20 | SANTO ANTÔNIO DO RETIRO | MINAS GERAIS | Brasil | 3160454 | 31 | 33 | nan | nan | nan | Cerrado | 4.8 |
| baf4389c-2ce4-33c2-89be-43120db770bd | -15.98891 | -43.27873 | 2026-09-22 04:04:00 | NOAA-20 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 13.7 |
| 0d99324c-fd79-33b7-9f8a-bec689ee0bda | -15.88048 | -41.3803 | 2026-09-22 04:04:00 | NOAA-20 | CACHOEIRA DE PAJEÚ | MINAS GERAIS | Brasil | 3102704 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 6138f93c-3b58-3a2a-a2fc-5ef9434f6b3b | -13.8597 | -51.84635 | 2026-09-22 04:04:00 | NOAA-20 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 8.7 |


[Clique aqui para ver as próximas entradas](README40.md)
