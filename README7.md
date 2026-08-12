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

## Dados Diários - Página 7

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 6ad296e2-1f1f-3941-84d8-b666bc8d6808 | -21.49202 | -48.64398 | 2026-08-12 03:34:00 | NOAA-20 | TAQUARITINGA | SÃO PAULO | Brasil | 3553708 | 35 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 8271c5fb-441e-3515-b216-9653c6649277 | -21.41631 | -45.94188 | 2026-08-12 03:34:00 | NOAA-20 | ALFENAS | MINAS GERAIS | Brasil | 3101607 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| 711506bc-f8a4-3bdb-8cef-60b9268a705e | -20.94293 | -48.89682 | 2026-08-12 03:34:00 | NOAA-20 | NOVAIS | SÃO PAULO | Brasil | 3533254 | 35 | 33 | nan | nan | nan | Mata Atlântica | 28.1 |
| f4217e8c-dcaf-3ecd-b659-127a0fe755d6 | -20.962 | -47.41682 | 2026-08-12 03:34:00 | NOAA-20 | ALTINÓPOLIS | SÃO PAULO | Brasil | 3501004 | 35 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 5bfe8578-0f4b-3f7a-bc14-377c52971bb1 | -20.94817 | -48.90564 | 2026-08-12 03:34:00 | NOAA-20 | NOVAIS | SÃO PAULO | Brasil | 3533254 | 35 | 33 | nan | nan | nan | Mata Atlântica | 28.1 |
| 82876ab6-a97a-324a-b458-e32b1ca6739e | -20.93931 | -48.91119 | 2026-08-12 03:34:00 | NOAA-20 | NOVAIS | SÃO PAULO | Brasil | 3533254 | 35 | 33 | nan | nan | nan | Mata Atlântica | 22.0 |
| d9139eba-46b2-319d-95ed-44eaa641e60c | -20.94627 | -48.9132 | 2026-08-12 03:34:00 | NOAA-20 | NOVAIS | SÃO PAULO | Brasil | 3533254 | 35 | 33 | nan | nan | nan | Mata Atlântica | 22.0 |
| bf1b7a52-fce5-3afc-a7f5-1c2b24a51223 | -8.9601 | -60.5165 | 2026-08-12 03:40:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 74.1 |
| b84e4e8f-10e2-3f65-abc4-ed584ea5a477 | -11.9719 | -46.3871 | 2026-08-12 03:40:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 62.0 |
| 145f4702-7029-3d27-9657-853e8d0c9a2a | -11.4869 | -44.5763 | 2026-08-12 03:40:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 123.5 |
| 73d09d24-2c60-3c9d-93de-efdf801b00dd | -11.4677 | -44.5791 | 2026-08-12 03:40:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 70.0 |
| 5d87bbab-f2a2-3155-8ac1-e56071ea9b94 | -20.9622 | -48.8894 | 2026-08-12 03:40:00 | GOES-19 | NOVAIS | SÃO PAULO | Brasil | 3533254 | 35 | 33 | nan | nan | nan | Mata Atlântica | 100.1 |
| 008e670e-579a-3ac0-811f-b34c94c2e2ff | -8.96 | -60.5358 | 2026-08-12 03:40:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 75.5 |
| b8e42b54-5b16-36cf-a930-12eeffa1b99e | -11.9535 | -46.3444 | 2026-08-12 03:40:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 74.8 |
| 3b112a92-3dc0-310a-a0b0-eb4449995e75 | -11.4873 | -44.553 | 2026-08-12 03:40:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 76.7 |
| db74b637-d8d7-3fa5-b316-15ef60f23776 | -6.6013 | -59.0037 | 2026-08-12 03:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 55.3 |
| a1a55d80-b7b4-3c21-a726-e9352979f508 | -11.4681 | -44.5558 | 2026-08-12 03:40:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 74.5 |
| 9a9469f1-4f0c-33a9-b54e-fc2a553212a0 | -11.9535 | -46.3444 | 2026-08-12 03:50:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 62.4 |
| 92bce435-ed44-3d25-b06b-d05d9aa74767 | -13.2943 | -49.709 | 2026-08-12 03:50:00 | GOES-19 | NOVO PLANALTO | GOIÁS | Brasil | 5215256 | 52 | 33 | nan | nan | nan | Cerrado | 71.7 |
| d4241868-ff86-391a-b99b-f43b9024b6b7 | -11.4869 | -44.5763 | 2026-08-12 03:50:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 84.9 |
| 1b11dcae-3ad2-3778-a1c7-87e382d66dff | -8.96 | -60.5358 | 2026-08-12 03:50:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 79.3 |
| 5b92a0eb-8a6d-3e43-af61-2acb44cab102 | -13.3135 | -49.7064 | 2026-08-12 03:50:00 | GOES-19 | NOVO PLANALTO | GOIÁS | Brasil | 5215256 | 52 | 33 | nan | nan | nan | Cerrado | 59.6 |
| d953d60d-c6a0-3fbc-9f9a-5c17d67ea220 | -8.9601 | -60.5165 | 2026-08-12 03:50:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 76.4 |
| 60419d40-7852-3f14-9f8b-6594963a5203 | -11.4677 | -44.5791 | 2026-08-12 03:50:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 74.0 |
| ee9d066b-d5ef-3661-8357-48f3bb322ae2 | -11.4681 | -44.5558 | 2026-08-12 03:50:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 69.9 |
| 5e27d08b-69cc-3eef-9cfb-2d09442f3dbc | -11.4873 | -44.553 | 2026-08-12 03:50:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 62.8 |
| 93afd200-e7c5-3271-82bd-e31cc49b97f7 | -8.96 | -60.5358 | 2026-08-12 04:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 83.2 |
| cc0948c1-3802-39ec-bb3a-e0ab2f108a94 | -11.4873 | -44.553 | 2026-08-12 04:00:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 61.5 |
| 498dd561-03f9-3b98-91a1-baf856eb1663 | -11.9719 | -46.3871 | 2026-08-12 04:00:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 68.6 |
| 706a0ee9-fc24-30e7-a5bc-3437539ce941 | -11.4869 | -44.5763 | 2026-08-12 04:00:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 64.2 |
| e4a35946-f788-3458-a35b-8df39ab49649 | -8.9601 | -60.5165 | 2026-08-12 04:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 75.0 |
| c6f8775c-a84c-31e5-bee3-db88e88d978d | -11.4681 | -44.5558 | 2026-08-12 04:00:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 63.1 |
| 09f0ce4b-7810-3bde-bd86-1eb479af8f6f | -11.4677 | -44.5791 | 2026-08-12 04:00:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 56.2 |
| bc2abc83-6674-3f75-8025-6843a6ad18bf | -13.2943 | -49.709 | 2026-08-12 04:00:00 | GOES-19 | NOVO PLANALTO | GOIÁS | Brasil | 5215256 | 52 | 33 | nan | nan | nan | Cerrado | 63.6 |
| 1c78ffa7-2804-3376-bfbc-6868fd58d22f | -13.3135 | -49.7064 | 2026-08-12 04:00:00 | GOES-19 | NOVO PLANALTO | GOIÁS | Brasil | 5215256 | 52 | 33 | nan | nan | nan | Cerrado | 51.7 |
| f03ab7ac-156f-3479-b4b7-3eeb4133b0bd | -11.4681 | -44.5558 | 2026-08-12 04:10:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 51.6 |
| f8e02eaf-6bbf-3061-b6ae-eda38f690ed0 | -11.4869 | -44.5763 | 2026-08-12 04:10:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 67.0 |
| eab81377-fbf4-31d6-906e-cecf5a8b8137 | -11.4873 | -44.553 | 2026-08-12 04:10:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 61.5 |
| 0dafa3f9-7494-3e3a-93e3-139272c93440 | -11.9911 | -46.3844 | 2026-08-12 04:10:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 68.6 |
| d165c431-8d86-3012-ade2-414f75dfdf6a | -3.15435 | -54.60548 | 2026-08-12 04:14:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 9caa40a4-1081-3f3a-b14f-63d2e796a7b0 | -5.80708 | -47.1279 | 2026-08-12 04:14:00 | NOAA-21 | MONTES ALTOS | MARANHÃO | Brasil | 2107001 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 40e44648-b996-3e40-87ef-5a0ea5f56818 | -8.6827 | -44.30533 | 2026-08-12 04:14:00 | NOAA-21 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 0.6 |
| ecbd28a2-4f57-340a-9d18-569192f5cf34 | -6.54172 | -43.12114 | 2026-08-12 04:14:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 090d447d-bda2-33e4-870a-4b6c5bd4eb8e | -6.53788 | -43.12408 | 2026-08-12 04:14:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 757253c8-c541-3661-b054-5a0f2e816e58 | -7.37102 | -42.84034 | 2026-08-12 04:14:00 | NOAA-21 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| dfd69add-82e7-3d56-8c1a-96e47cb11338 | -8.42019 | -49.48869 | 2026-08-12 04:14:00 | NOAA-21 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| aae8544b-aa7c-38ab-8eea-dc07594b66e3 | -7.60556 | -42.7521 | 2026-08-12 04:14:00 | NOAA-21 | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| cf5e86c1-8223-3a9d-8058-08ece92d59a1 | -8.47851 | -45.40944 | 2026-08-12 04:14:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 59b7eca3-883c-36b7-b93b-13552e8fff27 | -8.62485 | -47.45424 | 2026-08-12 04:14:00 | NOAA-21 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 53e12f3c-dff1-390b-b94d-0f221162f2e7 | -6.89486 | -41.93657 | 2026-08-12 04:14:00 | NOAA-21 | SÃO JOÃO DA VARJOTA | PIAUÍ | Brasil | 2209955 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 3b4abd9e-96e9-3857-aa5f-96c2a69b01fd | -5.64027 | -47.1041 | 2026-08-12 04:14:00 | NOAA-21 | BURITIRANA | MARANHÃO | Brasil | 2102358 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| da9ced15-53c1-3977-ac5f-fc951ce30949 | -4.71968 | -42.7675 | 2026-08-12 04:14:00 | NOAA-21 | UNIÃO | PIAUÍ | Brasil | 2211100 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 66cd3b1b-6460-3282-ba28-744d77dedfe7 | -8.60115 | -45.41029 | 2026-08-12 04:14:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 6.8 |
| c4ba85c5-c4dd-310f-b42e-32bb1c61d2fe | -8.36972 | -47.74943 | 2026-08-12 04:14:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 8b04eeb5-e7ab-3d4c-b054-79c6e43d5a56 | -8.26892 | -46.35488 | 2026-08-12 04:14:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 7ef4c491-4788-3237-be48-923a4673fb33 | -7.01717 | -44.61816 | 2026-08-12 04:14:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 3414f0a2-0bb2-3342-b12a-7ae5c1d32b97 | -1.82968 | -54.50673 | 2026-08-12 04:14:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 5b5bd753-3816-3ea3-a963-8ea03b89cb5b | -6.61114 | -41.81632 | 2026-08-12 04:14:00 | NOAA-21 | INHUMA | PIAUÍ | Brasil | 2204709 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 18a01c71-ebd1-34dd-bb83-9ac7d30888ee | -3.84425 | -49.03796 | 2026-08-12 04:14:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| a27ff9ed-e518-3d24-816f-cf54e175e2c0 | -3.84911 | -49.09274 | 2026-08-12 04:14:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 01dd2939-5f09-3026-b0b2-86f84752c967 | -6.89323 | -41.94725 | 2026-08-12 04:14:00 | NOAA-21 | SÃO JOÃO DA VARJOTA | PIAUÍ | Brasil | 2209955 | 22 | 33 | nan | nan | nan | Caatinga | 4.9 |
| 29df554a-e6c0-3378-810b-5a5c13b30e69 | -7.91135 | -45.11211 | 2026-08-12 04:14:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 6ef3bd57-839b-3ed7-b0cf-63fdd54a1e48 | -6.99459 | -42.0174 | 2026-08-12 04:14:00 | NOAA-21 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 18883b46-b613-372c-a2e5-35aedd16c750 | -8.60513 | -45.4072 | 2026-08-12 04:14:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 4c3cf2b0-0892-3df2-a4e9-4cd04f5baafc | -8.07653 | -44.84568 | 2026-08-12 04:14:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.3 |
| fb5212cc-5417-3381-8b86-f05a92afa0d8 | -4.66264 | -43.13263 | 2026-08-12 04:14:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c8281639-03ba-3f8c-9615-135e1b233a2c | -6.5461 | -43.11475 | 2026-08-12 04:14:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 4c7bf455-a93e-3f42-816f-9f8e2de31d2d | -6.8523 | -46.00755 | 2026-08-12 04:14:00 | NOAA-21 | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 369b6e38-90ce-330b-a6f4-03f8030f579d | -8.4405 | -46.88676 | 2026-08-12 04:14:00 | NOAA-21 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ca9b496b-cab3-399f-8239-69ed34b3ee0a | -7.01603 | -44.62531 | 2026-08-12 04:14:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a641cc09-b56a-32e2-82c8-bf184c6dfc65 | -6.7721 | -42.66809 | 2026-08-12 04:14:00 | NOAA-21 | FRANCISCO AYRES | PIAUÍ | Brasil | 2204105 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 70146c8e-df04-3a1b-99db-45591435a0c2 | -7.21438 | -42.95066 | 2026-08-12 04:14:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 0.5 |
| a9b8d882-d361-33ab-92e2-c08209c0bac9 | -8.64218 | -45.85008 | 2026-08-12 04:14:00 | NOAA-21 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 3164f449-59a8-38be-8828-690245b97dbc | -7.91811 | -45.11319 | 2026-08-12 04:14:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 3.3 |
| fe66f217-83f9-3e0a-8590-e34109e1a75e | -2.69069 | -48.20358 | 2026-08-12 04:14:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e915c94a-d353-30c3-b554-0fa34c9f82e5 | -8.35459 | -45.98126 | 2026-08-12 04:14:00 | NOAA-21 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 5.2 |
| c6807688-aca2-33d4-9803-1abae9a76889 | -2.68912 | -48.20774 | 2026-08-12 04:14:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 5f3e58ec-d2a0-30d7-9689-c503577f9a2e | -6.85647 | -46.00423 | 2026-08-12 04:14:00 | NOAA-21 | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 62d6e939-0694-36e6-8026-918c3e32828a | -8.47552 | -45.42785 | 2026-08-12 04:14:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 2c40e3f2-0d3f-3446-aee4-64bc9000e669 | -2.48567 | -48.01919 | 2026-08-12 04:14:00 | NOAA-21 | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 5167c50a-9359-3cca-9ef4-33bcb8564883 | -8.62595 | -45.86282 | 2026-08-12 04:14:00 | NOAA-21 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 97f20cb1-8407-3048-b3c5-362838adcf6d | -8.7818 | -45.79119 | 2026-08-12 04:14:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 5cff17e1-c2dc-38a0-a4d1-23a7c948c565 | -6.99124 | -42.0169 | 2026-08-12 04:14:00 | NOAA-21 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 0.6 |
| d90f7a1f-5136-3800-823b-cc07898a9f64 | -7.01267 | -44.62479 | 2026-08-12 04:14:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 4.9 |
| afb2e700-e090-36f0-b35b-4663fb9c8998 | -6.85611 | -46.00501 | 2026-08-12 04:14:00 | NOAA-21 | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 5e2c212f-b6d0-32ba-ac21-558681121e3d | -4.11169 | -50.44637 | 2026-08-12 04:14:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 089d8a94-432d-36b9-bf08-7230868cbd03 | -8.07537 | -46.51522 | 2026-08-12 04:14:00 | NOAA-21 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 5.2 |
| c14eac04-8cbd-3736-a3c3-b400e29b6776 | -6.77367 | -38.76486 | 2026-08-12 04:14:00 | NOAA-21 | IPAUMIRIM | CEARÁ | Brasil | 2305704 | 23 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 7c33993e-386e-3653-ae7e-6792b3f10700 | -8.0747 | -46.51928 | 2026-08-12 04:14:00 | NOAA-21 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 5.2 |
| a35b34d4-1498-39a9-b203-226921a4eb03 | -7.00415 | -44.83034 | 2026-08-12 04:14:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| b5da3942-2d76-3ab2-8128-0025ed52274e | -5.73929 | -44.50418 | 2026-08-12 04:14:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 063029cf-1219-389f-a1b1-55a44552621a | -8.11079 | -47.18071 | 2026-08-12 04:14:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| f3a033e8-25c9-3b3f-a3f1-aa7601e83bed | -6.33967 | -44.06349 | 2026-08-12 04:14:00 | NOAA-21 | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 8.9 |
| 15c67066-dd2e-31c2-9716-16d7a43cc94f | -5.71786 | -44.31366 | 2026-08-12 04:14:00 | NOAA-21 | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 5dffdc5e-ef03-344d-842c-9b493ea41194 | -7.39154 | -42.86135 | 2026-08-12 04:14:00 | NOAA-21 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| d0926058-8b6b-399a-814f-8fcc117f4dcd | -8.07613 | -46.51646 | 2026-08-12 04:14:00 | NOAA-21 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 215ba30e-b13f-34a5-b513-57ffc5440b58 | -8.49488 | -45.41602 | 2026-08-12 04:14:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 0f7ddd85-ce5e-3c16-8f43-596830e94105 | -3.96321 | -43.10397 | 2026-08-12 04:14:00 | NOAA-21 | BURITI | MARANHÃO | Brasil | 2102200 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| fafdf45a-41ae-35dc-ba30-c52880396549 | -6.85584 | -46.00809 | 2026-08-12 04:14:00 | NOAA-21 | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 96e44291-7851-3ec7-8028-770efd448827 | -7.00083 | -42.63972 | 2026-08-12 04:14:00 | NOAA-21 | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |


[Clique aqui para ver as próximas entradas](README8.md)
