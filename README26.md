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

## Dados Diários - Página 26

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 2e66ec69-4942-3946-b596-ad0c84fb9b0d | -3.9621 | -49.01559 | 2026-09-10 04:25:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 202897d3-0d7d-3705-abe4-34338f87e6ae | -9.65892 | -40.62643 | 2026-09-10 04:25:00 | NOAA-20 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 8511ed00-b78a-3a4a-a3d5-8cf02ec90318 | -6.78252 | -58.90118 | 2026-09-10 04:25:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| b36082ca-8606-3d63-a531-31b36431b3c0 | -3.55159 | -48.17551 | 2026-09-10 04:25:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| bb44bfb7-cc77-37f3-aceb-d8926daf52fb | -7.13031 | -42.10916 | 2026-09-10 04:25:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 05e5040f-1945-3de8-b47b-2287c1f0dbb9 | -4.86234 | -56.00631 | 2026-09-10 04:25:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 5e97d27e-d1c3-30f1-b5a7-ebedcd021be2 | -5.80267 | -43.80111 | 2026-09-10 04:25:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 5aaa57d8-f1f0-3d14-99a8-4c2ecb6792ac | -4.95884 | -45.14178 | 2026-09-10 04:25:00 | NOAA-20 | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 0cef8d30-9b8d-3426-ae2c-6360a18c9160 | -4.82836 | -55.76728 | 2026-09-10 04:25:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 23e1444b-b6a9-35a7-ace3-df3bed522c0c | -5.2789 | -55.96405 | 2026-09-10 04:25:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| a1fb51b9-a811-3f6f-9ffc-e56595fa778d | -7.48619 | -45.27109 | 2026-09-10 04:25:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| b88c27a6-3334-3f60-9767-2a531519c3b8 | -9.71509 | -43.39323 | 2026-09-10 04:25:00 | NOAA-20 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 1521ec05-bff7-3e2c-a598-571d07d78121 | -5.37896 | -46.29769 | 2026-09-10 04:25:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| b84afdf3-cacf-3b20-b053-b2c96a453a4d | -7.10997 | -42.12274 | 2026-09-10 04:25:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 5932fd10-beff-39c8-bc3f-7dc47aa4b84b | -9.68879 | -45.2167 | 2026-09-10 04:25:00 | NOAA-20 | MONTE ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2206605 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 1a8f79e8-8f10-348c-a52c-cdc7e4382b84 | -7.20659 | -43.63533 | 2026-09-10 04:25:00 | NOAA-20 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 6e443d2d-8f64-3da2-804c-4b884eee2f4a | -6.16371 | -44.63528 | 2026-09-10 04:25:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 1f509527-850f-353c-9a75-2f005445add0 | -8.24193 | -44.74354 | 2026-09-10 04:25:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 8049461c-7cea-3df5-9114-88aa792e3a33 | -9.69835 | -43.41023 | 2026-09-10 04:25:00 | NOAA-20 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 801b1dc0-8f20-3691-9c99-59b7a6f7229e | -5.48079 | -45.12877 | 2026-09-10 04:25:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 8fa3dd65-8fcc-3648-beab-3e2b98723d50 | -5.37838 | -46.30132 | 2026-09-10 04:25:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| b5326fac-03a3-3d84-820d-5414b5444bc9 | -5.27263 | -55.96421 | 2026-09-10 04:25:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3b086b75-4717-3c2f-a88b-458bb5018218 | -8.7613 | -46.43754 | 2026-09-10 04:25:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d81bf177-8338-3a3e-a16d-47726bad3076 | -7.02621 | -45.10898 | 2026-09-10 04:25:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| b7afc671-ef50-32d1-9775-7e16edbe6b7b | -5.6862 | -43.39112 | 2026-09-10 04:25:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 11e1b48a-2b5d-30bc-b418-57297fc4ed7b | -6.33346 | -43.7503 | 2026-09-10 04:25:00 | NOAA-20 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a84e1361-3ba2-3a57-88e1-f1f4005c7713 | -6.70454 | -45.46583 | 2026-09-10 04:25:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f1afcdea-b4c1-391b-a43d-07986df87970 | -4.36082 | -47.77966 | 2026-09-10 04:25:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 30c0ae27-945d-3a61-b7ae-917972519147 | -7.54512 | -45.15611 | 2026-09-10 04:25:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| e3a48157-03f9-32b1-a9ab-920501013dcf | -6.16924 | -44.64324 | 2026-09-10 04:25:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 57ce69bb-68b3-3c63-ad0e-a6a482051e39 | -5.41143 | -41.83585 | 2026-09-10 04:25:00 | NOAA-20 | SÃO JOÃO DA SERRA | PIAUÍ | Brasil | 2209906 | 22 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 424f1dc5-f41f-3f53-8b66-a3e233b6d9f1 | -4.01822 | -50.44412 | 2026-09-10 04:25:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e6127ad5-b7cb-37bc-b019-374f8f70bd99 | -9.3026 | -44.36721 | 2026-09-10 04:25:00 | NOAA-20 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 5e9a4d95-da58-3b3b-9cb3-60e50cc5078f | -6.76529 | -58.61667 | 2026-09-10 04:25:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 87f67c7d-115f-3c6b-ac30-0c2194b2ed0a | -4.03483 | -50.88381 | 2026-09-10 04:25:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 77418568-51f8-3d1d-9663-09f67eae40bb | -7.97554 | -43.94527 | 2026-09-10 04:25:00 | NOAA-20 | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 79fd9d11-2d1a-38b6-bfd7-e1f2665f2436 | -5.10518 | -46.94747 | 2026-09-10 04:25:00 | NOAA-20 | JOÃO LISBOA | MARANHÃO | Brasil | 2105500 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 7abb371e-8eef-3d17-98d3-8f8d8609d639 | -8.82072 | -46.92589 | 2026-09-10 04:25:00 | NOAA-20 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 86985dcf-559f-388b-bd38-57af74b024e6 | -7.51872 | -45.2585 | 2026-09-10 04:25:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 7cbf2b75-f7cd-300c-93f0-d93319640b9b | -9.77623 | -43.44922 | 2026-09-10 04:25:00 | NOAA-20 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| c2f26c53-5a99-3c86-9b0f-48273dec7fbb | -9.7653 | -43.41274 | 2026-09-10 04:25:00 | NOAA-20 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 05553609-970d-31c6-9f2a-8c4140d28b0f | -8.74974 | -47.48795 | 2026-09-10 04:25:00 | NOAA-20 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| d982f304-acaa-34d0-8d6a-e0253e596b99 | -7.12969 | -42.11323 | 2026-09-10 04:25:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 27c78570-9656-3414-b61b-9d246a7a0d8c | -6.46702 | -46.29196 | 2026-09-10 04:25:00 | NOAA-20 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a5e5dd2e-69a7-35e4-91fb-e633d0c370ae | -2.95407 | -48.59106 | 2026-09-10 04:25:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| a47b46c7-f53a-3a01-b038-b1d1bcf341e2 | -7.97954 | -43.98627 | 2026-09-10 04:25:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 2f23ee83-3b29-399c-b688-4bb3651fbb0b | -6.77541 | -58.89984 | 2026-09-10 04:25:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.1 |
| d3b9ac21-faf0-3e16-ac19-126446a394ca | -9.70297 | -43.40311 | 2026-09-10 04:25:00 | NOAA-20 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 3.9 |
| 1bd20e7a-d8f4-35b1-b795-88be8dc43020 | -7.04733 | -42.71881 | 2026-09-10 04:25:00 | NOAA-20 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 65284de1-e778-3faa-91db-c2058eb81149 | -7.56593 | -48.36404 | 2026-09-10 04:25:00 | NOAA-20 | NOVA OLINDA | TOCANTINS | Brasil | 1714880 | 17 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c690bba2-3b4c-3856-bba4-abd84862c96c | -6.773 | -58.89146 | 2026-09-10 04:25:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 05cac883-3f8e-3511-b02a-45d599d3bee1 | -9.77446 | -43.44542 | 2026-09-10 04:25:00 | NOAA-20 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 10057914-a522-39d5-bf6b-3eb71f19c670 | -6.4426 | -46.10134 | 2026-09-10 04:25:00 | NOAA-20 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 48ec53bd-9c8e-34ba-83dc-d1dbd047a7af | -4.86347 | -47.40636 | 2026-09-10 04:25:00 | NOAA-20 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 0093d857-60af-3fc8-b4da-6c47680c9cd4 | -7.46629 | -46.14191 | 2026-09-10 04:25:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 6e43a064-8e9b-32ac-a21f-ae2a08c9f586 | -6.76357 | -58.9629 | 2026-09-10 04:25:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 348700df-5f44-3ac9-b0d8-c5b77dd22f51 | -5.29936 | -41.22437 | 2026-09-10 04:25:00 | NOAA-20 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| e8c9be62-854c-39a4-8d91-02e1174c186c | -5.75908 | -45.08749 | 2026-09-10 04:25:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 5.6 |
| d85acb87-b016-3bfe-82e7-5f0e14675ac4 | -2.82628 | -49.2313 | 2026-09-10 04:25:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8af7bf2c-e488-37cb-b2d8-a24745c3047c | -9.78142 | -43.4618 | 2026-09-10 04:25:00 | NOAA-20 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 906f2409-5644-3f2a-9581-e67ca50cc577 | -9.5972 | -40.35713 | 2026-09-10 04:25:00 | NOAA-20 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 2.4 |
| a34f5996-49a8-38ab-9952-5d116125c1af | -6.76657 | -58.60975 | 2026-09-10 04:25:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 682820b2-e58d-364d-b7b8-5663fd571740 | -8.04365 | -46.89366 | 2026-09-10 04:25:00 | NOAA-20 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 5851df9f-392d-31f1-afcf-24c4c7bbb167 | -5.27805 | -55.96866 | 2026-09-10 04:25:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 397eff4f-a6c8-39ba-b53e-842a6cb5deed | -6.24939 | -51.67094 | 2026-09-10 04:25:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e736d324-8770-39c7-ae50-866998a78496 | -5.60248 | -44.85396 | 2026-09-10 04:25:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 9eed744a-1bb2-395f-8896-c1ff84e5df02 | -6.5246 | -44.5644 | 2026-09-10 04:25:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 0.4 |
| cc388f57-c20e-3ef5-827a-ace4c8856b4a | -2.73705 | -57.6307 | 2026-09-10 04:25:00 | NOAA-20 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 8fe88719-7a7f-303c-aa06-3e8ea96d397c | -7.08315 | -44.36031 | 2026-09-10 04:25:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ff068d16-c6fc-321e-806d-a6e53638bd99 | -12.84367 | -44.33543 | 2026-09-10 04:27:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 26.3 |
| 87c60a07-dd0a-30bc-b05c-18d823e63058 | -10.74767 | -45.93193 | 2026-09-10 04:27:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a88b23c7-25b9-383e-a910-7d1e3acd9b3c | -12.85823 | -44.61164 | 2026-09-10 04:27:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| a49a2d98-ce1b-331a-9593-a43ccd46ff40 | -10.0792 | -45.47609 | 2026-09-10 04:27:00 | NOAA-20 | SÃO GONÇALO DO GURGUÉIA | PIAUÍ | Brasil | 2209757 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| fb8350d5-000c-3491-9828-5bd037956af2 | -11.86258 | -44.87584 | 2026-09-10 04:27:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 703987a5-6722-392e-9e3d-bb45fb27fc8c | -10.75098 | -45.93247 | 2026-09-10 04:27:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| eb3f300b-73d0-398d-941c-1d0fd4f2b7c9 | -11.86703 | -44.84672 | 2026-09-10 04:27:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 49cde57b-bbf1-3a55-be4c-4f2902399e94 | -13.27169 | -43.64423 | 2026-09-10 04:27:00 | NOAA-20 | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| ebb52fcb-67cb-3316-a8f3-7895f659a351 | -10.02243 | -44.36008 | 2026-09-10 04:27:00 | NOAA-20 | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 09422a5f-a250-3a4a-9fa0-1521f3196684 | -14.91244 | -44.66744 | 2026-09-10 04:27:00 | NOAA-20 | CÔNEGO MARINHO | MINAS GERAIS | Brasil | 3117836 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| d9e544d3-7e3a-3cb5-acc5-b9c3cd50f9cf | -10.25361 | -45.23153 | 2026-09-10 04:27:00 | NOAA-20 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 34f3a50c-1adf-3e37-a96d-dd057ffd4941 | -10.07699 | -45.46857 | 2026-09-10 04:27:00 | NOAA-20 | SÃO GONÇALO DO GURGUÉIA | PIAUÍ | Brasil | 2209757 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 0985d0d5-8d80-398f-8e1b-3cb8faab11a1 | -10.73609 | -45.9193 | 2026-09-10 04:27:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b3d4e490-f5c6-312e-85aa-faaf1683a330 | -11.33437 | -45.74294 | 2026-09-10 04:27:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 6ad3ae4c-b9dd-3301-812d-9dc0b053265c | -11.19175 | -42.78653 | 2026-09-10 04:27:00 | NOAA-20 | GENTIO DO OURO | BAHIA | Brasil | 2911303 | 29 | 33 | nan | nan | nan | Caatinga | 8.3 |
| b90f5da0-edc9-3e48-9bcc-59a1b2785027 | -11.32884 | -45.77802 | 2026-09-10 04:27:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 8d4cbc64-4ff3-30fc-a8c3-30dafec3b7ff | -10.73057 | -45.91123 | 2026-09-10 04:27:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| eedb1f71-90c0-388a-ae11-4b301d46ecae | -13.4423 | -43.83401 | 2026-09-10 04:27:00 | NOAA-20 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 19.9 |
| 92eaa95d-3864-31af-99ca-8ddfdeec8f53 | -11.87376 | -44.84777 | 2026-09-10 04:27:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 9a0931e0-cdf5-3991-a51b-aaf979345db1 | -11.85025 | -44.86643 | 2026-09-10 04:27:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e4c7c080-7242-3aaf-95f9-fd04d20d8329 | -10.26522 | -45.20094 | 2026-09-10 04:27:00 | NOAA-20 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 0a0dc652-d44e-3a1e-8c2a-335e21792f20 | -10.76419 | -45.95606 | 2026-09-10 04:27:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 2f273f0d-0897-35de-b0e0-fdee535d75e1 | -11.32939 | -45.77451 | 2026-09-10 04:27:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| e98d820b-4712-3f14-a147-de1e0acaf0e3 | -11.33215 | -45.77855 | 2026-09-10 04:27:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 1497fd8e-c8c6-32b7-8cd6-f7c4820464cb | -12.86504 | -44.61271 | 2026-09-10 04:27:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 98ca47ed-651f-3607-9e35-2cd2539fb18a | -12.6353 | -47.08752 | 2026-09-10 04:27:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 8fed81c5-ea68-3c24-b599-26d685e0abe6 | -10.76695 | -45.9601 | 2026-09-10 04:27:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d76d2301-5caa-3287-8b3d-08d3a5dec06c | -10.93297 | -47.88799 | 2026-09-10 04:27:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 64790132-15d3-3855-94d1-8932d416b483 | -12.8368 | -44.33435 | 2026-09-10 04:27:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 14.2 |
| 1f4b346a-4be8-3782-9755-be5abb1a75d4 | -12.85683 | -44.34138 | 2026-09-10 04:27:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 42.9 |
| 8270e1af-d7e9-3229-970d-240e84d07c4b | -13.40993 | -44.17387 | 2026-09-10 04:27:00 | NOAA-20 | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |


[Clique aqui para ver as próximas entradas](README27.md)
