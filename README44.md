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

## Dados Diários - Página 44

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| cb4e8238-601f-3d45-b678-5c702331dfcc | -7.65979 | -46.2543 | 2025-08-23 04:51:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 98cba190-a65a-34b1-a4cd-e88e51096021 | -6.31954 | -43.75837 | 2025-08-23 04:51:00 | NOAA-21 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 49975216-bd28-3c26-bd5e-6778747a612a | -10.22182 | -47.56652 | 2025-08-23 04:51:00 | NOAA-21 | LAGOA DO TOCANTINS | TOCANTINS | Brasil | 1711951 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| c6abcba0-6c7a-3587-b210-ab9c7790bce8 | -7.63171 | -45.23203 | 2025-08-23 04:51:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 83a8b07e-7f8b-3f33-9e9e-1038abcef7cc | -9.19465 | -59.45883 | 2025-08-23 04:51:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.9 |
| decd517a-b3b7-3b2e-bc4c-5125349273db | -6.75065 | -50.96345 | 2025-08-23 04:51:00 | NOAA-21 | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 1da18465-c774-35e9-854e-82b9e97c8420 | -6.1454 | -57.71384 | 2025-08-23 04:51:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 0f33815f-f4c5-3b63-8f38-d5281091297d | -5.10806 | -43.21526 | 2025-08-23 04:51:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 9.8 |
| 5715af8a-4ac2-39ea-8255-b981217b75b7 | -8.52519 | -48.83873 | 2025-08-23 04:51:00 | NOAA-21 | ITAPORÃ DO TOCANTINS | TOCANTINS | Brasil | 1711100 | 17 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 24f7f7a8-7e6b-3f94-b46d-f7dc7f8d17a2 | -8.5973 | -62.6206 | 2025-08-23 04:51:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 3.0 |
| c047378f-1b94-362c-8e9c-3df25d7ce59c | -9.15975 | -59.50763 | 2025-08-23 04:51:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 6.8 |
| e0e559af-a38e-3d44-9a0d-f3599956876d | -9.03198 | -59.01231 | 2025-08-23 04:51:00 | NOAA-21 | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 8dc1fcf0-ff6d-383d-94b6-f351746e56d3 | -10.2747 | -46.74786 | 2025-08-23 04:51:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 491ea2ae-5413-3e27-b548-f5b6355b3bc9 | -6.47456 | -55.87508 | 2025-08-23 04:51:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| bb9a0ac1-2777-3938-b5a8-457cd6e7d082 | -4.34515 | -46.47042 | 2025-08-23 04:51:00 | NOAA-21 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 54.5 |
| d3ebcd96-0e53-3bad-932e-c478447dedd5 | -6.79678 | -44.99509 | 2025-08-23 04:51:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| a124a9c0-0d51-3416-a59e-2802468aaec4 | -6.57896 | -59.88896 | 2025-08-23 04:51:00 | NOAA-21 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 63c96cda-7860-3bf6-a7c1-f7048ad65b15 | -7.51181 | -63.83769 | 2025-08-23 04:51:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 2e26961d-5d11-3bf5-9fe2-77b133075d2e | -10.70781 | -48.20972 | 2025-08-23 04:51:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e167d960-67d1-3c20-ba21-ebf89511af36 | -9.21055 | -59.61007 | 2025-08-23 04:51:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 6ab2639d-ec77-3f9a-91c5-56aa9c3e609b | -5.94532 | -44.13999 | 2025-08-23 04:51:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 2a7712d1-647d-31ee-814d-bc8ec850a251 | -9.44289 | -47.64977 | 2025-08-23 04:51:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 5.6 |
| ff737d09-94a6-3cc6-bae4-2f23d47da349 | -10.74237 | -48.26542 | 2025-08-23 04:51:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 119b10cc-b5fd-34e9-a30b-fc1919f00b2c | -5.80616 | -59.22491 | 2025-08-23 04:51:00 | NOAA-21 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 46b620ef-bdef-30b2-b3e0-48d66a714900 | -6.38431 | -45.52795 | 2025-08-23 04:51:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 4.8 |
| a8beaf81-86d7-3cf6-9f13-e7e7b90d32e7 | -3.98607 | -47.88377 | 2025-08-23 04:51:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 8c52a3db-7a1a-3645-9fb4-135e534368da | -6.0678 | -53.88403 | 2025-08-23 04:51:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 72c381ab-2e75-31e2-bf46-b8af634c51a3 | -9.15693 | -59.60117 | 2025-08-23 04:51:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3eb4fbc1-d965-3f2f-9a98-a18de4f21773 | -3.26894 | -50.02081 | 2025-08-23 04:51:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 93a63fe7-74a7-3d03-80fe-324efc5beef7 | -9.25374 | -59.61778 | 2025-08-23 04:51:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2f63bcb4-587a-3a48-ba68-8b9c7a6a2177 | -10.62578 | -50.15848 | 2025-08-23 04:51:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 580a1433-cf91-3ebf-8d30-974a848fa524 | -6.7882 | -44.32746 | 2025-08-23 04:51:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 96db1be2-1fbc-35ef-a97c-59946d4d18ff | -7.65198 | -46.27672 | 2025-08-23 04:51:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 44f61ebc-43ea-30b0-8c3e-b2f305bb4e15 | -10.27918 | -46.74915 | 2025-08-23 04:51:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 0497f9e3-2021-3a40-b4b5-e12b017bcaf1 | -6.42938 | -41.22377 | 2025-08-23 04:51:00 | NOAA-21 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 505835a2-6871-3d90-9b36-ef4f9a8255a9 | -8.66297 | -51.27491 | 2025-08-23 04:51:00 | NOAA-21 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 92a5bef8-d627-3cd9-b80e-531e99b5b770 | -6.63055 | -58.40909 | 2025-08-23 04:51:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 1a332276-ae40-3158-a02b-06979efd9eb2 | -9.25302 | -59.62194 | 2025-08-23 04:51:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 73749ce2-41c9-3d5b-ae64-518c0edff1e8 | -6.2342 | -47.3139 | 2025-08-23 04:51:00 | NOAA-21 | CAMPESTRE DO MARANHÃO | MARANHÃO | Brasil | 2102556 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 03817e60-01a3-3f6c-a44c-68d848875382 | -9.05976 | -49.53672 | 2025-08-23 04:51:00 | NOAA-21 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 2566a124-00bc-3eaa-8e1f-95738e857bd8 | -6.37194 | -45.56408 | 2025-08-23 04:51:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 4.9 |
| eae32c16-5362-3e01-a527-368ad10c3aa3 | -7.02632 | -44.64464 | 2025-08-23 04:51:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 12.0 |
| 0edad6bd-1f09-3539-87b5-83bd4c369b85 | -8.61642 | -62.60649 | 2025-08-23 04:51:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.6 |
| cbfda8d7-cc30-3666-b6b2-bf438f1430a3 | -7.60645 | -44.37141 | 2025-08-23 04:51:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 597b6ee7-8022-3f7e-a6e0-149c771f6762 | -7.62402 | -63.48357 | 2025-08-23 04:51:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 486cbe1c-73ec-3303-bc87-c1df4503dbc4 | -9.16558 | -59.60266 | 2025-08-23 04:51:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.3 |
| e4200e25-6720-3265-ae08-9a2f2acbe02a | -9.18944 | -59.61948 | 2025-08-23 04:51:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 8.2 |
| 147b1d88-d78f-3992-b781-c4076837fd17 | -10.63505 | -50.14635 | 2025-08-23 04:51:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e41bfa7e-e6be-384a-9708-f4db06587193 | -7.03888 | -44.66372 | 2025-08-23 04:51:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| bec48049-7d2a-3e0b-94f2-b53744a7b7a7 | -6.27901 | -52.82548 | 2025-08-23 04:51:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 728dc9d1-f584-3979-bf69-2c2e664fd8da | -5.75533 | -57.59381 | 2025-08-23 04:51:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| fa17d549-4f1c-3ddc-8ee1-4db95b8c1fe5 | -6.31143 | -59.88552 | 2025-08-23 04:51:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 15eb4d32-a38e-367a-992a-87f2ea2e9f8d | -6.57517 | -59.88342 | 2025-08-23 04:51:00 | NOAA-21 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 16a8976f-9d10-3ac0-8cdf-6e11fd73fb42 | -6.60807 | -44.56321 | 2025-08-23 04:51:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 13.8 |
| d93fd93f-9677-3dc3-99d7-906b1d844cc4 | -10.7518 | -48.24308 | 2025-08-23 04:51:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| e20d64d4-82b0-384e-ab75-02ac5c0ce0d4 | -2.8526 | -54.89608 | 2025-08-23 04:51:00 | NOAA-21 | BELTERRA | PARÁ | Brasil | 1501451 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 7832512a-bb30-3871-a5e1-1c0d6cfced25 | -8.61703 | -62.60312 | 2025-08-23 04:51:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 3.6 |
| ef5c95e9-86d4-3b3a-9214-83ded8eae4df | -9.53126 | -48.12873 | 2025-08-23 04:51:00 | NOAA-21 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 3f9c0bd2-d019-3841-94ca-1dc66a8ba4c7 | -8.59792 | -62.61718 | 2025-08-23 04:51:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 3.0 |
| a90f019a-5c96-3cdc-ae57-0f1ce0ccb6f4 | -9.45082 | -47.65498 | 2025-08-23 04:51:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 0b94314c-0a25-39e8-82d6-fa9770681d09 | -6.11901 | -44.40643 | 2025-08-23 04:51:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 2aa392e6-6ce4-3346-91f6-16ac228cd46a | -6.38092 | -45.53508 | 2025-08-23 04:51:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 18.3 |
| 1cf168fe-0a26-3d39-bbd1-3a10e9271294 | -5.73989 | -57.58783 | 2025-08-23 04:51:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 24052db4-c45b-3767-898c-b34ee4113168 | -9.60201 | -55.35276 | 2025-08-23 04:51:00 | NOAA-21 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c9732369-bbf1-336c-9e3a-cdf48d9cbd4b | -7.63585 | -45.2382 | 2025-08-23 04:51:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 43ecbfa9-51ae-3621-a63e-17c54343ad78 | -5.79429 | -59.21392 | 2025-08-23 04:51:00 | NOAA-21 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f1c8712c-06bb-3564-b956-942a65a569cb | -7.54356 | -45.03857 | 2025-08-23 04:51:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 12881b08-8bc3-3cae-b1ac-db70c7e20907 | -7.23134 | -56.84614 | 2025-08-23 04:51:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 5cc1a7fe-b0f5-3150-84dd-a008c5ffc661 | -4.87247 | -48.90944 | 2025-08-23 04:51:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 51bfe185-afdf-3173-b023-503d3d7c4992 | -9.1728 | -59.61251 | 2025-08-23 04:51:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| d4fe1512-493c-3527-97a1-ddb25f0858d3 | -6.05832 | -53.87891 | 2025-08-23 04:51:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 57feaa21-90f7-3e52-9248-a6967fb1429c | -6.5806 | -59.87942 | 2025-08-23 04:51:00 | NOAA-21 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 7.7 |
| 673b2dd8-0979-3557-9306-9bacb80a3a01 | -9.17571 | -59.62158 | 2025-08-23 04:51:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 4dcb553a-8af3-3837-97b1-da9972a43264 | -9.19546 | -59.59464 | 2025-08-23 04:51:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e457f6b9-2309-31a1-a9bf-57ed9609d141 | -5.75016 | -57.60013 | 2025-08-23 04:51:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 397b0ef2-2837-388b-b605-161302b5b3cc | -6.79441 | -44.99644 | 2025-08-23 04:51:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 8.7 |
| a7732e0b-1b65-34de-9a33-0d45a73f5122 | -5.74907 | -57.5821 | 2025-08-23 04:51:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b073e771-bf2d-383c-a584-41f38291bfe0 | -5.89215 | -53.63928 | 2025-08-23 04:51:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ea0d24a8-0ca7-30ac-94ba-279f6415f1b7 | -5.44167 | -60.17466 | 2025-08-23 04:51:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 5c2aea02-f79a-30a4-b847-3ccee989446b | -6.78047 | -44.98888 | 2025-08-23 04:51:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| c9d4fac6-c447-33ab-ad05-83a10eec1a9c | -7.04753 | -51.41235 | 2025-08-23 04:51:00 | NOAA-21 | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 23e5a470-dcb1-34cb-b5ff-41dbd6ed658e | -10.62641 | -50.15407 | 2025-08-23 04:51:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 510a1bb9-f56a-36dc-b5e3-8bd49a723c79 | -4.3415 | -46.46563 | 2025-08-23 04:51:00 | NOAA-21 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 66f768d8-6470-3250-a5d7-83af2eaa7760 | -8.85301 | -52.05379 | 2025-08-23 04:51:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 95899059-0f6b-37df-8b66-71bf69eede9a | -4.07262 | -49.45639 | 2025-08-23 04:51:00 | NOAA-21 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 7512f5b6-21b2-3d1b-aa17-cc9b0851114f | -7.07497 | -44.06789 | 2025-08-23 04:51:00 | NOAA-21 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 60f7dc02-621f-3e14-b5e8-13ae42f93f48 | -7.80739 | -63.56294 | 2025-08-23 04:51:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 26abe881-e806-3faf-94d5-3f416f94000f | -10.74704 | -48.26227 | 2025-08-23 04:51:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 05ab37a1-213b-3363-8059-417c76941405 | -8.61581 | -62.60986 | 2025-08-23 04:51:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 6900e2de-6a5a-3839-87d8-00fc24841dbf | -5.95045 | -44.1407 | 2025-08-23 04:51:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| ea328533-0cb4-3d14-8b9e-7804c30e4267 | -7.43724 | -60.62411 | 2025-08-23 04:51:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 0614fb50-9879-3880-91fc-7d7d96f8c076 | -9.15621 | -59.60533 | 2025-08-23 04:51:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 4c505ea5-6010-3a87-94c6-b111f585635d | -7.02128 | -44.64399 | 2025-08-23 04:51:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 52c3cb37-ad82-3131-a5c3-bb43545f3215 | -6.0611 | -53.88298 | 2025-08-23 04:51:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 0a52f0e1-731d-3c67-8da5-7e05d829ed30 | -5.03007 | -56.12543 | 2025-08-23 04:51:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4a926ca6-2db3-3429-b70e-b4768ecee691 | -7.90511 | -61.51252 | 2025-08-23 04:51:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 13ffb86b-d050-3046-8d1e-5cefe9eb1016 | -5.1108 | -43.21523 | 2025-08-23 04:51:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 9.3 |
| 8705531a-bb05-3081-9f7f-5bb7b22ea645 | -5.90509 | -43.46614 | 2025-08-23 04:51:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 0d3f9354-fac3-3349-b594-1304bf138b16 | -5.75875 | -57.59798 | 2025-08-23 04:51:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| d3c20f1a-52e9-3e00-b3a9-44e5cf82a67f | -5.8784 | -57.75561 | 2025-08-23 04:51:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |


[Clique aqui para ver as próximas entradas](README45.md)
