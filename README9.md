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
| ffd763f0-7620-34d4-8723-d588fdc588e3 | -6.6977 | -45.586102 | 2026-09-28 00:55:00 | METOP-C | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| c5bb2350-3eb9-3204-b446-66f7c937d3a6 | -13.4603 | -48.587799 | 2026-09-28 00:55:00 | METOP-C | TROMBAS | GOIÁS | Brasil | 5221452 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 07b16f1f-b21b-3903-bebb-4aad4c1ec57e | -3.144 | -54.087502 | 2026-09-28 00:55:00 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| dbeed9bf-b164-371c-b999-e7f1da018312 | -11.3741 | -43.432701 | 2026-09-28 00:55:00 | METOP-C | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| e7db5fed-a4b9-31f5-8502-150f6f5fdf7e | -2.7715 | -49.496101 | 2026-09-28 00:55:00 | METOP-C | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ca7ccd86-ec30-30f4-9fa6-3e38cc50f103 | -2.7813 | -49.4939 | 2026-09-28 00:55:00 | METOP-C | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b6497df2-6482-35d5-bbb8-6088232e79a1 | -11.375 | -43.396099 | 2026-09-28 00:55:00 | METOP-C | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 763bacc7-dce7-3da8-8b9d-39599c0b1ad4 | -14.714 | -45.5723 | 2026-09-28 00:55:00 | METOP-C | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 2fe032fc-8509-3c38-803a-955cd4e60764 | -2.7269 | -54.2024 | 2026-09-28 00:55:00 | METOP-C | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 97ac8bd7-f5fa-3690-aed7-3b0eae8a29a3 | -17.8265 | -44.384499 | 2026-09-28 00:55:00 | METOP-C | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 31a80a9d-e99d-3b8b-94ab-30126df1a221 | -9.8233 | -45.254799 | 2026-09-28 00:55:00 | METOP-C | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| d99d8277-0aac-3062-b5d4-965e03781121 | -1.2284 | -54.099701 | 2026-09-28 00:55:00 | METOP-C | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| cc62ebb8-185c-3a8a-a55d-13b59d9b3da6 | -9.9831 | -45.357201 | 2026-09-28 00:55:00 | METOP-C | SÃO GONÇALO DO GURGUÉIA | PIAUÍ | Brasil | 2209757 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 16e52c64-5475-3677-8b11-ec575975c563 | -12.7422 | -47.7896 | 2026-09-28 00:55:00 | METOP-C | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| ff962661-2d6d-3347-b855-c613e53f3819 | -2.0578 | -56.865601 | 2026-09-28 00:55:00 | METOP-C | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 7033afc5-a2f9-3584-87ad-65d3bd1f64bd | -12.8716 | -44.795898 | 2026-09-28 00:55:00 | METOP-C | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 6fc5c0fc-4e70-3255-b51e-e9c477927330 | -3.2402 | -50.5751 | 2026-09-28 00:55:00 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 919b68cd-0063-38f1-81c2-97984366e66b | -11.4424 | -44.913101 | 2026-09-28 00:55:00 | METOP-C | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| a87af91f-d05a-3145-9c97-bfa5cc594b59 | -11.0661 | -49.478001 | 2026-09-28 00:55:00 | METOP-C | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| c3d9223b-4217-3ecc-b232-d87935b629cb | -1.9335 | -52.1451 | 2026-09-28 00:55:00 | METOP-C | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4faaca8f-c6dc-3d41-bcc8-05fc279a2d23 | -12.2039 | -50.371799 | 2026-09-28 00:55:00 | METOP-C | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 1390d3ff-aea7-3da3-aaa2-0c4e319e5b4b | -21.5191 | -45.110901 | 2026-09-28 00:55:00 | METOP-C | CARMO DA CACHOEIRA | MINAS GERAIS | Brasil | 3113909 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| bde4b127-edf9-34c0-bcfe-82adbd51c8b9 | -10.918 | -50.703201 | 2026-09-28 00:55:00 | METOP-C | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 8270b81d-df01-3b28-82cc-46f39f125e1f | -20.195499 | -48.575401 | 2026-09-28 00:55:00 | METOP-C | GUAÍRA | SÃO PAULO | Brasil | 3517406 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 1c57ea24-f053-331c-b844-35fa07291f21 | -13.105 | -47.407398 | 2026-09-28 00:55:00 | METOP-C | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 445c080d-1224-30a5-8cef-c4f2072f918d | -9.1701 | -45.783199 | 2026-09-28 00:55:00 | METOP-C | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 395d4364-01bd-34ef-b0f9-3ff04fd0f6bf | -11.4521 | -44.910599 | 2026-09-28 00:55:00 | METOP-C | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 6731a747-12b8-3ac0-9e0e-ac1a8cf17902 | -2.7798 | -57.6884 | 2026-09-28 00:55:00 | METOP-C | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 5bbad693-b7ec-3263-9d53-cc709209b49d | -9.3245 | -45.3661 | 2026-09-28 00:55:00 | METOP-C | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 51c5454e-d4e0-3eb1-90b6-c1a444fd94c7 | -13.584 | -51.448898 | 2026-09-28 00:55:00 | METOP-C | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 58d1eed2-2629-38ce-b46a-346b1ba13d2b | -11.6952 | -44.523201 | 2026-09-28 00:55:00 | METOP-C | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 02ac8c00-9a83-3819-b92e-6cccff72fa0b | -12.6907 | -45.021801 | 2026-09-28 00:55:00 | METOP-C | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 0452f87d-78e1-3dd1-b0f9-5a769cc6c7e5 | -12.6367 | -47.310699 | 2026-09-28 00:55:00 | METOP-C | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| cd8c3143-d785-390a-8caf-31f4d4b986a0 | -8.0363 | -54.906502 | 2026-09-28 00:55:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b13f4454-f519-3721-ae0b-476926b88b97 | -14.7167 | -45.583302 | 2026-09-28 00:55:00 | METOP-C | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 25058181-baa7-3634-ace0-032499562e54 | -15.2817 | -47.68 | 2026-09-28 00:55:00 | METOP-C | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| f84c2f08-71df-30a4-8ee5-9a8ac308b3de | -12.741 | -47.314201 | 2026-09-28 00:55:00 | METOP-C | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 0adbb39d-f5ad-3d89-a94b-fd15be09ed53 | -2.9958 | -54.745998 | 2026-09-28 00:55:00 | METOP-C | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a35bd6a2-8822-3ec2-9641-1a79be944c58 | -3.2116 | -51.0284 | 2026-09-28 00:55:00 | METOP-C | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 72df3d3b-7302-3b27-bff1-f7a90687dc1e | -5.1256 | -45.765301 | 2026-09-28 00:55:00 | METOP-C | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 8b6885bf-27f2-3aee-8da4-9decd5912e18 | -2.6655 | -56.460098 | 2026-09-28 00:55:00 | METOP-C | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1c308573-1b57-3823-a24e-8b6fe7f63805 | -6.6997 | -45.971802 | 2026-09-28 00:55:00 | METOP-C | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| cb20f0f7-6466-356b-af84-b6865a04f8b3 | -2.0479 | -56.867699 | 2026-09-28 00:55:00 | METOP-C | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| d42cfea0-5a85-37ef-bfca-d5e4e5b176b4 | -11.3352 | -54.1147 | 2026-09-28 00:55:00 | METOP-C | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| bf48e6db-348c-3bd9-8d62-98e45a567eb6 | -3.6936 | -51.3713 | 2026-09-28 00:55:00 | METOP-C | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3240f35c-96b4-3733-bab7-a6a0cb30a078 | -2.2677 | -57.018902 | 2026-09-28 00:55:00 | METOP-C | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 3680d3e8-9f41-3cfd-af79-b80987767373 | -9.8266 | -45.268398 | 2026-09-28 00:55:00 | METOP-C | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 214efde5-ba2e-3561-b06c-2744b45a6484 | -10.9519 | -43.879299 | 2026-09-28 00:55:00 | METOP-C | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 9c3eb32a-e0d1-3ba9-ab25-bc8f4c859720 | -13.4622 | -48.595798 | 2026-09-28 00:55:00 | METOP-C | TROMBAS | GOIÁS | Brasil | 5221452 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| e3a02f7f-70dd-3759-8008-744055a3abb3 | -3.1472 | -54.1012 | 2026-09-28 00:55:00 | METOP-C | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9ab5bb0e-28e8-3704-bdd8-04226129d5b4 | -13.5644 | -46.364899 | 2026-09-28 00:55:00 | METOP-C | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 57313f49-20c5-3674-a214-3d244b8f74a7 | -12.5957 | -51.957001 | 2026-09-28 00:55:00 | METOP-C | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 07fb5c9c-9e6e-3fc9-ba95-139510589ef3 | -2.9611 | -54.099602 | 2026-09-28 00:55:00 | METOP-C | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 00f77103-1784-37f4-8aca-7d714eebfc3a | -3.1523 | -54.078602 | 2026-09-28 00:55:00 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b041ca63-9d33-37f5-bd3a-1104e60d0ee4 | -15.3007 | -42.772598 | 2026-09-28 00:55:00 | METOP-C | SANTO ANTÔNIO DO RETIRO | MINAS GERAIS | Brasil | 3160454 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| bf2c01af-1f46-30b0-a83e-b5179b2b05fa | -6.69 | -45.974098 | 2026-09-28 00:55:00 | METOP-C | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 5283d1fd-318c-390a-a10c-72e0ee8ed5c3 | 1.6772 | -55.951801 | 2026-09-28 00:55:00 | METOP-C | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 766260ce-74b5-3b51-9e48-507f190b827a | -3.875 | -51.797199 | 2026-09-28 00:55:00 | METOP-C | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 774dceee-57c6-3562-8b9d-5ee213fd0d01 | -11.142 | -50.0667 | 2026-09-28 00:55:00 | METOP-C | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| eeabb50f-249b-3eca-90a1-0f6f37a68146 | -6.7074 | -45.583698 | 2026-09-28 00:55:00 | METOP-C | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 19ba5431-40e1-3adb-829a-fbf5c12d86c8 | -11.3335 | -54.106899 | 2026-09-28 00:55:00 | METOP-C | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 2d914ef4-8e52-308d-856f-b3aa9867ef35 | -11.6855 | -44.5257 | 2026-09-28 00:55:00 | METOP-C | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| a99ea664-7030-309f-bab7-b4dde8571738 | -11.3887 | -45.3983 | 2026-09-28 00:55:00 | METOP-C | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| e88759ed-ec67-3c88-ac6e-2d5a9f955df7 | -3.1554 | -54.0923 | 2026-09-28 00:55:00 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 44067aaf-461c-3c3a-8d76-e6ea2f7437ff | -12.5973 | -51.964001 | 2026-09-28 00:55:00 | METOP-C | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| e17b8aba-d5c7-360e-92e4-719647d5945f | -15.1906 | -48.428101 | 2026-09-28 00:55:00 | METOP-C | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 00df56ef-a85d-31dc-a700-e69bd627ccd6 | -5.6391 | -43.7192 | 2026-09-28 00:55:00 | METOP-C | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| b535cb08-bc36-393f-8257-f872046413b9 | 1.6624 | -55.9263 | 2026-09-28 00:55:00 | METOP-C | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 81eab760-d4d0-32e8-b02a-4e4ac56fd64c | -11.2325 | -44.777802 | 2026-09-28 00:55:00 | METOP-C | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 17b65f7d-2795-3d37-8938-02cd73f7476e | -15.2183 | -46.352299 | 2026-09-28 00:55:00 | METOP-C | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 2ea93893-5658-3f44-9a5d-23b20f971670 | -13.3404 | -51.3283 | 2026-09-28 00:55:00 | METOP-C | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 64319172-687e-3657-861c-d8fedb07cfbb | -15.4227 | -47.923698 | 2026-09-28 00:55:00 | METOP-C | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 48637f25-d02e-3f49-9ca7-b4b4289f0ed1 | -23.754601 | -51.931099 | 2026-09-28 00:55:00 | METOP-C | SÃO PEDRO DO IVAÍ | PARANÁ | Brasil | 4125803 | 41 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 33c9e63b-7762-3cd1-95cf-2d9a8b49bdca | -9.0813 | -49.867001 | 2026-09-28 00:55:00 | METOP-C | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a4faf0e6-cc23-362d-be87-6276dda1a0c4 | -8.2935 | -49.591499 | 2026-09-28 00:55:00 | METOP-C | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1a90e546-8a78-3719-835c-85758de76880 | -13.4739 | -48.601299 | 2026-09-28 00:55:00 | METOP-C | TROMBAS | GOIÁS | Brasil | 5221452 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| d3dbc8ed-a6e8-3173-902a-a7f053f5a6fc | -9.4921 | -46.3759 | 2026-09-28 00:55:00 | METOP-C | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| f0bf6145-9e57-3770-9d61-0d514d7f1991 | -11.8563 | -48.885502 | 2026-09-28 00:55:00 | METOP-C | GURUPI | TOCANTINS | Brasil | 1709500 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 2335ff5f-05d2-34ae-ba5a-c5fe2f0df432 | -2.9022 | -54.112701 | 2026-09-28 00:55:00 | METOP-C | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 947ad848-0600-3990-aff5-34b88c264a98 | -4.061 | -47.498001 | 2026-09-28 00:55:00 | METOP-C | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3144af6b-ec89-38b3-befe-43976d623f56 | -11.1937 | -44.7878 | 2026-09-28 00:55:00 | METOP-C | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 49e0d2bf-cca4-3c39-bc0d-66a25d6d334d | -11.782 | -51.050201 | 2026-09-28 00:55:00 | METOP-C | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| e50e1a9f-180d-316a-b8f9-a265aac2f8e7 | -11.1972 | -44.801701 | 2026-09-28 00:55:00 | METOP-C | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| eca44666-7f00-3041-950a-46714987463e | -7.7173 | -54.767399 | 2026-09-28 00:55:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 88423648-b056-3353-b2f9-aa3d3723468a | -18.680901 | -41.470699 | 2026-09-28 00:55:00 | METOP-C | DIVINO DAS LARANJEIRAS | MINAS GERAIS | Brasil | 3122108 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 359457d9-86b6-347c-b57a-2698a9fb4eb9 | -10.9032 | -50.6842 | 2026-09-28 00:55:00 | METOP-C | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 43dd3ea6-78f1-3fa2-8574-dd4c50ec8870 | -14.4867 | -53.642899 | 2026-09-28 00:55:00 | METOP-C | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 7f8170ce-b5ee-3168-ba29-436a52f45c43 | -11.2263 | -44.794201 | 2026-09-28 00:55:00 | METOP-C | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| e084a952-882f-36cf-817a-ada546e5d2ea | -1.7364 | -57.1717 | 2026-09-28 00:55:00 | METOP-C | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 30a4a617-5110-3957-8236-36a59acfc9fa | -10.9422 | -43.881901 | 2026-09-28 00:55:00 | METOP-C | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| fe5022db-001e-3e3e-bc95-625ec344fc99 | -13.8473 | -46.927101 | 2026-09-28 00:55:00 | METOP-C | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 27042fd9-58db-36f6-b77f-563dc4dc68ad | -10.7121 | -44.437302 | 2026-09-28 00:55:00 | METOP-C | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 1048f2fa-81c4-3b12-9292-61414ddf022a | -11.0827 | -51.3298 | 2026-09-28 00:55:00 | METOP-C | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 5551040f-3170-3512-bf44-cd04fc9ea50a | -11.8616 | -47.101299 | 2026-09-28 00:55:00 | METOP-C | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 4ba91f42-1ce8-3773-bef8-d4ada3be48a8 | -4.0421 | -54.227402 | 2026-09-28 00:55:00 | METOP-C | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 87f60ca6-2126-3bc4-9a1a-69567ee2a1bc | -8.2313 | -45.493401 | 2026-09-28 00:55:00 | METOP-C | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 8a733be0-e3f4-3a80-8999-7e44fcf83760 | -10.4211 | -53.837601 | 2026-09-28 00:55:00 | METOP-C | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 91772044-ecb2-3c95-a2ab-6f87cdde0039 | -12.6533 | -47.336102 | 2026-09-28 00:55:00 | METOP-C | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 04dc4622-106a-363f-9520-eac21d8ee7c6 | -12.6607 | -47.324402 | 2026-09-28 00:55:00 | METOP-C | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| a71326da-a39a-30af-9614-ebe6558a79f6 | -11.0811 | -51.322899 | 2026-09-28 00:55:00 | METOP-C | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | nan |


[Clique aqui para ver as próximas entradas](README10.md)
