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

## Dados Diários - Página 9

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 2f512217-1d79-34b1-9f52-817c4fad937e | -6.8774 | -43.5919 | 2025-10-20 04:00:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 76.9 |
| efebc548-6f44-3e93-bbe2-b0c7371938ff | -6.8774 | -43.5919 | 2025-10-20 04:10:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 50.2 |
| f8cf1885-0598-356f-98b8-ac03273826f1 | -2.2527 | -51.9108 | 2025-10-20 04:10:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 99.2 |
| 002577f8-1559-3aea-8db3-a13824f1aa2a | -5.6198 | -43.6493 | 2025-10-20 04:10:00 | GOES-19 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 71.3 |
| 205bf550-5020-3a82-9d0f-a06a865d1197 | -9.6401 | -64.7411 | 2025-10-20 04:10:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 43.0 |
| ec9ccbf0-6eaa-36f0-a748-cd03a4ad8b61 | -2.2527 | -51.9313 | 2025-10-20 04:10:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 53.5 |
| d6b3237e-a974-378e-ba93-ef7c15dbaefc | 0.87585 | -51.25685 | 2025-10-20 04:10:00 | NOAA-20 | FERREIRA GOMES | AMAPÁ | Brasil | 1600238 | 16 | 33 | nan | nan | nan | Amazônia | 3.6 |
| a98fd793-d248-357a-a8fe-c70364c6747c | 0.87937 | -51.26019 | 2025-10-20 04:10:00 | NOAA-20 | FERREIRA GOMES | AMAPÁ | Brasil | 1600238 | 16 | 33 | nan | nan | nan | Amazônia | 4.6 |
| aad987ed-d7e2-3a85-b72b-a8200c60c657 | 1.08086 | -51.30783 | 2025-10-20 04:10:00 | NOAA-20 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 3.8 |
| cdec40c5-b33b-3f31-8325-ab32974a9a01 | 0.97784 | -51.15091 | 2025-10-20 04:10:00 | NOAA-20 | FERREIRA GOMES | AMAPÁ | Brasil | 1600238 | 16 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 334548fc-bdc0-36bd-a9ac-fea746268886 | 0.87878 | -51.25631 | 2025-10-20 04:10:00 | NOAA-20 | FERREIRA GOMES | AMAPÁ | Brasil | 1600238 | 16 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 56c006d1-5801-38ca-9237-4a12d4c91d5c | 1.08342 | -51.30957 | 2025-10-20 04:10:00 | NOAA-20 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 2.4 |
| e709818a-d2d6-30ef-9fa4-dfc7ab55fd56 | 0.9813 | -51.15131 | 2025-10-20 04:10:00 | NOAA-20 | FERREIRA GOMES | AMAPÁ | Brasil | 1600238 | 16 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 1606bda4-8177-3a23-9234-7ee064e1cb8a | 1.08284 | -51.30569 | 2025-10-20 04:10:00 | NOAA-20 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 2.6 |
| fa8e5d41-a159-3511-8356-c78f3ce48250 | 0.87646 | -51.2607 | 2025-10-20 04:10:00 | NOAA-20 | FERREIRA GOMES | AMAPÁ | Brasil | 1600238 | 16 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 695b74ac-4c7c-3288-9114-fe03fad0e018 | 0.97342 | -51.15932 | 2025-10-20 04:10:00 | NOAA-20 | FERREIRA GOMES | AMAPÁ | Brasil | 1600238 | 16 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 18e54c55-11ba-3de9-a6ec-0a8ff0f48015 | -5.50282 | -43.51288 | 2025-10-20 04:12:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| fc8fac51-7757-3411-92e6-f044d64fb1b6 | -3.48318 | -46.00596 | 2025-10-20 04:12:00 | NOAA-20 | GOVERNADOR NEWTON BELLO | MARANHÃO | Brasil | 2104651 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 33b0e894-9aac-32f1-8739-96ef55ae0a57 | -2.25228 | -51.92146 | 2025-10-20 04:12:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 7.6 |
| b004437c-53c5-3a66-95ba-9d8c03dd8612 | -6.2369 | -44.68861 | 2025-10-20 04:12:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 1ce036e0-f4ce-39dc-ac74-e508dcdc70cb | -5.62495 | -43.64372 | 2025-10-20 04:12:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 5.1 |
| d31ed4f0-9768-3203-aedd-c62dd67f0221 | -7.5331 | -46.09374 | 2025-10-20 04:12:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 11.4 |
| 08b03556-7236-33b2-a85d-b9f38d9e4161 | -6.34048 | -41.5547 | 2025-10-20 04:12:00 | NOAA-20 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| f793ba39-3898-3349-a8fd-f9f7d37b9a73 | -1.44555 | -48.89257 | 2025-10-20 04:12:00 | NOAA-20 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 4a8b848d-1523-3e6c-9367-c96ab336a4a0 | -2.24857 | -51.90915 | 2025-10-20 04:12:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| b2818cf0-ee45-35af-9a96-c534f70d1d33 | -8.27616 | -42.94835 | 2025-10-20 04:12:00 | NOAA-20 | TAMBORIL DO PIAUÍ | PIAUÍ | Brasil | 2210953 | 22 | 33 | nan | nan | nan | Caatinga | 0.4 |
| a2429c3a-9ac3-30d9-9f77-c9d39743f0d2 | -3.4839 | -46.00152 | 2025-10-20 04:12:00 | NOAA-20 | GOVERNADOR NEWTON BELLO | MARANHÃO | Brasil | 2104651 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 933180d0-a985-3dd3-82c6-f6590b3bdc2a | -5.88605 | -43.92336 | 2025-10-20 04:12:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 60fca58a-1a71-3ef7-ba45-269d27fa75ec | -2.26915 | -51.92426 | 2025-10-20 04:12:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 245079bf-3ccd-3c02-b3fd-318fe5db167c | -5.24298 | -46.14974 | 2025-10-20 04:12:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| de136d0e-94d0-34d6-9e4d-9b49b1af80ec | -7.12869 | -44.24849 | 2025-10-20 04:12:00 | NOAA-20 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| cd628741-b0b8-39d8-b6e7-520106200d01 | -5.36736 | -42.8032 | 2025-10-20 04:12:00 | NOAA-20 | NAZÁRIA | PIAUÍ | Brasil | 2206720 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| f074d43c-ca74-35f4-bd9b-0727cca31369 | -5.6205 | -43.65021 | 2025-10-20 04:12:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 91880e45-5b81-3154-9193-d1983add9834 | -2.25356 | -51.91383 | 2025-10-20 04:12:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 10.9 |
| 64f8387b-3a2c-31ca-9844-430dec091eff | -6.20652 | -40.96938 | 2025-10-20 04:12:00 | NOAA-20 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| f550bc71-37fe-3830-b5bb-75b49b18856f | -4.48047 | -45.30008 | 2025-10-20 04:12:00 | NOAA-20 | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b5aae8cf-f189-3793-b734-4c5ad866df19 | -2.24793 | -51.91292 | 2025-10-20 04:12:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 10.9 |
| 3d63d69d-e253-3c0f-9c9d-1c729c07eaaf | -6.3625 | -46.15452 | 2025-10-20 04:12:00 | NOAA-20 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| b8ea81ca-73b6-3cf0-a8ac-743bc91cae03 | -4.47918 | -45.30811 | 2025-10-20 04:12:00 | NOAA-20 | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 53a1e0d8-2d39-3eba-95c0-d082e8b6d47f | -7.41652 | -40.06856 | 2025-10-20 04:12:00 | NOAA-20 | BODOCÓ | PERNAMBUCO | Brasil | 2602001 | 26 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 88856330-b6fe-35f2-a41b-bb50d6c4e02b | -4.44423 | -44.69183 | 2025-10-20 04:12:00 | NOAA-20 | SÃO LUÍS GONZAGA DO MARANHÃO | MARANHÃO | Brasil | 2111409 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| a9063149-d806-3b12-88f1-b072c1b735b2 | -5.42662 | -45.85122 | 2025-10-20 04:12:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 98275552-a4c8-362b-9c57-3df71787d94b | -2.25292 | -51.91764 | 2025-10-20 04:12:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 10.9 |
| 6d0c5533-fe42-31aa-87ba-e2d261691e57 | -7.53238 | -46.09276 | 2025-10-20 04:12:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 10.0 |
| 44ac86e8-a021-3788-b7d6-87e43137b39a | -7.20899 | -45.41959 | 2025-10-20 04:12:00 | NOAA-20 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 09877f02-bc36-3469-8f04-4873063cccf1 | -7.48482 | -45.08706 | 2025-10-20 04:12:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c790cce0-d801-31b5-b6ce-54f05988f6d3 | -5.61717 | -43.64968 | 2025-10-20 04:12:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 278b8857-b7e9-3dd7-b71d-478b6c938e9e | -5.09098 | -45.88587 | 2025-10-20 04:12:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 0f9ca9e1-6a4a-3af4-8619-d866b8c1e006 | -6.48996 | -43.63112 | 2025-10-20 04:12:00 | NOAA-20 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| ec7d4eec-12b9-3db2-98e6-8a0622159c29 | -6.10142 | -44.02258 | 2025-10-20 04:12:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 608238ab-7f27-357f-935f-a3740d1b9cb3 | -7.48051 | -42.73727 | 2025-10-20 04:12:00 | NOAA-20 | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| e5afac94-f3bb-38f7-b135-66b7c7cfd6e1 | -5.61329 | -43.65266 | 2025-10-20 04:12:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 79731221-40b8-3892-8256-8f8379038e4b | -2.90532 | -48.90542 | 2025-10-20 04:12:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 79776866-4a4f-30fa-8936-fb8ce30d13aa | -6.23388 | -44.14585 | 2025-10-20 04:12:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 921cf009-291f-32d9-b56b-b0ba415016de | -5.61952 | -46.41537 | 2025-10-20 04:12:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 7310ca11-108a-345f-bfb4-675aaf9fb359 | -8.00183 | -39.62831 | 2025-10-20 04:12:00 | NOAA-20 | PARNAMIRIM | PERNAMBUCO | Brasil | 2610400 | 26 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 2b58495a-3800-3e32-807d-3b8a37dd6f5c | -4.25391 | -44.28302 | 2025-10-20 04:12:00 | NOAA-20 | ALTO ALEGRE DO MARANHÃO | MARANHÃO | Brasil | 2100436 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 8b699b95-5708-3bea-8b30-3f0445ddee74 | -7.14554 | -46.5198 | 2025-10-20 04:12:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f6b2cc7c-bed2-34fd-a461-181c5a65ed63 | -5.33672 | -42.93264 | 2025-10-20 04:12:00 | NOAA-20 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 724294f1-389c-397f-9af6-1a54659e8446 | -5.36626 | -45.51129 | 2025-10-20 04:12:00 | NOAA-20 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| e23274db-eef5-3f35-9b9b-d04b97020c4d | -1.44189 | -48.89422 | 2025-10-20 04:12:00 | NOAA-20 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 7ad2bfbb-fa05-30b9-a73d-e3fda436930e | -5.58981 | -42.70734 | 2025-10-20 04:12:00 | NOAA-20 | MONSENHOR GIL | PIAUÍ | Brasil | 2206407 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 40736278-7841-36d2-984f-027c3c65f9c4 | -7.49824 | -43.8927 | 2025-10-20 04:12:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| fdf93728-f7e2-3770-8632-733e092853f2 | -2.43384 | -48.62103 | 2025-10-20 04:12:00 | NOAA-20 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 00772e78-3efa-33f1-8be0-738b12413e9e | -4.15127 | -42.17691 | 2025-10-20 04:12:00 | NOAA-20 | BATALHA | PIAUÍ | Brasil | 2201507 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 8bbd21f3-bfe4-33f4-b992-e4d123c55f13 | -6.1042 | -44.02664 | 2025-10-20 04:12:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| fec3858c-bedb-3230-9583-6ad61d86719d | -6.3108 | -40.90503 | 2025-10-20 04:12:00 | NOAA-20 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| d03c62e3-a35c-37df-a8c7-f79170b8240f | -8.47318 | -39.50906 | 2025-10-20 04:12:00 | NOAA-20 | CABROBÓ | PERNAMBUCO | Brasil | 2603009 | 26 | 33 | nan | nan | nan | Caatinga | 2.1 |
| a9221034-73e3-31e3-80ca-c6d982a7b7c7 | -4.82265 | -43.06717 | 2025-10-20 04:12:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 765afba1-27ba-3876-9bda-54cf1663eb9a | -6.54177 | -43.68885 | 2025-10-20 04:12:00 | NOAA-20 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 37f6ca2f-e1d8-3c64-963f-de006d911709 | -6.21407 | -41.53559 | 2025-10-20 04:12:00 | NOAA-20 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 93f4f622-b068-32ed-ae87-7cac19296340 | -4.40161 | -43.32057 | 2025-10-20 04:12:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d0e34ed6-1bd0-3933-8890-9985a476cd20 | -7.54374 | -46.09043 | 2025-10-20 04:12:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| cd3ace9b-e47b-384e-9859-794e5fb5aac4 | -4.82596 | -43.06768 | 2025-10-20 04:12:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 45093208-5f21-3bf3-965c-0b8a56353c58 | -7.99812 | -39.62775 | 2025-10-20 04:12:00 | NOAA-20 | PARNAMIRIM | PERNAMBUCO | Brasil | 2610400 | 26 | 33 | nan | nan | nan | Caatinga | 2.2 |
| af30d5ca-cb2a-3bfc-acde-7bbda3fc5644 | -5.08668 | -45.88939 | 2025-10-20 04:12:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 8e88eadc-96d6-3d80-b23f-1714edc28df7 | -6.13354 | -41.73108 | 2025-10-20 04:12:00 | NOAA-20 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| f181c252-5358-3b9f-9d30-70cb4dc63a3c | -4.89099 | -42.93629 | 2025-10-20 04:12:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| f031a047-83e2-3402-973e-e54cfc74d66f | -4.90034 | -45.52901 | 2025-10-20 04:12:00 | NOAA-20 | LAGOA GRANDE DO MARANHÃO | MARANHÃO | Brasil | 2105963 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 62e13b7c-5459-3c05-ae17-277736ccdddd | -7.54442 | -46.08637 | 2025-10-20 04:12:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 656f81b2-5d32-3b03-a28f-0037a18feba8 | -7.13204 | -44.24902 | 2025-10-20 04:12:00 | NOAA-20 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| b2c443ec-94db-39c7-9e24-71cccf17b4bd | -5.03807 | -45.12144 | 2025-10-20 04:12:00 | NOAA-20 | SÃO RAIMUNDO DO DOCA BEZERRA | MARANHÃO | Brasil | 2111631 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 91aacad9-472a-3631-bc41-850199e1d069 | -4.33531 | -43.61323 | 2025-10-20 04:12:00 | NOAA-20 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 9d21970b-ecb6-3b7b-898e-771bf42511cc | -4.60873 | -45.92424 | 2025-10-20 04:12:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 8a79733c-e378-3ca9-8e34-62761ea63e98 | -5.6255 | -43.64022 | 2025-10-20 04:12:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 5.1 |
| cf3a9121-5fc3-3912-be75-feaa09ea4ecd | -4.27651 | -43.42341 | 2025-10-20 04:12:00 | NOAA-20 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 8175edcc-13b7-35b8-96ed-f51cbadc3bc9 | -2.43903 | -48.61729 | 2025-10-20 04:12:00 | NOAA-20 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 6794f794-cfad-3d5a-9509-fb12705f3541 | -6.28529 | -44.41586 | 2025-10-20 04:12:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 9de7fbdd-f3f9-36b3-b225-09c5de47ea9d | -6.20596 | -40.97307 | 2025-10-20 04:12:00 | NOAA-20 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 989af1b4-f550-30aa-a4fa-01eddbaae75d | -2.24773 | -51.92852 | 2025-10-20 04:12:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| b2402868-4df2-3306-99de-c1e450464762 | -6.21335 | -40.97044 | 2025-10-20 04:12:00 | NOAA-20 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 5cf54635-0909-3e64-9277-b793b7e70543 | -6.39647 | -38.28556 | 2025-10-20 04:12:00 | NOAA-20 | PARANÁ | RIO GRANDE DO NORTE | Brasil | 2408607 | 24 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 0eb71daf-791a-357f-89b1-4a493f8014db | -3.09831 | -51.28275 | 2025-10-20 04:12:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| f494df23-d970-3980-8656-de846090717c | -7.47775 | -42.73328 | 2025-10-20 04:12:00 | NOAA-20 | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| c266cde0-8a66-36a8-a6f0-12fa9937de95 | -4.89677 | -45.52843 | 2025-10-20 04:12:00 | NOAA-20 | LAGOA GRANDE DO MARANHÃO | MARANHÃO | Brasil | 2105963 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 25bf1e94-bafa-3340-aa09-4fe6a5831e4f | -4.75242 | -46.85876 | 2025-10-20 04:12:00 | NOAA-20 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8bdba4d9-a75e-3b80-b630-8d9d0134d2a3 | -5.60996 | -43.65214 | 2025-10-20 04:12:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 3b483cd1-381e-3fe4-b79c-037f4ce6b79f | -4.33866 | -43.61376 | 2025-10-20 04:12:00 | NOAA-20 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 7637ed2c-1639-3038-8c8e-6cbfa2caf052 | -6.30566 | -40.89278 | 2025-10-20 04:12:00 | NOAA-20 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 3bc1c181-bcc6-3ca7-ac18-bc3b1df76ef1 | -2.25076 | -51.90959 | 2025-10-20 04:12:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 11.2 |


[Clique aqui para ver as próximas entradas](README10.md)
