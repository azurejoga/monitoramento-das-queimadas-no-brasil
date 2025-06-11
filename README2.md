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

## Dados Diários - Página 2

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 928cbda8-b635-30f1-986b-0163a5d2a90f | -12.2047 | -49.619202 | 2025-06-11 00:14:00 | METOP-B | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| c5fc88f8-dae5-37a1-9d58-101b0599bb75 | -17.397699 | -48.0499 | 2025-06-11 00:14:00 | METOP-B | URUTAÍ | GOIÁS | Brasil | 5221809 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 963ff767-bea2-3e97-8762-82c2f152613e | -10.05 | -48.662701 | 2025-06-11 00:14:00 | METOP-B | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| f49047e5-0994-3661-a577-29c9c92706ed | -5.6458 | -43.592999 | 2025-06-11 00:14:00 | METOP-B | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| c802550b-82db-34f8-953a-1b11da331d75 | -7.2314 | -44.784698 | 2025-06-11 00:14:00 | METOP-B | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| b3a11580-8fff-3421-ac3f-8a79e73b39ec | -9.611 | -49.0065 | 2025-06-11 00:14:00 | METOP-B | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| fdab2b7b-22f3-3bd7-8bcb-2a2b49bff0ab | -4.4221 | -47.659 | 2025-06-11 00:14:00 | METOP-B | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8b6044f7-180c-37d7-8ae1-637435ec0d1c | -8.9701 | -47.960201 | 2025-06-11 00:14:00 | METOP-B | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 6f900e31-d238-3d1e-9640-ba79b1c25730 | -3.626 | -47.510399 | 2025-06-11 00:14:00 | METOP-B | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d774fd62-c822-3cc3-a4df-d332c56f1f6e | -10.1883 | -49.586899 | 2025-06-11 00:14:00 | METOP-B | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 28f8d2af-8cc6-3bc6-9d91-5cdc0d2d5220 | -5.772 | -43.604 | 2025-06-11 00:14:00 | METOP-B | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 3d2c2438-c102-3de6-8c72-baa5f3c61ecd | -9.8466 | -47.875301 | 2025-06-11 00:14:00 | METOP-B | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 0c2b2cfd-e1ee-3f64-b9a2-31b14ad10f14 | -7.4665 | -45.493401 | 2025-06-11 00:14:00 | METOP-B | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 445dbaa6-3f7c-346c-a151-616efbb00a06 | -14.262 | -45.4972 | 2025-06-11 00:14:00 | METOP-B | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| bf70f98d-d0a1-39c7-8fd3-00fd6c633b7f | -13.5726 | -44.272301 | 2025-06-11 00:14:00 | METOP-B | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 841f3123-208a-3e3e-b9d8-7b2bfba81180 | -10.1964 | -49.5769 | 2025-06-11 00:14:00 | METOP-B | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| a5a9fe7e-478f-31ce-845a-fee987fa3cbc | -20.099501 | -50.859798 | 2025-06-11 00:14:00 | METOP-B | SANTA RITA D'OESTE | SÃO PAULO | Brasil | 3547403 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| b2851d7a-4e5a-3c78-a339-3004a1b679f6 | -10.8801 | -54.7188 | 2025-06-11 00:14:00 | METOP-B | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| f9c58e8f-5957-3588-a6af-6178f7394950 | -10.1866 | -49.578999 | 2025-06-11 00:14:00 | METOP-B | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 67fe7623-0126-30ce-9c1b-7c9faec5603a | -12.2145 | -49.6171 | 2025-06-11 00:14:00 | METOP-B | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 7321476b-95c2-3a83-8e01-fc06fc6809f9 | -6.9505 | -44.550598 | 2025-06-11 00:14:00 | METOP-B | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 2fb5dfc9-dd91-39a3-8a45-b1429585fbc9 | -12.8437 | -47.376598 | 2025-06-11 00:14:00 | METOP-B | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 3d26b668-0d6f-3392-9d57-b7875a387563 | -10.2414 | -52.2174 | 2025-06-11 00:14:00 | METOP-B | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| fc563073-a490-3977-b0b5-7bc61ad0bb09 | -8.9603 | -47.962399 | 2025-06-11 00:14:00 | METOP-B | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 37bd1f83-0522-3390-884b-d176c1c4697f | -13.5709 | -44.264801 | 2025-06-11 00:14:00 | METOP-B | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| e625fb01-572d-32b5-8d01-d29924f56bc2 | -14.5067 | -43.799801 | 2025-06-11 00:14:00 | METOP-B | MALHADA | BAHIA | Brasil | 2920205 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 971d4d1c-2312-3aa8-a8f7-bf91ce1a4475 | -6.9238 | -45.781101 | 2025-06-11 00:14:00 | METOP-B | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 493dad50-4690-3a0c-b221-14eff90e5bd2 | -10.2437 | -52.228401 | 2025-06-11 00:14:00 | METOP-B | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 9b781a04-96af-3b50-89bb-0edbf2664828 | -10.6535 | -49.411701 | 2025-06-11 00:14:00 | METOP-B | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 6f7223ef-3871-391e-ad4a-6247c986c897 | -8.2717 | -44.957298 | 2025-06-11 00:14:00 | METOP-B | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 728e0c9b-08c4-3490-9721-8beb5d0b975c | -6.0611 | -48.120998 | 2025-06-11 00:14:00 | METOP-B | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 4ddaac42-85a0-3cfe-b951-0d5cb7163d6b | -4.5544 | -48.017799 | 2025-06-11 00:14:00 | METOP-B | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9cad473f-c88c-3f4c-96eb-cdfde53cb1e7 | -6.9895 | -47.070702 | 2025-06-11 00:14:00 | METOP-B | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 996a592e-9ee4-3d71-9981-9313dda0f896 | -10.5078 | -53.6189 | 2025-06-11 00:14:00 | METOP-B | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 0eeab4f1-ee41-3e4e-ad0a-b9692e21573a | -12.2679 | -47.001499 | 2025-06-11 00:14:00 | METOP-B | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 50485130-4713-34c9-8a7d-046741bddcbc | -7.4601 | -45.510601 | 2025-06-11 00:14:00 | METOP-B | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 83dc9ee0-db3f-30cc-9678-20402ee47daa | -9.5353 | -47.491402 | 2025-06-11 00:14:00 | METOP-B | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| e36d2496-3ea6-3ede-aadd-3833730fa4ca | -9.773 | -48.195202 | 2025-06-11 00:14:00 | METOP-B | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| e326954e-fd37-378c-8c55-f5a7a1a0023f | -10.7048 | -49.507 | 2025-06-11 00:20:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 32.6 |
| c959fb26-9a61-3556-8871-369bad78b9ca | -10.6681 | -49.4246 | 2025-06-11 00:20:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 50.4 |
| 99b3759e-a652-368a-b6ce-1367552dcac2 | -7.4765 | -45.4872 | 2025-06-11 00:20:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 49.1 |
| 47a7d8a8-a54a-3b63-902e-a92413436933 | -10.6492 | -49.4267 | 2025-06-11 00:20:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 84.2 |
| 891985cd-2a80-3e20-bd4a-adc9f6fd67b9 | -7.4763 | -45.5099 | 2025-06-11 00:20:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 151.8 |
| c7944bcd-eb3d-31d1-a640-1d0e87dd129f | -7.4575 | -45.5116 | 2025-06-11 00:20:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 69.5 |
| c50d9368-3eb2-3eaf-85ad-b0ff49891461 | -10.6681 | -49.4246 | 2025-06-11 00:30:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 52.8 |
| ecd94f81-ceaf-3fb1-8f59-799423acdf4c | -12.5175 | -57.2231 | 2025-06-11 00:30:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 56.9 |
| fb10594c-c521-3f8c-9066-a91d58076dc8 | -7.4765 | -45.4872 | 2025-06-11 00:30:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 43.7 |
| 9e4aaf9b-e3b6-3b72-9504-69d878a690d1 | -16.2962 | -49.9354 | 2025-06-11 00:30:00 | GOES-19 | ANICUNS | GOIÁS | Brasil | 5201306 | 52 | 33 | nan | nan | nan | Cerrado | 73.0 |
| 74762143-eaab-3837-89f8-24fb948c6086 | -10.6492 | -49.4267 | 2025-06-11 00:30:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 66.8 |
| f5fb48d6-793f-3183-b02b-4f1ef5e936ab | -7.4575 | -45.5116 | 2025-06-11 00:30:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 104.0 |
| a7b727e2-a173-38b0-a708-0d6687e0a94c | -7.4577 | -45.489 | 2025-06-11 00:30:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 40.5 |
| 9fd29129-f44e-33b2-b2da-40af21e0366f | -7.4763 | -45.5099 | 2025-06-11 00:30:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 107.5 |
| 57d6e405-a3ff-3249-a7a7-23344ed1b4cc | -10.6492 | -49.4267 | 2025-06-11 00:40:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 62.9 |
| 87c7cdf7-def1-33e4-b795-1e1dc21df26c | -7.4763 | -45.5099 | 2025-06-11 00:40:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 108.6 |
| ca18e42f-c835-3107-b134-012a1fd34c62 | -16.2962 | -49.9354 | 2025-06-11 00:40:00 | GOES-19 | ANICUNS | GOIÁS | Brasil | 5201306 | 52 | 33 | nan | nan | nan | Cerrado | 111.9 |
| f3a64d6a-3d76-37a3-8cd8-f9e2ace2c71f | -12.5175 | -57.2231 | 2025-06-11 00:40:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 55.0 |
| b13d7d93-59d9-33c5-bd79-1ae3d3b3a68d | -7.4575 | -45.5116 | 2025-06-11 00:40:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 89.4 |
| d102bf4e-7611-3934-81dc-774fc4c25ed4 | -7.4765 | -45.4872 | 2025-06-11 00:40:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 41.7 |
| c20f749f-df73-3a9f-87b3-10aa8d882a54 | -10.6681 | -49.4246 | 2025-06-11 00:40:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 56.7 |
| bab57392-5466-3737-9ad9-64ff1c3dcf7f | -7.4763 | -45.5099 | 2025-06-11 00:50:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 122.8 |
| 69fcd5a1-34ff-3647-863e-c4d7aa6b3c91 | -10.6681 | -49.4246 | 2025-06-11 00:50:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 49.4 |
| 2324eb9c-853f-3fc2-8ca6-fbd8e5ba9c5e | -10.6492 | -49.4267 | 2025-06-11 00:50:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 78.6 |
| ff72c313-3958-3240-9bb8-909709d869c4 | -7.4575 | -45.5116 | 2025-06-11 00:50:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 68.2 |
| cdc6160f-0c66-3360-ad77-e4a3923229bb | -7.4763 | -45.5099 | 2025-06-11 01:00:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 114.3 |
| 171b3508-d204-34ab-bbba-9b0d5c3080fc | -7.4575 | -45.5116 | 2025-06-11 01:00:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 78.0 |
| 237343b1-744b-3a8a-a0cc-2f05a4f91a1f | -10.8832 | -54.742 | 2025-06-11 01:00:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 27.0 |
| fbfffa03-5724-3131-b261-340dbf318425 | -10.6681 | -49.4246 | 2025-06-11 01:00:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 39.4 |
| 23146c38-97cc-3859-9d67-3b854d9e88f5 | -10.6492 | -49.4267 | 2025-06-11 01:00:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 63.5 |
| e1e540e0-411b-39d3-a353-8efd70681a17 | -10.5132 | -53.632301 | 2025-06-11 01:04:00 | METOP-C | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 3428fb6e-58e9-3f4f-be6b-f1a5a142204b | -10.8894 | -54.7523 | 2025-06-11 01:04:00 | METOP-C | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 666e5e59-d72b-34f4-ac32-470b7f60fee6 | -3.6307 | -47.5061 | 2025-06-11 01:04:00 | METOP-C | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 64fabe29-7da2-37df-bc39-4f6e75d72570 | -11.7821 | -54.371799 | 2025-06-11 01:04:00 | METOP-C | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| b8c81b1a-8a00-31dc-81c8-4eedc2c8ca1e | -11.0545 | -55.031898 | 2025-06-11 01:04:00 | METOP-C | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| bc22efed-6f41-38e3-aa18-f3fc25fb415c | -10.0833 | -52.746498 | 2025-06-11 01:04:00 | METOP-C | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| cb8c8b15-7c19-3040-acad-e543e7aa8444 | -10.8878 | -54.745201 | 2025-06-11 01:04:00 | METOP-C | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| b491e593-079b-3f7a-b374-af1720a70656 | -7.4557 | -45.520802 | 2025-06-11 01:04:00 | METOP-C | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 9546b80e-3b19-380e-902f-a2d44ad16145 | -11.1465 | -53.9259 | 2025-06-11 01:04:00 | METOP-C | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| ca9d017c-609e-392d-b6ed-49c326123d04 | -12.2594 | -57.6106 | 2025-06-11 01:04:00 | METOP-C | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 1de8ba4a-6803-3854-9f6c-6d71c8114aa4 | -10.8796 | -54.754501 | 2025-06-11 01:04:00 | METOP-C | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 855cde1d-73f7-3ed1-89c5-1a4788fef477 | -12.2692 | -57.608501 | 2025-06-11 01:04:00 | METOP-C | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| db781e98-0bee-3441-9379-c3b150a03640 | -8.9733 | -47.968201 | 2025-06-11 01:04:00 | METOP-C | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| d9b13515-b3a8-343d-b893-db2ef164a6b0 | -10.5148 | -53.639198 | 2025-06-11 01:04:00 | METOP-C | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| fcf39ef1-cf03-3f89-961e-15f442463574 | -7.4799 | -45.534901 | 2025-06-11 01:04:00 | METOP-C | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 460a4ddf-f30c-3996-bef5-0d8dd3fab3c3 | -20.7647 | -48.534901 | 2025-06-11 01:04:00 | METOP-C | COLINA | SÃO PAULO | Brasil | 3512001 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 40448b33-c8f1-311b-8f56-8f59075ae303 | -7.4703 | -45.496899 | 2025-06-11 01:04:00 | METOP-C | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 44c7d8a5-d7fb-38da-8972-87377a237981 | -7.4702 | -45.5373 | 2025-06-11 01:04:00 | METOP-C | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 38d20122-0e8b-348c-8a80-0cba14a0a6e0 | -10.1978 | -49.600101 | 2025-06-11 01:04:00 | METOP-C | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 6774778e-3ae6-3586-8bac-45de494651c2 | -7.4654 | -45.518299 | 2025-06-11 01:04:00 | METOP-C | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 06680290-3183-357f-b3e1-9dc2a2d9feaa | -11.1449 | -53.9189 | 2025-06-11 01:04:00 | METOP-C | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| ad1df1f7-3e58-3c8c-ba04-4d4e422d5b7f | -7.4606 | -45.499298 | 2025-06-11 01:04:00 | METOP-C | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 71af2986-8c57-3d22-9b9c-d2cc4559fb53 | -10.8744 | -54.3181 | 2025-06-11 01:04:00 | METOP-C | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| ef35d27b-ae92-3167-b0fb-fe9fb7861fce | -10.878 | -54.747398 | 2025-06-11 01:04:00 | METOP-C | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 40998d58-9081-3afb-881f-5072a87ea7a8 | -11.1481 | -53.9328 | 2025-06-11 01:04:00 | METOP-C | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 46747cf3-26f2-31f4-af81-dcaaa39816d3 | -3.6346 | -47.522099 | 2025-06-11 01:04:00 | METOP-C | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f7f15281-90ca-343d-bd4b-cc96b5adf5cb | -10.9528 | -55.314899 | 2025-06-11 01:04:00 | METOP-C | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| fc124cda-a433-322a-b90f-0bf62edc4423 | -10.1955 | -49.590698 | 2025-06-11 01:04:00 | METOP-C | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 2f11ad4d-addb-33ea-862c-158c421a1c82 | -10.876 | -54.3251 | 2025-06-11 01:04:00 | METOP-C | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 48749691-1cc6-35ae-8250-6abbf6004c52 | -11.7837 | -54.378899 | 2025-06-11 01:04:00 | METOP-C | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| dd54c685-a4be-300d-9f37-c0d60d30a338 | -7.4751 | -45.5159 | 2025-06-11 01:04:00 | METOP-C | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| b84ddd4b-83a4-31d4-ab6d-2afc5d836e98 | -10.0849 | -52.753601 | 2025-06-11 01:04:00 | METOP-C | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | nan |


[Clique aqui para ver as próximas entradas](README3.md)
