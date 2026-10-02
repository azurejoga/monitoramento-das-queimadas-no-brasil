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

## Dados Diários - Página 3

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 935f02a3-aeeb-3d24-a9e7-23465e937a6a | -12.1861 | -48.4124 | 2026-10-02 00:20:00 | GOES-19 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 70.3 |
| 70e30c73-1fdf-32de-9123-96e29fb7f7e4 | -11.6977 | -43.5128 | 2026-10-02 00:20:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 113.0 |
| ddb63cda-5250-33b5-b090-e35e8151fd2a | -11.4695 | -43.4062 | 2026-10-02 00:20:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 66.0 |
| 03870cd7-f4be-383f-a241-fd8ec27cf8ba | -11.3425 | -51.3182 | 2026-10-02 00:20:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 72.0 |
| b10bf839-aca0-340e-9e4d-cf30251568cd | -4.286 | -50.7707 | 2026-10-02 00:20:00 | GOES-19 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 72.9 |
| 1443409b-7654-39a7-bb30-228cd1effd29 | -9.8925 | -60.2945 | 2026-10-02 00:20:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 67.4 |
| 63bfaf94-26e9-3bb5-a3d8-2a8d07982ee8 | -11.1615 | -44.6002 | 2026-10-02 00:20:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 91.0 |
| 2256a9ec-7ae3-39df-af8e-575efda300ad | -3.0189 | -53.9675 | 2026-10-02 00:20:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 73.5 |
| cb734fcb-5e18-3c1e-881c-53b8d8990708 | -6.8952 | -43.6833 | 2026-10-02 00:20:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 116.1 |
| 2be1080c-4857-3748-b29d-0ca3a209d164 | -11.1424 | -44.6029 | 2026-10-02 00:20:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 166.2 |
| eae3b8a7-bc52-30bd-82ae-76ad9d4ce462 | -9.5335 | -45.3405 | 2026-10-02 00:20:00 | GOES-19 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 107.4 |
| 106b8821-a78f-3ed5-98c5-86dddcd7b098 | -9.4959 | -45.3221 | 2026-10-02 00:20:00 | GOES-19 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 63.4 |
| 1548ff87-0c5d-3f0f-9407-9a4bbe7074aa | -7.0478 | -55.6302 | 2026-10-02 00:20:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 117.0 |
| 3502f533-fb67-3adc-9b69-bb2dff238c01 | -11.4955 | -47.462 | 2026-10-02 00:20:00 | GOES-19 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 115.7 |
| af0abe8a-9769-353c-bd98-1d4e33685332 | -11.4764 | -47.4645 | 2026-10-02 00:20:00 | GOES-19 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 187.4 |
| 823a9adf-d188-330b-822e-09ac50f83545 | -5.7355 | -43.2916 | 2026-10-02 00:20:00 | GOES-19 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 54.9 |
| 0c67e807-ccc9-33b0-9538-f7f44630b26f | -18.6573 | -41.6456 | 2026-10-02 00:20:00 | GOES-19 | GOVERNADOR VALADARES | MINAS GERAIS | Brasil | 3127701 | 31 | 33 | nan | nan | nan | Mata Atlântica | 98.7 |
| 4eb04a37-5687-3d16-ae74-d033cb567523 | -3.1655 | -54.0844 | 2026-10-02 00:20:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 107.5 |
| 8e9274d7-16a2-3f0f-8807-8c2c174a8eb2 | 1.8037 | -55.6051 | 2026-10-02 00:20:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 61.1 |
| 88f76f5e-e5f4-3e4b-8cdd-29d2ac1cb3bf | -4.2954 | -49.0807 | 2026-10-02 00:20:00 | GOES-19 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 141.8 |
| fbd9f8bf-e6eb-388c-bdf2-46f0ac4af6ea | -12.8056 | -51.4702 | 2026-10-02 00:20:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 84.1 |
| 406c3add-e2f8-3eb1-810b-829483a78787 | -12.8247 | -51.4679 | 2026-10-02 00:20:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 139.1 |
| 35b6a424-91d9-38ea-9a0d-e1e208c6a730 | -2.8897 | -54.1313 | 2026-10-02 00:20:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 60.5 |
| d072bb14-c998-37b0-9c7f-8822fd0ab472 | -6.4137 | -56.415 | 2026-10-02 00:20:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 78.3 |
| 8075966b-7bd1-3103-bd97-d06d83b2be64 | -3.1655 | -54.1045 | 2026-10-02 00:20:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 64.2 |
| 1c762f9d-fdcf-3741-8ef3-ca4b4a48f52d | -7.2013 | -52.6066 | 2026-10-02 00:20:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 67.7 |
| 22890a3a-83ad-35c8-8bb7-83fff5bf2ae6 | -7.2013 | -52.6066 | 2026-10-02 00:30:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 62.5 |
| 86620b49-62df-3718-8237-c7abcc488b76 | -12.7877 | -51.3873 | 2026-10-02 00:30:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 68.6 |
| 02ffb6fc-3789-3102-bcd8-a362d9c77bbe | -12.7881 | -51.366 | 2026-10-02 00:30:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 68.4 |
| eb6957cc-adc2-34ad-97ea-323bdaa7927a | -11.7926 | -43.5689 | 2026-10-02 00:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 201.3 |
| dbc91167-b144-38a6-a4ce-670da3a4951e | -11.4695 | -43.4062 | 2026-10-02 00:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 110.6 |
| a8017ee4-b7b9-3cf7-95f6-d94152c8f77a | -7.0477 | -55.6501 | 2026-10-02 00:30:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 95.7 |
| 8391e0ce-8323-3cd7-85e2-0ab27de11372 | -3.1655 | -54.1045 | 2026-10-02 00:30:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 73.3 |
| 24c5caf2-c188-3cd8-86e5-8efa00f91909 | -11.6771 | -43.587 | 2026-10-02 00:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 81.9 |
| 31ccf63c-5447-3888-9e03-2fe4fdafb517 | -11.7375 | -43.4356 | 2026-10-02 00:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 109.0 |
| 51e0f915-f583-335a-ba48-f001b3884ecf | -6.3952 | -56.4158 | 2026-10-02 00:30:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 94.1 |
| 86973de3-e5ae-36cf-a5a3-353d6fa17c67 | -11.7169 | -43.5098 | 2026-10-02 00:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 87.5 |
| b5fdcc5c-7e64-341c-98e8-f463095bc313 | -12.1861 | -48.4124 | 2026-10-02 00:30:00 | GOES-19 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 67.1 |
| f2588871-381a-3878-8a36-a517ee635e91 | -13.1348 | -51.2169 | 2026-10-02 00:30:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 127.2 |
| 5e72c136-1a63-37cc-b760-903bb59c4bb9 | -3.1655 | -54.0844 | 2026-10-02 00:30:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 93.2 |
| 22fa4636-d4ed-3aae-86e7-4f7488e15bf9 | -7.8308 | -55.1262 | 2026-10-02 00:30:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 81.0 |
| 93e6c87f-3531-306a-b7c2-9b51eff429e8 | -12.1857 | -48.4345 | 2026-10-02 00:30:00 | GOES-19 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 66.2 |
| 5ea26b45-e696-396e-a355-60808d048f4a | -6.914 | -43.6816 | 2026-10-02 00:30:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 109.1 |
| 0e7d4aee-afc6-37b1-acc7-8ef2dd128978 | -3.1838 | -54.104 | 2026-10-02 00:30:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 113.1 |
| 7ca8ac27-352b-31a7-a5a2-a4a69c65b81f | -9.4959 | -45.3221 | 2026-10-02 00:30:00 | GOES-19 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 62.2 |
| 90e4e82e-24e4-3fda-9c62-e793b8695978 | -11.6977 | -43.5128 | 2026-10-02 00:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 130.8 |
| bc51f8e6-ce1c-3306-b84d-de726761b6f4 | -3.1839 | -54.0839 | 2026-10-02 00:30:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 86.6 |
| f2bb1db6-4dac-3a39-9b6f-802c6ecb10a1 | -4.286 | -50.7707 | 2026-10-02 00:30:00 | GOES-19 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 71.5 |
| c12ebc20-2564-313e-a24b-f7b183145fcd | -11.7738 | -43.5482 | 2026-10-02 00:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 105.5 |
| b5f3111b-c572-3878-a940-acf50f0f91b3 | -11.6959 | -43.6077 | 2026-10-02 00:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 147.9 |
| 07327061-6919-3498-8184-a2628f200f16 | -11.4499 | -43.4329 | 2026-10-02 00:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 92.9 |
| d3a049a0-fd14-3145-aa2c-2ff707fcd6e3 | -11.142 | -44.6261 | 2026-10-02 00:30:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 89.7 |
| a5a939f7-7812-3547-80d5-4ecefb527524 | -13.1153 | -51.2407 | 2026-10-02 00:30:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 195.6 |
| 8572f6bf-152b-3350-a98f-f043e199e57d | -6.7199 | -44.2771 | 2026-10-02 00:30:00 | GOES-19 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 57.8 |
| 00b1c2f5-ee8e-38c8-87d4-a6f18189d197 | -11.6964 | -43.584 | 2026-10-02 00:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 130.2 |
| be5a6b5d-3c0d-35d7-83b9-7eb02bd63f2e | -11.4503 | -43.4091 | 2026-10-02 00:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 77.2 |
| acf30b97-4914-38f8-8171-7eadf185ddd3 | -3.1483 | -53.7426 | 2026-10-02 00:30:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 39.5 |
| babab8d4-23f8-301c-8aa4-e306073a24a0 | -9.5146 | -45.3427 | 2026-10-02 00:30:00 | GOES-19 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 109.4 |
| a962b638-23ad-3a84-9134-64a006c1a453 | -11.4691 | -43.4299 | 2026-10-02 00:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 180.4 |
| b87443c9-7aa7-3222-a4e0-af8e384b299f | -5.7563 | -45.152 | 2026-10-02 00:30:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 85.7 |
| 153fba92-7299-3494-b293-9c52722f08c4 | -4.2954 | -49.0807 | 2026-10-02 00:30:00 | GOES-19 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 147.4 |
| a35ef103-12d9-315e-b791-143b81ab0c0d | -9.5149 | -45.3199 | 2026-10-02 00:30:00 | GOES-19 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 120.9 |
| d8592110-9555-35c1-88ed-b7ba05dd4408 | -2.8897 | -54.1514 | 2026-10-02 00:30:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 54.2 |
| 17370481-308f-3f24-b50c-e3cffb3ea5eb | -4.2676 | -50.7506 | 2026-10-02 00:30:00 | GOES-19 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 116.1 |
| 834a8ff0-860b-3498-b7eb-19259b84144f | -6.9132 | -59.2806 | 2026-10-02 00:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 48.7 |
| e8ae907c-ab28-3500-b3b1-5297cc404a31 | -11.4764 | -47.4645 | 2026-10-02 00:30:00 | GOES-19 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 115.1 |
| 0c78ca99-af68-3afa-9d54-71f4df8c74f2 | -5.8966 | -53.4975 | 2026-10-02 00:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 70.3 |
| 175d853e-c2b5-3428-a4f8-07091a439278 | -6.8952 | -43.6833 | 2026-10-02 00:30:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 92.1 |
| 5b7481fd-e696-3b0b-8b7c-c02fd3b7ffba | -11.1615 | -44.6002 | 2026-10-02 00:30:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 145.9 |
| 7f52161a-fc6d-3d6d-8302-8fc372138c3d | 1.8037 | -55.6051 | 2026-10-02 00:30:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 78.0 |
| c1129119-f673-3f0e-83b3-2a6cf18de63b | -7.2889 | -55.5973 | 2026-10-02 00:30:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 83.4 |
| c18e8ada-1079-3dbb-950a-5dcd48df14ba | -13.1156 | -51.2193 | 2026-10-02 00:30:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 101.1 |
| d7d19a28-710a-39fb-a356-40db9b1c273d | -11.8118 | -43.5659 | 2026-10-02 00:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 83.4 |
| 8eab514c-e7e6-354d-9214-e17e59831f8f | -11.1232 | -44.6056 | 2026-10-02 00:30:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 76.4 |
| 41631bfc-fa04-3221-bbd4-cf512de23efa | -11.1427 | -44.5796 | 2026-10-02 00:30:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 94.9 |
| caea0bf0-7134-31db-8561-d44bdf51c068 | -13.1345 | -51.2383 | 2026-10-02 00:30:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 195.9 |
| 02f02192-994b-365f-be92-a3aeb1c761fb | -4.2953 | -49.1021 | 2026-10-02 00:30:00 | GOES-19 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 204.1 |
| 7699f45f-b4b2-3bfb-a1ce-6f02761b6031 | -7.0478 | -55.6302 | 2026-10-02 00:30:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 107.8 |
| c904f078-23ab-33a5-b483-2a498579f10f | -3.1656 | -54.0643 | 2026-10-02 00:30:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 48.4 |
| ffa800a1-1a3b-3f42-a1a7-78cf7996a16e | -11.793 | -43.5452 | 2026-10-02 00:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 73.6 |
| c49415ee-3537-3509-9a1e-eb6af2ce0b99 | -11.7541 | -43.5749 | 2026-10-02 00:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 101.7 |
| aa7026e8-e89b-337f-82a8-d3c6fe986553 | -2.8897 | -54.1313 | 2026-10-02 00:30:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 56.6 |
| 466be9fc-55d8-3f1f-9a2a-0fa7f798f12a | -4.2677 | -50.7297 | 2026-10-02 00:30:00 | GOES-19 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 71.8 |
| 5242c1a4-6f7b-3510-81a3-befeb67d2105 | -11.7733 | -43.5719 | 2026-10-02 00:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 180.7 |
| 45ec78a8-d33e-345d-9c4e-203f2b6ab790 | -12.5329 | -43.091 | 2026-10-02 00:30:00 | GOES-19 | PARATINGA | BAHIA | Brasil | 2923704 | 29 | 33 | nan | nan | nan | Caatinga | 90.6 |
| 9528003c-095a-369b-a5b5-4cf6b54921d5 | -2.0393 | -56.8789 | 2026-10-02 00:30:00 | GOES-19 | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | 63.5 |
| 8669032d-94d8-36a7-a9a4-058ff5ef8e3d | -11.1424 | -44.6029 | 2026-10-02 00:30:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 288.3 |
| 9efee13a-212d-3296-b56a-0d45854f0824 | -18.6573 | -41.6456 | 2026-10-02 00:30:00 | GOES-19 | GOVERNADOR VALADARES | MINAS GERAIS | Brasil | 3127701 | 31 | 33 | nan | nan | nan | Mata Atlântica | 95.2 |
| bb7c3c2f-6d0e-3b9a-b00d-3ac1aa56471e | -11.6767 | -43.6106 | 2026-10-02 00:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 104.0 |
| e777e34d-caab-37d8-a50c-deac93f1c6e6 | -3.1299 | -53.7431 | 2026-10-02 00:30:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 51.3 |
| ea213a21-e46a-3757-abc8-542c1207ceef | -7.7219 | -54.8114 | 2026-10-02 00:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 82.6 |
| 67519eaa-7435-3a92-8fd0-02dc878dd05e | -2.0577 | -56.8591 | 2026-10-02 00:40:00 | GOES-19 | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | 68.3 |
| 3e655cfc-96c8-3448-80b2-4b1c809b160b | -11.793 | -43.5452 | 2026-10-02 00:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 75.0 |
| c36ef940-d2e0-34a9-ac86-8df620046e5a | -11.6981 | -43.4891 | 2026-10-02 00:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 71.8 |
| 4e59a4d6-03dc-3c01-8142-4c6ce9f170ef | -11.7169 | -43.5098 | 2026-10-02 00:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 79.5 |
| 493b8812-b135-33c7-b65e-47bef1e7885b | -3.1838 | -54.104 | 2026-10-02 00:40:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 67.1 |
| b7c2042f-cea4-3dc8-8523-d6e6fa8cabeb | -6.914 | -43.6816 | 2026-10-02 00:40:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 115.8 |
| fd35cb45-7204-3a00-80ac-d7e3cf534fde | -12.7881 | -51.366 | 2026-10-02 00:40:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 78.6 |
| f8e3030c-561f-33c5-aac6-083c32761588 | -12.8244 | -51.4892 | 2026-10-02 00:40:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 62.5 |
| 25f9d153-960f-3c8e-93e6-dd35f97ceb61 | -12.8069 | -51.385 | 2026-10-02 00:40:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 55.1 |


[Clique aqui para ver as próximas entradas](README4.md)
