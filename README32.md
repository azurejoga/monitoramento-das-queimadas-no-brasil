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

## Dados Diários - Página 32

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 5ea9a4c0-7de9-3733-af08-88a344504976 | -13.36527 | -47.92001 | 2025-09-30 03:49:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 6e5776f6-93da-3bb0-af7f-0bd716fa9063 | -7.12715 | -45.50262 | 2025-09-30 03:49:00 | NOAA-20 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| d28a6af4-02ef-33cc-8f95-db225084b9a6 | -6.90719 | -44.00005 | 2025-09-30 03:49:00 | NOAA-20 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| dce87da6-0773-3e0d-8dc0-0eb3daeacc6b | -14.65202 | -41.24222 | 2025-09-30 03:49:00 | NOAA-20 | CARAÍBAS | BAHIA | Brasil | 2906899 | 29 | 33 | nan | nan | nan | Caatinga | 0.6 |
| dcd59c5e-18e6-3803-b74b-31a06d5d953d | -12.88313 | -44.68858 | 2025-09-30 03:49:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| d6ceba7d-4ad7-359e-955b-fcb99ccf93f1 | -14.53511 | -48.23932 | 2025-09-30 03:49:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| d6bb93ce-0cda-36bb-9bf9-8159633796a0 | -16.38617 | -47.03949 | 2025-09-30 03:49:00 | NOAA-20 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 77a9a692-8a1c-34b1-b4e1-46af285577b7 | -5.73232 | -43.96415 | 2025-09-30 03:49:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| d86861d7-5408-3ee4-a3de-8f8b35c9f7e0 | -14.70333 | -48.24834 | 2025-09-30 03:49:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| a3556d71-4afe-34f3-9ee6-5ecf096a992d | -14.70546 | -48.15456 | 2025-09-30 03:49:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 1200f0f7-393c-324a-9757-0d78938ad80a | -13.66557 | -44.31254 | 2025-09-30 03:49:00 | NOAA-20 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 7b041662-9668-35de-8b13-05e807163bde | -14.64605 | -46.96978 | 2025-09-30 03:49:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| c39177e6-c186-3532-98a1-6b5f43bd99a0 | -5.81193 | -42.86612 | 2025-09-30 03:49:00 | NOAA-20 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 3d84845c-790f-33eb-a040-a246b63d570b | -5.66769 | -45.30092 | 2025-09-30 03:49:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 1022b016-6f98-3df7-a251-39fb8af846b9 | -13.13157 | -44.61763 | 2025-09-30 03:49:00 | NOAA-20 | SANTA MARIA DA VITÓRIA | BAHIA | Brasil | 2928109 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 3283e654-e0f3-3480-b75f-35e2bf8d0a40 | -12.82898 | -47.00476 | 2025-09-30 03:49:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 16e88b31-e250-37bc-91a5-1c5b4628ea68 | -14.53882 | -48.2392 | 2025-09-30 03:49:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| a859f94e-c341-37b4-99b0-e8aed6092140 | -16.42199 | -47.03562 | 2025-09-30 03:49:00 | NOAA-20 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 3f6416ad-2eed-3b98-a4f7-c9c5f28bbe65 | -13.78462 | -47.96294 | 2025-09-30 03:49:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 67304b76-cf85-3a0c-b43b-1091de544be3 | -12.87053 | -46.9555 | 2025-09-30 03:49:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 856b510f-d9d4-3798-bd24-bf4340cd07d4 | -13.61708 | -48.034 | 2025-09-30 03:49:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| e2c65b29-fbf3-36b1-9ad1-27f40f988f84 | -13.73167 | -48.68233 | 2025-09-30 03:49:00 | NOAA-20 | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 34626b31-fe7c-3068-92cc-1aaa65baf8d6 | -15.27489 | -47.88818 | 2025-09-30 03:49:00 | NOAA-20 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |
| eec0953a-c1ee-3e42-9d17-b696c317110d | -14.51112 | -48.43939 | 2025-09-30 03:49:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 968915cc-463f-30d7-ba4e-fb1cd97c16be | -6.37117 | -45.6284 | 2025-09-30 03:49:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| be66b646-d560-32b0-8892-374cd605a626 | -12.84447 | -47.00736 | 2025-09-30 03:49:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 19708b4a-86f9-397b-a72c-44fca1bb8e83 | -15.59637 | -47.83102 | 2025-09-30 03:49:00 | NOAA-20 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 1.7 |
| bdce2754-fdb2-32a6-9e8d-ac82523fb105 | -12.8489 | -46.87629 | 2025-09-30 03:49:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| a1d14782-0c07-3a42-8f8e-2f81828f866d | -6.17515 | -43.93416 | 2025-09-30 03:49:00 | NOAA-20 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 6a6958ec-2a96-381a-aa1f-46d0fa1c4c66 | -7.03909 | -45.1801 | 2025-09-30 03:49:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| dc042a72-bf56-3241-ae55-e159f90c3fe7 | -6.3008 | -43.80599 | 2025-09-30 03:49:00 | NOAA-20 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 2441f82c-14e3-3d87-a82e-989a0cabde54 | -5.91282 | -43.91911 | 2025-09-30 03:49:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 0eccb36b-4267-3f41-9fac-ad973413c3df | -14.53129 | -48.24894 | 2025-09-30 03:49:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| fc8127d6-7624-314b-9bf5-790aeb033608 | -7.51812 | -45.4376 | 2025-09-30 03:49:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| b3e84d27-2799-3d7c-a66a-a64561a91dad | -11.80415 | -44.90734 | 2025-09-30 03:49:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| af615ada-de5e-3d5d-906a-2f238d074741 | -17.01979 | -44.98471 | 2025-09-30 03:49:00 | NOAA-20 | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a4857ba7-4e9f-3138-a069-5bd503f98422 | -14.58228 | -48.28379 | 2025-09-30 03:49:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 7141fec8-4cbf-3619-842d-cad53c0fa9fe | -5.77358 | -42.85232 | 2025-09-30 03:49:00 | NOAA-20 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 3.9 |
| 6ace8c62-fba6-3f13-8fb6-4d7f2fe15614 | -15.32544 | -46.26101 | 2025-09-30 03:49:00 | NOAA-20 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 46173d97-b062-3739-8dbf-cbb2eb31d28b | -13.21519 | -47.3297 | 2025-09-30 03:49:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 23f0124b-5638-3f62-bd8c-116b12d8dfa7 | -6.45876 | -44.00467 | 2025-09-30 03:49:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 26.7 |
| 9a0c9495-c86f-30ec-99e1-7eb9c7626597 | -14.69919 | -45.25336 | 2025-09-30 03:49:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| c56f8133-34ca-36d4-add3-5c454e685164 | -6.2007 | -44.21343 | 2025-09-30 03:49:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 177264bb-f781-3d0d-9f13-829de6cf6f03 | -18.47809 | -43.79724 | 2025-09-30 03:49:00 | NOAA-20 | GOUVEIA | MINAS GERAIS | Brasil | 3127602 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 473258ab-e56b-375b-8e14-807c3ced315b | -15.92656 | -43.07392 | 2025-09-30 03:49:00 | NOAA-20 | RIACHO DOS MACHADOS | MINAS GERAIS | Brasil | 3154507 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 47498a0b-522e-3239-a42f-5d371c2c22d7 | -12.83885 | -46.99874 | 2025-09-30 03:49:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 3522baa6-8b41-30ed-b6aa-711221cb8eff | -15.59517 | -47.83044 | 2025-09-30 03:49:00 | NOAA-20 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 3a98ae33-abc0-3f0c-abc7-670bc291e221 | -14.0412 | -42.15399 | 2025-09-30 03:49:00 | NOAA-20 | LAGOA REAL | BAHIA | Brasil | 2918753 | 29 | 33 | nan | nan | nan | Caatinga | 4.2 |
| 3ba4e229-7096-33d9-9115-fedc001933e6 | -6.88946 | -44.5188 | 2025-09-30 03:49:00 | NOAA-20 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 72e9d429-4e47-3d29-817d-f368cb0398a2 | -6.68357 | -42.78861 | 2025-09-30 03:49:00 | NOAA-20 | FRANCISCO AYRES | PIAUÍ | Brasil | 2204105 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 4f8d17e5-0baf-3206-bd4e-0be27634e71c | -5.47348 | -48.66296 | 2025-09-30 03:49:00 | NOAA-20 | SÃO JOÃO DO ARAGUAIA | PARÁ | Brasil | 1507508 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 7e5eea07-918b-3a01-b1e1-5e35df003b68 | -5.6625 | -45.3 | 2025-09-30 03:49:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| a6886451-8fcd-32db-9033-cc0dc8bca40c | -14.69105 | -48.14328 | 2025-09-30 03:49:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| c9cc3cdb-f96e-351b-b2a6-27c26876548c | -13.39202 | -48.0749 | 2025-09-30 03:49:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 895fdd0b-5c8e-3728-ba7d-78be08b30d1d | -13.78813 | -47.97339 | 2025-09-30 03:49:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| a2469f72-72bd-3863-9ac1-ad424ce76ce1 | -14.69787 | -48.24768 | 2025-09-30 03:49:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 55c36eca-4bd7-330a-ba55-611618a08b0a | -14.54205 | -48.48329 | 2025-09-30 03:49:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 8.0 |
| a7cb85fe-e431-3bf1-a35c-78dce53267e6 | -14.81077 | -48.76123 | 2025-09-30 03:49:00 | NOAA-20 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 1ab900b0-3e4b-3141-b635-15bdc1012c3c | -12.84298 | -46.97675 | 2025-09-30 03:49:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 7d2e286f-3353-381e-b057-b18869b02d8a | -15.53891 | -47.87054 | 2025-09-30 03:49:00 | NOAA-20 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 86da4e72-04e1-34a0-b967-bdbb8fe34f09 | -6.30695 | -43.43897 | 2025-09-30 03:49:00 | NOAA-20 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 195833f9-82b0-37c4-86fb-45bc570af928 | -12.68779 | -40.46967 | 2025-09-30 03:49:00 | NOAA-20 | BOA VISTA DO TUPIM | BAHIA | Brasil | 2903805 | 29 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 76dea12c-90bf-3dd4-8e0a-5397f7456aa9 | -15.32627 | -47.92909 | 2025-09-30 03:49:00 | NOAA-20 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 0.3 |
| 9c5cf414-e857-3585-bd74-539be5d8afe0 | -14.53947 | -48.49606 | 2025-09-30 03:49:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 3eaf738b-1aeb-3a7d-987b-d2e53a4cf7e8 | -12.83011 | -43.80554 | 2025-09-30 03:49:00 | NOAA-20 | SERRA DOURADA | BAHIA | Brasil | 2930303 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 3cb64431-079d-3635-8cd3-c144a50af855 | -12.86825 | -46.91261 | 2025-09-30 03:49:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| ee0b7bed-c485-3ef9-98d1-d4bfede06487 | -14.51352 | -48.42495 | 2025-09-30 03:49:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 305c19de-3242-362d-8d74-097108e61943 | -6.43136 | -43.07343 | 2025-09-30 03:49:00 | NOAA-20 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 9194b638-9c18-3fb9-8a04-22b8a15a2e58 | -6.39396 | -42.89355 | 2025-09-30 03:49:00 | NOAA-20 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 2.5 |
| c62f39da-428c-3255-8e54-b19b1b3262ef | -14.70246 | -48.2527 | 2025-09-30 03:49:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 93d69822-dbbe-31ff-9c0d-c68a00a08ea3 | -14.72417 | -45.66648 | 2025-09-30 03:49:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| e0234de0-16e0-31a6-bb66-823c5d7a5cbb | -16.49875 | -46.04033 | 2025-09-30 03:49:00 | NOAA-20 | BONFINÓPOLIS DE MINAS | MINAS GERAIS | Brasil | 3108206 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 926bbd3f-62fa-3015-b0b9-d3ac344ae14f | -12.78914 | -46.89719 | 2025-09-30 03:49:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 0dcd9969-23ba-38ce-8719-71615535a21b | -13.80915 | -47.95175 | 2025-09-30 03:49:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 49af8816-f216-3f19-acb3-23f91819a9ed | -16.42441 | -47.01566 | 2025-09-30 03:49:00 | NOAA-20 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 2511c184-3874-3179-b369-d0ae8958a761 | -15.7764 | -43.67046 | 2025-09-30 03:49:00 | NOAA-20 | SÃO JOÃO DA PONTE | MINAS GERAIS | Brasil | 3162401 | 31 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 2be6895f-4f11-318f-b0a1-20dea7521269 | -17.59281 | -39.26246 | 2025-09-30 03:49:00 | NOAA-20 | ALCOBAÇA | BAHIA | Brasil | 2900801 | 29 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| 702c388f-4b2a-337c-9450-8de9b55be5d6 | -14.68562 | -48.14263 | 2025-09-30 03:49:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 845118ed-d036-343c-b140-04c8191978b5 | -13.22184 | -50.94595 | 2025-09-30 03:49:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 9.7 |
| b7a1ecdd-d228-34f1-a42a-7ed2ce224c19 | -14.55706 | -48.46537 | 2025-09-30 03:49:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 5c988074-37da-394b-85b9-591ab02b49f4 | -12.83474 | -47.00259 | 2025-09-30 03:49:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 4252fbfc-0ef8-33cd-ae28-c26d04f8950a | -15.86073 | -46.23029 | 2025-09-30 03:49:00 | NOAA-20 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 9.5 |
| c63a96a2-f7fa-3235-8f50-249f1860b8b3 | -18.4805 | -44.0245 | 2025-09-30 03:49:00 | NOAA-20 | SANTO HIPÓLITO | MINAS GERAIS | Brasil | 3160603 | 31 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 384d06b8-6f73-3368-ac01-ceebef0c6c32 | -6.29062 | -43.9207 | 2025-09-30 03:49:00 | NOAA-20 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 31690720-8e13-385d-bee2-51184b881110 | -15.9268 | -46.21024 | 2025-09-30 03:49:00 | NOAA-20 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 9.6 |
| 0b9fafd8-8d36-325b-8d57-9c996e409148 | -6.49555 | -44.27221 | 2025-09-30 03:49:00 | NOAA-20 | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 33.8 |
| 139d915c-799b-374f-b056-5c7ad3a45119 | -13.79603 | -47.87719 | 2025-09-30 03:49:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 8b63cf77-591d-3d21-a3a3-ca1dbef57a27 | -5.97614 | -42.56283 | 2025-09-30 03:49:00 | NOAA-20 | HUGO NAPOLEÃO | PIAUÍ | Brasil | 2204600 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| a04cd9dc-df5a-32d0-985c-d00343ea59d0 | -14.54889 | -48.47764 | 2025-09-30 03:49:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 8.1 |
| da3e0d74-621a-3b94-91ca-22ad0b47c574 | -13.03048 | -42.81149 | 2025-09-30 03:49:00 | NOAA-20 | MACAÚBAS | BAHIA | Brasil | 2919801 | 29 | 33 | nan | nan | nan | Caatinga | 1.8 |
| dd9a9ca6-0a50-35bc-a5fd-fa4d4ad8b5f6 | -5.98129 | -43.60952 | 2025-09-30 03:49:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 7e0b71a5-bf9b-37a7-880b-4d0c878673e2 | -14.54703 | -48.26348 | 2025-09-30 03:49:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a68b892b-18d7-39eb-943c-a6447b25bfd9 | -15.26927 | -49.25439 | 2025-09-30 03:49:00 | NOAA-20 | GOIANÉSIA | GOIÁS | Brasil | 5208608 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| cd40dd4c-31d3-363d-812d-e2202de6d4c0 | -12.22633 | -47.79926 | 2025-09-30 03:49:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 8ec34ffe-2100-3846-8510-d2d0cd528f6e | -13.81059 | -47.50134 | 2025-09-30 03:49:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| d283ba89-a5b4-33e7-bc81-3802f6d12621 | -15.82181 | -48.16506 | 2025-09-30 03:49:00 | NOAA-20 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 7427a888-3eed-3e13-a184-d13b4c22bf2a | -18.05638 | -43.65298 | 2025-09-30 03:49:00 | NOAA-20 | DIAMANTINA | MINAS GERAIS | Brasil | 3121605 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 63c36b6a-4041-3bb6-9c45-fd46289fa05a | -14.51151 | -48.43515 | 2025-09-30 03:49:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| bfc3e4eb-e1b4-30ef-9d69-5a0a37a62fe7 | -6.50267 | -44.11546 | 2025-09-30 03:49:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| fe156c69-8c93-365d-805b-b7527b852010 | -6.05558 | -42.45041 | 2025-09-30 03:49:00 | NOAA-20 | HUGO NAPOLEÃO | PIAUÍ | Brasil | 2204600 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |


[Clique aqui para ver as próximas entradas](README33.md)
