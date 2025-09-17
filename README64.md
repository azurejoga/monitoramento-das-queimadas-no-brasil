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

## Dados Diários - Página 64

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| b85c83d2-6915-302b-ab18-871d8f2ab87e | -9.104 | -44.933 | 2025-09-17 13:30:00 | GOES-19 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 109.6 |
| ec757840-c295-331f-9dfe-4553f5e22f79 | -12.7294 | -47.9845 | 2025-09-17 13:30:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 83.0 |
| fb01bac9-b4d8-3069-8aca-9b7b3d122ad1 | -13.9653 | -44.921 | 2025-09-17 13:30:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 189.3 |
| 3ae66b85-68c2-3ce1-8802-dcd169909e9f | -8.9449 | -45.521 | 2025-09-17 13:30:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 147.4 |
| a3bb699f-ee92-3f34-9450-238698127e9e | -8.4467 | -47.692 | 2025-09-17 13:30:00 | GOES-19 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 68.0 |
| 9607a1e5-d9fb-3831-bac4-b6f873bb9fc0 | -6.6129 | -45.584 | 2025-09-17 13:30:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 138.4 |
| 7c63c877-5c76-3302-9f04-d1f6ef4a0a2d | -7.5227 | -44.7321 | 2025-09-17 13:40:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 111.6 |
| 3b64144c-8f6e-35a4-86f3-06e8229f1f8e | -6.6127 | -45.6066 | 2025-09-17 13:40:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 94.9 |
| 847076da-f297-3bb0-a58c-eb7d5faa74e6 | -8.992 | -46.2385 | 2025-09-17 13:40:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 87.6 |
| ebca88a4-17ea-3112-999d-ef322844f65b | -11.1299 | -45.3426 | 2025-09-17 13:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 70.4 |
| 5326a913-16f3-3d11-bd85-7fbe09f0ecad | -13.9648 | -44.9445 | 2025-09-17 13:40:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 100.7 |
| 77e7cca2-9f82-3264-b04c-cfcde497e675 | -8.9445 | -45.5438 | 2025-09-17 13:40:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 102.9 |
| a27b7b9a-c1c1-3b05-be61-86c1072f4993 | -13.9653 | -44.921 | 2025-09-17 13:40:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 184.1 |
| eb119c87-8963-3741-a9a8-c64fdd0da1f8 | -7.8259 | -46.153 | 2025-09-17 13:40:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 58.6 |
| 9c4ea8c9-ce89-3157-99ec-9154dfcccd80 | -7.676 | -44.4879 | 2025-09-17 13:40:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 92.5 |
| cc9243bd-e984-368d-9f1a-92ede5525563 | -9.1239 | -44.862 | 2025-09-17 13:40:00 | GOES-19 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 81.2 |
| e7fbe741-62e7-3891-850a-cd7249ffc6a8 | -8.9179 | -46.134 | 2025-09-17 13:40:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 67.2 |
| 41224d68-64bd-34b2-9c7e-a2febafbb29c | -12.729 | -48.0068 | 2025-09-17 13:40:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 108.2 |
| 008ab825-2a66-3a8d-b5e9-6db40f89ba65 | -6.6129 | -45.584 | 2025-09-17 13:40:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 93.1 |
| a158115f-e0b4-3bbf-b87b-eeb293e255ff | -12.6949 | -47.7669 | 2025-09-17 13:40:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 104.3 |
| 449cfa4a-96d7-37bd-b5cf-ebae801cda47 | -15.0549 | -42.4653 | 2025-09-17 13:40:00 | GOES-19 | MONTEZUMA | MINAS GERAIS | Brasil | 3143450 | 31 | 33 | nan | nan | nan | Caatinga | 105.8 |
| 3faba637-8f2f-3102-8e5f-1612cea25dff | -8.9176 | -46.1565 | 2025-09-17 13:40:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 74.4 |
| df01d718-d021-3155-b9d5-27e75b647f46 | -12.0243 | -46.6736 | 2025-09-17 13:40:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 78.3 |
| 1a5c57da-a2fd-39cb-b090-7db6e44a1908 | -12.7141 | -47.7642 | 2025-09-17 13:40:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 88.6 |
| 12d63b91-6877-3577-971c-9549528e6e2a | -8.6702 | -46.3394 | 2025-09-17 13:40:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 73.5 |
| 8314014b-f41a-34e8-8d55-7fc9d2832596 | -7.45 | -46.1871 | 2025-09-17 13:40:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 168.7 |
| 6c2d5fc8-9232-3ce2-b087-ad0e53eeb9a8 | -8.6882 | -46.4047 | 2025-09-17 13:40:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 81.4 |
| f346ea45-97f2-3bb8-bc0f-9361a70fae7a | -12.0051 | -46.6763 | 2025-09-17 13:40:00 | GOES-19 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 167.4 |
| b15f4f5e-3e51-38ba-ac45-b51914d3cea5 | -11.1108 | -45.3452 | 2025-09-17 13:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 119.0 |
| 7f08318c-c46a-3c61-b137-1e16cfbd5129 | -5.786 | -43.9147 | 2025-09-17 13:40:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 89.4 |
| 33d736a1-f458-36d2-8266-c51924a148bf | -8.6699 | -46.3618 | 2025-09-17 13:40:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 86.0 |
| 15d711e1-21b2-3cd5-bea3-fe63e30333a9 | -8.5609 | -47.5712 | 2025-09-17 13:40:00 | GOES-19 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 126.6 |
| d1764a6d-7fdb-3c1d-8546-c8138e550a21 | -8.631 | -46.4553 | 2025-09-17 13:40:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 118.6 |
| 1449b87f-f1ed-35ac-bc2c-ddf094af7d74 | -8.8958 | -47.8683 | 2025-09-17 13:40:00 | GOES-19 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 49.8 |
| bc80e9ca-8df0-3015-b1d3-3259051675e0 | -9.0851 | -44.9352 | 2025-09-17 13:40:00 | GOES-19 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 89.9 |
| fc635839-f50c-3ca0-af0b-b5d5a59d9fa8 | -5.8807 | -45.8865 | 2025-09-17 13:40:00 | GOES-19 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 101.4 |
| f6e835b3-91d6-36e4-ab6b-35bd892438bf | -8.899 | -46.136 | 2025-09-17 13:40:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 111.9 |
| 6d330876-7c3a-3605-bb6c-c698c096a327 | -10.6734 | -46.4928 | 2025-09-17 13:40:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 81.0 |
| daf188c5-ecc2-355d-b467-a7a626bb2ee5 | -14.7911 | -60.2289 | 2025-09-17 13:40:00 | GOES-19 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 227.9 |
| d007b4b7-7a84-3ca2-9d0b-b0bfcfd19573 | -8.9533 | -46.3099 | 2025-09-17 13:40:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 199.0 |
| e56b2b09-9563-3603-ad19-b477d1ff9892 | -12.7106 | -47.9649 | 2025-09-17 13:40:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 97.1 |
| f827ad30-beb2-3008-a49e-6859e2ff1fa8 | -8.9728 | -46.263 | 2025-09-17 13:40:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 84.7 |
| bd853bef-5b31-350e-bb28-e072db9e6770 | -8.6885 | -46.3823 | 2025-09-17 13:40:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 147.3 |
| ec8489e8-6688-387d-a587-3b15dd848eff | -9.1236 | -44.8849 | 2025-09-17 13:40:00 | GOES-19 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 111.8 |
| 88813388-8a37-3367-b0b2-d8ac773dd4c8 | -12.0047 | -46.6989 | 2025-09-17 13:40:00 | GOES-19 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 416.8 |
| c71e071c-bff1-32dd-a7b1-c252e30a6e97 | -8.8987 | -46.1585 | 2025-09-17 13:40:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 107.7 |
| 6686023d-da42-3451-946b-d4d224416f72 | -8.9725 | -46.2854 | 2025-09-17 13:40:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 121.7 |
| e0cc94ae-7699-3199-ae92-e09ba432385e | -3.8042 | -44.1072 | 2025-09-17 13:40:00 | GOES-19 | PIRAPEMAS | MARANHÃO | Brasil | 2108801 | 21 | 33 | nan | nan | nan | Cerrado | 181.2 |
| f77bdc10-9fe6-3ed7-922c-4541b3405209 | -6.3799 | -44.5122 | 2025-09-17 13:40:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 86.2 |
| 239dc8d9-dbb0-35ed-88b9-613a89f01342 | -7.581 | -44.566 | 2025-09-17 13:40:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 136.8 |
| fdd4c3a5-31ac-3fe9-a82e-3586e84fd479 | -9.0478 | -44.8936 | 2025-09-17 13:40:00 | GOES-19 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 81.3 |
| dc0b1d8b-7aff-3731-87ef-80de7bc1fc18 | -8.4467 | -47.692 | 2025-09-17 13:40:00 | GOES-19 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 66.2 |
| 487c5f25-83a4-3be9-aef2-84eeb8dad75a | -6.8734 | -43.9636 | 2025-09-17 13:40:00 | GOES-19 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 104.9 |
| b25de987-f1e4-35de-8edc-f82109d33793 | -11.5775 | -48.2926 | 2025-09-17 13:40:00 | GOES-19 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 80.0 |
| ec93bf3c-6bf1-338e-98bb-ebeec6936b49 | -8.4137 | -45.7583 | 2025-09-17 13:40:00 | GOES-19 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 100.7 |
| 3ca52a64-1877-33f1-a719-3db7083c4e43 | -14.7719 | -60.2305 | 2025-09-17 13:40:00 | GOES-19 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 187.8 |
| 3497d591-36ac-33e3-a49d-201a69f7fdf0 | -8.0005 | -45.6864 | 2025-09-17 13:40:00 | GOES-19 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 79.4 |
| e27cefbc-c8e0-3a18-b39c-a7e3afd8dac5 | -8.6887 | -46.3599 | 2025-09-17 13:40:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 128.3 |
| b594156d-4e4d-3698-934c-96ad33ae3ad6 | -14.7716 | -60.2503 | 2025-09-17 13:40:00 | GOES-19 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 120.7 |
| 6764594e-0cb9-3478-8d98-cab63860e4de | -8.9536 | -46.2874 | 2025-09-17 13:40:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 114.2 |
| c4b69665-bde2-39b6-805a-5992b4b2e217 | -7.6574 | -44.4667 | 2025-09-17 13:40:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 264.2 |
| 5a18cbb4-1818-3893-9e43-b5aea53d703e | -7.0048 | -45.7319 | 2025-09-17 13:40:00 | GOES-19 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 137.9 |
| 1ae5f658-3a11-3e2d-b15b-225c75f43b75 | -12.7294 | -47.9845 | 2025-09-17 13:40:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 101.3 |
| e151b0d2-cd18-3f0c-a03d-9547072ad9a0 | -11.5966 | -48.2902 | 2025-09-17 13:40:00 | GOES-19 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 75.3 |
| 7bcb1446-be14-35b5-ab3b-0b319ebc49e9 | -8.9449 | -45.521 | 2025-09-17 13:40:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 112.0 |
| 59c71f8a-8cab-31af-8cce-4b3f52ab27d1 | -9.0661 | -44.9374 | 2025-09-17 13:40:00 | GOES-19 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 91.9 |
| 3a02db28-835a-3199-9566-fb5063da84f5 | -8.414 | -45.7356 | 2025-09-17 13:40:00 | GOES-19 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 72.1 |
| 2888b102-0339-32d7-bd45-1594f3a9211c | -6.2055 | -45.1187 | 2025-09-17 13:40:00 | GOES-19 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 81.9 |
| ce7f8bc1-e842-32a6-9cb7-4f764fb12cef | -3.8756 | -41.6188 | 2025-09-17 13:40:00 | GOES-19 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 134.5 |
| 48501ece-5328-3b77-ad93-2eb5dc658f96 | -6.4102 | -43.3534 | 2025-09-17 13:40:00 | GOES-19 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 65.4 |
| e2f36d95-21e8-3d8a-92f0-4bc182e57c4a | -7.4109 | -50.0019 | 2025-09-17 13:40:00 | GOES-19 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 84.9 |
| e13133b0-2d09-3895-a9b2-6e1e77e4e7f0 | -10.9643 | -47.3514 | 2025-09-17 13:40:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 156.4 |
| 964b1587-bd3a-31fb-953b-c47199112739 | -8.1572 | -46.747 | 2025-09-17 13:40:00 | GOES-19 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 73.0 |
| 8510c11c-3f0a-3eaa-a70d-7b7129aabe19 | -7.4688 | -46.1854 | 2025-09-17 13:40:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 81.3 |
| 19570a65-cf25-3395-87f5-90c0641294dc | -9.4747 | -48.2698 | 2025-09-17 13:40:00 | GOES-19 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 57.5 |
| d64077f5-7d1f-33fe-984f-8024d46fed38 | -8.953 | -46.3324 | 2025-09-17 13:40:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 84.1 |
| 22982456-eb2d-36b7-a15b-9a26ccff9c7f | -7.6572 | -44.4897 | 2025-09-17 13:40:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 168.9 |
| c44f1e28-9ac8-34f7-aa5e-977b048b1d0b | -8.6313 | -46.4329 | 2025-09-17 13:40:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 76.3 |
| e24f6b09-08c9-3c77-a371-f290b03af53a | -8.5611 | -47.5492 | 2025-09-17 13:40:00 | GOES-19 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 61.5 |
| a1ed05d6-b274-359b-a102-4a0dde47c73d | -12.7018 | -45.2947 | 2025-09-17 13:50:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 132.0 |
| 62731184-70df-3039-9a2a-bb5ccc4d3661 | -7.6572 | -44.4897 | 2025-09-17 13:50:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 93.6 |
| 01390ad9-6b65-37d6-b572-5e26652291e1 | -12.6821 | -45.3209 | 2025-09-17 13:50:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 84.0 |
| 2d198677-dab2-3412-9ec7-5b59f73e9abe | -7.8259 | -46.153 | 2025-09-17 13:50:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 72.4 |
| c825ccea-3afe-337d-ade4-2a95337d33b1 | -12.6949 | -47.7669 | 2025-09-17 13:50:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 112.7 |
| 25112cb4-ec70-3a14-bcfe-f3b9ac6f2e0c | -9.0478 | -44.8936 | 2025-09-17 13:50:00 | GOES-19 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 102.1 |
| 7d7fb964-2b7b-3234-96e6-369af3cc9868 | -6.0071 | -44.3124 | 2025-09-17 13:50:00 | GOES-19 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 73.9 |
| 836df9e2-39fa-3790-88ba-2644b598d978 | -11.1104 | -45.3682 | 2025-09-17 13:50:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 89.2 |
| a162dd17-8e5c-3f08-bfdd-1010ac67db22 | -8.414 | -45.7356 | 2025-09-17 13:50:00 | GOES-19 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 79.8 |
| faef6e50-5fdb-34f8-ae14-7f4bb0219102 | -8.6313 | -46.4329 | 2025-09-17 13:50:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 77.2 |
| 15c18dcf-5b33-3d0d-b0a3-2e8a0710a438 | -5.9449 | -47.1032 | 2025-09-17 13:50:00 | GOES-19 | MONTES ALTOS | MARANHÃO | Brasil | 2107001 | 21 | 33 | nan | nan | nan | Cerrado | 102.3 |
| c5db976d-0827-31cd-8a1e-48c52149172b | -5.786 | -43.9147 | 2025-09-17 13:50:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 90.3 |
| 89f12f05-0036-3c32-bf39-9ab8dd599b4e | -5.7867 | -45.9603 | 2025-09-17 13:50:00 | GOES-19 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 64.0 |
| 4157f89f-e855-3cf9-9ede-3ccffcfb563f | -8.9449 | -45.521 | 2025-09-17 13:50:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 119.9 |
| 9fcd0f0a-bb04-38ac-a7ac-234006b8e28b | -8.899 | -46.136 | 2025-09-17 13:50:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 68.7 |
| 9c1695c3-d8f9-3383-9a13-8d5d2249af3f | -7.581 | -44.566 | 2025-09-17 13:50:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 307.1 |
| 116bf9e7-dc57-3b38-bcd1-adb547666c18 | -6.1868 | -45.1201 | 2025-09-17 13:50:00 | GOES-19 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 101.7 |
| 22428d9b-1db0-3d72-b8fd-2fe529528062 | -14.7719 | -60.2305 | 2025-09-17 13:50:00 | GOES-19 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 266.7 |
| bdd95516-4818-39b2-83b1-f945f66ccd42 | -7.0048 | -45.7319 | 2025-09-17 13:50:00 | GOES-19 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 83.9 |
| 5620f469-ec50-30d3-85b5-94c93017e528 | -13.9653 | -44.921 | 2025-09-17 13:50:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 284.5 |
| 04553538-6a09-3c46-bb51-0f3029756abf | -9.1236 | -44.8849 | 2025-09-17 13:50:00 | GOES-19 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 125.0 |


[Clique aqui para ver as próximas entradas](README65.md)
