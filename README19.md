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
| 93f8ced6-4931-3fc2-8165-963aa65070b1 | -5.84006 | -39.62454 | 2024-11-09 03:40:00 | NOAA-20 | MOMBAÇA | CEARÁ | Brasil | 2308500 | 23 | 33 | nan | nan | nan | Caatinga | 3.5 |
| 904fe99a-cd28-35a6-b924-2f6c32abecdf | -3.54013 | -43.56796 | 2024-11-09 03:40:00 | NOAA-20 | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 7ffb9385-0d43-3ebb-b92a-956ea9a35982 | -3.54368 | -43.57205 | 2024-11-09 03:40:00 | NOAA-20 | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 5f7a2786-0422-309e-87ed-82de7cc3fa60 | -3.97295 | -46.41179 | 2024-11-09 03:40:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 9d4fb586-f580-33ba-9d4d-51ec7e9af649 | -4.20403 | -46.70054 | 2024-11-09 03:40:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 10811015-2775-3187-9768-d7b34d2b5c68 | -4.8886 | -48.6173 | 2024-11-09 03:40:00 | NOAA-20 | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| e5f3e95d-b171-38e8-83b6-0d1b51f3a3e6 | -3.83744 | -46.50187 | 2024-11-09 03:40:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 3.9 |
| d110bef9-9b5d-3cc0-bb90-b846609d6850 | -4.15491 | -44.40215 | 2024-11-09 03:40:00 | NOAA-20 | ALTO ALEGRE DO MARANHÃO | MARANHÃO | Brasil | 2100436 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c83d3bac-cfa0-39b8-859b-0a8cd89c9d0b | -4.55953 | -38.00683 | 2024-11-09 03:40:00 | NOAA-20 | BEBERIBE | CEARÁ | Brasil | 2302206 | 23 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 35c64c38-8138-3283-a2ae-3cc6d9a27612 | -3.55951 | -43.57496 | 2024-11-09 03:40:00 | NOAA-20 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 355f39c8-28b1-32a8-9d71-6103565c6d09 | -3.44179 | -45.99084 | 2024-11-09 03:40:00 | NOAA-20 | GOVERNADOR NEWTON BELLO | MARANHÃO | Brasil | 2104651 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3d1c80df-6c9e-3f36-a119-d6083ce54ded | -4.40618 | -43.38 | 2024-11-09 03:40:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 6f97c303-b5ad-38af-953b-4efd08976829 | -2.82599 | -40.28495 | 2024-11-09 03:40:00 | NOAA-20 | ACARAÚ | CEARÁ | Brasil | 2300200 | 23 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 785065d4-6259-3037-9b0e-1e9196beb8e9 | -4.24492 | -47.57762 | 2024-11-09 03:40:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 30.2 |
| ac6b5549-e732-3bd2-9ab6-7d7fe1ad87c0 | -6.49814 | -39.55395 | 2024-11-09 03:40:00 | NOAA-20 | JUCÁS | CEARÁ | Brasil | 2307403 | 23 | 33 | nan | nan | nan | Caatinga | 4.0 |
| b893a922-32b7-3140-b440-f6f815cb0fbb | -4.80206 | -44.78737 | 2024-11-09 03:40:00 | NOAA-20 | POÇÃO DE PEDRAS | MARANHÃO | Brasil | 2108900 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 0e7a58be-861e-3932-b4f2-c2c73dd7009e | -2.4459 | -46.32444 | 2024-11-09 03:40:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 7.3 |
| c0692c0b-0536-3f6c-a841-5b6c349d671c | -2.22735 | -46.55091 | 2024-11-09 03:40:00 | NOAA-20 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 7.7 |
| 503944b3-93b4-3236-b6c9-35cc91760f6a | -2.54654 | -47.12725 | 2024-11-09 03:40:00 | NOAA-20 | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a3592a01-bc51-3691-be3e-7bec4e922c1c | -3.25511 | -43.20511 | 2024-11-09 03:40:00 | NOAA-20 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| b91c9e28-8966-3fb3-8f2f-113cb4313bef | -6.06415 | -44.15079 | 2024-11-09 03:40:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| c6eeb188-022e-3d1d-addf-0684697447c0 | -5.26083 | -37.94051 | 2024-11-09 03:40:00 | NOAA-20 | LIMOEIRO DO NORTE | CEARÁ | Brasil | 2307601 | 23 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 89d47e6a-decd-3933-9d6d-dde088b2c3ff | -3.54479 | -43.56557 | 2024-11-09 03:40:00 | NOAA-20 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 6a5501a3-74ee-389b-9e48-966df2b1c750 | -6.06474 | -44.14741 | 2024-11-09 03:40:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 73d42cfa-a5a7-3808-8ab7-a34455b424e6 | -2.44606 | -46.31774 | 2024-11-09 03:40:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 7d69f568-ca07-3023-aa84-aad1deb0d1f6 | -6.85184 | -38.88873 | 2024-11-09 03:40:00 | NOAA-20 | LAVRAS DA MANGABEIRA | CEARÁ | Brasil | 2307502 | 23 | 33 | nan | nan | nan | Caatinga | 3.3 |
| b7267fe3-b8da-38ae-9b5f-d01a99a79736 | -3.71805 | -40.70852 | 2024-11-09 03:40:00 | NOAA-20 | COREAÚ | CEARÁ | Brasil | 2304004 | 23 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 4da70e7b-64b1-3258-9194-23a537a982f0 | -3.55481 | -43.57058 | 2024-11-09 03:40:00 | NOAA-20 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 42489e9a-e5d9-3474-9f29-a7b00f8d4bf7 | -6.95049 | -37.06336 | 2024-11-09 03:40:00 | NOAA-20 | SÃO MAMEDE | PARAÍBA | Brasil | 2514909 | 25 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 8d9da10c-f07f-3439-8108-d46e1ce90f4d | -3.55599 | -43.57066 | 2024-11-09 03:40:00 | NOAA-20 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 4.9 |
| c02f891a-3977-384c-9a3d-5297667d21c8 | -3.5396 | -43.57119 | 2024-11-09 03:40:00 | NOAA-20 | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 377394c4-b29a-3555-9381-652dae116eca | -5.81459 | -44.12579 | 2024-11-09 03:40:00 | NOAA-20 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 6.3 |
| ff5c841b-0dea-38b0-9221-836055b7e77b | -6.49953 | -39.55679 | 2024-11-09 03:40:00 | NOAA-20 | JUCÁS | CEARÁ | Brasil | 2307403 | 23 | 33 | nan | nan | nan | Caatinga | 9.5 |
| a932b4e2-0ca0-3886-a5d9-7229bd04965a | -4.51526 | -45.68426 | 2024-11-09 03:40:00 | NOAA-20 | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 56f541f4-470d-375c-9f19-6236a58ada84 | -3.29552 | -46.42079 | 2024-11-09 03:40:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 7.6 |
| 8817ea9c-8f6a-3a2e-a421-5e8800124530 | -2.45337 | -46.31339 | 2024-11-09 03:40:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 2dc92471-b8a3-3181-aa7c-ba3e3842e494 | -5.71598 | -42.71277 | 2024-11-09 03:40:00 | NOAA-20 | AGRICOLÂNDIA | PIAUÍ | Brasil | 2200103 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| f8619c88-caa7-330f-98b8-0cedd1753d8b | -3.5484 | -43.57627 | 2024-11-09 03:40:00 | NOAA-20 | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 6bee0cbb-1fc3-3407-ac82-a1030d27c005 | -4.43748 | -43.64212 | 2024-11-09 03:40:00 | NOAA-20 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 8c1ffa99-9b38-3155-9487-194b22f038f1 | -4.2368 | -47.55982 | 2024-11-09 03:40:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 5bee17a4-f9dc-3423-bf3b-31dbf09b82c3 | -5.81608 | -44.12436 | 2024-11-09 03:40:00 | NOAA-20 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 9d97f452-a3ce-30a4-843d-b9798848e42d | -3.53949 | -43.56476 | 2024-11-09 03:40:00 | NOAA-20 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 18cb1de3-2f23-3327-9fd2-b73c06d64bba | -2.5769 | -48.18677 | 2024-11-09 03:40:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 37147369-98a7-30a1-bb41-7986d6e563d2 | -5.38843 | -40.65165 | 2024-11-09 03:40:00 | NOAA-20 | CRATEÚS | CEARÁ | Brasil | 2304103 | 23 | 33 | nan | nan | nan | Caatinga | 2.0 |
| d344a7be-ca83-3de9-97d7-aa916485cb87 | -6.53574 | -44.47271 | 2024-11-09 03:40:00 | NOAA-20 | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 1befd6aa-9180-3c5e-b86d-a8443725b2c0 | -7.49568 | -39.59061 | 2024-11-09 03:40:00 | NOAA-20 | EXU | PERNAMBUCO | Brasil | 2605301 | 26 | 33 | nan | nan | nan | Caatinga | 0.8 |
| d3c819dc-c94f-39b2-9229-fe299dba40b9 | -5.44774 | -43.26405 | 2024-11-09 03:40:00 | NOAA-20 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 7ff543fe-1bf2-315a-adfe-9caec01af0eb | -4.86332 | -45.67543 | 2024-11-09 03:40:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| ac38fafc-16fe-3fd3-9f80-3a223779d08c | -5.93473 | -43.65801 | 2024-11-09 03:40:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 3ebdec2a-e457-34b5-acfe-eafce6f908e9 | -6.2295 | -47.29542 | 2024-11-09 03:40:00 | NOAA-20 | CAMPESTRE DO MARANHÃO | MARANHÃO | Brasil | 2102556 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 7eaf9e7f-8f32-37de-91a2-e6d2bd72ac3d | -3.54424 | -43.56878 | 2024-11-09 03:40:00 | NOAA-20 | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 5.3 |
| b50f2bd2-47d0-351e-a657-3babbb6a0255 | -7.47122 | -38.51991 | 2024-11-09 03:40:00 | NOAA-20 | CONCEIÇÃO | PARAÍBA | Brasil | 2504405 | 25 | 33 | nan | nan | nan | Caatinga | 3.4 |
| 634d241d-efb0-3a3d-84b5-b2805a8836b0 | -2.4277 | -46.309 | 2024-11-09 03:40:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 1e1fcaad-3605-33f5-8569-e3f0b07800b5 | -4.50948 | -42.88535 | 2024-11-09 03:40:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 3f8c3325-ce4b-3a69-8d7b-a351a84b1c5a | -4.83294 | -45.63926 | 2024-11-09 03:40:00 | NOAA-20 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0e01de80-7aec-3fac-89cc-fb7e613b1b41 | -3.9839 | -46.42364 | 2024-11-09 03:40:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 55e2233f-e1c4-3d3c-8755-89f149865806 | -2.54552 | -47.13343 | 2024-11-09 03:40:00 | NOAA-20 | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e0e2e939-af7c-3089-964f-47f7a5c8f34f | -5.9959 | -46.10134 | 2024-11-09 03:40:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| fb9afd2a-bd5a-38b1-9f73-d89e976d4fd8 | -2.31176 | -46.4862 | 2024-11-09 03:40:00 | NOAA-20 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 6e59b11e-290b-33fb-b22c-af42f1bca9b7 | -6.18101 | -45.44526 | 2024-11-09 03:40:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 8.7 |
| 81ffda0f-0cb9-3473-82c5-d7a0d797257e | -4.20079 | -45.85936 | 2024-11-09 03:40:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 0658a49f-ab43-3eba-a93b-5eddbb91d644 | -3.96207 | -48.19104 | 2024-11-09 03:40:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 11.4 |
| 86c19589-dac5-3d99-88bc-6876359b4d89 | -3.55071 | -43.56972 | 2024-11-09 03:40:00 | NOAA-20 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 2cea2a12-42f3-391a-b048-d2a7dc1490ab | -2.22174 | -46.54433 | 2024-11-09 03:40:00 | NOAA-20 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 18.2 |
| aa398597-9b59-31cf-a827-fd494e8ca752 | -5.35931 | -44.14717 | 2024-11-09 03:40:00 | NOAA-20 | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| fb21ec1e-7ede-32da-beb2-1863c69aacf5 | -3.96562 | -48.20075 | 2024-11-09 03:40:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| dbe53f5e-6ac6-3338-ae31-aea203c92fb9 | -4.20935 | -46.69905 | 2024-11-09 03:40:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 402e503b-e4d4-3fea-b779-0270f1a72952 | -3.59738 | -47.34598 | 2024-11-09 03:40:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 35.2 |
| 6a5bd4d9-b3e9-3d9a-8910-69bc7ae02869 | -4.40565 | -43.38315 | 2024-11-09 03:40:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 0404e6a6-fd8f-350b-bf17-0a96ef0811cf | -5.63185 | -44.83332 | 2024-11-09 03:40:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 2878e447-83dd-3524-9d10-845591d18fe0 | -5.65254 | -42.73569 | 2024-11-09 03:40:00 | NOAA-20 | CURRALINHOS | PIAUÍ | Brasil | 2203255 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| c268f9e9-1e00-3551-9cb5-09d79491caf7 | -5.73768 | -41.99699 | 2024-11-09 03:40:00 | NOAA-20 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 74edac0d-37b3-3a32-955a-d5436eccfac1 | -6.24518 | -39.70466 | 2024-11-09 03:40:00 | NOAA-20 | ACOPIARA | CEARÁ | Brasil | 2300309 | 23 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 6440ad63-331d-3463-8d65-14e65e1d35aa | -5.14161 | -46.21247 | 2024-11-09 03:40:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 28bf85ab-3d3f-392d-8537-a90133e91ae4 | -4.6135 | -45.98727 | 2024-11-09 03:40:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ab989b92-7e84-3d4b-8bcf-ab5b9344be12 | -2.56689 | -47.35106 | 2024-11-09 03:40:00 | NOAA-20 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 2bff37eb-ef68-345a-8923-6a025d566c04 | -3.54897 | -43.57295 | 2024-11-09 03:40:00 | NOAA-20 | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 06e690c6-5d90-370d-9715-ec7615c86915 | -6.10431 | -44.7579 | 2024-11-09 03:40:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 5c4910dc-14c9-3491-bbe1-9e9b42ba3a04 | -6.23288 | -47.2824 | 2024-11-09 03:40:00 | NOAA-20 | CAMPESTRE DO MARANHÃO | MARANHÃO | Brasil | 2102556 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| d53cf571-9739-3a5f-a20e-baffe5b89105 | -3.59412 | -47.36477 | 2024-11-09 03:40:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 13.3 |
| 53b13b00-a192-3ab3-9534-81dc5be79b00 | -5.53593 | -41.68623 | 2024-11-09 03:40:00 | NOAA-20 | CASTELO DO PIAUÍ | PIAUÍ | Brasil | 2202604 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| f8045d44-a098-3177-b250-643f7ddca270 | -4.80274 | -44.78345 | 2024-11-09 03:40:00 | NOAA-20 | POÇÃO DE PEDRAS | MARANHÃO | Brasil | 2108900 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 85ea177c-030d-3b45-ad2e-32982ae8ecaf | -4.41541 | -43.38816 | 2024-11-09 03:40:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 701c751f-c917-3037-9c43-88af6c0f77a3 | -5.03985 | -46.80131 | 2024-11-09 03:40:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 634dd4e0-28d8-33cc-98fa-f7873d1def80 | -5.19767 | -44.92028 | 2024-11-09 03:40:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 0d66182a-4519-3e24-bf08-e21e3a29fa1a | -5.53669 | -41.68177 | 2024-11-09 03:40:00 | NOAA-20 | CASTELO DO PIAUÍ | PIAUÍ | Brasil | 2202604 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 31076c4d-a075-3884-be65-6aecceabc477 | -3.54953 | -43.56966 | 2024-11-09 03:40:00 | NOAA-20 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 4.8 |
| a541b2f4-4695-3a4e-879b-a07a86088944 | -4.12711 | -43.59792 | 2024-11-09 03:40:00 | NOAA-20 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 6.1 |
| c53ec35a-c77c-39bc-9008-557b90f3c990 | -5.81517 | -44.12257 | 2024-11-09 03:40:00 | NOAA-20 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 6.3 |
| d56f241f-e13a-3f57-ba93-5534deedfc5b | -6.19604 | -43.42884 | 2024-11-09 03:40:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c716249d-eba2-3cb2-8cc5-666f1e469e30 | -2.53978 | -47.12627 | 2024-11-09 03:40:00 | NOAA-20 | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 58714cd0-3fcf-3b9b-bd11-3c5be5170ebc | -5.90201 | -44.52231 | 2024-11-09 03:40:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| d879bd1e-7514-3fe2-91e5-7b90b1dfc965 | -2.82522 | -47.8702 | 2024-11-09 03:40:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 8229f6ae-02fb-33ae-a369-c3657952996a | -2.23491 | -46.62618 | 2024-11-09 03:40:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 64f375f9-0d73-395d-86a5-df588dc3e096 | -3.59068 | -47.34475 | 2024-11-09 03:40:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 35.2 |
| 65997aad-cb00-34bc-97c8-229ddc09c490 | -5.96695 | -39.68304 | 2024-11-09 03:40:00 | NOAA-20 | MOMBAÇA | CEARÁ | Brasil | 2308500 | 23 | 33 | nan | nan | nan | Caatinga | 0.9 |
| ea391edb-6535-3051-b6c4-c1f7c7d835a7 | -2.3607 | -46.86179 | 2024-11-09 03:40:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 2d903946-d0a3-3428-a378-a25c5caa8a10 | -4.88576 | -44.59379 | 2024-11-09 03:40:00 | NOAA-20 | SANTO ANTÔNIO DOS LOPES | MARANHÃO | Brasil | 2110302 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 14f509df-d9ed-341f-ba25-f4bf63c46af4 | -2.62907 | -46.77716 | 2024-11-09 03:40:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 306e89eb-ff06-301a-bdef-70465b395c78 | -5.4704 | -43.65162 | 2024-11-09 03:40:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 6.5 |


[Clique aqui para ver as próximas entradas](README20.md)
