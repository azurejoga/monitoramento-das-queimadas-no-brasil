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

## Dados Diários - Página 65

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 26be5bc4-2c8d-30af-a431-ccd4b01bdf08 | -3.33513 | -44.32641 | 2024-10-27 12:32:00 | TERRA_M-T | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Amazônia | 6.8 |
| e3af0baf-4998-3953-bbfa-85785099a0b0 | -3.27948 | -44.70888 | 2024-10-27 12:32:00 | TERRA_M-T | ANAJATUBA | MARANHÃO | Brasil | 2100709 | 21 | 33 | nan | nan | nan | Amazônia | 8.0 |
| 6d4312eb-fc7d-3017-a4c5-58cfd9b1db20 | -3.06773 | -44.32453 | 2024-10-27 12:32:00 | TERRA_M-T | BACABEIRA | MARANHÃO | Brasil | 2101251 | 21 | 33 | nan | nan | nan | Amazônia | 14.1 |
| 46c269a1-f3fe-3522-ad42-2d2d73e7d8b3 | -3.06645 | -44.33339 | 2024-10-27 12:32:00 | TERRA_M-T | BACABEIRA | MARANHÃO | Brasil | 2101251 | 21 | 33 | nan | nan | nan | Amazônia | 51.5 |
| eddd5480-2a9a-3482-8a9d-f202a344cbc3 | -3.02448 | -44.3727 | 2024-10-27 12:32:00 | TERRA_M-T | BACABEIRA | MARANHÃO | Brasil | 2101251 | 21 | 33 | nan | nan | nan | Amazônia | 9.4 |
| a548d5e7-2662-32f3-a150-11dfade283ee | -2.77742 | -45.30646 | 2024-10-27 12:32:00 | TERRA_M-T | PINHEIRO | MARANHÃO | Brasil | 2108603 | 21 | 33 | nan | nan | nan | Amazônia | 16.1 |
| b2009f19-33f5-3256-91c2-9d1cd045fb46 | -2.77607 | -45.31584 | 2024-10-27 12:32:00 | TERRA_M-T | PINHEIRO | MARANHÃO | Brasil | 2108603 | 21 | 33 | nan | nan | nan | Amazônia | 29.6 |
| cca2c42d-d043-3fe7-b988-a57aa21a5f74 | -2.46874 | -44.9545 | 2024-10-27 12:32:00 | TERRA_M-T | BEQUIMÃO | MARANHÃO | Brasil | 2101905 | 21 | 33 | nan | nan | nan | Amazônia | 9.4 |
| df256a9b-efcc-3e05-85a9-4bd1c1222525 | -2.46104 | -44.94407 | 2024-10-27 12:32:00 | TERRA_M-T | BEQUIMÃO | MARANHÃO | Brasil | 2101905 | 21 | 33 | nan | nan | nan | Amazônia | 16.6 |
| b72ce063-aaa4-350d-b60e-166140fae0c3 | -2.26201 | -45.42407 | 2024-10-27 12:32:00 | TERRA_M-T | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 43.5 |
| 3f0d6aad-124c-3af6-aa5f-a6cc36238c38 | -1.79129 | -46.3938 | 2024-10-27 12:32:00 | TERRA_M-T | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 14.2 |
| 4fb35df7-57d6-362b-9548-051bd26e988b | -9.77986 | -43.863 | 2024-10-27 12:34:00 | TERRA_M-T | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Cerrado | 5.7 |
| e18cbb91-4def-326d-90bb-698391a3e051 | -9.47241 | -44.60421 | 2024-10-27 12:34:00 | TERRA_M-T | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 9.2 |
| 4fd9e75f-0903-3ac5-a029-4decc75c40be | -9.47112 | -44.61325 | 2024-10-27 12:34:00 | TERRA_M-T | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 17.5 |
| 9200eaf5-8108-3921-9142-c35dcbf2a54e | -9.44568 | -44.465 | 2024-10-27 12:34:00 | TERRA_M-T | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 66.1 |
| 8963edcb-0fdc-30af-9e70-30aa160c9902 | -9.44438 | -44.47407 | 2024-10-27 12:34:00 | TERRA_M-T | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 45.9 |
| 8f5e9bfb-9abe-3da8-af3a-71e567e22be3 | -9.43675 | -44.46372 | 2024-10-27 12:34:00 | TERRA_M-T | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 11.0 |
| 074ba825-a97a-32f6-bf10-52bb8580cc3a | -9.17001 | -40.92379 | 2024-10-27 12:34:00 | TERRA_M-T | CASA NOVA | BAHIA | Brasil | 2907202 | 29 | 33 | nan | nan | nan | Caatinga | 14.0 |
| eee12034-c13e-3850-909b-279f64264a3c | -9.09455 | -45.04607 | 2024-10-27 12:34:00 | TERRA_M-T | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 9.9 |
| 9f6bbbb8-0f94-33dd-a3f9-b8319eb44901 | -9.0857 | -45.04481 | 2024-10-27 12:34:00 | TERRA_M-T | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 13.8 |
| 9f847bf3-c22d-3c5a-9340-74cae2dbcdfc | -9.06987 | -41.06757 | 2024-10-27 12:34:00 | TERRA_M-T | CASA NOVA | BAHIA | Brasil | 2907202 | 29 | 33 | nan | nan | nan | Caatinga | 14.8 |
| 9be45db3-df5b-3217-9811-e0cf3ac892fd | -8.93264 | -40.72156 | 2024-10-27 12:34:00 | TERRA_M-T | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 21.0 |
| 5aaabd84-d72d-3f9d-bb7e-25f17b5936d2 | -8.85781 | -44.39101 | 2024-10-27 12:34:00 | TERRA_M-T | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 7.1 |
| f411d288-2746-3427-9963-083dd69a2d3d | -8.83746 | -40.91072 | 2024-10-27 12:34:00 | TERRA_M-T | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 19.3 |
| 3b94700c-777b-340c-bda2-b0450e52bf1b | -8.74449 | -40.83802 | 2024-10-27 12:34:00 | TERRA_M-T | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 37.1 |
| aa09f1b3-f48a-3f40-839c-e572f8da6852 | -8.74268 | -40.85136 | 2024-10-27 12:34:00 | TERRA_M-T | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 23.3 |
| 826e5a7a-0916-3cfd-bb23-a207a7c13d93 | -8.73967 | -40.99226 | 2024-10-27 12:34:00 | TERRA_M-T | AFRÂNIO | PERNAMBUCO | Brasil | 2600203 | 26 | 33 | nan | nan | nan | Caatinga | 21.1 |
| 41cc6352-d5f8-3607-8a24-9999ea14ec38 | -8.73795 | -41.0055 | 2024-10-27 12:34:00 | TERRA_M-T | AFRÂNIO | PERNAMBUCO | Brasil | 2600203 | 26 | 33 | nan | nan | nan | Caatinga | 19.0 |
| a3a32549-f018-3d42-a8e1-f95bc9a59028 | -8.73551 | -40.82325 | 2024-10-27 12:34:00 | TERRA_M-T | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 116.3 |
| 4da65d70-02e6-3f44-8191-36dbb6971b08 | -8.73354 | -40.99897 | 2024-10-27 12:34:00 | TERRA_M-T | AFRÂNIO | PERNAMBUCO | Brasil | 2600203 | 26 | 33 | nan | nan | nan | Caatinga | 57.2 |
| b06f1399-ca87-3585-9fe5-f266fe1d2c95 | -8.69388 | -42.03912 | 2024-10-27 12:34:00 | TERRA_M-T | DOM INOCÊNCIO | PIAUÍ | Brasil | 2203453 | 22 | 33 | nan | nan | nan | Caatinga | 15.8 |
| d79d273b-943e-3e9f-86ca-559ea64eceaa | -8.61251 | -40.45513 | 2024-10-27 12:34:00 | TERRA_M-T | DORMENTES | PERNAMBUCO | Brasil | 2605152 | 26 | 33 | nan | nan | nan | Caatinga | 28.8 |
| 18812e53-a38e-3232-8c6f-10b48ae178bd | -8.61058 | -40.46948 | 2024-10-27 12:34:00 | TERRA_M-T | DORMENTES | PERNAMBUCO | Brasil | 2605152 | 26 | 33 | nan | nan | nan | Caatinga | 30.6 |
| 5fea24cf-0882-3ad0-a00d-7aa13fb7dd28 | -8.57695 | -40.99876 | 2024-10-27 12:34:00 | TERRA_M-T | AFRÂNIO | PERNAMBUCO | Brasil | 2600203 | 26 | 33 | nan | nan | nan | Caatinga | 152.2 |
| 2ea6e46c-3beb-3982-8340-bf618ff5b4ed | -8.57524 | -41.01176 | 2024-10-27 12:34:00 | TERRA_M-T | AFRÂNIO | PERNAMBUCO | Brasil | 2600203 | 26 | 33 | nan | nan | nan | Caatinga | 194.8 |
| e96d5fb1-28d3-35b9-9b00-8ef521779d25 | -8.57512 | -40.65046 | 2024-10-27 12:34:00 | TERRA_M-T | DORMENTES | PERNAMBUCO | Brasil | 2605152 | 26 | 33 | nan | nan | nan | Caatinga | 21.5 |
| 8cd66920-7cc0-3f88-bec0-6fdffdd044a8 | -8.57327 | -40.66431 | 2024-10-27 12:34:00 | TERRA_M-T | DORMENTES | PERNAMBUCO | Brasil | 2605152 | 26 | 33 | nan | nan | nan | Caatinga | 42.1 |
| 79bd5e03-6504-36b5-8ad7-65bce20e8b60 | -8.53872 | -41.00135 | 2024-10-27 12:34:00 | TERRA_M-T | AFRÂNIO | PERNAMBUCO | Brasil | 2600203 | 26 | 33 | nan | nan | nan | Caatinga | 29.9 |
| b616d8a7-a8ae-351b-a7a0-084f615e5c6c | -8.44599 | -41.37394 | 2024-10-27 12:34:00 | TERRA_M-T | QUEIMADA NOVA | PIAUÍ | Brasil | 2208650 | 22 | 33 | nan | nan | nan | Caatinga | 15.5 |
| f8538941-1d6e-3169-b029-9dd26fdd0096 | -8.44436 | -41.38616 | 2024-10-27 12:34:00 | TERRA_M-T | QUEIMADA NOVA | PIAUÍ | Brasil | 2208650 | 22 | 33 | nan | nan | nan | Caatinga | 11.6 |
| a37c613c-6e2e-3773-83cb-28098c7a57b0 | -8.43674 | -40.58383 | 2024-10-27 12:34:00 | TERRA_M-T | DORMENTES | PERNAMBUCO | Brasil | 2605152 | 26 | 33 | nan | nan | nan | Caatinga | 19.3 |
| 2d1cfcc4-7b52-362f-983b-27d1f75db77b | -8.4329 | -40.59148 | 2024-10-27 12:34:00 | TERRA_M-T | DORMENTES | PERNAMBUCO | Brasil | 2605152 | 26 | 33 | nan | nan | nan | Caatinga | 13.7 |
| 9b6b9164-60bb-3ecc-beed-c2a000d8ad12 | -8.17271 | -43.69897 | 2024-10-27 12:34:00 | TERRA_M-T | COLÔNIA DO GURGUÉIA | PIAUÍ | Brasil | 2202752 | 22 | 33 | nan | nan | nan | Caatinga | 11.5 |
| 36540340-3e8d-3b41-89c2-108cf7460c9b | -8.17139 | -43.70825 | 2024-10-27 12:34:00 | TERRA_M-T | COLÔNIA DO GURGUÉIA | PIAUÍ | Brasil | 2202752 | 22 | 33 | nan | nan | nan | Caatinga | 11.1 |
| cf2de067-61d9-3292-80be-9c69fec223b5 | -8.01653 | -43.43639 | 2024-10-27 12:34:00 | TERRA_M-T | PAVUSSU | PIAUÍ | Brasil | 2207850 | 22 | 33 | nan | nan | nan | Cerrado | 18.0 |
| e2ba28b8-1448-36a0-98fa-5b8a6c857a72 | -8.01446 | -41.62513 | 2024-10-27 12:34:00 | TERRA_M-T | CONCEIÇÃO DO CANINDÉ | PIAUÍ | Brasil | 2202802 | 22 | 33 | nan | nan | nan | Caatinga | 41.0 |
| c31470a5-b79d-3a7f-9458-64a66e133ec7 | -8.01326 | -41.63144 | 2024-10-27 12:34:00 | TERRA_M-T | CONCEIÇÃO DO CANINDÉ | PIAUÍ | Brasil | 2202802 | 22 | 33 | nan | nan | nan | Caatinga | 65.3 |
| 54bb2864-5bb8-38a9-a0d6-aafb01541e44 | -8.01285 | -41.6367 | 2024-10-27 12:34:00 | TERRA_M-T | CONCEIÇÃO DO CANINDÉ | PIAUÍ | Brasil | 2202802 | 22 | 33 | nan | nan | nan | Caatinga | 57.6 |
| 11c2443e-f49f-38f6-9cc7-a4a18099b874 | -7.80507 | -37.10807 | 2024-10-27 12:34:00 | TERRA_M-T | MONTEIRO | PARAÍBA | Brasil | 2509701 | 25 | 33 | nan | nan | nan | Caatinga | 42.6 |
| 8b120148-6d9a-3f1d-8e15-871ec0dcd64b | -7.64819 | -37.85345 | 2024-10-27 12:34:00 | TERRA_M-T | TAVARES | PARAÍBA | Brasil | 2516607 | 25 | 33 | nan | nan | nan | Caatinga | 83.9 |
| 8d4e8bb8-ccec-3b36-9245-9df9c31b279a | -7.64541 | -37.87509 | 2024-10-27 12:34:00 | TERRA_M-T | TAVARES | PARAÍBA | Brasil | 2516607 | 25 | 33 | nan | nan | nan | Caatinga | 26.4 |
| f851d97e-b3ce-381f-a88f-d44af9285c92 | -7.60882 | -39.98964 | 2024-10-27 12:34:00 | TERRA_M-T | BODOCÓ | PERNAMBUCO | Brasil | 2602001 | 26 | 33 | nan | nan | nan | Caatinga | 30.6 |
| 24f84a72-e21a-36d7-89f3-ed8d80a56326 | -7.50287 | -44.07078 | 2024-10-27 12:34:00 | TERRA_M-T | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 12.3 |
| 3fc9f4ac-dd35-3ac7-95b9-2016ea315b93 | -7.46771 | -44.75688 | 2024-10-27 12:34:00 | TERRA_M-T | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 9.8 |
| c208577a-6a9a-323e-bed4-435287980a68 | -7.40609 | -43.77673 | 2024-10-27 12:34:00 | TERRA_M-T | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 14.6 |
| aba2fcd2-d0b0-3d76-84fd-e120d9879ea0 | -7.40478 | -43.78586 | 2024-10-27 12:34:00 | TERRA_M-T | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 2c0bbb57-6691-3501-8653-720f17242fb0 | -7.39711 | -43.77544 | 2024-10-27 12:34:00 | TERRA_M-T | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 13.2 |
| 12d2b3a6-895c-34aa-bef4-d7a80637134f | -7.30403 | -43.6533 | 2024-10-27 12:34:00 | TERRA_M-T | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Caatinga | 16.4 |
| 9579f398-000e-3001-b840-52caa7b479e0 | -7.19673 | -42.9058 | 2024-10-27 12:34:00 | TERRA_M-T | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 10.1 |
| b6d2a8ba-c389-3aa3-b809-cca589633e05 | -6.95114 | -41.33678 | 2024-10-27 12:34:00 | TERRA_M-T | BOCAINA | PIAUÍ | Brasil | 2201804 | 22 | 33 | nan | nan | nan | Caatinga | 34.6 |
| 54a0fafe-6b2c-3d30-b003-25c5b8aae589 | -6.95113 | -41.33118 | 2024-10-27 12:34:00 | TERRA_M-T | BOCAINA | PIAUÍ | Brasil | 2201804 | 22 | 33 | nan | nan | nan | Caatinga | 21.3 |
| 6ff06399-04fb-3edc-b34b-b9279a04d3f2 | -6.68293 | -40.90426 | 2024-10-27 12:34:00 | TERRA_M-T | PIO IX | PIAUÍ | Brasil | 2208205 | 22 | 33 | nan | nan | nan | Caatinga | 31.5 |
| 41ef6592-65a7-3ce4-a31a-3d098bb1ccdc | -6.67254 | -40.90294 | 2024-10-27 12:34:00 | TERRA_M-T | PIO IX | PIAUÍ | Brasil | 2208205 | 22 | 33 | nan | nan | nan | Caatinga | 20.2 |
| bd39ff68-74a2-357f-87b8-738e1d67231b | -6.66864 | -43.39045 | 2024-10-27 12:34:00 | TERRA_M-T | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 12.7 |
| eaeae9b6-92e5-33f5-8458-ec34e3533500 | -6.55284 | -40.50986 | 2024-10-27 12:34:00 | TERRA_M-T | AIUABA | CEARÁ | Brasil | 2300408 | 23 | 33 | nan | nan | nan | Caatinga | 98.7 |
| 6711ecdf-047b-3010-bdd0-3e4f99889447 | -6.55105 | -40.52306 | 2024-10-27 12:34:00 | TERRA_M-T | AIUABA | CEARÁ | Brasil | 2300408 | 23 | 33 | nan | nan | nan | Caatinga | 30.8 |
| 85ea8288-1c61-3206-a814-ff97652b153b | -6.25 | -43.87224 | 2024-10-27 12:34:00 | TERRA_M-T | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 33.6 |
| e54f44ba-9c44-3d9b-b8d8-613104217416 | -15.42351 | -41.0778 | 2024-10-27 12:34:00 | TERRA_M-T | VITÓRIA DA CONQUISTA | BAHIA | Brasil | 2933307 | 29 | 33 | nan | nan | nan | Mata Atlântica | 75.5 |
| 5ddac5bd-76e5-3dd9-a612-dea357e805b7 | -15.42076 | -41.06721 | 2024-10-27 12:34:00 | TERRA_M-T | VITÓRIA DA CONQUISTA | BAHIA | Brasil | 2933307 | 29 | 33 | nan | nan | nan | Mata Atlântica | 45.6 |
| 4af35350-0043-318f-bb22-c21806e81b23 | -15.41886 | -41.08364 | 2024-10-27 12:34:00 | TERRA_M-T | VITÓRIA DA CONQUISTA | BAHIA | Brasil | 2933307 | 29 | 33 | nan | nan | nan | Mata Atlântica | 35.2 |
| 2fe02d5b-f29e-3089-87fe-741c4bb9b8b7 | -14.65699 | -42.8404 | 2024-10-27 12:34:00 | TERRA_M-T | SEBASTIÃO LARANJEIRAS | BAHIA | Brasil | 2930006 | 29 | 33 | nan | nan | nan | Caatinga | 30.3 |
| b7f81366-37fa-30f9-9199-b2eaf04a5ed3 | -13.76122 | -43.0665 | 2024-10-27 12:34:00 | TERRA_M-T | RIACHO DE SANTANA | BAHIA | Brasil | 2926400 | 29 | 33 | nan | nan | nan | Caatinga | 26.0 |
| dc5f5089-a109-3bcf-a4da-56abbbd14409 | -13.75972 | -43.07786 | 2024-10-27 12:34:00 | TERRA_M-T | RIACHO DE SANTANA | BAHIA | Brasil | 2926400 | 29 | 33 | nan | nan | nan | Caatinga | 47.3 |
| 4372e0f7-790a-39f3-8728-c9faa64a5545 | -13.51405 | -42.31408 | 2024-10-27 12:34:00 | TERRA_M-T | PARAMIRIM | BAHIA | Brasil | 2923605 | 29 | 33 | nan | nan | nan | Caatinga | 14.0 |
| a906d439-04ac-3ed7-8ae8-cca91346791b | -13.43712 | -41.60467 | 2024-10-27 12:34:00 | TERRA_M-T | JUSSIAPE | BAHIA | Brasil | 2918605 | 29 | 33 | nan | nan | nan | Caatinga | 16.7 |
| da5873f0-0c9c-3114-8e13-8e46a01d7ade | -13.43333 | -41.61268 | 2024-10-27 12:34:00 | TERRA_M-T | JUSSIAPE | BAHIA | Brasil | 2918605 | 29 | 33 | nan | nan | nan | Caatinga | 15.3 |
| a8ea4acf-a1c0-38ed-aa39-88d7c8efdcae | -13.37082 | -44.58542 | 2024-10-27 12:34:00 | TERRA_M-T | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 12.0 |
| 61b3e3c0-760d-3fda-aaea-4145c2aa447c | -13.32393 | -42.97747 | 2024-10-27 12:34:00 | TERRA_M-T | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Caatinga | 40.8 |
| c8d0fa5f-3c95-355f-ac59-ff4d3be7c0ce | -13.07881 | -42.13569 | 2024-10-27 12:34:00 | TERRA_M-T | RIO DO PIRES | BAHIA | Brasil | 2926905 | 29 | 33 | nan | nan | nan | Caatinga | 26.6 |
| bf4368e1-e838-3a3b-9d0b-b9eb0cb68a34 | -13.06831 | -42.13483 | 2024-10-27 12:34:00 | TERRA_M-T | RIO DO PIRES | BAHIA | Brasil | 2926905 | 29 | 33 | nan | nan | nan | Caatinga | 43.5 |
| 7b458247-bf0b-3a04-831d-f36d0f3d232d | -12.97103 | -43.18394 | 2024-10-27 12:34:00 | TERRA_M-T | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Caatinga | 8.0 |
| 92024903-87e4-3b0c-bffc-4db0b3300f7a | -12.96407 | -42.22989 | 2024-10-27 12:34:00 | TERRA_M-T | IBIPITANGA | BAHIA | Brasil | 2912509 | 29 | 33 | nan | nan | nan | Caatinga | 36.2 |
| 2c03c5c9-0afb-328f-ab4e-83bc1d72840c | -12.92562 | -40.38815 | 2024-10-27 12:34:00 | TERRA_M-T | IAÇU | BAHIA | Brasil | 2911907 | 29 | 33 | nan | nan | nan | Caatinga | 7.8 |
| 54754404-b1d1-3c65-a28a-99492febd93b | -12.8883 | -44.61273 | 2024-10-27 12:34:00 | TERRA_M-T | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 96.6 |
| f6dee6fa-12db-35e6-ac16-ac610e26889f | -12.88054 | -44.60198 | 2024-10-27 12:34:00 | TERRA_M-T | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 55.9 |
| e8bb0272-d68d-3836-856d-c49a451a31dd | -12.87923 | -44.61145 | 2024-10-27 12:34:00 | TERRA_M-T | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 156.9 |
| 73c5770a-79f5-33e5-9d92-f8cae2a47702 | -12.85901 | -41.74913 | 2024-10-27 12:34:00 | TERRA_M-T | BONINAL | BAHIA | Brasil | 2904001 | 29 | 33 | nan | nan | nan | Caatinga | 26.8 |
| 26c86a0c-1ab0-3c0e-bc45-cf706546c38d | -12.85513 | -41.74311 | 2024-10-27 12:34:00 | TERRA_M-T | BONINAL | BAHIA | Brasil | 2904001 | 29 | 33 | nan | nan | nan | Caatinga | 15.0 |
| 2ea120a6-1e36-3e3b-a523-e4182b079e07 | -12.78362 | -42.51074 | 2024-10-27 12:34:00 | TERRA_M-T | IBIPITANGA | BAHIA | Brasil | 2912509 | 29 | 33 | nan | nan | nan | Caatinga | 17.5 |
| f7f1759e-9d1d-37e6-b180-70c3acaf3426 | -12.74571 | -43.35038 | 2024-10-27 12:34:00 | TERRA_M-T | SÍTIO DO MATO | BAHIA | Brasil | 2930758 | 29 | 33 | nan | nan | nan | Cerrado | 38.2 |
| ee634282-c165-3d03-bfc8-68cf995977f1 | -12.74279 | -43.34348 | 2024-10-27 12:34:00 | TERRA_M-T | SÍTIO DO MATO | BAHIA | Brasil | 2930758 | 29 | 33 | nan | nan | nan | Cerrado | 35.2 |
| c2e0b474-3e3b-337b-9e53-14b2967022e4 | -12.74132 | -43.35418 | 2024-10-27 12:34:00 | TERRA_M-T | SÍTIO DO MATO | BAHIA | Brasil | 2930758 | 29 | 33 | nan | nan | nan | Cerrado | 35.9 |
| 159b03c2-3542-3ab8-96c6-8ac62213ec94 | -12.69715 | -42.78033 | 2024-10-27 12:34:00 | TERRA_M-T | BOQUIRA | BAHIA | Brasil | 2904100 | 29 | 33 | nan | nan | nan | Caatinga | 33.8 |
| 874740a9-a577-3388-9812-a533035b1cc9 | -12.6956 | -42.79201 | 2024-10-27 12:34:00 | TERRA_M-T | BOQUIRA | BAHIA | Brasil | 2904100 | 29 | 33 | nan | nan | nan | Caatinga | 16.1 |
| fb241ef0-5c38-3d61-a8ce-b2ff504cfca2 | -12.65908 | -41.92112 | 2024-10-27 12:34:00 | TERRA_M-T | SEABRA | BAHIA | Brasil | 2929909 | 29 | 33 | nan | nan | nan | Caatinga | 14.8 |
| 14b9ddec-fad1-3dd5-8ffc-7125aff51558 | -12.65367 | -41.92641 | 2024-10-27 12:34:00 | TERRA_M-T | SEABRA | BAHIA | Brasil | 2929909 | 29 | 33 | nan | nan | nan | Caatinga | 16.4 |
| eb8d7c05-38a2-3269-8613-1cd1f6ba23b0 | -12.61404 | -41.68473 | 2024-10-27 12:34:00 | TERRA_M-T | SEABRA | BAHIA | Brasil | 2929909 | 29 | 33 | nan | nan | nan | Caatinga | 16.0 |
| 1940a427-3185-3d6b-bb33-d85419996c26 | -12.37745 | -44.71079 | 2024-10-27 12:34:00 | TERRA_M-T | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 18.2 |
| 2592fcbb-f5c0-3c60-b75a-55f18fb8ef3a | -12.37615 | -44.72008 | 2024-10-27 12:34:00 | TERRA_M-T | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 5.8 |
| f0cee64f-4349-381d-8bbd-7d658d05433e | -12.37297 | -42.84473 | 2024-10-27 12:34:00 | TERRA_M-T | OLIVEIRA DOS BREJINHOS | BAHIA | Brasil | 2923209 | 29 | 33 | nan | nan | nan | Caatinga | 37.3 |


[Clique aqui para ver as próximas entradas](README66.md)
