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

## Dados Diários - Página 2

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| be805db4-baab-31df-9c12-4e2d9bfd5139 | -7.2405 | -43.0899 | 2025-05-30 01:00:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 68.8 |
| fad02e6c-f726-3e01-96f4-66219deb22bb | -11.1462 | -53.937901 | 2025-05-30 01:02:00 | METOP-B | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| f008a866-19d4-31f9-b21b-f09a88fd617e | -13.0914 | -52.041698 | 2025-05-30 01:02:00 | METOP-B | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| c09bd781-298b-393a-a04f-07e21acd73b7 | -12.0077 | -49.518902 | 2025-05-30 01:02:00 | METOP-B | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 8af8c003-349b-3f17-bd56-3e20259e86b0 | -11.4563 | -49.102501 | 2025-05-30 01:02:00 | METOP-B | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| b38ad552-ac19-398b-9ce0-578c0d3a7e3f | -11.3 | -53.9762 | 2025-05-30 01:02:00 | METOP-B | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| c5cc9bc8-f659-3374-b4a1-677231841921 | -11.9096 | -54.408798 | 2025-05-30 01:02:00 | METOP-B | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 87836486-3a03-39fe-a9c5-24ab50b55b9b | -12.0174 | -49.5163 | 2025-05-30 01:02:00 | METOP-B | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 46c2ba8c-3f92-30b6-985d-3d5037961de4 | -11.9118 | -54.418301 | 2025-05-30 01:02:00 | METOP-B | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 7b722937-8ba5-3827-9651-d9cc16c9ca23 | -13.1014 | -52.291302 | 2025-05-30 01:02:00 | METOP-B | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 6ecd01a4-baf5-3c86-b862-7981036c655a | -12.0127 | -49.5383 | 2025-05-30 01:02:00 | METOP-B | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 69156b72-286a-3c1d-8599-a4af80fe6043 | -13.0984 | -52.278999 | 2025-05-30 01:02:00 | METOP-B | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 28613259-7b08-30a1-8164-4d16aa0f01ab | -7.2405 | -43.0899 | 2025-05-30 01:10:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 73.2 |
| 57e58a45-6eb8-3f78-acf9-ccb62dbef00e | -7.2405 | -43.0899 | 2025-05-30 01:20:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 64.0 |
| 09741f65-16dc-33db-9542-2aa6dc572a0f | -7.2405 | -43.0899 | 2025-05-30 01:30:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 67.8 |
| edc761e6-50d0-3108-8462-7b33b35dd219 | -13.09849 | -52.28147 | 2025-05-30 01:34:00 | TERRA_M-M | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 25.3 |
| 4d0dc717-169b-33ad-8929-4558171ecd7e | -11.2943 | -53.98118 | 2025-05-30 01:37:00 | TERRA_M-M | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 16.7 |
| 85a1c57f-2e62-3d5b-bb79-a9821a46d718 | -10.29418 | -57.1422 | 2025-05-30 01:37:00 | TERRA_M-M | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 15.9 |
| 0cb04512-6286-3857-a5e1-14825652e100 | -4.98286 | -38.59772 | 2025-05-30 03:04:00 | NOAA-21 | IBICUITINGA | CEARÁ | Brasil | 2305332 | 23 | 33 | nan | nan | nan | Caatinga | 3.8 |
| 280a7e89-7d34-3c0c-8a6e-7aed58bc7e57 | -4.9829 | -38.6016 | 2025-05-30 03:04:00 | NOAA-21 | IBICUITINGA | CEARÁ | Brasil | 2305332 | 23 | 33 | nan | nan | nan | Caatinga | 2.9 |
| bb19adb6-84a7-3124-9f4d-51a142932914 | -4.89183 | -37.52593 | 2025-05-30 03:04:00 | NOAA-21 | ARACATI | CEARÁ | Brasil | 2301109 | 23 | 33 | nan | nan | nan | Caatinga | 3.3 |
| 63fd45ec-4f7c-3ae5-897c-4a69b08c4e0c | -5.07201 | -37.7159 | 2025-05-30 03:04:00 | NOAA-21 | BARAÚNA | RIO GRANDE DO NORTE | Brasil | 2401453 | 24 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 0bf677df-da60-3de3-9629-5f0bdcdc24e8 | -9.49957 | -40.30496 | 2025-05-30 03:06:00 | NOAA-21 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 7.6 |
| 506f6b1c-19be-3a8a-a83e-528c6df38b1a | -9.39829 | -40.37234 | 2025-05-30 03:06:00 | NOAA-21 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 6.3 |
| a06c030b-fbec-3757-9b32-b6e4b63d04e5 | -9.49723 | -40.30463 | 2025-05-30 03:06:00 | NOAA-21 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 8.2 |
| a2e41053-8cbe-387f-9fea-611b0c2d7555 | -9.39971 | -40.36527 | 2025-05-30 03:06:00 | NOAA-21 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 4.5 |
| 265f4f85-baab-366c-84f4-eb1839e503c5 | -13.5261 | -43.6797 | 2025-05-30 03:10:00 | GOES-19 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 59.0 |
| 4bf43bc1-5b20-331a-985a-d0b7e8da2ad6 | -13.5261 | -43.6797 | 2025-05-30 03:20:00 | GOES-19 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 66.6 |
| 6cc8c801-c545-30e4-b8c3-46a6381987bc | -13.5456 | -43.6762 | 2025-05-30 03:30:00 | GOES-19 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 82.4 |
| 1dbb4828-12b1-331a-b423-a8bf0802aa8c | -4.98071 | -38.59713 | 2025-05-30 03:30:00 | NPP-375D | IBICUITINGA | CEARÁ | Brasil | 2305332 | 23 | 33 | nan | nan | nan | Caatinga | 2.0 |
| b8265fad-e304-3f8f-8519-39b7a42b8753 | -5.30269 | -43.06857 | 2025-05-30 03:30:00 | NPP-375D | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 6e9ffbfd-7d60-3ae5-b62c-ccc88616741a | -5.2136 | -43.31921 | 2025-05-30 03:30:00 | NPP-375D | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 8dacbd29-27d7-3c0f-9252-9ac6d511b312 | -5.21448 | -43.31434 | 2025-05-30 03:30:00 | NPP-375D | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 564af04a-8c53-391d-8499-78c18f9369cb | -4.89539 | -37.52733 | 2025-05-30 03:30:00 | NPP-375D | ARACATI | CEARÁ | Brasil | 2301109 | 23 | 33 | nan | nan | nan | Caatinga | 6.2 |
| 29bf4d5b-8450-3288-b3f4-d76687474823 | -5.20909 | -43.30854 | 2025-05-30 03:30:00 | NPP-375D | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 0eb37216-0f66-3822-aa28-1686022ff184 | -3.95672 | -41.4798 | 2025-05-30 03:30:00 | NPP-375D | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 2a3d6b2a-5fa1-3a06-81dd-3785f40afa7c | -5.30188 | -43.07319 | 2025-05-30 03:30:00 | NPP-375D | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 9616fdc5-56c4-394d-9614-a4eff682e9b1 | -3.96238 | -41.48075 | 2025-05-30 03:30:00 | NPP-375D | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 7eba93eb-1a07-33fb-ac8b-998d5393135c | -5.20997 | -43.30362 | 2025-05-30 03:30:00 | NPP-375D | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 46b163b1-3685-368d-9d9c-5fe36436616c | -4.97993 | -38.60179 | 2025-05-30 03:30:00 | NPP-375D | IBICUITINGA | CEARÁ | Brasil | 2305332 | 23 | 33 | nan | nan | nan | Caatinga | 2.0 |
| d8d8fade-a223-3a12-8a6f-98d8aaad4f07 | -5.50843 | -35.59813 | 2025-05-30 03:30:00 | NPP-375D | TAIPU | RIO GRANDE DO NORTE | Brasil | 2413904 | 24 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 836dd7c2-7c47-3e79-ad06-d944f54ab323 | -5.21536 | -43.30943 | 2025-05-30 03:30:00 | NPP-375D | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 609b0efb-9725-3485-8442-ac265963d5f1 | -5.20821 | -43.31345 | 2025-05-30 03:30:00 | NPP-375D | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 56890032-44b3-3a65-a512-de38caff67de | -12.26331 | -44.60422 | 2025-05-30 03:32:00 | NPP-375D | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 9795a5cf-3391-382d-9904-b4d978cd8c1b | -11.69088 | -46.21077 | 2025-05-30 03:32:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 7d6da9de-48ce-33d4-bf80-caddd48f3d91 | -7.53922 | -43.32545 | 2025-05-30 03:32:00 | NPP-375D | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 79871f38-10ee-3dd6-842c-f685cddfb0fb | -7.61103 | -45.74311 | 2025-05-30 03:32:00 | NPP-375D | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 274db4a9-db76-3adf-9cf8-b47a8c12a293 | -6.24748 | -43.37432 | 2025-05-30 03:32:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e16e7f4b-5b32-3bf1-a305-b8bba821b6de | -7.96208 | -46.17694 | 2025-05-30 03:32:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| b8b0848b-74b8-3a4d-bc9e-632d9594456a | -7.58503 | -45.95078 | 2025-05-30 03:32:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| cd055220-2b06-34ba-8611-d1a50ad42405 | -7.26914 | -44.22748 | 2025-05-30 03:32:00 | NPP-375D | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 9bbec700-975e-3f1c-86d9-97f0bcee82de | -7.61212 | -45.74314 | 2025-05-30 03:32:00 | NPP-375D | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 071293dc-6fbb-3c2e-b5a9-cb69aaacec88 | -7.58614 | -45.95815 | 2025-05-30 03:32:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 9d2a7583-94ec-3187-a30a-f044f22a4a91 | -12.26423 | -44.59964 | 2025-05-30 03:32:00 | NPP-375D | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| dd1b9889-0475-351b-bffb-0cb4cb74c901 | -6.24018 | -43.37161 | 2025-05-30 03:32:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 255e6744-abab-3fa1-a458-4cc64915bd46 | -6.34504 | -43.38493 | 2025-05-30 03:32:00 | NPP-375D | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 0199ffb0-1808-3c7d-9927-6183d578b971 | -8.55082 | -46.42865 | 2025-05-30 03:32:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 96954edb-a8d0-3fff-b94f-1420b32a6282 | -7.62356 | -45.75866 | 2025-05-30 03:32:00 | NPP-375D | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 894375d6-e485-3bdd-a26f-bbcb4a8e3d14 | -9.39714 | -40.36709 | 2025-05-30 03:32:00 | NPP-375D | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 8.6 |
| d3429b4a-900a-32fa-8a96-c7ab6dbe38cf | -7.18198 | -43.10708 | 2025-05-30 03:32:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 3.2 |
| 4a566163-4d98-310a-b26d-e836eb68bfe8 | -9.49664 | -40.30657 | 2025-05-30 03:32:00 | NPP-375D | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 69.3 |
| ab366fb9-5730-3e72-81ac-89f5a91e6461 | -7.33234 | -35.06831 | 2025-05-30 03:32:00 | NPP-375D | PEDRAS DE FOGO | PARAÍBA | Brasil | 2511202 | 25 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 2d053dcb-c6b8-3611-970d-61f5ccb0fc39 | -11.81175 | -44.27002 | 2025-05-30 03:32:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 23dccc36-ac2c-3e2b-9075-916707f1b54f | -7.23355 | -43.09426 | 2025-05-30 03:32:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 6.2 |
| 45e1f48e-4d1c-3df1-a31f-e2166dda4054 | -11.79557 | -44.28952 | 2025-05-30 03:32:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 3.1 |
| ce1225f8-66f6-32b4-b8fc-8f9fa273c9a9 | -7.27649 | -44.22351 | 2025-05-30 03:32:00 | NPP-375D | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 71166877-51b2-331f-9cfc-a8c097bb680a | -8.5466 | -46.43076 | 2025-05-30 03:32:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| d23c95cd-94da-38c3-a852-686167996ed5 | -7.99911 | -45.68188 | 2025-05-30 03:32:00 | NPP-375D | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d14a7cfe-dcfc-3d4f-a591-7643835b4a99 | -6.3327 | -43.38295 | 2025-05-30 03:32:00 | NPP-375D | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 2ad42641-1481-3e9e-8d0e-ebb090c59179 | -7.61784 | -45.75089 | 2025-05-30 03:32:00 | NPP-375D | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 5.4 |
| d76bfc51-7c1d-34c4-902c-5f61ed7bc480 | -6.24137 | -43.37296 | 2025-05-30 03:32:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 66440367-1d7e-303a-8272-fcb5d5cec6dd | -7.23948 | -43.09543 | 2025-05-30 03:32:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 6.2 |
| 69786ca3-d7be-32bd-80a5-f4d0d65ca694 | -7.97001 | -45.94524 | 2025-05-30 03:32:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| ba34e503-f0d3-3cda-bbe2-538f4d063750 | -7.61933 | -45.73735 | 2025-05-30 03:32:00 | NPP-375D | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 0261dd17-c4c0-39e4-ac5a-5dbd994a5c2f | -6.33887 | -43.38395 | 2025-05-30 03:32:00 | NPP-375D | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| fc1e72a9-aeb6-36c1-8015-87123e539673 | -11.68968 | -46.21671 | 2025-05-30 03:32:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| e248551f-d388-3be5-8fdb-ea0090b6445d | -7.61803 | -45.74403 | 2025-05-30 03:32:00 | NPP-375D | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 862b7664-7d03-3739-b6d5-600ecfbb7251 | -7.24543 | -43.09654 | 2025-05-30 03:32:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 5.0 |
| 12e7bafa-8cda-3157-bb52-b65a19c12447 | -7.24465 | -43.10089 | 2025-05-30 03:32:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 9.5 |
| efdad61f-14fb-36a2-b7fb-6a6b63d08500 | -11.78964 | -44.28834 | 2025-05-30 03:32:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 388e1210-34d8-3107-b46c-5bdf7409e231 | -9.40099 | -40.37321 | 2025-05-30 03:32:00 | NPP-375D | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 12.0 |
| 559b7d92-1a06-3eac-a4a6-7d1b5a519bea | -7.62369 | -45.75186 | 2025-05-30 03:32:00 | NPP-375D | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 3cb4cf82-67fb-3532-89f3-c5b4ce060a90 | -6.23933 | -43.37622 | 2025-05-30 03:32:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 15cfbbab-2e9f-35ef-a0bf-0526c7be14a1 | -11.79644 | -44.28512 | 2025-05-30 03:32:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 3.1 |
| bc3f2082-287b-39b7-83a1-ed769f529cc4 | -9.40673 | -40.36882 | 2025-05-30 03:32:00 | NPP-375D | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 12.0 |
| 75ea626e-5ac3-37f5-b02a-6709f12b5be9 | -7.61672 | -45.7508 | 2025-05-30 03:32:00 | NPP-375D | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 3286dac8-c166-38cf-b10e-3fcc86b27e69 | -11.80434 | -41.19487 | 2025-05-30 03:32:00 | NPP-375D | MORRO DO CHAPÉU | BAHIA | Brasil | 2921708 | 29 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 9c14398b-caaa-329a-aa40-5f5e2abbd113 | -7.62481 | -45.75195 | 2025-05-30 03:32:00 | NPP-375D | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 39d07ac8-18a8-33d6-99af-69defed3e106 | -7.61088 | -45.74973 | 2025-05-30 03:32:00 | NPP-375D | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 281ad4be-aec2-329a-a298-09b3be744c7c | -7.61911 | -45.74409 | 2025-05-30 03:32:00 | NPP-375D | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 6c4e1178-9c04-328f-b5c3-db3fa9eb6218 | -6.24665 | -43.37901 | 2025-05-30 03:32:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f1982875-3524-3e7c-a40c-6c88a063f9aa | -7.59074 | -45.95881 | 2025-05-30 03:32:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| ce773e7d-6d5c-3e9b-a727-209feb921909 | -8.55215 | -46.42173 | 2025-05-30 03:32:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| b88b1363-21e1-3c38-b9f4-44c09f0dbecf | -7.24138 | -43.1008 | 2025-05-30 03:32:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 16.6 |
| e2acae4c-5b53-3e3c-946e-9711ad0ac3d1 | -11.81262 | -44.26564 | 2025-05-30 03:32:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| cd5e65fd-5ace-34c9-927a-b0c3c3716338 | -6.82629 | -44.65732 | 2025-05-30 03:32:00 | NPP-375D | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 5f95eb78-bca3-3197-a8b6-bd48601ee326 | -6.24457 | -43.38234 | 2025-05-30 03:32:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 7e52b11b-3320-3f4c-818a-f43748f6c9e2 | -8.07267 | -34.97488 | 2025-05-30 03:32:00 | NPP-375D | RECIFE | PERNAMBUCO | Brasil | 2611606 | 26 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| cc59f4f2-90bd-3a51-9eef-10cc2bb5e4b0 | -7.58162 | -45.86668 | 2025-05-30 03:32:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 26198c0d-31f4-33db-8678-778905682f4b | -7.19307 | -43.11378 | 2025-05-30 03:32:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 4.9 |


[Clique aqui para ver as próximas entradas](README3.md)
