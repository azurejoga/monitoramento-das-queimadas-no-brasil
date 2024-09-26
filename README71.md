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

## Dados Diários - Página 71

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 1826aae1-101c-37c1-9ea5-48324a4fd0f7 | -19.61707 | -44.1778 | 2024-09-26 04:08:00 | NOAA-20 | MATOZINHOS | MINAS GERAIS | Brasil | 3141108 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| c8297924-d3a5-3069-a489-b3a85dfbc050 | -19.61489 | -44.16991 | 2024-09-26 04:08:00 | NOAA-20 | MATOZINHOS | MINAS GERAIS | Brasil | 3141108 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 70d297f6-2175-36ea-8c0c-ec42b3cf3de6 | -19.61432 | -44.17357 | 2024-09-26 04:08:00 | NOAA-20 | MATOZINHOS | MINAS GERAIS | Brasil | 3141108 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 9a58c291-28ca-3f87-8837-2e940f7d008c | -19.6107 | -43.97755 | 2024-09-26 04:08:00 | NOAA-20 | CONFINS | MINAS GERAIS | Brasil | 3117876 | 31 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 3481d172-0613-3ffd-b38f-db01142cea39 | -19.61014 | -43.9812 | 2024-09-26 04:08:00 | NOAA-20 | CONFINS | MINAS GERAIS | Brasil | 3117876 | 31 | 33 | nan | nan | nan | Cerrado | 2.8 |
| c547ff5d-563b-3b62-bbea-4863e0a4cb06 | -19.58845 | -44.27411 | 2024-09-26 04:08:00 | NOAA-20 | ESMERALDAS | MINAS GERAIS | Brasil | 3124104 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 1369664b-7af1-3c84-959b-041c409289a6 | -19.52146 | -44.50608 | 2024-09-26 04:08:00 | NOAA-20 | CACHOEIRA DA PRATA | MINAS GERAIS | Brasil | 3109600 | 31 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 13f514be-44c7-303e-885d-52298b929ec9 | -19.51872 | -44.50185 | 2024-09-26 04:08:00 | NOAA-20 | CACHOEIRA DA PRATA | MINAS GERAIS | Brasil | 3109600 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 7eb77e52-1f97-3e97-9171-28c0a9f7a7de | -19.51815 | -44.5055 | 2024-09-26 04:08:00 | NOAA-20 | CACHOEIRA DA PRATA | MINAS GERAIS | Brasil | 3109600 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| c630570a-0b75-3747-9aac-39aeea9e7b50 | -19.95468 | -44.96432 | 2024-09-26 04:08:00 | NOAA-20 | PERDIGÃO | MINAS GERAIS | Brasil | 3149705 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 65a77a45-9893-3b17-b87d-339c60468dde | -19.95078 | -44.96739 | 2024-09-26 04:08:00 | NOAA-20 | PERDIGÃO | MINAS GERAIS | Brasil | 3149705 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 9c2b182b-e252-3835-b5ec-becfb5a1c081 | -19.90016 | -44.96695 | 2024-09-26 04:08:00 | NOAA-20 | NOVA SERRANA | MINAS GERAIS | Brasil | 3145208 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 2688e55e-c484-35fe-95d1-1ec33f530057 | -19.62918 | -44.79121 | 2024-09-26 04:08:00 | NOAA-20 | PITANGUI | MINAS GERAIS | Brasil | 3151404 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 5cafa9e7-d5d4-3f8a-8d22-c4aa4919b88d | -19.73475 | -44.76851 | 2024-09-26 04:08:00 | NOAA-20 | ONÇA DE PITANGUI | MINAS GERAIS | Brasil | 3145802 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 18be3e93-7e65-3150-8ae4-e154c6fa9e9b | -19.73417 | -44.77216 | 2024-09-26 04:08:00 | NOAA-20 | ONÇA DE PITANGUI | MINAS GERAIS | Brasil | 3145802 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| 0d4df582-2774-3ed8-85cd-91ceee74d783 | -19.73301 | -44.77946 | 2024-09-26 04:08:00 | NOAA-20 | ONÇA DE PITANGUI | MINAS GERAIS | Brasil | 3145802 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 83a0134f-4c54-372e-820a-228de554ddde | -12.97951 | -44.71935 | 2024-09-26 04:08:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 70ae7774-ced7-3398-9d17-d9892560cec8 | -12.96929 | -44.71756 | 2024-09-26 04:08:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| f9fdd527-b212-335e-bab9-1118c40cf9f1 | -12.96589 | -44.71694 | 2024-09-26 04:08:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 3d2571a0-b0ce-3fd0-9b03-853f6142da7a | -12.45538 | -44.79188 | 2024-09-26 04:08:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| aae67ab4-7184-3d98-aa29-b1b718da2eb4 | -12.45195 | -44.7913 | 2024-09-26 04:08:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f2e92c25-9586-36cb-b745-1da472a64655 | -13.66218 | -43.73382 | 2024-09-26 04:08:00 | NOAA-20 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 7e6ce3f0-293f-32c2-94f1-2f78cb4c582d | -13.44159 | -43.7746 | 2024-09-26 04:08:00 | NOAA-20 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| d1933eff-68d3-3cba-ba12-2013ad5c2b0c | -13.44102 | -43.77817 | 2024-09-26 04:08:00 | NOAA-20 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a7392a14-300e-30dd-98ca-39bec6dfcaf5 | -13.38244 | -43.74292 | 2024-09-26 04:08:00 | NOAA-20 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 83920074-66b4-3d44-aed4-80eeba507dca | -13.38187 | -43.74649 | 2024-09-26 04:08:00 | NOAA-20 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| b5c96532-04e8-3bcf-84c0-456bdbff0a69 | -13.3813 | -43.75006 | 2024-09-26 04:08:00 | NOAA-20 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| b2445a26-b896-37c7-9587-6934a9180ea0 | -13.26715 | -43.5698 | 2024-09-26 04:08:00 | NOAA-20 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 656574c4-7d54-3a6f-b184-6c74d5c4702e | -13.26659 | -43.57336 | 2024-09-26 04:08:00 | NOAA-20 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 2c3058bd-92ea-3cec-a8b2-d721a960119f | -12.58567 | -43.37062 | 2024-09-26 04:08:00 | NOAA-20 | SÍTIO DO MATO | BAHIA | Brasil | 2930758 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 9ee47f77-1643-3c95-85f5-1ec9a06b77e6 | -14.45698 | -45.232 | 2024-09-26 04:08:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 1f9232db-6388-3e60-867d-2066e03397f7 | -14.45635 | -45.23582 | 2024-09-26 04:08:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 33c5dfa2-1740-3319-96f6-1b0e343a21a2 | -14.45356 | -45.23137 | 2024-09-26 04:08:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 24131320-923a-3184-b3cd-30b61b947311 | -14.44232 | -45.25689 | 2024-09-26 04:08:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 276343ee-f261-3a38-a475-96068c322a3b | -14.44169 | -45.26068 | 2024-09-26 04:08:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| ebe743a5-2126-36fd-a2a3-ac266628c38b | -14.43826 | -45.26006 | 2024-09-26 04:08:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 640099e9-9739-3cff-a206-7fdf63aa843a | -14.43764 | -45.26388 | 2024-09-26 04:08:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 3.3 |
| c27c36bd-2385-3099-a926-64134d83e9e2 | -14.37437 | -45.24109 | 2024-09-26 04:08:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| df44ff68-8ce5-3cad-9f01-ac4875f544e6 | -14.08926 | -43.7613 | 2024-09-26 04:08:00 | NOAA-20 | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 30a4a1c4-7fee-3110-8ced-0d4df15efeb0 | -14.08869 | -43.76487 | 2024-09-26 04:08:00 | NOAA-20 | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 4c72047e-d8a1-3e8f-9982-60e2b73d6ee2 | -16.32846 | -45.67359 | 2024-09-26 04:08:00 | NOAA-20 | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 22ceb355-1d66-3baf-8be9-1c1bde7eb57e | -16.32503 | -45.67298 | 2024-09-26 04:08:00 | NOAA-20 | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 139bda2a-b45e-3617-a794-9f48bbba0fbf | -16.32439 | -45.67684 | 2024-09-26 04:08:00 | NOAA-20 | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | 2.6 |
| ab263c5e-6e7a-33de-ad03-778da111f612 | -16.32161 | -45.67236 | 2024-09-26 04:08:00 | NOAA-20 | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | 2.6 |
| d75b00f8-3c2a-3f4c-b44c-3ba69df9a4c9 | -16.32097 | -45.67623 | 2024-09-26 04:08:00 | NOAA-20 | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 8c5ca2cd-6952-3f85-b09f-c2501ce151ec | -15.91186 | -45.00249 | 2024-09-26 04:08:00 | NOAA-20 | SÃO FRANCISCO | MINAS GERAIS | Brasil | 3161106 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 94cce3bc-ebea-3ea8-a73d-22c0b911935c | -15.90849 | -45.0019 | 2024-09-26 04:08:00 | NOAA-20 | SÃO FRANCISCO | MINAS GERAIS | Brasil | 3161106 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 1ab7675f-4d00-3b48-abb0-39046192ba6c | -15.90392 | -45.00875 | 2024-09-26 04:08:00 | NOAA-20 | SÃO FRANCISCO | MINAS GERAIS | Brasil | 3161106 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| dd0b908c-f995-381a-9043-8a2d17c721eb | -15.53562 | -45.01117 | 2024-09-26 04:08:00 | NOAA-20 | JANUÁRIA | MINAS GERAIS | Brasil | 3135209 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| c990aa6f-54e6-3189-8e45-4b80ca6f840a | -15.53501 | -45.01489 | 2024-09-26 04:08:00 | NOAA-20 | JANUÁRIA | MINAS GERAIS | Brasil | 3135209 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 2a1a7912-00c2-3013-a35f-f562dde6fc69 | -16.88698 | -45.33135 | 2024-09-26 04:08:00 | NOAA-20 | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| da61193c-76a1-301b-8b40-b04c15c99846 | -19.4109 | -45.15656 | 2024-09-26 04:08:00 | NOAA-20 | MARTINHO CAMPOS | MINAS GERAIS | Brasil | 3140506 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| fc547331-25b5-3fd8-8a51-b0d3f18f1dfc | -19.35197 | -45.85641 | 2024-09-26 04:08:00 | NOAA-20 | SERRA DA SAUDADE | MINAS GERAIS | Brasil | 3166600 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| ec0c0303-db33-32b6-b9ab-83504948206a | -18.80971 | -45.80267 | 2024-09-26 04:08:00 | NOAA-20 | TIROS | MINAS GERAIS | Brasil | 3168903 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e836e145-d773-3ecf-9e2b-2f4edf4109bd | -18.80634 | -45.80207 | 2024-09-26 04:08:00 | NOAA-20 | TIROS | MINAS GERAIS | Brasil | 3168903 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| a585f2ff-bcaf-356b-87de-dd21336be66b | -18.43102 | -45.09853 | 2024-09-26 04:08:00 | NOAA-20 | TRÊS MARIAS | MINAS GERAIS | Brasil | 3169356 | 31 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 9845801e-0d09-3f45-a9a0-823b2ee66a8a | -19.97447 | -45.5573 | 2024-09-26 04:08:00 | NOAA-20 | LAGOA DA PRATA | MINAS GERAIS | Brasil | 3137205 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 367d310f-5d89-3ff3-9afd-8b4508ad30ae | -19.96235 | -45.54739 | 2024-09-26 04:08:00 | NOAA-20 | LAGOA DA PRATA | MINAS GERAIS | Brasil | 3137205 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 8dc49c7d-0a72-3d98-a648-a09b6c47e5b6 | -19.91313 | -45.28624 | 2024-09-26 04:08:00 | NOAA-20 | BOM DESPACHO | MINAS GERAIS | Brasil | 3107406 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 1ea3e552-40bc-3762-8ed7-962d61839326 | -12.23247 | -45.51047 | 2024-09-26 04:08:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| fc388ea3-5bf9-3777-991b-952d34f229dc | -12.2318 | -45.51453 | 2024-09-26 04:08:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 6bfd55a9-5763-3535-9f1d-f38ff22bb701 | -12.23113 | -45.5186 | 2024-09-26 04:08:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 585d84b8-66ee-3d4e-9d67-5c9312545ac5 | -12.23094 | -45.49769 | 2024-09-26 04:08:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 015b5cb2-8679-37b9-8cd8-26ae04b5fd27 | -12.23027 | -45.50174 | 2024-09-26 04:08:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| de3bf2c4-7acd-3b5c-802c-616674aa62df | -12.22979 | -45.52674 | 2024-09-26 04:08:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| fefd82ba-e53e-303c-b56b-d310fd123fff | -12.2296 | -45.50579 | 2024-09-26 04:08:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 5479ed94-5855-3b3c-a7b6-14787245fb93 | -12.22741 | -45.49708 | 2024-09-26 04:08:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 12.5 |
| 663d394c-ea5f-3b6c-80b6-ba8ec56bddfe | -12.22692 | -45.52206 | 2024-09-26 04:08:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 96285f7c-cf94-3fb8-bcab-4ed6250d9b5c | -12.22674 | -45.50112 | 2024-09-26 04:08:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 12.5 |
| c0234e3f-391f-37ce-b369-8785fe311541 | -12.22624 | -45.52612 | 2024-09-26 04:08:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 129606ba-3381-309c-87e0-346463457501 | -12.22607 | -45.50518 | 2024-09-26 04:08:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 14.1 |
| b46f80fd-f7f4-3fd2-ab38-65f41e97d9ff | -12.22557 | -45.5302 | 2024-09-26 04:08:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 53f84013-8797-33ae-b909-d05a6fd519ec | -12.22539 | -45.50924 | 2024-09-26 04:08:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 14.1 |
| 0cc6390a-7149-3fd0-b426-b60c23f0d7f1 | -12.22472 | -45.51331 | 2024-09-26 04:08:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 47.1 |
| 25aa3607-91f4-3f38-9c84-29d2ca56fd40 | -12.22405 | -45.51738 | 2024-09-26 04:08:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 47.1 |
| 55993d00-21f8-37e4-93af-44bdfcf45b65 | -12.22338 | -45.52145 | 2024-09-26 04:08:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 53.1 |
| 27fef61c-b685-3b44-b023-2b5d6dcad72b | -12.2232 | -45.50051 | 2024-09-26 04:08:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 12.5 |
| 93095b97-ae72-3e10-900f-06029b251e72 | -12.2227 | -45.52551 | 2024-09-26 04:08:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 53.1 |
| 53ae5373-c38e-3df3-a18a-533654955cb5 | -12.22253 | -45.50457 | 2024-09-26 04:08:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 14.1 |
| 3cefd861-6dcc-3fd3-93a1-7085377f4ef6 | -12.22118 | -45.5127 | 2024-09-26 04:08:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 47.1 |
| 6ac719af-cee9-39b2-9fb5-8a1cd8e67c04 | -12.22051 | -45.51677 | 2024-09-26 04:08:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 47.1 |
| c092f5f5-b1be-3f91-8cd4-b45957a0af57 | -12.21984 | -45.52084 | 2024-09-26 04:08:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 53.1 |
| dc68df06-b4e1-3151-ae7d-6cefb7afbe0f | -12.21916 | -45.5249 | 2024-09-26 04:08:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 53.1 |
| 18fa1d89-f688-3c35-9396-33017317e6f8 | -12.21629 | -45.52023 | 2024-09-26 04:08:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a70792e6-a126-35df-b59c-5400a6cbad12 | -12.21343 | -45.51556 | 2024-09-26 04:08:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 3c039aad-59da-38ac-adfd-07876b0ba625 | -13.33463 | -46.30371 | 2024-09-26 04:08:00 | NOAA-20 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| f44b5db1-9bd5-3858-b4a9-2729b1a3f8a1 | -13.33379 | -46.33043 | 2024-09-26 04:08:00 | NOAA-20 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 116e964c-3888-3701-bbb4-42b25b5d1205 | -13.33305 | -46.33475 | 2024-09-26 04:08:00 | NOAA-20 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 9d34d64c-699b-3c13-b820-2682acef9ab3 | -13.33178 | -46.29855 | 2024-09-26 04:08:00 | NOAA-20 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 575af007-5ff5-3b6f-ade6-4fa7c397025d | -13.33101 | -46.30302 | 2024-09-26 04:08:00 | NOAA-20 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 4de4ea97-8478-3603-b6ef-3c0885849ff5 | -13.32818 | -46.29776 | 2024-09-26 04:08:00 | NOAA-20 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 11373e88-b342-3085-80b9-9083bb15e505 | -13.32741 | -46.30224 | 2024-09-26 04:08:00 | NOAA-20 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 88a598d1-bdb2-33f7-a4c6-a6ca3a797743 | -13.32505 | -46.33776 | 2024-09-26 04:08:00 | NOAA-20 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 9df1d550-8cec-3082-bac9-bec02b6eaa22 | -13.32431 | -46.34208 | 2024-09-26 04:08:00 | NOAA-20 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 882fd389-f009-37da-97e5-5367b8c69113 | -13.32306 | -46.3058 | 2024-09-26 04:08:00 | NOAA-20 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| f9c7a442-db1d-3722-9a19-911d031d9a89 | -13.32142 | -46.33709 | 2024-09-26 04:08:00 | NOAA-20 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| e489dae5-f73f-32e0-b1d1-af1cd42362db | -13.32068 | -46.34142 | 2024-09-26 04:08:00 | NOAA-20 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 7d2a1e27-6126-3484-bfa3-53cc6e6950c2 | -13.31948 | -46.30487 | 2024-09-26 04:08:00 | NOAA-20 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 5e894e76-c963-34e5-89a0-3b512ee89ca2 | -13.31873 | -46.30926 | 2024-09-26 04:08:00 | NOAA-20 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| d2c85108-64fa-345b-a049-7ef832c5bf81 | -13.31779 | -46.33641 | 2024-09-26 04:08:00 | NOAA-20 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |


[Clique aqui para ver as próximas entradas](README72.md)
