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
| 01684140-c813-3872-b056-2ca6537d4989 | -12.39782 | -43.82941 | 2025-09-20 00:33:00 | TERRA_M-M | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 15.0 |
| 7a3eaf4b-b1e2-36e3-8204-783f3da981b9 | -10.23455 | -54.19417 | 2025-09-20 00:33:00 | TERRA_M-M | MATUPÁ | MATO GROSSO | Brasil | 5105606 | 51 | 33 | nan | nan | nan | Amazônia | 11.1 |
| 1c1a2ee8-b7d4-3d6c-941e-1a2dc37fd457 | -7.20412 | -44.42397 | 2025-09-20 00:33:00 | TERRA_M-M | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 12.8 |
| 2fc4f3c7-0400-332d-a64b-ab0a136fbaad | -14.58445 | -56.9252 | 2025-09-20 00:33:00 | TERRA_M-M | DENISE | MATO GROSSO | Brasil | 5103452 | 51 | 33 | nan | nan | nan | Amazônia | 48.6 |
| 94508844-a6fe-3bd9-82bb-a74e70d35c47 | -11.47943 | -43.57952 | 2025-09-20 00:33:00 | TERRA_M-M | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 13.6 |
| 050ef060-aba4-3867-b4ca-1aa66dbbb5e0 | -6.02674 | -49.86756 | 2025-09-20 00:33:00 | TERRA_M-M | PARAUAPEBAS | PARÁ | Brasil | 1505536 | 15 | 33 | nan | nan | nan | Amazônia | 6.8 |
| f64c92aa-1aa4-3f5f-9189-851609e1623f | -13.33458 | -48.74301 | 2025-09-20 00:33:00 | TERRA_M-M | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 513416b1-9cbc-3cc9-a057-e7e9ad8ebf49 | -11.47738 | -43.56613 | 2025-09-20 00:33:00 | TERRA_M-M | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 168.7 |
| c768deaf-6b27-34c7-a728-b3564fb9545b | -11.66738 | -41.75104 | 2025-09-20 00:33:00 | TERRA_M-M | LAPÃO | BAHIA | Brasil | 2919157 | 29 | 33 | nan | nan | nan | Caatinga | 15.3 |
| 872866cc-1530-3fa6-b272-9e1515538d99 | -12.35867 | -47.0658 | 2025-09-20 00:33:00 | TERRA_M-M | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 0d4ce1a5-0f65-38bb-86e6-c22ef1873701 | -12.23469 | -46.77591 | 2025-09-20 00:33:00 | TERRA_M-M | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 42ab3da3-b0b1-35ff-85ee-2d92be8ea215 | -12.08812 | -44.82318 | 2025-09-20 00:33:00 | TERRA_M-M | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 14bb49e7-f512-3d59-8489-261af98b52e5 | -12.08174 | -44.8463 | 2025-09-20 00:33:00 | TERRA_M-M | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 14.1 |
| 3b9603d9-05e0-3fea-aa4d-f5c64a8f5371 | -7.19534 | -44.43863 | 2025-09-20 00:33:00 | TERRA_M-M | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 10.1 |
| 3c35ee3b-d05b-394e-85cd-2b6a68e7c29c | -11.33772 | -43.47087 | 2025-09-20 00:33:00 | TERRA_M-M | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 9.2 |
| b566889b-2850-3f5f-be0f-ab98b52fe326 | -7.87147 | -45.62651 | 2025-09-20 00:33:00 | TERRA_M-M | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 15.1 |
| cdab511f-5359-3461-bcfb-95c66c648316 | -7.57049 | -46.72623 | 2025-09-20 00:33:00 | TERRA_M-M | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 8.6 |
| 08aa415f-211e-3262-9f10-8e7ede5fa959 | -12.72575 | -47.71817 | 2025-09-20 00:33:00 | TERRA_M-M | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 14.8 |
| 3237f3b9-ba66-34ff-953e-1a1dd00ff1b5 | -6.91355 | -44.76799 | 2025-09-20 00:33:00 | TERRA_M-M | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 53.6 |
| 39f9f9db-b8d3-3439-b97c-104e532acd49 | -10.95011 | -44.83306 | 2025-09-20 00:33:00 | TERRA_M-M | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 21.5 |
| 22c601bd-d587-34d7-a299-b2129dbb94f7 | -5.93612 | -45.08495 | 2025-09-20 00:33:00 | TERRA_M-M | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 31.6 |
| e4267744-b81a-34f9-bb48-62e83694b900 | -7.38581 | -47.04428 | 2025-09-20 00:33:00 | TERRA_M-M | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 88.1 |
| d8124f0e-7154-35d5-8bc4-0d1ae3e5c5c4 | -11.66426 | -44.87523 | 2025-09-20 00:33:00 | TERRA_M-M | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 14.1 |
| 0b664b48-2baa-3904-aba6-d2e714a6d989 | -5.52309 | -43.86722 | 2025-09-20 00:33:00 | TERRA_M-M | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | 14.6 |
| 76c0d28c-8cd1-3edc-99c2-3bcdeef2bac4 | -7.33366 | -44.56701 | 2025-09-20 00:33:00 | TERRA_M-M | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 14.0 |
| 54300a19-edff-3bf0-b539-a677b7d6d55c | -12.44682 | -44.75336 | 2025-09-20 00:33:00 | TERRA_M-M | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 5.2 |
| bcea447f-4748-3d0c-b73d-abaea944478b | -7.1131 | -47.85794 | 2025-09-20 00:33:00 | TERRA_M-M | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 1046909d-ef72-36c2-b2bf-e1f2145228e9 | -11.42871 | -43.53296 | 2025-09-20 00:33:00 | TERRA_M-M | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 9.1 |
| 79e85258-61a9-32a8-bd75-0e72d28fd0fc | -12.24485 | -46.78368 | 2025-09-20 00:33:00 | TERRA_M-M | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 12.4 |
| 2582b895-9a69-3586-a166-787fa8ba7b12 | -11.47534 | -43.55273 | 2025-09-20 00:33:00 | TERRA_M-M | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 15.4 |
| 308c9cc5-180e-3644-ad35-d8e0baa9e53c | -11.10274 | -44.88796 | 2025-09-20 00:33:00 | TERRA_M-M | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 16.2 |
| ded4913a-1a2d-398a-bfab-75c0396c8fdf | -9.01656 | -48.02471 | 2025-09-20 00:33:00 | TERRA_M-M | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 2b1e4fec-2546-31d1-9e43-d80a25f82274 | -13.70912 | -49.85887 | 2025-09-20 00:33:00 | TERRA_M-M | AMARALINA | GOIÁS | Brasil | 5200829 | 52 | 33 | nan | nan | nan | Cerrado | 4.3 |
| f41a02db-66c3-3b76-8c0a-8bd9be3ddfe6 | -5.63386 | -45.9552 | 2025-09-20 00:33:00 | TERRA_M-M | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 45eef1cc-dcb1-3a7d-a3e7-d2a01c68147a | -5.10972 | -43.19479 | 2025-09-20 00:33:00 | TERRA_M-M | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 61.9 |
| 867b9f70-bc11-3e49-8d91-715a197f2753 | -9.49934 | -43.06772 | 2025-09-20 00:33:00 | TERRA_M-M | CAMPO ALEGRE DE LOURDES | BAHIA | Brasil | 2905909 | 29 | 33 | nan | nan | nan | Caatinga | 14.3 |
| 86104780-c068-3732-9c5e-9f58e26338cd | -11.67393 | -44.87374 | 2025-09-20 00:33:00 | TERRA_M-M | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 15.7 |
| ac64f358-7aa5-3e12-a466-0e18662b1e82 | -8.9682 | -47.67734 | 2025-09-20 00:33:00 | TERRA_M-M | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 68cd5fc8-9a40-3c04-a227-7474e34c6557 | -7.53013 | -47.28405 | 2025-09-20 00:33:00 | TERRA_M-M | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 8.6 |
| b006a0b0-ed49-3aa4-83f7-2e38a761d432 | -6.19615 | -41.2202 | 2025-09-20 00:33:00 | TERRA_M-M | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 33.5 |
| 82636a15-db67-3556-a53c-9505f0c1d23a | -6.95533 | -44.76107 | 2025-09-20 00:33:00 | TERRA_M-M | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 11.6 |
| 2e7dfe95-2176-3229-9646-bf975d2c344e | -5.59102 | -44.0924 | 2025-09-20 00:33:00 | TERRA_M-M | GOVERNADOR LUIZ ROCHA | MARANHÃO | Brasil | 2104628 | 21 | 33 | nan | nan | nan | Cerrado | 9.6 |
| 39fc19f0-ba9e-3b20-87eb-76147fbc0f0e | -5.11243 | -43.21259 | 2025-09-20 00:33:00 | TERRA_M-M | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 97.8 |
| a08636a8-3fb0-3edf-b631-02bf7282a71e | -9.45419 | -47.92204 | 2025-09-20 00:33:00 | TERRA_M-M | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 0496428e-0503-3d53-9015-ea2d4e520724 | -5.83698 | -46.28888 | 2025-09-20 00:33:00 | TERRA_M-M | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 8.8 |
| e5156b48-93d1-336a-969b-0b190094604b | -12.15386 | -44.93459 | 2025-09-20 00:33:00 | TERRA_M-M | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 13.4 |
| c5916996-aa67-3552-89c1-9848c2911517 | -7.38448 | -47.03485 | 2025-09-20 00:33:00 | TERRA_M-M | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 6c3e6c66-d6c7-3014-81f6-b58e4c734490 | -8.82596 | -47.24672 | 2025-09-20 00:33:00 | TERRA_M-M | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 7.3 |
| e5afb54b-1714-3991-857f-3434825f9386 | -7.32703 | -44.56141 | 2025-09-20 00:33:00 | TERRA_M-M | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 29.0 |
| 148da494-8e48-37c8-8948-fc187076db1f | -8.03315 | -45.69619 | 2025-09-20 00:33:00 | TERRA_M-M | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 11.5 |
| 24f97cb3-3fe1-3c2f-b87d-f3f3d99fd41d | -11.67556 | -44.88472 | 2025-09-20 00:33:00 | TERRA_M-M | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 58.9 |
| 028ea84b-1d2d-3421-9fb4-8c7ae8d6fe1a | -14.27948 | -54.61648 | 2025-09-20 00:33:00 | TERRA_M-M | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 21.5 |
| 9b1d950b-4320-3e20-a1d3-7ef91c1fca23 | -11.45205 | -43.54286 | 2025-09-20 00:33:00 | TERRA_M-M | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 11.5 |
| 3e7ff403-12a9-3624-b226-7fd02aefe80c | -7.25083 | -46.60938 | 2025-09-20 00:33:00 | TERRA_M-M | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 8.6 |
| 504a9940-bf7b-3cfa-ad40-157655c3987b | -5.52074 | -43.85137 | 2025-09-20 00:33:00 | TERRA_M-M | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | 14.4 |
| 9da64986-268d-3805-bcef-8f3cfbb1270e | -11.09301 | -44.88956 | 2025-09-20 00:33:00 | TERRA_M-M | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 13.4 |
| ff08b6b3-fc01-37cc-af78-3543f8e59da2 | -5.81921 | -45.89293 | 2025-09-20 00:33:00 | TERRA_M-M | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 7.5 |
| edd52d92-7447-3f59-8447-e2f5f8fbed64 | -5.53463 | -43.8657 | 2025-09-20 00:33:00 | TERRA_M-M | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 20.4 |
| e80205d0-e882-3deb-a93d-c85332908107 | -7.92099 | -43.89133 | 2025-09-20 00:33:00 | TERRA_M-M | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 653b1a1c-d3a9-34db-be4e-ac8c5b8d6746 | -7.25752 | -45.49996 | 2025-09-20 00:33:00 | TERRA_M-M | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 11.8 |
| 6d54b9a1-244c-3182-b5dc-a3d7f62cd44d | -5.93427 | -45.0725 | 2025-09-20 00:33:00 | TERRA_M-M | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 101.4 |
| 08b2a92b-ea0b-3a66-af9c-d885d5610e78 | -3.73484 | -53.80825 | 2025-09-20 00:35:00 | TERRA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 9.1 |
| 11331c7d-b078-3e68-81cd-cdc7b3d53121 | -3.35205 | -48.395 | 2025-09-20 00:35:00 | TERRA_M-M | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 12.4 |
| 1e1d30c0-69ba-3116-90eb-1a0dbef53957 | -1.18558 | -47.8013 | 2025-09-20 00:35:00 | TERRA_M-M | SÃO FRANCISCO DO PARÁ | PARÁ | Brasil | 1507409 | 15 | 33 | nan | nan | nan | Amazônia | 7.2 |
| f101ad8a-172a-31ec-a0f9-cef73872d40d | -5.70119 | -51.74536 | 2025-09-20 00:35:00 | TERRA_M-M | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 95df5b31-03f6-319d-b831-b5c1628da65c | -4.29519 | -48.27698 | 2025-09-20 00:35:00 | TERRA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 02d2f81b-ba1a-3e26-b469-891a77b179d1 | -2.43191 | -49.33473 | 2025-09-20 00:35:00 | TERRA_M-M | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 50.7 |
| c237f892-bf95-32e7-b99a-da4b54c79f4b | -4.66215 | -49.33024 | 2025-09-20 00:35:00 | TERRA_M-M | JACUNDÁ | PARÁ | Brasil | 1503804 | 15 | 33 | nan | nan | nan | Amazônia | 11.7 |
| e03b0567-c407-34b0-86b8-f183e498e525 | -3.5163 | -52.75271 | 2025-09-20 00:35:00 | TERRA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 83.1 |
| 8bb1fe3f-4cfb-3557-80f5-b8737a460704 | -3.13208 | -44.42049 | 2025-09-20 00:35:00 | TERRA_M-M | SANTA RITA | MARANHÃO | Brasil | 2110203 | 21 | 33 | nan | nan | nan | Amazônia | 14.9 |
| af639641-1ba5-3410-887b-e23ccf6c3dd4 | -2.43313 | -49.34351 | 2025-09-20 00:35:00 | TERRA_M-M | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 23.2 |
| 7eee6a10-81bf-3512-a8b8-d84f8dc2f6bf | -5.36042 | -49.11136 | 2025-09-20 00:35:00 | TERRA_M-M | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| b9cbc3d3-f1b2-3b8b-8885-7f9af71be6f1 | -4.3526 | -46.2964 | 2025-09-20 00:35:00 | TERRA_M-M | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 19.6 |
| 0a7d4aee-31ab-3f46-9be5-2fb1d34a7ca7 | -2.83563 | -48.66069 | 2025-09-20 00:35:00 | TERRA_M-M | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 21.5 |
| 8e6b1d5f-e568-34b4-85b0-d01553b8c31a | -4.40968 | -46.27682 | 2025-09-20 00:35:00 | TERRA_M-M | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 7.3 |
| 171ccade-988f-395d-8172-8ba8127fcee2 | -4.66254 | -46.0397 | 2025-09-20 00:35:00 | TERRA_M-M | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 12.1 |
| 9a0c06ce-f346-3a52-af2f-9e0eec106997 | -4.34969 | -46.29148 | 2025-09-20 00:35:00 | TERRA_M-M | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 9.2 |
| 4a782254-df48-3ab5-bb14-4240db7d97c3 | -2.80199 | -47.15443 | 2025-09-20 00:35:00 | TERRA_M-M | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 8.0 |
| 633e9fe4-41a3-358b-b03a-abcc89f7d2ee | -1.76536 | -48.05743 | 2025-09-20 00:35:00 | TERRA_M-M | BUJARU | PARÁ | Brasil | 1501907 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| f512aa55-65eb-3b40-a5de-d9322253bc15 | -4.36238 | -46.29502 | 2025-09-20 00:35:00 | TERRA_M-M | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 183.3 |
| c3533969-7db0-390f-bc15-cdab16a5df34 | -5.16654 | -45.41967 | 2025-09-20 00:35:00 | TERRA_M-M | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 8.2 |
| 25ea077c-a6a6-3a66-8b50-16b817aa155d | -4.94312 | -45.49562 | 2025-09-20 00:35:00 | TERRA_M-M | LAGOA GRANDE DO MARANHÃO | MARANHÃO | Brasil | 2105963 | 21 | 33 | nan | nan | nan | Cerrado | 9.5 |
| 6d3dc516-4b4c-3d7d-99dc-e91002f2c7e8 | -3.92354 | -47.53578 | 2025-09-20 00:35:00 | TERRA_M-M | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 18.3 |
| 47d66d12-9357-32cc-8924-58253999e826 | -3.1343 | -44.43599 | 2025-09-20 00:35:00 | TERRA_M-M | SANTA RITA | MARANHÃO | Brasil | 2110203 | 21 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 035258f5-7317-3379-ae88-2b9333b22460 | -5.0451 | -47.90214 | 2025-09-20 00:35:00 | TERRA_M-M | CIDELÂNDIA | MARANHÃO | Brasil | 2103257 | 21 | 33 | nan | nan | nan | Amazônia | 11.1 |
| cb0aa98b-3edc-3b90-bf4c-d880b5f17b72 | -4.15947 | -47.83603 | 2025-09-20 00:35:00 | TERRA_M-M | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 694705f5-6bf1-3cf6-99be-2cf97e5d8fc1 | -2.79108 | -47.14543 | 2025-09-20 00:35:00 | TERRA_M-M | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| e7fb04d8-ba58-3b87-9f30-6f26d20a24d4 | -2.26129 | -47.8399 | 2025-09-20 00:35:00 | TERRA_M-M | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| fe00d0f5-1185-3853-9e8a-24a03912e1a2 | -4.20904 | -46.44041 | 2025-09-20 00:35:00 | TERRA_M-M | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 5.9 |
| f70ca448-cb02-33c6-b1cf-a677dc537e1b | -3.51785 | -52.76429 | 2025-09-20 00:35:00 | TERRA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 4c1471b7-4a27-30fd-a4db-e4b25d6e18c7 | -2.98815 | -49.29144 | 2025-09-20 00:35:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 7.9 |
| c5f7e241-3495-3378-ae02-868eb4b440a2 | -3.51476 | -52.74117 | 2025-09-20 00:35:00 | TERRA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 17.8 |
| 23bc7b02-bd5b-35fa-8d71-f7ca70ee5920 | -4.35099 | -46.28539 | 2025-09-20 00:35:00 | TERRA_M-M | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 9.5 |
| f483eee9-421d-3d72-9695-035cfbd2fd0a | -3.98862 | -51.06136 | 2025-09-20 00:35:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 9.3 |
| cc983626-fd7f-3db1-9837-387ca12b02d5 | -3.45632 | -51.21089 | 2025-09-20 00:35:00 | TERRA_M-M | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 40.4 |
| a4673123-e8e5-3966-9705-30bf88080bc0 | -2.80056 | -47.14417 | 2025-09-20 00:35:00 | TERRA_M-M | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 7.7 |
| 1d03dfdb-6f21-3615-a260-b8a4d2a8b838 | -3.83509 | -49.13791 | 2025-09-20 00:35:00 | TERRA_M-M | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 38d7d8ab-a962-3de0-b5ed-f5123d847f43 | -1.76402 | -48.04795 | 2025-09-20 00:35:00 | TERRA_M-M | BUJARU | PARÁ | Brasil | 1501907 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| f4e8e668-b9a5-36e3-9d98-98627bf1dc39 | -5.6915 | -51.74669 | 2025-09-20 00:35:00 | TERRA_M-M | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 10.0 |
| 8264a8ff-0272-3433-8567-5426f3f0886c | -5.71498 | -49.87434 | 2025-09-20 00:35:00 | TERRA_M-M | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |


[Clique aqui para ver as próximas entradas](README4.md)
