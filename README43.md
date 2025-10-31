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

## Dados Diários - Página 43

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| b1e25155-e354-3005-a87f-49200d3f6b37 | -13.23525 | -54.3562 | 2025-10-31 05:27:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| f1c2cc69-12e6-328a-9624-6bac95ab29c4 | -13.2401 | -54.35685 | 2025-10-31 05:27:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 3fa0bdf7-5139-35c2-a84b-d540537f8c78 | -12.04632 | -54.25083 | 2025-10-31 05:27:00 | NPP-375D | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 71adcf22-5b8e-3df8-ad30-71e76c90a138 | -12.28411 | -48.04258 | 2025-10-31 05:27:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| b302ce30-0505-31ec-82db-c5c8f1a90dc0 | -12.04699 | -54.24553 | 2025-10-31 05:27:00 | NPP-375D | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 188a7d0d-f898-369f-9899-f68b37a606f0 | -10.53005 | -53.71013 | 2025-10-31 05:27:00 | NPP-375D | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 6114800f-8772-3486-a3cf-01273ce4e0ce | -14.45785 | -55.83976 | 2025-10-31 05:27:00 | NPP-375D | NOBRES | MATO GROSSO | Brasil | 5105903 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 4e2ddfe3-3b08-39cd-9165-c06329748649 | -12.28669 | -48.04073 | 2025-10-31 05:27:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| e173aca3-c946-39b9-8694-1395e676742f | -11.14675 | -50.7204 | 2025-10-31 05:27:00 | NPP-375D | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 99d2a325-9e2e-323b-b4f3-dd643bac90bd | -12.25888 | -60.54777 | 2025-10-31 05:27:00 | NPP-375D | PIMENTA BUENO | RONDÔNIA | Brasil | 1100189 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| e01599a1-1769-3bb9-9cde-d009b87141d1 | -11.12001 | -54.63466 | 2025-10-31 05:27:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1e4eb15f-07f1-3362-8082-d4902e80159c | -13.23108 | -54.35007 | 2025-10-31 05:27:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 50699b0c-b8f6-3aab-9421-31107b333315 | -11.08607 | -51.54453 | 2025-10-31 05:27:00 | NPP-375D | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 63bb140f-50ea-39bc-ba6b-b178929e96d5 | -9.51908 | -47.26532 | 2025-10-31 05:27:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f6663a05-8d23-3de8-b9b9-2ed4244a43cd | -11.73186 | -59.30869 | 2025-10-31 05:27:00 | NPP-375D | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| f74b6f61-b3f9-3c6f-9fa6-788b17a7dac7 | -11.11935 | -54.63947 | 2025-10-31 05:27:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 8019078d-8a52-35c7-8f88-0af0fa15a277 | -11.62057 | -61.46334 | 2025-10-31 05:27:00 | NPP-375D | PIMENTA BUENO | RONDÔNIA | Brasil | 1100189 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 9acf4393-9b55-3db9-8ba8-95ff745e8f06 | -11.14621 | -50.72486 | 2025-10-31 05:27:00 | NPP-375D | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 06f2cd56-bda1-32ff-863b-c360e03d3b6b | -12.04217 | -54.2449 | 2025-10-31 05:27:00 | NPP-375D | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 3b0671f8-00f2-377e-ac33-f157d92f4c9a | -11.31621 | -51.44664 | 2025-10-31 05:27:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| e99b06b3-d12a-3520-8828-e9f9a20e25cf | -11.99413 | -63.94621 | 2025-10-31 05:27:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 49c229b8-6fa2-3380-9d4d-f24f964f68b8 | -15.84927 | -57.81723 | 2025-10-31 05:29:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 0.7 |
| f21b7261-11cb-37d9-89bf-1dcede850e40 | -19.66383 | -53.55934 | 2025-10-31 05:29:00 | NPP-375D | CAMAPUÃ | MATO GROSSO DO SUL | Brasil | 5002605 | 50 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 25a36c24-e83f-3dca-9962-3a53ee596e32 | -19.66202 | -53.55952 | 2025-10-31 05:29:00 | NPP-375D | CAMAPUÃ | MATO GROSSO DO SUL | Brasil | 5002605 | 50 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 23742c6f-0997-3f16-8d82-9a6bc78139d2 | -16.2413 | -60.16909 | 2025-10-31 05:29:00 | NPP-375D | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 39d9e5d1-46f3-3835-b937-58a373d8a65f | -4.8409 | -42.7465 | 2025-10-31 05:30:00 | GOES-19 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Cerrado | 71.5 |
| e11e627d-8df2-30c2-be0b-3c6f28d317fc | -3.017 | -49.4482 | 2025-10-31 05:30:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 35.3 |
| d54b70a6-2c36-3b22-8057-f8b6c234d39c | -7.3136 | -44.9343 | 2025-10-31 05:30:00 | GOES-19 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 64.6 |
| 724648b5-f479-34b3-a534-f67177752f63 | -4.8411 | -42.7229 | 2025-10-31 05:30:00 | GOES-19 | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Cerrado | 63.3 |
| f720347b-d238-3657-b9b8-46a44e7d5e57 | -7.3134 | -44.9572 | 2025-10-31 05:30:00 | GOES-19 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 75.4 |
| 3b48eb93-338f-3ea2-b699-97bf03bd947b | -7.3134 | -44.9572 | 2025-10-31 05:40:00 | GOES-19 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 76.7 |
| f4582b42-5d25-3e72-a71e-f67bd85f45ff | -3.017 | -49.4482 | 2025-10-31 05:40:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 45.5 |
| 807f10ee-787c-3484-9fbd-be81521aee0a | -7.3136 | -44.9343 | 2025-10-31 05:40:00 | GOES-19 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 85.1 |
| d91d7637-93ac-3be3-8693-fa107322c9ac | -1.8205 | -55.36124 | 2025-10-31 05:46:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 0bbd24e4-642c-39ae-98bf-dbe3fea0cd8a | -3.33233 | -54.0859 | 2025-10-31 05:46:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 71f2be12-d932-39bf-8e91-f31f8c387a48 | -2.04688 | -52.07766 | 2025-10-31 05:46:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| c2d6edf2-2f7e-34aa-867c-d2cc6f9e9080 | -1.81986 | -55.36544 | 2025-10-31 05:46:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c86fffd9-082c-3ece-8515-e14a84210197 | 3.22046 | -61.19989 | 2025-10-31 05:46:00 | NOAA-20 | ALTO ALEGRE | RORAIMA | Brasil | 1400050 | 14 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 010d9892-bcca-369a-b3c0-4e0e35cc1e55 | -3.3258 | -54.08561 | 2025-10-31 05:46:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e122fd5a-0c32-3ebd-a26d-2776d35d2048 | -3.32651 | -54.08065 | 2025-10-31 05:46:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| e2daef56-72eb-37cd-9fa8-2364e2a8bfbd | -5.13141 | -55.96103 | 2025-10-31 05:48:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 63c12a4b-b9ff-3b7e-bfdd-85a1a234fd92 | -5.13203 | -55.95668 | 2025-10-31 05:48:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 9c9100e5-0d93-3b82-b032-01186302a5cd | -3.017 | -49.4482 | 2025-10-31 05:50:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 37.6 |
| 9c09901f-09bc-3013-b355-23627d9ae298 | -11.62027 | -61.46299 | 2025-10-31 05:50:00 | NOAA-20 | PIMENTA BUENO | RONDÔNIA | Brasil | 1100189 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b6d532df-c465-37e8-a3b7-e6bec7365d4d | -11.94486 | -60.48231 | 2025-10-31 05:50:00 | NOAA-20 | PIMENTA BUENO | RONDÔNIA | Brasil | 1100189 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 9ff1dc67-bd7f-33c3-8f3e-63822660afea | -12.61918 | -62.03495 | 2025-10-31 05:50:00 | NOAA-20 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 89223fbc-d177-3d20-afdc-49144bdb88d2 | -11.94418 | -60.48745 | 2025-10-31 05:50:00 | NOAA-20 | PIMENTA BUENO | RONDÔNIA | Brasil | 1100189 | 11 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 27d45904-ce11-3469-a0f8-d4f4c253c278 | -12.43139 | -63.13217 | 2025-10-31 05:50:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f8ed8142-57f0-3374-bcbf-8f1000b0d6cc | -11.61943 | -61.4608 | 2025-10-31 05:50:00 | NOAA-20 | PIMENTA BUENO | RONDÔNIA | Brasil | 1100189 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d5b7a058-f9f4-3dd4-b47a-ef39ea96b165 | -11.99177 | -63.94746 | 2025-10-31 05:50:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 5bbf6c2a-4fd6-3c22-81e3-9f791119a9b7 | -9.73938 | -66.899 | 2025-10-31 05:50:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 6d573d3b-25aa-3339-9979-17cfc40ab28a | -12.1408 | -64.28216 | 2025-10-31 05:50:00 | NOAA-20 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d7e9c3f2-6383-3be9-8ffc-690fb394bcf9 | -12.42737 | -63.13161 | 2025-10-31 05:50:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 0ce5d9a4-8ad1-3086-910c-99e5348d4a6a | -3.017 | -49.4482 | 2025-10-31 06:00:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 36.2 |
| a2457ecf-ea95-3d8f-b6f3-63473d65a183 | -3.017 | -49.4482 | 2025-10-31 06:10:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 39.6 |
| 4304cd44-bbd7-3f6d-a619-139528b8d79d | -3.017 | -49.4482 | 2025-10-31 06:20:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 28.6 |
| 67514010-5270-3106-9668-5a0d7f66fac9 | -2.41616 | -49.29407 | 2025-10-31 06:31:00 | AQUA_M-M | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 13.2 |
| 3730c5d8-b5a7-3214-84c3-54ba5e35b6f3 | -2.31654 | -48.57724 | 2025-10-31 06:31:00 | AQUA_M-M | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 39.1 |
| 3af9c715-5177-3b79-bd8d-00d2ee2f5984 | -3.00582 | -49.44862 | 2025-10-31 06:31:00 | AQUA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 9.7 |
| d466c8a9-e6a9-3342-b3de-2d6ea524be3f | -3.09614 | -45.04132 | 2025-10-31 06:31:00 | AQUA_M-M | MATINHA | MARANHÃO | Brasil | 2106508 | 21 | 33 | nan | nan | nan | Amazônia | 34.6 |
| d6ed4304-0507-343e-8d30-d47eef42b8df | -5.58577 | -48.04553 | 2025-10-31 06:31:00 | AQUA_M-M | ARAGUATINS | TOCANTINS | Brasil | 1702208 | 17 | 33 | nan | nan | nan | Amazônia | 25.0 |
| 2d63ad21-6ecf-3497-8ced-661a61b90599 | -3.00002 | -44.96102 | 2025-10-31 06:31:00 | AQUA_M-M | OLINDA NOVA DO MARANHÃO | MARANHÃO | Brasil | 2107456 | 21 | 33 | nan | nan | nan | Amazônia | 39.2 |
| bf5d3214-2f8b-383a-8202-a1e3b1a817b4 | -2.62878 | -48.49666 | 2025-10-31 06:31:00 | AQUA_M-M | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 9.4 |
| 9064ff92-2d58-3373-bc3f-e2289bf87c20 | -2.44481 | -49.02915 | 2025-10-31 06:31:00 | AQUA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 8.6 |
| 0e979879-7c9f-3ba0-b24b-b6b98c00770a | -3.09149 | -45.04818 | 2025-10-31 06:31:00 | AQUA_M-M | MATINHA | MARANHÃO | Brasil | 2106508 | 21 | 33 | nan | nan | nan | Amazônia | 22.6 |
| 62c5d08c-7876-38ef-8b59-7e1888d97f72 | -3.87523 | -51.1902 | 2025-10-31 06:31:00 | AQUA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 9.0 |
| 11020aa2-587d-3758-89e1-3e4046b254f7 | -5.70731 | -48.88095 | 2025-10-31 06:31:00 | AQUA_M-M | SÃO DOMINGOS DO ARAGUAIA | PARÁ | Brasil | 1507151 | 15 | 33 | nan | nan | nan | Amazônia | 10.9 |
| d31c0fa8-a406-37fc-9a96-0692c7e3c1ab | -3.01858 | -49.4367 | 2025-10-31 06:31:00 | AQUA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 22.0 |
| e38905c6-8a92-389a-978d-e1b14a728c9e | -2.4198 | -49.29994 | 2025-10-31 06:31:00 | AQUA_M-M | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 10.1 |
| f251c13c-dec0-34fb-9d6c-f894d8821eeb | -3.13842 | -49.42449 | 2025-10-31 06:31:00 | AQUA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 10.7 |
| ce583d3c-a5f1-3f1b-b10e-61329eb746bf | -4.22857 | -55.65948 | 2025-10-31 06:31:00 | AQUA_M-M | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 19c7a360-2c32-3628-b9b3-bdd413b59f91 | -3.01658 | -49.4502 | 2025-10-31 06:31:00 | AQUA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 20.6 |
| 126cca38-f598-35f4-9921-064d6c1627a0 | -11.14993 | -50.71872 | 2025-10-31 06:33:00 | AQUA_M-M | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 56.4 |
| 5b93d492-4605-3dcc-be0c-38a56f3c9697 | -10.92426 | -50.7737 | 2025-10-31 06:33:00 | AQUA_M-M | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 26.1 |
| b3bee291-0c49-3adb-a60f-2ad757a85b15 | -10.63568 | -52.18364 | 2025-10-31 06:33:00 | AQUA_M-M | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Amazônia | 8.1 |
| f3231696-8cba-3d80-af05-c574ad6d8b21 | -12.10021 | -47.10028 | 2025-10-31 06:33:00 | AQUA_M-M | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 23.7 |
| 5135e8a3-9a5a-3315-86ae-400e4128f9f6 | -11.14798 | -50.73354 | 2025-10-31 06:33:00 | AQUA_M-M | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 8.5 |
| 82003da7-a5d1-3e9f-bcf8-0dcaa4ff31b5 | -11.08348 | -51.53907 | 2025-10-31 06:33:00 | AQUA_M-M | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Cerrado | 10.8 |
| 4b7832ec-bbde-31bb-9a59-687884c889f6 | -11.55628 | -47.08776 | 2025-10-31 06:33:00 | AQUA_M-M | PORTO ALEGRE DO TOCANTINS | TOCANTINS | Brasil | 1718006 | 17 | 33 | nan | nan | nan | Cerrado | 65.7 |
| 53ef3ced-1d70-3e1c-9d25-1dc3cba5d54e | -11.55986 | -47.0582 | 2025-10-31 06:33:00 | AQUA_M-M | PORTO ALEGRE DO TOCANTINS | TOCANTINS | Brasil | 1718006 | 17 | 33 | nan | nan | nan | Cerrado | 157.3 |
| 7e20447a-7244-38f8-aeb8-3f4b74119e5a | -4.99664 | -44.72567 | 2025-10-31 11:57:00 | TERRA_M-M | JOSELÂNDIA | MARANHÃO | Brasil | 2105609 | 21 | 33 | nan | nan | nan | Cerrado | 23.6 |
| ebcf0d62-3383-3708-94cc-d02a79630aad | -4.00425 | -42.10583 | 2025-10-31 11:57:00 | TERRA_M-M | BATALHA | PIAUÍ | Brasil | 2201507 | 22 | 33 | nan | nan | nan | Caatinga | 8.7 |
| cb412be6-1a7c-3d97-9679-37ad9f71d91e | -5.69707 | -43.29275 | 2025-10-31 11:57:00 | TERRA_M-M | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 10.3 |
| f426abca-97ae-3d8a-b02b-2514139282ca | -4.654 | -42.51711 | 2025-10-31 11:57:00 | TERRA_M-M | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Caatinga | 24.4 |
| 339fae61-936a-3011-8615-b2d47fd963b9 | -3.50431 | -39.09919 | 2025-10-31 11:57:00 | TERRA_M-M | PARACURU | CEARÁ | Brasil | 2310209 | 23 | 33 | nan | nan | nan | Caatinga | 9.7 |
| 12844255-f71c-37ac-8cff-4b3892441979 | -3.32994 | -41.51709 | 2025-10-31 11:57:00 | TERRA_M-M | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 18.6 |
| dc887c47-29c2-31a9-ba7d-1e1fb8f11216 | -5.68822 | -43.2915 | 2025-10-31 11:57:00 | TERRA_M-M | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 29.6 |
| 836c88aa-37ad-3053-b14b-4e49f2eda140 | -3.62421 | -42.68083 | 2025-10-31 11:57:00 | TERRA_M-M | BREJO | MARANHÃO | Brasil | 2102101 | 21 | 33 | nan | nan | nan | Cerrado | 322.1 |
| 9d1dc607-29b3-3414-a233-94886b656f03 | -3.63557 | -42.67981 | 2025-10-31 11:57:00 | TERRA_M-M | BREJO | MARANHÃO | Brasil | 2102101 | 21 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 14bec329-16fa-3cc5-a9be-0c81fe5e33fc | -6.19789 | -41.60035 | 2025-10-31 11:57:00 | TERRA_M-M | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 10.1 |
| ca594a8d-52cb-3bec-9ab7-03ec6dd54eda | -3.94046 | -43.88008 | 2025-10-31 11:57:00 | TERRA_M-M | VARGEM GRANDE | MARANHÃO | Brasil | 2112704 | 21 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 6fbcf285-6ae7-3974-9ce5-663b0d1a0f10 | -6.01592 | -41.9669 | 2025-10-31 11:57:00 | TERRA_M-M | SANTA CRUZ DOS MILAGRES | PIAUÍ | Brasil | 2209153 | 22 | 33 | nan | nan | nan | Caatinga | 11.4 |
| 166f75bc-921e-3867-b12c-bf07780a9dac | -4.86508 | -42.5383 | 2025-10-31 11:57:00 | TERRA_M-M | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Caatinga | 9.2 |
| 0984ba49-febe-35ba-bbda-cc34b1a3dc9c | -4.99016 | -44.7284 | 2025-10-31 11:57:00 | TERRA_M-M | JOSELÂNDIA | MARANHÃO | Brasil | 2105609 | 21 | 33 | nan | nan | nan | Cerrado | 19.4 |
| 97527847-6ab6-3be0-859a-cf2f02c5381a | -5.17472 | -43.19986 | 2025-10-31 11:57:00 | TERRA_M-M | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 351a7290-0957-3671-8e34-852681a17e25 | -4.84478 | -42.74134 | 2025-10-31 11:57:00 | TERRA_M-M | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Cerrado | 16.4 |
| e7223e24-a194-37d3-b081-f10e19dd3331 | -5.18358 | -43.2011 | 2025-10-31 11:57:00 | TERRA_M-M | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 89b30a3d-803a-3dbe-9d55-9cea5f80d157 | -6.13198 | -42.77599 | 2025-10-31 11:57:00 | TERRA_M-M | ANGICAL DO PIAUÍ | PIAUÍ | Brasil | 2200608 | 22 | 33 | nan | nan | nan | Caatinga | 10.1 |
| ec9f4f02-4a45-3855-b7a7-e22c62ef9537 | -4.84605 | -42.73255 | 2025-10-31 11:57:00 | TERRA_M-M | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 40040a0e-9d13-3f51-bd3e-f214f15db5f9 | -3.46151 | -42.27868 | 2025-10-31 11:57:00 | TERRA_M-M | LUZILÂNDIA | PIAUÍ | Brasil | 2205805 | 22 | 33 | nan | nan | nan | Cerrado | 6.5 |


[Clique aqui para ver as próximas entradas](README44.md)
