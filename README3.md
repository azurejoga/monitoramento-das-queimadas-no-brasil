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

## Dados Diários - Página 3

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| bdad166e-ec32-3ef4-87f0-424eb48287be | -6.3984 | -44.16971 | 2026-05-29 04:19:00 | NOAA-21 | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 33d03afe-d26c-3e50-96aa-4807e0db9c0b | -7.33462 | -49.86338 | 2026-05-29 04:19:00 | NOAA-21 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0d5d6e85-bc45-3141-ac65-03556df50f30 | -7.01047 | -45.00164 | 2026-05-29 04:19:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 00d9bc58-a62c-3ab4-ad95-d3b6f676d97d | -6.08733 | -44.00411 | 2026-05-29 04:19:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 6e5f05c6-5891-30cb-a1a0-f7a5deba2b22 | -6.53911 | -44.68608 | 2026-05-29 04:19:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 0a4e92ef-69d5-3558-a532-3eaac36a1b2e | -5.83578 | -43.49773 | 2026-05-29 04:19:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 54d628c7-6728-37d5-8b35-629f0dd69fd0 | -7.55672 | -42.65515 | 2026-05-29 04:19:00 | NOAA-21 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| c0a62c33-8821-3fa6-80f9-9c3db5c4f63f | -5.90743 | -45.56542 | 2026-05-29 04:19:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| cfdb16e4-2fce-32d7-8e3a-2cc47a85e9f9 | -6.24637 | -48.57032 | 2026-05-29 04:19:00 | NOAA-21 | SÃO GERALDO DO ARAGUAIA | PARÁ | Brasil | 1507458 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 949ee4a9-0bcc-37eb-9460-8ac9c46f4310 | -5.95022 | -43.48298 | 2026-05-29 04:19:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d359bcf3-1c3a-3f4f-b893-2ce65d40f15b | -6.39126 | -44.17214 | 2026-05-29 04:19:00 | NOAA-21 | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| cb278ffb-3e27-3779-94a3-de535ab41f8e | -7.00663 | -45.00458 | 2026-05-29 04:19:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 4252d261-0de3-36f4-a0b4-bd997ddfd4e8 | -5.32349 | -44.69199 | 2026-05-29 04:19:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| c6244fd1-75ce-3eec-9900-540d2e12a23c | -6.29159 | -43.62947 | 2026-05-29 04:19:00 | NOAA-21 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 5f0e25ca-aa7f-391b-8a16-4833693dbb4e | -5.83911 | -43.49825 | 2026-05-29 04:19:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| fd8bebe1-6880-3f22-9242-ee64ce50d21e | -2.96892 | -39.92508 | 2026-05-29 04:19:00 | NOAA-21 | ITAREMA | CEARÁ | Brasil | 2306553 | 23 | 33 | nan | nan | nan | Caatinga | 3.4 |
| 20e452aa-fa32-3088-bc18-0f834122bf6f | -6.99781 | -44.99612 | 2026-05-29 04:19:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| f6e127fc-1b61-3fa7-956f-1321ae1b99d0 | -5.2883 | -43.95984 | 2026-05-29 04:19:00 | NOAA-21 | SENADOR ALEXANDRE COSTA | MARANHÃO | Brasil | 2111748 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 9816344d-87ef-3f2b-b971-5b3b837e31ef | -6.76186 | -45.02571 | 2026-05-29 04:19:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 0f1c3a1b-2d60-3d9b-b678-d2b586ce7e21 | -5.92304 | -43.4824 | 2026-05-29 04:19:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| aa14bc0a-8691-3dc6-81a1-e598a1d764f5 | -7.60917 | -43.14647 | 2026-05-29 04:19:00 | NOAA-21 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| ed7dc005-a016-3fad-a5c3-710d57b92e13 | -5.32403 | -44.68854 | 2026-05-29 04:19:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 12122080-9fb2-3f2e-a305-16d40209e456 | -5.32679 | -44.6925 | 2026-05-29 04:19:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 43d224f6-08bb-3c15-9dec-01d9e0de9552 | -6.7657 | -45.02277 | 2026-05-29 04:19:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 028ddc3c-cdc7-3a2d-a3f0-1cb7fd8e9c9e | -5.32733 | -44.68905 | 2026-05-29 04:19:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 41fd62ff-fb06-347a-bcdf-e7c8af8d18ca | -5.92691 | -43.4794 | 2026-05-29 04:19:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 7c752f64-f3e2-35a1-8383-211aecee878d | -7.00717 | -45.00113 | 2026-05-29 04:19:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 3dda57ad-bda3-30e6-84c0-cc9f951e0530 | -6.75964 | -45.01828 | 2026-05-29 04:19:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 39ce559d-cc71-3137-943f-d54c35fae1da | -5.953 | -43.48701 | 2026-05-29 04:19:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| bb189f53-ed80-3d83-b8bb-4358e986e1c4 | -6.39509 | -44.1692 | 2026-05-29 04:19:00 | NOAA-21 | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| c5764327-7e73-338d-8582-03c4316337cd | -6.52843 | -43.68045 | 2026-05-29 04:19:00 | NOAA-21 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 9173b449-4fa1-3caf-99ac-3d9efd84ca84 | -2.96453 | -39.92151 | 2026-05-29 04:19:00 | NOAA-21 | ITAREMA | CEARÁ | Brasil | 2306553 | 23 | 33 | nan | nan | nan | Caatinga | 1.2 |
| ac62353c-fc59-3b81-b4ae-18c975063dde | -3.94579 | -40.97041 | 2026-05-29 04:19:00 | NOAA-21 | IBIAPINA | CEARÁ | Brasil | 2305308 | 23 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 69e6c8b2-a9c7-3de7-a68c-655a85862dcc | -7.00608 | -45.00804 | 2026-05-29 04:19:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| db2472cf-5606-32f9-9bdd-346985f01200 | -6.7624 | -45.02225 | 2026-05-29 04:19:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 758e5607-54e5-350f-8056-c55074327766 | -6.02279 | -44.22387 | 2026-05-29 04:19:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c0ed4207-2bf1-32c2-b277-8944f59726d3 | -11.591 | -47.4496 | 2026-05-29 04:20:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 88.4 |
| 59055577-4a9c-3e3e-bfc9-5de0eefd8212 | -12.04687 | -45.27231 | 2026-05-29 04:21:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| fa7d9096-d0cf-356f-a545-63eb46c6b861 | -8.71626 | -47.79734 | 2026-05-29 04:21:00 | NOAA-21 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| fb53c69d-f36a-3b5a-bcfc-8697338a4160 | -8.59868 | -45.93676 | 2026-05-29 04:21:00 | NOAA-21 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 19cde2c5-d2da-33ae-b410-30994c68df94 | -8.71478 | -47.91632 | 2026-05-29 04:21:00 | NOAA-21 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 1e8c5b09-8f1c-3362-b922-95ff0222f24c | -14.44101 | -48.89869 | 2026-05-29 04:21:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| a7503beb-726a-3700-bafd-8ae563a8bba4 | -12.0873 | -51.21927 | 2026-05-29 04:21:00 | NOAA-21 | SERRA NOVA DOURADA | MATO GROSSO | Brasil | 5107883 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b023e874-b279-3f41-882f-4d377568e464 | -11.83228 | -49.79289 | 2026-05-29 04:21:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 8671ebea-6a62-37ff-be2f-9f7bb11c9b92 | -11.59481 | -47.43802 | 2026-05-29 04:21:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 12.8 |
| eed85ce6-ffdb-3bca-98c4-2461052e3e76 | -8.87699 | -48.50175 | 2026-05-29 04:21:00 | NOAA-21 | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 42a7faa0-e298-35d2-b068-dacfff936185 | -11.58744 | -47.44059 | 2026-05-29 04:21:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 96b07cc8-d679-3e16-92e4-fa766d79cfc6 | -10.51217 | -47.71624 | 2026-05-29 04:21:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 8d823582-afbe-390c-915a-15c3bab715ae | -12.70451 | -44.79168 | 2026-05-29 04:21:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 891abd9c-e025-370b-8790-dd4f5aaed790 | -8.70504 | -47.79963 | 2026-05-29 04:21:00 | NOAA-21 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b0bff199-8cd3-3d6e-bef8-f1a1307b2359 | -9.75962 | -50.01076 | 2026-05-29 04:21:00 | NOAA-21 | MARIANÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1712504 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a4ec1f07-2f6e-3e3c-a221-226e40da07dc | -10.98257 | -45.096 | 2026-05-29 04:21:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 02f530cd-620c-3c66-b17b-4b9c0ba75d2c | -14.95885 | -48.70533 | 2026-05-29 04:21:00 | NOAA-21 | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 888e6c20-0f1e-3b60-a9b0-0e85edd1ca83 | -10.9818 | -48.15447 | 2026-05-29 04:21:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| fe64e14f-3947-3131-818e-f1ab0f77f809 | -11.30301 | -54.03264 | 2026-05-29 04:21:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 57c64fb1-402f-35c4-a268-995335fa50a0 | -13.28457 | -48.85862 | 2026-05-29 04:21:00 | NOAA-21 | TROMBAS | GOIÁS | Brasil | 5221452 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 41201fc3-97de-3d19-8a27-35bf839c10eb | -11.77954 | -52.51478 | 2026-05-29 04:21:00 | NOAA-21 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 10f637b9-686f-3a3c-b396-684d3f00c488 | -11.44461 | -55.10787 | 2026-05-29 04:21:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b4c92c42-5b27-33c2-b3bc-8390c6b412aa | -11.40958 | -48.44475 | 2026-05-29 04:21:00 | NOAA-21 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 5e18993a-6175-3810-9334-b96698cf314e | -8.43613 | -47.88937 | 2026-05-29 04:21:00 | NOAA-21 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| c0f47b7c-d50b-37ca-b60e-b3bbbb39f7ec | -10.97483 | -48.15329 | 2026-05-29 04:21:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b3b2e48a-3693-3d4a-9006-4f0ae77a5718 | -9.52998 | -47.4876 | 2026-05-29 04:21:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 654ce8dc-3427-385a-897e-41dcd207b9f5 | -9.85785 | -48.25264 | 2026-05-29 04:21:00 | NOAA-21 | LAJEADO | TOCANTINS | Brasil | 1712009 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 91b3d453-c8f3-37e9-99f7-0dc798911c8b | -11.89729 | -47.60957 | 2026-05-29 04:21:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 4c6c620c-376d-3339-ae6a-616ddf4db2fd | -10.09538 | -43.98169 | 2026-05-29 04:21:00 | NOAA-21 | AVELINO LOPES | PIAUÍ | Brasil | 2201101 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 1e6b7367-3aff-3ed1-b28a-3c8b3657fe20 | -9.17243 | -40.91935 | 2026-05-29 04:21:00 | NOAA-21 | CASA NOVA | BAHIA | Brasil | 2907202 | 29 | 33 | nan | nan | nan | Caatinga | 2.3 |
| dbd5dd6a-ccf1-34e3-985a-f3e7ab62633a | -9.52936 | -47.49142 | 2026-05-29 04:21:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 8095ec56-9e19-3bfd-ae22-f1f8def79d97 | -11.59699 | -47.44595 | 2026-05-29 04:21:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 18.1 |
| d2b04de0-3287-3c97-ab9c-4218cee3575d | -9.21538 | -47.91745 | 2026-05-29 04:21:00 | NOAA-21 | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 0bb4e708-2a79-3688-b66c-e47cd1e965a6 | -9.21475 | -48.59693 | 2026-05-29 04:21:00 | NOAA-21 | MIRANORTE | TOCANTINS | Brasil | 1713304 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 3c72a23c-ed19-31d0-b6a7-c9c2460fad24 | -13.55983 | -47.56637 | 2026-05-29 04:21:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 0.5 |
| a2c4bdc9-4199-398f-b21f-51f539b0acb8 | -12.00202 | -45.14243 | 2026-05-29 04:21:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 197910a9-7813-3a0f-9731-ee6756b1db91 | -15.10996 | -43.99372 | 2026-05-29 04:21:00 | NOAA-21 | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| b98608db-914a-3844-9505-68aa94601fd5 | -11.27311 | -53.97193 | 2026-05-29 04:21:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a681c6e1-dcb1-3d76-8353-3a20999e901c | -11.78844 | -52.51641 | 2026-05-29 04:21:00 | NOAA-21 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| baea4e33-94fc-335b-93ee-98ed7f313a87 | -11.80047 | -52.51701 | 2026-05-29 04:21:00 | NOAA-21 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 24272055-5527-3e3a-92d5-53270f5b8214 | -11.56193 | -54.58053 | 2026-05-29 04:21:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 5153befb-4929-3f98-9a52-cde0b4fc0423 | -9.39271 | -48.45162 | 2026-05-29 04:21:00 | NOAA-21 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 37d0f8da-0b4b-3831-b621-803782566485 | -11.68968 | -45.38123 | 2026-05-29 04:21:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 38b92f35-7a7c-3de6-be95-f5c8c8c19740 | -11.94356 | -43.40807 | 2026-05-29 04:21:00 | NOAA-21 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 5517bf48-a171-3cdb-ab3a-6057d3ad1130 | -11.47192 | -57.10058 | 2026-05-29 04:21:00 | NOAA-21 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 4.5 |
| b179e098-1c24-3da7-bcee-f29d727065ae | -12.00309 | -45.35578 | 2026-05-29 04:21:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| aaf6f386-7c1f-3c81-8f7f-95d801982f5d | -9.16004 | -46.8606 | 2026-05-29 04:21:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 0aeab621-357c-301e-adb4-ecf656db8a29 | -7.61384 | -49.46793 | 2026-05-29 04:21:00 | NOAA-21 | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4fc62279-d2e6-3599-b551-553e5311af98 | -12.36304 | -54.16988 | 2026-05-29 04:21:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| a564efd5-7405-3096-b153-5fa2ec0e0dd2 | -11.44396 | -55.11125 | 2026-05-29 04:21:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c24c0d3f-12cc-3938-b775-cc4b8ce4d2bc | -10.81596 | -56.5964 | 2026-05-29 04:21:00 | NOAA-21 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 3ebbcfbd-0330-35fa-ba22-b3468eb4cbfb | -11.97077 | -47.37151 | 2026-05-29 04:21:00 | NOAA-21 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a14bfbd1-2282-3d73-8913-235f984316f0 | -9.14926 | -50.04384 | 2026-05-29 04:21:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 946f1bd9-554a-3f0e-bc1d-674ebb24dc65 | -11.47522 | -52.92044 | 2026-05-29 04:21:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c16544b9-9033-3ceb-a132-7979cdb65177 | -10.82478 | -46.89579 | 2026-05-29 04:21:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| b9ecc5c8-85cc-3261-84ef-7e6ea34dc163 | -10.51851 | -48.10261 | 2026-05-29 04:21:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| deccb71b-a509-3f94-bb8e-9961be977eaa | -10.10123 | -52.17089 | 2026-05-29 04:21:00 | NOAA-21 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e4dc0450-96ae-3859-a5dc-714c65dc40c5 | -10.35714 | -45.26843 | 2026-05-29 04:21:00 | NOAA-21 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 0.6 |
| ddc71e5a-9b34-3843-80d0-a94e53da05dc | -10.80416 | -46.88133 | 2026-05-29 04:21:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 53274c57-b180-317a-9617-02d71a50856c | -11.59421 | -47.4417 | 2026-05-29 04:21:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 12.8 |
| 7cd49ea9-0b1e-30d4-811c-609ef7130e60 | -13.18125 | -52.70959 | 2026-05-29 04:21:00 | NOAA-21 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 5aa08973-1455-34ad-abdc-3a4175edffc1 | -11.33115 | -51.4048 | 2026-05-29 04:21:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 483d9e22-8e63-33fb-8aff-6b7bb7bbd2b8 | -9.3934 | -48.44743 | 2026-05-29 04:21:00 | NOAA-21 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 56c20bb7-e709-3eff-ae41-edd41820ff17 | -11.7404 | -44.51574 | 2026-05-29 04:21:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |


[Clique aqui para ver as próximas entradas](README4.md)
