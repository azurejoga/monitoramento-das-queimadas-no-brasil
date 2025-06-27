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

## Dados Diários - Página 2

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| d0b78712-b4fb-31b8-8965-07a241c39359 | -14.4281 | -48.8649 | 2025-06-27 00:20:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 53.2 |
| 04e29b14-0819-3c9c-b8d0-cf67b5b2c403 | -6.1789 | -48.0929 | 2025-06-27 00:20:00 | GOES-19 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 393.9 |
| fc198612-6f04-32ee-b9a0-ef0cff063883 | -21.58855 | -41.28922 | 2025-06-27 00:20:00 | TERRA_M-M | CAMPOS DOS GOYTACAZES | RIO DE JANEIRO | Brasil | 3301009 | 33 | 33 | nan | nan | nan | Mata Atlântica | 8.4 |
| 9bab79d3-e521-3bfe-b6af-ce5c9cfbc3d0 | -20.2529 | -46.74078 | 2025-06-27 00:20:00 | TERRA_M-M | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 11.9 |
| f3388457-f831-3458-b5cd-e2db6c7ec1bb | -21.58987 | -41.29869 | 2025-06-27 00:20:00 | TERRA_M-M | CAMPOS DOS GOYTACAZES | RIO DE JANEIRO | Brasil | 3301009 | 33 | 33 | nan | nan | nan | Mata Atlântica | 14.5 |
| 30ecfa35-09e5-3162-92ae-044c8d287d2e | -18.7492 | -40.07492 | 2025-06-27 00:20:00 | TERRA_M-M | SÃO MATEUS | ESPÍRITO SANTO | Brasil | 3204906 | 32 | 33 | nan | nan | nan | Mata Atlântica | 6.6 |
| 847785df-e1ce-3ca3-9097-d9c0911c1e61 | -7.73841 | -41.96883 | 2025-06-27 00:22:00 | TERRA_M-M | SIMPLÍCIO MENDES | PIAUÍ | Brasil | 2210805 | 22 | 33 | nan | nan | nan | Caatinga | 5.6 |
| 7dc1fffd-f692-3ae7-8dff-a4720f0a176c | -13.04164 | -48.83527 | 2025-06-27 00:22:00 | TERRA_M-M | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 14.5 |
| f53ea355-34fd-3ec9-bdc6-e6bcb7534cc4 | -11.14347 | -47.03924 | 2025-06-27 00:22:00 | TERRA_M-M | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 7aa1eaff-b996-388b-a12d-72a70fb02789 | -12.04224 | -48.07203 | 2025-06-27 00:22:00 | TERRA_M-M | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 9.6 |
| ce151136-d840-37e1-80d1-a7644bd3e7c9 | -8.30827 | -44.8973 | 2025-06-27 00:22:00 | TERRA_M-M | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 12.6 |
| 9868d275-6979-3bc7-9a2e-8b6614a9a773 | -10.24476 | -47.67876 | 2025-06-27 00:22:00 | TERRA_M-M | SANTA TEREZA DO TOCANTINS | TOCANTINS | Brasil | 1719004 | 17 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 53e24007-f262-356c-a1a9-5d955ee0b390 | -12.0454 | -48.07983 | 2025-06-27 00:22:00 | TERRA_M-M | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 30.3 |
| 27d8ac55-d6a9-381a-a372-c5c19a5cd12b | -8.37152 | -51.08611 | 2025-06-27 00:22:00 | TERRA_M-M | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 30.4 |
| d6c978cb-562a-38a3-ad66-eedea9658bec | -10.82051 | -53.75225 | 2025-06-27 00:22:00 | TERRA_M-M | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 42.0 |
| 5c8533b2-fc52-3464-9be9-446c0ef7cd04 | -12.03414 | -48.75322 | 2025-06-27 00:22:00 | TERRA_M-M | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 16.0 |
| c7259a72-ed2d-3ed9-8069-6c698818548b | -11.58366 | -52.14754 | 2025-06-27 00:22:00 | TERRA_M-M | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 63.2 |
| fa3b0c57-470f-3880-ac26-842c3e62f5c8 | -8.47808 | -48.26129 | 2025-06-27 00:22:00 | TERRA_M-M | TUPIRATINS | TOCANTINS | Brasil | 1721307 | 17 | 33 | nan | nan | nan | Cerrado | 35.4 |
| 6a77e250-03a7-33d2-a24a-feb075c0f514 | -7.534 | -45.83157 | 2025-06-27 00:22:00 | TERRA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 52.9 |
| c2124343-0cbc-3f69-97f5-7c6cf15ad1c2 | -8.49519 | -48.26659 | 2025-06-27 00:22:00 | TERRA_M-M | TUPIRATINS | TOCANTINS | Brasil | 1721307 | 17 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 2a44c307-c2c8-3f37-a744-aeba48cd9fb4 | -8.47983 | -48.27447 | 2025-06-27 00:22:00 | TERRA_M-M | TUPIRATINS | TOCANTINS | Brasil | 1721307 | 17 | 33 | nan | nan | nan | Cerrado | 20.6 |
| 2c5417bf-403e-3c6d-a51e-a88c7606a7a1 | -13.03954 | -48.81816 | 2025-06-27 00:22:00 | TERRA_M-M | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 38.6 |
| 5e2e2786-caee-3f19-9fdf-6e3d80f4b522 | -12.04407 | -48.08637 | 2025-06-27 00:22:00 | TERRA_M-M | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 10.1 |
| bf506563-5060-32e0-bcd9-d839a2478c81 | -7.55335 | -45.83832 | 2025-06-27 00:22:00 | TERRA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 22.0 |
| be8ce2d7-7874-3a3c-8e75-8627335f7d76 | -14.44562 | -48.86554 | 2025-06-27 00:22:00 | TERRA_M-M | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 120.6 |
| c8f3b12a-7efb-3a10-964f-7a9b3a658344 | -9.82545 | -48.37645 | 2025-06-27 00:22:00 | TERRA_M-M | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 8.9 |
| ce15de7f-ea1a-3625-9dc3-0888ea603f4c | -12.77197 | -44.40233 | 2025-06-27 00:22:00 | TERRA_M-M | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 13.1 |
| 0fbc293c-c3d3-37ba-a4a9-46c09b7278b5 | -8.36903 | -51.06518 | 2025-06-27 00:22:00 | TERRA_M-M | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 14.7 |
| b4b14d06-6744-3d86-a20e-ad265776d59d | -8.62729 | -51.5908 | 2025-06-27 00:22:00 | TERRA_M-M | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 75.5 |
| 5859e052-dd49-30d3-9da7-11db4cead9b3 | -7.54304 | -45.83028 | 2025-06-27 00:22:00 | TERRA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 42.6 |
| 9dca2471-a583-319f-a4cc-00a43374a480 | -7.21749 | -43.08488 | 2025-06-27 00:22:00 | TERRA_M-M | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 173.1 |
| 99d516a1-6f26-3713-a6e4-9072d45b7107 | -8.48864 | -48.25988 | 2025-06-27 00:22:00 | TERRA_M-M | TUPIRATINS | TOCANTINS | Brasil | 1721307 | 17 | 33 | nan | nan | nan | Cerrado | 14.3 |
| f849e1e7-36a3-31cd-8233-1305b42fb1ef | -11.56521 | -52.12006 | 2025-06-27 00:22:00 | TERRA_M-M | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 214.9 |
| f96b16a1-508d-30b1-85a8-bd90aca81424 | -11.36723 | -48.70877 | 2025-06-27 00:22:00 | TERRA_M-M | ALIANÇA DO TOCANTINS | TOCANTINS | Brasil | 1700350 | 17 | 33 | nan | nan | nan | Cerrado | 60.4 |
| b938369a-b744-3a53-a687-c3b5251cc7e3 | -8.3752 | -51.09231 | 2025-06-27 00:22:00 | TERRA_M-M | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 20.4 |
| 8e061af3-3348-3657-9118-6c11c10143cd | -7.5443 | -45.83963 | 2025-06-27 00:22:00 | TERRA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 10.1 |
| b2c4c212-2b81-3471-bf9f-a3f50a71557c | -7.20843 | -43.0862 | 2025-06-27 00:22:00 | TERRA_M-M | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 64.7 |
| 841af629-15cb-3166-b937-69c1712f216a | -11.36921 | -48.72449 | 2025-06-27 00:22:00 | TERRA_M-M | GURUPI | TOCANTINS | Brasil | 1709500 | 17 | 33 | nan | nan | nan | Cerrado | 9.8 |
| 49e4a455-536a-3db0-a79a-bb1179f6e5dc | -13.58516 | -45.25769 | 2025-06-27 00:22:00 | TERRA_M-M | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 7.9 |
| ac929572-3f34-3e74-ac8a-97d7173f6fe3 | -13.0535 | -48.83367 | 2025-06-27 00:22:00 | TERRA_M-M | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 15.7 |
| 18b3518b-36e5-3002-bdc1-d850fd3e1740 | -7.21617 | -43.07549 | 2025-06-27 00:22:00 | TERRA_M-M | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 26.7 |
| 752e546f-da19-3988-a411-3cf229a45703 | -11.77591 | -45.21405 | 2025-06-27 00:22:00 | TERRA_M-M | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 31088b3f-a5e9-328b-a5dd-fc1cae7fc47d | -9.12291 | -49.43864 | 2025-06-27 00:22:00 | TERRA_M-M | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 27.7 |
| 91bafae1-25df-39a0-81a8-31518c197b39 | -13.0478 | -48.82773 | 2025-06-27 00:22:00 | TERRA_M-M | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 61.5 |
| de1a68c6-be03-34d9-bf4d-e315c13328ea | -9.07837 | -49.43418 | 2025-06-27 00:22:00 | TERRA_M-M | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 94.4 |
| 17d201a9-36d5-31ed-bfe0-fd54f71171fe | -11.5803 | -52.11813 | 2025-06-27 00:22:00 | TERRA_M-M | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 828.5 |
| 4c7e8e5e-dec5-3ce9-a94c-5345b6edcf63 | -12.71162 | -43.15523 | 2025-06-27 00:22:00 | TERRA_M-M | PARATINGA | BAHIA | Brasil | 2923704 | 29 | 33 | nan | nan | nan | Caatinga | 4.1 |
| 7655ecfc-dbaa-39b5-814a-c59264b5e0d8 | -11.84161 | -43.79955 | 2025-06-27 00:22:00 | TERRA_M-M | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 19.6 |
| d281c76a-8212-39d0-96da-e2cf0d500d35 | -11.58828 | -44.63808 | 2025-06-27 00:22:00 | TERRA_M-M | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 10.3 |
| f5a05ce4-ce38-395c-b711-6271d4511eba | -12.75418 | -44.41073 | 2025-06-27 00:22:00 | TERRA_M-M | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 29.0 |
| f89b54d3-544b-30ec-a5e0-a7cc249077c1 | -9.09257 | -47.96807 | 2025-06-27 00:22:00 | TERRA_M-M | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 10.8 |
| eed3f098-ad2f-3e51-a8ff-e6809a5e22b6 | -12.03127 | -47.7824 | 2025-06-27 00:22:00 | TERRA_M-M | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 48.6 |
| 84e30a7d-cd21-3606-b33b-7f3cfd61249b | -7.20711 | -43.07682 | 2025-06-27 00:22:00 | TERRA_M-M | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 106.3 |
| 7f9b05d4-a087-38bc-bc49-e3f1f7136cec | -8.6107 | -51.56921 | 2025-06-27 00:22:00 | TERRA_M-M | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 143.8 |
| ad6d3154-270d-35f3-9cf0-bbb0d61ffd30 | -9.87695 | -48.05948 | 2025-06-27 00:22:00 | TERRA_M-M | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 3337b9ef-5731-3f70-b1e6-b44b2582832f | -10.27832 | -47.61042 | 2025-06-27 00:22:00 | TERRA_M-M | LAGOA DO TOCANTINS | TOCANTINS | Brasil | 1711951 | 17 | 33 | nan | nan | nan | Cerrado | 12.6 |
| 2003fdb9-5af4-379e-9b7d-72bf04e74ea1 | -12.75544 | -44.42001 | 2025-06-27 00:22:00 | TERRA_M-M | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 17.6 |
| 5f7c0204-5742-3dc9-83c3-7ab359354472 | -10.63118 | -46.70849 | 2025-06-27 00:22:00 | TERRA_M-M | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 5.7 |
| b4676261-5344-3ffe-8cec-0a5ca3171176 | -12.43115 | -43.7258 | 2025-06-27 00:22:00 | TERRA_M-M | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 216.8 |
| 4d20116a-d39e-3c56-b225-2e5224131fc6 | -13.28664 | -44.60455 | 2025-06-27 00:22:00 | TERRA_M-M | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 8.2 |
| 2b0bb286-1b20-3e5b-8ffa-685b3e159004 | -8.61338 | -51.59209 | 2025-06-27 00:22:00 | TERRA_M-M | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 100.6 |
| 9533ce3d-3ddf-3575-9761-ca7e37520ada | -13.05139 | -48.81659 | 2025-06-27 00:22:00 | TERRA_M-M | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 38.0 |
| 4d899709-bbbc-3de1-8f7c-db4e2cc876d1 | -10.82445 | -53.74673 | 2025-06-27 00:22:00 | TERRA_M-M | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 59.3 |
| 4c0b319e-5723-36db-a3b8-3c8545934dff | -7.2188 | -43.09424 | 2025-06-27 00:22:00 | TERRA_M-M | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 24.7 |
| fa186cec-bf88-30bb-b91b-64f35012c53e | -11.58174 | -52.14115 | 2025-06-27 00:22:00 | TERRA_M-M | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 207.8 |
| 0f3e90f8-ec14-3fed-91a1-c28cde511d9e | -9.87527 | -48.04628 | 2025-06-27 00:22:00 | TERRA_M-M | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 8.5 |
| cca0fee0-307a-3d3d-bb58-6419c53c7126 | -9.1112 | -49.44019 | 2025-06-27 00:22:00 | TERRA_M-M | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 19.8 |
| 72d86010-6477-34d0-a275-8fac5f32168b | -9.06666 | -49.43564 | 2025-06-27 00:22:00 | TERRA_M-M | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 66.5 |
| 5cc9b19d-fa4f-3fe4-978f-954fcd5e0ff9 | -8.37252 | -51.07119 | 2025-06-27 00:22:00 | TERRA_M-M | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 42.3 |
| ee9ded8c-08b5-3566-bb1f-7c15656260b4 | -9.37338 | -47.62933 | 2025-06-27 00:22:00 | TERRA_M-M | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 15.9 |
| 1e1c46e3-c7af-33e0-97bd-8cd1a7bd3a37 | -11.99642 | -47.16637 | 2025-06-27 00:22:00 | TERRA_M-M | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 20.4 |
| ef8f29f0-6502-367a-ba81-a88f2f466be5 | -8.60471 | -51.57663 | 2025-06-27 00:22:00 | TERRA_M-M | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 31.7 |
| 26a8c140-d3fb-380b-a689-293774dc7bce | -14.43343 | -48.86695 | 2025-06-27 00:22:00 | TERRA_M-M | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 26.8 |
| 0d98fd2f-df38-3ff1-976c-82e72199f9b1 | -11.99483 | -47.15402 | 2025-06-27 00:22:00 | TERRA_M-M | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 5b628f4f-b37b-3d38-b82c-517e2dbc2b2f | -14.43549 | -48.8852 | 2025-06-27 00:22:00 | TERRA_M-M | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 18.9 |
| e34a6d29-1966-3d7c-bf68-1c45ee93ebce | -12.03777 | -48.75842 | 2025-06-27 00:22:00 | TERRA_M-M | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 10.3 |
| a06cc69d-fe8c-3d96-9b9f-57923799fb80 | -12.0067 | -47.16499 | 2025-06-27 00:22:00 | TERRA_M-M | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 31.5 |
| 609465b9-287a-349b-a794-f2834c98dbdb | -14.44772 | -48.884 | 2025-06-27 00:22:00 | TERRA_M-M | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 29.4 |
| adccade0-8e57-3ecd-a1be-6ef8577edec1 | -12.71037 | -43.14623 | 2025-06-27 00:22:00 | TERRA_M-M | PARATINGA | BAHIA | Brasil | 2923704 | 29 | 33 | nan | nan | nan | Caatinga | 23.1 |
| 50ee7c2e-d145-3254-828e-2f3160b45265 | -11.57701 | -52.08929 | 2025-06-27 00:22:00 | TERRA_M-M | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 56.3 |
| f764e1dd-66bd-330d-843b-cfd226ad8b4f | -9.76125 | -48.04069 | 2025-06-27 00:22:00 | TERRA_M-M | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 10.5 |
| c2abb50e-5196-3cc0-8cfc-102d56a25643 | -8.62453 | -51.56749 | 2025-06-27 00:22:00 | TERRA_M-M | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 293.1 |
| c798d991-ba2f-3075-8561-44f943c3c69f | -9.75066 | -48.04218 | 2025-06-27 00:22:00 | TERRA_M-M | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 16.0 |
| b4e90902-31c9-36cf-8901-8780a9ec5a83 | -12.02962 | -47.76898 | 2025-06-27 00:22:00 | TERRA_M-M | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 54.3 |
| 7c3b3c37-57df-3c64-8e8f-0803f3e056b0 | -7.56294 | -45.63862 | 2025-06-27 00:22:00 | TERRA_M-M | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 458cbb30-68ee-3298-9e1c-3c625f49fa6f | -9.06461 | -49.41952 | 2025-06-27 00:22:00 | TERRA_M-M | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 19.8 |
| a3ad9812-2791-36f3-a154-d6b240a685df | -8.48462 | -48.26806 | 2025-06-27 00:22:00 | TERRA_M-M | TUPIRATINS | TOCANTINS | Brasil | 1721307 | 17 | 33 | nan | nan | nan | Cerrado | 30.1 |
| d6d71825-5e39-3f10-a7ab-cfcef44d8e99 | -8.61856 | -51.575 | 2025-06-27 00:22:00 | TERRA_M-M | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 442.9 |
| 5e1d2064-a5dd-35c6-a4f8-0a38ce5050f7 | -7.55209 | -45.82901 | 2025-06-27 00:22:00 | TERRA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 2e7abc25-5d5b-36cc-a639-f2c6a1533f0b | -13.04582 | -48.81066 | 2025-06-27 00:22:00 | TERRA_M-M | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 30.5 |
| 6a193db0-bfbf-3cdc-92d6-acd3782700f6 | -11.35579 | -48.71027 | 2025-06-27 00:22:00 | TERRA_M-M | ALIANÇA DO TOCANTINS | TOCANTINS | Brasil | 1700350 | 17 | 33 | nan | nan | nan | Cerrado | 27.9 |
| da5476c5-0e38-3656-97db-3c952f60f42c | -8.62147 | -51.59825 | 2025-06-27 00:22:00 | TERRA_M-M | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 39.9 |
| cf340993-7e70-311a-b33a-93de9bc48ab2 | -10.64097 | -46.70726 | 2025-06-27 00:22:00 | TERRA_M-M | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 8.5 |
| fe85a6cc-cb61-341d-abc0-90ef01f95948 | -14.21276 | -45.50745 | 2025-06-27 00:22:00 | TERRA_M-M | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 8.0 |
| c89cb249-259f-38c1-b652-2297a6104fa9 | -9.07629 | -49.41803 | 2025-06-27 00:22:00 | TERRA_M-M | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 98.8 |
| 84f9590e-5b55-3e48-89b8-2a6e3d59c617 | -12.42991 | -43.71679 | 2025-06-27 00:22:00 | TERRA_M-M | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 49.0 |
| a84edfab-5071-3196-bf9b-7002ab7a5d7d | -12.06902 | -45.83129 | 2025-06-27 00:22:00 | TERRA_M-M | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 1ccfe9e2-1e4d-32de-90cc-d3822d29cdf6 | -7.53275 | -45.82229 | 2025-06-27 00:22:00 | TERRA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 5.6 |
| dacb6c66-62b6-3281-be85-557afa8c8c37 | -11.5786 | -52.1117 | 2025-06-27 00:22:00 | TERRA_M-M | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 955.4 |
| ecaac0be-665f-3e88-9729-b4a5f12535aa | -11.58954 | -44.6473 | 2025-06-27 00:22:00 | TERRA_M-M | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 21.0 |


[Clique aqui para ver as próximas entradas](README3.md)
