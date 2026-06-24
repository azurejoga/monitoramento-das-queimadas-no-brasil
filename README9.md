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
| 53308238-1104-3c73-ab70-57fef0ab7f3e | -12.84388 | -44.37263 | 2026-06-24 03:47:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 38.8 |
| a5848b6a-e9f0-385c-b62f-f6ff65df80c1 | -15.01754 | -42.36879 | 2026-06-24 03:47:00 | NOAA-20 | MORTUGABA | BAHIA | Brasil | 2921807 | 29 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 9003cc2d-aec4-3758-b2f3-94ef2762dd3b | -12.81536 | -43.89513 | 2026-06-24 03:47:00 | NOAA-20 | SERRA DOURADA | BAHIA | Brasil | 2930303 | 29 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 07f8d7df-6bd3-3044-a393-fd23089f9383 | -6.86667 | -43.67517 | 2026-06-24 03:47:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 6571ad47-3f81-3eaf-bb68-dabf806b5701 | -12.78942 | -44.45269 | 2026-06-24 03:47:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c8476559-3663-3d6b-9dd3-c6db3a96b7fe | -6.36576 | -43.59798 | 2026-06-24 03:47:00 | NOAA-20 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 15.3 |
| e20617be-a4b1-3250-b993-065a48ce44f9 | -14.51539 | -40.35686 | 2026-06-24 03:47:00 | NOAA-20 | POÇÕES | BAHIA | Brasil | 2925105 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| e32bc932-ebba-324d-998a-70b5c19398e2 | -15.76051 | -43.22991 | 2026-06-24 03:47:00 | NOAA-20 | PORTEIRINHA | MINAS GERAIS | Brasil | 3152204 | 31 | 33 | nan | nan | nan | Caatinga | 9.4 |
| 886d473d-f64d-3593-80e5-61e3c87e793f | -4.55649 | -37.69799 | 2026-06-24 03:47:00 | NOAA-20 | ARACATI | CEARÁ | Brasil | 2301109 | 23 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 15b8df2c-7aaa-38bf-b493-b60b5fc337db | -12.78728 | -44.43745 | 2026-06-24 03:47:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 1298e16b-86d2-3ed8-912c-76a635297da1 | -12.87321 | -44.37314 | 2026-06-24 03:47:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 2fadb691-3cc3-3c58-be0a-37548196516b | -12.84959 | -44.36833 | 2026-06-24 03:47:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 38.8 |
| fde6000a-9f1f-3679-8e44-e35b1552d0df | -8.68522 | -47.85617 | 2026-06-24 03:47:00 | NOAA-20 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 7036c31f-28a7-3199-ad2c-b1447fce1f7f | -6.8672 | -43.67222 | 2026-06-24 03:47:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 7a9baf93-d1d1-33e0-8579-b4619e66fb04 | -6.99114 | -42.8949 | 2026-06-24 03:47:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 5.5 |
| d4b0e7bd-74ce-3d3e-994c-12bfec2d4bec | -12.87418 | -44.36795 | 2026-06-24 03:47:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 3a34c0c8-8218-344a-bdad-eb6d19baf297 | -5.51262 | -35.59655 | 2026-06-24 03:47:00 | NOAA-20 | TAIPU | RIO GRANDE DO NORTE | Brasil | 2413904 | 24 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 65da8147-9b2e-3fbc-8148-a2792d417ae5 | -15.23844 | -40.62638 | 2026-06-24 03:47:00 | NOAA-20 | ITAMBÉ | BAHIA | Brasil | 2915809 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 4c01c14a-2666-3540-8a35-cd6265a59b08 | -8.12901 | -47.88751 | 2026-06-24 03:47:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 9e23c50c-10fd-332f-96a2-3f80b1e6ef66 | -7.60097 | -46.47545 | 2026-06-24 03:47:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b2e57cae-a220-31db-bbbc-da798bd3328e | -4.66584 | -43.2253 | 2026-06-24 03:47:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 39dee935-82f0-3c38-bd4b-1ffe15687209 | -6.36678 | -43.59218 | 2026-06-24 03:47:00 | NOAA-20 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 11.2 |
| 61509fd8-1833-3bc1-851e-8d095c08ab7f | -9.2168 | -45.34333 | 2026-06-24 03:47:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 0e4ac3b4-ad29-33a8-a921-40cd2bf83ef1 | -12.77779 | -44.43547 | 2026-06-24 03:47:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 4229e17e-20fb-3f62-a797-b33aed100a10 | -8.68434 | -47.85181 | 2026-06-24 03:47:00 | NOAA-20 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 9.7 |
| 82fc201e-09e8-3091-9694-c97e581d5c88 | -8.60908 | -45.99928 | 2026-06-24 03:47:00 | NOAA-20 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 13.8 |
| efc875d2-090e-31c9-9e89-6fa897f4d133 | -13.79796 | -42.33318 | 2026-06-24 03:47:00 | NOAA-20 | CAETITÉ | BAHIA | Brasil | 2905206 | 29 | 33 | nan | nan | nan | Caatinga | 0.9 |
| a34cbe68-046b-3102-8050-d6e2ceef955c | -12.78186 | -44.44017 | 2026-06-24 03:47:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 6.6 |
| bc8e1205-122b-329f-8ea6-f7809bdd04cc | -9.377 | -41.2196 | 2026-06-24 03:47:00 | NOAA-20 | CASA NOVA | BAHIA | Brasil | 2907202 | 29 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 9418fe30-8c28-3d6f-974d-995b51e7014e | -3.8723 | -42.96755 | 2026-06-24 03:47:00 | NOAA-20 | BURITI | MARANHÃO | Brasil | 2102200 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d0a521aa-dee2-33cc-b1f5-7ba3d8b24a8f | -12.19735 | -47.96958 | 2026-06-24 03:47:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 7c126539-9414-3421-9779-029e4032a91e | -6.75725 | -44.74551 | 2026-06-24 03:47:00 | NOAA-20 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| dcdb66c1-3f9d-3595-95aa-520713957e67 | -12.77577 | -44.44597 | 2026-06-24 03:47:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 686227af-7d57-3bf8-86a8-58f82f7fdaa4 | -12.78153 | -44.44167 | 2026-06-24 03:47:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 8af5701d-79ee-3bbc-9be2-5d8780d8be66 | -3.95941 | -43.11962 | 2026-06-24 03:47:00 | NOAA-20 | BURITI | MARANHÃO | Brasil | 2102200 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 36ff8de3-c0b7-3eee-86b6-afbae55e3403 | -13.1795 | -43.40188 | 2026-06-24 03:47:00 | NOAA-20 | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Cerrado | 9.1 |
| d0bac053-1291-3247-9388-5060a46cc861 | -6.36178 | -43.59109 | 2026-06-24 03:47:00 | NOAA-20 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 6.7 |
| aff0e6e7-d9cc-38fe-9da3-f98f90ccdb6b | -7.59422 | -46.47869 | 2026-06-24 03:47:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 44476a40-8c0d-380f-9c8d-7f1d7648cbf4 | -12.77235 | -44.43827 | 2026-06-24 03:47:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 2c8363a6-d5ab-3677-b359-c212e6d35b2b | -5.50931 | -35.59602 | 2026-06-24 03:47:00 | NOAA-20 | TAIPU | RIO GRANDE DO NORTE | Brasil | 2413904 | 24 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 043538cf-af7d-3f62-bbd1-75bd31f4cbea | -11.2641 | -43.34393 | 2026-06-24 03:49:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 1.2 |
| c294a0bf-1b0d-32e9-8ab3-f090f8ccec80 | -11.23715 | -43.36123 | 2026-06-24 03:49:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 3.9 |
| aefb75cd-c8b9-3138-8646-cd0fcc1658e6 | -11.24326 | -43.35483 | 2026-06-24 03:49:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 37ef07f6-1cd0-3236-8a03-dbad46367c32 | -11.23343 | -43.35571 | 2026-06-24 03:49:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 3.5 |
| 8222f1dd-7582-37ef-8389-9785bad02ce5 | -11.23687 | -43.33651 | 2026-06-24 03:49:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 3.8 |
| 93e97db2-ec7c-3923-ba0d-7c7269e1e2ba | -11.47559 | -46.73475 | 2026-06-24 03:49:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 847aa139-7a8e-380c-af6a-d0e17e0a9085 | -12.29229 | -44.18459 | 2026-06-24 03:49:00 | NOAA-20 | TABOCAS DO BREJO VELHO | BAHIA | Brasil | 2930907 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 41523df0-124d-36f2-a464-bbdf963ef924 | -10.63064 | -44.85824 | 2026-06-24 03:49:00 | NOAA-20 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 355c90c9-2194-39d5-a946-3c2634d6d447 | -20.61572 | -42.27148 | 2026-06-24 03:49:00 | NOAA-20 | FERVEDOURO | MINAS GERAIS | Brasil | 3125952 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 100e9f8d-46a2-30a9-8086-ca41fe110300 | -10.11289 | -47.54867 | 2026-06-24 03:49:00 | NOAA-20 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 1eb54f91-41e0-31db-ae93-562d41514698 | -11.30836 | -43.33311 | 2026-06-24 03:49:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 5.3 |
| b156d5eb-c0e3-31e3-b7e7-b57a48df10cf | -17.28555 | -47.04102 | 2026-06-24 03:49:00 | NOAA-20 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 94d8f469-1386-3443-af19-bbb744010c37 | -10.69959 | -49.61661 | 2026-06-24 03:49:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 4c9e205e-4c54-3574-9019-848a66c7c0ad | -11.2514 | -43.33637 | 2026-06-24 03:49:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 174ae95b-e285-3011-b7ac-1b9268cb44a5 | -10.6312 | -44.85522 | 2026-06-24 03:49:00 | NOAA-20 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 6b5a870f-6219-3341-8498-cfe334a5150a | -12.29167 | -44.18196 | 2026-06-24 03:49:00 | NOAA-20 | TABOCAS DO BREJO VELHO | BAHIA | Brasil | 2930907 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| da3f25c5-6db0-3a4b-8abe-aab76fc7144d | -10.11196 | -47.55333 | 2026-06-24 03:49:00 | NOAA-20 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 5464d733-3134-3e22-bee2-b69db8906523 | -11.48615 | -46.74076 | 2026-06-24 03:49:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 8f287473-e37a-319a-8102-4c40d0628d92 | -9.43807 | -48.86449 | 2026-06-24 03:49:00 | NOAA-20 | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 566af5be-162c-303b-829f-a3a43b69b7ab | -11.91418 | -44.1721 | 2026-06-24 03:49:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 82f57e6b-5285-3f2a-ab29-0c8dd3baafa9 | -11.54762 | -48.26891 | 2026-06-24 03:49:00 | NOAA-20 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 09e25cf4-6690-35ec-9f95-6d70c8a642c4 | -10.69272 | -49.61549 | 2026-06-24 03:49:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b57be5a6-1fe0-30df-917a-6b6150104d9b | -11.30469 | -43.3275 | 2026-06-24 03:49:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 4.5 |
| bd852555-dff4-3ea5-9f36-723028cb4332 | -11.54862 | -48.26394 | 2026-06-24 03:49:00 | NOAA-20 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 89ae75d9-2621-3eb5-9f4d-af5301f30cc8 | -11.23427 | -43.35101 | 2026-06-24 03:49:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 3.5 |
| 1009c7a2-b080-3101-844b-bb0034971b09 | -9.43692 | -48.87021 | 2026-06-24 03:49:00 | NOAA-20 | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 565d365d-8412-3181-8c44-685107dd81a2 | -11.29207 | -43.31956 | 2026-06-24 03:49:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 3.7 |
| 97d6b1b7-3553-3fc7-8cce-2135646081bd | -11.48125 | -46.73583 | 2026-06-24 03:49:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| ca52bb25-bd03-39b0-82ff-739f094a50c8 | -17.61162 | -46.69787 | 2026-06-24 03:49:00 | NOAA-20 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 81c1e98b-b9a7-32c0-9288-79fce2ace3a3 | -11.25595 | -43.33485 | 2026-06-24 03:49:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 7413f61b-95f2-36da-8d88-61bf0aab78cd | -9.43961 | -48.87425 | 2026-06-24 03:49:00 | NOAA-20 | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 2aabe555-233a-33ae-854e-7ecdbe38eff7 | -20.61934 | -42.2724 | 2026-06-24 03:49:00 | NOAA-20 | FERVEDOURO | MINAS GERAIS | Brasil | 3125952 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.9 |
| d518b115-0e58-3f2a-bf6f-ce7be44fb511 | -11.2606 | -43.36288 | 2026-06-24 03:49:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 838d0f3a-dd46-30ee-ab6a-ab0fc03af77f | -17.28622 | -47.0378 | 2026-06-24 03:49:00 | NOAA-20 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 79e32b43-a869-31c7-b9c1-59b239014895 | -11.79559 | -42.63813 | 2026-06-24 03:49:00 | NOAA-20 | IPUPIARA | BAHIA | Brasil | 2914109 | 29 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 953a5399-1570-3194-a1d0-9643ab83e326 | -11.24152 | -43.36418 | 2026-06-24 03:49:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 6.6 |
| dea99bd1-4565-38d2-b18a-d55317790766 | -11.2424 | -43.35947 | 2026-06-24 03:49:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 6.6 |
| aa0679c7-dee8-3d4c-96f2-f1be81777886 | -11.24625 | -43.36293 | 2026-06-24 03:49:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 9.3 |
| af9536bc-c9a8-3137-a1ce-066a6463b313 | -11.3075 | -43.33784 | 2026-06-24 03:49:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 8f14ccd8-22a0-3f39-99f6-51913544e29e | -17.53207 | -42.47139 | 2026-06-24 03:49:00 | NOAA-20 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| e6f16f39-ee6f-313f-9432-db21ad8f8db4 | -11.23512 | -43.34628 | 2026-06-24 03:49:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 3.2 |
| 8461dd52-a1aa-3314-9625-89409016e9d1 | -11.26688 | -43.35434 | 2026-06-24 03:49:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 4.9 |
| f13a9678-26e5-36cd-8aec-6620486f37ee | -11.25142 | -43.33389 | 2026-06-24 03:49:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 66b3688b-4262-3668-9548-50053d0a0049 | -10.11102 | -47.55803 | 2026-06-24 03:49:00 | NOAA-20 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| ef669ca7-2f7c-327a-b013-86fde24feeb9 | -11.24695 | -43.3603 | 2026-06-24 03:49:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 7.4 |
| 6d1ca613-0158-31d5-b797-035c213b0474 | -10.1106 | -47.55935 | 2026-06-24 03:49:00 | NOAA-20 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 638aedbf-1781-3549-bdcd-0a1c29acaa9b | -11.30104 | -43.3218 | 2026-06-24 03:49:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 4.5 |
| 6b2c75e4-a4ca-3281-b4e2-b0df56a10fd5 | -11.24607 | -43.36504 | 2026-06-24 03:49:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 7.4 |
| 919ce4fc-cdbf-36a9-85a5-1606402149d1 | -17.79399 | -44.57038 | 2026-06-24 03:49:00 | NOAA-20 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| efe3178b-7918-32a9-9e17-cbd57526c8e9 | -11.91893 | -44.17301 | 2026-06-24 03:49:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| cde4a682-f26d-3f5d-843e-909577107f4d | -11.23871 | -43.354 | 2026-06-24 03:49:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 290dd9e0-5610-376b-8a70-85c72848fa66 | -11.29654 | -43.32077 | 2026-06-24 03:49:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 3.7 |
| c3901b63-3240-3d78-a9bf-ecb14bd70cd0 | -19.93495 | -40.79538 | 2026-06-24 03:49:00 | NOAA-20 | ITARANA | ESPÍRITO SANTO | Brasil | 3202900 | 32 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| fd66f1b8-13f3-3cad-a816-30cc2bc03f6c | -11.24253 | -43.35741 | 2026-06-24 03:49:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 4.0 |
| ed42fe16-7abf-340e-8dd4-a11ce2a62ce0 | -11.48046 | -46.73983 | 2026-06-24 03:49:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 548346b6-75d1-3f00-bfc8-771cd308967b | -11.2326 | -43.36036 | 2026-06-24 03:49:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 3.9 |
| 6ac05ddb-6f27-37d7-8425-0a7d968ca515 | -11.26776 | -43.34959 | 2026-06-24 03:49:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 3.2 |
| f324cd8a-2de7-3971-ac2e-c32f4042590b | -17.25808 | -46.32056 | 2026-06-24 03:49:00 | NOAA-20 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| c89fd3b7-d0ef-320d-9d4b-6b06b58a7f4d | -11.23598 | -43.34146 | 2026-06-24 03:49:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 3.2 |
| 15ede459-18b7-3c41-b8f4-ceb4d238e878 | -17.79311 | -44.57488 | 2026-06-24 03:49:00 | NOAA-20 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |


[Clique aqui para ver as próximas entradas](README10.md)
