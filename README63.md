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

## Dados Diários - Página 63

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 6faaf5af-bc78-369b-9adf-99ce332f94e8 | -7.88186 | -44.18106 | 2026-10-05 12:02:00 | TERRA_M-T | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 26.2 |
| ba7fc072-320a-3dc1-8190-75a1228ca355 | -10.4909 | -46.03412 | 2026-10-05 12:02:00 | TERRA_M-T | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 19.7 |
| 27c0cc6e-6913-3207-bd6f-afdd8e884230 | -8.67574 | -54.5597 | 2026-10-05 12:02:00 | TERRA_M-T | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 19.8 |
| b6ff36bc-4fef-3f27-a483-a120ad36bfc3 | -7.82718 | -45.31221 | 2026-10-05 12:02:00 | TERRA_M-T | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 21.3 |
| 0b7c0f5e-6f90-306f-96b7-dfbb0feb0b0e | -7.82709 | -45.29747 | 2026-10-05 12:02:00 | TERRA_M-T | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 15.3 |
| a2105d13-9cf7-3b7c-9e51-c012127e9baf | -8.31534 | -45.47269 | 2026-10-05 12:02:00 | TERRA_M-T | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 20.3 |
| a56d3edf-3904-311a-942b-2d34a7784ef9 | -11.35216 | -46.67989 | 2026-10-05 12:02:00 | TERRA_M-T | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 29.2 |
| edaad6a9-d5f4-3a87-b3f8-a058f4f4c674 | -7.88468 | -44.18691 | 2026-10-05 12:02:00 | TERRA_M-T | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 36.9 |
| 972fbdb3-f05f-30ff-a748-75385da57bc4 | -11.6763 | -43.6343 | 2026-10-05 12:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 111.5 |
| dfc4bf26-a21f-3a2f-92bd-f7c38d87d1de | -11.6763 | -43.6343 | 2026-10-05 12:20:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 75.1 |
| 0f4216e1-e871-36b5-a139-372579e56778 | -9.8631 | -44.8425 | 2026-10-05 12:30:00 | GOES-19 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 93.0 |
| b56b7e0b-d60f-3af4-b560-500efb4c974a | -7.8867 | -44.1902 | 2026-10-05 12:30:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 79.9 |
| e5a885a4-1947-3a07-ab7d-e816571fb66f | -9.8634 | -44.8195 | 2026-10-05 12:30:00 | GOES-19 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 83.8 |
| e77d3ae6-5a84-3182-8efe-8b3515232345 | -11.6763 | -43.6343 | 2026-10-05 12:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 78.1 |
| 6e91aeef-d4de-361c-ab89-9f21578cb123 | -11.6763 | -43.6343 | 2026-10-05 12:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 80.8 |
| 8766cc83-a56e-3ba6-a831-b0afc5f6ed74 | -7.8867 | -44.1902 | 2026-10-05 12:40:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 80.3 |
| d56333d6-9431-3a04-98af-567e345616bc | -7.8356 | -45.3175 | 2026-10-05 12:50:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 88.7 |
| cf9b818c-2387-3054-9db7-ec444012686b | -11.2817 | -44.2804 | 2026-10-05 12:50:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 103.9 |
| 4f4c557d-6d01-3769-94f9-cab25bcaa6ab | -11.2813 | -44.3038 | 2026-10-05 12:50:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 68.1 |
| a13dbf2a-76a4-3e0f-b991-26922868b617 | -11.6763 | -43.6343 | 2026-10-05 12:50:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 84.0 |
| ef9c13db-1454-381a-840e-42e85d376e79 | -12.2054 | -42.1115 | 2026-10-05 12:50:00 | GOES-19 | BROTAS DE MACAÚBAS | BAHIA | Brasil | 2904506 | 29 | 33 | nan | nan | nan | Caatinga | 86.8 |
| 8294cc88-f9b6-3b70-96b5-ef7c89baccfc | -11.3009 | -44.2776 | 2026-10-05 12:50:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 83.4 |
| bc62b7f9-9db3-3c24-9938-ded6abfca804 | -11.6758 | -43.658 | 2026-10-05 13:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 73.2 |
| a2440997-133e-30d6-8fb7-bf19fce25536 | -10.9758 | -45.4324 | 2026-10-05 13:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 85.1 |
| a747ea79-7c5a-3c03-89ee-7d5d1df89a90 | -7.8867 | -44.1902 | 2026-10-05 13:00:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 75.0 |
| 2891f413-467e-32f0-b83e-1ab8f22459cd | -10.9567 | -45.4349 | 2026-10-05 13:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 166.7 |
| 01b9a16c-b859-3d4d-ad75-e4a43e04df34 | -9.1259 | -67.7581 | 2026-10-05 13:00:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 53.2 |
| 9a4def12-205a-3c86-a29c-b3ac6dbac135 | -11.3009 | -44.2776 | 2026-10-05 13:00:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 84.1 |
| 92803aea-73c3-353a-98f5-022db62b0cd7 | -10.9571 | -45.412 | 2026-10-05 13:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 99.7 |
| 8311f713-bdea-3e0e-b5a5-0764e561e494 | -10.9762 | -45.4094 | 2026-10-05 13:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 61.0 |
| 0c63f584-2ae8-3e80-a911-a259ea7662d5 | -7.8356 | -45.3175 | 2026-10-05 13:00:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 80.6 |
| 9a91aeca-d2db-35e1-996c-8d388d95102c | -7.4889 | -42.8059 | 2026-10-05 13:00:00 | GOES-19 | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 100.7 |
| 09bf09d7-bc46-3197-b4ff-9bc3220193c7 | -11.2817 | -44.2804 | 2026-10-05 13:00:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 97.1 |
| 302e1398-5240-391e-a12a-bc7f80fe7d90 | -11.6763 | -43.6343 | 2026-10-05 13:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 85.3 |
| 9582a3b5-30c9-3bcf-ba25-3584f63db9fd | -9.1037 | -64.385 | 2026-10-05 13:10:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 55.3 |
| 3dc123ee-5e1f-3c59-b95c-8276b1cb6127 | -10.9567 | -45.4349 | 2026-10-05 13:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 146.6 |
| eae63183-54da-3d80-8b49-576268344284 | -10.9571 | -45.412 | 2026-10-05 13:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 96.2 |
| 2dde0fe1-4951-3ca2-a96d-9d217059b0e1 | -11.6758 | -43.658 | 2026-10-05 13:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 88.8 |
| 2675f384-95aa-3258-a415-1e6656b05007 | -9.1038 | -64.3662 | 2026-10-05 13:10:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 62.7 |
| 9edf6600-c4a8-3a2c-8141-219af23f05ad | -11.2817 | -44.2804 | 2026-10-05 13:10:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 74.2 |
| b776dd13-8841-3b13-bb71-a692584740f9 | -10.9762 | -45.4094 | 2026-10-05 13:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 72.2 |
| 3ae6ee08-ad6f-3c70-a20e-41bbf0a5d852 | -11.6763 | -43.6343 | 2026-10-05 13:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 109.1 |
| ee546f9a-978c-3efb-8218-5c6099dcb8cf | -9.8634 | -44.8195 | 2026-10-05 13:10:00 | GOES-19 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 97.7 |
| 13f22c5a-58f4-3cfd-a629-8355c39d5abf | -7.8356 | -45.3175 | 2026-10-05 13:10:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 78.9 |
| 0c7a7cd6-e0f2-3b06-b42e-9edbb94646dc | -10.9758 | -45.4324 | 2026-10-05 13:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 121.9 |
| f08da642-9cbd-362f-84e3-deaa68e395da | -9.8257 | -44.8011 | 2026-10-05 13:10:00 | GOES-19 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 77.3 |
| 1d246b15-b4b6-36f0-87b9-5cfb4b7c193c | -9.8447 | -44.7988 | 2026-10-05 13:10:00 | GOES-19 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 73.4 |
| f5ca60ec-1b84-305e-9266-705f209a7be7 | -7.8867 | -44.1902 | 2026-10-05 13:10:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 74.4 |
| bd4e18e7-eb1b-3d85-8434-97a14cf836ae | -11.6387 | -43.5929 | 2026-10-05 13:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 76.6 |
| f9d7f0e0-fc55-379b-beda-d5b3f25e23d7 | -7.4889 | -42.8059 | 2026-10-05 13:10:00 | GOES-19 | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 71.5 |
| d705cda2-4964-37c0-928a-61b39a42ba2f | -9.8631 | -44.8425 | 2026-10-05 13:10:00 | GOES-19 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 66.7 |
| 0a9485e9-ce3a-3754-8dc3-0889d0fda7fe | -9.1259 | -67.7581 | 2026-10-05 13:10:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 110.4 |
| fa0f6372-8b6c-357a-8459-926707aed2a9 | -9.8824 | -44.8171 | 2026-10-05 13:10:00 | GOES-19 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 71.5 |
| f7f2efd0-bf3f-31e8-9875-56ac43b0cba1 | -10.9571 | -45.412 | 2026-10-05 13:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 124.1 |
| 05174408-4eb7-3fa6-ad8c-f5f4acf02725 | -9.8634 | -44.8195 | 2026-10-05 13:20:00 | GOES-19 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 68.5 |
| 21a8a543-204f-3953-b6d3-293ed639b156 | -9.8447 | -44.7988 | 2026-10-05 13:20:00 | GOES-19 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 72.8 |
| b7bf08f8-bb99-3a87-a4ea-d057fcb58370 | -11.32 | -44.2748 | 2026-10-05 13:20:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 81.0 |
| 5fcab95f-bb82-3c31-9cb9-6adcde0e4746 | -8.7526 | -64.1909 | 2026-10-05 13:20:00 | GOES-19 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 54.1 |
| 4db548ab-c2a3-3a99-a537-b5d9dfc691fe | -7.1778 | -42.0055 | 2026-10-05 13:20:00 | GOES-19 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 101.0 |
| 4fc956d8-dcc3-3ffa-adfc-9e2f8cf32b85 | -7.8358 | -45.2948 | 2026-10-05 13:20:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 94.2 |
| 3414ac73-60f6-3053-b2e8-d6bdaf2f9534 | -7.8867 | -44.1902 | 2026-10-05 13:20:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 74.4 |
| 8e6628b9-47f7-3e50-9c82-80137b41f81f | -11.2817 | -44.2804 | 2026-10-05 13:20:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 79.0 |
| 11b60597-0fb8-3344-9b85-85edcf460768 | -7.8356 | -45.3175 | 2026-10-05 13:20:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 128.6 |
| 1dc01169-89ef-381e-a6a2-7e38ff55781c | -11.6776 | -43.5633 | 2026-10-05 13:20:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 112.5 |
| 1b95f935-93cf-3579-9109-9218faa0f1d9 | -9.1259 | -67.7581 | 2026-10-05 13:20:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 60.0 |
| 65c38444-de0b-3ff4-a755-d952c03ee13c | -11.6968 | -43.5603 | 2026-10-05 13:20:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 114.4 |
| f3c35ba5-1a39-3443-bfa3-8201312f5104 | -9.8067 | -44.8035 | 2026-10-05 13:20:00 | GOES-19 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 71.2 |
| 60660929-2d74-34d9-8be5-26bd369f5947 | -9.8257 | -44.8011 | 2026-10-05 13:20:00 | GOES-19 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 75.1 |
| 0b86fe66-6d19-3dcb-9ace-185c5d9c8ce5 | -8.8713 | -45.37 | 2026-10-05 13:20:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 78.4 |
| f2951b51-a3c7-38af-82c6-1ce4011117a9 | -11.3009 | -44.2776 | 2026-10-05 13:20:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 83.5 |
| e7281760-6c36-3581-9af0-336ac495c4d3 | -10.9567 | -45.4349 | 2026-10-05 13:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 225.1 |
| f67a8cfe-7eec-389d-a80a-ebfa95d952b1 | -11.3204 | -44.2514 | 2026-10-05 13:20:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 86.8 |
| cbcb2a1b-1c92-3e3e-a562-ad8cedf3577e | -10.9762 | -45.4094 | 2026-10-05 13:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 106.0 |
| 7ef926bc-7f65-3509-a4e5-20bb0dfd2c0e | -10.9575 | -45.389 | 2026-10-05 13:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 75.0 |
| 2e3b9b02-4eed-3122-9234-1a548a3b4f03 | -7.8356 | -45.3175 | 2026-10-05 13:30:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 171.4 |
| 98ed0c91-f06d-36b4-ae54-d45459521fd6 | -11.2813 | -44.3038 | 2026-10-05 13:30:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 71.5 |
| 1f2b9271-455a-3a72-bbd6-75facc2c131d | -11.32 | -44.2748 | 2026-10-05 13:30:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 89.5 |
| 81809b01-742c-31d0-80c7-77c6ca93fed9 | -10.4904 | -46.0419 | 2026-10-05 13:30:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 59.6 |
| 354f57ac-1745-3d08-8bf7-0b27d30f2a25 | -7.8358 | -45.2948 | 2026-10-05 13:30:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 134.4 |
| 1e23fed1-1072-374e-b133-e060f91c9922 | -11.3009 | -44.2776 | 2026-10-05 13:30:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 91.8 |
| f8301281-7400-3d9e-9027-a1c99cadd5e3 | -9.8257 | -44.8011 | 2026-10-05 13:30:00 | GOES-19 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 104.1 |
| 23f18198-474e-307a-b474-f846f03b3c74 | -11.2817 | -44.2804 | 2026-10-05 13:30:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 101.2 |
| 07e8f47b-5b6c-368e-ae60-681f48dca709 | -11.3013 | -44.2542 | 2026-10-05 13:30:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 87.4 |
| 07045734-60cd-337d-bece-304c7465ec7d | -7.4889 | -42.8059 | 2026-10-05 13:30:00 | GOES-19 | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 152.6 |
| c552e7ca-000e-305c-850a-818141b78acb | -9.8634 | -44.8195 | 2026-10-05 13:30:00 | GOES-19 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 72.0 |
| 8b104310-9d3b-3ccf-8950-98f0c21bc12e | -10.9575 | -45.389 | 2026-10-05 13:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 55.0 |
| 86770624-4d59-3f4b-bfe6-1f35587071a7 | -9.8447 | -44.7988 | 2026-10-05 13:30:00 | GOES-19 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 75.5 |
| bc8997f1-638b-3ee4-a94d-1690d2f3ec3d | -8.8713 | -45.37 | 2026-10-05 13:30:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 72.9 |
| e3c1f8e1-969b-3efc-9fb4-772c14857d44 | -8.7526 | -64.1909 | 2026-10-05 13:30:00 | GOES-19 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 54.4 |
| 8b11c3da-b5d2-35cd-8bfd-c81d25168370 | -11.2821 | -44.257 | 2026-10-05 13:30:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 88.7 |
| 1c89167e-6b6c-383e-a12f-07f95efe694b | -7.8867 | -44.1902 | 2026-10-05 13:30:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 77.6 |
| 37a79450-8ec2-30e3-a3b4-98cfe098ef87 | -11.3204 | -44.2514 | 2026-10-05 13:30:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 92.1 |
| 61ee4f5e-4bb7-3cbb-9749-f60339ff56e0 | -6.9138 | -43.7049 | 2026-10-05 13:30:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 70.5 |
| dc05122d-580a-3465-a60b-6fa64e53e4ef | -9.8067 | -44.8035 | 2026-10-05 13:30:00 | GOES-19 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 80.3 |
| 2010a21c-d4e5-35e7-8530-53ce4efc623e | -7.9056 | -44.1883 | 2026-10-05 13:30:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 71.4 |
| 14188580-dba1-3289-a441-269c7f122e46 | -6.895 | -43.7066 | 2026-10-05 13:30:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 78.1 |
| 9feb1f92-e1ae-35af-9424-9a5b4246fa06 | -9.8631 | -44.8425 | 2026-10-05 13:40:00 | GOES-19 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 61.5 |
| 9305a302-3ac8-3c39-8c52-1316d503e181 | -11.2817 | -44.2804 | 2026-10-05 13:40:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 92.1 |
| 35b2135f-f73a-3a49-a944-df96159fc545 | -9.8824 | -44.8171 | 2026-10-05 13:40:00 | GOES-19 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 56.4 |
| 89f312f8-f29c-35a8-9093-ec9d1b390ced | -11.32 | -44.2748 | 2026-10-05 13:40:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 91.8 |


[Clique aqui para ver as próximas entradas](README64.md)
