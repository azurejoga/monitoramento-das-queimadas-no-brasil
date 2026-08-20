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
| d4016c68-529b-3ed3-b2a5-145b84457be8 | -12.0046 | -53.441101 | 2026-08-20 00:38:00 | METOP-B | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| eacda9b6-d0eb-3f83-8f72-b35ec0886b6c | -14.1984 | -52.888699 | 2026-08-20 00:38:00 | METOP-B | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| de199a8d-2126-3994-9755-778f4234a2af | -14.4393 | -45.5914 | 2026-08-20 00:38:00 | METOP-B | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 7341a7dc-8d9a-317f-bd3c-9d96b93cb0eb | -11.1945 | -53.998699 | 2026-08-20 00:38:00 | METOP-B | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 0a805ba4-6971-3361-b509-71411d69e530 | -11.2162 | -55.041801 | 2026-08-20 00:38:00 | METOP-B | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 7a600d4e-d2a1-399e-8103-3ec49b6e24c9 | -14.1488 | -52.941601 | 2026-08-20 00:38:00 | METOP-B | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 54e1d82f-5c55-3c50-870e-66bc0968d1db | -11.2194 | -55.055901 | 2026-08-20 00:38:00 | METOP-B | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 6ccd5e9d-4669-3f3a-a8d8-3fa81e1667b2 | -4.3892 | -55.4729 | 2026-08-20 00:38:00 | METOP-B | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 59a0389a-6fb2-316c-a9b9-e19456ec37ab | -6.6973 | -59.093899 | 2026-08-20 00:38:00 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 2307a29f-d77d-30c0-af4e-a4a3ff2f2197 | -7.5463 | -55.5798 | 2026-08-20 00:38:00 | METOP-B | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 06bfa701-106f-36ce-b7ec-aa1a08341b1b | -6.0938 | -57.9058 | 2026-08-20 00:38:00 | METOP-B | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9fd10de0-6428-3557-9f25-b2e17b55c26d | -9.2175 | -59.7808 | 2026-08-20 00:38:00 | METOP-B | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| d140e559-cdfa-38de-a6b4-24d3df12aad0 | -8.5807 | -54.739399 | 2026-08-20 00:38:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 629ee42d-0c5c-3a79-aebc-100329dde966 | -9.3928 | -60.5527 | 2026-08-20 00:38:00 | METOP-B | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 084c28b9-37f7-3992-acf9-2e7cdc98a33f | -14.0143 | -53.657101 | 2026-08-20 00:38:00 | METOP-B | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| bc84c7e0-ae83-3dba-a357-5c7f513517f8 | -16.068399 | -54.960701 | 2026-08-20 00:38:00 | METOP-B | JACIARA | MATO GROSSO | Brasil | 5104807 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 68b541e8-a76c-396d-86cb-73980eb5a3ee | -13.4316 | -57.058201 | 2026-08-20 00:38:00 | METOP-B | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 4e80312d-0007-3df5-882c-4b9225cd1932 | -9.2156 | -59.772099 | 2026-08-20 00:38:00 | METOP-B | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 26c54693-b353-3a0f-84b9-93ee77199539 | -12.4759 | -54.734501 | 2026-08-20 00:38:00 | METOP-B | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| f3482754-d6be-3194-9141-fb37e2a69c88 | -9.3907 | -60.543098 | 2026-08-20 00:38:00 | METOP-B | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| e4dbeb8c-f430-396b-bfd7-a930f3c764d1 | -7.3404 | -55.671001 | 2026-08-20 00:38:00 | METOP-B | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2a4a0185-70bb-3e4b-88fc-b81ee4c49ab3 | -7.5333 | -55.567902 | 2026-08-20 00:38:00 | METOP-B | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 677e3992-2db0-3a5f-a795-63b1d6976d8c | -6.9168 | -59.344101 | 2026-08-20 00:38:00 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 00e03bf4-6fc0-3e84-b876-7c67798de10e | -6.4293 | -52.7556 | 2026-08-20 00:38:00 | METOP-B | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0e87a091-bb0a-30f7-8fbf-8fe2331a905f | -6.9471 | -52.809799 | 2026-08-20 00:38:00 | METOP-B | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3c9cce3b-4f26-3f84-81a0-4dcc14ea9fa9 | -6.8539 | -59.012001 | 2026-08-20 00:38:00 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 7bca6152-5c64-3d3c-b9c0-fafa98f2daf0 | -6.2471 | -55.396 | 2026-08-20 00:38:00 | METOP-B | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c104db97-e29a-317b-b0b4-8e124d15b52b | -8.5449 | -54.763 | 2026-08-20 00:38:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 365874ca-8927-3c7d-8617-812da202e995 | -10.5166 | -50.777 | 2026-08-20 00:38:00 | METOP-B | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 83e99838-2a0a-320e-8394-938545966350 | -9.4194 | -60.437401 | 2026-08-20 00:38:00 | METOP-B | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| dab38eae-effa-3cad-8105-622d0549059d | -8.6635 | -54.650799 | 2026-08-20 00:38:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d3be7937-2447-3e82-b47e-a85ae0b7b422 | -6.8831 | -56.425201 | 2026-08-20 00:38:00 | METOP-B | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| df1ad65b-f519-33d6-a959-801ac68c1598 | -7.3284 | -45.7845 | 2026-08-20 00:38:00 | METOP-B | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 697644ee-bdd4-3b08-90df-ae54ff36338e | -7.3638 | -55.502399 | 2026-08-20 00:38:00 | METOP-B | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4c04d2fd-5229-3fd4-b45a-2eee02191c16 | -8.5703 | -54.6492 | 2026-08-20 00:38:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f6d5d464-4885-39f9-bf6e-f7beb401fd08 | -14.4297 | -45.5942 | 2026-08-20 00:38:00 | METOP-B | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 31efe7b0-1be1-3458-910e-a483e526ae17 | -6.4177 | -54.926201 | 2026-08-20 00:38:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| da9360d0-6162-3a69-9e27-7710a854ba8e | -14.524 | -53.315601 | 2026-08-20 00:38:00 | METOP-B | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| c4d9ccd9-edd2-3eff-88b9-9f3231398e5c | -7.3255 | -45.813099 | 2026-08-20 00:38:00 | METOP-B | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| ba2a831d-fb9d-36c6-8687-c4fc767af26b | -5.4237 | -49.224098 | 2026-08-20 00:38:00 | METOP-B | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9ff7a49c-f6ab-37c6-806f-13ae3614cc57 | -6.7918 | -59.569302 | 2026-08-20 00:38:00 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| b2b3f009-1bda-3d8d-9ee7-d75106540bbc | -8.675 | -54.655998 | 2026-08-20 00:38:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| cdb7489e-d368-35da-901e-bd95cf5f84e3 | -15.8679 | -55.548698 | 2026-08-20 00:38:00 | METOP-B | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 6f3edc24-5584-3eec-bef6-78ff753c03c3 | -9.2217 | -59.752602 | 2026-08-20 00:38:00 | METOP-B | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 53a03aba-8b89-383c-a1d6-7c7e9628e4fd | -9.1455 | -51.124802 | 2026-08-20 00:38:00 | METOP-B | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 217665bc-adfa-3d5a-acdd-e63a981991bc | -9.5494 | -56.790901 | 2026-08-20 00:38:00 | METOP-B | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 9f2d1832-1904-36fd-ba1f-55d6736143a0 | -8.5905 | -54.737099 | 2026-08-20 00:38:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| db0c101c-84b8-3dfa-9b82-5b7956703c0c | -9.2565 | -56.907902 | 2026-08-20 00:38:00 | METOP-B | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 77797848-bd18-3392-a4a3-74cf195edcb8 | -7.9581 | -44.653999 | 2026-08-20 00:38:00 | METOP-B | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| dc834c8a-43a4-3678-a3fa-ca679c043aa5 | -6.8679 | -51.862099 | 2026-08-20 00:38:00 | METOP-B | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9108f9f7-6887-3575-80bd-0b0889f75c3e | -9.1016 | -60.3391 | 2026-08-20 00:38:00 | METOP-B | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 4f14c0d1-db3e-3cd1-b1b1-b6a94e2d1bb5 | -14.6707 | -55.6213 | 2026-08-20 00:38:00 | METOP-B | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 6cc8ad09-17fa-3fb8-9636-fd9ffe049600 | -10.7918 | -50.2952 | 2026-08-20 00:38:00 | METOP-B | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 53e569b6-318f-3550-aebd-96bcab536a15 | -6.5971 | -58.965801 | 2026-08-20 00:38:00 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 8e661436-f272-3d91-8ec0-3f8f1322632f | -5.7899 | -55.695599 | 2026-08-20 00:38:00 | METOP-B | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4c6e740c-a562-3e8e-a294-3e315a4509e9 | -6.4196 | -52.7579 | 2026-08-20 00:38:00 | METOP-B | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c9075553-73d8-3082-92bf-269adf76171e | -7.5447 | -55.572701 | 2026-08-20 00:38:00 | METOP-B | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d709f156-0302-3b8c-9acc-262316eca013 | -6.5857 | -58.9604 | 2026-08-20 00:38:00 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 2730dba0-d22a-3005-a5a0-c50d256fedda | -9.1228 | -61.5956 | 2026-08-20 00:38:00 | METOP-B | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 6f06b23c-0407-3099-8860-82c755154e33 | -15.5387 | -50.2644 | 2026-08-20 00:38:00 | METOP-B | FAINA | GOIÁS | Brasil | 5207535 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| af10c477-bbcb-311a-ac90-a2da99323093 | -21.712099 | -47.124901 | 2026-08-20 00:38:00 | METOP-B | CASA BRANCA | SÃO PAULO | Brasil | 3510807 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 01dfab6e-4349-3174-a005-eb32eefdbf30 | -8.5351 | -54.765301 | 2026-08-20 00:38:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c7009d23-284a-3273-a264-04d7a4797af6 | -8.5645 | -54.758499 | 2026-08-20 00:38:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| cd91e3c6-fb4a-365d-87f2-bf141aafb0cc | -7.3785 | -55.5215 | 2026-08-20 00:38:00 | METOP-B | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0d767e5d-3e14-320a-80e3-81e743881c63 | -11.1899 | -54.023201 | 2026-08-20 00:38:00 | METOP-B | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| c2d297ca-5601-3c4d-b285-ae5393a2a3fc | -4.9506 | -56.263 | 2026-08-20 00:38:00 | METOP-B | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 22269195-dcb2-354d-8839-457dc30a0779 | -9.4005 | -60.541 | 2026-08-20 00:38:00 | METOP-B | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| cb92f5be-268e-3787-b653-97a0c971a6f7 | -9.2254 | -59.769901 | 2026-08-20 00:38:00 | METOP-B | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 23eff49f-d673-3394-a9ee-8d630698e01f | -6.3147 | -55.9184 | 2026-08-20 00:38:00 | METOP-B | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 864b079c-5759-3dd5-bb77-5b159e6121d0 | -9.4154 | -60.418598 | 2026-08-20 00:38:00 | METOP-B | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 735a7ac2-8811-3197-95f8-dcf5eef14ebf | -9.204 | -59.765598 | 2026-08-20 00:38:00 | METOP-B | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| cfe787dc-0b04-3c6d-86e3-8a9fa73ca727 | -8.4997 | -54.880501 | 2026-08-20 00:38:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b79ab2c4-9a39-30f6-8839-d5554233b918 | -7.7954 | -61.1684 | 2026-08-20 00:38:00 | METOP-B | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 6aca04e0-51db-34a7-b27e-8433b3b81f14 | -8.5045 | -54.856602 | 2026-08-20 00:38:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 10d17376-b9de-37f6-ae31-82128b8e45eb | -11.1928 | -53.991199 | 2026-08-20 00:38:00 | METOP-B | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 88d78596-8c8b-32cd-a80d-3bbe89196375 | -9.2119 | -59.754799 | 2026-08-20 00:38:00 | METOP-B | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 27f1fd3e-a437-3c95-86d6-335b932dd70c | -13.5707 | -51.6674 | 2026-08-20 00:38:00 | METOP-B | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| c1e12975-50a0-359a-9e07-3ebf61639d5d | -6.5873 | -58.967899 | 2026-08-20 00:38:00 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| de1309de-9073-3fef-8597-79fc11ca7443 | -5.4963 | -60.121399 | 2026-08-20 00:38:00 | METOP-B | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| b98b1da4-de1c-3fbd-96a1-9ac0fecb294a | -18.5509 | -48.291 | 2026-08-20 00:38:00 | METOP-B | ARAGUARI | MINAS GERAIS | Brasil | 3103504 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| ac43629f-19de-38c2-868b-43ce76764d92 | -8.4981 | -54.873299 | 2026-08-20 00:38:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ab195e6b-7a25-3dce-9009-391cdde7b6ca | -12.7944 | -48.415798 | 2026-08-20 00:38:00 | METOP-B | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| a56762ca-f022-3c83-a64f-9a8d5965ce3f | -8.6716 | -54.6413 | 2026-08-20 00:38:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 39f8163f-50f6-37c0-815e-75eb52c29e0c | -10.2465 | -54.360699 | 2026-08-20 00:38:00 | METOP-B | MATUPÁ | MATO GROSSO | Brasil | 5105606 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 6b7d87d3-e865-3f69-aec6-cd991a5497ec | -16.5044 | -55.167301 | 2026-08-20 00:38:00 | METOP-B | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 4e1cff98-7701-3376-9c6e-16373993e2a5 | -8.1555 | -54.997799 | 2026-08-20 00:38:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e269634a-6e24-3f8b-8ab1-0609b378a390 | -11.4222 | -54.316601 | 2026-08-20 00:38:00 | METOP-B | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 6b5bfd59-b746-3f6b-88d8-b36870324d1f | -6.8964 | -55.7127 | 2026-08-20 00:38:00 | METOP-B | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 156d5ceb-af27-3b69-a832-27d354efe5f7 | -5.414 | -49.226398 | 2026-08-20 00:38:00 | METOP-B | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0c8458d4-a94b-3c42-9e75-50141d0b4f90 | -9.0544 | -57.063099 | 2026-08-20 00:38:00 | METOP-B | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 252c1710-37f8-344b-9600-f414ea0e024c | -7.8263 | -61.599701 | 2026-08-20 00:38:00 | METOP-B | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| d69609a2-6430-39e5-8b3a-6181bba507dc | -8.5258 | -54.859299 | 2026-08-20 00:38:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9cb993ca-a6c7-33c2-b255-213787b08ac0 | -10.7821 | -50.2976 | 2026-08-20 00:38:00 | METOP-B | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 12e29a4c-e4d8-333d-850b-9f0e7cda5d56 | -14.3205 | -53.237999 | 2026-08-20 00:38:00 | METOP-B | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 1fa0062d-a394-39f5-ac0c-3dc885385068 | -3.0979 | -61.207199 | 2026-08-20 00:38:00 | METOP-B | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| a17e7b34-e2de-3d56-8e1c-02a60d06f336 | -8.6682 | -54.626598 | 2026-08-20 00:38:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2c3de67a-28e4-302d-9d1f-9f8383e72b5a | -14.0207 | -53.640099 | 2026-08-20 00:38:00 | METOP-B | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 30b9f945-0a6a-389b-a4bd-b5567cd2af77 | -11.6821 | -54.5522 | 2026-08-20 00:38:00 | METOP-B | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 58191f1b-d707-3589-99ed-2f54d18f34e8 | -14.1948 | -52.873199 | 2026-08-20 00:38:00 | METOP-B | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| f3f6629f-c490-38e3-8879-3cdc0b47d837 | -8.0972 | -51.656502 | 2026-08-20 00:38:00 | METOP-B | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | nan |


[Clique aqui para ver as próximas entradas](README6.md)
