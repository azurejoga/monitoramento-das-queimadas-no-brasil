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

## Dados Diários - Página 20

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 66cefba0-c217-3154-8604-5911cfa14c43 | -9.99865 | -44.07951 | 2024-11-19 03:53:00 | NOAA-20 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 31234bbf-e75e-37be-8c1f-9b9214f4ce83 | -3.34248 | -45.36179 | 2024-11-19 03:53:00 | NOAA-20 | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | 3.2 |
| e32839ad-a4dd-3bcf-9637-2755dbe899ac | -4.5524 | -48.02614 | 2024-11-19 03:53:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b94a9c8a-eecf-317c-885e-52d8e5a03fa0 | -10.97688 | -44.4459 | 2024-11-19 03:53:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 4121b4f8-f521-381c-826d-c5b6985d8b7b | -5.65004 | -45.20164 | 2024-11-19 03:53:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| e346a988-d2ed-3655-9dd4-98786f4e4077 | -13.44966 | -44.01889 | 2024-11-19 03:53:00 | NOAA-20 | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 0.3 |
| 811350fb-4632-363c-bb98-7be995566970 | -3.88389 | -43.15799 | 2024-11-19 03:53:00 | NOAA-20 | BURITI | MARANHÃO | Brasil | 2102200 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 5ac4f53a-4d0e-3b4f-a7ef-73e371e355b1 | -10.52169 | -44.95284 | 2024-11-19 03:53:00 | NOAA-20 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 3.4 |
| ad2f1a9e-733c-3f05-a0b4-33432e4ce899 | -4.38017 | -47.77537 | 2024-11-19 03:53:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 2d82488e-36d0-352a-8eb6-2ef59de3785a | -10.40197 | -44.48126 | 2024-11-19 03:53:00 | NOAA-20 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 865c7a17-9b87-35f7-b894-41558160228d | -10.68658 | -44.01095 | 2024-11-19 03:53:00 | NOAA-20 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 4115f19d-f5c6-3b91-b635-e82183eb2b29 | -2.22921 | -46.48376 | 2024-11-19 03:53:00 | NOAA-20 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 1cd9bf60-b355-3617-b2e9-e71014ea98c4 | -3.33063 | -50.49305 | 2024-11-19 03:53:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e7e4fdab-ea27-3906-966b-d24a79b54f02 | -10.75933 | -44.35198 | 2024-11-19 03:53:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 403c5814-de9a-3679-a8ad-54f28f7b2382 | -12.27824 | -43.52981 | 2024-11-19 03:53:00 | NOAA-20 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ffc700e9-c5ee-36a9-b9e5-11611a33932e | -13.24798 | -43.65234 | 2024-11-19 03:53:00 | NOAA-20 | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 4454a912-8d29-3f12-bdc2-cd8de666f913 | -5.39155 | -40.65571 | 2024-11-19 03:53:00 | NOAA-20 | CRATEÚS | CEARÁ | Brasil | 2304103 | 23 | 33 | nan | nan | nan | Caatinga | 4.3 |
| c2c0d528-8f8a-33d9-b1d3-fdc5b828187a | -3.37196 | -45.33391 | 2024-11-19 03:53:00 | NOAA-20 | MONÇÃO | MARANHÃO | Brasil | 2106904 | 21 | 33 | nan | nan | nan | Amazônia | 12.6 |
| 8ab4cc3a-4845-323a-ab73-c00709a98e26 | -10.78765 | -44.33164 | 2024-11-19 03:53:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| baca7783-9cb0-3303-835c-d0a4b52ba419 | -7.39915 | -42.76322 | 2024-11-19 03:53:00 | NOAA-20 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 5.8 |
| d3d004d1-26a4-3171-a259-5f7f2a5133ec | -3.98631 | -49.92184 | 2024-11-19 03:53:00 | NOAA-20 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| ff6a5637-c658-3707-bfec-7e462f8905d5 | -2.39019 | -45.80313 | 2024-11-19 03:53:00 | NOAA-20 | PRESIDENTE MÉDICI | MARANHÃO | Brasil | 2109239 | 21 | 33 | nan | nan | nan | Amazônia | 0.5 |
| bbc27621-880b-3cac-812c-2b79554f8d41 | -11.16194 | -43.58478 | 2024-11-19 03:53:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 4.6 |
| da64b2c3-f6ae-32ef-aeb9-b7130c8d285c | -10.41885 | -44.48051 | 2024-11-19 03:53:00 | NOAA-20 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| cb4b9a4e-c26a-34ed-b94b-9e113cd87c8b | -4.11263 | -43.59553 | 2024-11-19 03:53:00 | NOAA-20 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 447b5cb3-7cc7-3a7c-b355-c42c5dfb7562 | -4.6867 | -41.11102 | 2024-11-19 03:53:00 | NOAA-20 | PORANGA | CEARÁ | Brasil | 2311009 | 23 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 16e211e7-fa90-3c0e-bcc8-1d0c2ae93059 | -3.5913 | -43.62416 | 2024-11-19 03:53:00 | NOAA-20 | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 8678538c-5f25-359c-a926-21cd673252d6 | -12.64189 | -48.81347 | 2024-11-19 03:53:00 | NOAA-20 | TALISMÃ | TOCANTINS | Brasil | 1720978 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 4ca5042f-87eb-352a-af15-fc470383ffce | -11.24574 | -44.65402 | 2024-11-19 03:53:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 51fc26e1-6b8c-3c33-9584-31c7538032a5 | -11.56169 | -44.0243 | 2024-11-19 03:53:00 | NOAA-20 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 3d07b390-961b-3f61-b359-52534733bdea | -5.04036 | -37.77416 | 2024-11-19 03:53:00 | NOAA-20 | QUIXERÉ | CEARÁ | Brasil | 2311504 | 23 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 93a39c15-25af-33fb-9a1b-6a8cab50cda2 | -10.40538 | -44.48565 | 2024-11-19 03:53:00 | NOAA-20 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 6dc1ce0d-a271-3aa9-96fc-bf46469f8024 | -3.5517 | -51.52783 | 2024-11-19 03:53:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 58ad396f-8c8e-3491-ab50-163738adec04 | -3.03539 | -49.46853 | 2024-11-19 03:53:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 5f97bbc3-6e27-34b5-9e26-88fb61025b7a | -3.4122 | -42.38716 | 2024-11-19 03:53:00 | NOAA-20 | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 165d43f1-bbd6-3306-bf13-a59469f9f1d3 | -10.83797 | -44.32646 | 2024-11-19 03:53:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 21490950-43df-3da8-bfc5-4e9fe14811d7 | -3.5926 | -43.62505 | 2024-11-19 03:53:00 | NOAA-20 | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 41a9b6a8-8fbb-3b93-8958-9acf0d53286b | -10.67308 | -40.54168 | 2024-11-19 03:53:00 | NOAA-20 | ANTÔNIO GONÇALVES | BAHIA | Brasil | 2901809 | 29 | 33 | nan | nan | nan | Caatinga | 0.7 |
| eeec582c-d193-36cb-b6bf-af0a50b714df | -7.49758 | -47.35584 | 2024-11-19 03:55:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| d9dd87d6-3346-32ae-9a80-d887769a0ca8 | -8.26308 | -44.01884 | 2024-11-19 03:55:00 | NOAA-20 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b5d49791-5429-3d84-bb1f-dc20827c5310 | -7.55066 | -45.26196 | 2024-11-19 03:55:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 7bf98c36-2946-3310-ac7a-026edf1504be | -10.40904 | -36.6426 | 2024-11-19 03:55:00 | NOAA-20 | PACATUBA | SERGIPE | Brasil | 2804904 | 28 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 650f4f40-a81c-326e-9041-636ed672d98a | -17.37914 | -42.48347 | 2024-11-19 03:55:00 | NOAA-20 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| dde20473-7c64-3d7c-aad2-5e3503374bcf | -7.9968 | -44.3854 | 2024-11-19 03:55:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e07aa411-b22a-3d12-b534-e6c12207f459 | -9.25602 | -45.01321 | 2024-11-19 03:55:00 | NOAA-20 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 8d9299c9-c5bb-3a09-8de9-010ab11c48f9 | -7.56836 | -46.46247 | 2024-11-19 03:55:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| b87d3ade-c2a8-3b15-a104-c16e34e2e83a | -9.29317 | -43.27461 | 2024-11-19 03:55:00 | NOAA-20 | CARACOL | PIAUÍ | Brasil | 2202505 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 72e3ce42-cd7d-3610-b2c4-1a12d0f980ef | -6.63892 | -47.91802 | 2024-11-19 03:55:00 | NOAA-20 | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 46589c73-1655-3af7-9de9-248b5837a3ae | -15.37503 | -43.04024 | 2024-11-19 03:55:00 | NOAA-20 | CATUTI | MINAS GERAIS | Brasil | 3115474 | 31 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 749d0d4d-250e-3766-b995-bd08f02dcc1c | -8.26407 | -44.03783 | 2024-11-19 03:55:00 | NOAA-20 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 9b5430b3-3d02-33bb-9c98-2f52a3894714 | -8.66901 | -47.98716 | 2024-11-19 03:55:00 | NOAA-20 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| c2fe9f27-8997-3da1-9dea-2f091dd0ef23 | -8.27874 | -44.02561 | 2024-11-19 03:55:00 | NOAA-20 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| e4c46213-a49e-3277-b32c-c3cf660e85b7 | -9.25389 | -45.00019 | 2024-11-19 03:55:00 | NOAA-20 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 6.7 |
| d24b14d2-4d34-34c2-af31-e35b8b22f3b3 | -8.67894 | -47.98642 | 2024-11-19 03:55:00 | NOAA-20 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 4d16520d-53ec-39ea-ab8b-63ba07208b03 | -7.89092 | -44.21847 | 2024-11-19 03:55:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 7ec25bde-d97d-39da-bfe5-14da4b495536 | -8.68081 | -47.98229 | 2024-11-19 03:55:00 | NOAA-20 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 78834ad9-078b-3e50-859f-16f08c4b3518 | -20.17832 | -40.22723 | 2024-11-19 03:55:00 | NOAA-20 | SERRA | ESPÍRITO SANTO | Brasil | 3205002 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 8d5a1db2-bb83-3213-8e60-ce0f37b35534 | -10.41255 | -36.64317 | 2024-11-19 03:55:00 | NOAA-20 | PACATUBA | SERGIPE | Brasil | 2804904 | 28 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 7108d6c1-f0e1-3718-be52-1a2faebd794d | -7.56928 | -46.45707 | 2024-11-19 03:55:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| caee36d7-0720-33c2-a06c-f7766dc678c0 | -8.52217 | -37.06424 | 2024-11-19 03:55:00 | NOAA-20 | BUÍQUE | PERNAMBUCO | Brasil | 2602803 | 26 | 33 | nan | nan | nan | Caatinga | 4.4 |
| e9146e56-d128-3609-a484-8a05e54fb5c2 | -15.37152 | -43.03962 | 2024-11-19 03:55:00 | NOAA-20 | CATUTI | MINAS GERAIS | Brasil | 3115474 | 31 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 20b98a4f-2b13-3863-8c70-bd58cd097eb8 | -10.13649 | -38.5233 | 2024-11-19 03:55:00 | NOAA-20 | JEREMOABO | BAHIA | Brasil | 2918100 | 29 | 33 | nan | nan | nan | Caatinga | 13.4 |
| 094a22a3-3c76-3a24-93d8-91ff3b9c46d7 | -7.89508 | -44.2192 | 2024-11-19 03:55:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 8954099c-63f3-310f-ad37-d0b1be91e5ea | -7.8938 | -44.22672 | 2024-11-19 03:55:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a8b7c322-62cf-38bc-8ed8-0a870bc1f4c3 | -7.91556 | -43.77973 | 2024-11-19 03:55:00 | NOAA-20 | ELISEU MARTINS | PIAUÍ | Brasil | 2203602 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 80827879-7b8c-3eb6-b806-95a0a8e9b1cd | -8.67551 | -47.9814 | 2024-11-19 03:55:00 | NOAA-20 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| c7d36ddd-92ae-363f-a43c-3bee434b1903 | -9.58806 | -40.61162 | 2024-11-19 03:55:00 | NOAA-20 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 1.6 |
| b612097c-98d7-32e8-af63-1cd2339a3292 | -9.7705 | -35.88294 | 2024-11-19 03:55:00 | NOAA-20 | MARECHAL DEODORO | ALAGOAS | Brasil | 2704708 | 27 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| 5065a7ec-0165-33cd-82c2-f0085ecae5c6 | -9.25745 | -45.00505 | 2024-11-19 03:55:00 | NOAA-20 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 6d96cbf8-3578-3062-8d35-695b29138116 | -8.0052 | -44.38682 | 2024-11-19 03:55:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 5490dbac-e26f-3f40-8e52-aa0ce7b6c8cf | -9.24889 | -45.00351 | 2024-11-19 03:55:00 | NOAA-20 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 6.7 |
| df8b9fc8-ac27-3aa5-83db-debdc5916b55 | -7.57076 | -46.46429 | 2024-11-19 03:55:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| f8ffd93e-aa77-3c3f-beb0-6b8295a7fd83 | -15.43393 | -43.05848 | 2024-11-19 03:55:00 | NOAA-20 | PAI PEDRO | MINAS GERAIS | Brasil | 3146552 | 31 | 33 | nan | nan | nan | Caatinga | 1.0 |
| d04dfa23-168a-351a-8867-f89235410874 | -9.25317 | -45.00427 | 2024-11-19 03:55:00 | NOAA-20 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 42b45a19-bac3-30b2-9ed2-73576c2a9d30 | -9.24533 | -44.99866 | 2024-11-19 03:55:00 | NOAA-20 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 18f31d68-cb29-337e-baa5-145dae912ec8 | -8.8699 | -40.77946 | 2024-11-19 03:55:00 | NOAA-20 | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 8c921719-6b02-31d7-9296-ab40180616b6 | -7.99746 | -44.3815 | 2024-11-19 03:55:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 7ddb65c0-c864-3009-83a6-a84bcdd2d793 | -7.9034 | -44.22057 | 2024-11-19 03:55:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c39ac5f1-cb55-332e-8030-a93703a74f3a | -7.99458 | -44.37299 | 2024-11-19 03:55:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 40b6dc24-a1e1-3ed3-8377-f97c59b22794 | -14.15194 | -44.58623 | 2024-11-19 03:55:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| edff580e-2041-3fc8-a598-e723e16a42e4 | -20.76226 | -46.77052 | 2024-11-19 03:55:00 | NOAA-20 | ITAÚ DE MINAS | MINAS GERAIS | Brasil | 3133758 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| c870084e-78ae-3f2b-a995-9e1ece7226e3 | -8.67832 | -47.98977 | 2024-11-19 03:55:00 | NOAA-20 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 5.2 |
| eb157d18-ddd1-3668-8ddf-ae3aa38721de | -9.2653 | -45.01066 | 2024-11-19 03:55:00 | NOAA-20 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 4ded8269-7803-3da1-986c-cd70997afe09 | -9.2603 | -45.01398 | 2024-11-19 03:55:00 | NOAA-20 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 3.3 |
| c013bf9e-de6d-3e0a-bf26-cf1def00c0eb | -7.99524 | -44.36909 | 2024-11-19 03:55:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 1648e9ea-3d81-3e21-be34-463a142eeb68 | -7.99878 | -44.37369 | 2024-11-19 03:55:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |
| c656d183-b2f6-38d7-b198-13b86f64f1e7 | -20.10305 | -47.4683 | 2024-11-19 03:55:00 | NOAA-20 | PEDREGULHO | SÃO PAULO | Brasil | 3537008 | 35 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 6f121a22-3058-35ce-bcdd-abca3b7d39d1 | -8.27424 | -44.00249 | 2024-11-19 03:55:00 | NOAA-20 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 35fbaa2c-04b5-3386-9a11-127d29f11316 | -8.67956 | -47.98308 | 2024-11-19 03:55:00 | NOAA-20 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 6.3 |
| c147b5c2-eae8-3c02-9d62-42544c6d7e49 | -20.89875 | -43.82112 | 2024-11-19 03:55:00 | NOAA-20 | CARANDAÍ | MINAS GERAIS | Brasil | 3113206 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| da513b4f-815f-3c48-824a-9737df8bff69 | -7.99812 | -44.3776 | 2024-11-19 03:55:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |
| c116419c-c42d-31f6-9f57-467363d19e65 | -8.26592 | -44.02688 | 2024-11-19 03:55:00 | NOAA-20 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| be46b668-cc8d-33e9-aafe-e2f3096722a0 | -9.58865 | -40.60796 | 2024-11-19 03:55:00 | NOAA-20 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 4949fae7-eadd-3e63-a7b8-c182a77474ed | -9.24461 | -45.00274 | 2024-11-19 03:55:00 | NOAA-20 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 8e0e79b2-f6aa-36b7-920f-3088c1dc00be | -7.89028 | -44.22224 | 2024-11-19 03:55:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c3319f54-e8cf-3400-ba64-9045296d70e3 | -9.26102 | -45.00989 | 2024-11-19 03:55:00 | NOAA-20 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 51da90c8-3eac-3f4a-b1dd-eed560ea4037 | -7.20226 | -45.10091 | 2024-11-19 03:55:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e84e550c-09e0-3ce4-91ce-b43593be870d | -7.56744 | -46.46788 | 2024-11-19 03:55:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 87f34446-d8d4-3a3b-a434-563d669af26b | -7.89443 | -44.22298 | 2024-11-19 03:55:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 3a1f3962-b4d1-3adb-8615-7f52865df2fd | -8.67962 | -47.98898 | 2024-11-19 03:55:00 | NOAA-20 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |


[Clique aqui para ver as próximas entradas](README21.md)
