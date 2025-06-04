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

## Dados Diários - Página 5

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 49d230f2-5cfc-3ea4-9393-f2ed35eba5c9 | -22.85638 | -42.98023 | 2025-06-04 03:42:00 | NPP-375D | SÃO GONÇALO | RIO DE JANEIRO | Brasil | 3304904 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 0a199c94-87df-3be8-a5d2-818e0952c9c7 | -23.40702 | -46.55576 | 2025-06-04 03:42:00 | NPP-375D | GUARULHOS | SÃO PAULO | Brasil | 3518800 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| b90f8389-ef0d-3a37-97d3-3921a240dfc1 | -22.67536 | -42.85495 | 2025-06-04 03:42:00 | NPP-375D | ITABORAÍ | RIO DE JANEIRO | Brasil | 3301900 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 81b45ed3-72e9-346d-87ba-52cbc834ec99 | -22.90165 | -43.75268 | 2025-06-04 03:42:00 | NPP-375D | RIO DE JANEIRO | RIO DE JANEIRO | Brasil | 3304557 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| d505f7b5-c45a-31ac-8e26-8e26c2e06fa4 | -22.54007 | -48.81433 | 2025-06-04 03:42:00 | NPP-375D | MACATUBA | SÃO PAULO | Brasil | 3528007 | 35 | 33 | nan | nan | nan | Cerrado | 1.7 |
| b4b00a22-90fa-31da-b670-67254af3b3b7 | -23.33862 | -46.77173 | 2025-06-04 03:42:00 | NPP-375D | CAIEIRAS | SÃO PAULO | Brasil | 3509007 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| c989105c-8da2-3fa1-a2d5-146081d6f165 | -22.78738 | -43.75871 | 2025-06-04 03:42:00 | NPP-375D | SEROPÉDICA | RIO DE JANEIRO | Brasil | 3305554 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 8decc630-11b4-3985-9b49-4ca46a860d2c | -25.57209 | -49.35968 | 2025-06-04 03:45:00 | NPP-375D | ARAUCÁRIA | PARANÁ | Brasil | 4101804 | 41 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| 77c23cda-2c87-37a8-8df1-2b1691c8a5d7 | -25.5691 | -49.3564 | 2025-06-04 03:45:00 | NPP-375D | ARAUCÁRIA | PARANÁ | Brasil | 4101804 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| e6b43be8-65da-352b-aedc-8856845a3a3d | -25.57304 | -49.35559 | 2025-06-04 03:45:00 | NPP-375D | ARAUCÁRIA | PARANÁ | Brasil | 4101804 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 9239267a-1f95-31f6-94d5-38f1a65f31d4 | -25.19283 | -49.32664 | 2025-06-04 03:45:00 | NPP-375D | RIO BRANCO DO SUL | PARANÁ | Brasil | 4122206 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| d869af2d-489d-34dc-a582-6646e39f2833 | -25.57465 | -49.35801 | 2025-06-04 03:45:00 | NPP-375D | ARAUCÁRIA | PARANÁ | Brasil | 4101804 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 9b943515-b81f-37b6-a9cb-6c33fdd0e908 | -25.19937 | -49.32419 | 2025-06-04 03:45:00 | NPP-375D | RIO BRANCO DO SUL | PARANÁ | Brasil | 4122206 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 4d8dae6f-9746-3c63-b86c-b9dd37c951e4 | -6.9791 | -42.9034 | 2025-06-04 03:50:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 65.5 |
| a30bdd08-94b1-39cc-a04b-ee9ce51e5314 | -6.9602 | -42.9052 | 2025-06-04 03:50:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 80.3 |
| dbd6f81c-f413-31e9-9e9f-361491ffeb27 | -4.11759 | -38.3352 | 2025-06-04 03:57:00 | NOAA-20 | CASCAVEL | CEARÁ | Brasil | 2303501 | 23 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 137a9040-9c3b-3ed1-bcd3-7b737fedd967 | -3.28587 | -42.53231 | 2025-06-04 03:57:00 | NOAA-20 | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| d5606af5-163b-3dd0-a8bb-13b6d3c54653 | -4.8591 | -37.59859 | 2025-06-04 03:57:00 | NOAA-20 | ARACATI | CEARÁ | Brasil | 2301109 | 23 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 3c4e55dd-516d-349b-bd3d-ee2dc2f10a29 | -5.22837 | -37.65782 | 2025-06-04 03:57:00 | NOAA-20 | BARAÚNA | RIO GRANDE DO NORTE | Brasil | 2401453 | 24 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 15031f82-cc0c-3b81-bb62-6fbada35ee38 | -4.80583 | -45.26257 | 2025-06-04 03:57:00 | NOAA-20 | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 91b20976-7974-39fc-baf7-8ede0e693624 | -5.50072 | -35.58113 | 2025-06-04 03:57:00 | NOAA-20 | TAIPU | RIO GRANDE DO NORTE | Brasil | 2413904 | 24 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 89cb80f3-38fe-36ae-aa10-113d249f99cd | -3.13516 | -41.79215 | 2025-06-04 03:57:00 | NOAA-20 | BURITI DOS LOPES | PIAUÍ | Brasil | 2202000 | 22 | 33 | nan | nan | nan | Caatinga | 6.3 |
| 4b2fd5fb-36a0-3c0e-9400-932f11e87501 | -4.56761 | -43.20228 | 2025-06-04 03:57:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 631aa65d-5d32-31a8-afbf-dc09ad3a8eb4 | -4.81006 | -45.26316 | 2025-06-04 03:57:00 | NOAA-20 | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 15add4cb-42c4-3d53-9c4c-1d6082ca5877 | -4.00256 | -43.24456 | 2025-06-04 03:57:00 | NOAA-20 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 9c86a428-b5d5-3956-8eff-56dea976fcef | -3.28952 | -42.53289 | 2025-06-04 03:57:00 | NOAA-20 | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 0d533cb6-44cb-3049-9167-962bc8afc984 | -4.80558 | -45.2629 | 2025-06-04 03:57:00 | NOAA-20 | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| d2d74d53-a2c7-3cef-ae70-931297bee183 | -3.13227 | -41.78765 | 2025-06-04 03:57:00 | NOAA-20 | BURITI DOS LOPES | PIAUÍ | Brasil | 2202000 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 744d3bd3-2eb4-35a1-95ef-58becc8d0242 | -3.66734 | -39.21399 | 2025-06-04 03:57:00 | NOAA-20 | SÃO GONÇALO DO AMARANTE | CEARÁ | Brasil | 2312403 | 23 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 4f176974-eb32-328d-a082-98a31b101aa8 | -4.81893 | -44.35658 | 2025-06-04 03:57:00 | NOAA-20 | SANTO ANTÔNIO DOS LOPES | MARANHÃO | Brasil | 2110302 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 8050b8f9-772b-33f7-8a92-89890aae8697 | -5.22779 | -37.66155 | 2025-06-04 03:57:00 | NOAA-20 | BARAÚNA | RIO GRANDE DO NORTE | Brasil | 2401453 | 24 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 4ef8b232-fbce-3181-9ae2-ea5fd3fbdcf1 | -4.80622 | -45.25892 | 2025-06-04 03:57:00 | NOAA-20 | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 205c360c-d9a8-3c2d-81a0-0210639822ee | -3.89028 | -42.54746 | 2025-06-04 03:57:00 | NOAA-20 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| d1e52421-7394-36ef-982d-c55a5faf3879 | -4.00631 | -43.24516 | 2025-06-04 03:57:00 | NOAA-20 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 0ee6a4f2-38fe-3c60-af23-0341133624b7 | -4.8065 | -45.25859 | 2025-06-04 03:57:00 | NOAA-20 | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| b5dafdcf-f9f9-30de-b612-bd489ea7a948 | -3.13579 | -41.78821 | 2025-06-04 03:57:00 | NOAA-20 | BURITI DOS LOPES | PIAUÍ | Brasil | 2202000 | 22 | 33 | nan | nan | nan | Caatinga | 6.3 |
| 4ff5146e-1ab1-3b6e-a40f-22d0209c2727 | -6.9791 | -42.9034 | 2025-06-04 04:00:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 65.2 |
| 8f8c0845-807e-36e6-9555-7919dc0955b9 | -6.9602 | -42.9052 | 2025-06-04 04:00:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 107.0 |
| 31644988-7cfb-3f6e-af1c-09a11607325a | -10.1884 | -48.47564 | 2025-06-04 04:00:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 9f4718d8-ecca-3b23-8e1f-e66ffbf309f4 | -9.26079 | -47.64927 | 2025-06-04 04:00:00 | NOAA-20 | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 81d809d5-66ee-358a-9950-f748979ac3fe | -7.01606 | -44.58388 | 2025-06-04 04:00:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 12.3 |
| 173d2286-b2e1-3ad0-b5af-9c4c319731bf | -6.86701 | -47.84355 | 2025-06-04 04:00:00 | NOAA-20 | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 7abef99f-9acc-3a66-8e7b-6690e02ac3d6 | -6.37002 | -43.68256 | 2025-06-04 04:00:00 | NOAA-20 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 3dcaa410-b057-3171-9663-4395167db46b | -6.24821 | -43.36753 | 2025-06-04 04:00:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| aeff6761-3e7c-3293-b3cf-7e576055f8e4 | -10.65276 | -44.49452 | 2025-06-04 04:00:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 03fb9c0d-9efa-379a-b3f3-b71d8c8e33c1 | -7.87562 | -45.99039 | 2025-06-04 04:00:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 03767a5a-8e43-34f9-8bd2-630be0bda232 | -8.9104 | -50.04317 | 2025-06-04 04:00:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| e752cf11-c209-3e58-8df4-33122f00bf8e | -9.56161 | -50.51586 | 2025-06-04 04:00:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| cb6d0c9f-b7db-3625-8521-551998f97c83 | -10.6535 | -44.49012 | 2025-06-04 04:00:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 7ec34398-7707-3095-811a-5324378da2df | -6.36629 | -43.68194 | 2025-06-04 04:00:00 | NOAA-20 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a2390583-ff57-3eb9-8b95-b1a60fb637ba | -7.87629 | -45.98649 | 2025-06-04 04:00:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 4a1d00c5-8a41-3889-ab5a-cca6726301ab | -7.90281 | -50.35906 | 2025-06-04 04:00:00 | NOAA-20 | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| c4dfb10d-65b1-3c30-bcc5-4cdadecc74b6 | -10.61846 | -44.76716 | 2025-06-04 04:00:00 | NOAA-20 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| cefdf1c3-0b7a-3ed3-a0ee-6ff70da87c42 | -6.56159 | -44.48651 | 2025-06-04 04:00:00 | NOAA-20 | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 0ddc32cc-8fec-373a-ad5d-46bd72cb7ece | -8.75531 | -49.77049 | 2025-06-04 04:00:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 446285d7-6996-3f17-8adb-de7964bce725 | -10.61472 | -44.76649 | 2025-06-04 04:00:00 | NOAA-20 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 3.2 |
| e9d004d2-5881-3950-9060-82cdf72d2532 | -7.14988 | -44.03898 | 2025-06-04 04:00:00 | NOAA-20 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 18bcde70-7493-3f79-9eee-d9e8fc6e2ae0 | -7.21079 | -43.13752 | 2025-06-04 04:00:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 643114aa-0cd3-326f-93d8-0d24bdf33405 | -6.68837 | -43.68134 | 2025-06-04 04:00:00 | NOAA-20 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 46c3cefd-0600-33ab-8d1c-b31ad6f4b122 | -7.222 | -43.12529 | 2025-06-04 04:00:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| b320e63c-842b-3b3b-b128-f81dc9b97529 | -10.22209 | -47.57003 | 2025-06-04 04:00:00 | NOAA-20 | LAGOA DO TOCANTINS | TOCANTINS | Brasil | 1711951 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| da6ebe6f-9a22-3d57-92de-1def8b6a5c3e | -7.89362 | -46.1928 | 2025-06-04 04:00:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 219e4a90-833d-3fd3-871a-6a2150aa5469 | -9.20125 | -49.69308 | 2025-06-04 04:00:00 | NOAA-20 | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| bcc65931-5748-3da2-8500-aee64270f186 | -7.00801 | -44.60791 | 2025-06-04 04:00:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 6143da0d-5ddd-386e-b480-538da1b1e3f4 | -10.69944 | -44.81674 | 2025-06-04 04:00:00 | NOAA-20 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 9eba8d0d-c05d-3bce-9ef4-ae8796a630b3 | -7.98395 | -47.21792 | 2025-06-04 04:00:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| a05049d2-fe90-346e-8caf-5a8402469fd6 | -9.13911 | -41.0018 | 2025-06-04 04:00:00 | NOAA-20 | CASA NOVA | BAHIA | Brasil | 2907202 | 29 | 33 | nan | nan | nan | Caatinga | 6.7 |
| 9239bb69-509b-3158-8a4a-5aefb028234b | -7.89008 | -46.18772 | 2025-06-04 04:00:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| c5ecb09d-0a33-3f7e-81bf-faf0d2258fcf | -10.0534 | -44.64243 | 2025-06-04 04:00:00 | NOAA-20 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 3a88b442-39b8-32c8-8b91-a02166ca7ffa | -7.01443 | -44.59362 | 2025-06-04 04:00:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 12.0 |
| c307a968-3a23-3c24-8c99-ae3fbaea7cea | -6.96937 | -42.90249 | 2025-06-04 04:00:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 20.0 |
| 536fd245-b22c-3904-b952-423b4cfe91e2 | -8.7547 | -49.77388 | 2025-06-04 04:00:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| a37ca948-de68-32d6-ac92-4445f447a14c | -6.24751 | -43.37184 | 2025-06-04 04:00:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 5c89eb7f-d7d4-3b92-98e4-a424cee63518 | -7.00885 | -44.60292 | 2025-06-04 04:00:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 82d6541d-2217-378b-9b09-4fe4c3aa02e5 | -11.62629 | -41.83139 | 2025-06-04 04:00:00 | NOAA-20 | IBITITÁ | BAHIA | Brasil | 2913101 | 29 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 6d27f8c1-8c8c-3f51-bb2f-a829c0289a47 | -6.63039 | -43.20639 | 2025-06-04 04:00:00 | NOAA-20 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 1d41a381-db4a-3c13-80fc-0a6b7cc6908f | -9.58706 | -40.33761 | 2025-06-04 04:00:00 | NOAA-20 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 0.3 |
| dd9d81fd-ee74-3595-864d-30adfa669dd9 | -7.37358 | -43.1114 | 2025-06-04 04:00:00 | NOAA-20 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 74488083-897b-3e43-a5d5-adfe2f6703b6 | -6.20941 | -43.33147 | 2025-06-04 04:00:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 84a4151f-c750-3e1b-8d63-9291f5119324 | -7.22627 | -43.12177 | 2025-06-04 04:00:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 1712a018-8f5e-34d2-a78d-5674ec36b24c | -10.35416 | -48.73097 | 2025-06-04 04:00:00 | NOAA-20 | PARAÍSO DO TOCANTINS | TOCANTINS | Brasil | 1716109 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 8cad6051-e862-3eb6-8ce0-9e6d0748a05c | -7.14538 | -44.04284 | 2025-06-04 04:00:00 | NOAA-20 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| c6009fe5-9c0b-3b76-9f50-531f6d058180 | -9.4992 | -40.3126 | 2025-06-04 04:00:00 | NOAA-20 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 1.1 |
| a2de65f7-b9ce-3314-9de3-9c447e2ab25c | -6.68765 | -43.68577 | 2025-06-04 04:00:00 | NOAA-20 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 2975a6fc-afb4-3b96-8e86-633d8f260d49 | -7.96783 | -47.03536 | 2025-06-04 04:00:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| cd794f96-ccbb-3963-8c19-ce86026af655 | -10.03721 | -48.78258 | 2025-06-04 04:00:00 | NOAA-20 | PARAÍSO DO TOCANTINS | TOCANTINS | Brasil | 1716109 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| b0623cea-d9a7-39af-a39a-7147b3facf3d | -8.55787 | -44.55471 | 2025-06-04 04:00:00 | NOAA-20 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| a4fe067e-ca4e-3a5f-b6d4-bb50979c81f8 | -7.2072 | -43.13694 | 2025-06-04 04:00:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 0d3ada01-7265-32ec-9edf-b3941896ddca | -7.14161 | -44.04222 | 2025-06-04 04:00:00 | NOAA-20 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ddf8b2f2-fb91-3159-bb74-d87de1f6d87e | -7.01524 | -44.58876 | 2025-06-04 04:00:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 12.3 |
| 72d588bd-e7cc-3662-b9e5-fb1a19a16196 | -7.43405 | -37.21305 | 2025-06-04 04:00:00 | NOAA-20 | SÃO JOSÉ DO EGITO | PERNAMBUCO | Brasil | 2613602 | 26 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 2c1caa75-125e-3a89-baf0-6f9b74fd0a97 | -7.21277 | -43.13647 | 2025-06-04 04:00:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 6.0 |
| 70af0b6a-7440-3b90-bc6e-2dc26313c2a4 | -7.01194 | -44.6084 | 2025-06-04 04:00:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 3cfe7030-8db3-3a46-a91e-8e0359755fea | -6.94982 | -42.80016 | 2025-06-04 04:00:00 | NOAA-20 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| a89cc106-bbcc-3c06-a2b9-09f51f375e15 | -6.29243 | -47.00647 | 2025-06-04 04:00:00 | NOAA-20 | SÃO JOÃO DO PARAÍSO | MARANHÃO | Brasil | 2111052 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| d68a7151-1f9c-3252-94d6-abbd4dd5bd50 | -6.68593 | -43.6834 | 2025-06-04 04:00:00 | NOAA-20 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| e5e242b9-15a7-3553-ab87-437edb621197 | -6.96383 | -42.914 | 2025-06-04 04:00:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 14.0 |
| 526c3f90-cac0-3f34-88bc-52e4e597878a | -8.90434 | -50.04559 | 2025-06-04 04:00:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 2e243013-17c8-356e-bf37-b05e3784d237 | -6.37172 | -43.68114 | 2025-06-04 04:00:00 | NOAA-20 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c8eec10a-f725-3ff3-9ea2-bc4937139c3d | -7.08425 | -49.5983 | 2025-06-04 04:00:00 | NOAA-20 | XINGUARA | PARÁ | Brasil | 1508407 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |


[Clique aqui para ver as próximas entradas](README6.md)
