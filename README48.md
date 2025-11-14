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

## Dados Diários - Página 48

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| e3f05d37-c60f-3252-ac1a-579a3ceddaaa | -11.8528 | -49.2188 | 2025-11-14 04:46:00 | NOAA-20 | CARIRI DO TOCANTINS | TOCANTINS | Brasil | 1703867 | 17 | 33 | nan | nan | nan | Cerrado | 37.6 |
| 7483ebc1-338c-31d6-9858-ae9aeafa0f09 | -9.05902 | -44.78076 | 2025-11-14 04:46:00 | NOAA-20 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 97b1d5f4-e6bb-392f-93b4-ac40ba4258fe | -11.24928 | -47.50113 | 2025-11-14 04:46:00 | NOAA-20 | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| a1423369-3eb9-3d6d-98eb-7442b860f186 | -11.44221 | -49.08995 | 2025-11-14 04:46:00 | NOAA-20 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| c560bea9-8a48-3af2-9b71-b091c1c7e994 | -10.7561 | -44.91344 | 2025-11-14 04:46:00 | NOAA-20 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 4012b135-db6e-3892-99c3-55ae44a560d4 | -9.81827 | -48.35358 | 2025-11-14 04:46:00 | NOAA-20 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| d9012468-19c3-3ce8-a44c-4ad90489b64c | -13.33492 | -43.19011 | 2025-11-14 04:46:00 | NOAA-20 | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 1b171d14-9f05-333a-8e2d-4445e9c913f9 | -10.06317 | -54.39718 | 2025-11-14 04:46:00 | NOAA-20 | MATUPÁ | MATO GROSSO | Brasil | 5105606 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 10d43fe4-8ed4-3299-9e0b-b625afa19c74 | -12.01373 | -46.76948 | 2025-11-14 04:46:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| df9c2551-e111-300a-b0c6-0aafa9eb2663 | -8.93885 | -49.81902 | 2025-11-14 04:46:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| cfc6cf4f-56c9-36ac-8f5e-28e64d0e9c01 | -7.86172 | -44.30829 | 2025-11-14 04:46:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 0f5baa5a-b967-361f-aa58-c5aa34dd242d | -11.73498 | -48.52032 | 2025-11-14 04:46:00 | NOAA-20 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 3b6989d7-47ea-3222-9a68-3a01937a2b51 | -8.75792 | -45.66539 | 2025-11-14 04:46:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 6b250617-4989-3d7f-b85d-54c95540d50a | -11.73061 | -48.52425 | 2025-11-14 04:46:00 | NOAA-20 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f4bf106b-7873-39dd-a211-d02f92114f8e | -12.71448 | -45.42041 | 2025-11-14 04:46:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 11.8 |
| ac227d01-a5ff-3e5e-9e3a-d4cf4dbd0044 | -7.85117 | -44.29007 | 2025-11-14 04:46:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 2ecf106f-5126-3036-9dfc-676da7aefc09 | -8.9468 | -49.81268 | 2025-11-14 04:46:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 0.2 |
| 25385cf0-03ce-3413-aad4-32b4794b667f | -11.81685 | -47.78751 | 2025-11-14 04:46:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| d9542018-eb7c-3968-8a48-8fb8d825357c | -7.38449 | -48.65165 | 2025-11-14 04:46:00 | NOAA-20 | ARAGUAÍNA | TOCANTINS | Brasil | 1702109 | 17 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 62e25f4f-d11a-320d-a88a-3ad33a067bdc | -7.66569 | -45.87994 | 2025-11-14 04:46:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 986bb582-e0e6-3c88-9337-a7f29457c572 | -10.10638 | -40.89561 | 2025-11-14 04:46:00 | NOAA-20 | CAMPO FORMOSO | BAHIA | Brasil | 2906006 | 29 | 33 | nan | nan | nan | Caatinga | 5.6 |
| 3f6ac960-df24-39d0-b655-86d2283416de | -7.6338 | -46.15672 | 2025-11-14 04:46:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 7d5199bd-0707-3543-b30a-7815e7e10e70 | -14.69715 | -46.60819 | 2025-11-14 04:46:00 | NOAA-20 | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 6c140a48-e8e9-3d0f-b7eb-117dd6f19100 | -11.73433 | -48.52481 | 2025-11-14 04:46:00 | NOAA-20 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 26926c19-325b-3bb4-a7a2-bec5aa24f799 | -7.78901 | -49.61914 | 2025-11-14 04:46:00 | NOAA-20 | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 38206084-42b3-35cf-b354-a0e879b94509 | -7.23005 | -46.26918 | 2025-11-14 04:46:00 | NOAA-20 | NOVA COLINAS | MARANHÃO | Brasil | 2107258 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ad098ab9-af76-33d1-8b40-a8266ab54b81 | -7.78562 | -49.61861 | 2025-11-14 04:46:00 | NOAA-20 | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| ea3e4c8f-cfd8-3204-8dc7-ebb9d7dbb2c6 | -7.14833 | -46.29655 | 2025-11-14 04:46:00 | NOAA-20 | NOVA COLINAS | MARANHÃO | Brasil | 2107258 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 4c0719fb-344a-302f-93f5-d025798d6ad2 | -9.49466 | -47.45443 | 2025-11-14 04:46:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 2654bd94-e7d0-3840-9bde-879938d8d181 | -9.35237 | -46.59958 | 2025-11-14 04:46:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 5.8 |
| b706397c-0f29-301c-84b4-ce1a4b5238fb | -10.75549 | -45.01738 | 2025-11-14 04:46:00 | NOAA-20 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 87e8d2e5-b637-3fa8-9a84-c8c9af0d88d6 | -12.39058 | -49.97559 | 2025-11-14 04:46:00 | NOAA-20 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| ccf82325-5e01-366d-b0d7-4a80bf457ffc | -9.31915 | -47.83572 | 2025-11-14 04:46:00 | NOAA-20 | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| f18eb6f4-be76-317a-a0c5-a9013309b902 | -11.81616 | -47.79241 | 2025-11-14 04:46:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 0b5dfce4-4d51-3453-8945-30a07017bed7 | -7.53571 | -45.85772 | 2025-11-14 04:46:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 927b28a1-f70a-33a9-b11e-88975b0e51b5 | -12.4517 | -44.63914 | 2025-11-14 04:46:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 045cf7ed-3b56-3b6c-b2a4-05490cb5383c | -8.12371 | -55.30169 | 2025-11-14 04:46:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 991d4959-5564-37b1-ad2c-7e9888fba81a | -10.0557 | -44.76883 | 2025-11-14 04:46:00 | NOAA-20 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 53ed4496-3407-36d5-88ea-18f0e365f47d | -7.84123 | -44.29355 | 2025-11-14 04:46:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 1ea9fcce-0465-37d4-9390-319c45c9b008 | -8.90003 | -47.89655 | 2025-11-14 04:46:00 | NOAA-20 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 51bc29e7-67f8-3a3c-ab08-9fa0bbfe7dbb | -13.39525 | -46.72302 | 2025-11-14 04:46:00 | NOAA-20 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 428f94e2-3c94-3fe1-8bfa-f39fcb367a36 | -11.03211 | -44.65253 | 2025-11-14 04:46:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| f04bf3e3-5de4-38f9-8e23-6f5e84733d3c | -7.59306 | -46.76011 | 2025-11-14 04:46:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| fb0635c3-1fa5-3e0c-ad11-bcfa5600d9b0 | -11.84799 | -49.22654 | 2025-11-14 04:46:00 | NOAA-20 | CARIRI DO TOCANTINS | TOCANTINS | Brasil | 1703867 | 17 | 33 | nan | nan | nan | Cerrado | 13.5 |
| a975ff97-ec0e-3b97-a9df-f6e1b3e098e6 | -9.95217 | -44.94637 | 2025-11-14 04:46:00 | NOAA-20 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 4.7 |
| c5762b73-7241-34aa-9247-72ab2fadbafd | -10.62584 | -45.00941 | 2025-11-14 04:46:00 | NOAA-20 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |
| de012075-3dc4-3dbe-94e1-3392b7f95ee6 | -11.17563 | -47.45625 | 2025-11-14 04:46:00 | NOAA-20 | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| fc1d53da-1fec-30fb-954f-abd85fc6ba83 | -7.8373 | -44.28812 | 2025-11-14 04:46:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 8a49f5db-3c30-3805-8fa1-eef88008d740 | -7.8881 | -44.32182 | 2025-11-14 04:46:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| f5b4133d-af20-357b-bb20-0cfc5f57694f | -11.85874 | -49.22817 | 2025-11-14 04:46:00 | NOAA-20 | CARIRI DO TOCANTINS | TOCANTINS | Brasil | 1703867 | 17 | 33 | nan | nan | nan | Cerrado | 12.3 |
| 1970719e-a61f-3ca8-87a6-a990243a7529 | -10.1096 | -40.89722 | 2025-11-14 04:46:00 | NOAA-20 | CAMPO FORMOSO | BAHIA | Brasil | 2906006 | 29 | 33 | nan | nan | nan | Caatinga | 1.8 |
| fe1cf11c-7efd-3039-9d6f-e8fbdf309563 | -7.79241 | -49.61968 | 2025-11-14 04:46:00 | NOAA-20 | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| f81aebe0-b52f-3f3c-a9b6-1e68c51e7e68 | -7.26265 | -46.88773 | 2025-11-14 04:46:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 077a14dc-e578-37d5-a50f-ec5637f0bf64 | -7.84978 | -44.29965 | 2025-11-14 04:46:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 9.7 |
| e68ddcbf-6f79-3ffc-aa90-ba17fde06088 | -11.85577 | -49.22349 | 2025-11-14 04:46:00 | NOAA-20 | CARIRI DO TOCANTINS | TOCANTINS | Brasil | 1703867 | 17 | 33 | nan | nan | nan | Cerrado | 12.3 |
| f8ceb45f-b385-3d07-a16b-18ae1089ed3e | -7.84655 | -44.28941 | 2025-11-14 04:46:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.3 |
| b4de0977-0fc5-354a-bd19-95978dd2eba6 | -11.57364 | -44.87038 | 2025-11-14 04:46:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 8a5c9e99-bb56-3fde-ab24-cff49c0f2de7 | -9.91353 | -47.86614 | 2025-11-14 04:46:00 | NOAA-20 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 5.1 |
| c86000f9-bc91-3aa9-a8b9-25e5cb8685a0 | -11.84922 | -49.21825 | 2025-11-14 04:46:00 | NOAA-20 | CARIRI DO TOCANTINS | TOCANTINS | Brasil | 1703867 | 17 | 33 | nan | nan | nan | Cerrado | 37.6 |
| 1f5def7b-1402-385e-8331-d6a6399417dd | -7.54039 | -45.85453 | 2025-11-14 04:46:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 7bc3fea8-64a3-366d-867b-829c7db6b482 | -11.80524 | -44.26189 | 2025-11-14 04:46:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 31a0de6b-3745-3a1f-91e2-8ca74c2c304c | -7.88118 | -48.40702 | 2025-11-14 04:46:00 | NOAA-20 | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 581e2740-f0ca-3810-8048-28d5ddeff7c8 | -7.14885 | -46.29303 | 2025-11-14 04:46:00 | NOAA-20 | NOVA COLINAS | MARANHÃO | Brasil | 2107258 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| ce08bc27-9217-34c2-ad7b-09a161982ca7 | -10.6118 | -52.17928 | 2025-11-14 04:46:00 | NOAA-20 | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 6825e460-430e-31a6-9c7c-e6af2575c4f2 | -13.5001 | -43.64368 | 2025-11-14 04:46:00 | NOAA-20 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d87d3416-4d21-3e6b-b299-2a2e16092540 | -10.48141 | -51.86438 | 2025-11-14 04:46:00 | NOAA-20 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 1b3fa7c6-52b8-3d32-9e47-76cfb7242bd0 | -7.93918 | -44.32208 | 2025-11-14 04:46:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 562456af-f879-3f17-bf09-72437ebd8868 | -7.93326 | -44.33098 | 2025-11-14 04:46:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 1e5c9673-0101-3521-93bc-b754bd1f00b1 | -12.00127 | -46.76775 | 2025-11-14 04:46:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| f20e5317-c739-3791-8b48-fcf36c192100 | -11.99098 | -44.28886 | 2025-11-14 04:46:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 660be7be-b913-3874-b68b-04e06a03ac35 | -10.6095 | -42.31584 | 2025-11-14 04:46:00 | NOAA-20 | ITAGUAÇU DA BAHIA | BAHIA | Brasil | 2915353 | 29 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 79a0d65e-aaad-3694-a0d9-fcc9d7126e98 | -10.92201 | -44.5919 | 2025-11-14 04:46:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 8737bad5-e767-314f-aaea-47d347abe519 | -13.33259 | -43.19005 | 2025-11-14 04:46:00 | NOAA-20 | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 69ce7fd6-7608-348e-b2ab-abfe6936bbd2 | -8.62718 | -54.94052 | 2025-11-14 04:46:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 4dd1fc2f-9385-31c9-bb89-e8fe77d53454 | -14.27871 | -45.36255 | 2025-11-14 04:46:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d03d08dc-cbdf-3919-a190-4eebb39636e9 | -9.14492 | -45.17575 | 2025-11-14 04:46:00 | NOAA-20 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 83895a21-39e6-32da-a302-2a485f88b872 | -10.3383 | -49.91728 | 2025-11-14 04:46:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 0f51b44d-b343-3b3d-8fd5-19e4d0f0fe14 | -14.69556 | -46.6203 | 2025-11-14 04:46:00 | NOAA-20 | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 22e5a5a1-59ba-360f-b950-d7163ea9ff23 | -7.92965 | -44.3278 | 2025-11-14 04:46:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 0cf77068-ecba-34ba-9cd2-e0291a41729f | -14.69608 | -46.61637 | 2025-11-14 04:46:00 | NOAA-20 | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 8aff6e5e-5979-3065-9407-89e3d41d1924 | -12.06174 | -48.20902 | 2025-11-14 04:46:00 | NOAA-20 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 13.4 |
| 84d8131f-ac16-3550-a4ba-04f70a875447 | -10.74262 | -48.17442 | 2025-11-14 04:46:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 7b704860-2b82-3e0b-ac8b-84b789185527 | -7.93495 | -44.32369 | 2025-11-14 04:46:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 3cb15206-ec8d-35ad-a7fd-0b366c612a87 | -9.09454 | -44.3228 | 2025-11-14 04:46:00 | NOAA-20 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 5aa32340-79f5-3489-9ff9-304071900ea4 | -7.92897 | -44.33256 | 2025-11-14 04:46:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| acc7ffc6-f998-310f-a48e-4637df492dd8 | -14.66216 | -46.56982 | 2025-11-14 04:46:00 | NOAA-20 | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 8629f366-f0ad-37cb-a258-bd18a3d57ea8 | -11.73673 | -48.53433 | 2025-11-14 04:46:00 | NOAA-20 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 67c72d2c-e401-3116-b7f8-0369b3d85516 | -7.72549 | -47.18842 | 2025-11-14 04:46:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| c1bad31e-ce0c-3cd4-b88e-f3a0d7ff7207 | -10.76071 | -44.91418 | 2025-11-14 04:46:00 | NOAA-20 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 2fce348c-b763-3d37-81a2-2b3e7b0a5093 | -7.347 | -46.01647 | 2025-11-14 04:46:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f1c84b32-213d-38ad-b069-4b2f08455133 | -12.66482 | -46.7441 | 2025-11-14 04:46:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 5932085a-2e6e-31e1-a9d6-ac2a9ab29093 | -8.65487 | -47.3857 | 2025-11-14 04:46:00 | NOAA-20 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| b8c3dfba-bac7-3dfc-9048-156c45460629 | -12.67217 | -46.75323 | 2025-11-14 04:46:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 5.5 |
| f8c73ddd-bf3f-3c86-a6ad-aae660c55434 | -9.34883 | -46.59539 | 2025-11-14 04:46:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| f545a8c0-f538-3294-9334-ead19222067c | -12.01989 | -46.76854 | 2025-11-14 04:46:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 2fbc93c2-2814-3f46-b984-dc94d9bca726 | -7.93889 | -44.32911 | 2025-11-14 04:46:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| aa8b4f79-77db-365e-85ac-87ac8896d747 | -13.33216 | -43.19351 | 2025-11-14 04:46:00 | NOAA-20 | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Caatinga | 1.2 |
| c72bc537-c019-3864-8e00-2379ea4b772b | -9.02612 | -48.74631 | 2025-11-14 04:46:00 | NOAA-20 | COLMÉIA | TOCANTINS | Brasil | 1716703 | 17 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6db6e68a-c2d7-3170-aa99-0fc716af630e | -10.48086 | -51.86787 | 2025-11-14 04:46:00 | NOAA-20 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 5285cb49-4615-3e79-8885-d1684195ddd1 | -10.37315 | -47.68579 | 2025-11-14 04:46:00 | NOAA-20 | SANTA TEREZA DO TOCANTINS | TOCANTINS | Brasil | 1719004 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |


[Clique aqui para ver as próximas entradas](README49.md)
