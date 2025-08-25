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

## Dados Diários - Página 22

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| f946deb7-3270-328b-a9b4-00741d2415d9 | -7.59414 | -45.23651 | 2025-08-25 04:14:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 391bc79a-c182-362b-bac2-a84502c11ae6 | -8.2863 | -47.24057 | 2025-08-25 04:14:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 51eb593e-4dd9-3688-b728-473ce2bc3dd3 | -6.32844 | -44.4476 | 2025-08-25 04:14:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| ee218a2e-7bc0-38f3-ac5e-113bfffe23c3 | -8.22038 | -49.56202 | 2025-08-25 04:14:00 | NOAA-21 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 74643f77-85e8-3821-b165-0b5e9a702dce | -6.79506 | -44.33686 | 2025-08-25 04:14:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 9e98b140-8249-37f7-867a-8f435abab727 | -6.04095 | -44.11272 | 2025-08-25 04:14:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 249866fe-0586-341c-bd65-43e030a683d5 | -6.30717 | -43.76203 | 2025-08-25 04:14:00 | NOAA-21 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 34749b0c-ae4f-3677-9867-8a4ccb901268 | -5.7973 | -45.40132 | 2025-08-25 04:14:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 6fba7be6-3b95-3615-8e66-af594b224fc3 | -7.69508 | -46.93002 | 2025-08-25 04:14:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 92414b90-53ea-3b31-917b-ca752b2ac7d8 | -5.55394 | -45.5602 | 2025-08-25 04:14:00 | NOAA-21 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 851820ef-f7d9-3c8e-a5dd-636b70fd04d2 | -5.94036 | -44.14727 | 2025-08-25 04:14:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 212eeed0-66f9-33f0-84d7-3733e5f11e0a | -8.38866 | -44.94881 | 2025-08-25 04:14:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f31ccf03-2ab7-357a-9be4-9269e80d0f85 | -3.45423 | -43.34255 | 2025-08-25 04:14:00 | NOAA-21 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| fa5a7a0d-7d28-3f6d-b480-1eb8b54e358c | -6.7845 | -44.31723 | 2025-08-25 04:14:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 16a090d0-f99b-3836-97a3-52694d370c9c | -6.88065 | -45.65577 | 2025-08-25 04:14:00 | NOAA-21 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 7e2209d4-20c9-3359-941e-22b3be7045e5 | -4.96421 | -55.80943 | 2025-08-25 04:14:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| ad5edbab-6016-36ba-8a8c-9e7d9a876976 | -6.03561 | -42.80206 | 2025-08-25 04:14:00 | NOAA-21 | ANGICAL DO PIAUÍ | PIAUÍ | Brasil | 2200608 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 5e997963-7aef-3b46-98c0-2ce89caa05e1 | -6.1671 | -43.00719 | 2025-08-25 04:14:00 | NOAA-21 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 522fd778-b0c9-3d1b-a5fa-056b1bc336b3 | -8.12827 | -47.12708 | 2025-08-25 04:14:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 58abc864-57cf-3bb1-bb50-89bfb1a6929b | -6.7945 | -44.3188 | 2025-08-25 04:14:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 2caccbc1-082c-338f-8756-ec453f2f0172 | -6.31216 | -43.77344 | 2025-08-25 04:14:00 | NOAA-21 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 41d2c55e-2345-31f1-9107-8063af19ff0c | -5.53295 | -36.84631 | 2025-08-25 04:14:00 | NOAA-21 | IPANGUAÇU | RIO GRANDE DO NORTE | Brasil | 2404705 | 24 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 129de728-9b91-385b-9d50-c0dfa418fb5c | -8.29448 | -46.36133 | 2025-08-25 04:14:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 6e237f2b-4cc5-3940-8844-98b24d0c0df6 | -5.94092 | -44.14373 | 2025-08-25 04:14:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 08aa16cc-7a25-3015-9906-eb8b9747e8ee | -7.66815 | -42.66875 | 2025-08-25 04:14:00 | NOAA-21 | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| f74c04c6-1da4-31b9-bcdb-986ecf66b482 | -10.08351 | -38.43095 | 2025-08-25 04:14:00 | NOAA-21 | JEREMOABO | BAHIA | Brasil | 2918100 | 29 | 33 | nan | nan | nan | Caatinga | 1.4 |
| f7fa6b58-6c9a-349b-9a97-14a79e975fdd | -7.66537 | -42.66471 | 2025-08-25 04:14:00 | NOAA-21 | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 3.2 |
| 903d7e5e-8bbc-324b-92b3-67f956a86049 | -7.32817 | -44.53424 | 2025-08-25 04:14:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 9dbc5bda-2212-3728-a4bc-dda3a52d2763 | -7.90507 | -42.5432 | 2025-08-25 04:14:00 | NOAA-21 | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 04d0e6d2-f47f-3ecc-ba50-764e93d2416e | -6.38522 | -43.26446 | 2025-08-25 04:14:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b97b808e-0a09-30a7-98c5-7c05ed0c41a3 | -6.0497 | -44.37791 | 2025-08-25 04:14:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 61bf5726-08d5-346c-8408-ef0d9f37415c | -8.0575 | -49.67555 | 2025-08-25 04:14:00 | NOAA-21 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 906420b0-1a8f-3d7e-bc5e-243b55e9cfa8 | -7.8191 | -46.88713 | 2025-08-25 04:14:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 63cdce45-195d-3c57-9d24-b503bd1e6784 | -6.30939 | -43.76947 | 2025-08-25 04:14:00 | NOAA-21 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| a5b37dd7-2655-38c0-bd60-9c0328fbba0e | -6.05771 | -43.6833 | 2025-08-25 04:14:00 | NOAA-21 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| e4600059-5c8f-3f97-a6e8-dbfdcddab35a | -7.54437 | -46.02196 | 2025-08-25 04:14:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 12.4 |
| e15384f7-b1b3-3dc6-a546-d1528387aa21 | -6.77176 | -44.31144 | 2025-08-25 04:14:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 29647014-161b-32b6-b8ab-4a97f9e6a345 | -3.42812 | -49.05093 | 2025-08-25 04:14:00 | NOAA-21 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 2c201523-6f9d-341f-a8a5-6809e7c36fdc | -6.19068 | -44.13311 | 2025-08-25 04:14:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 906c70cf-a452-330c-9ff3-73a4edce8a4e | -4.31091 | -48.097 | 2025-08-25 04:14:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| ecf1a3b9-7353-36ce-8e1c-8a59058d848c | -6.75206 | -50.96182 | 2025-08-25 04:14:00 | NOAA-21 | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 123bdbbd-0090-3a8a-83ad-cb4321030910 | -5.11213 | -43.20415 | 2025-08-25 04:14:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 22.5 |
| e005f170-9f69-3b3c-a9f7-da40ef9f5901 | -7.14889 | -44.16341 | 2025-08-25 04:14:00 | NOAA-21 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| ba084faf-9599-3343-8819-858e2d3ff025 | -6.2847 | -43.86163 | 2025-08-25 04:14:00 | NOAA-21 | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 99fc4824-cfc5-31ba-9290-9e48601841fa | -8.02554 | -44.98228 | 2025-08-25 04:14:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c30df0c4-bc0a-3e2d-b0aa-bbd15ab05fc3 | -8.06524 | -49.65601 | 2025-08-25 04:14:00 | NOAA-21 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| c965c6d3-3610-3bb9-bf0b-e2258291f18f | -5.38974 | -42.36368 | 2025-08-25 04:14:00 | NOAA-21 | BENEDITINOS | PIAUÍ | Brasil | 2201606 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| c5728ed4-c46b-36e6-abca-6038e8bcbbce | -6.33234 | -44.44459 | 2025-08-25 04:14:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c0988c76-86a7-3b48-b2ff-2ed1d447c6d5 | -4.30681 | -48.09633 | 2025-08-25 04:14:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2cd5d223-dc41-3f8e-928b-52568bd25aad | -6.01907 | -42.79953 | 2025-08-25 04:14:00 | NOAA-21 | ANGICAL DO PIAUÍ | PIAUÍ | Brasil | 2200608 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| b427be61-cb2d-3859-93c5-82323ad0c6dc | -5.68213 | -45.13577 | 2025-08-25 04:14:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 5ad316b8-83d0-3491-b143-b41cbbee0ed2 | -8.54263 | -48.86115 | 2025-08-25 04:14:00 | NOAA-21 | ITAPORÃ DO TOCANTINS | TOCANTINS | Brasil | 1711100 | 17 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e815b6c8-1fa9-306f-87b1-6666909c3d54 | -7.14336 | -44.15533 | 2025-08-25 04:14:00 | NOAA-21 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 6.0 |
| ecd69e29-16ac-326d-a89c-15c423fc373d | -5.85832 | -51.75457 | 2025-08-25 04:14:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 09ed710c-712a-346e-9107-a2452c865313 | -6.43789 | -44.55225 | 2025-08-25 04:14:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 4224f170-9297-3885-b612-b24f1038a8fc | -5.64905 | -43.44845 | 2025-08-25 04:14:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| e2c3ecaf-9d7b-34d0-bfa9-6da52f225bb5 | -6.90137 | -47.93231 | 2025-08-25 04:14:00 | NOAA-21 | WANDERLÂNDIA | TOCANTINS | Brasil | 1722081 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| a4b5e287-8780-3e24-a981-0c70f5d64d74 | -6.03593 | -43.99344 | 2025-08-25 04:14:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| f9692066-7ca2-36bf-b6a3-4f6aa30986b7 | -5.53338 | -41.28625 | 2025-08-25 04:14:00 | NOAA-21 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 8a2195b4-904a-305f-a60f-62b70b636a4e | -8.54606 | -48.8654 | 2025-08-25 04:14:00 | NOAA-21 | ITAPORÃ DO TOCANTINS | TOCANTINS | Brasil | 1711100 | 17 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 917cf050-6510-3554-82d5-9afb9ec6c7c3 | -5.25439 | -40.72856 | 2025-08-25 04:14:00 | NOAA-21 | CRATEÚS | CEARÁ | Brasil | 2304103 | 23 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 57d31eed-7e5b-3be5-9f44-8c7783b9785c | -5.45942 | -42.61635 | 2025-08-25 04:14:00 | NOAA-21 | LAGOA DO PIAUÍ | PIAUÍ | Brasil | 2205581 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 5f5c74ca-1939-30aa-9158-eab7f8e41b20 | -7.81839 | -46.89137 | 2025-08-25 04:14:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 3595a7bd-892d-330d-989b-500922827552 | -6.44237 | -44.56073 | 2025-08-25 04:14:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 7bd050e6-b8e9-36ae-ae15-95114a9e0b78 | -8.54786 | -48.85467 | 2025-08-25 04:14:00 | NOAA-21 | ITAPORÃ DO TOCANTINS | TOCANTINS | Brasil | 1711100 | 17 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 53224752-69ed-3db7-af90-74ea649cd7e6 | -7.66095 | -42.67125 | 2025-08-25 04:14:00 | NOAA-21 | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 924d093c-2dca-32b1-a351-3e8ea614e7d1 | -6.44068 | -44.55632 | 2025-08-25 04:14:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| cf30c206-9ef0-3758-950c-15ba8c33a077 | -7.18618 | -44.66124 | 2025-08-25 04:14:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 67507fe2-849b-36f9-b943-b0d89fe24147 | -7.09135 | -44.63153 | 2025-08-25 04:14:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 016f8a7c-52c7-3290-ade6-7e8af746c7c8 | -7.14613 | -44.15937 | 2025-08-25 04:14:00 | NOAA-21 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 77fcdf47-e1ec-3c37-98e9-00a39ff5fb4c | -6.91394 | -43.7771 | 2025-08-25 04:14:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 3.9 |
| b224856f-5c25-3e37-b5e4-d579a2724e6a | -8.75778 | -49.94785 | 2025-08-25 04:14:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 3af976a0-2fb9-3c0e-b99c-e8dc0912a74b | -6.21067 | -44.13615 | 2025-08-25 04:14:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 00bf9191-6943-3dfa-b3d3-33eac93eb86a | -5.89055 | -43.38366 | 2025-08-25 04:14:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 5f19b51c-f9e4-3750-89a8-a689964799d9 | -6.22121 | -44.11271 | 2025-08-25 04:14:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 032447af-2ee0-3981-9ef8-6c75adf3fcaf | -5.29974 | -45.26515 | 2025-08-25 04:14:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| bbc336ed-de04-3e3e-81f8-270800ea6dcf | -5.37021 | -41.20932 | 2025-08-25 04:14:00 | NOAA-21 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| cd67f3cd-77d5-3208-930d-1b6267261522 | -7.84894 | -49.99517 | 2025-08-25 04:14:00 | NOAA-21 | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| ce82d005-e8aa-3227-aa16-2a4ec575a964 | -5.91762 | -44.97901 | 2025-08-25 04:14:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| e984ea90-4f93-3a15-896e-9eeef5a7baf8 | -6.24977 | -43.73883 | 2025-08-25 04:14:00 | NOAA-21 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| e89b7e18-7df5-35be-8751-bf6ca16d8c0e | -7.59177 | -46.24278 | 2025-08-25 04:14:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 568ea532-ba2f-3ac2-a4c6-20856094ab19 | -9.52056 | -40.3088 | 2025-08-25 04:14:00 | NOAA-21 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 55cc532f-56e3-3e98-beb3-ca75e5c5ad93 | -9.52668 | -40.31879 | 2025-08-25 04:14:00 | NOAA-21 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 16b24991-e49f-3ddb-ab11-3816d1513a6d | -7.33428 | -44.53882 | 2025-08-25 04:14:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| e7a916bf-7181-3bca-81a5-87e8e5547a26 | -8.22146 | -47.17677 | 2025-08-25 04:14:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 4c72f2c0-14e4-3afb-ae4f-74a1147c6437 | -3.79914 | -51.18769 | 2025-08-25 04:14:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| badad4c9-bf2d-3c01-a41f-91333fff7822 | -5.97519 | -43.34032 | 2025-08-25 04:14:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 4c8c2f45-851d-362b-961f-c58166c78e8f | -5.68273 | -45.13204 | 2025-08-25 04:14:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 5e9d578d-b15d-3f12-8884-e4fc314cf8e4 | -4.8274 | -43.54495 | 2025-08-25 04:14:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b466ac0d-d2c7-3083-ba02-84f8ffad4e4f | -6.44294 | -44.55716 | 2025-08-25 04:14:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| be21b8d4-674e-3538-a483-04a708e006df | -8.07106 | -49.67358 | 2025-08-25 04:14:00 | NOAA-21 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 494d4b14-1028-398d-ab14-2bda20c2fca6 | -7.90173 | -42.54269 | 2025-08-25 04:14:00 | NOAA-21 | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| c758b0aa-a45d-3d71-8a5b-34bc197e0e1e | -8.38467 | -47.99349 | 2025-08-25 04:14:00 | NOAA-21 | ITAPIRATINS | TOCANTINS | Brasil | 1710904 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 3de96861-4810-30ec-82e0-6fedf23ad0a6 | -5.26741 | -42.73444 | 2025-08-25 04:14:00 | NOAA-21 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| a2edd999-1be9-3383-91ad-490706a4a99c | -8.05973 | -49.68833 | 2025-08-25 04:14:00 | NOAA-21 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 35.9 |
| 9cdb06f5-b845-3523-9349-1a206a63038f | -8.06081 | -47.30423 | 2025-08-25 04:14:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 82a7498c-d5fd-3d80-9c7b-425dc0948873 | -7.11087 | -44.63828 | 2025-08-25 04:14:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 12f15936-f8e0-3a06-a66f-63aff86ae21d | -6.27453 | -43.6894 | 2025-08-25 04:14:00 | NOAA-21 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ea21bea3-9e21-3ebf-bde6-63dcd8e80c05 | -5.64483 | -45.14911 | 2025-08-25 04:14:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| ebb1d79a-4525-307e-9362-86fbb8148bcf | -3.43255 | -49.05165 | 2025-08-25 04:14:00 | NOAA-21 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 13.9 |


[Clique aqui para ver as próximas entradas](README23.md)
