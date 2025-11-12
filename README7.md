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

## Dados Diários - Página 7

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| f72dbbf0-bfe2-3398-8991-5713f1042429 | -4.14609 | -47.66593 | 2025-11-12 03:42:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8fa175ac-ac88-361e-84f1-0058c41f7701 | -3.9675 | -43.78176 | 2025-11-12 03:42:00 | NOAA-20 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 943a80b9-081d-3a01-88cd-ac59508b8a62 | -6.31195 | -43.81508 | 2025-11-12 03:42:00 | NOAA-20 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| b43376d0-2a4c-3636-b421-d4a68d38d9c8 | -9.66848 | -43.90437 | 2025-11-12 03:42:00 | NOAA-20 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| aa9fa76c-a06c-386a-8469-b978b05636e4 | -5.73085 | -35.29818 | 2025-11-12 03:42:00 | NOAA-20 | SÃO GONÇALO DO AMARANTE | RIO GRANDE DO NORTE | Brasil | 2412005 | 24 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 37db6911-5460-3867-82d5-2de8c552832f | -8.55251 | -36.25478 | 2025-11-12 03:42:00 | NOAA-20 | ALTINHO | PERNAMBUCO | Brasil | 2600807 | 26 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 89c535d3-360e-3bc0-ab71-bc77664ee53c | -9.45053 | -44.87818 | 2025-11-12 03:42:00 | NOAA-20 | MONTE ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2206605 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 7bc095c9-bd54-3cc4-8cd4-ebd6af318ef8 | -6.31298 | -43.80906 | 2025-11-12 03:42:00 | NOAA-20 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 50645763-73f1-3cdc-8c1e-5fd79f3ab0ba | -5.75402 | -35.32307 | 2025-11-12 03:42:00 | NOAA-20 | SÃO GONÇALO DO AMARANTE | RIO GRANDE DO NORTE | Brasil | 2412005 | 24 | 33 | nan | nan | nan | Caatinga | 0.7 |
| f7abfdea-e63e-3ac7-b717-544f8bd3afa8 | -7.45414 | -44.74185 | 2025-11-12 03:42:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 6b38e7b9-7a6e-3188-975a-ca3503efdfe3 | -6.51548 | -35.21453 | 2025-11-12 03:42:00 | NOAA-20 | PEDRO VELHO | RIO GRANDE DO NORTE | Brasil | 2409803 | 24 | 33 | nan | nan | nan | Mata Atlântica | 31.0 |
| f2372ce5-0dd4-3c2a-ace5-6eaa4188507e | -8.15442 | -36.00154 | 2025-11-12 03:42:00 | NOAA-20 | CARUARU | PERNAMBUCO | Brasil | 2604106 | 26 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| c086e82c-3349-356f-a114-6d07713a0d43 | -5.0049 | -46.82663 | 2025-11-12 03:42:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 805ff128-3185-364e-8037-1779339d7434 | -5.10102 | -40.77403 | 2025-11-12 03:42:00 | NOAA-20 | CRATEÚS | CEARÁ | Brasil | 2304103 | 23 | 33 | nan | nan | nan | Caatinga | 1.3 |
| b6da561d-db4d-30dc-9451-a24f491acca7 | -6.89822 | -42.07646 | 2025-11-12 03:42:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 41bff1a1-d53b-3caf-b92b-afb426a28343 | -5.25109 | -38.4334 | 2025-11-12 03:42:00 | NOAA-20 | MORADA NOVA | CEARÁ | Brasil | 2308708 | 23 | 33 | nan | nan | nan | Caatinga | 1.6 |
| d2da0410-d518-384b-8e1a-b3e5b62c5c6c | -7.59788 | -38.84041 | 2025-11-12 03:42:00 | NOAA-20 | BREJO SANTO | CEARÁ | Brasil | 2302503 | 23 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 9a8bb2dc-f431-324c-8532-c76bdf02d775 | -7.47498 | -42.55798 | 2025-11-12 03:42:00 | NOAA-20 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 68a22347-ee8c-30c0-8527-c4607de9e8d8 | -5.08967 | -43.74502 | 2025-11-12 03:42:00 | NOAA-20 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 31fdc1a5-01e9-3d5d-9ce2-051bda3a651c | -5.00256 | -46.83027 | 2025-11-12 03:42:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| d8d477ce-5b06-37fa-9cd9-46b42cda40c3 | -4.13925 | -47.66504 | 2025-11-12 03:42:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5b634a70-c663-3db4-859c-64c3de5bb19c | -4.93717 | -44.29967 | 2025-11-12 03:42:00 | NOAA-20 | GOVERNADOR ARCHER | MARANHÃO | Brasil | 2104503 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 1822951b-9ff9-321e-832c-cc1f0c0934dd | -3.98028 | -47.30056 | 2025-11-12 03:42:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 3c1d8102-c5b3-313f-b275-a0fc35adcf7d | -7.4804 | -42.55415 | 2025-11-12 03:42:00 | NOAA-20 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 5c974a5f-b175-30ec-9540-45ece4178c73 | -7.76809 | -36.41983 | 2025-11-12 03:42:00 | NOAA-20 | CARAÚBAS | PARAÍBA | Brasil | 2504074 | 25 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 911de00a-cb79-3cb0-b6b6-5812e72b526d | -4.09758 | -48.01698 | 2025-11-12 03:42:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 12.9 |
| 8ed2e765-e49c-3ce6-9559-1531056eeccf | -6.31507 | -43.80934 | 2025-11-12 03:42:00 | NOAA-20 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 347e0f5f-40d1-38ec-9bc2-55d9a634c9a2 | -6.44433 | -43.49003 | 2025-11-12 03:42:00 | NOAA-20 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| af5198af-fe43-34d8-a9eb-f8fb307a9fb3 | -7.45164 | -44.75558 | 2025-11-12 03:42:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 4.0 |
| a53632f4-df41-3cb7-a206-acc5754bb889 | -10.94993 | -37.20219 | 2025-11-12 03:42:00 | NOAA-20 | SÃO CRISTÓVÃO | SERGIPE | Brasil | 2806701 | 28 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 3098727f-0ec3-35e3-a5f7-5fc5ab6f1611 | -7.45891 | -44.74607 | 2025-11-12 03:42:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c05f5dd7-08f9-3ff2-90dd-e8cea3cb29d4 | -8.92204 | -35.40133 | 2025-11-12 03:42:00 | NOAA-20 | JACUÍPE | ALAGOAS | Brasil | 2703502 | 27 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 701997a7-bedf-37fa-aa70-139b7ebd795d | -4.10327 | -48.02515 | 2025-11-12 03:42:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 39.7 |
| 91c399a1-ce8e-38ce-88cf-3676f25ee0bd | -6.31452 | -43.81238 | 2025-11-12 03:42:00 | NOAA-20 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 11.0 |
| afce6688-1770-3bdf-8c8f-1498de92eb99 | -6.51493 | -35.21799 | 2025-11-12 03:42:00 | NOAA-20 | PEDRO VELHO | RIO GRANDE DO NORTE | Brasil | 2409803 | 24 | 33 | nan | nan | nan | Mata Atlântica | 31.0 |
| fa06d82a-687b-3536-8561-d1b22263f0e2 | -6.90272 | -42.07738 | 2025-11-12 03:42:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 9756b67b-bf1e-3e9a-9b01-b9d7f087a57f | -4.32402 | -44.54589 | 2025-11-12 03:42:00 | NOAA-20 | SÃO LUÍS GONZAGA DO MARANHÃO | MARANHÃO | Brasil | 2111409 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 8725b849-c53f-3cce-99d8-eabcf0d77aaa | -7.13132 | -41.87289 | 2025-11-12 03:42:00 | NOAA-20 | SANTA CRUZ DO PIAUÍ | PIAUÍ | Brasil | 2209104 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 2c995027-6f1a-3630-9c44-7a18a47296d1 | -4.14425 | -47.66669 | 2025-11-12 03:42:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6293ad6d-f229-371c-9798-081a655faf57 | -3.9574 | -43.77664 | 2025-11-12 03:42:00 | NOAA-20 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e26763cd-39e7-3eb6-b423-95e4bdedf699 | -7.60083 | -38.84512 | 2025-11-12 03:42:00 | NOAA-20 | BREJO SANTO | CEARÁ | Brasil | 2302503 | 23 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 76546ff0-b576-3f27-a46d-b0c2dd6dd270 | -4.32339 | -44.5496 | 2025-11-12 03:42:00 | NOAA-20 | SÃO LUÍS GONZAGA DO MARANHÃO | MARANHÃO | Brasil | 2111409 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| e3e05abb-918b-3afa-9f42-4c7a2f1f3c91 | -10.25779 | -36.68552 | 2025-11-12 03:42:00 | NOAA-20 | IGREJA NOVA | ALAGOAS | Brasil | 2703205 | 27 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 61331128-9097-321d-bde8-6e17a9fb3126 | -7.14044 | -41.26221 | 2025-11-12 03:42:00 | NOAA-20 | GEMINIANO | PIAUÍ | Brasil | 2204352 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 70cca58d-d8d7-34c7-8142-821988c6a29b | -4.10567 | -48.01166 | 2025-11-12 03:42:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 18.6 |
| ae28020f-1bb8-31cc-b405-45d17e6bfef6 | -9.67335 | -43.90536 | 2025-11-12 03:42:00 | NOAA-20 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| e043da3f-4137-378c-8a7b-90bf8ca85bef | -4.75623 | -44.46697 | 2025-11-12 03:42:00 | NOAA-20 | SANTO ANTÔNIO DOS LOPES | MARANHÃO | Brasil | 2110302 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ba2799cf-a345-3034-ae30-e86f86a31395 | -5.18499 | -37.6489 | 2025-11-12 03:42:00 | NOAA-20 | BARAÚNA | RIO GRANDE DO NORTE | Brasil | 2401453 | 24 | 33 | nan | nan | nan | Caatinga | 0.8 |
| e68885a1-393f-36a4-9212-c257ebf4f354 | -7.0217 | -38.83428 | 2025-11-12 03:42:00 | NOAA-20 | BARRO | CEARÁ | Brasil | 2302008 | 23 | 33 | nan | nan | nan | Caatinga | 7.4 |
| fcf4de37-a30d-3ba2-8c7f-28169b800f04 | -7.45829 | -44.74949 | 2025-11-12 03:42:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| e581d1de-76fd-3e66-9dd1-22545aed846d | -4.64728 | -47.95995 | 2025-11-12 03:42:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 174a6069-8fa5-3ef8-adf6-d646acbe75c1 | -7.13618 | -41.2615 | 2025-11-12 03:42:00 | NOAA-20 | GEMINIANO | PIAUÍ | Brasil | 2204352 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| f9f8ab07-3943-3356-b852-a8902fbb294f | -7.93273 | -36.24103 | 2025-11-12 03:42:00 | NOAA-20 | SANTA CRUZ DO CAPIBARIBE | PERNAMBUCO | Brasil | 2612505 | 26 | 33 | nan | nan | nan | Caatinga | 0.9 |
| a5d2f0af-b850-3159-8ca3-9d54fe497278 | -4.10453 | -48.01807 | 2025-11-12 03:42:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 18.6 |
| 057cb06c-979f-3ebf-a849-2e73506b75b6 | -9.18811 | -41.03075 | 2025-11-12 03:42:00 | NOAA-20 | CASA NOVA | BAHIA | Brasil | 2907202 | 29 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 0fea5850-ffbb-3b94-8d32-3ba40175b4b6 | -9.52401 | -42.93635 | 2025-11-12 03:42:00 | NOAA-20 | FARTURA DO PIAUÍ | PIAUÍ | Brasil | 2203750 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| eefa3fa4-6385-3457-be24-63d9ed3e9c5f | -4.99856 | -46.82533 | 2025-11-12 03:42:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 95b0d6b1-b36f-3bf0-a038-e4a0a5e7ff6f | -8.29097 | -43.84947 | 2025-11-12 03:42:00 | NOAA-20 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Caatinga | 3.8 |
| e62b4c41-7010-3246-84d8-3ccfdc32719e | -3.71591 | -45.82558 | 2025-11-12 03:42:00 | NOAA-20 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2a9402bb-57c7-314d-8f28-0faa74c4e15f | -7.60451 | -38.84556 | 2025-11-12 03:42:00 | NOAA-20 | BREJO SANTO | CEARÁ | Brasil | 2302503 | 23 | 33 | nan | nan | nan | Caatinga | 3.5 |
| c34f0e6d-23c3-3524-ad21-d52136c6daee | -7.28581 | -41.5779 | 2025-11-12 03:42:00 | NOAA-20 | AROEIRAS DO ITAIM | PIAUÍ | Brasil | 2200954 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 62d89f41-a754-3bf5-ba70-cc7108727445 | -4.92877 | -40.14201 | 2025-11-12 03:42:00 | NOAA-20 | MONSENHOR TABOSA | CEARÁ | Brasil | 2308609 | 23 | 33 | nan | nan | nan | Caatinga | 1.0 |
| e8095406-2b78-3eaa-9766-1d99f1927fcd | -4.99274 | -39.73006 | 2025-11-12 03:42:00 | NOAA-20 | BOA VIAGEM | CEARÁ | Brasil | 2302404 | 23 | 33 | nan | nan | nan | Caatinga | 0.7 |
| dfdb617a-ba60-367c-9420-a839b62e3c22 | -4.26212 | -44.60483 | 2025-11-12 03:42:00 | NOAA-20 | BACABAL | MARANHÃO | Brasil | 2101202 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 42ec1577-26a2-38ee-aab4-3ae426ae9f0a | -9.84104 | -36.03723 | 2025-11-12 03:42:00 | NOAA-20 | ROTEIRO | ALAGOAS | Brasil | 2707800 | 27 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| d1490c6e-9e9a-3843-99b8-03040a4f140e | -7.13756 | -41.25339 | 2025-11-12 03:42:00 | NOAA-20 | GEMINIANO | PIAUÍ | Brasil | 2204352 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| cd0e6fd9-1bf7-342a-bc42-0cfa459fb9ed | -7.53899 | -35.21051 | 2025-11-12 03:42:00 | NOAA-20 | ALIANÇA | PERNAMBUCO | Brasil | 2600708 | 26 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 92e12397-3d12-3774-a0b5-9dbf622c609b | -6.68326 | -35.07861 | 2025-11-12 03:42:00 | NOAA-20 | RIO TINTO | PARAÍBA | Brasil | 2512903 | 25 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 3301a538-31ca-3580-be91-39c4709252e7 | -6.51163 | -35.21747 | 2025-11-12 03:42:00 | NOAA-20 | PEDRO VELHO | RIO GRANDE DO NORTE | Brasil | 2409803 | 24 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| bdd26420-6677-38d7-9e08-684f330fa426 | -7.13399 | -41.2486 | 2025-11-12 03:42:00 | NOAA-20 | GEMINIANO | PIAUÍ | Brasil | 2204352 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| d43a652e-3416-3cd1-bf1e-c42f1a3d60bf | -6.51878 | -35.21506 | 2025-11-12 03:42:00 | NOAA-20 | PEDRO VELHO | RIO GRANDE DO NORTE | Brasil | 2409803 | 24 | 33 | nan | nan | nan | Mata Atlântica | 31.0 |
| 5e0783b0-bc17-38c8-ab23-405b5ebb8c4c | -6.9967 | -41.28917 | 2025-11-12 03:42:00 | NOAA-20 | SANTO ANTÔNIO DE LISBOA | PIAUÍ | Brasil | 2209401 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| b6b229a3-c69d-3d34-87f1-3e493fca1b15 | -3.96807 | -43.77843 | 2025-11-12 03:42:00 | NOAA-20 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 98df9018-ecaa-3f76-bcfa-3abb9bb58bcf | -8.0066 | -43.35295 | 2025-11-12 03:42:00 | NOAA-20 | PAVUSSU | PIAUÍ | Brasil | 2207850 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 5a753341-f2c2-3e37-842e-32f451b4ceaa | -5.09021 | -43.74188 | 2025-11-12 03:42:00 | NOAA-20 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 0197b0f3-29a9-3553-a160-cead62d005cb | -8.15387 | -36.00501 | 2025-11-12 03:42:00 | NOAA-20 | CARUARU | PERNAMBUCO | Brasil | 2604106 | 26 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 681982ce-2ee1-3c14-91cd-e28e6eb45531 | -5.22946 | -38.59149 | 2025-11-12 03:42:00 | NOAA-20 | MORADA NOVA | CEARÁ | Brasil | 2308708 | 23 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 86a53b2b-a48f-3068-9c89-17ce103d909a | -4.95405 | -43.74942 | 2025-11-12 03:42:00 | NOAA-20 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| f7b27331-c07c-36ec-baac-b15d234943b7 | -7.11194 | -35.13933 | 2025-11-12 03:42:00 | NOAA-20 | SAPÉ | PARAÍBA | Brasil | 2515302 | 25 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| bbdd09fc-22a3-365c-b44f-fdd26dc6782b | -10.26054 | -36.68958 | 2025-11-12 03:42:00 | NOAA-20 | IGREJA NOVA | ALAGOAS | Brasil | 2703205 | 27 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| f1d53250-3908-300f-804b-6f04cab4f9ee | -3.71552 | -45.82744 | 2025-11-12 03:42:00 | NOAA-20 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 0a19d804-202e-3c96-abd6-382825b2ec3a | -4.9323 | -44.29534 | 2025-11-12 03:42:00 | NOAA-20 | GOVERNADOR ARCHER | MARANHÃO | Brasil | 2104503 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| ebab7848-429e-32de-84fe-68a2953f9f07 | -9.05548 | -38.93574 | 2025-11-12 03:42:00 | NOAA-20 | MACURURÉ | BAHIA | Brasil | 2919900 | 29 | 33 | nan | nan | nan | Caatinga | 0.8 |
| e7d960a8-df30-3706-bbe1-84e7c3f6a629 | -7.06568 | -43.58568 | 2025-11-12 03:42:00 | NOAA-20 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 4e2c912b-0ced-3e90-a43b-49a64614b1e7 | -4.91064 | -44.32411 | 2025-11-12 03:42:00 | NOAA-20 | DOM PEDRO | MARANHÃO | Brasil | 2103802 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| f8aa3bc1-d9d9-31fa-9348-81091b3a8e1d | -3.97931 | -47.30622 | 2025-11-12 03:42:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 74c3477f-d8b1-3cf1-b16e-59796ac7dd15 | -4.93906 | -44.29709 | 2025-11-12 03:42:00 | NOAA-20 | GOVERNADOR ARCHER | MARANHÃO | Brasil | 2104503 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 59747408-cc9a-3bf0-986e-ad4e36c29507 | -4.0952 | -48.0303 | 2025-11-12 03:42:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 22.3 |
| 2204e390-9781-3e53-8ab6-641271d5b858 | -9.44993 | -44.88149 | 2025-11-12 03:42:00 | NOAA-20 | MONTE ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2206605 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| dcd92bb8-f9d2-3d60-8731-200afd2dc8ce | -4.40851 | -43.12542 | 2025-11-12 03:42:00 | NOAA-20 | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b7aefb2c-6b7a-3584-a547-a4e09de5a387 | -7.12837 | -41.86345 | 2025-11-12 03:42:00 | NOAA-20 | SANTA CRUZ DO PIAUÍ | PIAUÍ | Brasil | 2209104 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 1d89e1e8-d101-308f-9842-4ab0d238a019 | -7.00239 | -42.78877 | 2025-11-12 03:42:00 | NOAA-20 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 3.1 |
| 00c60ab4-8ea4-3f75-a233-2622b262fc9f | -4.59958 | -40.40022 | 2025-11-12 03:42:00 | NOAA-20 | NOVA RUSSAS | CEARÁ | Brasil | 2309300 | 23 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 5bcc84b1-1788-3f3f-b313-889ddd57ae8c | -9.6695 | -43.89885 | 2025-11-12 03:42:00 | NOAA-20 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| a149a6af-5fab-3244-853d-067985933303 | -6.47541 | -43.54454 | 2025-11-12 03:42:00 | NOAA-20 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 559a8241-6f7b-3ce8-be7b-ce227c2eef0a | -4.11147 | -48.01923 | 2025-11-12 03:42:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 18.6 |
| e99fd98f-24fb-3480-ba19-545972365443 | -6.09927 | -41.56939 | 2025-11-12 03:42:00 | NOAA-20 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| c79c9b25-cd15-3100-a09f-82d1f5b6fd78 | -6.90732 | -34.99326 | 2025-11-12 03:42:00 | NOAA-20 | RIO TINTO | PARAÍBA | Brasil | 2512903 | 25 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 8a1d3869-262c-34f1-bb45-53920e0278b2 | -4.75851 | -42.66422 | 2025-11-12 03:42:00 | NOAA-20 | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Caatinga | 3.1 |
| 2b41d056-c431-30f4-9bb0-a783cad2c5fa | -8.63313 | -39.92945 | 2025-11-12 03:42:00 | NOAA-20 | SANTA MARIA DA BOA VISTA | PERNAMBUCO | Brasil | 2612604 | 26 | 33 | nan | nan | nan | Caatinga | 1.1 |


[Clique aqui para ver as próximas entradas](README8.md)
