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

## Dados Diários - Página 46

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| caac9cf9-ec69-3793-9709-53889210b6f9 | -7.96773 | -50.00145 | 2025-11-17 05:08:00 | NPP-375D | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 1d7cabb0-3711-3bbe-9432-6d9dc8d93f32 | -3.58074 | -50.41893 | 2025-11-17 05:08:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c59cc67b-7941-3df3-ab72-45405736b3ba | -7.08861 | -42.73486 | 2025-11-17 05:08:00 | NPP-375D | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 74688ad8-caf2-395e-89cf-a77f09800b3a | -11.20386 | -46.62529 | 2025-11-17 05:08:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| ff852d6c-2031-32b3-8e73-57694490b555 | -6.67865 | -42.03521 | 2025-11-17 05:08:00 | NPP-375D | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 12.2 |
| e651fcde-8992-320c-8186-82ea26a51671 | -3.88465 | -46.46213 | 2025-11-17 05:08:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 35a0c9f6-6904-37b2-9c3a-fa9ee1d8ca69 | -6.00276 | -51.51762 | 2025-11-17 05:08:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 559d094d-161b-348f-97b0-201d410571f8 | -3.30553 | -53.85219 | 2025-11-17 05:08:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d7a040f8-0383-342b-9d4c-29843f85e4c6 | -10.66454 | -49.35983 | 2025-11-17 05:08:00 | NPP-375D | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 553a16b4-a4ef-3187-9759-f15b85cfaf2e | -3.33229 | -49.90721 | 2025-11-17 05:08:00 | NPP-375D | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6c721761-b586-386b-a07c-4de5ba761c0a | -4.10137 | -48.02565 | 2025-11-17 05:08:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| e81337bd-a244-354c-8df0-a52d63ab6cf5 | -3.40641 | -50.26999 | 2025-11-17 05:08:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| abd68903-c784-3adf-8b1e-6fb2826f0fca | -3.46524 | -49.99047 | 2025-11-17 05:08:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 6eca1576-9937-3bb9-861a-f43c488df977 | -4.24458 | -49.67744 | 2025-11-17 05:08:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 965ba59e-9ce6-3326-b02b-4ab9bf0458da | -8.32335 | -45.40722 | 2025-11-17 05:08:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| aed70fc8-36d4-318a-aa46-b56b2a9b67ae | -4.40781 | -45.8398 | 2025-11-17 05:08:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 1be05bd1-6c74-37db-94b5-97d69cc62cfa | -4.5749 | -50.94257 | 2025-11-17 05:08:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 9648d61c-a55c-3b45-8253-99ecd6f25d43 | -7.03162 | -47.61635 | 2025-11-17 05:08:00 | NPP-375D | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 5f83886c-f0b8-3ff3-a1ea-e0d84c4e7f98 | -3.30263 | -50.07803 | 2025-11-17 05:08:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2b257c01-3424-3653-b4f1-eb29ab0e0782 | -7.81391 | -55.07091 | 2025-11-17 05:08:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 986603c2-7c0a-3959-af39-7c9793c15e0e | -7.96714 | -50.00563 | 2025-11-17 05:08:00 | NPP-375D | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 0d326d60-da33-380e-b79d-2a71153c7dea | -3.29936 | -53.84759 | 2025-11-17 05:08:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4fad3b60-5246-3e3d-93c9-c68a50ddd1c2 | -2.99701 | -51.01287 | 2025-11-17 05:08:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 812abdc4-6c35-3692-9720-683224986e0c | -10.65892 | -48.16542 | 2025-11-17 05:08:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 0e6b0974-4d42-36a8-8ea5-4119a09cb3e4 | -7.03122 | -47.61924 | 2025-11-17 05:08:00 | NPP-375D | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| efb8ceb9-dc20-3088-a736-80e06e46f2d5 | -3.91511 | -45.79591 | 2025-11-17 05:08:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 71903393-90da-3fcc-8fea-410cdf2135bd | -3.20332 | -54.58918 | 2025-11-17 05:08:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 0.3 |
| 8585c167-8fed-3451-8360-78a5e4630a6b | -3.23393 | -50.51029 | 2025-11-17 05:08:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 7bae8a60-3c23-33eb-91c9-e9f07a096423 | -9.32462 | -46.57364 | 2025-11-17 05:08:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 10.7 |
| 6685430f-54ef-34c9-acbf-45dcd47f497d | -9.15605 | -48.06886 | 2025-11-17 05:08:00 | NPP-375D | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 27c29a21-2504-35fc-b1c0-a92364c98bd7 | -10.85205 | -46.75636 | 2025-11-17 05:08:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| f02094e3-bfc5-3d5a-b4f9-94ab42552847 | -3.80096 | -51.95994 | 2025-11-17 05:08:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 9c8c4cb6-a50b-354e-9c71-99c904e1617d | -4.72897 | -46.38155 | 2025-11-17 05:08:00 | NPP-375D | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 60a73c89-e649-338c-91d2-2d2188ebc1ca | -10.63637 | -44.6082 | 2025-11-17 05:08:00 | NPP-375D | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a60d40d2-4a3e-3827-9979-933e31b9fcb0 | -2.89499 | -53.28392 | 2025-11-17 05:08:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| edfea2e9-9a31-33bc-93fb-3ace098174a1 | -4.71995 | -46.38441 | 2025-11-17 05:08:00 | NPP-375D | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 03e68373-cfd3-30bf-9fdd-852e77d2ec9b | -5.81983 | -48.99918 | 2025-11-17 05:08:00 | NPP-375D | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 1b2c6894-9c3a-32a3-a2db-e1ab13662193 | -4.66158 | -46.73774 | 2025-11-17 05:08:00 | NPP-375D | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 5.7 |
| c222b442-922c-3b61-8623-cc3813659efd | -6.30146 | -43.78938 | 2025-11-17 05:08:00 | NPP-375D | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 9.1 |
| c6e42841-2e96-36ee-b0db-53ec9cbc16fe | -2.89101 | -53.28704 | 2025-11-17 05:08:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 4efba9de-badc-3063-acea-6429cfc81a0f | -4.09664 | -48.0251 | 2025-11-17 05:08:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 1b26d7fa-7ee2-3cc2-a30c-b0fccdab9ce0 | -6.68078 | -42.04134 | 2025-11-17 05:08:00 | NPP-375D | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 8.7 |
| c4a06497-fd21-310e-8363-140a87e6e1ec | -10.95402 | -48.67793 | 2025-11-17 05:08:00 | NPP-375D | BREJINHO DE NAZARÉ | TOCANTINS | Brasil | 1703701 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 26c4a862-cc5f-3376-9c4a-819705c75eeb | -4.07931 | -46.19934 | 2025-11-17 05:08:00 | NPP-375D | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 1524d1d3-414b-36d8-960a-d276da1a1832 | -3.24087 | -50.49083 | 2025-11-17 05:08:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| be3caad8-ac28-3301-b721-964b4e594135 | -6.30789 | -43.79033 | 2025-11-17 05:08:00 | NPP-375D | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 9.1 |
| 8ea91fdf-2955-3d9e-8064-05dfb6de441b | -3.77819 | -50.13871 | 2025-11-17 05:08:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| c8a13a10-da13-3ccc-9fd5-4eb31cd23f98 | -11.15363 | -44.04137 | 2025-11-17 05:08:00 | NPP-375D | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 1b5bc427-1e6f-3aab-bb52-5b160c3dee12 | -3.49207 | -54.04382 | 2025-11-17 05:08:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3ad02a7a-9f34-3256-a67f-de0fb4a38257 | -3.18474 | -50.65168 | 2025-11-17 05:08:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 932d6a11-f706-35eb-9f5f-7f6341097443 | -4.04947 | -49.02959 | 2025-11-17 05:08:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 059b6e35-4bd6-3fab-9ac8-de574d3cb9a2 | -7.13597 | -47.13425 | 2025-11-17 05:08:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 78eaffa5-9674-3c73-b936-383fa1eb71e4 | -7.2645 | -48.01983 | 2025-11-17 05:08:00 | NPP-375D | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| de31c0ee-5d34-3eb9-8866-e1a27627763a | -10.66317 | -49.36998 | 2025-11-17 05:08:00 | NPP-375D | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 14.7 |
| 0947ba47-6358-3a88-8590-a3a3bf417563 | -3.83318 | -49.80471 | 2025-11-17 05:08:00 | NPP-375D | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 681a9895-c610-3f9b-8198-aabd4f8ecb8d | -3.3893 | -54.33335 | 2025-11-17 05:08:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 0d5d0c58-c101-3125-a066-d6b277d8f017 | -9.15793 | -47.58847 | 2025-11-17 05:08:00 | NPP-375D | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 20597957-bf9c-37c9-b0a1-0a043cad01c5 | -5.88709 | -43.97656 | 2025-11-17 05:08:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 26a68c5e-69c3-3971-9487-bba851cf87f0 | -4.69304 | -46.30872 | 2025-11-17 05:08:00 | NPP-375D | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 851591a5-df9c-3d47-a3d5-d5f3e37f1b9b | -5.35578 | -44.86541 | 2025-11-17 05:08:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 4358ef70-6efd-38af-b763-6d8254ad7e5f | -4.68053 | -46.93873 | 2025-11-17 05:08:00 | NPP-375D | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8f767dc6-ea23-39c5-a405-78b807367d08 | -3.77492 | -49.24889 | 2025-11-17 05:08:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 0.3 |
| b4bd1b3a-6d4a-34e7-aed9-99034f634ba4 | -3.01195 | -51.34526 | 2025-11-17 05:08:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 90380902-1a22-351e-b36e-5467fb990ff3 | -3.30235 | -50.21703 | 2025-11-17 05:08:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 55717c78-5805-3da8-b5fd-381653a8a31a | -4.04399 | -54.30215 | 2025-11-17 05:08:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 938a5b1c-f2d9-3518-893b-73b89cf59257 | -7.25618 | -48.00756 | 2025-11-17 05:08:00 | NPP-375D | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 5ef538bd-ceae-334a-b0d2-b2fd1a781e23 | -3.29854 | -50.07775 | 2025-11-17 05:08:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e2e0e118-c6a7-3bf7-9f26-c11026a53509 | -4.66117 | -46.7443 | 2025-11-17 05:08:00 | NPP-375D | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 0815fc30-49e9-37cb-8221-d3e39e3f6322 | -5.88592 | -43.97099 | 2025-11-17 05:08:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 30f47ea3-7fe5-3a09-9c19-6f5bd770d4b8 | -3.77862 | -49.2536 | 2025-11-17 05:08:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 5ab29a95-ce3a-33a7-89c3-b683a6f8bdf5 | -3.60523 | -55.53636 | 2025-11-17 05:08:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7e571230-6df0-31a5-8fe2-d6e560b22ac3 | -8.8792 | -44.78503 | 2025-11-17 05:08:00 | NPP-375D | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 6ea01758-c0a4-3505-ab80-c0990a40266b | -7.96338 | -50.00083 | 2025-11-17 05:08:00 | NPP-375D | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4f489f66-7824-30a3-ab57-30927b5fcfd3 | -4.01622 | -48.80563 | 2025-11-17 05:08:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| f2b5b7c7-009d-3452-ac4a-9eb0bfbf8f8a | -6.67055 | -42.04107 | 2025-11-17 05:08:00 | NPP-375D | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 6.8 |
| 3dcc633a-49c7-37d0-a257-cf2c4cf3b528 | -3.39393 | -50.18928 | 2025-11-17 05:08:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 42d7e19c-c995-37e9-b6b2-b36de5ce05fa | -3.23351 | -50.49305 | 2025-11-17 05:08:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| d5eedc4f-d270-3db4-9805-bac9bc53188f | -3.30272 | -53.84811 | 2025-11-17 05:08:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9ac345e0-4c2d-3442-83ad-8899ecb14747 | -4.00365 | -48.97495 | 2025-11-17 05:08:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6e8a1ca8-e030-3f60-a218-b5887da50bba | -4.94059 | -44.5262 | 2025-11-17 05:08:00 | NPP-375D | SANTO ANTÔNIO DOS LOPES | MARANHÃO | Brasil | 2110302 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f427ed82-44c9-36ac-b4ee-de2eec516c05 | -11.05123 | -47.60613 | 2025-11-17 05:08:00 | NPP-375D | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 9adfbb58-b27f-3f40-a5ca-4a0cc8a07f56 | -6.6875 | -42.0296 | 2025-11-17 05:10:00 | GOES-19 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 65.7 |
| 89936986-eb0c-3cf0-97f1-04d215687982 | -12.8857 | -46.45819 | 2025-11-17 05:10:00 | NPP-375D | COMBINADO | TOCANTINS | Brasil | 1705557 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 31c9adf9-c991-3c77-89cc-395943ec2d66 | -12.7444 | -48.92317 | 2025-11-17 05:10:00 | NPP-375D | TALISMÃ | TOCANTINS | Brasil | 1720978 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| bd53764c-508a-395c-9338-8f238fdcfe05 | -12.91055 | -45.11065 | 2025-11-17 05:10:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 810bcc5a-e1e2-3a2c-b5ee-0ed439cfcc46 | -11.96984 | -44.30283 | 2025-11-17 05:10:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 13e2e48c-40e7-39e8-a5f0-59ed960b27c5 | -12.40897 | -47.53631 | 2025-11-17 05:10:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| e472f617-9ab2-3255-a492-440d1b4e31bf | -12.43888 | -44.74749 | 2025-11-17 05:10:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| f6a4ef95-38f0-39d2-9a9f-d8b2b69a655b | -12.87039 | -46.43393 | 2025-11-17 05:10:00 | NPP-375D | COMBINADO | TOCANTINS | Brasil | 1705557 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 8660b93c-ca5b-3750-8627-0ff96b20f8d6 | -12.80661 | -46.43367 | 2025-11-17 05:10:00 | NPP-375D | LAVANDEIRA | TOCANTINS | Brasil | 1712157 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| b17b5557-e148-36b8-940b-3159de8f7681 | -11.34138 | -48.90219 | 2025-11-17 05:10:00 | NPP-375D | ALIANÇA DO TOCANTINS | TOCANTINS | Brasil | 1700350 | 17 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 85db90d0-8b0d-3d9d-af4c-01c65dccad51 | -9.48675 | -59.45903 | 2025-11-17 05:10:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| fa64b630-f2f0-3fcb-9a50-36f200023ad5 | -13.27595 | -47.29102 | 2025-11-17 05:10:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| aed7950c-3ed5-3665-acf2-99775607c959 | -11.97049 | -44.29696 | 2025-11-17 05:10:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 6878dc7a-509d-3fe2-bce4-b4d4b0bb17b8 | -11.99762 | -49.27307 | 2025-11-17 05:10:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| e591b945-ede3-36fa-b4d7-64b9ce189c2c | -11.70655 | -48.86298 | 2025-11-17 05:10:00 | NPP-375D | GURUPI | TOCANTINS | Brasil | 1709500 | 17 | 33 | nan | nan | nan | Cerrado | 10.8 |
| 86c89a9f-488e-3811-b0a7-b3680f83844e | -11.70685 | -44.44532 | 2025-11-17 05:10:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| cb98ed56-cb6f-3f2d-a101-280438710b14 | -10.91467 | -49.41271 | 2025-11-17 05:10:00 | NPP-375D | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 3f7bb000-9610-383e-a0d1-7c45abc819fc | -13.43339 | -56.83078 | 2025-11-17 05:10:00 | NPP-375D | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 3822eecc-94a0-3872-a226-0d3e8cad3448 | -11.81 | -45.30484 | 2025-11-17 05:10:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |


[Clique aqui para ver as próximas entradas](README47.md)
