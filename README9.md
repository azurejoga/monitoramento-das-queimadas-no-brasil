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

## Dados Diários - Página 9

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| e7293b60-6a93-3af2-bb88-6e329313d2a5 | -25.19946 | -49.32413 | 2025-05-14 04:51:00 | NOAA-21 | RIO BRANCO DO SUL | PARANÁ | Brasil | 4122206 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 531e4fa2-efa0-376c-b27d-01d7eea58bb6 | -23.44225 | -49.86553 | 2025-05-14 04:51:00 | NOAA-21 | JOAQUIM TÁVORA | PARANÁ | Brasil | 4112801 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 7dcd071d-0a45-331d-8d7f-3df39d08c469 | -23.98401 | -48.91872 | 2025-05-14 04:51:00 | NOAA-21 | ITAPEVA | SÃO PAULO | Brasil | 3522406 | 35 | 33 | nan | nan | nan | Cerrado | 0.7 |
| a537c575-4e0a-351f-b493-5fd9484c9b24 | -21.89581 | -56.26644 | 2025-05-14 04:51:00 | NOAA-21 | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 1405695e-d676-3084-a279-72a324b66d22 | -21.6059 | -56.04236 | 2025-05-14 04:51:00 | NOAA-21 | GUIA LOPES DA LAGUNA | MATO GROSSO DO SUL | Brasil | 5004106 | 50 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 57ddf80c-e306-3b4c-b007-55587578dc43 | -21.71852 | -55.37472 | 2025-05-14 04:51:00 | NOAA-21 | MARACAJU | MATO GROSSO DO SUL | Brasil | 5005400 | 50 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 31d90a8e-8afa-384e-a628-b30f5aa08573 | -22.15271 | -56.64434 | 2025-05-14 04:51:00 | NOAA-21 | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d1331a4b-edf2-325e-8968-69154a541589 | -21.60926 | -56.04298 | 2025-05-14 04:51:00 | NOAA-21 | GUIA LOPES DA LAGUNA | MATO GROSSO DO SUL | Brasil | 5004106 | 50 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 3a956fd1-ce22-3ed9-ad8c-34b71d6e10d7 | -21.77574 | -55.31612 | 2025-05-14 04:51:00 | NOAA-21 | MARACAJU | MATO GROSSO DO SUL | Brasil | 5005400 | 50 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 7534f91c-23fc-3379-8a99-7e41fa6cab47 | -21.72184 | -55.37533 | 2025-05-14 04:51:00 | NOAA-21 | MARACAJU | MATO GROSSO DO SUL | Brasil | 5005400 | 50 | 33 | nan | nan | nan | Cerrado | 8.9 |
| 225676ae-1c3a-3ac3-8cc1-ef28881d0f5d | -22.67915 | -42.85344 | 2025-05-14 04:51:00 | NOAA-21 | ITABORAÍ | RIO DE JANEIRO | Brasil | 3301900 | 33 | 33 | nan | nan | nan | Mata Atlântica | 5.5 |
| 1b8005ed-9540-3a5e-8869-a03a51af211a | -26.60278 | -53.14976 | 2025-05-14 04:51:00 | NOAA-21 | SANTA TEREZINHA DO PROGRESSO | SANTA CATARINA | Brasil | 4215687 | 42 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| 0d5a7aa2-b9ef-3f3f-8bc6-8010a0866dec | -21.60863 | -56.04682 | 2025-05-14 04:51:00 | NOAA-21 | GUIA LOPES DA LAGUNA | MATO GROSSO DO SUL | Brasil | 5004106 | 50 | 33 | nan | nan | nan | Cerrado | 3.7 |
| d618acbd-39e6-3880-b0d0-3696cec81407 | -23.79301 | -54.86513 | 2025-05-14 04:51:00 | NOAA-21 | TACURU | MATO GROSSO DO SUL | Brasil | 5007950 | 50 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| f76e8977-58a4-3565-9ae9-1a5a6bffbc50 | -20.97885 | -48.99902 | 2025-05-14 04:51:00 | NOAA-21 | TABAPUÃ | SÃO PAULO | Brasil | 3552601 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 94c4adb7-8931-367b-b6ad-e9fb2997dccc | -21.46457 | -57.15224 | 2025-05-14 04:51:00 | NOAA-21 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 2.4 |
| b56fed60-89b0-394e-960c-7b67546b1aad | -21.25558 | -49.16778 | 2025-05-14 04:51:00 | NOAA-21 | MARAPOAMA | SÃO PAULO | Brasil | 3528858 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| eab5df7b-a250-3ccc-8259-82c975f07460 | -20.82082 | -49.78596 | 2025-05-14 04:51:00 | NOAA-21 | MONTE APRAZÍVEL | SÃO PAULO | Brasil | 3531407 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| dcc90ddf-ec4e-3ce0-83af-f74788df60f6 | -20.98004 | -48.48347 | 2025-05-14 04:51:00 | NOAA-21 | BEBEDOURO | SÃO PAULO | Brasil | 3506102 | 35 | 33 | nan | nan | nan | Cerrado | 1.6 |
| d0db979d-27ef-3332-bc63-20b0a2662f46 | -21.60526 | -56.0462 | 2025-05-14 04:51:00 | NOAA-21 | GUIA LOPES DA LAGUNA | MATO GROSSO DO SUL | Brasil | 5004106 | 50 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 2730cd98-0129-3d0d-9218-124c554abd34 | -20.47816 | -53.67496 | 2025-05-14 04:51:00 | NOAA-21 | RIBAS DO RIO PARDO | MATO GROSSO DO SUL | Brasil | 5007109 | 50 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 83532327-9e57-327a-883a-869bb4e0b8bc | -21.77514 | -55.31986 | 2025-05-14 04:51:00 | NOAA-21 | MARACAJU | MATO GROSSO DO SUL | Brasil | 5005400 | 50 | 33 | nan | nan | nan | Cerrado | 0.7 |
| ab007cd7-8031-3535-836d-18a006289128 | -28.66709 | -50.25124 | 2025-05-14 04:53:00 | NOAA-21 | BOM JESUS | RIO GRANDE DO SUL | Brasil | 4302303 | 43 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| c29568c3-2b36-3cf7-a384-a52f9e7e2f3f | -15.2755 | -43.0758 | 2025-05-14 05:10:00 | GOES-19 | MONTE AZUL | MINAS GERAIS | Brasil | 3142908 | 31 | 33 | nan | nan | nan | Caatinga | 53.4 |
| e6008954-0936-3963-b6b9-4db285ed7bee | -2.75244 | -54.59241 | 2025-05-14 05:10:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 47d641f5-ce5d-3832-a468-c2aa0a8d61e1 | -7.7246 | -46.33287 | 2025-05-14 05:12:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 9382a24e-703b-36dc-85ca-c98b92b73c19 | -7.72342 | -46.34182 | 2025-05-14 05:12:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 11.4 |
| 8bcdcc39-b30a-3635-8aab-baefc69829b8 | -7.72398 | -46.33755 | 2025-05-14 05:12:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 8.0 |
| a9cbaf81-7516-34d5-9d85-b8117277afaf | -7.71722 | -46.34096 | 2025-05-14 05:12:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 66292e2f-5eee-3b41-9bfd-cce459e883c6 | -7.7178 | -46.33654 | 2025-05-14 05:12:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 3cd8c732-1c61-3a11-b085-21be43846e42 | -11.63719 | -48.12414 | 2025-05-14 05:12:00 | NPP-375D | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| f4ea6108-b211-32c2-b3fe-76601a37e8cc | -9.2587 | -60.31659 | 2025-05-14 05:12:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| b5252eaa-cf13-340f-b04d-5bcde0ee292e | -11.63086 | -48.12747 | 2025-05-14 05:12:00 | NPP-375D | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 059be9a5-0976-3e76-8aac-d2d4a5057a13 | -11.62554 | -48.1226 | 2025-05-14 05:12:00 | NPP-375D | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| e289ca4b-9531-3bb0-bc9a-152227da50d1 | -9.26541 | -50.21163 | 2025-05-14 05:12:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 0c8ae94d-3447-3d24-8e55-008d849d2778 | -10.00315 | -47.83646 | 2025-05-14 05:12:00 | NPP-375D | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 93ed8e4e-f2b4-3366-b3f7-0e8dffb57fbb | -11.63136 | -48.12339 | 2025-05-14 05:12:00 | NPP-375D | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 34098419-6476-3533-9355-ee0b9c623d43 | -9.2628 | -60.31332 | 2025-05-14 05:12:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 90728c24-a72f-3027-87b6-2979cffae009 | -11.80156 | -44.27804 | 2025-05-14 05:12:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 14db8305-1e68-3897-875b-ac2f754b87b7 | -11.79622 | -46.64096 | 2025-05-14 05:12:00 | NPP-375D | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 583ae423-08f6-38ba-a30a-988da1962a67 | -9.25537 | -56.32763 | 2025-05-14 05:12:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 96fef4ba-92a0-37b2-b8a9-64a5a293d57e | -10.00359 | -47.83379 | 2025-05-14 05:12:00 | NPP-375D | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d9a4c0af-7bbe-3245-a87e-d71b745c928c | -10.00894 | -47.83742 | 2025-05-14 05:12:00 | NPP-375D | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| f344db80-b0e3-358f-869b-5f73f9d79d11 | -9.26832 | -50.21066 | 2025-05-14 05:12:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| c3812937-aabe-3f8b-a2bb-a157080cff3d | -9.99726 | -47.83702 | 2025-05-14 05:12:00 | NPP-375D | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 0870e912-46b4-3789-968d-efdfa0f9f777 | -8.07193 | -47.13123 | 2025-05-14 05:12:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| ebfcdf5a-542a-3b4a-91ef-9fbbd7deed65 | -9.25932 | -60.31274 | 2025-05-14 05:12:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d4b12d39-934f-3ca8-b518-9de6989d0da9 | -10.17937 | -48.02312 | 2025-05-14 05:12:00 | NPP-375D | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| cac04e75-5b86-397a-ae5a-0db77fd258f5 | -10.48557 | -49.14718 | 2025-05-14 05:12:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 97b1954b-80ab-350a-a406-fdd6f7b904ba | -10.48313 | -49.14592 | 2025-05-14 05:12:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 9a7e5785-a294-349c-b836-f10c81b92593 | -10.00938 | -47.83478 | 2025-05-14 05:12:00 | NPP-375D | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 0aa0d92b-afdf-3fe1-a43a-9b39ae6c38c6 | -9.25542 | -56.32723 | 2025-05-14 05:12:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 5627ba64-84d9-377e-b960-2b06fe09a16c | -9.99737 | -47.83538 | 2025-05-14 05:12:00 | NPP-375D | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| aa38200c-8d2e-313a-b6af-9283f72a5e1f | -9.57376 | -49.10782 | 2025-05-14 05:12:00 | NPP-375D | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 6213ec1d-4de6-37d1-a1c1-f870a37a4a49 | -11.80265 | -46.6416 | 2025-05-14 05:12:00 | NPP-375D | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| bb3a6a27-e01e-35ca-8a4d-23cc31431539 | -8.06659 | -47.12601 | 2025-05-14 05:12:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 1248b2ea-bced-3d8a-9a50-b4fbcfa77bee | -10.18508 | -48.02421 | 2025-05-14 05:12:00 | NPP-375D | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 685687c0-f97c-3cbf-ba60-335afe50775e | -10.00883 | -47.83897 | 2025-05-14 05:12:00 | NPP-375D | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 08c8e747-057c-3748-9de4-0d957821b6af | -10.00947 | -47.83315 | 2025-05-14 05:12:00 | NPP-375D | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 3548fa30-105d-30b4-8ed3-df99a5637f6a | -9.26218 | -60.31717 | 2025-05-14 05:12:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 254453f9-83e2-3cc7-8a04-722a47362523 | -9.25879 | -56.32817 | 2025-05-14 05:12:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3ac62155-b729-3d3a-8a32-37eca3b87223 | -10.00993 | -47.8305 | 2025-05-14 05:12:00 | NPP-375D | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 997be94a-e1af-398a-b069-2ad03360708f | -9.25823 | -56.33189 | 2025-05-14 05:12:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 4b734be5-ad46-33b5-9921-820e66a4531d | -10.00304 | -47.83807 | 2025-05-14 05:12:00 | NPP-375D | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 7a585c3d-4dd2-363a-be00-1bd6d081d132 | -9.5742 | -49.10453 | 2025-05-14 05:12:00 | NPP-375D | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 75f76f29-fef7-3323-9a9e-cb7728028c65 | -13.96511 | -56.79333 | 2025-05-14 05:14:00 | NPP-375D | DIAMANTINO | MATO GROSSO | Brasil | 5103502 | 51 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 6885c1e0-7b0f-3183-9bf6-c4bb8cdb9ae1 | -11.65675 | -54.95412 | 2025-05-14 05:14:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 0674dcb9-bb4c-36fa-82ea-dac5c95b897d | -12.30215 | -52.4937 | 2025-05-14 05:14:00 | NPP-375D | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1b927737-95b6-36c9-985e-a810bf9af09f | -13.55786 | -52.87922 | 2025-05-14 05:14:00 | NPP-375D | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 5a549008-22a1-32d4-a3a4-24210c0f4572 | -11.85052 | -57.8561 | 2025-05-14 05:14:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 5935389f-20dc-3eaa-8c3f-a904a912c53f | -13.04896 | -53.72474 | 2025-05-14 05:14:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 304c11dc-54e7-3ed7-b6f1-5905946f8db1 | -13.95987 | -56.78029 | 2025-05-14 05:14:00 | NPP-375D | DIAMANTINO | MATO GROSSO | Brasil | 5103502 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d2abe78a-6c20-3c84-bc9e-b634a07b4995 | -10.48386 | -59.14695 | 2025-05-14 05:14:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 38c54cb5-d215-3585-a6ac-54f3dec4e03b | -14.63513 | -45.11288 | 2025-05-14 05:14:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| fac8108c-ddf4-3d6d-b40e-192aa6763031 | -12.86783 | -55.05984 | 2025-05-14 05:14:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3bcd3f2b-0541-38d6-96b5-57da84131896 | -11.65271 | -58.26471 | 2025-05-14 05:14:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 5e241ebe-5ea8-33a0-8d52-7aa19bf84dfd | -12.8685 | -55.05524 | 2025-05-14 05:14:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 792c8799-3048-3a6b-accf-c8944b5f2aa8 | -12.69057 | -58.12781 | 2025-05-14 05:14:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 3222dd37-5043-3823-baa5-552b2cbb0ec5 | -12.15595 | -48.00938 | 2025-05-14 05:14:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 35fe95d5-8ce5-35b7-bcd7-f7f12f5f6bc7 | -9.67468 | -65.5375 | 2025-05-14 05:14:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.2 |
| a7d8c25b-caf4-3120-b63b-571f72f4c10b | -12.29182 | -52.47028 | 2025-05-14 05:14:00 | NPP-375D | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 2da8ebf1-e76d-3ee9-a5d7-a755aed68eba | -13.96104 | -56.79671 | 2025-05-14 05:14:00 | NPP-375D | DIAMANTINO | MATO GROSSO | Brasil | 5103502 | 51 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 6c4eb488-b869-3cc4-b1e7-40ae68b735e0 | -12.50223 | -57.21606 | 2025-05-14 05:14:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e0da7569-88d6-338e-b0ee-27096eca2d8a | -13.07063 | -52.01915 | 2025-05-14 05:14:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| c6f9abaf-f9d7-338e-ab42-6b14c00c07b0 | -14.63379 | -45.11508 | 2025-05-14 05:14:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| dc280e53-344c-34ce-8b8d-6d271582833b | -13.56221 | -52.87984 | 2025-05-14 05:14:00 | NPP-375D | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 8766d4c0-547a-3460-af81-66660ebc34f6 | -13.96279 | -56.78482 | 2025-05-14 05:14:00 | NPP-375D | DIAMANTINO | MATO GROSSO | Brasil | 5103502 | 51 | 33 | nan | nan | nan | Cerrado | 6.9 |
| d851637a-b3bf-3e25-815a-8b959d4784cb | -13.96337 | -56.78085 | 2025-05-14 05:14:00 | NPP-375D | DIAMANTINO | MATO GROSSO | Brasil | 5103502 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d83babd9-7e80-3959-aa57-1981abdbbe0e | -13.5677 | -52.87187 | 2025-05-14 05:14:00 | NPP-375D | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 83d7c89e-2efc-3721-bd83-2248ac49a7a6 | -12.64855 | -54.08336 | 2025-05-14 05:14:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 94e607b7-3db4-31d0-b48d-e7b8a438329c | -12.50508 | -57.22033 | 2025-05-14 05:14:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 939f1234-d482-3d66-bff4-8e69e6289f45 | -13.98201 | -56.80002 | 2025-05-14 05:14:00 | NPP-375D | DIAMANTINO | MATO GROSSO | Brasil | 5103502 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| f5c0c4ae-41b2-3475-a168-4ebcf1e6709f | -10.4833 | -59.1505 | 2025-05-14 05:14:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 081c42ee-472c-38d2-ba9f-59f3e8d1c930 | -12.73095 | -54.9706 | 2025-05-14 05:14:00 | NPP-375D | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| eac8c6fe-6959-38a9-934c-a05d08b00909 | -11.91915 | -54.40411 | 2025-05-14 05:14:00 | NPP-375D | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8e8551bc-073e-3fe7-b080-450f8823f9ac | -14.6293 | -45.0973 | 2025-05-14 05:14:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 3.1 |
| a5f355ac-c3fb-3839-8a09-a9b1c3dba6f6 | -13.56713 | -52.87615 | 2025-05-14 05:14:00 | NPP-375D | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 5c46bc2e-ab28-3c29-8872-88020c74df90 | -11.44035 | -54.09375 | 2025-05-14 05:14:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7a66a6bf-c394-34dd-9a60-5d57daeeb114 | -14.62805 | -45.09957 | 2025-05-14 05:14:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| e9b49d4b-bf3a-3a59-be3e-e080900fdbca | -12.15544 | -48.01365 | 2025-05-14 05:14:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |


[Clique aqui para ver as próximas entradas](README10.md)
