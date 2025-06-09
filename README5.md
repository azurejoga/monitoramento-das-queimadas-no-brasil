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

## Dados Diários - Página 5

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| c5a3a9cc-86ff-3749-a1da-cd2be24f9c68 | -16.6945 | -41.01911 | 2025-06-09 04:08:00 | NOAA-20 | JOAÍMA | MINAS GERAIS | Brasil | 3136009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| c0552257-1a73-3d61-af1b-219c25202561 | -14.93598 | -42.29028 | 2025-06-09 04:08:00 | NOAA-20 | MORTUGABA | BAHIA | Brasil | 2921807 | 29 | 33 | nan | nan | nan | Caatinga | 3.7 |
| 02c3a68c-c7a8-388f-9322-8d0663b11dc5 | -13.15553 | -43.26374 | 2025-06-09 04:08:00 | NOAA-20 | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 567ba601-bc31-328f-b8d4-7a3fc43eca52 | -10.64636 | -44.48009 | 2025-06-09 04:08:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 46deab84-5b35-3b23-95d7-fcfb192d16a6 | -19.96969 | -44.21717 | 2025-06-09 04:10:00 | NOAA-20 | BETIM | MINAS GERAIS | Brasil | 3106705 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 7aaf2631-d1f7-38c2-8570-6bce2e5ab21d | -19.49556 | -44.27577 | 2025-06-09 04:10:00 | NOAA-20 | SETE LAGOAS | MINAS GERAIS | Brasil | 3167202 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 3cb30fcb-a44c-3ecd-bfc6-c77dec9920aa | -18.77348 | -40.90208 | 2025-06-09 04:10:00 | NOAA-20 | BARRA DE SÃO FRANCISCO | ESPÍRITO SANTO | Brasil | 3200904 | 32 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| a40bc6d1-3333-3056-ad02-6674a98aef0e | -19.71061 | -43.96281 | 2025-06-09 04:10:00 | NOAA-20 | SÃO JOSÉ DA LAPA | MINAS GERAIS | Brasil | 3162955 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 39e5d9e7-8515-365b-939b-eca043e796df | -19.51269 | -44.275 | 2025-06-09 04:10:00 | NOAA-20 | SETE LAGOAS | MINAS GERAIS | Brasil | 3167202 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 97eaae76-844d-3f8c-ac89-8386c42ab186 | -20.41708 | -43.55435 | 2025-06-09 04:10:00 | NOAA-20 | OURO PRETO | MINAS GERAIS | Brasil | 3146107 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| 033cbaf1-57f8-3baf-b9f9-6c494e31aa37 | -19.43794 | -44.34171 | 2025-06-09 04:10:00 | NOAA-20 | SETE LAGOAS | MINAS GERAIS | Brasil | 3167202 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f685457b-35ac-3a8c-87bc-b674771d4019 | -19.45407 | -45.30593 | 2025-06-09 04:10:00 | NOAA-20 | MARTINHO CAMPOS | MINAS GERAIS | Brasil | 3140506 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 4c8f9318-d293-373d-87da-b8a8a693701c | -19.3455 | -42.766 | 2025-06-09 04:10:00 | NOAA-20 | FERROS | MINAS GERAIS | Brasil | 3125903 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 2499d2f7-8be4-3193-92df-804aab21148a | -19.71708 | -40.35272 | 2025-06-09 04:10:00 | NOAA-20 | JOÃO NEIVA | ESPÍRITO SANTO | Brasil | 3203130 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 78d5f92a-4d3b-3f80-abc0-89dffca92d77 | -19.4691 | -44.29467 | 2025-06-09 04:10:00 | NOAA-20 | SETE LAGOAS | MINAS GERAIS | Brasil | 3167202 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| d1280053-85ec-3ae8-bfae-89b94fdd9021 | -20.41764 | -43.5506 | 2025-06-09 04:10:00 | NOAA-20 | OURO PRETO | MINAS GERAIS | Brasil | 3146107 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| 21a39059-aca9-384f-9653-eac5e47c37d8 | -20.37795 | -45.60248 | 2025-06-09 04:10:00 | NOAA-20 | PAINS | MINAS GERAIS | Brasil | 3146503 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| e3d1a4a6-e957-300c-81e1-d04734fa2993 | 0.91519 | -52.09651 | 2025-06-09 04:55:00 | NOAA-21 | PEDRA BRANCA DO AMAPARI | AMAPÁ | Brasil | 1600154 | 16 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 89f2d34b-d44d-3566-b240-1a7fa5b9a281 | -3.03361 | -47.86533 | 2025-06-09 04:55:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c525105c-f17d-385b-88b4-de56157f31c5 | -3.05107 | -49.43496 | 2025-06-09 04:55:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| dc672895-688a-3dee-a5f9-38fad815c3e0 | -2.58772 | -51.91889 | 2025-06-09 04:55:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 40bbe4af-f594-35aa-8995-cead07f83ad4 | -3.26497 | -48.9793 | 2025-06-09 04:55:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 17379745-4920-35d9-b143-464375eb529c | -7.01725 | -44.59394 | 2025-06-09 04:57:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 54240275-3a32-3891-aee1-63f9c4a717a5 | -7.02001 | -44.60898 | 2025-06-09 04:57:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 813fdd07-12bb-337e-9b0c-bb7e28fdca91 | -7.24189 | -45.45064 | 2025-06-09 04:57:00 | NOAA-21 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c679f8dc-523c-328e-9d63-85a689db069c | -9.40471 | -48.44235 | 2025-06-09 04:57:00 | NOAA-21 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 9f0c683f-d5de-3cec-b615-9cd5bfc732f8 | -9.41237 | -48.44553 | 2025-06-09 04:57:00 | NOAA-21 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| d3f2fee1-e556-32cd-8cf9-640b012bbd16 | -9.41038 | -48.43418 | 2025-06-09 04:57:00 | NOAA-21 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 75d96409-e795-3bad-84fd-d2880b75a01c | -7.02079 | -44.6095 | 2025-06-09 04:57:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 370f4589-cfd1-3202-8727-da70ee11d0ab | -6.74235 | -44.99292 | 2025-06-09 04:57:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 74077d07-e87a-32d0-8d9e-98f1b17cce45 | -7.01778 | -44.59013 | 2025-06-09 04:57:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 2dd73dff-02a7-3a74-af3f-7af772ad9b4d | -7.0244 | -44.57539 | 2025-06-09 04:57:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 32ea49ff-4b6f-3076-84a7-dbe4cde386d5 | -7.87318 | -47.89577 | 2025-06-09 04:57:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a5c71794-9dd5-3e54-a017-124a9a2d86e3 | -9.4174 | -48.44174 | 2025-06-09 04:57:00 | NOAA-21 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| ed9b6038-a1e1-3c38-b27b-91501b728339 | -8.87445 | -50.1866 | 2025-06-09 04:57:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 075ed112-2b65-33f7-8b1e-540a7275a307 | -9.41357 | -48.44369 | 2025-06-09 04:57:00 | NOAA-21 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| cc271d56-d416-3b59-92ff-1b98f615dc0f | -9.40976 | -48.4386 | 2025-06-09 04:57:00 | NOAA-21 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 51e8ff38-c5d2-3b5d-bd74-26e55689ee00 | -9.40584 | -48.4265 | 2025-06-09 04:57:00 | NOAA-21 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| e96608fa-3fea-3a61-8f45-62e80f9ffac1 | -10.21097 | -46.94222 | 2025-06-09 04:57:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| ed2c53e6-05a0-352f-a3bf-3b36e90d5475 | -10.26502 | -46.99275 | 2025-06-09 04:57:00 | NOAA-21 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 44f7a159-bf6d-3191-ba8a-c9254946c985 | -7.00814 | -44.61889 | 2025-06-09 04:57:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 3ec1bf2b-014c-31bf-a18e-6c06b7c13493 | -7.01622 | -44.60145 | 2025-06-09 04:57:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 9e7c3154-4dc0-3083-a6a9-0769b0272e25 | -9.41681 | -48.44618 | 2025-06-09 04:57:00 | NOAA-21 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| a8d1e577-f75b-3561-bd3b-63341124ae01 | -7.24098 | -45.45295 | 2025-06-09 04:57:00 | NOAA-21 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 7caf0282-af76-34e7-a7a6-d7568109feca | -10.02809 | -49.13249 | 2025-06-09 04:57:00 | NOAA-21 | MONTE SANTO DO TOCANTINS | TOCANTINS | Brasil | 1713700 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a01fcff8-2a18-3bc4-a2fd-8a62a900ca30 | -7.02343 | -44.58281 | 2025-06-09 04:57:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 0a1d2cd6-120a-3556-9637-b23fb55ac51b | -9.40532 | -48.43795 | 2025-06-09 04:57:00 | NOAA-21 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 782cdcc2-a793-3c53-92fc-7fab14d4b7d1 | -7.87059 | -47.89683 | 2025-06-09 04:57:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 337102b7-f4fb-3e0c-9911-600086a112cb | -7.04761 | -55.43156 | 2025-06-09 04:57:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d5844b69-da22-3bb8-b5c1-8907ad9ed41c | -7.0183 | -44.58635 | 2025-06-09 04:57:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| f8a0bab2-e81e-3511-810d-70578d320d18 | -9.41355 | -48.43665 | 2025-06-09 04:57:00 | NOAA-21 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 12800f28-60b5-3738-b8a6-64bfea9d7310 | -7.01984 | -44.57514 | 2025-06-09 04:57:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| bcfecdbb-7063-3650-9289-4ff1b409761b | -7.01902 | -44.61663 | 2025-06-09 04:57:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| da72b6cc-6627-3379-b627-3794bc9ce2f6 | -6.01466 | -45.77242 | 2025-06-09 04:57:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| bf271ca8-cb36-3cc3-92d7-1bed3b13fd97 | -9.08014 | -47.14883 | 2025-06-09 04:57:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 8cb9f5a5-7dc5-3864-89c0-257a3c3410e0 | -6.87258 | -47.24808 | 2025-06-09 04:57:00 | NOAA-21 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f9a64060-9867-3ea5-ba8e-268bcaa8fecb | -4.27089 | -48.62127 | 2025-06-09 04:57:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 1732e62d-4690-38a5-a437-e4e2a7edd5b6 | -4.48665 | -43.77499 | 2025-06-09 04:57:00 | NOAA-21 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 699c6509-6ff9-336c-b756-7f801c899441 | -7.23698 | -45.44722 | 2025-06-09 04:57:00 | NOAA-21 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 0d23d8bd-6bb8-3b59-8b28-df32f1fcf6cd | -7.27555 | -44.22651 | 2025-06-09 04:57:00 | NOAA-21 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 1402922e-dd0d-310c-a0b8-3a5c7ada298a | -7.01952 | -44.61277 | 2025-06-09 04:57:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 37975a3e-c8e8-329a-816a-52ec7cd8474c | -6.2184 | -48.54198 | 2025-06-09 04:57:00 | NOAA-21 | SÃO GERALDO DO ARAGUAIA | PARÁ | Brasil | 1507458 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| acdfbcce-df1e-324e-8881-7d85b01a73b5 | -7.24145 | -45.45381 | 2025-06-09 04:57:00 | NOAA-21 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 35a89990-95e4-37b4-853b-9578345829db | -7.0244 | -44.58336 | 2025-06-09 04:57:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 601612c1-34db-3922-899a-d94178f3b28c | -7.28239 | -44.21916 | 2025-06-09 04:57:00 | NOAA-21 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 410e5a1c-4438-3ab6-9906-03f3a9c7f4ea | -7.58993 | -45.9936 | 2025-06-09 04:57:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 0839e4ae-dd60-3049-b125-f8f995e517ac | -7.93285 | -61.55845 | 2025-06-09 04:57:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8d380541-e9a9-3d1d-bedc-8178d6121252 | -9.41295 | -48.44808 | 2025-06-09 04:57:00 | NOAA-21 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| e75260b7-bf15-3968-9c4f-3562d390d0f8 | -7.65597 | -46.1034 | 2025-06-09 04:57:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 0ca31217-679b-3690-9c50-618b64672e83 | -5.47805 | -46.22769 | 2025-06-09 04:57:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 82cd77fb-1acd-3c7f-8466-c9cca0d79c33 | -9.40911 | -48.43599 | 2025-06-09 04:57:00 | NOAA-21 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| ff05173c-475f-3a90-a47d-4f73a883651b | -10.25617 | -46.90769 | 2025-06-09 04:57:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b435121e-7d57-3475-b384-e9addd01111f | -7.27609 | -44.22249 | 2025-06-09 04:57:00 | NOAA-21 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| e236a167-4066-34d7-91f4-f41e4400da96 | -9.40212 | -48.42847 | 2025-06-09 04:57:00 | NOAA-21 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 0d498599-5567-3fc5-885f-81f795800f4f | -7.02294 | -44.58654 | 2025-06-09 04:57:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 36fe5490-b710-3931-bca8-7f1d71426d13 | -7.87382 | -47.89127 | 2025-06-09 04:57:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b3e3af23-408c-3c57-a295-ef6489a4b73d | -9.40852 | -48.44043 | 2025-06-09 04:57:00 | NOAA-21 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| f6087717-e89a-362c-8b78-a99979e5aef1 | -7.01933 | -44.57885 | 2025-06-09 04:57:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 71ff7903-b337-337c-8fd5-5b542c99b7e3 | -7.35213 | -45.38155 | 2025-06-09 04:57:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a0600c82-9aaa-3be1-aca0-1a5ad68b491e | -7.02541 | -44.57601 | 2025-06-09 04:57:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 3278eeef-1756-3cd9-819b-6deda708b811 | -9.41296 | -48.44109 | 2025-06-09 04:57:00 | NOAA-21 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| c6b3f793-56e7-34f2-a562-2d1e048922a6 | -6.23754 | -48.52864 | 2025-06-09 04:57:00 | NOAA-21 | SÃO GERALDO DO ARAGUAIA | PARÁ | Brasil | 1507458 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 9f5dd8a0-6fff-39ac-98d3-241be0846555 | -7.0157 | -44.6052 | 2025-06-09 04:57:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 1d5e904a-7012-3a4b-801b-cea0dee3d476 | -10.24538 | -46.91237 | 2025-06-09 04:57:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 08e1cc82-80e6-3788-8362-1274ea43c90d | -8.96495 | -47.97297 | 2025-06-09 04:57:00 | NOAA-21 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 72be321e-9000-3659-9f8d-b649ee57f242 | -7.01519 | -44.60895 | 2025-06-09 04:57:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 3f9c595e-8d40-3cff-bb26-373b0fce4677 | -6.23277 | -48.5318 | 2025-06-09 04:57:00 | NOAA-21 | SÃO GERALDO DO ARAGUAIA | PARÁ | Brasil | 1507458 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 989ae6a8-dfb4-3df3-b100-c902253b151c | -7.65638 | -46.10042 | 2025-06-09 04:57:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| a3cd70c0-9915-3f50-a96f-00310346e5ab | -8.0115 | -46.78539 | 2025-06-09 04:57:00 | NOAA-21 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 2b9108a0-a567-39d0-876e-fc92e7b1127b | -10.21628 | -46.94037 | 2025-06-09 04:57:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 12c8348c-588e-3669-a52b-d1373f88e687 | -6.21899 | -48.5379 | 2025-06-09 04:57:00 | NOAA-21 | SÃO GERALDO DO ARAGUAIA | PARÁ | Brasil | 1507458 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7dd612b0-b063-3a10-bef0-8095258a6d91 | -9.40914 | -48.44302 | 2025-06-09 04:57:00 | NOAA-21 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| ae0dc1a0-cba2-3261-b70d-496a5b8bfac7 | -9.92222 | -49.83163 | 2025-06-09 04:57:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 512f548c-dbb4-3651-8538-bf288936f30d | -7.00965 | -44.60792 | 2025-06-09 04:57:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| a7b88c6e-2f38-3904-beba-aa66989257e1 | -8.3957 | -46.34063 | 2025-06-09 04:57:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 86616322-30e4-3a2f-90bf-5873554e0765 | -10.24999 | -46.91592 | 2025-06-09 04:57:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b73e21df-1732-3921-99ef-9a32740c8682 | -10.25607 | -46.91085 | 2025-06-09 04:57:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 3650110c-efcf-3ddc-a667-cc3a00833516 | -9.40793 | -48.44484 | 2025-06-09 04:57:00 | NOAA-21 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 13ef187c-cb90-3b2d-9e72-adfc9cd2a074 | -9.05299 | -47.91003 | 2025-06-09 04:57:00 | NOAA-21 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e5a0f424-28af-3eb0-9e96-7fc490e2b08d | -7.35337 | -45.38117 | 2025-06-09 04:57:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |


[Clique aqui para ver as próximas entradas](README6.md)
