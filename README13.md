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

## Dados Diários - Página 13

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| de001537-685d-3cb3-8960-d3d7d5b745ff | -2.3792 | -50.323601 | 2024-10-11 00:47:17 | METOP-B | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| eaeb5d3d-d21b-3b1e-be91-c45b97c7d7ad | -2.9586 | -52.888802 | 2024-10-11 00:47:17 | METOP-B | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5355591b-e85f-34f7-804d-f5dcef3f454d | -2.9602 | -52.895802 | 2024-10-11 00:47:17 | METOP-B | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 07be1015-d2b2-3b43-a5e0-8c72b63cbd56 | -2.9618 | -52.902802 | 2024-10-11 00:47:17 | METOP-B | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| aded3c42-8c33-3a03-a847-c59c7240adcc | -2.9633 | -52.909698 | 2024-10-11 00:47:17 | METOP-B | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f4713799-584c-3c94-80fc-dca59ece5b1c | -3.3425 | -54.604401 | 2024-10-11 00:47:17 | METOP-B | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8dc20331-d604-31c0-8bf4-f01170303a17 | -3.3442 | -54.612301 | 2024-10-11 00:47:17 | METOP-B | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 669ab491-42bb-396d-b8dc-0196502a1649 | -2.3873 | -50.404999 | 2024-10-11 00:47:17 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f7d4d71e-7779-315b-b42c-ddcc23f7e720 | -3.1258 | -53.7262 | 2024-10-11 00:47:17 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d448af12-f0d8-3295-bcc7-6c615151d3b6 | -3.1274 | -53.733501 | 2024-10-11 00:47:17 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| db89b60f-3974-359e-9c82-b8df44782420 | -3.1144 | -53.720901 | 2024-10-11 00:47:17 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7fa38d05-4c04-3867-9081-e97bfd010e80 | -3.116 | -53.728298 | 2024-10-11 00:47:17 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b1e58136-d48f-394d-bceb-db362d73a9e7 | -2.6493 | -51.698399 | 2024-10-11 00:47:17 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 102c9609-e5f4-3d37-a9d0-00fa52befdc5 | -2.6379 | -51.693802 | 2024-10-11 00:47:18 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e6f382c5-1409-3464-b9c9-8b8372957a97 | -2.6395 | -51.7006 | 2024-10-11 00:47:18 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b1856ab1-a8dc-3f4e-9f04-5df57666db5f | -2.641 | -51.707401 | 2024-10-11 00:47:18 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ebd61499-793d-3a01-8a59-9f0907365573 | -2.7808 | -52.4645 | 2024-10-11 00:47:18 | METOP-B | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 227d3df0-69e2-3520-8519-0e90cc1c5d0d | -2.7824 | -52.471298 | 2024-10-11 00:47:18 | METOP-B | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 01b4e6eb-df80-3b6b-888c-8e7c15596074 | -2.7839 | -52.478199 | 2024-10-11 00:47:18 | METOP-B | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 75cb5532-576d-3cd3-bc8d-99def54a9218 | -2.771 | -52.466702 | 2024-10-11 00:47:18 | METOP-B | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3610ee72-97e9-3d38-9ea1-9aa49fb9efb4 | -2.7726 | -52.473499 | 2024-10-11 00:47:18 | METOP-B | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 17c863c0-5a76-370a-97eb-6898d666468a | -2.7741 | -52.4804 | 2024-10-11 00:47:18 | METOP-B | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1ab599af-a97d-325e-b5f0-5bd973b1dfb9 | -2.7757 | -52.487301 | 2024-10-11 00:47:18 | METOP-B | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b88f3d3f-3cbb-3f64-93f2-47dfea219f27 | -2.8476 | -52.8988 | 2024-10-11 00:47:19 | METOP-B | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| dc479e8e-4efb-3e55-b886-0a77fce34ff1 | -2.844 | -52.928799 | 2024-10-11 00:47:19 | METOP-B | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9ce3450d-56b4-373f-be59-dffd3ba360c4 | -2.8456 | -52.935699 | 2024-10-11 00:47:19 | METOP-B | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 928a9eef-4843-378b-9902-07c9e13cb7ec | -2.5844 | -51.9132 | 2024-10-11 00:47:19 | METOP-B | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 53c866f0-9b51-368d-aec9-35c5b0f5eda1 | -2.586 | -51.919998 | 2024-10-11 00:47:19 | METOP-B | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 44326f6f-7f95-3e66-81c8-f7e7182e5bf4 | -2.8001 | -52.916599 | 2024-10-11 00:47:19 | METOP-B | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5b307145-4535-3650-885b-c433909dd963 | -4.2539 | -59.965801 | 2024-10-11 00:47:21 | METOP-B | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 3996fefe-02cd-3801-8e23-e896048c1ecf | -3.0697 | -54.7645 | 2024-10-11 00:47:22 | METOP-B | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ea7309bc-6765-37c6-8ef1-9079937799d6 | -2.9736 | -54.610401 | 2024-10-11 00:47:23 | METOP-B | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0c72a52a-3b45-3201-af80-8cb9c658b379 | -2.9754 | -54.618301 | 2024-10-11 00:47:23 | METOP-B | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 62fb6235-cd7a-3f54-994d-fd9584d91647 | -2.6776 | -53.334 | 2024-10-11 00:47:23 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1248ba1d-52df-3355-a297-e0859082f255 | -2.6792 | -53.341 | 2024-10-11 00:47:23 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 340654a2-c87b-3f32-bb98-7f9a18a161db | -2.6661 | -53.328999 | 2024-10-11 00:47:23 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a12911d1-34ce-35d7-a964-e6a246b65e0c | -2.6677 | -53.336102 | 2024-10-11 00:47:23 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3f3e65bc-7054-39ca-817d-300f6cbbb83d | -2.6693 | -53.343201 | 2024-10-11 00:47:23 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 195dc0a4-a5df-3d56-ba14-aed830323e06 | -2.6709 | -53.3503 | 2024-10-11 00:47:23 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7dd9791e-4968-3eca-88da-0ab3bfbbf746 | -2.6563 | -53.3312 | 2024-10-11 00:47:23 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ca403a8b-9c9b-32a0-87c7-5a812b259390 | -2.6579 | -53.338299 | 2024-10-11 00:47:23 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 717e38b9-3462-38e5-9b9f-60e45de5bb67 | -2.6595 | -53.345402 | 2024-10-11 00:47:23 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| abb78137-12c9-352d-89e9-5af9929576ba | -2.6611 | -53.352501 | 2024-10-11 00:47:23 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 83d2c468-9d22-3b44-a290-baa623f3a5bd | -2.8008 | -53.975399 | 2024-10-11 00:47:23 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 292d0a2a-c473-36d9-9f35-384c570a8765 | -2.8025 | -53.9828 | 2024-10-11 00:47:23 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 10013e2f-4d60-3374-a302-3570143c0cb7 | -2.8011 | -54.069 | 2024-10-11 00:47:24 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b5ed147d-ca0d-3b53-b916-3ae8fc6680c5 | -2.8028 | -54.0765 | 2024-10-11 00:47:24 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| aff0b2d0-a702-3570-9986-fb63cf3abedd | -2.7947 | -54.086201 | 2024-10-11 00:47:24 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| fcdd8c8e-2031-3a4f-a08a-3cfc01ea843e | -1.9758 | -51.089901 | 2024-10-11 00:47:26 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0b1d43da-12ef-38f4-b0e7-5c0ca58ae49d | -2.2539 | -53.4645 | 2024-10-11 00:47:30 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 39919161-9a34-344d-a27d-2fb0c9f6496f | -2.2555 | -53.4716 | 2024-10-11 00:47:30 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f55e61b1-e072-35d4-80ef-104ce909627a | -1.6651 | -52.131302 | 2024-10-11 00:47:35 | METOP-B | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| dfcc1996-002b-3eff-ad7d-0ec9fe65a277 | -1.7186 | -52.505798 | 2024-10-11 00:47:35 | METOP-B | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5b1a5583-9b45-3b31-ae50-b8016f27dac0 | -2.681 | -57.911301 | 2024-10-11 00:47:39 | METOP-B | URUCARÁ | AMAZONAS | Brasil | 1304302 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 85545a0b-bb7e-3071-82ab-1d06872d3c52 | -2.6837 | -57.923401 | 2024-10-11 00:47:39 | METOP-B | URUCARÁ | AMAZONAS | Brasil | 1304302 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 115df18e-4cc6-3223-bd6f-63d1a67add76 | -1.4764 | -52.5737 | 2024-10-11 00:47:40 | METOP-B | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c597f959-c405-3237-9295-62dc178efe20 | -1.5951 | -53.329102 | 2024-10-11 00:47:40 | METOP-B | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c9526ac5-778c-391e-b63c-609b21a7bc44 | -1.5966 | -53.335999 | 2024-10-11 00:47:40 | METOP-B | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 03ff9590-6ff7-3c0f-81cd-97f1415556d8 | -1.5982 | -53.342999 | 2024-10-11 00:47:40 | METOP-B | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 39bace8f-40cf-3585-920d-fd3453bd19e1 | -1.5868 | -53.3381 | 2024-10-11 00:47:41 | METOP-B | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d4b28d6b-5331-39ed-b403-e01a6f537217 | -1.5884 | -53.3451 | 2024-10-11 00:47:41 | METOP-B | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9ed23278-1786-3bd6-b052-e4d517bbe387 | -1.7062 | -54.3727 | 2024-10-11 00:47:42 | METOP-B | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 126b77b3-ad54-351f-b79f-9ac9361f3471 | -1.7079 | -54.380199 | 2024-10-11 00:47:42 | METOP-B | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c7fb21f9-34ea-38ae-bcec-797cc8cf42db | -2.002 | -56.013802 | 2024-10-11 00:47:44 | METOP-B | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b0ed5e72-6745-391f-aa0b-2c42477dedc8 | -1.7536 | -55.3176 | 2024-10-11 00:47:45 | METOP-B | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 91032ab6-d992-3473-9929-fd4f375ee71c | -1.7555 | -55.325802 | 2024-10-11 00:47:45 | METOP-B | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 802e12bc-e08f-3eb1-a96a-e5981908162f | -3.0425 | -61.633701 | 2024-10-11 00:47:47 | METOP-B | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| f687547f-1575-348d-8b6b-d68e17879555 | -3.0328 | -61.635799 | 2024-10-11 00:47:47 | METOP-B | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 5957280f-9d85-3ed7-9728-72ca1763cbe8 | -3.0377 | -61.6581 | 2024-10-11 00:47:47 | METOP-B | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 6e1c5cec-5109-3c85-b4cf-daba1262aadd | -1.1833 | -53.375999 | 2024-10-11 00:47:47 | METOP-B | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2f417f88-26db-3420-9466-2ba527733767 | -1.1735 | -53.378101 | 2024-10-11 00:47:47 | METOP-B | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 41704da3-b6b9-3713-9747-79205e6b8e0e | -1.1751 | -53.385101 | 2024-10-11 00:47:47 | METOP-B | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f84947ec-c9d6-376b-b4e5-0e46d8314aef | -1.1767 | -53.392101 | 2024-10-11 00:47:47 | METOP-B | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5c1cf67a-5005-393a-803b-f7d49be6ce1d | -1.1653 | -53.387299 | 2024-10-11 00:47:48 | METOP-B | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| fec5f1e9-4af8-3522-90dc-6c76ce6a52b6 | -1.1669 | -53.394299 | 2024-10-11 00:47:48 | METOP-B | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e8b7f6a4-2528-36df-85ba-170068694218 | -1.1684 | -53.401299 | 2024-10-11 00:47:48 | METOP-B | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f92d242b-31ed-394a-9be7-64b920b6740a | -1.1555 | -53.3894 | 2024-10-11 00:47:48 | METOP-B | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3b5f0443-2568-3307-9d98-b6b382a90633 | -1.1571 | -53.3964 | 2024-10-11 00:47:48 | METOP-B | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4d768258-df9e-362e-b277-ef21ccbf99de | -1.1275 | -53.631302 | 2024-10-11 00:47:49 | METOP-B | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 96f8a5f7-100c-3782-86d7-efcbf53a46bb | -1.5258 | -55.402401 | 2024-10-11 00:47:49 | METOP-B | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7bc38154-0639-33e1-96d2-961645c120ce | -1.5277 | -55.410599 | 2024-10-11 00:47:49 | METOP-B | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 201bf2fb-3b92-3353-a418-2bd98d436b24 | -1.113 | -53.612301 | 2024-10-11 00:47:49 | METOP-B | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| bcdd4b26-8d2d-32ad-8052-99a8758be183 | -1.516 | -55.404499 | 2024-10-11 00:47:49 | METOP-B | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9ddc97b5-3eb6-3eb7-9a99-c5b935d044b2 | -1.1196 | -54.053398 | 2024-10-11 00:47:51 | METOP-B | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b1d36c6f-9934-3765-99de-ff3acf2954cb | -1.1426 | -54.201199 | 2024-10-11 00:47:51 | METOP-B | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1047d138-d285-360b-8a87-2d5e7f605d99 | -1.0242 | -53.721001 | 2024-10-11 00:47:51 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d545f38a-e5df-314d-9317-646f757bf908 | -1.0258 | -53.7281 | 2024-10-11 00:47:51 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 134fac45-dd96-366c-8746-3b1d0c569a67 | -1.1344 | -54.210701 | 2024-10-11 00:47:51 | METOP-B | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e23c91c2-06e8-3550-bbf0-1562baf68be9 | -0.3811 | -52.058201 | 2024-10-11 00:47:55 | METOP-B | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | nan |
| 947b9f03-aeaf-3778-9f60-43d2777fc35e | 2.4842 | -50.814602 | 2024-10-11 00:48:37 | METOP-B | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | nan |
| 41b4fdec-7f3c-3921-a227-bf20a56c38fc | 2.4825 | -50.822201 | 2024-10-11 00:48:37 | METOP-B | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | nan |
| 1666e4e4-e7f3-3968-94e7-f106a3a5ad65 | 2.3492 | -51.553902 | 2024-10-11 00:48:38 | METOP-B | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | nan |
| 4db10a26-b6bd-3d5c-8cd5-3e07de65ceac | -13.82399 | -42.42636 | 2024-10-11 00:54:00 | TERRA_M-M | CAETITÉ | BAHIA | Brasil | 2905206 | 29 | 33 | nan | nan | nan | Caatinga | 8.0 |
| 24312df4-2e59-3ef6-b6b2-db07117adf1b | -9.62139 | -40.35163 | 2024-10-11 00:54:00 | TERRA_M-M | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 23.5 |
| ddd0aff9-5a70-3edd-a2ff-9ca0e2e6331f | -9.61756 | -40.32811 | 2024-10-11 00:54:00 | TERRA_M-M | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 25.7 |
| 887f7b66-45a4-3e64-8fdd-79d1cc25e657 | -11.83485 | -42.82109 | 2024-10-11 00:54:00 | TERRA_M-M | BROTAS DE MACAÚBAS | BAHIA | Brasil | 2904506 | 29 | 33 | nan | nan | nan | Caatinga | 8.3 |
| 25a0de05-f2d9-36e6-a81d-ac40952f808b | -11.08445 | -42.30698 | 2024-10-11 00:54:00 | TERRA_M-M | ITAGUAÇU DA BAHIA | BAHIA | Brasil | 2915353 | 29 | 33 | nan | nan | nan | Caatinga | 9.9 |
| 970086ab-247d-3b61-b403-0438f67a3a54 | -13.45964 | -42.6664 | 2024-10-11 00:54:00 | TERRA_M-M | MACAÚBAS | BAHIA | Brasil | 2919801 | 29 | 33 | nan | nan | nan | Caatinga | 6.3 |
| f809074b-ba39-3772-8235-106b676970f6 | -13.08045 | -43.3717 | 2024-10-11 00:54:00 | TERRA_M-M | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 5046a0dd-af70-33f0-beab-f0ee968d7a27 | -12.59026 | -42.42049 | 2024-10-11 00:54:00 | TERRA_M-M | IBITIARA | BAHIA | Brasil | 2913002 | 29 | 33 | nan | nan | nan | Caatinga | 13.0 |


[Clique aqui para ver as próximas entradas](README14.md)
