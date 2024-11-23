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

## Dados Diários - Página 11

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 4810021c-3074-32b5-8e24-11f23dfc404f | -3.1004 | -54.2827 | 2024-11-23 00:45:00 | METOP-B | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b0b8d410-5219-326a-878b-b1b1a05ceac8 | -2.8955 | -54.0135 | 2024-11-23 00:45:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3c658d56-cb66-3cd5-a147-7d3872854c9a | -2.8319 | -54.0061 | 2024-11-23 00:45:00 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 933a7126-efa2-3cdc-a250-29a5bb123b2f | -1.74 | -52.369202 | 2024-11-23 00:45:00 | METOP-B | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 18c8aac9-94a5-3268-9553-cd551d20b171 | -3.0348 | -45.1712 | 2024-11-23 00:45:00 | METOP-B | VIANA | MARANHÃO | Brasil | 2112803 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 6f25a600-c2f0-370f-b019-9587a03008cb | -2.6066 | -45.6105 | 2024-11-23 00:45:00 | METOP-B | SANTA LUZIA DO PARUÁ | MARANHÃO | Brasil | 2110039 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 1bf84dce-3c49-3b47-87a3-15b9484b85f1 | -1.3094 | -51.743 | 2024-11-23 00:45:00 | METOP-B | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5c86c691-135e-34ae-ad22-24750d9922c4 | -3.7516 | -49.992401 | 2024-11-23 00:45:00 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4ad2364f-8aea-38ab-b375-7952743c55d4 | -3.7558 | -50.010601 | 2024-11-23 00:45:00 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7c9d6968-10d1-34bc-aad6-b8f304730d69 | -3.7273 | -46.062302 | 2024-11-23 00:45:00 | METOP-B | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| a3b8a33e-417c-3c5f-8646-08f505d8aee3 | -2.5764 | -53.969799 | 2024-11-23 00:45:00 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 027d6afc-fc8a-38c8-a6e8-da2addf07903 | -1.366 | -52.2645 | 2024-11-23 00:45:00 | METOP-B | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0e07663c-c56b-3e5e-a5cc-6a011762f34c | -3.2151 | -54.242901 | 2024-11-23 00:45:00 | METOP-B | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b22e45f4-a8c7-3ebf-b9bd-2fec61e54c8b | -3.1213 | -53.097801 | 2024-11-23 00:45:00 | METOP-B | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0e803174-b1bc-37e6-9db3-913dc98c3cbf | -3.0069 | -51.5518 | 2024-11-23 00:45:00 | METOP-B | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3f037425-fa45-3b81-b383-29cb1ed64453 | -1.3985 | -55.190201 | 2024-11-23 00:45:00 | METOP-B | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4d106311-a561-37a5-98cd-9ec4c10aa514 | -2.7197 | -45.699402 | 2024-11-23 00:45:00 | METOP-B | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 729647ad-f151-33b8-9d9e-c4874d436c08 | -3.2762 | -53.828701 | 2024-11-23 00:45:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7ffdccf9-c3be-3b7f-88af-9f8217428382 | -3.1013 | -53.738499 | 2024-11-23 00:45:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| fb821f2d-5b2f-3444-800b-be623a5dabc4 | -2.7679 | -54.041801 | 2024-11-23 00:45:00 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| adae3f2a-f390-3674-834f-da0ac7b080a2 | -1.7864 | -53.6203 | 2024-11-23 00:45:00 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4698e475-97cd-3d90-91b7-8c161bb0e7d0 | -3.2513 | -54.2206 | 2024-11-23 00:45:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| af560c95-8332-37e5-8b89-34acfcd52c74 | -1.8033 | -52.284901 | 2024-11-23 00:45:00 | METOP-B | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 892032bd-54c8-3c12-9c09-2472266bcb64 | -1.6326 | -53.304798 | 2024-11-23 00:45:00 | METOP-B | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4ad1b8f8-9e9f-31a9-92a6-44b084e69ef6 | -4.5564 | -48.008801 | 2024-11-23 00:45:00 | METOP-B | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 845a3040-a932-3c71-a52d-1f8f4ea01d25 | 0.7675 | -50.795101 | 2024-11-23 00:45:00 | METOP-B | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | nan |
| 2305c9b9-fc5a-3333-9981-527e27f45fdc | -1.6117 | -52.575401 | 2024-11-23 00:45:00 | METOP-B | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| cfcaec77-a02a-3911-bc50-e7bd769a9e24 | -2.6874 | -45.649601 | 2024-11-23 00:45:00 | METOP-B | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| b999649b-2971-32d7-a6bf-4b1cbcd62ce6 | -3.6865 | -50.1119 | 2024-11-23 00:45:00 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ae0a1955-526e-386c-9c0f-7e1f9f961a36 | -3.9333 | -47.195 | 2024-11-23 00:45:00 | METOP-B | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 72d4c4eb-9429-321b-b41e-4d43e56414b5 | -0.7683 | -51.7635 | 2024-11-23 00:45:00 | METOP-B | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | nan |
| 67ab7259-8f52-3391-a9fb-f102899ae15a | -3.2497 | -54.213799 | 2024-11-23 00:45:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6607ca5a-40df-3d68-86f8-fd68a42a92e0 | -3.1886 | -51.354599 | 2024-11-23 00:45:00 | METOP-B | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| cbe5ec4c-6680-34fb-ae4e-26cc2ad19729 | -4.1551 | -50.089699 | 2024-11-23 00:45:00 | METOP-B | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 79e950f4-70da-3539-8ec1-8dac273ac435 | -2.8138 | -54.0172 | 2024-11-23 00:45:00 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| dadb3e0d-c633-345f-9dae-679ab8a92ad7 | -1.8921 | -53.313 | 2024-11-23 00:45:00 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 82361dc3-7563-3d7e-8c49-e6567c444fee | -1.9375 | -54.061401 | 2024-11-23 00:45:00 | METOP-B | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9fe8d89c-4fe0-3392-83c1-374db44da6c6 | -2.1712 | -45.672901 | 2024-11-23 00:45:00 | METOP-B | GOVERNADOR NUNES FREIRE | MARANHÃO | Brasil | 2104677 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 64eb4c8b-602c-3ab3-888b-db8888f87fca | -5.5667 | -46.284302 | 2024-11-23 00:45:00 | METOP-B | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| e432fc80-d3d9-3a3b-8e2f-6d939fe39186 | -1.7817 | -53.599602 | 2024-11-23 00:45:00 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 94907646-fb75-3b77-90a9-03ed1e1bbc34 | -3.0256 | -45.132198 | 2024-11-23 00:45:00 | METOP-B | MATINHA | MARANHÃO | Brasil | 2106508 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 3cc02211-5b49-3cca-bad8-64e06fb224e7 | -1.7734 | -53.6087 | 2024-11-23 00:45:00 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 55afdbe5-21af-3e91-b776-4716f416231d | -2.0592 | -53.231899 | 2024-11-23 00:45:00 | METOP-B | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1aa721d9-6086-3876-9b48-81804042c46b | -3.8035 | -51.3396 | 2024-11-23 00:45:00 | METOP-B | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| dec99dde-b5fa-3b76-bcc9-5488cc05e052 | -1.116 | -53.390301 | 2024-11-23 00:45:00 | METOP-B | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8a575290-b151-300a-b02d-9b7869a24000 | -1.7811 | -53.643101 | 2024-11-23 00:45:00 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 71c10719-bd8a-3239-9caa-d5ac5792b94e | -2.1809 | -45.670601 | 2024-11-23 00:45:00 | METOP-B | GOVERNADOR NUNES FREIRE | MARANHÃO | Brasil | 2104677 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 5678b506-14a5-3ed4-a24d-89af8d678216 | -2.9535 | -45.087002 | 2024-11-23 00:45:00 | METOP-B | MATINHA | MARANHÃO | Brasil | 2106508 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 7199c8ce-a35c-3ca4-9f58-dae3a5ffb994 | -2.8175 | -45.1604 | 2024-11-23 00:45:00 | METOP-B | PALMEIRÂNDIA | MARANHÃO | Brasil | 2107605 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 05bb3e04-27a2-3ccd-880b-d3836c156d4c | -1.7244 | -53.2551 | 2024-11-23 00:45:00 | METOP-B | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ba4a837d-e7ba-3142-a614-15a145cb2b3c | -1.3054 | -52.2701 | 2024-11-23 00:45:00 | METOP-B | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 69d8645f-734a-3a90-b8a9-9965240f2600 | -3.068 | -53.226398 | 2024-11-23 00:45:00 | METOP-B | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 282963d5-c318-3a6d-861d-5d1e8df7c801 | -1.1918 | -51.769299 | 2024-11-23 00:45:00 | METOP-B | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 65400267-fe1e-32b5-a4f6-2b0af387d132 | -2.8078 | -45.162701 | 2024-11-23 00:45:00 | METOP-B | PALMEIRÂNDIA | MARANHÃO | Brasil | 2107605 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 70be6c22-5561-3b71-a352-12d65a59433e | -3.2317 | -54.224998 | 2024-11-23 00:45:00 | METOP-B | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 09c8eab1-e9c0-312d-9b1f-55637708d403 | -21.316601 | -55.937302 | 2024-11-23 00:45:00 | METOP-B | NIOAQUE | MATO GROSSO DO SUL | Brasil | 5005806 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| 6d188ebf-63f2-35ff-a623-8ac66b4ebdee | -3.6765 | -51.7309 | 2024-11-23 00:45:00 | METOP-B | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1bb92cc1-4552-3ac9-8d81-994251240716 | -2.7777 | -54.0396 | 2024-11-23 00:45:00 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| db2f7e8c-0728-30cb-8131-a3adf950fa63 | -3.2275 | -53.932598 | 2024-11-23 00:45:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d5d2773d-0781-33da-bdcc-3f0b80c0d759 | -2.4542 | -53.702801 | 2024-11-23 00:45:00 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| fa435feb-2b30-399a-9ce0-25d3fffa5c48 | -2.5918 | -54.037998 | 2024-11-23 00:45:00 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| af76801a-8bde-390e-9d7d-f12deceac2d3 | -3.7125 | -50.538399 | 2024-11-23 00:45:00 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 07a0da40-a34d-3948-98aa-c4f22a49face | -4.1531 | -50.080799 | 2024-11-23 00:45:00 | METOP-B | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d65a10f4-9cc9-30b9-aaaf-ac48c64f2e1a | -1.2469 | -46.757 | 2024-11-23 00:45:00 | METOP-B | BRAGANÇA | PARÁ | Brasil | 1501709 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8318f824-7f96-3525-aaee-ffd3792b66f2 | -2.8225 | -45.1385 | 2024-11-23 00:45:00 | METOP-B | PALMEIRÂNDIA | MARANHÃO | Brasil | 2107605 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| e8346db9-3d85-30b7-be84-a4187d7085f0 | -2.9884 | -52.511501 | 2024-11-23 00:45:00 | METOP-B | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f4891491-200e-3368-953d-da4f7d4e2d01 | -3.0577 | -53.272202 | 2024-11-23 00:45:00 | METOP-B | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b76df573-735b-3849-bb80-c1f8f181e21f | -3.5401 | -50.5056 | 2024-11-23 00:45:00 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| fe4d680c-7877-3096-83bd-20b5e05bacbb | -2.6047 | -54.0494 | 2024-11-23 00:45:00 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| eb6010f3-47b0-351f-bdfc-a2b6e3e971e0 | -4.5372 | -45.888 | 2024-11-23 00:45:00 | METOP-B | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| a08b528c-fd93-3f52-860e-f20f955f4213 | -4.1201 | -43.223999 | 2024-11-23 00:45:00 | METOP-B | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 5f1b2b29-abaa-3b4c-8aad-ecfcf4b59605 | -3.2053 | -54.245098 | 2024-11-23 00:45:00 | METOP-B | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ab2382ef-fd4c-34fb-a213-d6dbba69d439 | -4.6984 | -45.832401 | 2024-11-23 00:45:00 | METOP-B | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 689d11cc-70fa-3018-ae28-877b96f75750 | -2.804 | -54.019402 | 2024-11-23 00:45:00 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2a368f01-3b49-3861-bbf3-0dcb45d98f3d | -1.6024 | -53.399399 | 2024-11-23 00:45:00 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 261efce1-d718-3a08-8cf4-b0008684ed3a | -2.8335 | -54.012901 | 2024-11-23 00:45:00 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2ddfaf00-c87e-3ef1-9a8b-5691d9e5b035 | -2.7094 | -46.265701 | 2024-11-23 00:45:00 | METOP-B | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| a9aad638-8eea-3cd1-9142-1d1a7b656315 | -2.7467 | -54.039398 | 2024-11-23 00:45:00 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b5aaf905-20a5-333b-bab1-05ebcc210948 | -4.2562 | -48.7048 | 2024-11-23 00:45:00 | METOP-B | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 656cdc8b-eb27-39f0-b103-bd0558f8cd83 | -3.2135 | -54.236099 | 2024-11-23 00:45:00 | METOP-B | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5b0b4cef-ab99-3744-b4a2-2aeb8b74f6d1 | -1.5285 | -51.618999 | 2024-11-23 00:45:00 | METOP-B | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6a18bc15-39af-3963-9952-9c731814904d | -2.7924 | -54.1507 | 2024-11-23 00:45:00 | METOP-B | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 87a92eeb-d513-3c8b-aba4-ceb10598561a | -1.2364 | -51.784199 | 2024-11-23 00:45:00 | METOP-B | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e1d81bff-32ad-3f73-8fb3-08b9d5f7f882 | -1.2227 | -53.680199 | 2024-11-23 00:45:00 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 61a28418-5c5e-30c6-a03b-14a88579a7f1 | -1.6379 | -52.6003 | 2024-11-23 00:45:00 | METOP-B | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 22377453-7d4a-31ab-a158-733d931053d9 | -3.3005 | -52.569599 | 2024-11-23 00:45:00 | METOP-B | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5f458a19-717d-3be4-96d5-22df6a9474a3 | -2.8009 | -54.005798 | 2024-11-23 00:45:00 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5b0f5cfd-ffa2-3686-bc31-88fd02b1e92f | -3.2747 | -53.821899 | 2024-11-23 00:45:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| bca7afcd-fb72-318a-9d3d-74eac3165073 | -4.4201 | -44.123402 | 2024-11-23 00:45:00 | METOP-B | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 634adfd4-0485-3925-b53f-5e970ae0d236 | -5.1273 | -47.0284 | 2024-11-23 00:45:00 | METOP-B | JOÃO LISBOA | MARANHÃO | Brasil | 2105500 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| f6175b07-9d0f-34a1-b53c-eaac0a728765 | -1.6355 | -52.408001 | 2024-11-23 00:45:00 | METOP-B | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3bdec5cd-a516-3cd8-a679-915371e8ce93 | -3.7371 | -46.060001 | 2024-11-23 00:45:00 | METOP-B | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 4a6e6fd8-a98e-3116-8e94-6aef6fdc1986 | -5.7487 | -46.2719 | 2024-11-23 00:45:00 | METOP-B | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 56508239-aa81-311d-b34d-f61c691a60cf | -1.2942 | -51.721401 | 2024-11-23 00:45:00 | METOP-B | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5967c7b3-ce6c-3304-8528-0d8c7fad10e9 | -3.2363 | -54.245499 | 2024-11-23 00:45:00 | METOP-B | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a2fb8f6d-a233-3071-9e54-687421f97c55 | -1.604 | -53.406399 | 2024-11-23 00:45:00 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7113cb73-6dab-370f-b6df-7c1d7e593694 | -2.5485 | -53.983101 | 2024-11-23 00:45:00 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 09fb4609-555c-39a9-829b-c7532f583185 | -3.7 | -51.788898 | 2024-11-23 00:45:00 | METOP-B | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 405ab178-d19d-3f76-ad3a-cad94a066143 | -5.5689 | -50.946899 | 2024-11-23 00:45:00 | METOP-B | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7016d217-d951-3e1a-baa8-1f44d17dd8d8 | -2.551 | -54.039902 | 2024-11-23 00:45:00 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |


[Clique aqui para ver as próximas entradas](README12.md)
