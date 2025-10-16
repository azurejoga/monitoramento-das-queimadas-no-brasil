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

## Dados Diários - Página 19

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 5129f753-0258-3947-86fd-f97d1ea551ec | -4.3685 | -43.4071 | 2025-10-16 03:30:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 305.0 |
| 0b69cc83-288b-35d3-a2ea-fd85a09b24f2 | -4.0976 | -48.0144 | 2025-10-16 03:30:00 | GOES-19 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 168.0 |
| e3d81dec-433e-378f-a7c9-7e8f74cf9553 | -6.3733 | -41.4828 | 2025-10-16 03:30:00 | GOES-19 | LAGOA DO SÍTIO | PIAUÍ | Brasil | 2205599 | 22 | 33 | nan | nan | nan | Caatinga | 148.5 |
| 21765ca9-66fe-3e36-8d8f-4ae20b9d587f | -4.0974 | -48.0361 | 2025-10-16 03:30:00 | GOES-19 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 125.4 |
| 5069c7e3-c3b5-3e28-9eeb-13cf6ca0bd41 | -15.59455 | -42.3972 | 2025-10-16 03:30:00 | NPP-375D | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Cerrado | 4.3 |
| c5efa3dc-0123-35d0-acd6-a553e9449860 | -15.57528 | -42.37677 | 2025-10-16 03:30:00 | NPP-375D | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| aa189af4-b682-3164-8dfd-6067357c3097 | -15.78839 | -43.65232 | 2025-10-16 03:30:00 | NPP-375D | CAPITÃO ENÉAS | MINAS GERAIS | Brasil | 3112703 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| de580e1f-20fc-34a6-bd3a-8997c2e33f20 | -15.97056 | -43.01974 | 2025-10-16 03:30:00 | NPP-375D | RIACHO DOS MACHADOS | MINAS GERAIS | Brasil | 3154507 | 31 | 33 | nan | nan | nan | Cerrado | 6.3 |
| f68831b7-6eca-3ba8-af81-fe7cffbfb52a | -15.96254 | -43.0179 | 2025-10-16 03:30:00 | NPP-375D | RIACHO DOS MACHADOS | MINAS GERAIS | Brasil | 3154507 | 31 | 33 | nan | nan | nan | Cerrado | 5.6 |
| f81cda61-611c-320d-90c3-276aa1a3ea80 | -17.93753 | -46.73222 | 2025-10-16 03:30:00 | NPP-375D | LAGAMAR | MINAS GERAIS | Brasil | 3137106 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 88d4b2ce-b70a-343a-b416-83e025a6933e | -18.44902 | -44.48796 | 2025-10-16 03:30:00 | NPP-375D | CORINTO | MINAS GERAIS | Brasil | 3119104 | 31 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 49530360-d2af-34b3-8723-e3bbc300e044 | -15.5938 | -42.40084 | 2025-10-16 03:30:00 | NPP-375D | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 9c58dc8a-b306-3a98-adf4-7af51281db0b | -15.80048 | -42.02752 | 2025-10-16 03:30:00 | NPP-375D | TAIOBEIRAS | MINAS GERAIS | Brasil | 3168002 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 33045cb0-2914-32f6-8ed9-7ace0c46ec5b | -15.80118 | -42.02403 | 2025-10-16 03:30:00 | NPP-375D | TAIOBEIRAS | MINAS GERAIS | Brasil | 3168002 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 5a070660-a847-3d32-bde1-0e2cc141c8b7 | -17.93072 | -46.73114 | 2025-10-16 03:30:00 | NPP-375D | LAGAMAR | MINAS GERAIS | Brasil | 3137106 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| f96fbef6-7ebc-38f9-aeee-bf7aca323e74 | -19.07378 | -46.82826 | 2025-10-16 03:30:00 | NPP-375D | PATROCÍNIO | MINAS GERAIS | Brasil | 3148103 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 4a052211-3e9f-3f8c-bf73-b0e1a7e6d3ad | -15.96493 | -43.0187 | 2025-10-16 03:30:00 | NPP-375D | RIACHO DOS MACHADOS | MINAS GERAIS | Brasil | 3154507 | 31 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 80a88089-a5e4-3cb9-83b2-83aef5e3fcbc | -15.57576 | -42.37864 | 2025-10-16 03:30:00 | NPP-375D | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 0617e9df-f136-34d0-b93a-95cda548f86d | -15.57924 | -42.38522 | 2025-10-16 03:30:00 | NPP-375D | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| ce0ce2dd-0913-3b02-adbf-892e7135ab84 | -15.78259 | -43.65084 | 2025-10-16 03:30:00 | NPP-375D | CAPITÃO ENÉAS | MINAS GERAIS | Brasil | 3112703 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e67ac713-f7ed-3eb8-a16c-637212598d51 | -15.7817 | -43.65503 | 2025-10-16 03:30:00 | NPP-375D | SÃO JOÃO DA PONTE | MINAS GERAIS | Brasil | 3162401 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 161f4aa4-9e7c-3c0a-b9c6-56be76c42159 | -15.57649 | -42.37513 | 2025-10-16 03:30:00 | NPP-375D | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 06893d66-11e9-3e38-bd22-7490a6d3a67a | -15.96817 | -43.01897 | 2025-10-16 03:30:00 | NPP-375D | RIACHO DOS MACHADOS | MINAS GERAIS | Brasil | 3154507 | 31 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 3007b001-db93-3aa1-818d-a40a26af8b91 | -15.59226 | -42.4083 | 2025-10-16 03:30:00 | NPP-375D | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 336320c2-0314-3fbd-989c-44cccfda5a37 | -15.96739 | -43.02277 | 2025-10-16 03:30:00 | NPP-375D | RIACHO DOS MACHADOS | MINAS GERAIS | Brasil | 3154507 | 31 | 33 | nan | nan | nan | Cerrado | 9.6 |
| c82868dd-4e15-3c09-aaef-1a14e99f78a1 | -15.58042 | -42.38346 | 2025-10-16 03:30:00 | NPP-375D | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a77e9b8b-23e4-3e74-8861-5e4e32e8ffb1 | -15.59305 | -42.4045 | 2025-10-16 03:30:00 | NPP-375D | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 75c0f146-a1c1-3792-8dbe-3f01ba4544ad | -15.58589 | -42.38437 | 2025-10-16 03:30:00 | NPP-375D | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 45ba009d-35ed-3a5e-b169-3c8ab3d8e05c | -19.07513 | -46.82256 | 2025-10-16 03:30:00 | NPP-375D | PATROCÍNIO | MINAS GERAIS | Brasil | 3148103 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 719b63ab-c766-39b9-b335-e6e4b79f6c16 | -15.96412 | -43.02251 | 2025-10-16 03:30:00 | NPP-375D | RIACHO DOS MACHADOS | MINAS GERAIS | Brasil | 3154507 | 31 | 33 | nan | nan | nan | Cerrado | 9.2 |
| b0ab770f-2372-3144-8e77-ae79acf0c9d8 | -20.9542 | -47.41566 | 2025-10-16 03:32:00 | NPP-375D | ALTINÓPOLIS | SÃO PAULO | Brasil | 3501004 | 35 | 33 | nan | nan | nan | Cerrado | 3.4 |
| c6bc1db7-9892-3fa7-b010-669aa365b9b0 | -20.95702 | -47.41574 | 2025-10-16 03:32:00 | NPP-375D | ALTINÓPOLIS | SÃO PAULO | Brasil | 3501004 | 35 | 33 | nan | nan | nan | Cerrado | 8.4 |
| b27b49fd-e398-31db-ba21-e69db92d8d4a | -20.96077 | -47.41727 | 2025-10-16 03:32:00 | NPP-375D | ALTINÓPOLIS | SÃO PAULO | Brasil | 3501004 | 35 | 33 | nan | nan | nan | Cerrado | 3.4 |
| c1c47721-6a13-3318-8a02-c12f55a580a2 | -22.63539 | -47.99263 | 2025-10-16 03:32:00 | NPP-375D | SÃO PEDRO | SÃO PAULO | Brasil | 3550407 | 35 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 561ec82b-c7f7-36f6-af36-ee0e3df96bfc | -29.17595 | -50.12948 | 2025-10-16 03:34:00 | NPP-375D | CAMBARÁ DO SUL | RIO GRANDE DO SUL | Brasil | 4303608 | 43 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 66064a2c-19b6-30e1-9932-46e73a18a292 | -29.17708 | -50.12538 | 2025-10-16 03:34:00 | NPP-375D | CAMBARÁ DO SUL | RIO GRANDE DO SUL | Brasil | 4303608 | 43 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| 409b76ae-7108-3b15-a23d-ffa5d1474c87 | -29.16969 | -50.12718 | 2025-10-16 03:34:00 | NPP-375D | CAMBARÁ DO SUL | RIO GRANDE DO SUL | Brasil | 4303608 | 43 | 33 | nan | nan | nan | Mata Atlântica | 4.0 |
| 182ce064-cd50-3a98-a958-1e3e92b57fac | -29.17082 | -50.12309 | 2025-10-16 03:34:00 | NPP-375D | CAMBARÁ DO SUL | RIO GRANDE DO SUL | Brasil | 4303608 | 43 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| 73a63239-ecaf-3073-bb64-9a4546246546 | -29.18013 | -50.13965 | 2025-10-16 03:34:00 | NPP-375D | CAMBARÁ DO SUL | RIO GRANDE DO SUL | Brasil | 4303608 | 43 | 33 | nan | nan | nan | Mata Atlântica | 3.5 |
| 7e7bcbd6-bed3-3103-9ab0-d459e374c3d1 | -29.17546 | -50.13141 | 2025-10-16 03:34:00 | NPP-375D | CAMBARÁ DO SUL | RIO GRANDE DO SUL | Brasil | 4303608 | 43 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| 08c9d25a-faad-327b-a25b-213990b480aa | -29.1776 | -50.12347 | 2025-10-16 03:34:00 | NPP-375D | CAMBARÁ DO SUL | RIO GRANDE DO SUL | Brasil | 4303608 | 43 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 08b5261b-e68e-3e61-95cb-eb8ae71ae925 | -29.16921 | -50.12906 | 2025-10-16 03:34:00 | NPP-375D | CAMBARÁ DO SUL | RIO GRANDE DO SUL | Brasil | 4303608 | 43 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| de797f82-a6dc-35c9-8457-f983bf8039ef | -4.6813 | -44.082 | 2025-10-16 03:40:00 | GOES-19 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 62.3 |
| 99d10bff-b516-3078-931d-59ed87e7e4cd | 1.8218 | -55.7431 | 2025-10-16 03:40:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 44.7 |
| 9c6e4f8d-e631-3b99-b4ac-5e94166ba0c7 | -6.1532 | -40.9215 | 2025-10-16 03:40:00 | GOES-19 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 106.0 |
| 1d1dc655-5e13-32eb-86fa-b5e07e2cb4a5 | -4.4061 | -43.3816 | 2025-10-16 03:40:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 54.9 |
| 67473571-a8c5-3c19-94a5-a1adbbaf5ccc | -4.6623 | -44.1292 | 2025-10-16 03:40:00 | GOES-19 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 33.9 |
| 77a4f06b-ad7c-396f-8c2e-a71d029dcd12 | -4.0974 | -48.0361 | 2025-10-16 03:40:00 | GOES-19 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 153.1 |
| 1e877c9b-f911-31fe-affd-f74ebcddc36c | -3.0157 | -45.3903 | 2025-10-16 03:40:00 | GOES-19 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 176.4 |
| 409e422e-32bf-3429-81fa-89c7b96b8e19 | -4.6626 | -44.0832 | 2025-10-16 03:40:00 | GOES-19 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 125.5 |
| 313da44c-94ea-3d99-ac28-e9c91bb1ccee | -4.116 | -48.0352 | 2025-10-16 03:40:00 | GOES-19 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 116.9 |
| 7dea8c29-17ed-3b99-bf22-0cc48ea31185 | -5.4762 | -42.9367 | 2025-10-16 03:40:00 | GOES-19 | NAZÁRIA | PIAUÍ | Brasil | 2206720 | 22 | 33 | nan | nan | nan | Caatinga | 41.2 |
| 561f9971-fccc-362b-8a40-10c34ed11c8b | -5.6819 | -45.112 | 2025-10-16 03:40:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 58.9 |
| d44fb4b0-f825-3857-a742-cd360e2cdc8a | -4.6437 | -44.1073 | 2025-10-16 03:40:00 | GOES-19 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 38.1 |
| d96fcc6b-ac9e-3de3-8162-2ca0f3bc2e94 | -8.4528 | -44.1767 | 2025-10-16 03:40:00 | GOES-19 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 87.4 |
| 8e4513fb-2d3d-361e-9030-302867d7d94b | -4.3874 | -43.3827 | 2025-10-16 03:40:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 273.5 |
| 39474d26-265b-30bb-a935-39f9054ff10c | -2.9971 | -45.391 | 2025-10-16 03:40:00 | GOES-19 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 30.6 |
| ce44901e-3179-3b3a-ad16-a3a9edc8c78b | -5.8799 | -43.8844 | 2025-10-16 03:40:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 39.5 |
| 54132044-08ed-3a67-bee2-d8267d5d8e5a | -8.4717 | -44.1746 | 2025-10-16 03:40:00 | GOES-19 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 86.6 |
| eaf7a35c-1977-3192-8955-3d547e3d5016 | -4.3872 | -43.406 | 2025-10-16 03:40:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 385.8 |
| 9ff1c396-5d03-327a-8856-c492979189b3 | -8.4714 | -44.1978 | 2025-10-16 03:40:00 | GOES-19 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 69.1 |
| eb709920-2f70-39d8-98ca-d8e6cfd796f3 | -6.1534 | -40.8971 | 2025-10-16 03:40:00 | GOES-19 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 121.1 |
| 7ac42ad2-0b74-3f82-9124-883c54fc6f20 | -5.8802 | -43.8613 | 2025-10-16 03:40:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 35.6 |
| 4b35f6a2-c027-3a64-9d21-4c384ed38fb7 | -6.1723 | -40.8954 | 2025-10-16 03:40:00 | GOES-19 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 66.2 |
| 78a57fb8-1bdd-3da2-9b94-2a2c49e38b6d | -4.3687 | -43.3838 | 2025-10-16 03:40:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 294.2 |
| ea4c6a5a-5128-33f0-a627-b1326f72f56e | -7.9439 | -44.1381 | 2025-10-16 03:40:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 66.4 |
| 956e6810-5ca4-3918-aef6-222458c411c7 | -6.3733 | -41.4828 | 2025-10-16 03:40:00 | GOES-19 | LAGOA DO SÍTIO | PIAUÍ | Brasil | 2205599 | 22 | 33 | nan | nan | nan | Caatinga | 88.4 |
| 8ebea3a4-c9a5-349e-baeb-b92ec4244b79 | -7.3955 | -39.6845 | 2025-10-16 03:40:00 | GOES-19 | EXU | PERNAMBUCO | Brasil | 2605301 | 26 | 33 | nan | nan | nan | Caatinga | 75.7 |
| e7550ba4-662f-35e1-90df-e0d5072cfceb | -4.4059 | -43.4049 | 2025-10-16 03:40:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 80.7 |
| ab1b371f-cef3-3d6b-a314-a06d7bf6a478 | -4.1161 | -48.0136 | 2025-10-16 03:40:00 | GOES-19 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 114.5 |
| 26bef380-98e1-3aae-9b74-ae26f6749f0c | -4.6624 | -44.1062 | 2025-10-16 03:40:00 | GOES-19 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 205.6 |
| 3e9ca370-05c0-343b-b252-7a46eaa3a756 | -4.0976 | -48.0144 | 2025-10-16 03:40:00 | GOES-19 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 140.9 |
| 003bfd81-6976-3f18-ae2d-bc71986128be | -3.0158 | -45.3679 | 2025-10-16 03:40:00 | GOES-19 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 89.8 |
| b0fb04cd-f417-3bee-b9a6-17b2d73cb70f | -4.6811 | -44.105 | 2025-10-16 03:40:00 | GOES-19 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 94.5 |
| 0d82a952-ba6a-3f70-9098-385b30e4bb13 | -5.6821 | -45.0893 | 2025-10-16 03:40:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 64.0 |
| 7b65ace5-78a7-3cd5-a52c-02af80559a43 | -4.3685 | -43.4071 | 2025-10-16 03:40:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 357.2 |
| 5c0fc76d-3797-3707-91cd-35a891f4203a | -6.172 | -40.9198 | 2025-10-16 03:40:00 | GOES-19 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 57.0 |
| 0fa50b9d-a411-3507-8060-17d4e618f1cb | -11.43486 | -44.15036 | 2025-10-16 03:47:00 | NOAA-20 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 770ffdc5-16ed-3705-9f01-ce5c107bb763 | -4.36736 | -43.38659 | 2025-10-16 03:47:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 8.3 |
| bf7ad00e-8a4d-3de2-bd1c-6771aa2713b7 | -6.10035 | -40.88682 | 2025-10-16 03:47:00 | NOAA-20 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 19.3 |
| 13c5f28c-9c0c-309c-a848-1d79208ba142 | -11.44775 | -44.05471 | 2025-10-16 03:47:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 4c68ecc0-cefe-3da8-9420-8294d6ffe01c | -10.33711 | -47.77474 | 2025-10-16 03:47:00 | NOAA-20 | SANTA TEREZA DO TOCANTINS | TOCANTINS | Brasil | 1719004 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 1a89ffa0-5594-3130-af8c-70146026c0b4 | -10.61276 | -45.24105 | 2025-10-16 03:47:00 | NOAA-20 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| fd8dbe51-65d9-33d0-b4d4-3b30ddef409a | -4.65173 | -44.09373 | 2025-10-16 03:47:00 | NOAA-20 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 1e64dc51-906d-3b18-97dd-4551e21489b9 | -11.7017 | -44.27865 | 2025-10-16 03:47:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 492863cc-edd2-33bc-af18-5a1f0348f34d | -6.06573 | -41.89907 | 2025-10-16 03:47:00 | NOAA-20 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 06b58b83-5b20-3f3e-b3e2-de31687d4c34 | -9.22653 | -48.60154 | 2025-10-16 03:47:00 | NOAA-20 | MIRANORTE | TOCANTINS | Brasil | 1713304 | 17 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 4898c622-da36-3ae8-88a8-512b8ddbd3fc | -9.36751 | -46.95571 | 2025-10-16 03:47:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 8fd980f1-788b-37ca-9a69-695d690b99dc | -4.65664 | -44.09453 | 2025-10-16 03:47:00 | NOAA-20 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 51b3ee70-21fd-3ff2-8fd9-e09531cf96c9 | -9.21951 | -48.60518 | 2025-10-16 03:47:00 | NOAA-20 | MIRANORTE | TOCANTINS | Brasil | 1713304 | 17 | 33 | nan | nan | nan | Cerrado | 5.7 |
| bd0eabf3-366f-3cfd-85d7-d8bfca3f6bc1 | -3.84775 | -41.59119 | 2025-10-16 03:47:00 | NOAA-20 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 2d5ba40a-51a9-31d3-b745-a4f9032429af | -10.12758 | -44.58543 | 2025-10-16 03:47:00 | NOAA-20 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 10.9 |
| abe69244-c258-3dc0-bb0c-1b846074e91c | -9.69264 | -44.51916 | 2025-10-16 03:47:00 | NOAA-20 | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 557b545a-9001-38d8-9e5e-dafd3819a1d6 | -6.06288 | -41.8909 | 2025-10-16 03:47:00 | NOAA-20 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| dee644f2-e18b-3482-9528-f07e12944c43 | -12.169 | -45.06557 | 2025-10-16 03:47:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 63428121-45f3-3d43-9d5d-a269ef2ac1c6 | -4.11204 | -48.0173 | 2025-10-16 03:47:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 14.7 |
| f97943bd-dcf7-3291-9adc-28f8b7fda3f2 | -6.13423 | -41.76829 | 2025-10-16 03:47:00 | NOAA-20 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 3fefb1d3-20be-3a34-8fa7-5cb8e0052345 | -11.57365 | -44.0596 | 2025-10-16 03:47:00 | NOAA-20 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 25662ba3-675a-3833-a8a8-6947326884f3 | -6.46826 | -41.84266 | 2025-10-16 03:47:00 | NOAA-20 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| e5f91206-121c-3948-a91c-a38c643b5583 | -5.35343 | -43.75039 | 2025-10-16 03:47:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |


[Clique aqui para ver as próximas entradas](README20.md)
