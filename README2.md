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
| 9ea5c82c-555c-35de-9bf9-a7de2c7dea54 | -4.55937 | -45.64686 | 2024-11-18 00:05:00 | TERRA_M-M | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Cerrado | 24.6 |
| f9b1606e-ffb8-358c-a38f-f4a83e5b0bf1 | -3.16109 | -46.58493 | 2024-11-18 00:05:00 | TERRA_M-M | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 29.1 |
| 951475c6-0e21-3baa-b565-010fd869fc86 | -6.53608 | -35.1927 | 2024-11-18 00:05:00 | TERRA_M-M | PEDRO VELHO | RIO GRANDE DO NORTE | Brasil | 2409803 | 24 | 33 | nan | nan | nan | Mata Atlântica | 9.2 |
| 7747f083-ce3e-30ae-9f28-271b12969131 | -8.13015 | -35.13284 | 2024-11-18 00:05:00 | TERRA_M-M | MORENO | PERNAMBUCO | Brasil | 2609402 | 26 | 33 | nan | nan | nan | Mata Atlântica | 3.9 |
| fb5ff6dd-95b6-3b70-bb30-84cd9d03dcf6 | -3.74823 | -45.94875 | 2024-11-18 00:05:00 | TERRA_M-M | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 29.1 |
| 6123c4c8-7dbf-3355-932c-8c304e3efa94 | -8.14779 | -35.19418 | 2024-11-18 00:05:00 | TERRA_M-M | MORENO | PERNAMBUCO | Brasil | 2609402 | 26 | 33 | nan | nan | nan | Mata Atlântica | 4.1 |
| 5c0b60b2-0052-3d1b-809f-b5a6e11e9260 | -10.02846 | -36.40715 | 2024-11-18 00:05:00 | TERRA_M-M | TEOTÔNIO VILELA | ALAGOAS | Brasil | 2709152 | 27 | 33 | nan | nan | nan | Mata Atlântica | 7.4 |
| dca03d5f-1fe7-3c93-a1ce-7d124a03b630 | -7.40495 | -42.75504 | 2024-11-18 00:05:00 | TERRA_M-M | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 21.4 |
| 0f0ef355-920a-32d9-8a9c-4f4f643d2a87 | -3.36458 | -45.62265 | 2024-11-18 00:05:00 | TERRA_M-M | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 22.4 |
| 3f78b348-4740-3c36-baa6-c47882d4e7d7 | -3.22544 | -45.54424 | 2024-11-18 00:05:00 | TERRA_M-M | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 35.6 |
| 52fb987e-3422-35cf-ad4e-fd0b44cd355f | -3.23142 | -45.54896 | 2024-11-18 00:05:00 | TERRA_M-M | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | 47.6 |
| 43c543da-e89e-3ef7-bdc0-efa08cf91747 | -10.11416 | -36.36082 | 2024-11-18 00:05:00 | TERRA_M-M | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | 27.1 |
| e6d7f9e5-c957-388d-9b94-9851545ff75e | -7.64348 | -35.33374 | 2024-11-18 00:05:00 | TERRA_M-M | VICÊNCIA | PERNAMBUCO | Brasil | 2616308 | 26 | 33 | nan | nan | nan | Caatinga | 4.5 |
| 6d8be851-6926-3536-9a85-f14edd23291f | -5.61798 | -36.87204 | 2024-11-18 00:05:00 | TERRA_M-M | ITAJÁ | RIO GRANDE DO NORTE | Brasil | 2404853 | 24 | 33 | nan | nan | nan | Caatinga | 5.4 |
| cbeabe47-a9fe-37ed-91b1-dcac246557e5 | -3.17457 | -46.58802 | 2024-11-18 00:05:00 | TERRA_M-M | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 35.3 |
| 93a6b9fc-9dff-3366-af58-a2944df5eddd | -4.16542 | -43.91661 | 2024-11-18 00:05:00 | TERRA_M-M | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 17.4 |
| 86a6be73-0810-3f02-83b7-e86b742b6ca7 | -3.35796 | -45.61724 | 2024-11-18 00:05:00 | TERRA_M-M | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 35.9 |
| 8ba196f7-25c2-3648-90a0-b9df2f5ee807 | -8.12889 | -35.1239 | 2024-11-18 00:05:00 | TERRA_M-M | MORENO | PERNAMBUCO | Brasil | 2609402 | 26 | 33 | nan | nan | nan | Mata Atlântica | 5.4 |
| 9f3d9bbf-842a-3a21-8e21-a5774e7588bf | -3.05104 | -44.34443 | 2024-11-18 00:05:00 | TERRA_M-M | BACABEIRA | MARANHÃO | Brasil | 2101251 | 21 | 33 | nan | nan | nan | Amazônia | 18.5 |
| c7a8715b-220b-373d-832b-7ed917bf38c9 | -4.21017 | -44.03581 | 2024-11-18 00:05:00 | TERRA_M-M | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 18.1 |
| a42351b3-b1d9-368d-9a56-6602b5ba15b4 | -4.5755 | -45.64435 | 2024-11-18 00:05:00 | TERRA_M-M | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Cerrado | 76.3 |
| 61e0dd17-6901-36ff-996a-28cbb244cd35 | -2.17446 | -46.40862 | 2024-11-18 00:07:00 | TERRA_M-M | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 39.9 |
| 75570188-8289-3eb4-b01c-16aa91b82807 | -2.18222 | -45.78816 | 2024-11-18 00:07:00 | TERRA_M-M | MARANHÃOZINHO | MARANHÃO | Brasil | 2106375 | 21 | 33 | nan | nan | nan | Amazônia | 22.7 |
| dae9e599-a06f-3796-b61c-0ce0f6e5eb61 | -2.16975 | -46.37327 | 2024-11-18 00:07:00 | TERRA_M-M | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 23.9 |
| c71684a3-9b30-338d-872c-63996d0c8e96 | -2.69268 | -45.72103 | 2024-11-18 00:07:00 | TERRA_M-M | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | 173.4 |
| b8f60e3a-58ab-3ef6-a3a5-151c94c33ce9 | -2.68227 | -45.68488 | 2024-11-18 00:07:00 | TERRA_M-M | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | 68.6 |
| 7776f096-cab2-361e-b9e8-74e7caedaf95 | -2.68832 | -45.68929 | 2024-11-18 00:07:00 | TERRA_M-M | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | 132.4 |
| 47bbab56-6c2b-32df-9597-61ebfaa3106e | -2.12535 | -45.36283 | 2024-11-18 00:07:00 | TERRA_M-M | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 32.6 |
| 63823672-65d1-30e7-a91e-fbe1d93fb4ec | -2.12413 | -45.33831 | 2024-11-18 00:07:00 | TERRA_M-M | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 21.5 |
| 185662c6-41a6-3189-8c27-f07455940be3 | -1.71978 | -45.84891 | 2024-11-18 00:07:00 | TERRA_M-M | CÂNDIDO MENDES | MARANHÃO | Brasil | 2102606 | 21 | 33 | nan | nan | nan | Amazônia | 32.6 |
| 7b4c0141-9f06-35c3-9039-590e8a491c29 | -1.70532 | -45.82523 | 2024-11-18 00:07:00 | TERRA_M-M | CÂNDIDO MENDES | MARANHÃO | Brasil | 2102606 | 21 | 33 | nan | nan | nan | Amazônia | 175.8 |
| c641d009-9806-3793-9df2-2931a4cb8a72 | -1.69988 | -45.81944 | 2024-11-18 00:07:00 | TERRA_M-M | CÂNDIDO MENDES | MARANHÃO | Brasil | 2102606 | 21 | 33 | nan | nan | nan | Amazônia | 84.1 |
| cd046126-77c2-3523-ab12-428ae0dfa5a3 | -1.70976 | -45.8569 | 2024-11-18 00:07:00 | TERRA_M-M | AMAPÁ DO MARANHÃO | MARANHÃO | Brasil | 2100550 | 21 | 33 | nan | nan | nan | Amazônia | 63.1 |
| fde88c3d-e476-3630-9a09-af256e46c6b5 | -2.23381 | -46.47326 | 2024-11-18 00:07:00 | TERRA_M-M | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 30.1 |
| 3233bb2c-d173-3cf3-ad9e-1b0c91e13914 | -1.70408 | -45.85118 | 2024-11-18 00:07:00 | TERRA_M-M | CÂNDIDO MENDES | MARANHÃO | Brasil | 2102606 | 21 | 33 | nan | nan | nan | Amazônia | 82.1 |
| 0f6e91bd-b566-3453-b118-93312d26ede4 | -1.71556 | -45.81731 | 2024-11-18 00:07:00 | TERRA_M-M | CÂNDIDO MENDES | MARANHÃO | Brasil | 2102606 | 21 | 33 | nan | nan | nan | Amazônia | 42.4 |
| 1886278b-bb8a-3134-9d93-a0fe176d2d3a | -2.68638 | -45.71659 | 2024-11-18 00:07:00 | TERRA_M-M | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | 227.1 |
| 97d8ba9a-c13d-33ad-a6ab-89b3f838f4d6 | -2.18836 | -45.79223 | 2024-11-18 00:07:00 | TERRA_M-M | MARANHÃOZINHO | MARANHÃO | Brasil | 2106375 | 21 | 33 | nan | nan | nan | Amazônia | 25.6 |
| 5ef4b38d-8ccb-3193-9271-2e8fdfd76c81 | -2.12824 | -45.36737 | 2024-11-18 00:07:00 | TERRA_M-M | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 23.3 |
| 28265d8e-5c61-3cef-9230-059956de7a24 | -3.04 | -44.3475 | 2024-11-18 00:09:00 | METOP-C | BACABEIRA | MARANHÃO | Brasil | 2101251 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 6b1b663d-5158-3a27-816e-bfa400ad1873 | -2.0887 | -46.2733 | 2024-11-18 00:09:00 | METOP-C | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 16f00f77-4bd1-3028-a5a5-65c63eb1a22d | -2.741 | -52.57 | 2024-11-18 00:09:00 | METOP-C | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 030a0c6d-81b3-3d5f-a02b-a6cc06b56fe3 | -1.6885 | -45.822102 | 2024-11-18 00:09:00 | METOP-C | CÂNDIDO MENDES | MARANHÃO | Brasil | 2102606 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| b9fe9de7-3295-3454-b744-4012f18a69ba | -4.7676 | -46.478298 | 2024-11-18 00:09:00 | METOP-C | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| b7a0eafc-9bcf-3a43-95d5-d556d297f019 | -5.2555 | -44.053902 | 2024-11-18 00:09:00 | METOP-C | SENADOR ALEXANDRE COSTA | MARANHÃO | Brasil | 2111748 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 9d38aeda-e9dc-3c60-b90d-cc39116a0f65 | -6.8191 | -42.260601 | 2024-11-18 00:09:00 | METOP-C | SANTA ROSA DO PIAUÍ | PIAUÍ | Brasil | 2209377 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 3426bd17-f318-3086-a4b5-d7499558495e | -2.6634 | -46.183201 | 2024-11-18 00:09:00 | METOP-C | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 03ae489e-b363-391a-a447-cde31b45c8a7 | -5.3388 | -40.9006 | 2024-11-18 00:09:00 | METOP-C | CRATEÚS | CEARÁ | Brasil | 2304103 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| f6a3ef1a-8170-3dd3-8068-481d8d4973b6 | -6.2048 | -43.2878 | 2024-11-18 00:09:00 | METOP-C | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 1aa43d28-e32c-3839-86a9-dcf7c16c82f6 | -3.2168 | -45.542198 | 2024-11-18 00:09:00 | METOP-C | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 742504b6-f01e-3ec7-8946-b19846e531d6 | -3.1712 | -45.430901 | 2024-11-18 00:09:00 | METOP-C | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 99ed498f-e832-3147-b132-e8c7af5a076b | -2.86 | -51.790699 | 2024-11-18 00:09:00 | METOP-C | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 067d7903-5bc9-30f6-9e01-f0f372d35dd8 | -9.291 | -46.2131 | 2024-11-18 00:09:00 | METOP-C | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 613b695a-6433-394a-b5fc-174ee6f3b97e | -4.564 | -45.6511 | 2024-11-18 00:09:00 | METOP-C | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 2da4dbee-35f0-3823-9377-834433a860f8 | -2.2779 | -46.066502 | 2024-11-18 00:09:00 | METOP-C | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 79afefb8-e7b1-335e-a3fe-dfb6985c7233 | -3.7835 | -46.011799 | 2024-11-18 00:09:00 | METOP-C | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| cefbd132-d27d-3eda-aed0-88622cb65aa8 | -7.1811 | -39.122799 | 2024-11-18 00:09:00 | METOP-C | MISSÃO VELHA | CEARÁ | Brasil | 2308401 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| 14b60e5c-2361-39ca-89af-f9bb5328ff57 | -2.1661 | -46.389 | 2024-11-18 00:09:00 | METOP-C | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 689aaefc-9697-31e4-b564-13df9ceccc00 | -2.6883 | -45.7024 | 2024-11-18 00:09:00 | METOP-C | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 0739311e-3ce8-3072-8ed5-05276c2d7889 | -7.3975 | -38.986698 | 2024-11-18 00:09:00 | METOP-C | ABAIARA | CEARÁ | Brasil | 2300101 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| 51a5170e-5e66-3975-ae78-8a0c37948e77 | -4.7774 | -46.4762 | 2024-11-18 00:09:00 | METOP-C | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 47b58bc6-0092-3536-a469-4998a7f731f4 | -2.6711 | -46.217701 | 2024-11-18 00:09:00 | METOP-C | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 88cdbbf1-5a0e-38cd-b759-348bfb02bb18 | -6.8564 | -38.877102 | 2024-11-18 00:09:00 | METOP-C | LAVRAS DA MANGABEIRA | CEARÁ | Brasil | 2307502 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| 7fcf2c1a-e78b-32a8-8a35-888e81e93ea0 | -2.8474 | -51.734501 | 2024-11-18 00:09:00 | METOP-C | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 08b026fa-15f4-35ac-9ecb-a178b16937cc | -3.7511 | -45.958302 | 2024-11-18 00:09:00 | METOP-C | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 5d9e0fd7-9e33-3162-a80f-f09cf1b92a75 | -2.6732 | -46.181099 | 2024-11-18 00:09:00 | METOP-C | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 0ae359c8-46b0-3dfd-af67-c70b72580b11 | -4.5517 | -45.641899 | 2024-11-18 00:09:00 | METOP-C | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| b1e3756f-9f82-3acc-b02d-005f5bafb61b | -5.1376 | -44.354801 | 2024-11-18 00:09:00 | METOP-C | PRESIDENTE DUTRA | MARANHÃO | Brasil | 2109106 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 01c7038b-667e-3fbb-9e67-606e07fbe0b2 | -2.8441 | -51.764599 | 2024-11-18 00:09:00 | METOP-C | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3861f445-38d2-39cc-a6c2-8769480503d8 | -6.858 | -38.883999 | 2024-11-18 00:09:00 | METOP-C | AURORA | CEARÁ | Brasil | 2301703 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| be11cbfd-19c8-3452-b2dd-8b8d285bb17c | -1.6983 | -45.82 | 2024-11-18 00:09:00 | METOP-C | CÂNDIDO MENDES | MARANHÃO | Brasil | 2102606 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 5668f284-07a6-3b23-b75c-31cf38da91c4 | -4.2915 | -46.7309 | 2024-11-18 00:09:00 | METOP-C | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 2b3f0b4e-506f-377d-b7da-4cdfa922dc45 | -6.331 | -39.689602 | 2024-11-18 00:09:00 | METOP-C | JUCÁS | CEARÁ | Brasil | 2307403 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| 25959535-107f-3ab3-88f7-55fac03c9671 | -10.1 | -36.353001 | 2024-11-18 00:09:00 | METOP-C | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | nan |
| da81b263-64f7-3fad-8fe7-20938cc62997 | -5.4808 | -43.2673 | 2024-11-18 00:09:00 | METOP-C | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 59d502c8-098e-3ccb-a25b-23ac940c732c | -5.5374 | -43.290298 | 2024-11-18 00:09:00 | METOP-C | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| e46b26ea-2e1f-37e9-b839-7faefb0328c2 | -4.8005 | -42.208302 | 2024-11-18 00:09:00 | METOP-C | CAMPO MAIOR | PIAUÍ | Brasil | 2202208 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 426ab960-9a44-3883-a998-7077b94ffa6e | -3.346 | -45.615002 | 2024-11-18 00:09:00 | METOP-C | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| f57c44d0-713c-3fbb-959e-2f7f4db87878 | -3.3205 | -46.003899 | 2024-11-18 00:09:00 | METOP-C | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 95db6bdf-dde3-33c4-8569-bb47a518dfba | -3.2759 | -46.170898 | 2024-11-18 00:09:00 | METOP-C | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| aa75f226-f4db-3e58-aa83-4713db14c9d3 | -4.2945 | -46.744099 | 2024-11-18 00:09:00 | METOP-C | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 59e056cb-9bfa-373c-91a8-2a4e4cf0cd53 | -4.6776 | -41.1208 | 2024-11-18 00:09:00 | METOP-C | PORANGA | CEARÁ | Brasil | 2311009 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| ed437a51-90a5-36ac-a18c-9abf555ae7da | -2.6119 | -48.547401 | 2024-11-18 00:09:00 | METOP-C | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 89e08eb8-8d3e-367c-93e7-7725d4532c2c | -2.6786 | -45.704601 | 2024-11-18 00:09:00 | METOP-C | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 0f46bcfe-38f5-33c0-9ddb-b3523bd42089 | -2.6354 | -46.832699 | 2024-11-18 00:09:00 | METOP-C | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| cdab20f7-6250-38a9-8d8b-20267792f4ea | -2.6608 | -46.171799 | 2024-11-18 00:09:00 | METOP-C | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| b52d01d6-0eb0-3e7b-b99c-592186912e6e | -3.085 | -45.9603 | 2024-11-18 00:09:00 | METOP-C | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 079d7679-079a-3347-b18f-68918a3047a2 | -2.2238 | -46.4622 | 2024-11-18 00:09:00 | METOP-C | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d77005ad-69c7-333b-9542-0c65d290ebc6 | -1.2871 | -51.732498 | 2024-11-18 00:09:00 | METOP-C | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f16c5f26-eced-3df0-82d4-f7f7026fbdd7 | -3.2885 | -42.899101 | 2024-11-18 00:09:00 | METOP-C | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 4c388340-05aa-305c-8849-38baff55f6f3 | -7.1795 | -39.115898 | 2024-11-18 00:09:00 | METOP-C | MISSÃO VELHA | CEARÁ | Brasil | 2308401 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| 8597ad3f-cccd-33aa-9c67-dc29f0e6e1df | -2.1066 | -46.487999 | 2024-11-18 00:09:00 | METOP-C | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| fd276375-f9a3-315e-9214-ac516c6b14e1 | -2.7385 | -52.604 | 2024-11-18 00:09:00 | METOP-C | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| cfe6fd54-5c67-32f2-9dc4-3fc813e7894a | -5.3075 | -44.287899 | 2024-11-18 00:09:00 | METOP-C | GONÇALVES DIAS | MARANHÃO | Brasil | 2104404 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| be7408f2-030c-34b2-aa4c-4b9b6baf3251 | -2.8249 | -46.6731 | 2024-11-18 00:09:00 | METOP-C | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2b94d7e7-01ef-3ac4-9c5f-1aeb02efd319 | -3.2192 | -45.552799 | 2024-11-18 00:09:00 | METOP-C | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| ce6de4f6-5f6b-34e6-9c41-64bb6503fa14 | -7.0497 | -35.208698 | 2024-11-18 00:09:00 | METOP-C | SAPÉ | PARAÍBA | Brasil | 2515302 | 25 | 33 | nan | nan | nan | Mata Atlântica | nan |
| ad16a162-8c4e-3d85-ac1a-882fc96b9ff1 | -1.8899 | -46.4375 | 2024-11-18 00:09:00 | METOP-C | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 32b0bae2-c350-3f78-8490-7cd86ffc2e78 | -4.2037 | -44.036301 | 2024-11-18 00:09:00 | METOP-C | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| df167fc2-639b-39a9-9994-e16441a0bbe0 | -1.7956 | -46.519402 | 2024-11-18 00:09:00 | METOP-C | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | nan |


[Clique aqui para ver as próximas entradas](README3.md)
