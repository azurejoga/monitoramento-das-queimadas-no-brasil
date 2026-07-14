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
| 878a0fb4-54e4-3ff2-91e2-dd0254616db7 | -18.7743 | -52.4061 | 2026-07-14 00:00:00 | GOES-19 | CASSILÂNDIA | MATO GROSSO DO SUL | Brasil | 5002902 | 50 | 33 | nan | nan | nan | Cerrado | 70.9 |
| 8d13c585-b501-3dd0-b137-91cb352ef37d | -8.4985 | -48.0813 | 2026-07-14 00:00:00 | GOES-19 | ITAPIRATINS | TOCANTINS | Brasil | 1710904 | 17 | 33 | nan | nan | nan | Cerrado | 77.3 |
| f1ef3765-cfc5-375c-af44-e107b63af6b2 | -8.5175 | -48.0577 | 2026-07-14 00:00:00 | GOES-19 | ITAPIRATINS | TOCANTINS | Brasil | 1710904 | 17 | 33 | nan | nan | nan | Cerrado | 108.5 |
| ee593fc0-7b8b-30f6-826c-651a8ff55bb4 | -18.7943 | -52.4027 | 2026-07-14 00:00:00 | GOES-19 | CASSILÂNDIA | MATO GROSSO DO SUL | Brasil | 5002902 | 50 | 33 | nan | nan | nan | Cerrado | 63.3 |
| 11dddc4a-1d76-36b5-9218-b151ed504d7b | -10.0731 | -50.1104 | 2026-07-14 00:00:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 78.9 |
| e75cfbb4-d806-3f80-8a7e-da44948170a1 | -10.0728 | -50.1318 | 2026-07-14 00:00:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 96.2 |
| 60ca4735-2c3e-3570-b651-c01bf10e8c72 | -8.5173 | -48.0796 | 2026-07-14 00:00:00 | GOES-19 | ITAPIRATINS | TOCANTINS | Brasil | 1710904 | 17 | 33 | nan | nan | nan | Cerrado | 96.3 |
| 79dd343b-d033-39ac-83db-97715df8af1f | -8.4987 | -48.0594 | 2026-07-14 00:00:00 | GOES-19 | ITAPIRATINS | TOCANTINS | Brasil | 1710904 | 17 | 33 | nan | nan | nan | Cerrado | 87.1 |
| 3fa449d5-9409-3c4f-b93d-0100a9c52922 | -10.191 | -50.108101 | 2026-07-14 00:03:00 | METOP-B | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 07f5ff3c-0e47-34aa-9ced-9238bd3598b4 | -8.5099 | -48.053398 | 2026-07-14 00:03:00 | METOP-B | ITAPIRATINS | TOCANTINS | Brasil | 1710904 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| f3eadfbe-af03-3885-bf4d-1594669f47a1 | -6.6708 | -47.5201 | 2026-07-14 00:03:00 | METOP-B | PALMEIRAS DO TOCANTINS | TOCANTINS | Brasil | 1713809 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 3392950a-33e3-3b15-ab33-3b7b7f748893 | -12.4471 | -49.4422 | 2026-07-14 00:03:00 | METOP-B | FIGUEIRÓPOLIS | TOCANTINS | Brasil | 1707652 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| e584ec13-c0c0-3c5f-a2a8-3c0d804f88f0 | -8.5115 | -48.060398 | 2026-07-14 00:03:00 | METOP-B | ITAPIRATINS | TOCANTINS | Brasil | 1710904 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 3ae517d9-baab-3f0c-a0de-75df6b4266c6 | -19.1385 | -43.514301 | 2026-07-14 00:03:00 | METOP-B | CONCEIÇÃO DO MATO DENTRO | MINAS GERAIS | Brasil | 3117504 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| e42c1e42-f9d6-3cf0-9512-4bb957709e1d | -4.3757 | -47.760399 | 2026-07-14 00:03:00 | METOP-B | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 082f21f6-6ad6-3682-975a-ad64f0e213f9 | -7.9062 | -48.254101 | 2026-07-14 00:03:00 | METOP-B | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| fae610b9-4f6d-3c2a-978f-d46e68317b35 | -7.7495 | -45.015099 | 2026-07-14 00:03:00 | METOP-B | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| bbab3c10-43c5-3402-a853-16a3cb2e55b6 | -10.0875 | -50.1035 | 2026-07-14 00:03:00 | METOP-B | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 06743931-b359-345e-aadb-925a9f8d9ad2 | -18.788401 | -52.382999 | 2026-07-14 00:03:00 | METOP-B | CASSILÂNDIA | MATO GROSSO DO SUL | Brasil | 5002902 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| d5898f93-f58f-3a75-801c-35688f1b67d7 | -6.483 | -42.204899 | 2026-07-14 00:03:00 | METOP-B | VÁRZEA GRANDE | PIAUÍ | Brasil | 2211407 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 9b52efda-0431-30b2-96a9-204f1ca62ec1 | -8.5017 | -48.062599 | 2026-07-14 00:03:00 | METOP-B | ITAPIRATINS | TOCANTINS | Brasil | 1710904 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| bad527ee-3559-3ab2-8bd6-8ffc331791d5 | -19.1402 | -43.521599 | 2026-07-14 00:03:00 | METOP-B | CONCEIÇÃO DO MATO DENTRO | MINAS GERAIS | Brasil | 3117504 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 7ba8bbbc-9b52-3381-a457-045b106e1e03 | -11.8921 | -43.8311 | 2026-07-14 00:03:00 | METOP-B | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| d2f30be8-a69a-3d78-9c9d-e8897330929a | -12.4447 | -49.576801 | 2026-07-14 00:03:00 | METOP-B | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| fb943613-2d68-3f8a-99a6-4880b3358995 | -4.3741 | -47.753601 | 2026-07-14 00:03:00 | METOP-B | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a6ea8e66-1bf8-32c7-8cac-7d078bcba5d3 | -20.6534 | -48.664001 | 2026-07-14 00:03:00 | METOP-B | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| e7a96ae3-2334-3593-b4b8-50d904f17430 | -9.6958 | -47.692799 | 2026-07-14 00:03:00 | METOP-B | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| a1e9e001-d46a-3094-a6e1-39f7458c8b27 | -4.3772 | -47.7673 | 2026-07-14 00:03:00 | METOP-B | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 806ef55c-3e18-31a4-adb4-f5f1e758a52f | -3.9234 | -47.811199 | 2026-07-14 00:03:00 | METOP-B | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b948aff3-bc2a-3711-bf50-a7b3c2fd6b42 | -8.5032 | -48.069599 | 2026-07-14 00:03:00 | METOP-B | ITAPIRATINS | TOCANTINS | Brasil | 1710904 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 2db3fb77-edfa-31c8-8e16-da3b4186e816 | -4.4945 | -48.286499 | 2026-07-14 00:03:00 | METOP-B | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 74930c29-7437-372d-8cf3-e11424ebefc5 | -10.068 | -50.1077 | 2026-07-14 00:03:00 | METOP-B | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 78fa1562-6feb-3df4-b752-196f3d973075 | -5.8232 | -43.472401 | 2026-07-14 00:03:00 | METOP-B | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 8df2e2a4-4f05-3996-8668-d303bb24ead5 | -4.0183 | -48.048199 | 2026-07-14 00:03:00 | METOP-B | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d8e3783b-aa7a-3746-a073-e0ddfb122176 | -2.9628 | -48.986698 | 2026-07-14 00:03:00 | METOP-B | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f07efc5b-9ac6-39e6-9f74-3258137064b6 | -10.7512 | -42.105 | 2026-07-14 00:03:00 | METOP-B | ITAGUAÇU DA BAHIA | BAHIA | Brasil | 2915353 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| 2b4d2997-a6eb-3ca2-b59c-f8b8aab688c5 | -2.7944 | -49.519199 | 2026-07-14 00:03:00 | METOP-B | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| cc0dad9d-cdd3-338a-87ff-c6847d80b5c3 | -5.9419 | -46.351501 | 2026-07-14 00:03:00 | METOP-B | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 767f7e37-1d11-351b-80f8-8ff0da2c5d78 | -8.9452 | -47.604198 | 2026-07-14 00:03:00 | METOP-B | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 1310e0f9-2149-30df-bb8f-fc8d63b17974 | -10.0716 | -50.124802 | 2026-07-14 00:03:00 | METOP-B | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| f4959ee2-a187-32c2-8246-58609ba3a3f2 | -7.753 | -45.0303 | 2026-07-14 00:03:00 | METOP-B | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| d8308a91-12aa-344a-8372-33654e30a54a | -7.9046 | -48.247002 | 2026-07-14 00:03:00 | METOP-B | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 2a8a0e97-edd1-38b4-a1d9-d5fbfdde2e64 | -7.0143 | -45.405602 | 2026-07-14 00:03:00 | METOP-B | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 8ab98ba1-d11b-303d-9c4e-e588cc002e9d | -5.3094 | -47.2416 | 2026-07-14 00:03:00 | METOP-B | JOÃO LISBOA | MARANHÃO | Brasil | 2105500 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 00894a1d-3093-363d-89b0-d311d516fe2e | -5.3063 | -47.227798 | 2026-07-14 00:03:00 | METOP-B | JOÃO LISBOA | MARANHÃO | Brasil | 2105500 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 3a2fa65e-5ab7-30c7-8188-03ac5dff3d65 | -5.3078 | -47.234699 | 2026-07-14 00:03:00 | METOP-B | JOÃO LISBOA | MARANHÃO | Brasil | 2105500 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 8cfad648-286f-3273-b7c7-9f26616373c7 | -5.909 | -43.618999 | 2026-07-14 00:03:00 | METOP-B | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| aa1488fd-1421-33fd-93e8-b478814befde | -4.0198 | -48.055 | 2026-07-14 00:03:00 | METOP-B | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 45e0c268-e16d-3f14-bd30-78e5f325c69b | -9.6973 | -47.699799 | 2026-07-14 00:03:00 | METOP-B | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 5910c923-182e-3d2b-910d-345c1c76e214 | -12.4545 | -49.574699 | 2026-07-14 00:03:00 | METOP-B | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 0e4a4778-cf6d-3cd0-af7b-a76339686ec1 | -10.0796 | -50.114101 | 2026-07-14 00:03:00 | METOP-B | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 9860f33d-4d87-3d91-84ab-3302dc31b01d | -11.8903 | -43.823299 | 2026-07-14 00:03:00 | METOP-B | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| a5620dc7-fb10-38c8-83cc-7cafb731dbd9 | -5.833 | -43.4702 | 2026-07-14 00:03:00 | METOP-B | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| f18f9980-c201-345c-844d-5c71dae8b44d | -10.0778 | -50.105598 | 2026-07-14 00:03:00 | METOP-B | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 29f05e80-f215-3981-bf57-262334394604 | -5.9069 | -43.609798 | 2026-07-14 00:03:00 | METOP-B | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 00c63299-3d7e-3133-86dc-e4ca9e8f0d85 | -6.6692 | -47.513302 | 2026-07-14 00:03:00 | METOP-B | PALMEIRAS DO TOCANTINS | TOCANTINS | Brasil | 1713809 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 1f04c30d-a9d2-3bac-8d48-1de1c77c73fb | -18.775801 | -52.369099 | 2026-07-14 00:03:00 | METOP-B | APORÉ | GOIÁS | Brasil | 5201504 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 74abd7e5-1670-306f-9579-231fbfca89b5 | -12.4596 | -46.509701 | 2026-07-14 00:03:00 | METOP-B | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 5c8296e7-c712-3e81-8ccb-94eba73cd4da | -18.1752 | -46.902199 | 2026-07-14 00:03:00 | METOP-B | LAGAMAR | MINAS GERAIS | Brasil | 3137106 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| dcf5e1cd-57ed-3f99-bad8-f81eb85b51b8 | -11.5762 | -48.391201 | 2026-07-14 00:03:00 | METOP-B | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 0bd2bca1-4c64-3970-bbda-a2f9cb6bf835 | -6.4882 | -42.226898 | 2026-07-14 00:03:00 | METOP-B | VÁRZEA GRANDE | PIAUÍ | Brasil | 2211407 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| eb395ec5-2302-3b18-8407-750e48bf900f | -10.0954 | -50.0928 | 2026-07-14 00:03:00 | METOP-B | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 43cc4139-4b80-3f5c-8747-193c2d3b69d6 | -4.0085 | -48.0504 | 2026-07-14 00:03:00 | METOP-B | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1df0827b-ab83-3cd7-8ba1-2d2aae369621 | -10.0838 | -50.086399 | 2026-07-14 00:03:00 | METOP-B | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| eff254c0-f5d3-3149-8ff3-a3df2afefa0a | -8.7343 | -48.322701 | 2026-07-14 00:03:00 | METOP-B | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| a9c815d4-fc06-37cb-885d-096b5611caaf | -7.016 | -45.412998 | 2026-07-14 00:03:00 | METOP-B | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 3ec4acb5-93c3-3e4d-8f99-a160ab5c737c | -5.2528 | -42.666199 | 2026-07-14 00:03:00 | METOP-B | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| e13f8aff-de93-39d8-86e8-3400a57d4599 | -10.0618 | -50.126999 | 2026-07-14 00:03:00 | METOP-B | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 3c5d0e5e-4539-39fc-9d95-a87c2769eb98 | -5.9403 | -46.344398 | 2026-07-14 00:03:00 | METOP-B | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| ab117d14-908d-3400-9e87-f6b7ddb0b1b4 | -8.903 | -50.174 | 2026-07-14 00:03:00 | METOP-B | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d90eda1a-5616-3709-b52d-071af56fdf0b | -6.4758 | -42.2183 | 2026-07-14 00:03:00 | METOP-B | VÁRZEA GRANDE | PIAUÍ | Brasil | 2211407 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| ddd34c3d-5133-3ce2-8286-ca763f482e3b | -2.7928 | -49.512199 | 2026-07-14 00:03:00 | METOP-B | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| bd3c49c3-3d03-30a2-a70a-406c526757df | -5.2439 | -44.927299 | 2026-07-14 00:03:00 | METOP-B | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 828c495f-124d-39b5-87ca-a441d0afb4f1 | -6.8935 | -47.960999 | 2026-07-14 00:03:00 | METOP-B | WANDERLÂNDIA | TOCANTINS | Brasil | 1722081 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| ebcb0bb1-564f-3438-87ec-17d01d2a72c2 | -5.242 | -44.9193 | 2026-07-14 00:03:00 | METOP-B | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 0d21d545-be94-3178-9269-9cf56d0d931a | -18.7815 | -52.400799 | 2026-07-14 00:03:00 | METOP-B | CASSILÂNDIA | MATO GROSSO DO SUL | Brasil | 5002902 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| 84fb9b5c-8ab9-3368-abec-ffb224720aaa | -8.5001 | -48.055599 | 2026-07-14 00:03:00 | METOP-B | ITAPIRATINS | TOCANTINS | Brasil | 1710904 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| f2176c35-7022-31cf-8a51-4e9e8e2392ac | -18.1768 | -46.91 | 2026-07-14 00:03:00 | METOP-B | LAGAMAR | MINAS GERAIS | Brasil | 3137106 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 9b59dc80-761f-3890-a958-79cf96a1885a | -20.6553 | -48.674 | 2026-07-14 00:03:00 | METOP-B | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 7775ed06-ad6a-32a6-b521-ff214b30d9bc | -18.778601 | -52.384899 | 2026-07-14 00:03:00 | METOP-B | APORÉ | GOIÁS | Brasil | 5201504 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| e3a565ec-3de6-3205-b9e1-b383be697797 | -10.0893 | -50.112 | 2026-07-14 00:03:00 | METOP-B | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 4d15f857-229e-3b76-a82b-3fd6f937115d | -10.1891 | -50.099499 | 2026-07-14 00:03:00 | METOP-B | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 63f1f85f-45cd-31c8-bfbf-5ac5b9e42b96 | -18.178499 | -46.917801 | 2026-07-14 00:03:00 | METOP-B | LAGAMAR | MINAS GERAIS | Brasil | 3137106 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| c1345322-af6b-3031-a18d-aceeff62ecee | -5.8254 | -43.4818 | 2026-07-14 00:03:00 | METOP-B | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| a303d068-bb5e-38bf-b60c-16cf9b7a81d9 | -10.0698 | -50.116199 | 2026-07-14 00:03:00 | METOP-B | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 3b86c5ec-fb24-3c76-965e-1f7fc51c04db | -6.4856 | -42.2159 | 2026-07-14 00:03:00 | METOP-B | VÁRZEA GRANDE | PIAUÍ | Brasil | 2211407 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 98333b8a-8f7a-3b59-9236-11e62853ee65 | -10.761 | -42.1026 | 2026-07-14 00:03:00 | METOP-B | ITAGUAÇU DA BAHIA | BAHIA | Brasil | 2915353 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| 73028c89-2ec8-3d36-bd36-c0e10d997101 | -10.7489 | -42.095299 | 2026-07-14 00:03:00 | METOP-B | ITAGUAÇU DA BAHIA | BAHIA | Brasil | 2915353 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| 320d5bc5-ccfe-313f-bb54-51d0fde474d6 | -7.7513 | -45.022701 | 2026-07-14 00:03:00 | METOP-B | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 819c1a8d-650d-3e95-a0ce-6c86319b5405 | -10.0936 | -50.084301 | 2026-07-14 00:03:00 | METOP-B | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| b1836fd3-4362-37e5-84ae-f732afd22ec7 | -4.01 | -48.057201 | 2026-07-14 00:03:00 | METOP-B | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 86f880f4-5ed1-3937-be3b-476b7ebd9f75 | -10.092 | -50.1085 | 2026-07-14 00:10:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 69.7 |
| 5e52438f-67f1-371f-a859-b93e0359f471 | -8.5175 | -48.0577 | 2026-07-14 00:10:00 | GOES-19 | ITAPIRATINS | TOCANTINS | Brasil | 1710904 | 17 | 33 | nan | nan | nan | Cerrado | 66.0 |
| f1bbb1a1-eba4-322a-a78a-a3682b69f660 | -10.0728 | -50.1318 | 2026-07-14 00:10:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 121.7 |
| 5fb81090-7be1-3e97-b31d-6eef1d803f5d | -18.7943 | -52.4027 | 2026-07-14 00:10:00 | GOES-19 | CASSILÂNDIA | MATO GROSSO DO SUL | Brasil | 5002902 | 50 | 33 | nan | nan | nan | Cerrado | 56.5 |
| 74a9bf5f-30c6-3bcb-89c9-4a133c7519ce | -18.7743 | -52.4061 | 2026-07-14 00:10:00 | GOES-19 | CASSILÂNDIA | MATO GROSSO DO SUL | Brasil | 5002902 | 50 | 33 | nan | nan | nan | Cerrado | 63.5 |
| 7b6b8246-9d34-36a9-b0b0-37e705a2a4c4 | -8.4987 | -48.0594 | 2026-07-14 00:10:00 | GOES-19 | ITAPIRATINS | TOCANTINS | Brasil | 1710904 | 17 | 33 | nan | nan | nan | Cerrado | 105.3 |
| 9cc3addb-1073-3a76-8f32-521ecb11599d | -8.4985 | -48.0813 | 2026-07-14 00:10:00 | GOES-19 | ITAPIRATINS | TOCANTINS | Brasil | 1710904 | 17 | 33 | nan | nan | nan | Cerrado | 95.4 |
| 927a2b32-7947-37bb-bacd-7b24385a61d2 | -10.0731 | -50.1104 | 2026-07-14 00:10:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 105.7 |
| 52373558-e767-3012-9c43-cc95a251549c | -10.0539 | -50.1337 | 2026-07-14 00:20:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 46.8 |


[Clique aqui para ver as próximas entradas](README2.md)
