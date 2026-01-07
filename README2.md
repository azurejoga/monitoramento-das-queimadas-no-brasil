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
| fdde6aa3-a9cb-3f30-b47d-9f2034693812 | -10.68964 | -40.40461 | 2026-01-07 03:44:00 | NOAA-21 | PINDOBAÇU | BAHIA | Brasil | 2924603 | 29 | 33 | nan | nan | nan | Caatinga | 7.0 |
| e49f676a-d013-3d80-8623-5baa2a3f096c | -5.85351 | -43.88448 | 2026-01-07 03:44:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 2832a897-bec8-3dbf-952d-7e92ba6fc58f | -5.84833 | -43.88372 | 2026-01-07 03:44:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| a9df5a60-41f1-30aa-9c9b-d83cb72ecce9 | -7.51068 | -38.32848 | 2026-01-07 03:44:00 | NOAA-21 | IBIARA | PARAÍBA | Brasil | 2506608 | 25 | 33 | nan | nan | nan | Caatinga | 5.8 |
| eca03981-1464-3fd8-8ae5-bc1be617037b | -8.29072 | -36.50212 | 2026-01-07 03:44:00 | NOAA-21 | BELO JARDIM | PERNAMBUCO | Brasil | 2601706 | 26 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 925cd95e-8a85-3f75-98dc-b9b88f77e5b6 | -13.633 | -40.10107 | 2026-01-07 03:44:00 | NOAA-21 | JAGUAQUARA | BAHIA | Brasil | 2917607 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| c33f12e1-886c-3084-b999-7e521fee3c23 | -15.54551 | -39.41304 | 2026-01-07 03:46:00 | NOAA-21 | MASCOTE | BAHIA | Brasil | 2920908 | 29 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| 2fedda06-0edc-3e81-bc08-1f432847d350 | -15.54538 | -39.41369 | 2026-01-07 03:46:00 | NOAA-21 | MASCOTE | BAHIA | Brasil | 2920908 | 29 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| 9a5a6a63-4e26-30e3-b13e-945dd8fc6791 | -15.48857 | -39.09528 | 2026-01-07 03:46:00 | NOAA-21 | CANAVIEIRAS | BAHIA | Brasil | 2906303 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| dad2f60f-e4d5-34f0-9823-532ce1d470e8 | -15.53556 | -39.93811 | 2026-01-07 03:46:00 | NOAA-21 | POTIRAGUÁ | BAHIA | Brasil | 2925402 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 762b3694-ea3b-3478-a81a-2b89e36db9e5 | -15.82898 | -39.33659 | 2026-01-07 03:46:00 | NOAA-21 | MASCOTE | BAHIA | Brasil | 2920908 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 4440e5e1-13ad-3997-910c-56e153332b4d | -23.8701 | -49.74366 | 2026-01-07 03:49:00 | NOAA-21 | WENCESLAU BRAZ | PARANÁ | Brasil | 4128500 | 41 | 33 | nan | nan | nan | Mata Atlântica | 2.7 |
| 7c28fccc-0a8c-3598-8170-25659d0cd8ab | -24.09772 | -50.13577 | 2026-01-07 03:49:00 | NOAA-21 | VENTANIA | PARANÁ | Brasil | 4128534 | 41 | 33 | nan | nan | nan | Mata Atlântica | 2.8 |
| 30fd6e6d-eb57-30c5-9b04-f3950da4200f | -24.0923 | -50.13435 | 2026-01-07 03:49:00 | NOAA-21 | VENTANIA | PARANÁ | Brasil | 4128534 | 41 | 33 | nan | nan | nan | Mata Atlântica | 2.8 |
| b7b13bb3-c68a-35a9-878a-bd42f88fe58d | -20.22438 | -50.79932 | 2026-01-07 03:49:00 | NOAA-21 | SANTANA DA PONTE PENSA | SÃO PAULO | Brasil | 3547205 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| a2ab0a0b-a3b2-3076-9d8b-4edb87b86377 | -23.87092 | -49.74007 | 2026-01-07 03:49:00 | NOAA-21 | WENCESLAU BRAZ | PARANÁ | Brasil | 4128500 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 535ee42b-a75d-3527-b226-5a6dd8d67919 | -24.09868 | -50.13164 | 2026-01-07 03:49:00 | NOAA-21 | VENTANIA | PARANÁ | Brasil | 4128534 | 41 | 33 | nan | nan | nan | Mata Atlântica | 2.8 |
| ffa4bf9b-db93-3b7f-b65e-3e745316def2 | -27.425 | -52.50267 | 2026-01-07 03:51:00 | NOAA-21 | ITATIBA DO SUL | RIO GRANDE DO SUL | Brasil | 4310702 | 43 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| 8aeb769a-ef6f-3c2e-ac91-2fe8cfefe41d | -27.01683 | -51.50824 | 2026-01-07 03:51:00 | NOAA-21 | ÁGUA DOCE | SANTA CATARINA | Brasil | 4200408 | 42 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 42957d55-a988-346b-8c24-78948571bbfc | -1.32079 | -46.4312 | 2026-01-07 04:12:00 | NPP-375D | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| bbe47aeb-a2b0-3f80-9985-3c2d90188285 | -3.53013 | -39.73178 | 2026-01-07 04:12:00 | NPP-375D | ITAPIPOCA | CEARÁ | Brasil | 2306405 | 23 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 6118ca2b-dfb9-3cd1-b314-a2d67e49931c | -1.5647 | -46.17666 | 2026-01-07 04:12:00 | NPP-375D | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 958ccda7-b227-37d6-8c3f-60485bab5832 | -1.71247 | -45.24377 | 2026-01-07 04:12:00 | NPP-375D | BACURI | MARANHÃO | Brasil | 2101301 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e98e2920-3bdf-3c90-a22a-4ca8ee415e4a | -2.91477 | -40.51863 | 2026-01-07 04:12:00 | NPP-375D | JIJOCA DE JERICOACOARA | CEARÁ | Brasil | 2307254 | 23 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 1c9a8649-2ddd-3d6c-8c4f-2f0077c3102e | -3.52957 | -39.73536 | 2026-01-07 04:12:00 | NPP-375D | ITAPIPOCA | CEARÁ | Brasil | 2306405 | 23 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 13f3e15b-d4f0-32be-8e44-c16fc7e6a567 | -1.71642 | -45.24442 | 2026-01-07 04:12:00 | NPP-375D | BACURI | MARANHÃO | Brasil | 2101301 | 21 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 611dc26c-b5aa-3036-8bdf-413f38c44ac1 | -1.31649 | -46.43051 | 2026-01-07 04:12:00 | NPP-375D | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 399f9f5b-c081-31ba-903a-cd0e5e714c05 | -2.87347 | -40.46272 | 2026-01-07 04:12:00 | NPP-375D | JIJOCA DE JERICOACOARA | CEARÁ | Brasil | 2307254 | 23 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 0ed2a687-3f87-30f7-83c4-0e78e024ee0d | -3.42581 | -41.65237 | 2026-01-07 04:12:00 | NPP-375D | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 3.8 |
| c927326a-8170-3ce9-8ea8-4c1eb3912e8c | -3.00422 | -40.34093 | 2026-01-07 04:12:00 | NPP-375D | BELA CRUZ | CEARÁ | Brasil | 2302305 | 23 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 620b0b45-4389-37c5-a9e6-783040dce843 | -3.42526 | -41.65586 | 2026-01-07 04:12:00 | NPP-375D | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 5.2 |
| b1d1d3eb-d44d-3942-af51-1cd940e8ad13 | -3.62629 | -40.05886 | 2026-01-07 04:12:00 | NPP-375D | SOBRAL | CEARÁ | Brasil | 2312908 | 23 | 33 | nan | nan | nan | Caatinga | 1.3 |
| e2231f4a-3110-39dd-9cc8-48f71eaa8eab | -3.00089 | -40.34041 | 2026-01-07 04:12:00 | NPP-375D | BELA CRUZ | CEARÁ | Brasil | 2302305 | 23 | 33 | nan | nan | nan | Caatinga | 0.8 |
| e763b30e-20a4-384d-af11-41843b301e10 | -0.94458 | -47.16566 | 2026-01-07 04:12:00 | NPP-375D | PRIMAVERA | PARÁ | Brasil | 1506104 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7e04a4b8-1eb2-3f7b-a4d5-21dcd1b7c4b5 | -0.94475 | -47.16428 | 2026-01-07 04:12:00 | NPP-375D | PRIMAVERA | PARÁ | Brasil | 1506104 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c389367a-0c71-3616-80d6-d8924a2c80a1 | -1.91363 | -46.95825 | 2026-01-07 04:12:00 | NPP-375D | SANTA LUZIA DO PARÁ | PARÁ | Brasil | 1506559 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| a9a4e6f8-a351-378b-9e31-4b21a3064b1f | -2.69363 | -48.9953 | 2026-01-07 04:12:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 660b7e26-bb16-31b8-ad8c-0dad4d12ed4d | -4.91103 | -43.2916 | 2026-01-07 04:12:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| d3ea9209-f54a-356c-b7bb-3378eb500738 | -2.69447 | -48.99433 | 2026-01-07 04:12:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| ef89c343-cbee-39f7-8eda-9cac71c4fd5f | -5.25002 | -42.8552 | 2026-01-07 04:12:00 | NPP-375D | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 7c13a342-fda8-3a4b-ba94-c1d51c32b724 | -6.84897 | -35.1886 | 2026-01-07 04:12:00 | NPP-375D | ITAPOROROCA | PARAÍBA | Brasil | 2507101 | 25 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| dc1c6f7e-f690-3807-9824-0a3a0b211430 | -2.69039 | -48.98769 | 2026-01-07 04:12:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| be561f08-de37-3fe5-b760-c7886ee0beb0 | -5.97644 | -44.29121 | 2026-01-07 04:12:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 0.3 |
| b6a5efc9-f116-3a2c-bcff-4d0ee194fbf2 | -5.52137 | -40.41758 | 2026-01-07 04:12:00 | NPP-375D | INDEPENDÊNCIA | CEARÁ | Brasil | 2305605 | 23 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 75b0a97e-6b6c-3378-90c0-66ee83b1d4dc | -4.34438 | -45.35312 | 2026-01-07 04:12:00 | NPP-375D | VITORINO FREIRE | MARANHÃO | Brasil | 2113009 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 2ee10259-c311-3942-a27e-187c81b47b00 | -6.34267 | -40.70098 | 2026-01-07 04:12:00 | NPP-375D | PARAMBU | CEARÁ | Brasil | 2310308 | 23 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 2d869381-360c-3b72-be1a-8201b495958a | -2.36735 | -51.74787 | 2026-01-07 04:12:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 833dc57e-de66-319a-b61c-ffa5b13adfd1 | -2.69541 | -48.98852 | 2026-01-07 04:12:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 350c4525-028c-36a5-b65c-9bf79232a96f | -2.3681 | -51.74345 | 2026-01-07 04:12:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d75de8e4-8d8e-3922-89fc-442a428f92ec | -3.91244 | -40.69649 | 2026-01-07 04:12:00 | NPP-375D | CARIRÉ | CEARÁ | Brasil | 2303105 | 23 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 418bec8f-eae7-3fe6-b9d5-17e5d7f53cae | -3.69779 | -43.43575 | 2026-01-07 04:12:00 | NPP-375D | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 6b595bfd-a3f0-3ef6-951e-bdfdf2553c85 | -2.16308 | -51.9946 | 2026-01-07 04:12:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 75166be0-42f0-3e2d-93bf-7720d530319a | -5.19512 | -44.45611 | 2026-01-07 04:12:00 | NPP-375D | PRESIDENTE DUTRA | MARANHÃO | Brasil | 2109106 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 538af7a0-ba57-35f3-b248-0f19021fb7fc | -3.7747 | -40.55774 | 2026-01-07 04:12:00 | NPP-375D | SOBRAL | CEARÁ | Brasil | 2312908 | 23 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 97e8c761-60b1-3218-b1cf-3fb0f91f52d0 | -5.75152 | -45.11163 | 2026-01-07 04:12:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 029ab649-dd23-3cf8-92f1-d0e202627bcc | -3.69717 | -43.43962 | 2026-01-07 04:12:00 | NPP-375D | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 0b0174a4-a2b1-3695-a3a1-85ce9f1d1903 | -2.69962 | -48.9904 | 2026-01-07 04:12:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 296ccc9e-29e6-3393-8d32-b94baa27555a | -2.69461 | -48.98951 | 2026-01-07 04:12:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 26d92b68-93d3-3d76-b5fb-a686613541b9 | -2.16386 | -51.98988 | 2026-01-07 04:12:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| b566c8ea-7612-3a85-a659-394bfea79da9 | -7.21118 | -35.59515 | 2026-01-07 04:12:00 | NPP-375D | INGÁ | PARAÍBA | Brasil | 2506806 | 25 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 5764b53a-e508-3ff5-96f4-50d6f5ffcde6 | -5.97289 | -44.29059 | 2026-01-07 04:12:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 8335d244-8178-311a-a10f-f8c703fd3662 | -5.90785 | -43.84748 | 2026-01-07 04:12:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 1fd5161e-e66a-3b19-a800-1e8f25e721a3 | -5.51802 | -40.41706 | 2026-01-07 04:12:00 | NPP-375D | INDEPENDÊNCIA | CEARÁ | Brasil | 2305605 | 23 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 6870c896-7db7-305c-bbcc-b1fd338c864f | -5.81781 | -44.13706 | 2026-01-07 04:12:00 | NPP-375D | JATOBÁ | MARANHÃO | Brasil | 2105450 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 926863d1-e93b-31d3-a4d0-f56c17bc576c | -6.34036 | -41.91781 | 2026-01-07 04:12:00 | NPP-375D | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| e685cb96-38af-3f94-9a7b-0b516807123b | -2.90038 | -49.3852 | 2026-01-07 04:12:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d283d923-ec19-3b16-92e2-3d525dfc0368 | -5.82135 | -44.13762 | 2026-01-07 04:12:00 | NPP-375D | JATOBÁ | MARANHÃO | Brasil | 2105450 | 21 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 9677f49e-eeb3-3c03-b980-a533909ff1e7 | -5.85153 | -43.88563 | 2026-01-07 04:12:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ce569b3e-ae6a-3f7d-9b5b-49b16a0277e0 | -5.82552 | -44.13426 | 2026-01-07 04:12:00 | NPP-375D | JATOBÁ | MARANHÃO | Brasil | 2105450 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 9b7c56d2-eee2-360b-9d4a-ab6961d30c1f | -2.9009 | -49.38208 | 2026-01-07 04:12:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| fdb5e07d-b0d6-3cf2-903d-c6003032c58c | -3.70129 | -43.43631 | 2026-01-07 04:12:00 | NPP-375D | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 6.0 |
| fb9f5808-3320-30ff-9edd-207797a4a907 | -4.74126 | -38.72515 | 2026-01-07 04:12:00 | NPP-375D | IBARETAMA | CEARÁ | Brasil | 2305266 | 23 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 8a156feb-848e-3346-9f62-b92843c879c7 | -2.44329 | -49.02823 | 2026-01-07 04:12:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4345ce8c-bb0a-3c46-a038-e283a9ff6132 | -6.84447 | -35.18798 | 2026-01-07 04:12:00 | NPP-375D | ITAPOROROCA | PARAÍBA | Brasil | 2507101 | 25 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| a02d5f6b-dc8a-3f2b-b569-bf2820e803ed | -4.34054 | -45.35248 | 2026-01-07 04:12:00 | NPP-375D | VITORINO FREIRE | MARANHÃO | Brasil | 2113009 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 9aee466f-5f74-3a00-9e16-796418598cbd | -2.69949 | -48.99524 | 2026-01-07 04:12:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 16fbec6d-635e-354e-b564-99511e64bfc2 | -6.97207 | -34.94262 | 2026-01-07 04:12:00 | NPP-375D | SANTA RITA | PARAÍBA | Brasil | 2513703 | 25 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| cf001471-f0bb-3ce8-87ec-99bbf39083e6 | -2.70042 | -48.98946 | 2026-01-07 04:12:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| de603bac-7dfd-3f44-8ad0-328aa64b9531 | -4.43447 | -41.43801 | 2026-01-07 04:12:00 | NPP-375D | PEDRO II | PIAUÍ | Brasil | 2207900 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 063624eb-b325-30f0-aaf2-1d78445d33ed | -10.68538 | -40.40636 | 2026-01-07 04:14:00 | NPP-375D | PINDOBAÇU | BAHIA | Brasil | 2924603 | 29 | 33 | nan | nan | nan | Caatinga | 12.6 |
| e1ceac00-a6f2-3fba-9ac5-a8dafdeaa0ce | -9.66267 | -36.01972 | 2026-01-07 04:14:00 | NPP-375D | MARECHAL DEODORO | ALAGOAS | Brasil | 2704708 | 27 | 33 | nan | nan | nan | Mata Atlântica | 2.6 |
| 051309ef-a260-3361-8209-60c37e41d177 | -11.01983 | -37.4618 | 2026-01-07 04:14:00 | NPP-375D | SALGADO | SERGIPE | Brasil | 2806206 | 28 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 1aa54a2d-d6f7-3b10-99d6-5454c49333f8 | -8.19053 | -39.34156 | 2026-01-07 04:14:00 | NPP-375D | TERRA NOVA | PERNAMBUCO | Brasil | 2615201 | 26 | 33 | nan | nan | nan | Caatinga | 1.0 |
| ffedba26-00d8-36fd-bc64-b5f0487ac6f0 | -10.84832 | -40.35734 | 2026-01-07 04:14:00 | NPP-375D | SAÚDE | BAHIA | Brasil | 2929800 | 29 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 9267be10-0d9e-3ede-afe6-d3accd0ec8e3 | -11.01572 | -37.46128 | 2026-01-07 04:14:00 | NPP-375D | SALGADO | SERGIPE | Brasil | 2806206 | 28 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 0ca3a795-7fcf-398d-a766-7c721a1ff611 | -10.69349 | -40.40706 | 2026-01-07 04:14:00 | NPP-375D | PINDOBAÇU | BAHIA | Brasil | 2924603 | 29 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 1fb06231-b673-37c8-a270-ee4d9ee5d0ea | -7.56713 | -45.62711 | 2026-01-07 04:14:00 | NPP-375D | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 55e1b9ee-253b-345c-a48a-2c550ac612b3 | -7.56786 | -45.62265 | 2026-01-07 04:14:00 | NPP-375D | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 4d20730d-a68e-3ac4-9acc-56ba94370243 | -10.37024 | -39.06579 | 2026-01-07 04:14:00 | NPP-375D | CANUDOS | BAHIA | Brasil | 2906824 | 29 | 33 | nan | nan | nan | Caatinga | 1.6 |
| d54023ca-5717-3c76-9077-b68c01d2f44f | -10.68597 | -40.40984 | 2026-01-07 04:14:00 | NPP-375D | PINDOBAÇU | BAHIA | Brasil | 2924603 | 29 | 33 | nan | nan | nan | Caatinga | 29.5 |
| 95322bfd-63ae-3abd-9673-f50614b0618d | -10.69407 | -40.40317 | 2026-01-07 04:14:00 | NPP-375D | PINDOBAÇU | BAHIA | Brasil | 2924603 | 29 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 8b533748-a71b-3b79-be84-a1bd884a4c01 | -10.68652 | -40.40615 | 2026-01-07 04:14:00 | NPP-375D | PINDOBAÇU | BAHIA | Brasil | 2924603 | 29 | 33 | nan | nan | nan | Caatinga | 14.0 |
| e708f58f-e89d-3767-9539-7afaa8a61859 | -7.57159 | -45.62327 | 2026-01-07 04:14:00 | NPP-375D | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 21ce991b-5195-3aec-9903-400ead0d0bee | -10.69058 | -40.40278 | 2026-01-07 04:14:00 | NPP-375D | PINDOBAÇU | BAHIA | Brasil | 2924603 | 29 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 354d64a3-e484-3117-b1e5-09060a783a20 | -10.69 | -40.40664 | 2026-01-07 04:14:00 | NPP-375D | PINDOBAÇU | BAHIA | Brasil | 2924603 | 29 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 7df10f85-2ce9-3a12-bc86-09c48ad57b40 | -6.96495 | -46.22058 | 2026-01-07 04:14:00 | NPP-375D | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| c042ee5a-9a57-38cc-a497-cf779071c7aa | -10.68482 | -40.41004 | 2026-01-07 04:14:00 | NPP-375D | PINDOBAÇU | BAHIA | Brasil | 2924603 | 29 | 33 | nan | nan | nan | Caatinga | 20.4 |
| 65b79588-79b1-3f1d-bd41-6a325de843de | -10.68944 | -40.41041 | 2026-01-07 04:14:00 | NPP-375D | PINDOBAÇU | BAHIA | Brasil | 2924603 | 29 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 36d49491-2922-3e46-abd7-6a4a0d5cf888 | -9.74742 | -43.9056 | 2026-01-07 04:14:00 | NPP-375D | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| d5704f65-a80f-3fda-85ac-fde9ccbaf8a8 | -21.25499 | -48.65693 | 2026-01-07 04:16:00 | NPP-375D | FERNANDO PRESTES | SÃO PAULO | Brasil | 3515608 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |


[Clique aqui para ver as próximas entradas](README3.md)
