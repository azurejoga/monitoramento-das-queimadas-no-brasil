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

## Dados Diários - Página 1

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 25150ec1-02aa-3d0e-9a72-c3f699a61f1f | -4.42 | -46.55 | 2024-12-27 00:00:00 | MSG-03 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 1b498605-22b6-37bc-9179-c909b461bbe3 | -5.66 | -43.71 | 2024-12-27 00:00:00 | MSG-03 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 0c358f4f-bb9b-3b00-aad1-c73dfb96b5e1 | -2.27 | -45.57 | 2024-12-27 00:00:00 | MSG-03 | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| eeeed206-424f-38d2-b97f-2926fe2dd5bf | -4.42 | -46.6 | 2024-12-27 00:00:00 | MSG-03 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 40899264-c3ce-3f48-b939-2a2d8b63a0d1 | -5.63 | -43.71 | 2024-12-27 00:00:00 | MSG-03 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 9dd79b91-f070-35aa-9523-c866936accb0 | -3.9312 | -46.987099 | 2024-12-27 00:02:00 | METOP-C | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| cba349dd-c12c-3561-9e7a-2af26b5cf08e | -11.9741 | -41.3391 | 2024-12-27 00:02:00 | METOP-C | BONITO | BAHIA | Brasil | 2904050 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| 005de017-88b0-35a2-869e-b9760daffe46 | -5.6619 | -43.714199 | 2024-12-27 00:02:00 | METOP-C | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 327a4d68-3b63-3677-8306-1c51c719a4a7 | -4.4324 | -46.534401 | 2024-12-27 00:02:00 | METOP-C | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 94f8f412-e6d5-3f83-ba44-b951d80c336c | -12.7294 | -40.215599 | 2024-12-27 00:02:00 | METOP-C | ITABERABA | BAHIA | Brasil | 2914703 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| a5df9930-488b-30c8-a749-1102c64ca27a | -10.1085 | -36.457802 | 2024-12-27 00:02:00 | METOP-C | PENEDO | ALAGOAS | Brasil | 2706703 | 27 | 33 | nan | nan | nan | Caatinga | nan |
| f171116a-987a-3bf8-bbc9-17d790953c14 | -4.566 | -44.130501 | 2024-12-27 00:02:00 | METOP-C | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 77671d6d-03d8-33ba-a01d-1d37fe8dc8ad | -10.4966 | -36.9828 | 2024-12-27 00:02:00 | METOP-C | CAPELA | SERGIPE | Brasil | 2801306 | 28 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 4cfb0674-22fe-3744-9834-65cf33f532dd | -2.2558 | -46.3825 | 2024-12-27 00:02:00 | METOP-C | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 820506f9-3201-38d2-a984-b3b344cedf27 | -4.7032 | -38.1642 | 2024-12-27 00:02:00 | METOP-C | RUSSAS | CEARÁ | Brasil | 2311801 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| 5c333e9e-ca52-3ceb-a1d8-009a3a89fed2 | -5.9207 | -43.4944 | 2024-12-27 00:02:00 | METOP-C | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| ffba4f6e-06f1-334c-8e64-869c1b9c913f | -8.6336 | -40.4827 | 2024-12-27 00:02:00 | METOP-C | DORMENTES | PERNAMBUCO | Brasil | 2605152 | 26 | 33 | nan | nan | nan | Caatinga | nan |
| f35dc2a2-b5a0-3e09-83f7-6f59de9034ae | -12.1923 | -41.355701 | 2024-12-27 00:02:00 | METOP-C | LENÇÓIS | BAHIA | Brasil | 2919306 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| 627431ac-e4c8-3203-9f51-2bc50483c408 | -4.5384 | -42.072899 | 2024-12-27 00:02:00 | METOP-C | BOQUEIRÃO DO PIAUÍ | PIAUÍ | Brasil | 2201945 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| a497f910-bac3-34b3-99ce-7f67c761bbc1 | -3.9467 | -46.965099 | 2024-12-27 00:02:00 | METOP-C | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| f9c17268-1cf4-393d-a106-a506fa7b6c72 | -6.3962 | -39.397999 | 2024-12-27 00:02:00 | METOP-C | IGUATU | CEARÁ | Brasil | 2305506 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| 6c7dc5c0-da42-3202-a00e-1036615686f2 | -4.4226 | -46.536499 | 2024-12-27 00:02:00 | METOP-C | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| bf408c69-c1bc-3b7b-a4f9-023e58dfc8fc | -5.4019 | -42.953899 | 2024-12-27 00:02:00 | METOP-C | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Caatinga | nan |
| 6ad21f11-7619-36a1-82c6-620e69a14db2 | -5.4042 | -42.963902 | 2024-12-27 00:02:00 | METOP-C | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Caatinga | nan |
| 4cb24e4c-233d-3220-8197-ac5a82c8324b | -5.9158 | -43.472198 | 2024-12-27 00:02:00 | METOP-C | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| ae3dfdd7-1e7d-39f5-beca-b02e1c22b75b | -5.9109 | -43.496498 | 2024-12-27 00:02:00 | METOP-C | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| b41e182c-890d-3e00-9a5c-67e2bb8ec673 | -7.2019 | -35.054699 | 2024-12-27 00:02:00 | METOP-C | SANTA RITA | PARAÍBA | Brasil | 2513703 | 25 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 023e0380-4326-3bc1-b745-8f83523fe29c | -5.6569 | -43.691601 | 2024-12-27 00:02:00 | METOP-C | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 15e18917-ca38-3e5c-845a-559728bb9bd4 | -4.0003 | -43.247501 | 2024-12-27 00:02:00 | METOP-C | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| a324f4ba-812c-3e03-8512-ff8caf3e9efa | -12.7215 | -40.226601 | 2024-12-27 00:02:00 | METOP-C | ITABERABA | BAHIA | Brasil | 2914703 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| 5ca38150-5e98-38cd-a372-057d4c7707aa | -10.7284 | -37.141102 | 2024-12-27 00:02:00 | METOP-C | MARUIM | SERGIPE | Brasil | 2804003 | 28 | 33 | nan | nan | nan | Mata Atlântica | nan |
| aef0bc13-c6e6-3a0e-8f34-908d53771a7b | -5.1553 | -39.377399 | 2024-12-27 00:02:00 | METOP-C | QUIXERAMOBIM | CEARÁ | Brasil | 2311405 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| 2987c2e5-adab-3859-8522-120d1c11ccf2 | -4.9176 | -38.740799 | 2024-12-27 00:02:00 | METOP-C | QUIXADÁ | CEARÁ | Brasil | 2311306 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| 0d8c4a41-a642-31bf-b37d-8b707ab14486 | -9.6586 | -36.117199 | 2024-12-27 00:02:00 | METOP-C | BOCA DA MATA | ALAGOAS | Brasil | 2701001 | 27 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 9d185498-0fcc-354f-af5b-962c3a512687 | -5.6546 | -43.727699 | 2024-12-27 00:02:00 | METOP-C | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| f0422983-3103-328b-b6c5-8721db95dab2 | -9.8298 | -36.367298 | 2024-12-27 00:02:00 | METOP-C | JUNQUEIRO | ALAGOAS | Brasil | 2704005 | 27 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 0d406bc6-0b41-32b1-a26a-1589f8d0e3c4 | -5.6398 | -43.7071 | 2024-12-27 00:02:00 | METOP-C | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 5631d0c1-7ff7-33d6-bc8a-00710f61235f | -3.1968 | -46.114101 | 2024-12-27 00:02:00 | METOP-C | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 59595b5c-0281-3def-ab4f-7368394bd18f | -10.4981 | -36.9897 | 2024-12-27 00:02:00 | METOP-C | CAPELA | SERGIPE | Brasil | 2801306 | 28 | 33 | nan | nan | nan | Mata Atlântica | nan |
| f453d348-8b31-314c-9dbb-719727be1b32 | -9.267 | -35.585499 | 2024-12-27 00:02:00 | METOP-C | SÃO LUÍS DO QUITUNDE | ALAGOAS | Brasil | 2708501 | 27 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 926911cf-e402-3748-a72e-a7d6f34c2570 | -10.0748 | -36.266399 | 2024-12-27 00:02:00 | METOP-C | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 13185794-189c-309f-abf5-bfb811914c28 | -10.0732 | -36.2593 | 2024-12-27 00:02:00 | METOP-C | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | nan |
| db6c89c5-9cfd-3419-8aff-14a2286fb616 | -5.6423 | -43.718498 | 2024-12-27 00:02:00 | METOP-C | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| b2c43d71-091c-31f2-9508-dab15cc58e6f | -6.036 | -39.764099 | 2024-12-27 00:02:00 | METOP-C | ACOPIARA | CEARÁ | Brasil | 2300309 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| 04fa7e88-c124-359d-a109-7279218f06bf | -3.4259 | -44.896599 | 2024-12-27 00:02:00 | METOP-C | VITÓRIA DO MEARIM | MARANHÃO | Brasil | 2112902 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 3d225f5d-684d-31c3-8be6-cdbe42c3c8f1 | -5.1462 | -43.234299 | 2024-12-27 00:02:00 | METOP-C | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| a622340f-889e-354e-aff0-0afb6b2f5015 | -9.995 | -36.009399 | 2024-12-27 00:02:00 | METOP-C | JEQUIÁ DA PRAIA | ALAGOAS | Brasil | 2703759 | 27 | 33 | nan | nan | nan | Mata Atlântica | nan |
| dbc3bb33-ada2-30b4-9e59-9a19477854c2 | -4.4458 | -46.549301 | 2024-12-27 00:02:00 | METOP-C | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 99c2b05d-c503-3410-bac0-7bf2ec6a7b82 | -3.5046 | -45.753601 | 2024-12-27 00:02:00 | METOP-C | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 92348021-e3a2-37a0-98c7-7249a2325ece | -5.1387 | -43.2467 | 2024-12-27 00:02:00 | METOP-C | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 3bf36014-d44c-31ea-91cd-42e138231248 | -4.3373 | -44.253399 | 2024-12-27 00:02:00 | METOP-C | PERITORÓ | MARANHÃO | Brasil | 2108454 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 1cd2d351-5f19-3dd3-8a51-7083639a3175 | -5.1364 | -43.236401 | 2024-12-27 00:02:00 | METOP-C | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 931c357f-d2bf-3375-bc23-aa5bb95cfa47 | -5.1485 | -43.244598 | 2024-12-27 00:02:00 | METOP-C | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| f9d3600f-e86d-3a6d-ad52-c16f151a59cf | -2.9966 | -48.048698 | 2024-12-27 00:02:00 | METOP-C | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5993690b-9a34-39db-aab2-ceae29c6e356 | -4.4263 | -46.553501 | 2024-12-27 00:02:00 | METOP-C | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 400df0cc-7338-3ac9-9256-8dd08fb33772 | -2.2835 | -45.553299 | 2024-12-27 00:02:00 | METOP-C | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| d51c09b0-a03b-35cc-a82e-825ab3110361 | -5.3959 | -40.6703 | 2024-12-27 00:02:00 | METOP-C | CRATEÚS | CEARÁ | Brasil | 2304103 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| 4dd9acb9-31e1-392d-88f9-b70da41f3cc1 | -2.2768 | -45.568901 | 2024-12-27 00:02:00 | METOP-C | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 50d19e13-57f7-3674-8d27-adeed1b5f01c | -10.1069 | -36.450802 | 2024-12-27 00:02:00 | METOP-C | PENEDO | ALAGOAS | Brasil | 2706703 | 27 | 33 | nan | nan | nan | Caatinga | nan |
| bdecf8f4-6b95-3e9f-ae3e-81f9e7bc6db0 | -5.6471 | -43.693699 | 2024-12-27 00:02:00 | METOP-C | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 385e76ec-6eac-309b-ad99-19ecfcb961cf | -4.4879 | -44.332699 | 2024-12-27 00:02:00 | METOP-C | PERITORÓ | MARANHÃO | Brasil | 2108454 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 029876fe-8f85-3a99-aa16-56a78ac55486 | -10.8738 | -37.283001 | 2024-12-27 00:02:00 | METOP-C | SÃO CRISTÓVÃO | SERGIPE | Brasil | 2806701 | 28 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 7856fb36-eecb-3d83-9c65-42929c3d29fe | -9.0369 | -39.935501 | 2024-12-27 00:02:00 | METOP-C | CURAÇÁ | BAHIA | Brasil | 2909901 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| 9e12bc40-46c6-35b8-b2e3-b17a76c83ebc | -4.5247 | -42.057598 | 2024-12-27 00:02:00 | METOP-C | BOQUEIRÃO DO PIAUÍ | PIAUÍ | Brasil | 2201945 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| b1fd17c9-fd6a-3979-a48d-afa8ff123fb0 | -9.2687 | -35.592899 | 2024-12-27 00:02:00 | METOP-C | SÃO LUÍS DO QUITUNDE | ALAGOAS | Brasil | 2708501 | 27 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 8d8ba1e7-a271-3792-93f6-e0ee2095ce31 | -5.6521 | -43.7164 | 2024-12-27 00:02:00 | METOP-C | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| e8a35833-453e-3976-8816-33adef8b6ed0 | -12.1944 | -41.365799 | 2024-12-27 00:02:00 | METOP-C | LENÇÓIS | BAHIA | Brasil | 2919306 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| b437397b-8805-3d42-babc-ff0188641a4d | -6.4348 | -39.752102 | 2024-12-27 00:02:00 | METOP-C | JUCÁS | CEARÁ | Brasil | 2307403 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| b4461b8c-927e-347d-90df-8ca579d6d3bf | -5.2247 | -41.236301 | 2024-12-27 00:02:00 | METOP-C | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 57870f83-25a6-3e66-b0f6-bd142f715d94 | -3.1871 | -46.116299 | 2024-12-27 00:02:00 | METOP-C | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 6b13c8f1-97d1-3f91-91b9-c9cad1cf64e0 | -4.713 | -38.1619 | 2024-12-27 00:02:00 | METOP-C | RUSSAS | CEARÁ | Brasil | 2311801 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| 98acea5d-1e51-3d37-a8f9-9136c43dbdcf | -4.4398 | -46.568401 | 2024-12-27 00:02:00 | METOP-C | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| a4cafd91-6bef-3592-8519-830095c0730b | -3.7098 | -43.416698 | 2024-12-27 00:02:00 | METOP-C | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| f1c7b0be-73ba-3c3a-861e-613d85a2692c | -5.2533 | -41.409801 | 2024-12-27 00:02:00 | METOP-C | CASTELO DO PIAUÍ | PIAUÍ | Brasil | 2202604 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 50848637-4a5e-32d2-91e8-f865060284ae | -10.0764 | -36.273399 | 2024-12-27 00:02:00 | METOP-C | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 170487fc-1ef9-305c-b218-72968fc20809 | -1.6472 | -45.863602 | 2024-12-27 00:02:00 | METOP-C | AMAPÁ DO MARANHÃO | MARANHÃO | Brasil | 2100550 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 86e014e1-ae0e-3800-a7ce-42203b09613b | -9.1899 | -35.5648 | 2024-12-27 00:02:00 | METOP-C | PASSO DE CAMARAGIBE | ALAGOAS | Brasil | 2706505 | 27 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 798b8e5b-5676-3f5c-b46d-9ac85cdac674 | -9.8216 | -36.376598 | 2024-12-27 00:02:00 | METOP-C | JUNQUEIRO | ALAGOAS | Brasil | 2704005 | 27 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 7f5be3fa-a305-3be7-9812-613d1e875dde | -10.5456 | -36.9716 | 2024-12-27 00:02:00 | METOP-C | JAPARATUBA | SERGIPE | Brasil | 2803302 | 28 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 498b4415-e256-3dc6-a06b-68b6f2eb1ec2 | -9.0352 | -39.9277 | 2024-12-27 00:02:00 | METOP-C | CURAÇÁ | BAHIA | Brasil | 2909901 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| 07d37d21-7aa6-35a6-92f8-1a3afd5d0f08 | -11.9721 | -41.329102 | 2024-12-27 00:02:00 | METOP-C | BONITO | BAHIA | Brasil | 2904050 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| 61c64273-cc77-349b-aead-fcfdfcee10c6 | -5.3645 | -39.345699 | 2024-12-27 00:02:00 | METOP-C | QUIXERAMOBIM | CEARÁ | Brasil | 2311405 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| ee570e58-45a5-3301-ac77-8e02fabbd87f | -5.2203 | -41.262699 | 2024-12-27 00:02:00 | METOP-C | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 26a846d8-8fca-3fc7-9787-dacb05ce8d09 | -10.0846 | -36.264099 | 2024-12-27 00:02:00 | METOP-C | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | nan |
| defa13e3-b5ab-3fce-94e2-57827ced2e4e | -17.728701 | -40.186699 | 2024-12-27 00:02:00 | METOP-C | IBIRAPUÃ | BAHIA | Brasil | 2912806 | 29 | 33 | nan | nan | nan | Mata Atlântica | nan |
| d5ba3db9-8fef-3773-a37e-356bc882ccca | -4.4782 | -44.334801 | 2024-12-27 00:02:00 | METOP-C | PERITORÓ | MARANHÃO | Brasil | 2108454 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 1c177c17-770d-388e-bdb6-1b2186a54940 | -3.034 | -40.0182 | 2024-12-27 00:02:00 | METOP-C | ACARAÚ | CEARÁ | Brasil | 2300200 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| 08edd0b6-17e5-338f-b082-b275b8ffc641 | -4.5286 | -42.075001 | 2024-12-27 00:02:00 | METOP-C | BOQUEIRÃO DO PIAUÍ | PIAUÍ | Brasil | 2201945 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| e2be698e-3905-3fa9-bac1-bc3d0c5b0384 | -2.2798 | -45.582298 | 2024-12-27 00:02:00 | METOP-C | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 1f638220-8ec0-3919-b1fc-28128bca2fab | -7.3197 | -34.985298 | 2024-12-27 00:02:00 | METOP-C | ALHANDRA | PARAÍBA | Brasil | 2500601 | 25 | 33 | nan | nan | nan | Mata Atlântica | nan |
| bb8dec5e-f674-32b7-a9e6-3321f51b9113 | -9.1933 | -35.579498 | 2024-12-27 00:02:00 | METOP-C | PASSO DE CAMARAGIBE | ALAGOAS | Brasil | 2706505 | 27 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 971eba47-2e17-3845-9896-0402c7c957e7 | -10.1101 | -36.464699 | 2024-12-27 00:02:00 | METOP-C | PENEDO | ALAGOAS | Brasil | 2706703 | 27 | 33 | nan | nan | nan | Caatinga | nan |
| d242c918-146c-3d9b-8360-d078ba4aa80c | -6.912 | -39.5854 | 2024-12-27 00:02:00 | METOP-C | FARIAS BRITO | CEARÁ | Brasil | 2304301 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| 1d6895e7-7273-37c4-b48b-fac44b4ad0f8 | -5.9084 | -43.485401 | 2024-12-27 00:02:00 | METOP-C | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 48c766c2-4792-37b5-97e9-f1c37bbf5747 | -5.4057 | -40.668201 | 2024-12-27 00:02:00 | METOP-C | CRATEÚS | CEARÁ | Brasil | 2304103 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| 57d25b16-bcd8-3bb5-b118-81df3a878028 | -5.2265 | -41.2444 | 2024-12-27 00:02:00 | METOP-C | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 762857eb-5a9f-313b-b9ed-af2d0fcf2ca8 | -4.7146 | -38.168701 | 2024-12-27 00:02:00 | METOP-C | RUSSAS | CEARÁ | Brasil | 2311801 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| 47e6a2de-5719-3d64-a669-af8654e2e38a | -3.7 | -43.4188 | 2024-12-27 00:02:00 | METOP-C | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| dec2b6e0-4a4f-339a-a0de-2bb3821f7867 | -5.2514 | -41.4016 | 2024-12-27 00:02:00 | METOP-C | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 9b978f58-b6fb-3cfb-a1f5-ab1fe3143f3c | -4.7048 | -38.171001 | 2024-12-27 00:02:00 | METOP-C | RUSSAS | CEARÁ | Brasil | 2311801 | 23 | 33 | nan | nan | nan | Caatinga | nan |


[Clique aqui para ver as próximas entradas](README2.md)
