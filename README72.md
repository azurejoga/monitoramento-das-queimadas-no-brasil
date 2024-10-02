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

## Dados Diários - Página 72

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 5ee5d4f7-2fcd-3895-b00c-e480aab37be9 | -19.60424 | -47.20926 | 2024-10-02 03:55:00 | NOAA-20 | ARAXÁ | MINAS GERAIS | Brasil | 3104007 | 31 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 58a5c0bf-bd04-358e-ae6d-dfa2f07efb95 | -15.02433 | -47.55458 | 2024-10-02 03:55:00 | NOAA-20 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 0ad7e353-63d9-3d29-a418-11f335e64404 | -15.02288 | -47.55494 | 2024-10-02 03:55:00 | NOAA-20 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 98c67a5e-9371-3324-83d4-b375e8f61f62 | -15.01968 | -47.55388 | 2024-10-02 03:55:00 | NOAA-20 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 0.3 |
| ac7f81db-8d77-3ae0-b0a3-6929ca0ca470 | -14.82363 | -47.68438 | 2024-10-02 03:55:00 | NOAA-20 | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 16.8 |
| 12b99766-b85d-3753-9ea0-fc9f289fcf13 | -14.78841 | -48.07426 | 2024-10-02 03:55:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 309277c0-6046-3492-8707-7f8db7ff9c55 | -14.78363 | -48.07323 | 2024-10-02 03:55:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| dd760a7e-25bd-36f9-8599-de561437754e | -14.75709 | -48.08191 | 2024-10-02 03:55:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 4acc7c2e-0fb0-3107-943e-4080f23d0929 | -14.15235 | -46.9813 | 2024-10-02 03:55:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 9001a1f7-9b37-380c-b1b9-482a24da3116 | -14.14947 | -46.97883 | 2024-10-02 03:55:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 83b6fe0e-2e19-3111-9009-cb8f451b18bf | -14.14858 | -46.98347 | 2024-10-02 03:55:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 4.2 |
| a2d16d40-48a9-35a3-b414-7e12523413e6 | -14.14785 | -46.98035 | 2024-10-02 03:55:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 2086d143-2daf-33f3-9d5a-8dde464a5220 | -14.147 | -46.98501 | 2024-10-02 03:55:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| b2a87946-2e2a-3f05-96d7-5fd03799a837 | -14.02666 | -47.92493 | 2024-10-02 03:55:00 | NOAA-20 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| e51eeb64-8e7e-3dcc-8f6f-ad80122a86e0 | -15.55351 | -48.05183 | 2024-10-02 03:55:00 | NOAA-20 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 381f7d6b-4baa-326f-b021-225c3c6d3c8b | -15.54775 | -48.05632 | 2024-10-02 03:55:00 | NOAA-20 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 71f48397-0b7e-3146-a27e-719a0ee2d03d | -15.38746 | -47.433 | 2024-10-02 03:55:00 | NOAA-20 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 1ae87fa5-405a-3b6f-982b-d660620b94cb | -15.38284 | -47.43249 | 2024-10-02 03:55:00 | NOAA-20 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| a3a0b76c-3f55-3e59-b9e3-232c70239e88 | -15.36985 | -47.42649 | 2024-10-02 03:55:00 | NOAA-20 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 9e9882ee-7957-3d2c-85e2-909e4d72d214 | -15.36904 | -47.42831 | 2024-10-02 03:55:00 | NOAA-20 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 1cf6441c-5240-3f4e-8d2b-e8174aba9b10 | -15.36434 | -47.42828 | 2024-10-02 03:55:00 | NOAA-20 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| d620655c-748f-3f28-bbf7-3541cbeeaa7e | -15.36344 | -47.43306 | 2024-10-02 03:55:00 | NOAA-20 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 7c25795b-a312-38c0-8f18-17b604ca7aab | -15.28186 | -47.514 | 2024-10-02 03:55:00 | NOAA-20 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 2fa0980c-46a4-3463-a04f-5aeee7d25069 | -15.28107 | -47.51807 | 2024-10-02 03:55:00 | NOAA-20 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 10.1 |
| 4d76ffa6-509b-3ff7-a161-140d4ce58ea9 | -15.28029 | -47.52217 | 2024-10-02 03:55:00 | NOAA-20 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 10.1 |
| d964a358-35b9-3ab2-a0fc-c92e79002340 | -15.27655 | -47.51691 | 2024-10-02 03:55:00 | NOAA-20 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 72546722-b9c2-3908-ac71-2c21c3c14db8 | -15.20385 | -47.94394 | 2024-10-02 03:55:00 | NOAA-20 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| f22434c1-aa45-379d-8347-96ee3fe97abd | -15.20181 | -47.95447 | 2024-10-02 03:55:00 | NOAA-20 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| cc399901-4fbd-3d24-9ac9-6f97c2bcaf3a | -15.19916 | -47.94289 | 2024-10-02 03:55:00 | NOAA-20 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| ab9d7b78-9179-36c0-9c46-2edf555b5fb9 | -15.19347 | -47.94696 | 2024-10-02 03:55:00 | NOAA-20 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 96480baf-eb16-3f7a-9948-3588002e2ea2 | -17.73176 | -48.45238 | 2024-10-02 03:55:00 | NOAA-20 | IPAMERI | GOIÁS | Brasil | 5210109 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| c62365b0-3133-356d-b505-859022bbd65f | -17.73077 | -48.45743 | 2024-10-02 03:55:00 | NOAA-20 | IPAMERI | GOIÁS | Brasil | 5210109 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| df269bdf-6267-363b-9d06-a0bfdfe2e13e | -16.68909 | -47.8263 | 2024-10-02 03:55:00 | NOAA-20 | CRISTALINA | GOIÁS | Brasil | 5206206 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 38c41857-6f42-318a-a206-6c1d0971ae04 | -16.68457 | -47.82518 | 2024-10-02 03:55:00 | NOAA-20 | CRISTALINA | GOIÁS | Brasil | 5206206 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| f90796bd-32b6-3940-921a-b93cdd2140cc | -18.04911 | -48.59946 | 2024-10-02 03:55:00 | NOAA-20 | CALDAS NOVAS | GOIÁS | Brasil | 5204508 | 52 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| 1e122827-f2aa-30ed-bd67-e11940bf9a60 | -18.04808 | -48.60471 | 2024-10-02 03:55:00 | NOAA-20 | CALDAS NOVAS | GOIÁS | Brasil | 5204508 | 52 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| ac8f166e-d636-343b-a8eb-e6aedaab9cfc | -20.63477 | -48.75619 | 2024-10-02 03:55:00 | NOAA-20 | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Mata Atlântica | 5.4 |
| fe541ab3-db8d-31c7-bef2-3aebb6ece0ba | -19.6925 | -48.79354 | 2024-10-02 03:55:00 | NOAA-20 | CAMPO FLORIDO | MINAS GERAIS | Brasil | 3111408 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 78d8ef46-634f-3163-ae33-e66c2c856df6 | -13.20969 | -48.62123 | 2024-10-02 03:55:00 | NOAA-20 | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 552ecf75-27fb-3928-96da-60066ef607f6 | -13.49601 | -48.61832 | 2024-10-02 03:55:00 | NOAA-20 | TROMBAS | GOIÁS | Brasil | 5221452 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 7b610e7b-2e93-3e85-bb89-51c92bbca48d | -13.49542 | -48.62139 | 2024-10-02 03:55:00 | NOAA-20 | TROMBAS | GOIÁS | Brasil | 5221452 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 06e5b9f6-562e-3b52-97c2-f75f20dd628f | -13.49088 | -48.61752 | 2024-10-02 03:55:00 | NOAA-20 | TROMBAS | GOIÁS | Brasil | 5221452 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 43057bef-17b3-368b-9765-e52fdf403656 | -13.22564 | -48.6211 | 2024-10-02 03:55:00 | NOAA-20 | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 955d2024-0057-3fef-9f7b-796852ebd699 | -13.22174 | -48.6139 | 2024-10-02 03:55:00 | NOAA-20 | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| d882d336-1fa9-3546-a873-9b4257c97432 | -13.22118 | -48.61677 | 2024-10-02 03:55:00 | NOAA-20 | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 71bfccb2-5436-375e-9e0a-3422be3ffafb | -13.22061 | -48.61971 | 2024-10-02 03:55:00 | NOAA-20 | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 9e4fc3b0-75c9-3f05-aff3-e49f4c4c1df7 | -13.21663 | -48.61287 | 2024-10-02 03:55:00 | NOAA-20 | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 9dc909d2-84e7-3ea2-93ca-dd9b00266ccc | -13.21605 | -48.61588 | 2024-10-02 03:55:00 | NOAA-20 | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 790fd65c-f097-393f-9ea7-5ee0923d400d | -13.21332 | -48.60268 | 2024-10-02 03:55:00 | NOAA-20 | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| fb1352a1-e17e-3126-84eb-0c29b3ca9aa2 | -13.21274 | -48.60561 | 2024-10-02 03:55:00 | NOAA-20 | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 87b4e2ce-0188-3c52-93aa-84fa6a3be303 | -13.21214 | -48.6087 | 2024-10-02 03:55:00 | NOAA-20 | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 7a2ae200-c087-335f-923d-480edf2cfedf | -13.21093 | -48.6149 | 2024-10-02 03:55:00 | NOAA-20 | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 3bb3dacf-2ce5-3371-b66a-1c9e224fe5e3 | -13.21031 | -48.61805 | 2024-10-02 03:55:00 | NOAA-20 | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| ac21f3b4-39c9-3068-98c4-91b992429567 | -13.20907 | -48.62443 | 2024-10-02 03:55:00 | NOAA-20 | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 698ef1ba-32b0-33aa-a0c1-b23cf47a61d4 | -13.20844 | -48.62763 | 2024-10-02 03:55:00 | NOAA-20 | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 7f5a577f-44ca-327b-8ac0-808677bd48e7 | -13.20816 | -48.60194 | 2024-10-02 03:55:00 | NOAA-20 | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 5bfb7b69-4113-3a7a-bcf7-acbbb4c6f904 | -13.20782 | -48.63081 | 2024-10-02 03:55:00 | NOAA-20 | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 347b73e6-c0ac-38a3-95f0-7c1dc74ac36c | -13.2072 | -48.63401 | 2024-10-02 03:55:00 | NOAA-20 | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 8.6 |
| 17d95c9f-63b6-3ec7-bc6a-896001b1e641 | -13.20657 | -48.6372 | 2024-10-02 03:55:00 | NOAA-20 | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 8.6 |
| 69801b86-68a0-35dd-a300-590e930d565a | -13.20646 | -48.61064 | 2024-10-02 03:55:00 | NOAA-20 | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 4e828a2f-f715-365c-8fd4-d52d557d9d82 | -13.20586 | -48.6137 | 2024-10-02 03:55:00 | NOAA-20 | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| bedaf9eb-1081-3dd7-bf6a-5bfaacba6721 | -13.20565 | -48.60186 | 2024-10-02 03:55:00 | NOAA-20 | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| b3753490-fa2e-36cf-9ac1-4f61ab200296 | -13.20521 | -48.617 | 2024-10-02 03:55:00 | NOAA-20 | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 563fe016-20e7-3711-a3b7-5410873249e1 | -13.20456 | -48.62033 | 2024-10-02 03:55:00 | NOAA-20 | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 4.7 |
| b70c641d-990e-37ac-94bd-5c91e2a37f2e | -13.20403 | -48.61047 | 2024-10-02 03:55:00 | NOAA-20 | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| f3993484-889b-3afa-9d13-aed0718642b5 | -13.20394 | -48.62352 | 2024-10-02 03:55:00 | NOAA-20 | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 4.7 |
| aaed80f5-15e7-34f4-a27f-c5a80c5dcee3 | -13.20346 | -48.61348 | 2024-10-02 03:55:00 | NOAA-20 | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 28856815-38c3-371a-81c3-f0a14d63abd0 | -13.20332 | -48.62667 | 2024-10-02 03:55:00 | NOAA-20 | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 2f6c8aea-8388-30b2-8150-a5779289e718 | -13.20284 | -48.61679 | 2024-10-02 03:55:00 | NOAA-20 | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| d520be3c-f896-37e2-8c93-17a0187e0d81 | -13.2027 | -48.62981 | 2024-10-02 03:55:00 | NOAA-20 | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 6.2 |
| dc3ac38e-d417-3c30-9e9a-58e8ee2396bb | -13.20222 | -48.62011 | 2024-10-02 03:55:00 | NOAA-20 | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 2985c759-a0cc-31a7-a7f0-e4c8cf39e7e8 | -13.20208 | -48.63298 | 2024-10-02 03:55:00 | NOAA-20 | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 6582ea0c-96ec-31c8-9cf8-eb875275f552 | -13.20162 | -48.62329 | 2024-10-02 03:55:00 | NOAA-20 | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 9a489d71-88f6-3b39-a367-399638d92e71 | -13.20146 | -48.63616 | 2024-10-02 03:55:00 | NOAA-20 | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 46851009-9474-37e9-9d15-222d2298b0a0 | -13.20102 | -48.62645 | 2024-10-02 03:55:00 | NOAA-20 | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 759f461f-0230-36bb-808c-ccd9fd2456d0 | -13.20043 | -48.62963 | 2024-10-02 03:55:00 | NOAA-20 | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 7cbdaaf6-2594-320f-9182-0bd4f0be19f0 | -13.20013 | -48.61583 | 2024-10-02 03:55:00 | NOAA-20 | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| fe1e770a-68e6-3b2d-822e-a849c5b6beed | -13.19982 | -48.63282 | 2024-10-02 03:55:00 | NOAA-20 | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 5.8 |
| b2d22710-886b-34ee-a7ba-59eea4d18ca2 | -13.1995 | -48.61904 | 2024-10-02 03:55:00 | NOAA-20 | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 250c9d08-2ec0-399f-b2ca-fd7b38c0e740 | -13.19888 | -48.62223 | 2024-10-02 03:55:00 | NOAA-20 | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 1bf527cc-8b94-3266-b63f-3c1549c51514 | -13.19825 | -48.62542 | 2024-10-02 03:55:00 | NOAA-20 | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 6.2 |
| a8bdbf26-7e78-39ad-9003-beaa80e263e4 | -13.19775 | -48.61564 | 2024-10-02 03:55:00 | NOAA-20 | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| c3395c41-1f82-3ce8-b9d9-f8b4618b54a8 | -13.19762 | -48.62862 | 2024-10-02 03:55:00 | NOAA-20 | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 6.2 |
| a6c24242-9366-3b02-84a1-761fb48d8ba4 | -13.19716 | -48.61878 | 2024-10-02 03:55:00 | NOAA-20 | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 7658ea6e-4781-3c53-8ffc-b3834a64cc07 | -13.19699 | -48.63184 | 2024-10-02 03:55:00 | NOAA-20 | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 6.4 |
| a510ea6f-a9f3-3410-b402-08b45a802cfa | -13.19656 | -48.62197 | 2024-10-02 03:55:00 | NOAA-20 | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 4.8 |
| b6611dee-e8e8-3252-9a66-62b4864a0581 | -13.1944 | -48.61798 | 2024-10-02 03:55:00 | NOAA-20 | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| e4562f6f-7382-3930-a950-1b90144aec2a | -13.75468 | -48.31778 | 2024-10-02 03:55:00 | NOAA-20 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| db31047b-f2b2-3bf3-a9b7-d280ff6e32a5 | -13.75091 | -48.31058 | 2024-10-02 03:55:00 | NOAA-20 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 12308caa-5580-3cbb-8979-152e25507f40 | -13.74967 | -48.31703 | 2024-10-02 03:55:00 | NOAA-20 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 2d8b11d1-ef2f-3e21-9bd0-ec2fbb16d097 | -13.23594 | -48.59536 | 2024-10-02 03:55:00 | NOAA-20 | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 131d9698-6cbf-396f-b8bc-242a5bc6f3ce | -13.19576 | -48.51431 | 2024-10-02 03:55:00 | NOAA-20 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d4c222ad-385e-3725-9f40-9dcaacce4594 | -13.19121 | -48.51052 | 2024-10-02 03:55:00 | NOAA-20 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ed79bc00-4270-37f3-81cc-716c6fa2ac5c | -13.26007 | -48.58002 | 2024-10-02 03:55:00 | NOAA-20 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 638ae017-ed12-329d-96c0-e3633895a2d1 | -13.25943 | -48.58331 | 2024-10-02 03:55:00 | NOAA-20 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 4255fed4-d923-3f51-a9ea-70c646f7f2ec | -13.25552 | -48.57618 | 2024-10-02 03:55:00 | NOAA-20 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 965d879e-a111-350e-8bb9-927a6a63127c | -13.25494 | -48.57916 | 2024-10-02 03:55:00 | NOAA-20 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 507f6fbb-99ec-3874-bd5a-7edebb66f70e | -13.25433 | -48.58237 | 2024-10-02 03:55:00 | NOAA-20 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 5d5ce16f-8168-3b19-95ea-ce8900da6c3f | -13.2537 | -48.58564 | 2024-10-02 03:55:00 | NOAA-20 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 0ef3d18b-2e9b-3ec5-b3ae-9ebbc919b94b | -13.24978 | -48.57851 | 2024-10-02 03:55:00 | NOAA-20 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |


[Clique aqui para ver as próximas entradas](README73.md)
