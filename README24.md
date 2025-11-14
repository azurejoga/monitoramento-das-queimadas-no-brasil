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

## Dados Diários - Página 24

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| d8b8dd66-111a-3487-b260-165973e9d2e3 | -16.24005 | -45.64169 | 2025-11-14 03:57:00 | NOAA-21 | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 2b55cab8-115a-3a01-9449-12f98a44858b | -20.82693 | -45.8386 | 2025-11-14 03:57:00 | NOAA-21 | GUAPÉ | MINAS GERAIS | Brasil | 3128105 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 02f6338e-9103-3679-8f73-859162fe13ea | -17.98877 | -42.99199 | 2025-11-14 03:57:00 | NOAA-21 | ITAMARANDIBA | MINAS GERAIS | Brasil | 3132503 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 781fbeee-f85f-3f02-ba72-016c33bf8e21 | -20.39357 | -41.95782 | 2025-11-14 03:57:00 | NOAA-21 | MANHUMIRIM | MINAS GERAIS | Brasil | 3139508 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| fb8ccaa5-3b21-320c-9c3c-91a6ec232336 | -21.65386 | -48.63021 | 2025-11-14 03:57:00 | NOAA-21 | TABATINGA | SÃO PAULO | Brasil | 3552700 | 35 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 50e5cd27-8773-369d-b237-05eccf5807a2 | -18.70705 | -43.00791 | 2025-11-14 03:57:00 | NOAA-21 | SABINÓPOLIS | MINAS GERAIS | Brasil | 3156809 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 8cbe8ba8-fa87-36b1-8bd4-8665be487a4d | -17.67907 | -42.44416 | 2025-11-14 03:57:00 | NOAA-21 | CAPELINHA | MINAS GERAIS | Brasil | 3112307 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| bede1568-e733-357c-9894-e2aa62ab69a7 | -20.10134 | -41.67651 | 2025-11-14 03:57:00 | NOAA-21 | LAJINHA | MINAS GERAIS | Brasil | 3137700 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 4419826a-ecca-3726-87a4-88a786b2d394 | 3.1094 | -60.765 | 2025-11-14 04:00:00 | GOES-19 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 93.7 |
| c859b889-f425-3b4d-bfe0-ec140447a870 | -11.8486 | -49.2218 | 2025-11-14 04:00:00 | GOES-19 | CARIRI DO TOCANTINS | TOCANTINS | Brasil | 1703867 | 17 | 33 | nan | nan | nan | Cerrado | 128.8 |
| d1d85ae3-473a-3970-847e-1f9e2de5e364 | 3.0911 | -60.7653 | 2025-11-14 04:00:00 | GOES-19 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 64.3 |
| d440e9e5-f72c-30d2-885c-037c2328c445 | -11.8677 | -49.2195 | 2025-11-14 04:00:00 | GOES-19 | CARIRI DO TOCANTINS | TOCANTINS | Brasil | 1703867 | 17 | 33 | nan | nan | nan | Cerrado | 98.7 |
| 78b0c5ac-e060-32bf-b041-70d1910cb52a | -14.7066 | -46.6164 | 2025-11-14 04:00:00 | GOES-19 | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 81.7 |
| e8bb52cc-35c8-3de7-b10a-17b3b53db9ad | -14.7066 | -46.6164 | 2025-11-14 04:10:00 | GOES-19 | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 71.9 |
| 2c08972b-4de4-32c6-a57b-40b7cda36e42 | 3.0911 | -60.7653 | 2025-11-14 04:10:00 | GOES-19 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 64.3 |
| 7554da3c-4824-363b-b8e2-ec2564817a4a | 3.1094 | -60.765 | 2025-11-14 04:10:00 | GOES-19 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 78.6 |
| c0c313f1-8f4a-3318-af07-beb3b579b935 | -11.8677 | -49.2195 | 2025-11-14 04:10:00 | GOES-19 | CARIRI DO TOCANTINS | TOCANTINS | Brasil | 1703867 | 17 | 33 | nan | nan | nan | Cerrado | 102.7 |
| b4805955-71a3-385e-9b07-e9085a35dad8 | -11.8486 | -49.2218 | 2025-11-14 04:10:00 | GOES-19 | CARIRI DO TOCANTINS | TOCANTINS | Brasil | 1703867 | 17 | 33 | nan | nan | nan | Cerrado | 124.8 |
| 99043879-de05-380d-ad82-dc85bc37e5bd | 3.1094 | -60.765 | 2025-11-14 04:20:00 | GOES-19 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 74.5 |
| e5f3efda-192e-3080-b6a6-754edb443ae2 | 3.0911 | -60.7653 | 2025-11-14 04:20:00 | GOES-19 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 68.0 |
| f3009c85-77c1-35d6-89ec-7ad776d80f23 | -14.7066 | -46.6164 | 2025-11-14 04:20:00 | GOES-19 | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 81.8 |
| 4835c387-7555-38ff-a003-c7b0be393c91 | -11.8486 | -49.2218 | 2025-11-14 04:20:00 | GOES-19 | CARIRI DO TOCANTINS | TOCANTINS | Brasil | 1703867 | 17 | 33 | nan | nan | nan | Cerrado | 121.0 |
| f2ad08ab-dac9-3047-81af-528209d677dc | -2.9434 | -49.3655 | 2025-11-14 04:20:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 30.7 |
| edfb250b-03a9-30a9-ae96-a62aadab9f43 | -11.8677 | -49.2195 | 2025-11-14 04:20:00 | GOES-19 | CARIRI DO TOCANTINS | TOCANTINS | Brasil | 1703867 | 17 | 33 | nan | nan | nan | Cerrado | 83.5 |
| 7edb5869-1102-37b4-92d7-1f34a78a74e5 | -4.29094 | -41.81561 | 2025-11-14 04:23:00 | NPP-375D | PIRIPIRI | PIAUÍ | Brasil | 2208403 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| c510bd6b-8bd9-3a33-9602-c1051fb1b8e8 | -9.05861 | -44.77968 | 2025-11-14 04:23:00 | NPP-375D | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 11cadaca-bc98-3089-9ae3-cc64269ed284 | -3.40823 | -42.3688 | 2025-11-14 04:23:00 | NPP-375D | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 18dfaf39-eaa0-39b3-a2df-8b0de2538fd5 | -9.95421 | -44.93936 | 2025-11-14 04:23:00 | NPP-375D | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 549fab60-62f1-3c33-9cf4-bc720338c519 | -9.50143 | -47.27145 | 2025-11-14 04:23:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| ab6b3c5d-f662-309f-b7a0-f1efd6d4dca1 | -2.65403 | -47.00047 | 2025-11-14 04:23:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d271d35d-3739-37e0-a228-99e2d827b7d7 | -7.29327 | -45.46288 | 2025-11-14 04:23:00 | NPP-375D | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| fcebc004-451d-3054-b391-f14947d30644 | -4.44737 | -44.00618 | 2025-11-14 04:23:00 | NPP-375D | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| d7c9aa7c-f3c4-3987-8958-ac1eb27d9b57 | -9.1456 | -45.17675 | 2025-11-14 04:23:00 | NPP-375D | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 65a5d93d-7955-3922-9f8f-297fb00878a4 | -10.10615 | -40.8968 | 2025-11-14 04:23:00 | NPP-375D | CAMPO FORMOSO | BAHIA | Brasil | 2906006 | 29 | 33 | nan | nan | nan | Caatinga | 8.9 |
| 793c62f7-b81c-331a-99ee-95f6d9f61b74 | -4.37233 | -41.73189 | 2025-11-14 04:23:00 | NPP-375D | PIRIPIRI | PIAUÍ | Brasil | 2208403 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| e27a85e5-4259-37a5-91ec-c1e0fa238afe | -10.63553 | -44.82213 | 2025-11-14 04:23:00 | NPP-375D | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 6650a889-a013-33ea-b6ce-f35e4d09c771 | -9.22117 | -45.18862 | 2025-11-14 04:23:00 | NPP-375D | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 1b4647ef-12c6-32ea-80ac-7b9805ebd9aa | -4.71968 | -42.93842 | 2025-11-14 04:23:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| af0ae94a-a34d-315c-b025-eafb60bcd140 | -9.66891 | -43.89859 | 2025-11-14 04:23:00 | NPP-375D | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 6cf25dc5-4b73-3227-bcbe-3b7162ffb5ae | -9.95754 | -44.93989 | 2025-11-14 04:23:00 | NPP-375D | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| b8b4f268-ef7f-3b12-be7e-9df286e3a19c | -4.50258 | -43.95813 | 2025-11-14 04:23:00 | NPP-375D | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 35abbb55-dcc3-34ad-a30c-a45179501d13 | -3.45967 | -43.18301 | 2025-11-14 04:23:00 | NPP-375D | ANAPURUS | MARANHÃO | Brasil | 2100808 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| f9eda952-08b3-3f72-aa68-c8901458623e | -2.23647 | -46.07371 | 2025-11-14 04:23:00 | NPP-375D | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 09234ed6-f15c-368b-a783-be7ed9442c60 | -7.01948 | -46.43389 | 2025-11-14 04:23:00 | NPP-375D | FEIRA NOVA DO MARANHÃO | MARANHÃO | Brasil | 2104073 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| b6cffa3b-9fb1-3e7a-a7c1-605a3efd2fa3 | -3.51569 | -45.55914 | 2025-11-14 04:23:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c35d4ace-1253-372a-a700-4ea0acd82f5b | -7.93742 | -44.31538 | 2025-11-14 04:23:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 30a038ba-0e9d-3206-ae85-9abec3c9a489 | -9.35003 | -46.58882 | 2025-11-14 04:23:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c989ba71-83fa-35f8-bb03-8b99dccffdd2 | -4.41192 | -46.02739 | 2025-11-14 04:23:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| d3fe85d9-5b05-373b-9b33-6b52fcd50e59 | -7.78467 | -49.61784 | 2025-11-14 04:23:00 | NPP-375D | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| f09c8ad3-ce7c-3b0e-9856-d352b52c7207 | -2.65765 | -47.00104 | 2025-11-14 04:23:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 93c378f8-4470-32f1-8d75-f9192d82bdfd | -4.53016 | -43.39216 | 2025-11-14 04:23:00 | NPP-375D | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| fdd19b69-d870-315e-b83a-51c229d4b577 | -6.88168 | -47.24235 | 2025-11-14 04:23:00 | NPP-375D | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 5aa42010-72d8-3ae0-9532-1740aa8333b4 | -9.95699 | -44.94341 | 2025-11-14 04:23:00 | NPP-375D | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 5.2 |
| dd806016-36e7-3589-8c89-b9a4cf1ce486 | -9.31559 | -47.83521 | 2025-11-14 04:23:00 | NPP-375D | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 5.6 |
| a8760166-c34b-310f-bbd5-7769bc18e8e9 | -7.7322 | -47.25333 | 2025-11-14 04:23:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 9e9cae24-d792-3a94-9783-e97d033e37c3 | -9.65085 | -44.54032 | 2025-11-14 04:23:00 | NPP-375D | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c76438dc-11b1-3eef-be2b-eaa933606499 | -7.23186 | -46.26648 | 2025-11-14 04:23:00 | NPP-375D | NOVA COLINAS | MARANHÃO | Brasil | 2107258 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f7b602c4-835a-3da9-aab1-a57da0e927bc | -3.94193 | -38.31672 | 2025-11-14 04:23:00 | NPP-375D | AQUIRAZ | CEARÁ | Brasil | 2301000 | 23 | 33 | nan | nan | nan | Caatinga | 3.0 |
| 8a627ff4-8f24-31be-b88e-5096fec45d07 | -7.86099 | -44.30704 | 2025-11-14 04:23:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 25a34380-52a4-3ce8-8972-d53a60c8a3ee | -4.68585 | -42.81562 | 2025-11-14 04:23:00 | NPP-375D | UNIÃO | PIAUÍ | Brasil | 2211100 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e493b8a4-6145-3f61-9f72-344a2b557d44 | -3.78563 | -42.47823 | 2025-11-14 04:23:00 | NPP-375D | SÃO JOÃO DO ARRAIAL | PIAUÍ | Brasil | 2209971 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| f622884b-ebe5-362f-b8ed-8b1b9db73669 | -7.44997 | -42.576 | 2025-11-14 04:23:00 | NPP-375D | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| d4f91578-f1b5-3aea-91f5-ffd872d43803 | -2.88406 | -49.47873 | 2025-11-14 04:23:00 | NPP-375D | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 8a7ae595-565a-3613-bd3f-c29b776bcc2b | -4.0171 | -48.81122 | 2025-11-14 04:23:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 86fbf644-00dd-328c-8a3b-74579c8468b0 | -7.35648 | -43.35191 | 2025-11-14 04:23:00 | NPP-375D | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| c3d02360-3de8-36c3-b9f7-2d50b343af8f | -2.7275 | -49.56553 | 2025-11-14 04:23:00 | NPP-375D | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 3aee5a95-884d-36f5-af87-2fd0e788ea91 | -7.38505 | -48.6531 | 2025-11-14 04:23:00 | NPP-375D | ARAGUAÍNA | TOCANTINS | Brasil | 1702109 | 17 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 327e6683-47ef-382a-a0aa-31b802abaac3 | -4.71575 | -42.94149 | 2025-11-14 04:23:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 95c7e6bf-7f79-3b1a-8969-856c95a793be | -1.83639 | -53.79368 | 2025-11-14 04:23:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7d31d127-394c-3ab2-aa2f-780c53d458fb | -10.74929 | -45.06492 | 2025-11-14 04:23:00 | NPP-375D | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 99dd9d2c-1340-356a-81fd-4bff99893432 | -10.75371 | -44.91353 | 2025-11-14 04:23:00 | NPP-375D | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 0c7974df-b156-3dd8-9d5b-5fdff4ee6235 | -7.35141 | -43.36227 | 2025-11-14 04:23:00 | NPP-375D | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 48fe140b-3971-310a-ba6b-c4fbc1a52858 | -3.35802 | -45.34256 | 2025-11-14 04:23:00 | NPP-375D | MONÇÃO | MARANHÃO | Brasil | 2106904 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| f0770add-4824-3e32-9f42-37c6a7a4b87e | -10.76038 | -44.9146 | 2025-11-14 04:23:00 | NPP-375D | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 1ec0df0c-2029-3130-a868-7e8bda3cd857 | -4.90182 | -42.9072 | 2025-11-14 04:23:00 | NPP-375D | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 49b63887-41dd-3af0-b98b-1e2f594f784f | -7.15008 | -46.2943 | 2025-11-14 04:23:00 | NPP-375D | NOVA COLINAS | MARANHÃO | Brasil | 2107258 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 2137bf4d-ca04-3fc2-914c-0d7be55d09fe | -3.47329 | -45.64881 | 2025-11-14 04:23:00 | NPP-375D | GOVERNADOR NEWTON BELLO | MARANHÃO | Brasil | 2104651 | 21 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 4d749231-6f5b-368c-8730-58697415ccb9 | -3.91335 | -44.32563 | 2025-11-14 04:23:00 | NPP-375D | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| a45b5483-6cb1-3ac7-adc9-50e6eee1a253 | -4.62872 | -43.36781 | 2025-11-14 04:23:00 | NPP-375D | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 9d0af51e-bf81-3b24-91e6-26fd33d9fd26 | -2.47038 | -45.18929 | 2025-11-14 04:23:00 | NPP-375D | PINHEIRO | MARANHÃO | Brasil | 2108603 | 21 | 33 | nan | nan | nan | Amazônia | 17.3 |
| ade21651-6789-39a3-9cbb-ae91499dc789 | -2.23996 | -46.07426 | 2025-11-14 04:23:00 | NPP-375D | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 8523f867-3d01-3f0f-88ba-67fdc5eca20e | -10.44755 | -47.34064 | 2025-11-14 04:23:00 | NPP-375D | LAGOA DO TOCANTINS | TOCANTINS | Brasil | 1711951 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 8ad2e75f-03dd-372e-a6b2-b4cdec0bd604 | -3.36303 | -48.40012 | 2025-11-14 04:23:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 8014df52-658c-3c06-aa46-7e209404623b | -1.83448 | -53.79835 | 2025-11-14 04:23:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 8add4622-31ea-3e5a-9029-dde008ed6f17 | -3.31402 | -49.46689 | 2025-11-14 04:23:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c2131c2e-d1b8-3f64-a2b4-a657e2f42719 | -7.14728 | -46.29015 | 2025-11-14 04:23:00 | NPP-375D | NOVA COLINAS | MARANHÃO | Brasil | 2107258 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 34212679-b154-3f58-91f1-5143f437ef3f | -7.46801 | -42.57484 | 2025-11-14 04:23:00 | NPP-375D | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 05da87ae-353c-3f26-9053-396211c4ec00 | -2.43501 | -48.04792 | 2025-11-14 04:23:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 0ce7f8cc-783d-3731-9c2a-7a2475747cef | -4.603 | -43.29911 | 2025-11-14 04:23:00 | NPP-375D | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 3c0095f7-993a-3a6b-9cb5-d2c2e8074e8d | -9.9888 | -45.14987 | 2025-11-14 04:23:00 | NPP-375D | SÃO GONÇALO DO GURGUÉIA | PIAUÍ | Brasil | 2209757 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 83c416ad-4c04-3ecb-870e-0de3dd383af6 | -10.37666 | -47.68782 | 2025-11-14 04:23:00 | NPP-375D | SANTA TEREZA DO TOCANTINS | TOCANTINS | Brasil | 1719004 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 0a0df638-76c8-3e5a-a7ed-819ec1360994 | -5.02761 | -41.10487 | 2025-11-14 04:23:00 | NPP-375D | CRATEÚS | CEARÁ | Brasil | 2304103 | 23 | 33 | nan | nan | nan | Caatinga | 2.2 |
| af76e18e-7d36-3ddf-b1e7-5198ca176b5d | -10.73183 | -44.01844 | 2025-11-14 04:23:00 | NPP-375D | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 87026f9e-65b2-365f-b7a4-a8acfc1b4cf8 | -3.76263 | -45.08278 | 2025-11-14 04:23:00 | NPP-375D | PIO XII | MARANHÃO | Brasil | 2108702 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 295fa015-1598-3b87-a1db-64ccd14a95df | -4.01003 | -48.80489 | 2025-11-14 04:23:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a04d181c-5cb1-3ef0-9e26-1e26f93fd658 | -3.95106 | -47.49819 | 2025-11-14 04:23:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e83a5deb-de77-3989-9335-f83ae190b5cb | -10.74982 | -44.91655 | 2025-11-14 04:23:00 | NPP-375D | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d3ffbe29-fd00-3a31-bd54-c6701d93a0ed | -4.06439 | -43.06424 | 2025-11-14 04:23:00 | NPP-375D | DUQUE BACELAR | MARANHÃO | Brasil | 2103901 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 9663976c-3125-3a73-89a0-8355dbebef7c | -3.25039 | -43.28956 | 2025-11-14 04:23:00 | NPP-375D | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 259fa2ed-1204-3e42-a900-f76016ce3a4c | -5.02893 | -41.09626 | 2025-11-14 04:23:00 | NPP-375D | CRATEÚS | CEARÁ | Brasil | 2304103 | 23 | 33 | nan | nan | nan | Caatinga | 1.4 |


[Clique aqui para ver as próximas entradas](README25.md)
