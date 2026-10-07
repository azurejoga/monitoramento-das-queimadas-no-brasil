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

## Dados Diários - Página 246

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| cd7d9ff8-5012-30e5-9c8b-829eca6677eb | -11.2333 | -44.8678 | 2026-10-07 18:10:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 111.4 |
| 648ef053-4d3e-3356-996e-45ef608d84fc | -11.3749 | -46.6722 | 2026-10-07 18:10:00 | GOES-19 | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 77.2 |
| e23bcbc9-0b54-3085-a452-43f47fae9c69 | -9.8431 | -65.0341 | 2026-10-07 18:10:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 74.4 |
| 87a2317e-6dbd-3a26-b715-7ea4a19df205 | -8.575 | -66.6973 | 2026-10-07 18:10:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 66.7 |
| 9e8ce112-1848-32cc-9441-0fb687c44cdd | -3.6381 | -55.5084 | 2026-10-07 18:10:00 | GOES-19 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 60.1 |
| 976dd39d-f303-3e11-b9be-444c446aa67b | -3.6197 | -55.5089 | 2026-10-07 18:10:00 | GOES-19 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 57.9 |
| 597e1191-a06c-3e2b-8d29-bdf0d5cdaafd | -8.0852 | -70.0619 | 2026-10-07 18:10:00 | GOES-19 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 125.7 |
| 49f7085a-0ce8-3279-b973-28e5e2c30afb | 1.9134 | -55.7024 | 2026-10-07 18:10:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 69.7 |
| 535f0c51-55e5-327c-81e5-96894d47df2c | -3.2717 | -50.4102 | 2026-10-07 18:10:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 59.7 |
| 6e73a0ab-0ec8-3176-a0ae-26d168638e67 | -5.5148 | -42.8164 | 2026-10-07 18:10:00 | GOES-19 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Caatinga | 87.1 |
| 5b882130-70fa-35fe-9b05-1c380c41729f | -3.3637 | -50.4701 | 2026-10-07 18:10:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 103.6 |
| 95930c98-82a7-3aa9-ad51-92ff002712ed | -5.8114 | -45.2612 | 2026-10-07 18:10:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 79.7 |
| 2e153ce1-70e3-3d2a-b450-e8fa2e0fcb59 | -4.2744 | -46.3846 | 2026-10-07 18:10:00 | GOES-19 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 444.6 |
| 03969dae-023f-3868-82cd-98b818f555ad | 2.44 | -50.8303 | 2026-10-07 18:10:00 | GOES-19 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 74.0 |
| e7762053-1c4b-3a00-a778-215247a090e8 | -6.5794 | -41.5841 | 2026-10-07 18:10:00 | GOES-19 | INHUMA | PIAUÍ | Brasil | 2204709 | 22 | 33 | nan | nan | nan | Caatinga | 96.6 |
| 70bda78e-55cb-3ed4-a01d-35660ba03f7b | -3.5061 | -51.6924 | 2026-10-07 18:10:00 | GOES-19 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 60.6 |
| 7c644c04-0749-3d48-a6fd-72918a66169e | -2.8712 | -54.192 | 2026-10-07 18:10:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 54.4 |
| 466e016f-bbed-35a6-9f23-dd95fb494a7a | -11.619 | -43.6196 | 2026-10-07 18:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 92.1 |
| b25511b5-66d0-34f1-8e6c-9294ec3537ae | -9.7312 | -65.0944 | 2026-10-07 18:10:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 65.9 |
| 8aaef458-3c3e-31d2-8a97-51bf08a31f12 | -5.7312 | -41.7309 | 2026-10-07 18:10:00 | GOES-19 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 138.1 |
| cb7fdd67-da0e-3bb7-a41b-1b0eb30f190b | -8.6511 | -44.8919 | 2026-10-07 18:10:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 53.5 |
| 893eda4a-98a8-3f7c-b9d0-f0c831fc95ce | 1.8768 | -55.7227 | 2026-10-07 18:10:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 85.2 |
| e360a50b-46f7-37fb-92b9-51de54b698d0 | -9.5313 | -46.8513 | 2026-10-07 18:10:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 73.4 |
| fc807000-3cbd-3054-906e-39b0bc38b327 | -6.1502 | -39.4158 | 2026-10-07 18:10:00 | GOES-19 | ACOPIARA | CEARÁ | Brasil | 2300309 | 23 | 33 | nan | nan | nan | Caatinga | 149.2 |
| efb63cb2-7a94-3ee3-92b2-d9e5e0199bbe | -3.8788 | -44.1035 | 2026-10-07 18:10:00 | GOES-19 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 108.2 |
| 5e118ee4-e01a-3d8b-a2fd-b496b0493d5a | -11.8503 | -43.5598 | 2026-10-07 18:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 166.0 |
| c6d88fef-da61-3d97-98d0-047cdb6bee2d | -9.6757 | -65.0401 | 2026-10-07 18:10:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 76.5 |
| d49fb92c-88d6-36d0-a381-0029f7896c68 | 1.8951 | -55.7027 | 2026-10-07 18:10:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 67.8 |
| a85282ba-629d-36db-9fd6-4e2b861011d6 | -10.4594 | -46.8333 | 2026-10-07 18:10:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 112.4 |
| 9e880cf2-a402-342c-abd1-41a03e51051f | -2.9819 | -54.0488 | 2026-10-07 18:10:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 306.1 |
| 5522fbb7-cd3f-3c33-970b-4fa1543f5dae | -3.8786 | -44.1265 | 2026-10-07 18:10:00 | GOES-19 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 102.6 |
| 1ef03ee1-268a-381a-8dc1-01b1b0751cf8 | -3.2398 | -53.8813 | 2026-10-07 18:10:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 71.2 |
| 90c7cc44-ec7d-377e-aa01-c4956d4195c4 | -2.9084 | -54.0304 | 2026-10-07 18:10:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 59.5 |
| 3d74b102-cb84-3d11-b0f5-98bd67728ae6 | -6.0632 | -53.4891 | 2026-10-07 18:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 51.4 |
| eb7b5742-24e0-36ee-a633-4d45894125b9 | -11.3745 | -46.6948 | 2026-10-07 18:10:00 | GOES-19 | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 82.3 |
| 3d73622d-0a7d-38a2-b3e7-99c010b3c271 | -9.9596 | -43.5045 | 2026-10-07 18:10:00 | GOES-19 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 109.2 |
| 229324b6-0951-321a-b07d-b99ae0b6fc9a | -6.9925 | -45.1223 | 2026-10-07 18:10:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 84.2 |
| be1b2bae-bdf5-38d9-8e05-6031b764614f | -9.96 | -43.481 | 2026-10-07 18:10:00 | GOES-19 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 133.9 |
| b589dff7-96eb-3735-b502-3a3e2b46b730 | -7.9178 | -70.9245 | 2026-10-07 18:10:00 | GOES-19 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 125.6 |
| cb025c77-7bff-3369-8df9-7034ae91e612 | -5.7659 | -42.0389 | 2026-10-07 18:10:00 | GOES-19 | SANTA CRUZ DOS MILAGRES | PIAUÍ | Brasil | 2209153 | 22 | 33 | nan | nan | nan | Caatinga | 278.0 |
| 2a83961c-cb1f-347e-8caf-980b2d5a6215 | 1.7487 | -55.6059 | 2026-10-07 18:10:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 67.3 |
| 7981148b-e8b9-3d14-bc22-17500c2f48c9 | 2.4585 | -50.8299 | 2026-10-07 18:10:00 | GOES-19 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 54.5 |
| bd1b8ee9-c59e-3281-bdb9-019b61b2ffe0 | -5.9887 | -53.5538 | 2026-10-07 18:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 61.6 |
| 7e67093b-4038-30b0-bf53-60f6157e472a | -6.6223 | -53.031 | 2026-10-07 18:10:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 63.6 |
| fd6fc183-7a3f-32d3-9615-7663db9a7f56 | -8.0852 | -70.0802 | 2026-10-07 18:10:00 | GOES-19 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 91.7 |
| 4a2a5e2d-4270-344c-a307-946bd5b4bc1d | -13.3865 | -43.8708 | 2026-10-07 18:10:00 | GOES-19 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 128.7 |
| d1d394ef-2437-31b2-b0fc-815892c5e61e | -10.3735 | -46.2372 | 2026-10-07 18:10:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 119.5 |
| 8a1a5ddf-ce35-3431-ba08-cb6a28808cba | -7.3744 | -46.2385 | 2026-10-07 18:10:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 91.9 |
| adb7d813-328a-372c-afdc-806b493fcf2d | -5.9649 | -40.914 | 2026-10-07 18:10:00 | GOES-19 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 188.8 |
| 1158f1ec-13f2-398b-92ae-6564a539f033 | -5.2274 | -48.4113 | 2026-10-07 18:10:00 | GOES-19 | SÃO SEBASTIÃO DO TOCANTINS | TOCANTINS | Brasil | 1720309 | 17 | 33 | nan | nan | nan | Amazônia | 74.7 |
| c5dcda3e-8d94-3f87-9bca-ca100b25e067 | -11.8508 | -43.5361 | 2026-10-07 18:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 106.6 |
| f2cbb249-8250-32d0-8269-63bb001b549a | -8.0837 | -70.831 | 2026-10-07 18:10:00 | GOES-19 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 95.6 |
| ac73b3ac-53ba-3d18-9197-2393f66737e9 | -7.6802 | -70.0677 | 2026-10-07 18:10:00 | GOES-19 | ENVIRA | AMAZONAS | Brasil | 1301506 | 13 | 33 | nan | nan | nan | Amazônia | 110.5 |
| 3bfb6a77-1b23-3681-8a9a-3308b4fe5d66 | -9.4621 | -67.0817 | 2026-10-07 18:10:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 69.3 |
| e38844f3-d400-3828-a1f9-b21430ace4a8 | -4.1407 | -54.0152 | 2026-10-07 18:10:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 66.0 |
| 936211dd-c617-386d-a8dd-2225936e2f38 | -2.7612 | -54.1142 | 2026-10-07 18:10:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 941.5 |
| 023159b1-50da-3c68-b69a-5716df86eb80 | -3.5875 | -54.3138 | 2026-10-07 18:10:00 | GOES-19 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 90.0 |
| d8a08fb3-33c3-3af1-bc6c-d9bd8c263fe2 | 1.8767 | -55.7424 | 2026-10-07 18:10:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 77.7 |
| ce7878fd-01f6-3388-8d4e-69b038684122 | -3.1102 | -54.146 | 2026-10-07 18:10:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 125.8 |
| 2b63b1d3-8d8f-32d1-aa19-bf83ec711327 | -3.019 | -53.9272 | 2026-10-07 18:10:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 219.5 |
| 0af574ab-ec0f-327a-9ae3-dd8f96cb8461 | -3.6612 | -54.2715 | 2026-10-07 18:10:00 | GOES-19 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 66.4 |
| bf038a12-3785-3716-a6be-83ef7d55eb24 | -3.05 | -53.93 | 2026-10-07 18:15:00 | MSG-03 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 531b2179-2e39-3863-a143-49798d3a5f97 | -12.19 | -44.83 | 2026-10-07 18:15:00 | MSG-03 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 97edfdc1-7113-3656-a3a4-ec49ea0ad562 | -2.79 | -54.03 | 2026-10-07 18:15:00 | MSG-03 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 52a473c9-0683-36e5-8a32-6efb6c3a6836 | -5.7 | -45.13 | 2026-10-07 18:15:00 | MSG-03 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| b7cbb967-3a5c-33c5-be1b-283f491834ea | -8.98 | -45.91 | 2026-10-07 18:15:00 | MSG-03 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 1eee12ba-beb0-3d8a-877c-0a4ae1c420ad | -3.26 | -54.07 | 2026-10-07 18:15:00 | MSG-03 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c3f4c000-a68b-38d4-ab4c-09432de57565 | -3.29 | -54.01 | 2026-10-07 18:15:00 | MSG-03 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5d3269fc-4899-3509-902d-5a0e1fee2569 | -9.95 | -43.56 | 2026-10-07 18:15:00 | MSG-03 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| e3d65c29-5f85-3821-8dbc-34b5c2863991 | -3.02 | -53.99 | 2026-10-07 18:15:00 | MSG-03 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| cd3d816d-db41-3863-9b57-3ea06af08339 | -3.0 | -54.04 | 2026-10-07 18:15:00 | MSG-03 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c47cd6ef-ddd7-3a75-92cf-3dd80c8592e8 | -4.27 | -46.39 | 2026-10-07 18:15:00 | MSG-03 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 3ab4c537-e69a-3428-aba3-cc7bbcae8775 | -9.98 | -43.52 | 2026-10-07 18:15:00 | MSG-03 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| d2b91778-5558-3c2e-a194-c0b4dc6c55e0 | -9.95 | -43.6 | 2026-10-07 18:15:00 | MSG-03 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| c535ff32-7d71-3f89-9585-7db1e1377148 | -2.79 | -54.09 | 2026-10-07 18:15:00 | MSG-03 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 621a4d86-7bbe-3b50-b02d-acfe93b153fa | -6.22 | -52.82 | 2026-10-07 18:15:00 | MSG-03 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| cbb221a5-7478-3f1e-b2ec-46eea70e09d1 | -5.73 | -45.14 | 2026-10-07 18:15:00 | MSG-03 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 92e1a5e5-177f-3046-a48a-2a1857f9a15b | -9.11 | -45.09 | 2026-10-07 18:15:00 | MSG-03 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| f4e11ebf-d07b-3e9c-90e4-47f7329fe797 | -3.29 | -54.07 | 2026-10-07 18:15:00 | MSG-03 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c6fb3f69-d530-39e5-9e19-75069e439c37 | -6.86 | -48.69 | 2026-10-07 18:15:00 | MSG-03 | ARAGOMINAS | TOCANTINS | Brasil | 1701309 | 17 | 33 | nan | nan | nan | Amazônia | nan |
| 6b167a09-a4dd-3fc8-94fe-730a862a5822 | -7.46 | -42.84 | 2026-10-07 18:15:00 | MSG-03 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 8f4ae6c7-66d9-3472-9b0a-ba39c0928c35 | -3.02 | -53.92 | 2026-10-07 18:15:00 | MSG-03 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 66551402-10d6-3027-84eb-882a17b8792b | -12.19 | -44.78 | 2026-10-07 18:15:00 | MSG-03 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 94334c8b-56a6-3f96-8fd2-1a94476ecbdc | -2.76 | -54.15 | 2026-10-07 18:15:00 | MSG-03 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 14040af0-256d-3ae2-bb1f-84eacda8f2c6 | -3.26 | -54.01 | 2026-10-07 18:15:00 | MSG-03 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 64a23cf5-1a69-3632-943b-a4fbf21c0722 | -5.73 | -45.18 | 2026-10-07 18:15:00 | MSG-03 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 865ea09c-2402-3e2c-9c6b-6b64f24d3bef | -7.86 | -54.98 | 2026-10-07 18:15:00 | MSG-03 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 89609e41-579c-37cb-a85a-87e3c7a967e6 | -7.49 | -42.85 | 2026-10-07 18:15:00 | MSG-03 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 6348f421-5a3c-3e3c-8bb8-27cbf20dfcf3 | -2.76 | -54.08 | 2026-10-07 18:15:00 | MSG-03 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 88f35f99-97c8-37b3-b9bc-ccb04d6a0844 | -5.7 | -45.18 | 2026-10-07 18:15:00 | MSG-03 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 4e98d926-ae6e-3bce-bbb9-6f2e5bb20995 | -6.22 | -52.88 | 2026-10-07 18:15:00 | MSG-03 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| cb8f790c-05f9-34dd-8c6d-5b6c75f65c79 | -11.63 | -43.67 | 2026-10-07 18:15:00 | MSG-03 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| ce1b9110-1402-3c6a-92d2-7d0e9aab59f4 | -11.6 | -43.61 | 2026-10-07 18:15:00 | MSG-03 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 9a92c3dc-d068-3da0-9f93-b853c7f8e998 | -6.1502 | -39.4158 | 2026-10-07 18:20:00 | GOES-19 | ACOPIARA | CEARÁ | Brasil | 2300309 | 23 | 33 | nan | nan | nan | Caatinga | 146.9 |
| 09137346-cc6e-36f8-af39-e05cbf3f00ef | -9.9596 | -43.5045 | 2026-10-07 18:20:00 | GOES-19 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 119.3 |
| 4b6284c5-4225-32cd-a696-ce8394e6d285 | -7.1825 | -52.6283 | 2026-10-07 18:20:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 141.0 |
| 0679f637-ece2-3a45-86c3-12b843f02a0e | -10.3731 | -45.0306 | 2026-10-07 18:20:00 | GOES-19 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 105.2 |
| 0ac3e748-50bb-3452-8fa9-c8ce32e26a53 | -7.6802 | -70.0677 | 2026-10-07 18:20:00 | GOES-19 | ENVIRA | AMAZONAS | Brasil | 1301506 | 13 | 33 | nan | nan | nan | Amazônia | 126.5 |
| ed41fdf7-2ebe-313b-ba5f-323a6ea0f7a2 | 1.7121 | -55.6261 | 2026-10-07 18:20:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 81.3 |
| c6498bfa-a36f-366e-b524-430ba50f8e07 | -7.1964 | -42.0275 | 2026-10-07 18:20:00 | GOES-19 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 41.0 |


[Clique aqui para ver as próximas entradas](README247.md)
