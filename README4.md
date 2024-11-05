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

## Dados Diários - Página 4

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 2cb517d8-8b43-31f0-a598-a076169b9eb6 | -3.8839 | -46.602699 | 2024-11-05 00:20:00 | METOP-B | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 9bdb784d-49f6-3054-83e2-5cc466ccb584 | -3.1784 | -50.576099 | 2024-11-05 00:20:00 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 43999758-468a-3606-a28b-5da20bdfe763 | -14.2708 | -43.213001 | 2024-11-05 00:20:00 | METOP-B | PALMAS DE MONTE ALTO | BAHIA | Brasil | 2923407 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| 9a353f4b-f9b9-336f-82b4-cb7ca10b2eba | -4.4077 | -43.1222 | 2024-11-05 00:20:00 | METOP-B | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| f4c923ce-cf1b-3d54-ac79-ac62ab1cfe75 | -3.6199 | -39.231998 | 2024-11-05 00:20:00 | METOP-B | SÃO LUÍS DO CURU | CEARÁ | Brasil | 2312601 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| e9c300b9-827e-374a-8f5f-1984bb2150ab | -3.4754 | -45.528702 | 2024-11-05 00:20:00 | METOP-B | MONÇÃO | MARANHÃO | Brasil | 2106904 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 1a0a9aa8-7599-3235-a3cd-45ce1c467d2e | -4.4035 | -43.104099 | 2024-11-05 00:20:00 | METOP-B | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 51d93398-b2e2-33a7-8ba2-a65988d6d0aa | 3.6288 | -51.296902 | 2024-11-05 00:20:00 | METOP-B | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | nan |
| 491fa1b7-904d-34bd-be7d-017d8e1c467b | -4.5926 | -48.0588 | 2024-11-05 00:20:00 | METOP-B | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a7cef834-52b6-389f-85fd-2b055f861a80 | -3.9599 | -48.360001 | 2024-11-05 00:20:00 | METOP-B | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 904d8f0e-af90-342c-995a-8a76dab7d9c6 | -4.2459 | -44.929699 | 2024-11-05 00:20:00 | METOP-B | BACABAL | MARANHÃO | Brasil | 2101202 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| b08fd418-64b3-303d-86b2-9bc430a77747 | -5.8039 | -44.125301 | 2024-11-05 00:20:00 | METOP-B | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 967b7e45-e378-395e-b6fd-b0775bd8863d | -4.8111 | -43.218201 | 2024-11-05 00:20:00 | METOP-B | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 04d81183-421b-36d6-82c3-4a96c028a0f2 | -1.4005 | -52.186501 | 2024-11-05 00:20:00 | METOP-B | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3cae72e4-3d91-385b-9431-6a336aafa238 | -3.4639 | -45.523602 | 2024-11-05 00:20:00 | METOP-B | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 578a26cb-7596-3ad5-a444-4b19ab665295 | -5.3118 | -43.333099 | 2024-11-05 00:20:00 | METOP-B | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| f69ae1bd-4b05-3566-9a0f-20eec5643c9a | -3.9702 | -48.130402 | 2024-11-05 00:20:00 | METOP-B | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a94ec15a-c058-39a2-b061-409d00c153d4 | -3.5486 | -44.629299 | 2024-11-05 00:20:00 | METOP-B | ARARI | MARANHÃO | Brasil | 2101004 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 14d6fea4-e064-3328-b789-2b919b79d743 | -3.1765 | -50.567699 | 2024-11-05 00:20:00 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b3c29b22-8da3-3c64-b8a9-56825574969e | -3.9635 | -48.1464 | 2024-11-05 00:20:00 | METOP-B | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3f293fdc-b725-3435-be6d-4cd1ebcb32cc | -3.962 | -48.1395 | 2024-11-05 00:20:00 | METOP-B | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4bacf839-2b40-3ebc-aed4-5ba483d693ea | -8.4638 | -45.479401 | 2024-11-05 00:20:00 | METOP-B | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| f81daba4-1739-31ce-9a5f-e9cde5ea8295 | -4.1387 | -48.745701 | 2024-11-05 00:20:00 | METOP-B | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 68cfdf45-dd32-3aa8-b2f8-44207d829e2c | -3.5898 | -50.253399 | 2024-11-05 00:20:00 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 705cee82-dfeb-3583-b8c0-17b1a444e048 | -3.4079 | -50.267601 | 2024-11-05 00:20:00 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6366fcce-71a3-39ec-a807-2ddaf2fa176c | -4.2263 | -44.934101 | 2024-11-05 00:20:00 | METOP-B | BACABAL | MARANHÃO | Brasil | 2101202 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 62fbdee4-99a9-38f2-be46-bcf154a5d709 | -10.8058 | -44.485298 | 2024-11-05 00:20:00 | METOP-B | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| d31dd7ce-6f89-3a39-b402-284ce6849872 | -5.6959 | -45.8195 | 2024-11-05 00:20:00 | METOP-B | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| f5518a9b-3e00-3cd6-8a4d-edb007804273 | -4.4132 | -43.101799 | 2024-11-05 00:20:00 | METOP-B | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 6a7b86f9-6ca5-3957-9921-2f0cbe0ce02e | -4.3484 | -48.624199 | 2024-11-05 00:20:00 | METOP-B | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a083147e-4522-335b-8078-b07c79235958 | -4.3678 | -47.882401 | 2024-11-05 00:20:00 | METOP-B | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6b46c7a5-2a25-3e27-9f90-644adcf2b4a8 | -5.3717 | -46.436298 | 2024-11-05 00:20:00 | METOP-B | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| d5114037-fc96-3631-8fd8-b8851d85c848 | -3.0882 | -54.4781 | 2024-11-05 00:20:00 | METOP-B | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 33f867fa-fe8b-38f9-8687-3fde8c599f56 | -5.0628 | -44.2201 | 2024-11-05 00:20:00 | METOP-B | GOVERNADOR ARCHER | MARANHÃO | Brasil | 2104503 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| cebcebe0-b813-3904-a02f-d01e5818476f | -3.86 | -45.9963 | 2024-11-05 00:20:00 | METOP-B | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| df597bd8-2359-32f0-bac0-e09066ff44bc | -3.9539 | -45.819801 | 2024-11-05 00:20:00 | METOP-B | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 08d5a4b8-5315-3721-bf08-e8ac3a112e33 | -5.8358 | -43.637501 | 2024-11-05 00:20:00 | METOP-B | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| cc1fc79b-0800-3db7-bf17-dcadb8c720c3 | -3.4524 | -47.659302 | 2024-11-05 00:20:00 | METOP-B | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a3dedbac-dbc8-368d-803e-f14172c87a71 | -4.355 | -48.6077 | 2024-11-05 00:20:00 | METOP-B | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4a1d15f0-0ff8-3201-b5bf-0bdc1bd75cd7 | -5.6892 | -45.835602 | 2024-11-05 00:20:00 | METOP-B | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 933bb9c5-92ff-3049-b6da-194ee48f2d7f | -4.35 | -48.631401 | 2024-11-05 00:20:00 | METOP-B | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e7b12ab5-4b1a-343e-8971-2350da927006 | -3.1901 | -50.582199 | 2024-11-05 00:20:00 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 098a0e97-507f-3435-8e68-233df069449f | -1.3962 | -52.167099 | 2024-11-05 00:20:00 | METOP-B | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0bd806c6-fc43-3490-a262-ba6ee1fa6020 | -5.0646 | -44.228001 | 2024-11-05 00:20:00 | METOP-B | GOVERNADOR ARCHER | MARANHÃO | Brasil | 2104503 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| b8b0f13a-9493-38d1-bede-379f72c67a99 | -2.8558 | -45.614101 | 2024-11-05 00:20:00 | METOP-B | SANTA HELENA | MARANHÃO | Brasil | 2109809 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| ffe744eb-a7c9-37bd-ad0c-64567512ee6a | -5.383 | -46.440899 | 2024-11-05 00:20:00 | METOP-B | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 452e132f-2b5f-3823-8d54-cc9c16ff4e1f | -4.0008 | -49.9282 | 2024-11-05 00:20:00 | METOP-B | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a36aaf52-02d9-3637-8d60-2d2dd950d219 | -3.2092 | -50.621899 | 2024-11-05 00:20:00 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 27e4bf93-b370-3faa-b3da-c717aac1c2ae | -3.9718 | -48.137299 | 2024-11-05 00:20:00 | METOP-B | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b40078cf-c5d7-3f85-88de-fb01627dd9bf | -3.2396 | -50.527802 | 2024-11-05 00:20:00 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| fb35666a-2644-31a3-a1a2-2c40a77dcf05 | -5.3019 | -43.068001 | 2024-11-05 00:20:00 | METOP-B | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 24b7886c-daae-3914-98d1-5ba50152d846 | -5.4759 | -48.603901 | 2024-11-05 00:20:00 | METOP-B | SÃO JOÃO DO ARAGUAIA | PARÁ | Brasil | 1507508 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f7f7de48-3985-3669-b1ab-607a29eb95cc | -10.6738 | -45.041599 | 2024-11-05 00:20:00 | METOP-B | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 5fc3d722-346f-3fec-bc22-525a48ffe97f | -10.3672 | -45.053101 | 2024-11-05 00:20:00 | METOP-B | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 46e4579d-fe81-38b4-b55c-db7163141133 | -1.4869 | -47.214699 | 2024-11-05 00:20:00 | METOP-B | OURÉM | PARÁ | Brasil | 1505403 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4aff8f22-c1a8-3a51-8b24-cd13746cd629 | -3.3053 | -50.1301 | 2024-11-05 00:20:00 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f6d501ea-6f11-30ec-941f-2099b0cbfa77 | -10.3688 | -45.060001 | 2024-11-05 00:20:00 | METOP-B | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 94186afd-b23e-34f8-b185-6ca968d53b3b | -5.8991 | -46.0797 | 2024-11-05 00:20:00 | METOP-B | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 2c62848c-a2d3-3512-9949-37f0e30a2971 | -5.3207 | -44.086601 | 2024-11-05 00:20:00 | METOP-B | SENADOR ALEXANDRE COSTA | MARANHÃO | Brasil | 2111748 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| a7783c2d-b1fc-3273-86eb-0352a083385a | -10.6838 | -44.766499 | 2024-11-05 00:20:00 | METOP-B | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| c7bc1e6c-8b4b-3b39-9d13-949cf19fec6a | -1.1435 | -52.002602 | 2024-11-05 00:20:00 | METOP-B | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | nan |
| ac43a334-419a-3c50-bd83-c5984ad469a3 | -3.1803 | -50.5844 | 2024-11-05 00:20:00 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a5d9b49c-46da-3b24-8caa-36dbd08475f6 | -5.3815 | -46.434101 | 2024-11-05 00:20:00 | METOP-B | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 68f7e9c4-69dd-3ae8-b014-292507afde3a | -4.7225 | -46.437099 | 2024-11-05 00:20:00 | METOP-B | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 1000f944-2169-3ce1-bbee-cca5c1295596 | -3.7338 | -44.5382 | 2024-11-05 00:20:00 | METOP-B | MATÕES DO NORTE | MARANHÃO | Brasil | 2106631 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 5c85f852-7510-31a0-905b-1ccbed47724f | -2.8155 | -52.918701 | 2024-11-05 00:20:00 | METOP-B | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| da9ced08-68ed-3e17-842f-51115a658f35 | -1.0373 | -47.779301 | 2024-11-05 00:20:00 | METOP-B | TERRA ALTA | PARÁ | Brasil | 1507961 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 324ac1ca-ef15-37aa-9d3d-5b603a6d5f75 | -4.0796 | -48.296799 | 2024-11-05 00:20:00 | METOP-B | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 28fa563f-d6f7-329c-be27-05affc79b769 | -5.4486 | -43.2561 | 2024-11-05 00:20:00 | METOP-B | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 0260738c-a551-3c76-8258-62b95cc60935 | -6.117 | -43.962601 | 2024-11-05 00:20:00 | METOP-B | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 2ece7ecd-949f-3eae-9cb3-50b32a3354d7 | -1.5153 | -47.294498 | 2024-11-05 00:20:00 | METOP-B | BONITO | PARÁ | Brasil | 1501600 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6aa0c440-b647-381e-bd4a-24d7117827a5 | -10.3401 | -45.1619 | 2024-11-05 00:20:00 | METOP-B | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 27366cdf-ac32-397f-882a-fe13b2b88fa7 | -4.8841 | -46.696201 | 2024-11-05 00:20:00 | METOP-B | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| f8978649-4066-3bd4-9acf-0449792ef321 | -5.8506 | -39.416302 | 2024-11-05 00:20:00 | METOP-B | PIQUET CARNEIRO | CEARÁ | Brasil | 2310902 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| a1a5fc35-d7d8-39c3-b334-b36e9c2f7a34 | -4.603 | -46.866402 | 2024-11-05 00:20:00 | METOP-B | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 8f457438-6858-3ed7-ad44-5a1e6e21716d | -4.008 | -43.622299 | 2024-11-05 00:20:00 | METOP-B | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| f32167fb-8e00-38ee-b1bd-f5a788a48707 | -11.987 | -42.888 | 2024-11-05 00:20:00 | METOP-B | OLIVEIRA DOS BREJINHOS | BAHIA | Brasil | 2923209 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| 39f130b8-18d9-33c6-8a33-e0b5d6a65e3a | -12.0317 | -43.9356 | 2024-11-05 00:20:00 | METOP-B | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 6d0db35e-b38b-35db-ba16-12f7443d1653 | -3.484 | -46.065701 | 2024-11-05 00:20:00 | METOP-B | GOVERNADOR NEWTON BELLO | MARANHÃO | Brasil | 2104651 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 68bae4a4-e590-36f6-aa2c-f81d1cc6a1f8 | -2.1861 | -46.523899 | 2024-11-05 00:20:00 | METOP-B | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d68d1826-5492-31f7-b1a0-83cf3d7f8471 | -4.7241 | -46.444 | 2024-11-05 00:20:00 | METOP-B | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 45b079f5-ff50-3b7a-b11f-6f65beb73868 | -4.2362 | -48.536499 | 2024-11-05 00:20:00 | METOP-B | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f3f69c03-e586-3bb9-8780-eb2f1b0fe5f2 | -10.3568 | -44.234699 | 2024-11-05 00:20:00 | METOP-B | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 46beca44-42a7-33e8-afd4-0cee731796b6 | -2.8253 | -52.916599 | 2024-11-05 00:20:00 | METOP-B | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 604f4712-cc3f-3144-bc29-eeec6af7670a | -4.8336 | -44.93 | 2024-11-05 00:20:00 | METOP-B | ESPERANTINÓPOLIS | MARANHÃO | Brasil | 2104008 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 9d1bb80c-929f-3eb7-b072-3dd37f9593ac | -2.92 | -49.326199 | 2024-11-05 00:20:00 | METOP-B | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a0741f60-9afa-3281-a492-e6ad43c67073 | -4.2361 | -44.9319 | 2024-11-05 00:20:00 | METOP-B | BACABAL | MARANHÃO | Brasil | 2101202 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| a385330a-a31b-3b66-b495-dacbecfca078 | -4.4072 | -43.4767 | 2024-11-05 00:20:00 | METOP-B | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| fd7bc1a9-1351-3e8a-9688-bcc068dc896f | -6.5237 | -45.9249 | 2024-11-05 00:20:00 | METOP-B | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 46651e3c-5aab-3f1e-ac04-09f83169c750 | -6.1848 | -39.2244 | 2024-11-05 00:20:00 | METOP-B | QUIXELÔ | CEARÁ | Brasil | 2311355 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| 05975cef-dadb-3ceb-bea1-b9dab6ecc08b | 0.1983 | -51.068802 | 2024-11-05 00:20:00 | METOP-B | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | nan |
| 03356bd5-4246-385c-82fa-e0c1ce7b7875 | -8.3218 | -43.594398 | 2024-11-05 00:20:00 | METOP-B | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| bf6a2433-9955-32af-aa22-d926cfe51776 | -2.8065 | -51.768101 | 2024-11-05 00:20:00 | METOP-B | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 57b3bd60-1251-3125-a449-01eee5481531 | -1.5184 | -53.491501 | 2024-11-05 00:20:00 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 11259377-025d-3616-87e1-d6e5103c1909 | -4.3763 | -47.232201 | 2024-11-05 00:20:00 | METOP-B | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 84c8bfdc-7148-3501-956b-b52b4123498e | -4.837 | -44.944801 | 2024-11-05 00:20:00 | METOP-B | ESPERANTINÓPOLIS | MARANHÃO | Brasil | 2104008 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| a425e5e1-a5ef-329f-b7d5-f2d64808ee52 | -3.9534 | -46.3629 | 2024-11-05 00:20:00 | METOP-B | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 0c5c4fce-bb72-325f-9210-3d490b6dd27c | -5.7687 | -46.369099 | 2024-11-05 00:20:00 | METOP-B | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 5a1b6e7d-2ad2-30e4-aa67-1ec0e8d5d659 | -4.051 | -46.9319 | 2024-11-05 00:20:00 | METOP-B | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 6d5aabc8-ca24-3bf6-9e12-341930edb363 | -4.5126 | -44.068699 | 2024-11-05 00:20:00 | METOP-B | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | nan |


[Clique aqui para ver as próximas entradas](README5.md)
