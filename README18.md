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

## Dados Diários - Página 18

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| bc7bac71-61c6-39a4-bf6f-525e4de5d937 | -9.844 | -44.8449 | 2026-10-02 01:50:00 | GOES-19 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 65.0 |
| 4021acc8-394a-3a08-a781-b21befd32abb | -12.8435 | -51.4869 | 2026-10-02 02:00:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 209.8 |
| ee27fd1a-e737-32f4-9b00-54c8a91bd4c8 | -10.8007 | -53.7476 | 2026-10-02 02:00:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 158.3 |
| 252a82c1-4e9b-3981-a498-6c7adac8faf4 | -11.7541 | -43.5749 | 2026-10-02 02:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 136.0 |
| 78561c7f-40de-3c42-bd7d-1db3885fa4f9 | -2.0394 | -56.8593 | 2026-10-02 02:00:00 | GOES-19 | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | 65.5 |
| 93411261-ed0a-340b-8278-2b024dc9516a | -3.295 | -53.8597 | 2026-10-02 02:00:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 46.5 |
| 7a08bea5-ff76-3a18-a6a2-3d603a3e28dc | -3.1839 | -54.0839 | 2026-10-02 02:00:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 52.6 |
| 68ca7b48-e577-3760-9b21-d21544ef184a | -3.0008 | -53.8874 | 2026-10-02 02:00:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 51.7 |
| 9a6d24ca-03c3-3961-a0ce-481b6932c27b | -7.8682 | -44.169 | 2026-10-02 02:00:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 84.3 |
| 6f669b65-b311-3392-999b-056c57d4b2f5 | 1.7853 | -55.6251 | 2026-10-02 02:00:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 53.7 |
| 142cb434-e949-3b9b-9dfc-ea83206f046c | -4.2676 | -50.7506 | 2026-10-02 02:00:00 | GOES-19 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 113.8 |
| 1ef1b46c-05cf-3792-b1c6-a7cf8ef58509 | -2.0577 | -56.8591 | 2026-10-02 02:00:00 | GOES-19 | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | 57.0 |
| fa58623e-b407-3319-ad0d-3dcd3fd7ecf4 | -6.3952 | -56.4158 | 2026-10-02 02:00:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 68.0 |
| bf14f853-346c-3511-910e-980a1c26b8f0 | -4.2677 | -50.7297 | 2026-10-02 02:00:00 | GOES-19 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 73.0 |
| d090bc1f-27e8-3e43-908a-3a6403875158 | -6.2091 | -60.0187 | 2026-10-02 02:00:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 64.7 |
| e3ed1e48-dab5-3d8a-9b86-4713da01b360 | -13.3287 | -43.8573 | 2026-10-02 02:00:00 | GOES-19 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 90.5 |
| d81c2966-8c61-3b18-89bf-6ad076c16364 | -11.4691 | -43.4299 | 2026-10-02 02:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 94.7 |
| b2aedd4b-360e-3825-bb4c-e59250d67764 | -10.7818 | -53.7493 | 2026-10-02 02:00:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 163.1 |
| 5a945ab4-f981-3441-bdac-4296738102f4 | 1.767 | -55.6254 | 2026-10-02 02:00:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 29.8 |
| 606c71de-5718-3f33-8cd4-97a21e2e7a70 | -7.2889 | -55.5973 | 2026-10-02 02:00:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 81.7 |
| 9888be23-ba6a-3a74-8856-83e650896cc1 | -11.7926 | -43.5689 | 2026-10-02 02:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 119.7 |
| 44f13e05-ec5a-3a80-af01-20b937ca8fec | -3.0192 | -53.887 | 2026-10-02 02:00:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 55.2 |
| ef47c979-2cae-3f67-83ca-a66e24c6c1fa | -3.1655 | -54.1045 | 2026-10-02 02:00:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 46.8 |
| 8f15357b-87c4-3da5-83be-b1cdfd4b1e54 | -11.1615 | -44.6002 | 2026-10-02 02:00:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 103.7 |
| 26fb294c-6607-30ac-b0e9-fbaac654bee7 | -3.1655 | -54.0844 | 2026-10-02 02:00:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 56.7 |
| 69ebde91-cd1d-334d-a0d9-ac9ed6d3e06b | -6.0074 | -53.5325 | 2026-10-02 02:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 56.8 |
| 759b2b4d-537d-3f61-8545-c91d5f2983b1 | -10.8005 | -53.7682 | 2026-10-02 02:00:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 162.1 |
| c8f080a1-ab0e-38cf-9787-db1a02aa0821 | -4.4507 | -47.9112 | 2026-10-02 02:00:00 | GOES-19 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 65.3 |
| a87eda67-d646-389d-9cad-9c72afd485f5 | -6.209 | -60.0378 | 2026-10-02 02:00:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 73.0 |
| 9a30b84c-1c36-3a8a-847f-28827f5df2bc | -12.8439 | -51.4656 | 2026-10-02 02:00:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 125.3 |
| 53d5a304-16c7-34e9-b049-382103e54fea | -12.8247 | -51.4679 | 2026-10-02 02:00:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 105.6 |
| 4c33e619-127f-3a78-8ab2-c5b3cf2c0b8b | -3.1299 | -53.7431 | 2026-10-02 02:00:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 43.0 |
| 5edc93f9-8258-3e8d-916f-2165646d8881 | -5.7563 | -45.152 | 2026-10-02 02:00:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 55.7 |
| 43d62dff-43f9-3fbe-9f89-e52c0c3c2a74 | -7.7551 | -49.2067 | 2026-10-02 02:00:00 | GOES-19 | ARAPOEMA | TOCANTINS | Brasil | 1702307 | 17 | 33 | nan | nan | nan | Amazônia | 50.7 |
| 6e535f6f-eac7-325d-9d4c-cd7f96a18da3 | -3.1838 | -54.104 | 2026-10-02 02:00:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 76.2 |
| d7401e2b-fbd0-3d64-b99f-90be6e842971 | -4.4506 | -47.9329 | 2026-10-02 02:00:00 | GOES-19 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 57.9 |
| d86a5b6c-462a-32ed-a01a-acf401468474 | -12.9803 | -51.3 | 2026-10-02 02:00:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 111.9 |
| 840a1c81-7426-3ab1-be42-10fe7c6b20fc | -13.0183 | -51.3166 | 2026-10-02 02:00:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 79.8 |
| 32cccfb2-1529-34e6-81af-b40a304e98a2 | -10.7816 | -53.7699 | 2026-10-02 02:00:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 195.1 |
| e8d58524-5aca-3b00-afd5-e839c7fddc44 | -7.0478 | -55.6302 | 2026-10-02 02:00:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 76.6 |
| 159fc08a-2700-349a-9a74-8fb9c59c1413 | -13.3481 | -43.8538 | 2026-10-02 02:00:00 | GOES-19 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 191.8 |
| ea825ba1-3031-3661-b80f-b1a7153bfd9d | -11.7733 | -43.5719 | 2026-10-02 02:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 188.9 |
| 67f53c98-22cd-30fd-8c67-854eff5e33ff | -12.8254 | -51.4253 | 2026-10-02 02:00:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 74.0 |
| 25b2060c-faf3-3fd3-a511-e6bd4cd03f80 | -7.887 | -44.1671 | 2026-10-02 02:00:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 94.5 |
| 2d3682b6-36c2-3e45-b518-9eb94a9683b1 | -2.0576 | -56.8786 | 2026-10-02 02:00:00 | GOES-19 | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | 64.4 |
| 6e46fb9a-1643-3f27-b5e9-611ceffde3f9 | -12.9995 | -51.2976 | 2026-10-02 02:00:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 377.8 |
| cc9d34c8-ec20-37e0-a64f-cdbe2e2dfa5f | -12.9998 | -51.2763 | 2026-10-02 02:00:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 129.6 |
| 9c1df309-5c05-3f6a-97a7-fd636628d4a5 | -12.8432 | -51.5082 | 2026-10-02 02:00:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 81.6 |
| dd3a833c-8821-3b74-95d2-5ced3ba199a5 | -13.0187 | -51.2953 | 2026-10-02 02:00:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 112.7 |
| 3c102111-72a5-345c-acd6-3ad7fda15e26 | -3.2767 | -53.84 | 2026-10-02 02:00:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 48.6 |
| 1e8a4548-2292-3d8e-980d-cb24700fa4f7 | -11.1424 | -44.6029 | 2026-10-02 02:00:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 202.1 |
| bf3da799-25a1-32aa-bfb8-a24d5c13675f | -12.8244 | -51.4892 | 2026-10-02 02:00:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 119.2 |
| 46f8635a-b68d-36c1-9aa0-ff0ed2a10960 | -13.3476 | -43.8776 | 2026-10-02 02:00:00 | GOES-19 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 104.9 |
| 02f18b71-e10c-379b-85af-13c789a6c77f | -12.8627 | -51.4846 | 2026-10-02 02:00:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 89.5 |
| d38d5eaf-8d1a-31f1-b9dc-c54497e656ee | -3.2951 | -53.8395 | 2026-10-02 02:00:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 57.1 |
| dc7a405e-ab1a-3bbc-b608-2d707695f180 | -4.2953 | -49.1021 | 2026-10-02 02:00:00 | GOES-19 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 53.6 |
| c792fb38-6c35-3609-ac9d-252940369b85 | -11.142 | -44.6261 | 2026-10-02 02:00:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 86.4 |
| dd1a3bd9-9871-30c6-94bc-876bc9281301 | -12.9992 | -51.319 | 2026-10-02 02:00:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 158.8 |
| 1e6ef0c1-ad42-3ff8-91b5-b958aea29758 | -2.0393 | -56.8789 | 2026-10-02 02:00:00 | GOES-19 | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | 75.0 |
| 0af3c5cd-a3ca-37ee-aced-b84b9b178ed6 | -2.0394 | -56.8593 | 2026-10-02 02:10:00 | GOES-19 | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | 65.4 |
| fb64872c-d889-3a74-ac15-731034c92569 | -11.142 | -44.6261 | 2026-10-02 02:10:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 64.8 |
| e8f770e4-6ff2-371b-98b3-2fca14debf25 | -10.7627 | -53.7715 | 2026-10-02 02:10:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 72.3 |
| 5569299b-4c78-3ebc-8854-836a22bf40cb | -3.1655 | -54.0844 | 2026-10-02 02:10:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 71.9 |
| 488389aa-6897-3dee-a9a4-22ca82cd45fb | -11.4691 | -43.4299 | 2026-10-02 02:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 90.7 |
| f4eee2ab-e487-361f-85e3-5c9eb8e22417 | -10.8005 | -53.7682 | 2026-10-02 02:10:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 167.8 |
| 139cc0eb-4042-33d2-8180-dac569023169 | -12.9995 | -51.2976 | 2026-10-02 02:10:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 217.1 |
| 8d5e58ba-fffb-3711-b7c0-2a4d69d42c57 | -13.3481 | -43.8538 | 2026-10-02 02:10:00 | GOES-19 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 159.4 |
| e024e0fd-4a62-366a-9ade-8a3cba77a8ed | -11.1424 | -44.6029 | 2026-10-02 02:10:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 156.2 |
| 8ac06656-c25d-3374-b00e-083056159e5b | -13.0187 | -51.2953 | 2026-10-02 02:10:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 93.6 |
| c8d9eeb9-38dc-3ffa-a87a-2a783e8a7af0 | -11.1615 | -44.6002 | 2026-10-02 02:10:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 87.9 |
| 0e9aba05-4c3b-3e26-b068-2263308cc483 | -6.3952 | -56.4158 | 2026-10-02 02:10:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 67.3 |
| 6893364e-3fc5-3410-a042-01170897aaec | -4.4691 | -47.932 | 2026-10-02 02:10:00 | GOES-19 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 50.0 |
| efb9ab79-459f-39c3-8b7a-2171a943f9a5 | -12.9803 | -51.3 | 2026-10-02 02:10:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 71.5 |
| 864fc0c9-c0d4-3f09-af66-06527d34cdca | -4.2676 | -50.7506 | 2026-10-02 02:10:00 | GOES-19 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 110.1 |
| 41d3a2c2-516a-3679-bf28-71f06b4c3183 | -13.3287 | -43.8573 | 2026-10-02 02:10:00 | GOES-19 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 78.9 |
| 99fa6834-87e9-312a-b00f-4abea066bed7 | -7.7551 | -49.2067 | 2026-10-02 02:10:00 | GOES-19 | ARAPOEMA | TOCANTINS | Brasil | 1702307 | 17 | 33 | nan | nan | nan | Amazônia | 46.0 |
| fc8ce68c-3c93-31f2-aca1-17e72b8d7ced | -12.9992 | -51.319 | 2026-10-02 02:10:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 88.1 |
| 5473515e-5c1c-3fd5-92f0-47b17bea87e5 | -13.3476 | -43.8776 | 2026-10-02 02:10:00 | GOES-19 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 83.2 |
| 2cf44fb2-363d-3eb9-bb4a-ea4d6d386d62 | -10.8007 | -53.7476 | 2026-10-02 02:10:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 194.4 |
| dc65c1e4-5bdd-3c3a-9ead-41884c7602e8 | -4.4693 | -47.9103 | 2026-10-02 02:10:00 | GOES-19 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 63.4 |
| 05ad4471-fef2-3c5e-850a-f4cfdd5a8c5b | -3.1838 | -54.104 | 2026-10-02 02:10:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 66.5 |
| 88e68b98-25c7-3dd2-b513-874b19886222 | -10.7818 | -53.7493 | 2026-10-02 02:10:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 216.3 |
| e015a339-9831-3651-bec8-d1deb3ff0042 | -3.1839 | -54.0839 | 2026-10-02 02:10:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 60.6 |
| eab85d5c-7369-31f4-9bbb-9abdfadb11e4 | -7.2889 | -55.5973 | 2026-10-02 02:10:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 81.2 |
| fd8a3707-ab20-33a3-9a16-59c5daa4cc63 | -4.4506 | -47.9329 | 2026-10-02 02:10:00 | GOES-19 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 71.3 |
| 856f1cec-7b6a-396d-9b56-888f82a09ed3 | -11.7733 | -43.5719 | 2026-10-02 02:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 168.3 |
| 19904bc0-4e9d-31e0-a359-5688af709387 | -12.9998 | -51.2763 | 2026-10-02 02:10:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 99.9 |
| 4ae3194b-e317-33bf-b238-ef58c14d2dfc | -6.209 | -60.0378 | 2026-10-02 02:10:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 57.7 |
| aac1be05-a273-30c3-a0dc-942433ba5c03 | -2.0393 | -56.8789 | 2026-10-02 02:10:00 | GOES-19 | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | 74.3 |
| a0f334de-88c1-3f54-a73c-61935915db9a | -4.2677 | -50.7297 | 2026-10-02 02:10:00 | GOES-19 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 67.9 |
| 9e8ffb53-abf4-36c4-9fe3-c4ea61594655 | -11.7541 | -43.5749 | 2026-10-02 02:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 103.2 |
| 9e042ea9-6b9c-363f-9837-e7251607ed09 | -11.7926 | -43.5689 | 2026-10-02 02:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 100.1 |
| 1adfc938-f916-3012-b639-22af3f87ab4f | -2.0577 | -56.8591 | 2026-10-02 02:10:00 | GOES-19 | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | 58.6 |
| f2c4f245-2651-3585-a319-8ab5008bc3af | -2.0576 | -56.8786 | 2026-10-02 02:10:00 | GOES-19 | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | 65.4 |
| 2a9b98c9-4de5-3d2d-a103-858b0d20362f | -4.2953 | -49.1021 | 2026-10-02 02:10:00 | GOES-19 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 53.5 |
| 99145980-01f1-3a0c-8631-5af5e8eb9e0e | -4.4507 | -47.9112 | 2026-10-02 02:10:00 | GOES-19 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 89.8 |
| a55e8341-fca0-33d6-a508-a320ea9e002f | -6.2091 | -60.0187 | 2026-10-02 02:10:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 56.3 |
| 21f69d1e-d1e6-3b91-a0e5-eb8e1197b5ed | -7.4031 | -55.2114 | 2026-10-02 02:10:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 66.6 |
| c3eed8f0-0e88-3a1b-9e94-869e97edf61b | -10.7816 | -53.7699 | 2026-10-02 02:10:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 231.1 |
| c421f725-e9b9-33b7-9de1-92962d3d1434 | -11.77 | -43.57 | 2026-10-02 02:15:00 | MSG-03 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | nan |


[Clique aqui para ver as próximas entradas](README19.md)
