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

## Dados Diários - Página 42

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 5575fef4-98c9-3764-b84b-a64c0d5046bd | 1.74969 | -55.77856 | 2025-10-16 04:36:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e880368c-6115-3801-b306-dfa006174e16 | 1.74644 | -55.79085 | 2025-10-16 04:36:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 0e723b1a-3e8a-30c4-85d1-0d4d9e775067 | 1.84317 | -55.71767 | 2025-10-16 04:36:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a9fac0fa-3608-38c0-b664-10de0fab8750 | 1.81712 | -55.74806 | 2025-10-16 04:36:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 607fb969-7212-3844-8641-0190b977946b | 1.19941 | -51.28508 | 2025-10-16 04:36:00 | NOAA-21 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 2a3776fc-6f1c-3b48-bf78-111a7ca62612 | 1.08079 | -51.00233 | 2025-10-16 04:36:00 | NOAA-21 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 499537fa-0c33-38ab-913c-a7279727473d | 1.82211 | -55.74728 | 2025-10-16 04:36:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| cbb53034-2012-3a2c-b458-b4fa2d666b73 | 1.79435 | -55.73677 | 2025-10-16 04:36:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 5942cef6-d4f5-376a-8483-4540074f745c | 1.83015 | -55.76669 | 2025-10-16 04:36:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 4a73a2f2-90b8-3a62-9529-1605e56c28ac | 0.8744 | -51.12244 | 2025-10-16 04:36:00 | NOAA-21 | FERREIRA GOMES | AMAPÁ | Brasil | 1600238 | 16 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 6f800974-3ca6-39f7-9b1c-9151011ea233 | 1.79027 | -55.74331 | 2025-10-16 04:36:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ea4507ed-333b-3ee2-8d00-9241cc519c91 | 1.84555 | -55.69983 | 2025-10-16 04:36:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c84e50ec-6131-3a70-875a-ffb4683a2c63 | -3.84539 | -44.54527 | 2025-10-16 04:38:00 | NOAA-21 | MATÕES DO NORTE | MARANHÃO | Brasil | 2106631 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| fbc994c3-b744-3399-a484-93ab0118a72c | -3.67247 | -48.3097 | 2025-10-16 04:38:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 85c601a2-03c5-3e58-94a8-63e09fce60c3 | -8.25504 | -44.07289 | 2025-10-16 04:38:00 | NOAA-21 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c414e7aa-1614-30d7-a8a8-db435e7a7342 | -7.16822 | -42.49604 | 2025-10-16 04:38:00 | NOAA-21 | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 67fcd9e7-535c-3e5d-bb94-cbe993416f47 | -7.4782 | -42.75823 | 2025-10-16 04:38:00 | NOAA-21 | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 9.6 |
| 000d75f1-d487-3474-97e1-baa9c1409c17 | -6.22792 | -44.15448 | 2025-10-16 04:38:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| bf3b6733-db19-348b-8869-87e87d241fe9 | -7.94076 | -44.12584 | 2025-10-16 04:38:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 4.5 |
| bc1febca-e3e3-3337-8514-1714b568462f | -7.48403 | -42.13961 | 2025-10-16 04:38:00 | NOAA-21 | SANTO INÁCIO DO PIAUÍ | PIAUÍ | Brasil | 2209500 | 22 | 33 | nan | nan | nan | Caatinga | 4.2 |
| 684f5041-e0a6-33b6-9d1a-85138b388e55 | -4.67492 | -44.08834 | 2025-10-16 04:38:00 | NOAA-21 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 07b811e4-62f2-32e6-a11a-21f59626c324 | -7.47856 | -42.14408 | 2025-10-16 04:38:00 | NOAA-21 | SANTO INÁCIO DO PIAUÍ | PIAUÍ | Brasil | 2209500 | 22 | 33 | nan | nan | nan | Caatinga | 6.2 |
| c7b3e8b5-0474-3663-acf6-2523dc473110 | -5.43933 | -42.72238 | 2025-10-16 04:38:00 | NOAA-21 | LAGOA DO PIAUÍ | PIAUÍ | Brasil | 2205581 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 6f487afa-5931-3343-9fe0-27b3033a36c1 | -3.34816 | -49.25355 | 2025-10-16 04:38:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 264c18f2-42e0-3f29-9b8b-9545f367fc79 | -7.46655 | -42.67254 | 2025-10-16 04:38:00 | NOAA-21 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 5af1def5-7c75-3f20-afd7-38ad69372ac8 | -6.22261 | -44.60246 | 2025-10-16 04:38:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 1246df8d-7a5d-371f-b503-860d1270bc67 | -6.06095 | -41.88534 | 2025-10-16 04:38:00 | NOAA-21 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 0800cd72-66eb-3d2e-8f56-a310930d7851 | -8.25341 | -44.08475 | 2025-10-16 04:38:00 | NOAA-21 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 16a99d63-3d9d-3b31-8bc7-746319e0acd3 | -5.21065 | -46.19478 | 2025-10-16 04:38:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1b8f3db4-cc61-3edb-b1a0-5898cf0c54b1 | -8.29653 | -43.40728 | 2025-10-16 04:38:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| fbce63e1-413d-3985-86b3-fd50ed25f3e6 | -2.90115 | -49.77827 | 2025-10-16 04:38:00 | NOAA-21 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| acc23832-d40a-3998-af10-2e8d1e0fb42c | -7.31 | -45.75431 | 2025-10-16 04:38:00 | NOAA-21 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 05cd9b52-f86e-3192-a97d-2a7ebbf5acfb | -5.87525 | -42.81985 | 2025-10-16 04:38:00 | NOAA-21 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 3.1 |
| 26d38824-f59a-3a30-9579-f46b5da017b8 | -6.21977 | -44.15337 | 2025-10-16 04:38:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 2f7d266c-38dd-342d-9ea6-a319078d16a0 | -7.00475 | -43.74486 | 2025-10-16 04:38:00 | NOAA-21 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 4.2 |
| c7d7a30b-ec63-3e0f-a962-e66ddad22572 | -5.59969 | -46.4465 | 2025-10-16 04:38:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| accba651-c591-36a3-8c4c-7fe2195e2cfd | -5.87266 | -43.88137 | 2025-10-16 04:38:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 96f5611f-fc77-3c50-884f-18b51b5d0df7 | -3.15912 | -51.81591 | 2025-10-16 04:38:00 | NOAA-21 | VITÓRIA DO XINGU | PARÁ | Brasil | 1508357 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| aee21e9a-94ab-39ba-8de9-e7cc59a0714c | -7.39548 | -39.70297 | 2025-10-16 04:38:00 | NOAA-21 | EXU | PERNAMBUCO | Brasil | 2605301 | 26 | 33 | nan | nan | nan | Caatinga | 8.4 |
| 1e06c31e-0fc9-3a43-b81f-cf386a2304f8 | -2.93833 | -40.099 | 2025-10-16 04:38:00 | NOAA-21 | ACARAÚ | CEARÁ | Brasil | 2300200 | 23 | 33 | nan | nan | nan | Caatinga | 1.6 |
| e3ea1311-c790-3ee4-916e-d513da881ddd | -5.42316 | -40.97733 | 2025-10-16 04:38:00 | NOAA-21 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 9715f6e8-1480-3eef-bc18-53f199a4775b | -6.95161 | -47.7427 | 2025-10-16 04:38:00 | NOAA-21 | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 9997f80b-3772-373e-b6d1-6c653423b286 | -3.42466 | -50.25331 | 2025-10-16 04:38:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c9323749-59ae-30e2-8374-e27ba2429526 | -6.04419 | -41.93446 | 2025-10-16 04:38:00 | NOAA-21 | SANTA CRUZ DOS MILAGRES | PIAUÍ | Brasil | 2209153 | 22 | 33 | nan | nan | nan | Caatinga | 3.6 |
| e73903b1-c152-341b-a39c-b34f874ddb61 | -4.25587 | -48.56347 | 2025-10-16 04:38:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f09215f9-fbf7-3609-9b52-2cc482012595 | -3.28509 | -50.15052 | 2025-10-16 04:38:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 933e10e1-9100-326d-b291-0c04fb159180 | -5.91988 | -44.72669 | 2025-10-16 04:38:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 4159efc3-1ce5-3f0b-9673-333a85399c1f | -5.88921 | -44.8278 | 2025-10-16 04:38:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 986f2a99-e84b-3a11-a0c1-63cd4a17c823 | -2.44393 | -49.37317 | 2025-10-16 04:38:00 | NOAA-21 | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| db781076-590f-38c7-af88-f967203e3cf3 | -8.25634 | -43.43752 | 2025-10-16 04:38:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b27b5aae-5060-371f-b5e0-87601ab7a4b5 | -4.37728 | -43.40174 | 2025-10-16 04:38:00 | NOAA-21 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 10.6 |
| fa10b533-1baf-3a54-bba3-d7cf16832b15 | -3.85224 | -41.56853 | 2025-10-16 04:38:00 | NOAA-21 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 6.7 |
| 6c717517-b0b3-3ed5-9311-404080541b89 | -6.17592 | -43.43896 | 2025-10-16 04:38:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| bedd04af-a974-3546-a77c-bb901d52330b | -7.73349 | -42.46435 | 2025-10-16 04:38:00 | NOAA-21 | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| cce1a239-601a-3326-bb9f-a2180a9eed27 | -6.04819 | -41.94027 | 2025-10-16 04:38:00 | NOAA-21 | SANTA CRUZ DOS MILAGRES | PIAUÍ | Brasil | 2209153 | 22 | 33 | nan | nan | nan | Caatinga | 3.8 |
| e6e2f649-a170-3f14-913f-3190225c1cfb | -3.53844 | -52.70249 | 2025-10-16 04:38:00 | NOAA-21 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 2c5e3e3b-d35b-3572-ab76-15745f157c4d | -5.86813 | -41.23775 | 2025-10-16 04:38:00 | NOAA-21 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 5a1d2904-9c91-3f4f-bd75-8fd51d8b6c8a | -8.25518 | -44.09784 | 2025-10-16 04:38:00 | NOAA-21 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| b576ecec-f809-3584-9fa1-a5f2e2179555 | -3.42186 | -50.24921 | 2025-10-16 04:38:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6ac71b29-7fce-311d-b03d-f7e3385c215b | -4.26132 | -48.55022 | 2025-10-16 04:38:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b4dfccb1-4aa5-3a64-9bbb-557e63bbb572 | -3.67819 | -45.83579 | 2025-10-16 04:38:00 | NOAA-21 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d4124f58-8371-3bdc-8b6e-6a0d6608fe0e | -4.72686 | -46.15887 | 2025-10-16 04:38:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 8.2 |
| 44f2bd13-e3a4-36c5-80f8-9916a8e32e48 | -7.28581 | -42.95591 | 2025-10-16 04:38:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 414b1c53-5be5-3d6c-8787-79a1f58cf4af | -5.74376 | -44.98421 | 2025-10-16 04:38:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 6a1d2c06-5f79-37a6-b822-b2edb654425f | -5.44561 | -44.26694 | 2025-10-16 04:38:00 | NOAA-21 | GRAÇA ARANHA | MARANHÃO | Brasil | 2104701 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 2d980d47-59df-3ba1-ae6f-e63b26f5eb4c | -4.65841 | -44.08931 | 2025-10-16 04:38:00 | NOAA-21 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 8732fe85-e7a5-3016-ad64-ba677903804e | -6.34128 | -43.18039 | 2025-10-16 04:38:00 | NOAA-21 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f7b0faf3-8e14-3e1b-a8da-0f42a7f6db65 | -6.58815 | -44.37112 | 2025-10-16 04:38:00 | NOAA-21 | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| a83e736a-07bc-3fbf-8193-d0058ada49b6 | -3.22814 | -50.05407 | 2025-10-16 04:38:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 665894b0-a194-35f2-ad9d-fee8f5c3c4fd | -7.16874 | -42.52529 | 2025-10-16 04:38:00 | NOAA-21 | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| e6c5dc92-c54a-3aa4-b072-5fb72585d74e | -6.61576 | -42.22506 | 2025-10-16 04:38:00 | NOAA-21 | VÁRZEA GRANDE | PIAUÍ | Brasil | 2211407 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 695408be-ebca-3ad1-9663-fed43187878e | -3.99852 | -48.33595 | 2025-10-16 04:38:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 8ec68f0f-745a-3863-a0fb-401e51f457a1 | -7.66664 | -42.37664 | 2025-10-16 04:38:00 | NOAA-21 | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 8.4 |
| 8b25d181-66b9-3122-8d1f-e87a87d11d5e | -4.91354 | -45.98132 | 2025-10-16 04:38:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b4590f18-bfca-3a0e-a0e1-6fabc32547da | -3.65274 | -51.75145 | 2025-10-16 04:38:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 1f66b6c8-4354-31f6-9248-a9a4d6524e4c | -4.12337 | -50.7187 | 2025-10-16 04:38:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| e2eae50c-a48a-3d76-bf0e-d80cb7783dd5 | -4.39202 | -43.38844 | 2025-10-16 04:38:00 | NOAA-21 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 9f8da751-89ce-3f24-a990-eee91f7bb977 | -7.06782 | -44.74644 | 2025-10-16 04:38:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 6fafc1c2-57f3-35d2-8771-85a1d867384e | -2.59613 | -51.34691 | 2025-10-16 04:38:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c5c97e87-6ec7-33e0-bc0d-300a617b7385 | -4.10467 | -48.02605 | 2025-10-16 04:38:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 21.2 |
| 1bf38db6-1308-322b-aa5d-038f86d2f5b6 | -2.92504 | -48.30101 | 2025-10-16 04:38:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| b1d0d2a6-336b-306f-82cc-e039674a8068 | -4.86992 | -44.57876 | 2025-10-16 04:38:00 | NOAA-21 | SANTO ANTÔNIO DOS LOPES | MARANHÃO | Brasil | 2110302 | 21 | 33 | nan | nan | nan | Cerrado | 10.8 |
| 692ffb45-d593-3910-945e-b0b15e62099c | -3.08612 | -49.48845 | 2025-10-16 04:38:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 8fff37d0-a654-36b9-bbc2-e1b2298adacf | -5.64662 | -45.96764 | 2025-10-16 04:38:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c4c2dd7a-4aab-3731-abcc-b04735334226 | -7.0399 | -42.73594 | 2025-10-16 04:38:00 | NOAA-21 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 3.8 |
| 479198a7-caf7-3da3-96b2-4d8105cc7ccf | -3.67979 | -47.62991 | 2025-10-16 04:38:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| efe61d48-d54e-3b3a-8f9a-27b7e05bf82e | -4.83998 | -42.78985 | 2025-10-16 04:38:00 | NOAA-21 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Cerrado | 26.8 |
| 0fde18b6-f10b-3c42-8c89-9da1e846f19a | -5.87587 | -42.81553 | 2025-10-16 04:38:00 | NOAA-21 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 7bc8ec4a-e2a6-3d65-83b3-de3db9386f8b | -3.8547 | -52.08074 | 2025-10-16 04:38:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 1813e90e-04eb-3bd2-9d0a-a9b578a052a5 | -3.85003 | -41.58324 | 2025-10-16 04:38:00 | NOAA-21 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 8.7 |
| 24bc4ac6-9e28-3b2e-88b4-0feb797a8f43 | -5.79078 | -46.00146 | 2025-10-16 04:38:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 2ae6a692-0bf5-39f0-b81a-513c32819e78 | -6.53846 | -44.69205 | 2025-10-16 04:38:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| ff6d5387-147b-3da9-aad9-74195a410214 | -6.19773 | -44.10596 | 2025-10-16 04:38:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| b20793b1-47cc-35dd-86fb-901cb0c55793 | -3.51387 | -50.21216 | 2025-10-16 04:38:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 15cbcbfa-cbad-3355-bc19-c6b111bac229 | -8.26075 | -43.43817 | 2025-10-16 04:38:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 06b003e3-4e58-304e-b807-78735d1402d2 | -7.93186 | -44.12846 | 2025-10-16 04:38:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 11.7 |
| fffd0f18-be23-354f-8f4e-4db956003242 | -4.67439 | -44.09185 | 2025-10-16 04:38:00 | NOAA-21 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 74e2c20a-d1bb-3e26-8dd6-27b5e0f4ca29 | -7.85347 | -45.40731 | 2025-10-16 04:38:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 9.0 |
| 6351409e-b10c-30e3-b574-98ed2a119a59 | -1.90055 | -47.03732 | 2025-10-16 04:38:00 | NOAA-21 | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e0a2f366-b993-33d8-a586-54d166526d26 | -5.65876 | -45.96082 | 2025-10-16 04:38:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |


[Clique aqui para ver as próximas entradas](README43.md)
