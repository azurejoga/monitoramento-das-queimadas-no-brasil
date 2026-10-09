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

## Dados Diários - Página 253

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 797b029d-29dc-3af8-a0f5-aae0041b98cb | -5.30754 | -40.80701 | 2026-10-09 15:24:00 | NOAA-21 | CRATEÚS | CEARÁ | Brasil | 2304103 | 23 | 33 | nan | nan | nan | Caatinga | 6.1 |
| d18b2840-1f63-3888-8cec-450ceba3362c | -3.4095 | -58.0013 | 2026-10-09 15:30:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 64.5 |
| 5a18fb7c-bb96-37ab-b8d9-5c139530da1d | -8.0766 | -45.6112 | 2026-10-09 15:30:00 | GOES-19 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 108.1 |
| 5581c972-9981-3b65-809d-59d96dfd3f2c | -1.2175 | -55.6512 | 2026-10-09 15:30:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1040.6 |
| 1d192f02-f618-3ef8-8418-3a0132bd8666 | -3.6998 | -58.8634 | 2026-10-09 15:30:00 | GOES-19 | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 53.0 |
| 621f2af1-248f-3d49-9147-d5d6c0cb3367 | -2.9703 | -57.9136 | 2026-10-09 15:30:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 63.8 |
| 0eb2e15f-404c-33b8-abf8-4f95c42b485e | -3.7346 | -59.4385 | 2026-10-09 15:30:00 | GOES-19 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 65.6 |
| 63d448ce-536a-32b0-9fb1-f445608e1a68 | -2.0403 | -56.3895 | 2026-10-09 15:30:00 | GOES-19 | TERRA SANTA | PARÁ | Brasil | 1507979 | 15 | 33 | nan | nan | nan | Amazônia | 63.4 |
| 4323325e-8088-3468-8ae2-bebef41eb132 | -3.0605 | -58.4145 | 2026-10-09 15:30:00 | GOES-19 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 60.7 |
| 0a518acd-1593-3a28-82df-a88ed9d50f88 | -10.9575 | -45.389 | 2026-10-09 15:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 180.0 |
| 63a6ed76-c97d-32c7-b327-3972bb3528d8 | -12.2316 | -44.7427 | 2026-10-09 15:30:00 | GOES-19 | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 154.3 |
| ff2ec4e5-ce18-3211-b73e-86cbe009b44f | -3.0769 | -59.126 | 2026-10-09 15:30:00 | GOES-19 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 65.6 |
| 0d2ced32-a6a1-3934-8c9a-572874474046 | -3.9729 | -59.3564 | 2026-10-09 15:30:00 | GOES-19 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 74.0 |
| 97d9c3e5-1d3b-38fd-87d3-b3f1252dac14 | -2.9327 | -58.3011 | 2026-10-09 15:30:00 | GOES-19 | SILVES | AMAZONAS | Brasil | 1304005 | 13 | 33 | nan | nan | nan | Amazônia | 72.9 |
| f82a2ebd-6b7b-3e7c-a1fe-2bf74464570d | -1.4569 | -54.7562 | 2026-10-09 15:30:00 | GOES-19 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 89.5 |
| edf8ab6e-cf39-3c65-97d1-c09c7d6b9fbf | -1.1992 | -55.6712 | 2026-10-09 15:30:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 106.5 |
| 5a263680-ed5e-3847-8b4a-da6b9556d9ca | -3.1833 | -60.4032 | 2026-10-09 15:30:00 | GOES-19 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 60.7 |
| f17bbd45-f59f-3410-b3de-48fdc7cca55b | -3.0768 | -59.1452 | 2026-10-09 15:30:00 | GOES-19 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 56.5 |
| e7fbd6a6-ae41-3ff5-90ae-0b63de430fc3 | -1.3277 | -55.4327 | 2026-10-09 15:30:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 55.2 |
| 14c0d60b-b7be-3d93-b72e-f6a1606ce319 | -6.4297 | -60.0682 | 2026-10-09 15:30:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 87.7 |
| 7cfd7b7a-ab03-3916-965e-75ccca7376dc | -3.5709 | -59.0969 | 2026-10-09 15:30:00 | GOES-19 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 50.9 |
| 2f02500e-89cd-3363-95c5-f47422612c5e | -2.348 | -58.0017 | 2026-10-09 15:30:00 | GOES-19 | SÃO SEBASTIÃO DO UATUMÃ | AMAZONAS | Brasil | 1303957 | 13 | 33 | nan | nan | nan | Amazônia | 93.6 |
| 4b2efeed-12c9-374d-a5c3-8770df8ba863 | -2.572 | -56.1842 | 2026-10-09 15:30:00 | GOES-19 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 46.9 |
| 7bf1ea94-24a1-3ddd-b2b0-d6fba5fecf4e | -3.7731 | -58.8425 | 2026-10-09 15:30:00 | GOES-19 | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 65.9 |
| 329fe84a-3efa-347a-add5-fb79f0751d15 | -1.5307 | -54.5159 | 2026-10-09 15:30:00 | GOES-19 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 72.3 |
| 7fa0f42d-9769-3de9-a7b5-370133f60655 | -2.4942 | -58.0768 | 2026-10-09 15:30:00 | GOES-19 | SÃO SEBASTIÃO DO UATUMÃ | AMAZONAS | Brasil | 1303957 | 13 | 33 | nan | nan | nan | Amazônia | 46.6 |
| 260f38dd-c16b-3b0f-b738-53b3a3505714 | -1.1094 | -54.1802 | 2026-10-09 15:30:00 | GOES-19 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 68.8 |
| c2cd8d97-15ad-3cb4-96c2-281420d58891 | -3.5909 | -58.5577 | 2026-10-09 15:30:00 | GOES-19 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 60.7 |
| 2d4ad072-9351-366f-a603-145589f838b5 | -3.9511 | -55.3209 | 2026-10-09 15:30:00 | GOES-19 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 78.8 |
| 03c8dccf-32ec-3817-b3ef-6a8722bfbd1f | -4.0837 | -44.1389 | 2026-10-09 15:30:00 | GOES-19 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 113.2 |
| 0ec4609e-ed4f-38d1-aa73-afe4f803897b | -6.9851 | -47.6858 | 2026-10-09 15:30:00 | GOES-19 | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 121.0 |
| 854a98d5-0331-3fe3-884e-3ec56ea9b4d2 | -17.5151 | -43.6694 | 2026-10-09 15:30:00 | GOES-19 | OLHOS-D'ÁGUA | MINAS GERAIS | Brasil | 3145455 | 31 | 33 | nan | nan | nan | Cerrado | 88.4 |
| 2685a281-5d8d-3ea4-a88c-f63289a5be49 | -1.1094 | -54.1601 | 2026-10-09 15:30:00 | GOES-19 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 66.7 |
| d952a79f-d968-3349-9f60-6d2a1aa2446f | -3.6815 | -58.8639 | 2026-10-09 15:30:00 | GOES-19 | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 51.3 |
| 3fb43b01-6ce0-3a21-80cb-d4373b8c5010 | -1.2082 | -49.2539 | 2026-10-09 15:30:00 | GOES-19 | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | 70.9 |
| 5e457b87-56b5-3a00-8b77-9f2594014231 | -1.4939 | -54.5563 | 2026-10-09 15:30:00 | GOES-19 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 93.1 |
| 78665331-a17e-300f-a715-4dbbafd1223e | -3.4397 | -60.2083 | 2026-10-09 15:30:00 | GOES-19 | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 63.8 |
| 4f397eee-6a2a-3e97-8f5c-7838d5cc662f | -4.722 | -55.6529 | 2026-10-09 15:30:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 54.0 |
| 1daebf32-0699-3fe1-9c8f-6f7d01782317 | -12.1549 | -44.7314 | 2026-10-09 15:30:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 137.6 |
| 69b95452-c2e8-3351-b41f-ce9b06f2ed41 | -3.188 | -58.6241 | 2026-10-09 15:30:00 | GOES-19 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 81.1 |
| 0ed1fbd1-ba7e-3590-b0be-ed1d2d402585 | -3.5893 | -59.0773 | 2026-10-09 15:30:00 | GOES-19 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 62.0 |
| c01afb8d-c33b-3776-80a0-741d3d1c2426 | -2.7613 | -54.0941 | 2026-10-09 15:30:00 | GOES-19 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 88.8 |
| c3458982-d5cc-381b-be4a-0f8b80ed8017 | 2.2246 | -55.8555 | 2026-10-09 15:30:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 53.1 |
| 5894e5c3-80e6-3c74-bfea-de793e5ae82d | -1.4118 | -48.9318 | 2026-10-09 15:30:00 | GOES-19 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 62.8 |
| 810ccc56-6ad9-3b5d-a145-6acb08c73527 | -2.8434 | -57.4696 | 2026-10-09 15:30:00 | GOES-19 | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | 53.3 |
| bc72ae20-ca37-3d74-9515-cf4d83bb8888 | -2.8691 | -54.8718 | 2026-10-09 15:30:00 | GOES-19 | BELTERRA | PARÁ | Brasil | 1501451 | 15 | 33 | nan | nan | nan | Amazônia | 59.7 |
| 4d9ad7ff-204c-309d-9bb0-0eaae12fb556 | -10.7475 | -46.6184 | 2026-10-09 15:30:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 175.9 |
| 50b43979-e63e-3846-b611-de95f90f2707 | -1.7296 | -56.0597 | 2026-10-09 15:30:00 | GOES-19 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 57.2 |
| 0676d177-0e57-3127-90cd-556cd4968996 | -4.1012 | -54.6185 | 2026-10-09 15:30:00 | GOES-19 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 58.8 |
| a76a8329-4081-374a-9fde-b2ea53c1c5c0 | -11.0953 | -44.0037 | 2026-10-09 15:30:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 144.5 |
| b68d5358-8024-3aa3-80da-fa5f97fef07a | -3.0219 | -59.1653 | 2026-10-09 15:30:00 | GOES-19 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 78.4 |
| d136f365-5ed0-350b-a1b8-fa597261d4af | -1.4753 | -54.756 | 2026-10-09 15:30:00 | GOES-19 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 89.7 |
| f6c0aa1e-4860-3a3f-991c-ce3b026638d2 | -3.1697 | -58.6244 | 2026-10-09 15:30:00 | GOES-19 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 135.9 |
| 25e6635e-fa4f-30b0-840d-b2510b072064 | -5.5127 | -43.0512 | 2026-10-09 15:30:00 | GOES-19 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 315.6 |
| 1d55d2db-2292-3827-87b1-1cce7b2b5306 | -2.3849 | -57.885 | 2026-10-09 15:30:00 | GOES-19 | URUCARÁ | AMAZONAS | Brasil | 1304302 | 13 | 33 | nan | nan | nan | Amazônia | 46.8 |
| 8a10e6ad-64af-341a-b31a-439faaecfac7 | -3.022 | -59.1462 | 2026-10-09 15:30:00 | GOES-19 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 65.1 |
| afea5564-de94-3a9b-b2f2-a1ec1fd9e8ef | -2.1361 | -54.4671 | 2026-10-09 15:30:00 | GOES-19 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 58.7 |
| ef63aa36-c8c3-36ba-b4e5-91c55970b203 | -3.1285 | -54.1657 | 2026-10-09 15:30:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 114.6 |
| ff035fcf-99e6-34cb-b2f6-b9f326988054 | -1.383 | -55.1944 | 2026-10-09 15:30:00 | GOES-19 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 64.4 |
| 6ed88f89-f1ff-373d-8dd0-ad31ae4fdf46 | -3.2393 | -54.0222 | 2026-10-09 15:30:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 45.9 |
| 01cdb73c-1d2a-3bf5-9c05-beb1ff17a000 | -2.3848 | -57.9044 | 2026-10-09 15:30:00 | GOES-19 | URUCARÁ | AMAZONAS | Brasil | 1304302 | 13 | 33 | nan | nan | nan | Amazônia | 67.5 |
| dd8e6069-5a8b-31e9-96f0-cd57b4b25eb0 | -10.2488 | -49.6636 | 2026-10-09 15:30:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 60.4 |
| 1d9082c4-ca1a-31a1-9138-055de9455163 | -6.6145 | -59.9464 | 2026-10-09 15:30:00 | GOES-19 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 63.3 |
| d546fe43-33bc-357f-b165-5cdd3444aab8 | -13.1641 | -54.3178 | 2026-10-09 15:30:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 163.7 |
| 9af09ade-9570-3e56-a32d-38f6c50b4024 | -3.1697 | -58.6437 | 2026-10-09 15:30:00 | GOES-19 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 111.6 |
| 00be1c35-fdad-3db0-a531-967c53be606b | -12.2127 | -44.7224 | 2026-10-09 15:30:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 281.4 |
| 73458f81-d5bf-3f31-9773-2a09cba013c8 | -1.4569 | -54.7761 | 2026-10-09 15:30:00 | GOES-19 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 85.9 |
| c4c4184e-14c4-30f7-842d-c5dcb41b9e89 | -2.9173 | -57.2151 | 2026-10-09 15:30:00 | GOES-19 | BARREIRINHA | AMAZONAS | Brasil | 1300508 | 13 | 33 | nan | nan | nan | Amazônia | 64.7 |
| f339d773-fe97-30b0-a5e2-1a808163f0dd | -1.3934 | -48.9321 | 2026-10-09 15:30:00 | GOES-19 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 53.5 |
| 5f0e4e20-3d5e-3514-b788-c6d0ecfc5534 | -2.6231 | -57.7261 | 2026-10-09 15:30:00 | GOES-19 | URUCARÁ | AMAZONAS | Brasil | 1304302 | 13 | 33 | nan | nan | nan | Amazônia | 51.4 |
| f7c9012d-492d-317d-b3e1-0836d090f944 | -2.4806 | -56.0678 | 2026-10-09 15:30:00 | GOES-19 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 101.3 |
| 5ef6fa63-d810-3eea-8661-393544131e2f | -2.4623 | -56.0682 | 2026-10-09 15:30:00 | GOES-19 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 67.7 |
| d43df614-ac28-3f32-b33f-2727576e7242 | -1.254 | -55.7496 | 2026-10-09 15:30:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 93.9 |
| f050fdd2-4d85-3bc2-aa3f-37d372b123cf | -3.1842 | -60.0607 | 2026-10-09 15:30:00 | GOES-19 | IRANDUBA | AMAZONAS | Brasil | 1301852 | 13 | 33 | nan | nan | nan | Amazônia | 64.1 |
| ae0838f3-8e8f-34ac-be64-26ef9e61ec98 | -3.4214 | -60.2277 | 2026-10-09 15:30:00 | GOES-19 | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 62.6 |
| df1bc085-969b-393d-963c-bd9ceaacc72f | -3.1696 | -58.6629 | 2026-10-09 15:30:00 | GOES-19 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 47.8 |
| 86cec1a3-883d-3a32-9ec4-acd308bed436 | -2.8822 | -56.6688 | 2026-10-09 15:30:00 | GOES-19 | PARINTINS | AMAZONAS | Brasil | 1303403 | 13 | 33 | nan | nan | nan | Amazônia | 46.0 |
| d79f42bc-7188-38c8-ad86-abf67f3231a8 | -1.3447 | -56.3979 | 2026-10-09 15:30:00 | GOES-19 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 50.7 |
| 4bd1ecfa-2f13-3c88-a1d3-0b17d1e8ae14 | -2.899 | -57.2155 | 2026-10-09 15:30:00 | GOES-19 | BARREIRINHA | AMAZONAS | Brasil | 1300508 | 13 | 33 | nan | nan | nan | Amazônia | 87.3 |
| 9fa38647-f8a8-39b1-b99f-ef61440ec11d | -3.4062 | -59.1004 | 2026-10-09 15:30:00 | GOES-19 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 52.1 |
| 9eb5ce7c-9a76-3569-aa29-e77095b8a905 | -2.8433 | -57.4891 | 2026-10-09 15:30:00 | GOES-19 | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | 46.8 |
| 862b3edd-fc32-392c-b89d-250f1a4b2a08 | -13.2015 | -54.3757 | 2026-10-09 15:30:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 57.8 |
| b24812ce-e604-3a7c-bc8a-80be4c9d4181 | -2.9704 | -57.8942 | 2026-10-09 15:30:00 | GOES-19 | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | 62.9 |
| 382cd761-17b7-3b7d-9c4d-7bd31c7c7f55 | -2.4623 | -56.0879 | 2026-10-09 15:30:00 | GOES-19 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 51.2 |
| e693f018-6d3e-38b9-85f1-d5a678737088 | -2.3481 | -57.9824 | 2026-10-09 15:30:00 | GOES-19 | SÃO SEBASTIÃO DO UATUMÃ | AMAZONAS | Brasil | 1303957 | 13 | 33 | nan | nan | nan | Amazônia | 89.1 |
| 5460749a-105e-37f1-98ba-af46c258493c | -3.0225 | -58.935 | 2026-10-09 15:30:00 | GOES-19 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 89.1 |
| 8cef88c6-4833-3c86-929d-0ff5ff915be0 | -3.4397 | -60.2273 | 2026-10-09 15:30:00 | GOES-19 | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 66.6 |
| 091245c9-a477-315c-9b56-88c3a1246865 | -3.0403 | -59.1458 | 2026-10-09 15:30:00 | GOES-19 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 52.8 |
| 94a11833-073d-3582-b657-d548bc598e08 | -13.1641 | -54.3178 | 2026-10-09 15:40:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 157.1 |
| a1511f6c-3cf7-380d-9491-a794f4b3a657 | -11.2849 | -45.2063 | 2026-10-09 15:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 145.0 |
| f085efc3-7b6a-3e1f-916c-d0974b108b30 | -1.383 | -55.1944 | 2026-10-09 15:40:00 | GOES-19 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 126.4 |
| 2a40f1bb-de3d-3ecd-8b13-243e465109b0 | -2.8575 | -59.1107 | 2026-10-09 15:40:00 | GOES-19 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 42.4 |
| 78922e72-26f5-346a-9046-b6625ea108cc | -1.4569 | -54.7562 | 2026-10-09 15:40:00 | GOES-19 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 84.3 |
| f3022706-0beb-3728-a932-7ee55dc64c27 | -1.254 | -55.7299 | 2026-10-09 15:40:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 67.2 |
| 967a6d37-f952-314d-913d-b8ad3dce7cd7 | -2.8822 | -56.6688 | 2026-10-09 15:40:00 | GOES-19 | PARINTINS | AMAZONAS | Brasil | 1303403 | 13 | 33 | nan | nan | nan | Amazônia | 45.8 |
| 0637c009-003f-3f6e-b38a-3747e85c229c | -2.4623 | -56.0682 | 2026-10-09 15:40:00 | GOES-19 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 77.2 |
| 85e4797e-9fd1-3c0b-b3d7-0850de7d517f | -2.3849 | -57.885 | 2026-10-09 15:40:00 | GOES-19 | URUCARÁ | AMAZONAS | Brasil | 1304302 | 13 | 33 | nan | nan | nan | Amazônia | 64.4 |
| 102285b7-0ab8-3ebd-a9ff-3b352ebe1dca | -1.3932 | -48.9961 | 2026-10-09 15:40:00 | GOES-19 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 60.7 |
| 27dd4adf-1353-3b3e-aaad-d7d008a91fd2 | -3.188 | -58.6241 | 2026-10-09 15:40:00 | GOES-19 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 78.0 |
| 1eab7f7b-f0ec-3b96-af34-617688dfe6a6 | -3.5709 | -59.0969 | 2026-10-09 15:40:00 | GOES-19 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 54.2 |


[Clique aqui para ver as próximas entradas](README254.md)
