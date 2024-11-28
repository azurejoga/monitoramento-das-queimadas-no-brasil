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

## Dados Diários - Página 28

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 6ea1300a-ca60-31a6-a0bb-493721079a42 | -6.83229 | -44.39088 | 2024-11-28 03:38:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 575842d0-2d6b-3826-a5e8-f5b9cfbf5ef8 | -6.71228 | -47.26291 | 2024-11-28 03:38:00 | NOAA-21 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 9113d989-de7d-30a6-bf9f-1d8cf1616682 | -6.82581 | -44.39376 | 2024-11-28 03:38:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 3a8959a6-c774-3e26-b2a2-f28d34ad2b1c | -5.31095 | -43.08077 | 2024-11-28 03:38:00 | NOAA-21 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 852ebd60-9823-30e4-816d-5bcfcfe19d60 | -6.09083 | -41.94454 | 2024-11-28 03:38:00 | NOAA-21 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 3.5 |
| 73893106-8dcb-34cc-98f2-827d4218c5aa | -5.94714 | -39.66274 | 2024-11-28 03:38:00 | NOAA-21 | MOMBAÇA | CEARÁ | Brasil | 2308500 | 23 | 33 | nan | nan | nan | Caatinga | 4.7 |
| d78683f9-0452-324d-918a-0f93feb50a62 | -8.12886 | -47.98207 | 2024-11-28 03:38:00 | NOAA-21 | ITAPIRATINS | TOCANTINS | Brasil | 1710904 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 62278621-25e5-3ef1-b80a-5e92ee3ca550 | -5.98499 | -45.36976 | 2024-11-28 03:38:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| edaf1823-716c-3958-a81d-648606b3aa66 | -9.45473 | -35.91045 | 2024-11-28 03:38:00 | NOAA-21 | RIO LARGO | ALAGOAS | Brasil | 2707701 | 27 | 33 | nan | nan | nan | Mata Atlântica | 21.4 |
| 5bf52b17-29ad-39af-9262-654f23ca56f3 | -4.85962 | -42.66919 | 2024-11-28 03:38:00 | NOAA-21 | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 658bccde-7017-3f82-bdd4-9c7823054db7 | -7.4763 | -35.30156 | 2024-11-28 03:38:00 | NOAA-21 | FERREIROS | PERNAMBUCO | Brasil | 2605509 | 26 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 3cc1c742-a55c-3c07-9283-03cabb4d7cfc | -6.92254 | -38.14299 | 2024-11-28 03:38:00 | NOAA-21 | SÃO JOSÉ DA LAGOA TAPADA | PARAÍBA | Brasil | 2514206 | 25 | 33 | nan | nan | nan | Caatinga | 1.5 |
| e66ebb28-7eb1-335e-a75b-32b0c7be6bf8 | -6.99105 | -34.90865 | 2024-11-28 03:38:00 | NOAA-21 | SANTA RITA | PARAÍBA | Brasil | 2513703 | 25 | 33 | nan | nan | nan | Mata Atlântica | 2.6 |
| 683ad570-3ba6-3c32-bb6d-fd5bf5b88999 | -6.16422 | -42.61864 | 2024-11-28 03:38:00 | NOAA-21 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 5.2 |
| 192a81fc-0a44-3b46-b573-aadf60c0c82c | -7.69505 | -42.98177 | 2024-11-28 03:38:00 | NOAA-21 | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 7.8 |
| 7eaf69e7-ea0b-3ff2-ae1e-476b55d65881 | -5.97481 | -45.36595 | 2024-11-28 03:38:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 42.1 |
| b81c4199-0426-3b0e-822d-0f3082f8047e | -6.16256 | -42.6281 | 2024-11-28 03:38:00 | NOAA-21 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 4.0 |
| b283f258-210b-319f-b447-cfa807bff7e9 | -4.43759 | -46.34664 | 2024-11-28 03:38:00 | NOAA-21 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 2.9 |
| a1f519d6-105e-3222-a5be-30c9d9f750c9 | -7.68913 | -42.97976 | 2024-11-28 03:38:00 | NOAA-21 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| d4b12681-221e-348e-a4ba-2654848d76eb | -6.38195 | -45.69006 | 2024-11-28 03:38:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 4.9 |
| ad4e0da2-6469-3df8-afba-e25f9fd86906 | -5.30566 | -44.43511 | 2024-11-28 03:38:00 | NOAA-21 | PRESIDENTE DUTRA | MARANHÃO | Brasil | 2109106 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 19730fb3-535d-3064-a5a5-15d00ef28e3b | -9.4581 | -35.91098 | 2024-11-28 03:38:00 | NOAA-21 | RIO LARGO | ALAGOAS | Brasil | 2707701 | 27 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| ceb3a073-dbfd-3603-a6a2-b8c637b2031d | -4.65783 | -44.04476 | 2024-11-28 03:38:00 | NOAA-21 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 6c249c23-28cf-3aba-95e5-477669c4c395 | -6.22963 | -42.98652 | 2024-11-28 03:38:00 | NOAA-21 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| e8f4fb02-3648-3d3d-a091-aa56a4449f4d | -4.18327 | -44.27143 | 2024-11-28 03:38:00 | NOAA-21 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| ee35c2df-19f4-3bba-994c-e63a7c310667 | -4.77573 | -44.42841 | 2024-11-28 03:38:00 | NOAA-21 | SANTO ANTÔNIO DOS LOPES | MARANHÃO | Brasil | 2110302 | 21 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 8aef6e9e-0c07-3c12-afda-5e629192f2c3 | -7.30672 | -42.10002 | 2024-11-28 03:38:00 | NOAA-21 | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 3f55f5d8-565c-3e06-aa18-74747bb73946 | -9.17384 | -44.72035 | 2024-11-28 03:38:00 | NOAA-21 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 7d8a1bc5-c155-3530-b28c-4d6e756a371f | -6.11684 | -46.59185 | 2024-11-28 03:38:00 | NOAA-21 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 48cbde4a-eca3-32fb-aaa0-c46fc0f1da44 | -6.11576 | -46.59778 | 2024-11-28 03:38:00 | NOAA-21 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 4e02416b-e8b8-3ad2-b60d-b28f8bfdcc2d | -5.96359 | -39.72299 | 2024-11-28 03:38:00 | NOAA-21 | MOMBAÇA | CEARÁ | Brasil | 2308500 | 23 | 33 | nan | nan | nan | Caatinga | 0.9 |
| a0b3b862-e025-3916-aa38-d480eed13ef2 | -9.00238 | -35.99294 | 2024-11-28 03:38:00 | NOAA-21 | SÃO JOSÉ DA LAJE | ALAGOAS | Brasil | 2708303 | 27 | 33 | nan | nan | nan | Mata Atlântica | 2.8 |
| 7fadec61-9683-3f69-932c-b93fc67e45c3 | -6.39947 | -39.5529 | 2024-11-28 03:38:00 | NOAA-21 | JUCÁS | CEARÁ | Brasil | 2307403 | 23 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 2f6048dd-4072-37b9-9524-771863d0e80f | -4.65857 | -44.04048 | 2024-11-28 03:38:00 | NOAA-21 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b3ae4196-dd96-3d46-a75e-fb266a502832 | -4.66443 | -44.04142 | 2024-11-28 03:38:00 | NOAA-21 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| f08f3fd9-b407-3d38-a175-815b3fedea29 | -5.57656 | -43.1485 | 2024-11-28 03:38:00 | NOAA-21 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 4577669d-a580-3541-bada-e6db27322fe6 | -7.70945 | -42.99105 | 2024-11-28 03:38:00 | NOAA-21 | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 30f3f944-5804-352e-a871-a31705b95ec8 | -6.15845 | -42.62095 | 2024-11-28 03:38:00 | NOAA-21 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 5.2 |
| 260f8fe0-013a-3302-bafc-16414889680a | -5.96234 | -39.72173 | 2024-11-28 03:38:00 | NOAA-21 | MOMBAÇA | CEARÁ | Brasil | 2308500 | 23 | 33 | nan | nan | nan | Caatinga | 0.9 |
| a12e5319-0ebe-3c0e-9e4b-559470b807c9 | -6.17632 | -42.61066 | 2024-11-28 03:38:00 | NOAA-21 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 43a9ff6a-3e14-32e8-bb4b-f06d6470757d | -6.83084 | -44.3989 | 2024-11-28 03:38:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 68cc443b-8a26-31db-96cf-d50a749a025d | -8.50033 | -43.28541 | 2024-11-28 03:38:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 47dd1572-8412-33f0-b07b-5e757aa9afbb | -4.43871 | -46.34032 | 2024-11-28 03:38:00 | NOAA-21 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 42d476ee-6f17-3396-9008-60aa85987604 | -6.35822 | -47.06017 | 2024-11-28 03:38:00 | NOAA-21 | PORTO FRANCO | MARANHÃO | Brasil | 2109007 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| d7b29f4d-c0a7-3352-a78f-0a32447f23a7 | -6.76293 | -39.69157 | 2024-11-28 03:38:00 | NOAA-21 | TARRAFAS | CEARÁ | Brasil | 2313252 | 23 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 139d1c0d-1537-314b-a24a-bde600eac865 | -5.52844 | -38.26703 | 2024-11-28 03:38:00 | NOAA-21 | ALTO SANTO | CEARÁ | Brasil | 2300705 | 23 | 33 | nan | nan | nan | Caatinga | 1.3 |
| c3284ff9-7764-3c4b-97a6-c56a31a7e3f6 | -6.16944 | -42.61944 | 2024-11-28 03:38:00 | NOAA-21 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 4.3 |
| 4a215f70-f9b2-38fa-aaa3-e92a7c64ad5e | -8.5009 | -43.28125 | 2024-11-28 03:38:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 8a3bd0b0-05f0-353c-a883-4a5aba005a64 | -5.95141 | -39.66343 | 2024-11-28 03:38:00 | NOAA-21 | MOMBAÇA | CEARÁ | Brasil | 2308500 | 23 | 33 | nan | nan | nan | Caatinga | 36.2 |
| b8cff9e8-17e2-3699-ba7a-9b97bec55f6e | -6.43874 | -35.45809 | 2024-11-28 03:38:00 | NOAA-21 | NOVA CRUZ | RIO GRANDE DO NORTE | Brasil | 2408300 | 24 | 33 | nan | nan | nan | Caatinga | 1.4 |
| fd289d4c-13a6-3e69-bd7c-d5ef5682eb9a | -3.1113 | -53.8242 | 2024-11-28 03:40:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 55.8 |
| 214526b9-ed01-3fe1-98fc-7073103affb3 | -5.9601 | -45.3635 | 2024-11-28 03:40:00 | GOES-16 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 51.0 |
| 9abbe7b7-f8e3-3320-9a98-9ed83481c313 | -5.979 | -45.3395 | 2024-11-28 03:40:00 | GOES-16 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 99.6 |
| d66ed855-843d-3c14-8a20-2692a67f0c12 | -1.5897 | -52.271 | 2024-11-28 03:40:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 86.6 |
| d8fe6bf7-164d-3aa9-a354-e3732852d342 | 1.2538 | -55.927 | 2024-11-28 03:40:00 | GOES-16 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 43.1 |
| 3a4a0527-bb08-38f7-948f-b9807f3c4d60 | -1.3329 | -51.9463 | 2024-11-28 03:40:00 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 50.4 |
| 87632957-2d48-3fec-b3b4-d95a15c8f684 | -3.1114 | -53.8041 | 2024-11-28 03:40:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 45.8 |
| c7493233-4de1-3023-91b5-6f53d05c3f7e | -23.7338 | -50.547 | 2024-11-28 03:40:00 | GOES-16 | CONGONHINHAS | PARANÁ | Brasil | 4106001 | 41 | 33 | nan | nan | nan | Mata Atlântica | 66.8 |
| 047b9d6c-6a35-3bd9-a672-469e68b0d976 | -5.9975 | -45.3607 | 2024-11-28 03:40:00 | GOES-16 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 57.7 |
| 3b4063cd-33d5-3ac4-aeb8-4e37cf9bdd84 | -3.3837 | -50.1125 | 2024-11-28 03:40:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 38.5 |
| 78c7f239-dc85-30a4-b115-c7feb77de882 | -2.861 | -46.8406 | 2024-11-28 03:40:00 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 47.8 |
| 63b7482f-ea53-3fe5-b0ea-50c32087464b | -2.8609 | -46.8626 | 2024-11-28 03:40:00 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 52.9 |
| aa2670fb-7d0f-3df9-b141-86d266424ef4 | -1.6623 | -52.7396 | 2024-11-28 03:40:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 53.0 |
| c06f74dd-8512-3eae-9636-86f27f0ebff2 | -5.9788 | -45.3621 | 2024-11-28 03:40:00 | GOES-16 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 165.7 |
| c3f3e035-a6a3-3778-b8fe-08466ed05cb4 | -17.84972 | -46.00284 | 2024-11-28 03:40:00 | NOAA-21 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 32e6c405-2a40-3670-87af-b80606cb9068 | -16.67991 | -43.88494 | 2024-11-28 03:40:00 | NOAA-21 | MONTES CLAROS | MINAS GERAIS | Brasil | 3143302 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 61de1064-e8b7-3b95-93ab-b2666c82b65e | -15.52665 | -44.16019 | 2024-11-28 03:40:00 | NOAA-21 | PEDRAS DE MARIA DA CRUZ | MINAS GERAIS | Brasil | 3149150 | 31 | 33 | nan | nan | nan | Cerrado | 0.2 |
| d04d9787-caec-369d-afb1-fc00e9b1812f | -13.29398 | -39.80131 | 2024-11-28 03:40:00 | NOAA-21 | SANTA INÊS | BAHIA | Brasil | 2927903 | 29 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 79b6601d-eafe-31f5-bf38-75334e4743bf | -15.53263 | -44.15554 | 2024-11-28 03:40:00 | NOAA-21 | PEDRAS DE MARIA DA CRUZ | MINAS GERAIS | Brasil | 3149150 | 31 | 33 | nan | nan | nan | Cerrado | 0.2 |
| fb1d9c14-852d-35bb-9ecc-064ba6937f44 | -13.29309 | -39.80648 | 2024-11-28 03:40:00 | NOAA-21 | SANTA INÊS | BAHIA | Brasil | 2927903 | 29 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 2f98af2d-4c15-3051-9a5f-df0d4d95cadf | -17.67617 | -42.74461 | 2024-11-28 03:40:00 | NOAA-21 | ITAMARANDIBA | MINAS GERAIS | Brasil | 3132503 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 43138648-a7a6-3866-8b9e-a68fbd958c35 | -16.35051 | -43.69821 | 2024-11-28 03:40:00 | NOAA-21 | CAPITÃO ENÉAS | MINAS GERAIS | Brasil | 3112703 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 02b303c4-d460-3bca-9b4a-7b159dffb1a7 | -17.85044 | -45.99942 | 2024-11-28 03:40:00 | NOAA-21 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 1ec5dd79-d85d-3e11-b13d-eb04ec631580 | -17.85121 | -45.99939 | 2024-11-28 03:40:00 | NOAA-21 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| a7fcf4e5-599e-32a3-a363-22485202b79f | -17.29157 | -44.35216 | 2024-11-28 03:40:00 | NOAA-21 | FRANCISCO DUMONT | MINAS GERAIS | Brasil | 3126604 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b5f546d9-b460-3c99-8ebf-fc3d5c10207a | -19.02975 | -42.85776 | 2024-11-28 03:40:00 | NOAA-21 | GUANHÃES | MINAS GERAIS | Brasil | 3128006 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 8e3ed502-cdd1-3697-a606-4627606c8721 | -17.85052 | -46.00279 | 2024-11-28 03:40:00 | NOAA-21 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 1b084f74-75c6-3fc4-96fa-acaed956939c | -16.19824 | -43.38653 | 2024-11-28 03:40:00 | NOAA-21 | FRANCISCO SÁ | MINAS GERAIS | Brasil | 3126703 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 6d67e0e0-c9c2-3f0a-b81b-3b2ea70a4246 | -13.28922 | -39.80592 | 2024-11-28 03:40:00 | NOAA-21 | SANTA INÊS | BAHIA | Brasil | 2927903 | 29 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 66f6c8d9-2415-3f34-90ec-4bd9b549dcfe | -17.77769 | -42.80793 | 2024-11-28 03:40:00 | NOAA-21 | ITAMARANDIBA | MINAS GERAIS | Brasil | 3132503 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| b260ccb5-498d-315e-ba54-1986441eafcc | -18.95181 | -43.70828 | 2024-11-28 03:40:00 | NOAA-21 | CONGONHAS DO NORTE | MINAS GERAIS | Brasil | 3118106 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 699913a7-e16a-363b-ba59-b492ddcd7fb5 | -18.95061 | -43.70551 | 2024-11-28 03:40:00 | NOAA-21 | CONGONHAS DO NORTE | MINAS GERAIS | Brasil | 3118106 | 31 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 0c19faee-d04a-34e7-b48c-e50dbf8e4e6a | -17.09526 | -43.80327 | 2024-11-28 03:40:00 | NOAA-21 | BOCAIÚVA | MINAS GERAIS | Brasil | 3107307 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 03bc9683-43ed-333d-afaf-3f4bd6283e47 | -16.34867 | -43.69564 | 2024-11-28 03:40:00 | NOAA-21 | CAPITÃO ENÉAS | MINAS GERAIS | Brasil | 3112703 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ec60375d-cbcc-3d61-bbe8-8284a936d937 | -22.90611 | -43.65791 | 2024-11-28 03:42:00 | NOAA-21 | RIO DE JANEIRO | RIO DE JANEIRO | Brasil | 3304557 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| f194a922-e1d1-35ec-a253-47fbe47d1aa6 | -23.70801 | -50.55411 | 2024-11-28 03:42:00 | NOAA-21 | CONGONHINHAS | PARANÁ | Brasil | 4106001 | 41 | 33 | nan | nan | nan | Mata Atlântica | 4.7 |
| ef901aad-9cab-3255-98a6-4e33431c05f3 | -23.36977 | -47.06066 | 2024-11-28 03:42:00 | NOAA-21 | ARAÇARIGUAMA | SÃO PAULO | Brasil | 3502754 | 35 | 33 | nan | nan | nan | Mata Atlântica | 5.5 |
| de0fc4bc-e20d-3629-b403-c517d2fbcae6 | -20.90104 | -43.81968 | 2024-11-28 03:42:00 | NOAA-21 | CARANDAÍ | MINAS GERAIS | Brasil | 3113206 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| bd8c4669-2f5f-36dc-9b1a-96ce185f3699 | -23.71909 | -50.5619 | 2024-11-28 03:42:00 | NOAA-21 | CONGONHINHAS | PARANÁ | Brasil | 4106001 | 41 | 33 | nan | nan | nan | Mata Atlântica | 9.6 |
| b5828097-1201-3bc7-ba82-c89d759f4564 | -23.70668 | -50.55952 | 2024-11-28 03:42:00 | NOAA-21 | CONGONHINHAS | PARANÁ | Brasil | 4106001 | 41 | 33 | nan | nan | nan | Mata Atlântica | 5.5 |
| 1b5a05f6-c243-3347-a72a-b440c430ecab | -23.37044 | -47.05756 | 2024-11-28 03:42:00 | NOAA-21 | ARAÇARIGUAMA | SÃO PAULO | Brasil | 3502754 | 35 | 33 | nan | nan | nan | Mata Atlântica | 5.5 |
| 451804e1-eb5f-3144-8d3d-2f88114e9584 | -23.47816 | -45.34937 | 2024-11-28 03:42:00 | NOAA-21 | NATIVIDADE DA SERRA | SÃO PAULO | Brasil | 3532306 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| d60f4f06-0387-3094-a692-4b309866794f | -21.12261 | -48.64933 | 2024-11-28 03:42:00 | NOAA-21 | PIRANGI | SÃO PAULO | Brasil | 3539004 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 7286c17d-ae59-39d3-8217-7bd470626a47 | -22.7873 | -43.75832 | 2024-11-28 03:42:00 | NOAA-21 | SEROPÉDICA | RIO DE JANEIRO | Brasil | 3305554 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| a013dff1-b6f5-33af-b55a-562b364be181 | -23.72054 | -50.55601 | 2024-11-28 03:42:00 | NOAA-21 | CONGONHINHAS | PARANÁ | Brasil | 4106001 | 41 | 33 | nan | nan | nan | Mata Atlântica | 6.6 |
| 548d0381-5ea8-341a-8404-496fbe817045 | -21.12422 | -47.85463 | 2024-11-28 03:42:00 | NOAA-21 | RIBEIRÃO PRETO | SÃO PAULO | Brasil | 3543402 | 35 | 33 | nan | nan | nan | Cerrado | 10.3 |
| 639a3a3c-f147-3127-bd65-d845d24bac56 | -20.45583 | -46.14482 | 2024-11-28 03:42:00 | NOAA-21 | PIUMHI | MINAS GERAIS | Brasil | 3151503 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 86cce9d7-ba69-37ac-9aef-42717ec00f1f | -19.52686 | -47.33561 | 2024-11-28 03:42:00 | NOAA-21 | PERDIZES | MINAS GERAIS | Brasil | 3149804 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| fdce0ba3-b259-3d63-8d7a-db4e02217501 | -22.54179 | -48.81361 | 2024-11-28 03:42:00 | NOAA-21 | MACATUBA | SÃO PAULO | Brasil | 3528007 | 35 | 33 | nan | nan | nan | Cerrado | 3.1 |
| c97b803d-e753-386f-8fd4-6564e868452b | -23.70823 | -50.55734 | 2024-11-28 03:42:00 | NOAA-21 | CONGONHINHAS | PARANÁ | Brasil | 4106001 | 41 | 33 | nan | nan | nan | Mata Atlântica | 12.9 |


[Clique aqui para ver as próximas entradas](README29.md)
