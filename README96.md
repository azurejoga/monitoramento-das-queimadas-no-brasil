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

## Dados Diários - Página 96

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| f5474d36-6c12-3fda-bcb7-4a9742179300 | -9.2366 | -67.885 | 2026-10-06 17:50:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 118.2 |
| 454d08a2-de90-3898-9635-1206acf0aa02 | -11.6374 | -43.664 | 2026-10-06 17:50:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 100.7 |
| 5ae5115b-714e-35a6-a15e-81e3b9986065 | -9.4621 | -67.0817 | 2026-10-06 17:50:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 154.9 |
| f3977762-fa7e-3c56-955a-adf7950b4534 | -11.4507 | -43.3854 | 2026-10-06 17:50:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 134.3 |
| 1ea138d1-321e-3fde-b8f4-3fec28710e48 | -11.21 | -46.2655 | 2026-10-06 17:50:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 112.8 |
| bdb1d47b-3bff-3f26-ac95-3793e1473293 | -9.4819 | -66.7836 | 2026-10-06 17:50:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 100.3 |
| 9f680d49-bae2-3e8a-a02c-6a297edb55f2 | -6.7066 | -45.5765 | 2026-10-06 17:50:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 147.4 |
| af54f273-dc57-3dcc-b0f2-2ac2293d260a | -9.5469 | -64.8008 | 2026-10-06 17:50:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 105.8 |
| f768e5ec-e759-30cc-83a6-31158430f73d | -8.5367 | -67.032 | 2026-10-06 17:50:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 98.8 |
| 74498331-db8c-3961-b190-b75ccde2386a | -9.0045 | -65.7174 | 2026-10-06 17:50:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 94.8 |
| 356389fa-7b16-39e3-807c-098bfb806c07 | -9.8619 | -64.9958 | 2026-10-06 17:50:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 102.7 |
| dc6d1b42-4b53-31b3-822f-d7fc8ae70767 | -3.292 | -42.2673 | 2026-10-06 17:50:00 | GOES-19 | MAGALHÃES DE ALMEIDA | MARANHÃO | Brasil | 2106300 | 21 | 33 | nan | nan | nan | Cerrado | 179.1 |
| 1671c086-44cc-36fe-908b-cbfd55adaf0b | -9.8844 | -64.2802 | 2026-10-06 17:50:00 | GOES-19 | BURITIS | RONDÔNIA | Brasil | 1100452 | 11 | 33 | nan | nan | nan | Amazônia | 120.0 |
| f65833bb-d867-37e9-a41e-1f5fda5385d8 | -7.8982 | -71.6555 | 2026-10-06 17:50:00 | GOES-19 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 75.2 |
| 4bbe3e8a-888f-3976-b180-5f5e875f544e | -8.845 | -68.7989 | 2026-10-06 17:50:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 92.8 |
| 02ede127-20a1-3bb8-a7bc-0c02f976c1af | -9.7318 | -64.9818 | 2026-10-06 17:50:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 125.6 |
| 2ca8df71-1cdb-369d-b4ab-a0366f64bb14 | -9.1441 | -67.8502 | 2026-10-06 17:50:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 86.5 |
| 4240ef05-0982-395a-90c7-432bdbe1a8f2 | -9.0231 | -65.7169 | 2026-10-06 17:50:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 93.9 |
| 9e075184-7d07-3ce1-8acc-5cc20e9d9f1d | -9.1253 | -67.9432 | 2026-10-06 18:00:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 95.3 |
| 06cd2f2c-6282-389c-996a-13a6bc061b6e | -3.292 | -42.2673 | 2026-10-06 18:00:00 | GOES-19 | MAGALHÃES DE ALMEIDA | MARANHÃO | Brasil | 2106300 | 21 | 33 | nan | nan | nan | Cerrado | 221.1 |
| c7533a88-ef71-3f4f-99a9-c2b7f8f06481 | -11.47 | -43.3824 | 2026-10-06 18:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 99.8 |
| 9e21e326-dbed-379b-9b0f-2bf6a452ecb5 | -11.8296 | -44.688 | 2026-10-06 18:00:00 | GOES-19 | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 658.7 |
| eae3badf-caeb-337f-85e9-35f975d2b9e4 | -9.5006 | -66.7459 | 2026-10-06 18:00:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 95.5 |
| 497d2026-16be-3bca-9e84-6aaed9321a8f | -7.5332 | -70.0331 | 2026-10-06 18:00:00 | GOES-19 | ENVIRA | AMAZONAS | Brasil | 1301506 | 13 | 33 | nan | nan | nan | Amazônia | 92.0 |
| 9c5afe64-cf5c-390d-884b-1e3724724a22 | -9.1645 | -67.3495 | 2026-10-06 18:00:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 162.5 |
| 7bedf9a0-884b-306a-9771-5984324a2b61 | 1.8767 | -55.7424 | 2026-10-06 18:00:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 60.3 |
| 4d31d331-416e-3f5f-9a5d-8324c3e97521 | -9.1829 | -67.3861 | 2026-10-06 18:00:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 89.8 |
| 4ed95ce7-d212-3447-b25f-1c658e8902a5 | -11.8311 | -43.5628 | 2026-10-06 18:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 100.1 |
| 848eeda6-cbb7-3557-ac52-5f3dd0199e5c | -9.1332 | -65.9559 | 2026-10-06 18:00:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 92.9 |
| e0309ad2-9681-3f33-819e-5659a7900ba5 | -9.5151 | -67.7484 | 2026-10-06 18:00:00 | GOES-19 | PORTO ACRE | ACRE | Brasil | 1200807 | 12 | 33 | nan | nan | nan | Amazônia | 210.4 |
| 042c190a-b561-3c94-8ae3-ae63c4e8248e | -9.2199 | -67.3852 | 2026-10-06 18:00:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 86.8 |
| 1bb7d92b-2be0-375c-8c69-86f2c478a1c2 | -8.845 | -68.7989 | 2026-10-06 18:00:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 85.9 |
| 5d6d7c60-fdc9-30a0-933c-f4d3c2cec051 | -9.4819 | -66.7836 | 2026-10-06 18:00:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 104.2 |
| 7dbd34d1-bcf5-3006-aa72-4d94b3d4b311 | 3.5263 | -51.2778 | 2026-10-06 18:00:00 | GOES-19 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 60.2 |
| 85727bae-ffcf-3261-8c79-9ec53b0cb6d9 | -8.5367 | -67.032 | 2026-10-06 18:00:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 95.7 |
| c59c0620-3d18-3ccd-bf70-d32fd9065cd6 | -11.7143 | -43.652 | 2026-10-06 18:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 99.3 |
| e27c9161-043a-3676-9f1f-fc5d32ed523d | -11.6575 | -43.6136 | 2026-10-06 18:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 102.4 |
| 3b0daacf-17d4-3fb6-94c0-01d40c77df45 | -9.4621 | -67.0817 | 2026-10-06 18:00:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 151.9 |
| 6752a999-c2a0-32bf-8e72-afb7a0618141 | 1.7304 | -55.6259 | 2026-10-06 18:00:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 70.4 |
| 37da276f-3f26-3524-bb58-0c657f703311 | -9.1256 | -67.8507 | 2026-10-06 18:00:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 102.8 |
| 703a5931-07b4-35a8-8716-2323988f532b | -9.5468 | -64.8196 | 2026-10-06 18:00:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 248.5 |
| 1d7bbfac-5222-3896-ad6b-804e32fd1af1 | -8.9964 | -67.7613 | 2026-10-06 18:00:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 80.7 |
| f4446899-8ad2-38d3-82a0-3fd3623442a2 | -11.6378 | -43.6403 | 2026-10-06 18:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 117.0 |
| cf3a52fe-e4b3-374e-b0c4-38fcf36131de | -6.0078 | -42.2808 | 2026-10-06 18:00:00 | GOES-19 | ELESBÃO VELOSO | PIAUÍ | Brasil | 2203503 | 22 | 33 | nan | nan | nan | Caatinga | 106.6 |
| 86b02733-e988-3209-b368-7c6384627d15 | -7.7127 | -73.0611 | 2026-10-06 18:00:00 | GOES-19 | RODRIGUES ALVES | ACRE | Brasil | 1200427 | 12 | 33 | nan | nan | nan | Amazônia | 62.8 |
| 0207c4fb-f846-376a-aafa-8e1e8a8dfbde | -9.8844 | -64.2802 | 2026-10-06 18:00:00 | GOES-19 | BURITIS | RONDÔNIA | Brasil | 1100452 | 11 | 33 | nan | nan | nan | Amazônia | 124.9 |
| 90cb9cc1-8a7c-33c1-bf2c-9e4753db7772 | -5.7321 | -41.6349 | 2026-10-06 18:00:00 | GOES-19 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 234.7 |
| 8e230084-9505-38d5-985c-e78a9c1bd411 | -10.1793 | -69.0104 | 2026-10-06 18:00:00 | GOES-19 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 87.1 |
| 7b65d12b-6356-3ccd-923d-65a81157abc2 | -11.4507 | -43.3854 | 2026-10-06 18:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 127.4 |
| f675c0e4-fc08-354e-9334-4b4a75ddb104 | -4.5706 | -46.5907 | 2026-10-06 18:00:00 | GOES-19 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 49.0 |
| dc9ea791-7d8b-34c5-875f-61337411d854 | -5.7509 | -41.6333 | 2026-10-06 18:00:00 | GOES-19 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 157.8 |
| f02c0737-85aa-3f1e-a294-3c8abff135dd | -9.1829 | -67.3676 | 2026-10-06 18:00:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 89.8 |
| 0615f520-2595-3776-8259-7d281f263bd3 | -9.96 | -43.481 | 2026-10-06 18:00:00 | GOES-19 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 195.0 |
| 6b36b900-7d7e-3391-9ce1-e673de267731 | -15.6055 | -41.6797 | 2026-10-06 18:00:00 | GOES-19 | ÁGUAS VERMELHAS | MINAS GERAIS | Brasil | 3101003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 173.2 |
| 9b9c482c-fd86-3d08-8deb-7b390a7805b5 | -8.7788 | -66.5804 | 2026-10-06 18:00:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 122.5 |
| 44d3bbef-65bb-30a8-863c-9bec5fe89c1d | 1.4922 | -55.688 | 2026-10-06 18:00:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 44.2 |
| 7eb3d9f0-1d5f-3dc8-8133-c81e2311b563 | -11.2267 | -45.2604 | 2026-10-06 18:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 252.0 |
| 0e317cda-2398-3d47-9dee-c52489b3f88c | -2.989 | -43.1259 | 2026-10-06 18:00:00 | GOES-19 | BARREIRINHAS | MARANHÃO | Brasil | 2101707 | 21 | 33 | nan | nan | nan | Cerrado | 88.2 |
| c9bbab3a-39c2-3cc6-be71-09b18fe458fd | -9.9444 | -67.1982 | 2026-10-06 18:00:00 | GOES-19 | SENADOR GUIOMARD | ACRE | Brasil | 1200450 | 12 | 33 | nan | nan | nan | Amazônia | 120.6 |
| af79c9ce-17c5-3cdb-ac94-3fe8701832f6 | -9.1072 | -67.8326 | 2026-10-06 18:00:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 107.1 |
| ee0ee700-6855-3216-9991-202d14aa217a | -9.0045 | -65.7174 | 2026-10-06 18:00:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 103.6 |
| a9c0ece0-e5e1-38ff-b4cf-4aa9397bfa6a | 3.5079 | -51.2784 | 2026-10-06 18:00:00 | GOES-19 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 58.4 |
| 040945e2-7d59-3a7b-8b32-1cc5f5a4479d | -9.1259 | -67.7766 | 2026-10-06 18:00:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 82.0 |
| e1e738fd-2cc7-3f0f-8bbf-6ebfb48e41dc | -9.8634 | -44.8195 | 2026-10-06 18:00:00 | GOES-19 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 128.5 |
| f9e20e2d-dd67-319e-aa86-ef3f25dd992f | -10.6254 | -69.241 | 2026-10-06 18:00:00 | GOES-19 | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 73.0 |
| d375364d-0a21-3bce-8d8f-d71c5eea9c41 | -9.0892 | -67.685 | 2026-10-06 18:00:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 257.3 |
| b3294558-e4c5-3aa1-bf98-05dbeae1e705 | -8.9875 | -65.4006 | 2026-10-06 18:00:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 98.3 |
| b54b573a-2e5c-3fd0-a3bf-0517d7b53824 | -9.8824 | -44.8171 | 2026-10-06 18:00:00 | GOES-19 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 322.0 |
| 97bdb9c6-8dec-30b1-bd8d-539520f97c15 | -9.5469 | -64.8008 | 2026-10-06 18:00:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 142.3 |
| 28562f74-a27d-35dd-9b80-b1f65fae19cf | -11.8315 | -43.5391 | 2026-10-06 18:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 189.3 |
| 53d0379f-e214-3547-a320-607edd1a3be8 | -3.3921 | -44.4923 | 2026-10-06 18:00:00 | GOES-19 | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Amazônia | 136.8 |
| 35b9dfcc-c749-361e-95d4-92ee164bde83 | -9.2366 | -67.885 | 2026-10-06 18:00:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 124.6 |
| 6f7298a7-8754-3157-976f-3e142b919b1d | -9.5467 | -64.8384 | 2026-10-06 18:00:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 95.6 |
| 92efa605-ba7e-3005-a1fb-eb4327d8e0a5 | -9.462 | -67.1002 | 2026-10-06 18:00:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 94.3 |
| 64105eaa-8b19-33ca-a68b-474a2738df24 | -9.7881 | -44.7828 | 2026-10-06 18:00:00 | GOES-19 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 90.1 |
| 1857e577-7dfd-3a76-8fc8-d94cf6799efd | -9.1055 | -68.3135 | 2026-10-06 18:00:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 95.4 |
| 596f1380-8e40-3c70-8142-43ee203ea786 | -4.2967 | -42.9915 | 2026-10-06 18:00:00 | GOES-19 | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 142.0 |
| ff454ade-72e3-3821-a86c-a3aecdb194af | -11.6382 | -43.6166 | 2026-10-06 18:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 157.1 |
| f01ff275-23f8-39a2-8978-4423741dcb4a | -9.0889 | -67.759 | 2026-10-06 18:00:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 88.2 |
| 8527a4d1-340f-3410-8303-aaa2663b6a8f | -8.7324 | -69.4271 | 2026-10-06 18:00:00 | GOES-19 | MANOEL URBANO | ACRE | Brasil | 1200344 | 12 | 33 | nan | nan | nan | Amazônia | 82.7 |
| 004cb9e3-3d32-38bc-8ba1-0dbfc7b12358 | -9.1895 | -65.7863 | 2026-10-06 18:00:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 92.7 |
| e0dbab56-b3f0-39f7-8964-59f9094b1e1b | -6.0266 | -42.2792 | 2026-10-06 18:00:00 | GOES-19 | ELESBÃO VELOSO | PIAUÍ | Brasil | 2203503 | 22 | 33 | nan | nan | nan | Caatinga | 139.9 |
| 448345fa-82a3-358b-b3fe-21f0bfdf412c | -9.2365 | -67.9035 | 2026-10-06 18:00:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 110.9 |
| 5f14d3c8-210f-3443-9356-caa7bfa6e32f | -10.8516 | -68.5676 | 2026-10-06 18:00:00 | GOES-19 | EPITACIOLÂNDIA | ACRE | Brasil | 1200252 | 12 | 33 | nan | nan | nan | Amazônia | 96.2 |
| 5fddba77-94d4-34f5-9956-48bf1566a554 | -7.5332 | -70.0148 | 2026-10-06 18:00:00 | GOES-19 | ENVIRA | AMAZONAS | Brasil | 1301506 | 13 | 33 | nan | nan | nan | Amazônia | 82.7 |
| 6328d9d2-6e98-37f4-b4aa-a8e5b38290d6 | -6.5985 | -41.5582 | 2026-10-06 18:00:00 | GOES-19 | INHUMA | PIAUÍ | Brasil | 2204709 | 22 | 33 | nan | nan | nan | Caatinga | 93.7 |
| 46861e47-e563-34c9-b260-f9bf8a0c7be8 | -11.6374 | -43.664 | 2026-10-06 18:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 119.4 |
| d86168c8-bb5d-39e2-8963-a0c8525ea8d8 | -9.1068 | -67.9437 | 2026-10-06 18:00:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 89.7 |
| 98a103f0-1776-37b5-9684-f3ac9151dba1 | -11.6951 | -43.655 | 2026-10-06 18:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 128.3 |
| dabdc04a-7e08-3061-9c56-91d3ea5eec92 | -2.5353 | -65.8819 | 2026-10-06 18:00:00 | GOES-19 | FONTE BOA | AMAZONAS | Brasil | 1301605 | 13 | 33 | nan | nan | nan | Amazônia | 88.8 |
| 6a165c30-9e92-391a-90dd-fd099a7a1075 | -8.9191 | -68.7789 | 2026-10-06 18:10:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 98.4 |
| f76a382d-7f69-3b62-a23d-40d820ab58ea | -9.2365 | -67.9035 | 2026-10-06 18:10:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 118.9 |
| 172c72cc-5617-32e4-99ed-8fc46c329b66 | -3.3607 | -43.3893 | 2026-10-06 18:10:00 | GOES-19 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 261.6 |
| 1f4f2f0d-3514-32b8-abf2-5c3e92579f45 | -5.7321 | -41.6349 | 2026-10-06 18:10:00 | GOES-19 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 229.9 |
| 6a96e7ea-889c-3fe3-8d0d-30643a5c3290 | -10.9758 | -45.4324 | 2026-10-06 18:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 120.5 |
| 6dc8cf90-0438-31ba-b54d-92c04fb1ce51 | -9.1332 | -65.9559 | 2026-10-06 18:10:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 90.9 |
| d05d6fab-cb0e-3493-a5d8-3c7d5baf0feb | -11.6378 | -43.6403 | 2026-10-06 18:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 105.5 |
| 443aa603-4971-33a9-90ed-67616f8b0367 | -11.6382 | -43.6166 | 2026-10-06 18:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 129.1 |
| 2f99de90-6f9e-3bbd-a8a6-a906057b15ed | -9.8634 | -44.8195 | 2026-10-06 18:10:00 | GOES-19 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 83.0 |
| 7ab15753-3a6d-3931-a54f-511e690c7c48 | -9.2367 | -67.8665 | 2026-10-06 18:10:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 90.3 |


[Clique aqui para ver as próximas entradas](README97.md)
