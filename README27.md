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

## Dados Diários - Página 27

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 7b4183ad-76c2-3985-91d1-3645ac854b05 | -11.46432 | -44.56483 | 2026-08-12 05:10:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| b88222df-ce64-3965-9b46-06cf71c9c683 | -8.943 | -60.50242 | 2026-08-12 05:10:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9474a4a5-8392-326b-b06d-1cb192821846 | -8.97672 | -60.53463 | 2026-08-12 05:10:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 2252efa5-f308-3d0c-9605-821b10042444 | -11.47511 | -44.5742 | 2026-08-12 05:10:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 8.7 |
| 7d131b6c-0435-3c52-bdd8-d623cbc41e7c | -7.40157 | -59.99224 | 2026-08-12 05:10:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 77c0f8d1-fa6d-358a-90e5-83f3eb4f5e9e | -11.60883 | -54.64981 | 2026-08-12 05:10:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7b0c1ea0-04c5-3e06-9d94-d76a62cfc9be | -9.13227 | -46.39383 | 2026-08-12 05:10:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 2d9cf3d8-c7e1-34b9-b9ec-1774b7015675 | -8.95155 | -60.56828 | 2026-08-12 05:10:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 32e986ce-0058-3d6b-95b5-f079eb7e6cb9 | -10.22437 | -45.93555 | 2026-08-12 05:10:00 | NOAA-20 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 60a5391c-a8cc-3ad4-b403-0c51a6246af1 | -9.13651 | -46.39067 | 2026-08-12 05:10:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 56e623eb-1792-3aa2-ad54-8992efd583e8 | -6.04395 | -43.86561 | 2026-08-12 05:10:00 | NOAA-20 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 3c244664-8443-3a3e-8378-8215ba5321de | -6.33531 | -44.06394 | 2026-08-12 05:10:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 1e39a08f-42ca-35b5-b347-b2d35bea5656 | -8.95493 | -60.54708 | 2026-08-12 05:10:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 663c9bfd-4d1b-3c82-b649-2bd638251a6b | -7.41057 | -60.0075 | 2026-08-12 05:10:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3e95db17-7837-3564-8054-b846e939eedf | -8.96087 | -60.53667 | 2026-08-12 05:10:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| aa6b60c2-11eb-38fd-a5d3-f5c8895b9379 | -6.59928 | -59.00628 | 2026-08-12 05:10:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 96fc4550-07e1-308d-9a78-bbdbe90185e3 | -8.98533 | -60.5978 | 2026-08-12 05:10:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| da4f1bf4-3ccd-39e9-8b65-6cb8b8a11be2 | -11.61114 | -54.65825 | 2026-08-12 05:10:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4fa6e312-5f22-31a2-a56b-4dfa8d70692d | -8.95481 | -60.59466 | 2026-08-12 05:10:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d4c6b97c-2c7c-3289-9cee-db4c929fea04 | -11.48413 | -44.56721 | 2026-08-12 05:10:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 13.1 |
| 821839b7-4cc6-37ec-8cb6-0a2a3ab6af38 | -11.82665 | -51.84215 | 2026-08-12 05:10:00 | NOAA-20 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 0debd6ce-2c18-3904-ba5b-b933d86c5cfb | -10.22504 | -45.93024 | 2026-08-12 05:10:00 | NOAA-20 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 28aa0cc1-6ecb-3713-bb84-d31eae2a4adf | -9.13177 | -46.3978 | 2026-08-12 05:10:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 3e66d147-3864-374e-9b89-0a3be51c28e8 | -11.21771 | -54.82816 | 2026-08-12 05:10:00 | NOAA-20 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 08b5f44e-9e6c-39f2-9c71-100915e1ca0f | -11.94604 | -46.35921 | 2026-08-12 05:10:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 9874437c-b731-393f-ba0e-f91eab2a0600 | -8.60128 | -45.40781 | 2026-08-12 05:10:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| cb1b49f1-d98e-33fd-b1ae-67b6be51ccc9 | -11.79225 | -51.84844 | 2026-08-12 05:10:00 | NOAA-20 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d21538c0-211e-3cb8-acb1-8cde103426da | -7.42047 | -60.00167 | 2026-08-12 05:10:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 37fa8ee7-f3db-33de-8ebc-c88e054d260b | -7.00224 | -44.82988 | 2026-08-12 05:10:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| fd73c9fa-4820-34e0-9016-096bcf8632a0 | -8.89294 | -60.56971 | 2026-08-12 05:10:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b85b3c17-292d-3a58-82b7-6dc69e15ff2d | -8.89359 | -60.58887 | 2026-08-12 05:10:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 4b3f3bcc-ca1d-3791-8a82-0e9dfe29a279 | -6.60526 | -59.00641 | 2026-08-12 05:10:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 619a0244-0645-3d22-a081-aae371bdcce0 | -11.82559 | -51.84957 | 2026-08-12 05:10:00 | NOAA-20 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 01f35325-66aa-3df7-bc76-137ea72d9b15 | -6.60169 | -59.00582 | 2026-08-12 05:10:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 03c82b9c-1e39-327a-bab2-fa9914ba380e | -9.34245 | -47.50021 | 2026-08-12 05:10:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| c384bf70-93f1-39d0-8129-5d71dc2ea3b9 | -8.95804 | -60.50499 | 2026-08-12 05:10:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| d934761e-d8af-3ccb-949d-96d6ba7920bc | -7.68954 | -55.16676 | 2026-08-12 05:10:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 5ea4c1d4-3bb6-395f-9c76-65a4aac0eeb3 | -6.05039 | -43.86642 | 2026-08-12 05:10:00 | NOAA-20 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 2e77f3c9-b2d7-3074-932c-9dd8e3937f20 | -10.22555 | -45.92623 | 2026-08-12 05:10:00 | NOAA-20 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 3.1 |
| c0e3de63-100b-3ab1-8d1a-42e384541b44 | -6.59861 | -59.0104 | 2026-08-12 05:10:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 6f98e466-337a-3f9d-a996-cf8dfa8b6e57 | -8.89216 | -60.57433 | 2026-08-12 05:10:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0c93e040-3f4c-3dd3-b0f9-1340b794001f | -8.89893 | -60.58026 | 2026-08-12 05:10:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ddc9995b-09eb-3d61-bb5f-3938220da1d5 | -10.84112 | -50.35139 | 2026-08-12 05:10:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 72098c62-98a1-3dd2-b772-adbc0cb96605 | -8.36766 | -47.75117 | 2026-08-12 05:10:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| dfe02f08-90e5-3706-8ffe-ecfebb1d90ad | -8.95809 | -60.50786 | 2026-08-12 05:10:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 4485b2c7-6605-35e0-b285-efdf9588ea01 | -11.47024 | -44.57138 | 2026-08-12 05:10:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 3.3 |
| c9e6a4c7-33dc-3fc3-9e0b-c8858099cbf5 | -11.60765 | -54.65771 | 2026-08-12 05:10:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 68da418c-41c9-3656-ab8e-f0abf0aac758 | -9.13799 | -46.39459 | 2026-08-12 05:10:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 4420cfb9-95ed-3b39-8755-f5071e3cbc14 | -8.9573 | -60.51242 | 2026-08-12 05:10:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.2 |
| b4456890-5b0a-3c3e-adb9-e6fc88568660 | -11.97846 | -46.39023 | 2026-08-12 05:10:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| f4103bb3-3fe2-326a-8c76-3451931b1245 | -9.33937 | -47.52359 | 2026-08-12 05:10:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| fb212415-fb42-3ae6-93e0-e50d6fb3eae3 | -11.82255 | -51.84153 | 2026-08-12 05:10:00 | NOAA-20 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 535c92a8-4df9-33ef-8415-13a62eeba47b | -7.45377 | -46.15279 | 2026-08-12 05:10:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 6a41ade5-1472-3cc9-b4ea-d8933d85f544 | -9.34865 | -47.49434 | 2026-08-12 05:10:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 77c27d17-477f-3074-ac43-e2899c00ea26 | -11.47576 | -44.56844 | 2026-08-12 05:10:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 8.7 |
| 7cf45f2d-fa87-3807-bfae-b785fbce1452 | -6.60285 | -59.00688 | 2026-08-12 05:10:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 0a352a22-3faa-3509-8ad2-e065e36fdc93 | -11.94849 | -46.33876 | 2026-08-12 05:10:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 12.6 |
| 83b3841c-46d2-3967-8265-9d98af3b904a | -9.13545 | -46.39855 | 2026-08-12 05:10:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 5.0 |
| aac66634-bbfe-37cb-a781-869ea9f7f292 | -11.4698 | -44.56189 | 2026-08-12 05:10:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 6a90ad8c-8922-360f-a4f3-ad939485fd39 | -9.35044 | -47.48081 | 2026-08-12 05:10:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 5ff06a93-4f64-3262-a803-f1bd81d102a7 | -7.40757 | -60.00238 | 2026-08-12 05:10:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 1039665a-ab4f-3e9f-befc-488c1176ba30 | -10.09886 | -46.21898 | 2026-08-12 05:10:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 1afee3e9-0545-34d2-9439-8adb445ff7ce | -8.89672 | -60.57037 | 2026-08-12 05:10:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ddb1c19e-7bc7-36e0-8a7a-994175d26b15 | -9.45445 | -51.81674 | 2026-08-12 05:10:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8aa6631d-4b58-3da1-8b34-7badf0635373 | -9.37133 | -47.44625 | 2026-08-12 05:10:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| bbd0412f-e633-3cac-8d31-1d51a7f37b76 | -10.82298 | -50.33281 | 2026-08-12 05:10:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| c5628578-b740-3c2d-aa6b-6e33253dea07 | -11.9539 | -46.34402 | 2026-08-12 05:10:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 7.1 |
| a98e8903-52e1-3181-a177-75f178d08638 | -7.9199 | -45.1143 | 2026-08-12 05:10:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| d84df7fb-33c8-3952-b800-3f3b8db2cfea | -8.36723 | -47.75429 | 2026-08-12 05:10:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 37904f7d-3bb8-3407-a603-57ab0729784b | -4.45568 | -55.66586 | 2026-08-12 05:10:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 85f6e450-249c-36f9-b9dc-e2f00810dfcd | -11.60238 | -54.66897 | 2026-08-12 05:10:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 45a93b87-9d89-3ec5-bcb1-a3683a82beb6 | -11.98996 | -46.37288 | 2026-08-12 05:10:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| e1b1addd-166d-37e1-aa6e-63d945fe7612 | -8.94517 | -60.53587 | 2026-08-12 05:10:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 5ce00804-a303-3d6c-be8a-d9d4f0830a52 | -9.34421 | -47.48688 | 2026-08-12 05:10:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| b0e96697-39a9-3de9-94e8-4959485f234e | -9.47621 | -60.51825 | 2026-08-12 05:10:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 59b610ef-4911-3948-baf4-d976ed8c9284 | -11.22807 | -54.85343 | 2026-08-12 05:10:00 | NOAA-20 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 6f0739fd-c2b9-3e35-9a02-59efb57f195f | -11.97897 | -46.38604 | 2026-08-12 05:10:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 9e8d6305-6ef9-3dc4-9268-f1f2c2644ff8 | -11.60646 | -54.66558 | 2026-08-12 05:10:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| fedb210a-5f97-3706-b8fa-0735371dc41b | -7.4113 | -60.00299 | 2026-08-12 05:10:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 33715ab0-66fe-3ff3-88d6-46266c11240a | -5.67899 | -49.82751 | 2026-08-12 05:10:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 125ee304-1d63-366a-9e94-83f80bfbdd69 | -8.95046 | -60.52731 | 2026-08-12 05:10:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 524a156c-3104-3d75-90be-3db25f97e383 | -11.81184 | -51.8284 | 2026-08-12 05:10:00 | NOAA-20 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3f473075-afbe-3a33-a491-ab235f59fdad | -8.95966 | -60.49874 | 2026-08-12 05:10:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| ee03c99a-2af1-31eb-a3e5-f3597a6fbbbc | -11.8905 | -45.82933 | 2026-08-12 05:10:00 | NOAA-20 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| aba8f8b4-0e5f-3ce4-9948-74e27fb0064e | -11.49355 | -54.60081 | 2026-08-12 05:10:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| a8df0d5f-af4e-35f2-895e-b289749061da | -8.59931 | -45.40907 | 2026-08-12 05:10:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 41cad4d3-e7e7-30b9-b64b-8ce1c9480f08 | -11.60824 | -54.65376 | 2026-08-12 05:10:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9511de5b-5514-3a8e-b11f-f3144c1a25ee | -9.06797 | -60.40524 | 2026-08-12 05:10:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 80e90c71-e3fd-39eb-9702-821ddcacabea | -11.82917 | -51.85386 | 2026-08-12 05:10:00 | NOAA-20 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| dcb28c6c-af1e-3355-a44b-3ddeeb6cee89 | -6.04268 | -43.86567 | 2026-08-12 05:10:00 | NOAA-20 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 867596d3-440d-32af-af82-537585f79a42 | -10.84171 | -50.34689 | 2026-08-12 05:10:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 6.9 |
| a9eae0b9-708f-3485-b70d-5f98caeb6437 | -9.0717 | -60.40589 | 2026-08-12 05:10:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3c89a5cb-e29b-3f8a-8fcc-ac3513f3f294 | -11.98676 | -46.37164 | 2026-08-12 05:10:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 11133749-1cd5-3833-92a8-ef3012684f7f | -8.95487 | -60.57082 | 2026-08-12 05:10:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 5a57bebc-5051-3898-8cbb-00bac7f43df3 | -11.78351 | -51.85109 | 2026-08-12 05:10:00 | NOAA-20 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 7f8a47ef-ddb8-3443-92f4-2d6280ec449a | -6.04195 | -43.8709 | 2026-08-12 05:10:00 | NOAA-20 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| a27edda8-bf95-3d06-ba8b-30579beca785 | -10.46785 | -46.61848 | 2026-08-12 05:10:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| fadc17ad-577e-3259-991b-d4166489cbb4 | -12.02847 | -47.80096 | 2026-08-12 05:10:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 065a6199-c7d0-3443-bc90-28913be5b2e7 | -10.21859 | -45.93327 | 2026-08-12 05:10:00 | NOAA-20 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 4.2 |
| e2e5481f-7f46-3c9a-9fbc-efc5c4d17612 | -6.34166 | -44.06511 | 2026-08-12 05:10:00 | NOAA-20 | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |


[Clique aqui para ver as próximas entradas](README28.md)
