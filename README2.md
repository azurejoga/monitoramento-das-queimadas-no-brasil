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
| 353cb090-309a-3a53-baf1-b264cdb7694b | -5.9571 | -38.259899 | 2024-12-19 00:03:00 | METOP-B | ERERÊ | CEARÁ | Brasil | 2304277 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| 80a15c75-630b-3d25-969c-256e9a78a440 | -2.6455 | -45.748199 | 2024-12-19 00:03:00 | METOP-B | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 73509d36-3b1d-301c-b2ed-f1fdd5e1ed49 | -4.8651 | -41.401402 | 2024-12-19 00:03:00 | METOP-B | MILTON BRANDÃO | PIAUÍ | Brasil | 2206357 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| f64185e1-9bb5-3557-a1f5-096847997b0c | -6.7248 | -35.085499 | 2024-12-19 00:03:00 | METOP-B | MARCAÇÃO | PARAÍBA | Brasil | 2509057 | 25 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 1e05c15c-c55b-3c2c-9231-45ed173ef74f | -10.7381 | -37.0891 | 2024-12-19 00:03:00 | METOP-B | MARUIM | SERGIPE | Brasil | 2804003 | 28 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 10015bb4-ef35-3ca4-9ce4-69b97b261208 | -4.8865 | -41.4048 | 2024-12-19 00:03:00 | METOP-B | JUAZEIRO DO PIAUÍ | PIAUÍ | Brasil | 2205516 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 8d42564c-6840-3338-8ad0-3a8e72b5080a | -6.1354 | -43.953602 | 2024-12-19 00:03:00 | METOP-B | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 6b8838c3-e467-3026-940c-cbd7abf97c3e | -4.4762 | -45.4184 | 2024-12-19 00:03:00 | METOP-B | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 553ca70d-f815-3f25-97b0-04dc6496f849 | -6.9733 | -43.557598 | 2024-12-19 00:03:00 | METOP-B | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| fc51f468-eead-3a07-a732-733d64a5b642 | -6.4939 | -39.5788 | 2024-12-19 00:03:00 | METOP-B | JUCÁS | CEARÁ | Brasil | 2307403 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| 953fc76e-a3eb-392f-bf88-c072311237df | -4.1149 | -43.218399 | 2024-12-19 00:03:00 | METOP-B | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 2e357a38-b5de-346d-8cb3-38699b624ba3 | -4.8676 | -41.367599 | 2024-12-19 00:03:00 | METOP-B | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| dc94ace6-5874-3ae7-9521-49faabab2799 | -6.9868 | -43.5257 | 2024-12-19 00:03:00 | METOP-B | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 57d60025-19e8-3052-9a86-aa29ed67de8f | -4.9075 | -41.316799 | 2024-12-19 00:03:00 | METOP-B | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 81f60d2e-7139-3e4a-9f06-59235bbc6603 | -5.2139 | -43.293701 | 2024-12-19 00:03:00 | METOP-B | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 8c53ea5b-d79c-3579-9115-60191f4fae30 | -2.9797 | -40.279301 | 2024-12-19 00:03:00 | METOP-B | BELA CRUZ | CEARÁ | Brasil | 2302305 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| f661132e-c7e1-335e-b886-44861d74b8ea | -4.8499 | -41.380001 | 2024-12-19 00:03:00 | METOP-B | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| a2fc3d82-c72c-3e9f-ade3-c0c9cf67f7c5 | -4.9696 | -43.717201 | 2024-12-19 00:03:00 | METOP-B | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| f788f0b0-d428-3ff2-beb8-94e4adcab549 | -6.9853 | -43.518799 | 2024-12-19 00:03:00 | METOP-B | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 91d26396-cbe9-3f80-834e-996657d874a4 | -8.9899 | -36.140202 | 2024-12-19 00:03:00 | METOP-B | CANHOTINHO | PERNAMBUCO | Brasil | 2603702 | 26 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 6bff4705-9265-33c2-8fcd-22455c3b14ae | -3.8429 | -40.451099 | 2024-12-19 00:03:00 | METOP-B | CARIRÉ | CEARÁ | Brasil | 2303105 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| b0c9f3c1-eb15-3656-94ae-c9f18effa32b | -6.1323 | -43.939899 | 2024-12-19 00:03:00 | METOP-B | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| cf86a0b9-7568-3cdd-846a-5f28650b1a70 | -12.7154 | -40.201401 | 2024-12-19 00:03:00 | METOP-B | ITABERABA | BAHIA | Brasil | 2914703 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| 183dbe5e-9a2f-3426-834c-4def4eebae99 | -5.116 | -44.3675 | 2024-12-19 00:03:00 | METOP-B | PRESIDENTE DUTRA | MARANHÃO | Brasil | 2109106 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| ad552127-4c86-3490-af3b-a6e95ac5d462 | -4.9665 | -43.7034 | 2024-12-19 00:03:00 | METOP-B | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| b7c11955-4f01-37e8-a9d4-fbe53a9f6e3a | -4.8012 | -44.020802 | 2024-12-19 00:03:00 | METOP-B | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| c0c4f7d3-709e-32c6-8bf7-6eb57e509a3e | -5.2124 | -43.2868 | 2024-12-19 00:03:00 | METOP-B | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| cdc8fd05-20f8-3918-8769-46a6ff65a65a | -4.7725 | -44.580502 | 2024-12-19 00:03:00 | METOP-B | POÇÃO DE PEDRAS | MARANHÃO | Brasil | 2108900 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 840b99b3-32bb-396b-861e-ffaa261b8c3d | -4.8615 | -41.385601 | 2024-12-19 00:03:00 | METOP-B | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 1513ee07-6281-3600-8a1f-7362a3ed4fe8 | -10.2571 | -36.345501 | 2024-12-19 00:03:00 | METOP-B | FELIZ DESERTO | ALAGOAS | Brasil | 2702702 | 27 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 5fa4c871-2c98-30e8-8875-cd89bd0e2cbb | -7.1105 | -35.066898 | 2024-12-19 00:03:00 | METOP-B | CRUZ DO ESPÍRITO SANTO | PARAÍBA | Brasil | 2504900 | 25 | 33 | nan | nan | nan | Mata Atlântica | nan |
| db751784-5cb5-35f8-bc44-d4f4aace0eaf | -6.9687 | -43.536999 | 2024-12-19 00:03:00 | METOP-B | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| f4eca69c-c5c1-3323-96b7-39f1c3de927f | -4.8793 | -41.373299 | 2024-12-19 00:03:00 | METOP-B | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 6b99e63d-8698-39e8-a533-5841495cfcb0 | -4.3485 | -48.458599 | 2024-12-19 00:03:00 | METOP-B | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| bd04031c-7587-3185-957a-260cf45df72b | -6.3798 | -35.2281 | 2024-12-19 00:03:00 | METOP-B | CANGUARETAMA | RIO GRANDE DO NORTE | Brasil | 2402204 | 24 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 86eddfca-81f3-37ad-9456-acf16dba2030 | -5.1938 | -37.687099 | 2024-12-19 00:03:00 | METOP-B | BARAÚNA | RIO GRANDE DO NORTE | Brasil | 2401453 | 24 | 33 | nan | nan | nan | Caatinga | nan |
| f1b79a8c-768e-39bf-8100-d119be3cb3e6 | -10.7284 | -37.091499 | 2024-12-19 00:03:00 | METOP-B | MARUIM | SERGIPE | Brasil | 2804003 | 28 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 907105ae-3861-3ec0-8ab8-36345b2df781 | -4.7931 | -46.379501 | 2024-12-19 00:03:00 | METOP-B | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 7da52613-dfdb-3762-bb8d-d23b0817cbc4 | -5.2057 | -43.302799 | 2024-12-19 00:03:00 | METOP-B | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 0a206f6a-14f1-3193-9944-5d21fe2c4f73 | -4.486 | -45.416199 | 2024-12-19 00:03:00 | METOP-B | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 78fe6c2d-fd0f-379c-a9a8-a8dac08ac128 | -5.1175 | -44.374298 | 2024-12-19 00:03:00 | METOP-B | PRESIDENTE DUTRA | MARANHÃO | Brasil | 2109106 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 0618e4b8-9420-3d99-a63b-ee3824884af6 | -4.4778 | -45.425499 | 2024-12-19 00:03:00 | METOP-B | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 639dadc3-127f-3f4e-881b-db008cc0f54f | -8.9934 | -36.1544 | 2024-12-19 00:03:00 | METOP-B | CANHOTINHO | PERNAMBUCO | Brasil | 2603702 | 26 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 5b562405-78e7-3575-be69-408c023256ae | -2.7151 | -45.828602 | 2024-12-19 00:03:00 | METOP-B | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 35a81425-1c4f-3644-9ed7-11215f018029 | -5.3072 | -46.0546 | 2024-12-19 00:03:00 | METOP-B | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| da576a98-55d4-3406-a980-23aaff306ab5 | -2.843 | -49.489899 | 2024-12-19 00:03:00 | METOP-B | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ffe14ab6-381e-3c52-b36f-0457f228b9d2 | -6.9589 | -43.5392 | 2024-12-19 00:03:00 | METOP-B | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| caeac620-1097-3d9d-9345-1fcc5ad52ec7 | -5.8611 | -39.164299 | 2024-12-19 00:03:00 | METOP-B | SOLONÓPOLE | CEARÁ | Brasil | 2313005 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| 2cd41af2-5946-3e76-8bbb-eecea74501de | -6.0713 | -44.633301 | 2024-12-19 00:03:00 | METOP-B | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 66fb5024-b031-342f-b622-4c794983eba4 | -4.9173 | -41.314602 | 2024-12-19 00:03:00 | METOP-B | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 02050928-7353-388f-95bc-e271484017d0 | -4.8731 | -41.3913 | 2024-12-19 00:03:00 | METOP-B | MILTON BRANDÃO | PIAUÍ | Brasil | 2206357 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 5000cb8f-a167-31b3-a50c-68e689bdb317 | -1.4704 | -45.926701 | 2024-12-19 00:07:00 | METOP-B | LUÍS DOMINGUES | MARANHÃO | Brasil | 2106201 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| bcc6fa25-1208-3052-9bed-dca42a9fbc40 | -3.9962 | -46.357399 | 2024-12-19 00:07:00 | METOP-B | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 0c349ef8-7893-32fc-bf12-3e661d52ba7a | -1.7909 | -46.802799 | 2024-12-19 00:07:00 | METOP-B | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| df65bb9f-b292-3725-a559-ba447e5af42a | -4.0478 | -49.75 | 2024-12-19 00:07:00 | METOP-B | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ab22ec5a-c654-369e-ab8f-9bdb563fa4f6 | -5.2534 | -41.387402 | 2024-12-19 00:07:00 | METOP-B | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 09923c78-7a93-3098-a919-e46ba543f6d8 | -1.4689 | -45.919701 | 2024-12-19 00:07:00 | METOP-B | LUÍS DOMINGUES | MARANHÃO | Brasil | 2106201 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 322f02a2-068d-3f2e-8b1f-de7350517d1f | -3.6876 | -43.743401 | 2024-12-19 00:07:00 | METOP-B | VARGEM GRANDE | MARANHÃO | Brasil | 2112704 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| cd45d415-d324-33ce-bde9-df07e4b81ea5 | -3.4126 | -41.853699 | 2024-12-19 00:07:00 | METOP-B | CAXINGÓ | PIAUÍ | Brasil | 2202653 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 6e8a597c-9f6f-3ac1-ad28-54b0e9e9b99f | -3.2277 | -46.785702 | 2024-12-19 00:07:00 | METOP-B | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 87402838-a4d4-3219-b9f7-7cad7279ac74 | -1.7652 | -45.817799 | 2024-12-19 00:07:00 | METOP-B | CÂNDIDO MENDES | MARANHÃO | Brasil | 2102606 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 0a610236-3a0f-3eae-980e-1d0b65685c10 | -3.5878 | -44.534199 | 2024-12-19 00:07:00 | METOP-B | MIRANDA DO NORTE | MARANHÃO | Brasil | 2106755 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| e995b479-127e-3041-93ea-0fb99aa9dcb6 | -3.2294 | -46.793301 | 2024-12-19 00:07:00 | METOP-B | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| af617dc3-1d70-3ae5-a12c-be423f125391 | -4.0346 | -46.8997 | 2024-12-19 00:07:00 | METOP-B | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 61f69d1f-9d18-3b9e-a3e4-3eb298f4b409 | -3.6891 | -43.750198 | 2024-12-19 00:07:00 | METOP-B | VARGEM GRANDE | MARANHÃO | Brasil | 2112704 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| ae16ded1-4bd8-37a3-a752-d24b264a3457 | -4.331 | -48.2864 | 2024-12-19 00:07:00 | METOP-B | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 97902200-9031-3150-8692-7d301093b5c5 | -5.2516 | -41.379601 | 2024-12-19 00:07:00 | METOP-B | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 9f519ff5-1cbb-34cf-99ba-fbafbcb8b7f7 | -2.5218 | -47.2635 | 2024-12-19 00:07:00 | METOP-B | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 27d4921c-6af7-3045-8fb7-4c82f3f55467 | -3.5992 | -44.538799 | 2024-12-19 00:07:00 | METOP-B | MIRANDA DO NORTE | MARANHÃO | Brasil | 2106755 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| b73272c9-b33c-3e22-978a-eb2e811365f3 | -3.5863 | -44.527401 | 2024-12-19 00:07:00 | METOP-B | MIRANDA DO NORTE | MARANHÃO | Brasil | 2106755 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 2466c1aa-7136-3c5a-aca4-133b0823636e | -2.7359 | -46.197201 | 2024-12-19 00:07:00 | METOP-B | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 4aa955dc-114f-31fc-9bfb-212e43e1c871 | -3.226 | -46.778099 | 2024-12-19 00:07:00 | METOP-B | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 03813aa4-7c05-3dc6-a76f-d8375d088af3 | -3.8871 | -47.022301 | 2024-12-19 00:07:00 | METOP-B | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| ebfc806d-1697-3588-83b8-b520a3a8bc76 | -3.2375 | -46.7836 | 2024-12-19 00:07:00 | METOP-B | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b41c9962-0b10-3125-805d-54b355156236 | -3.9995 | -46.372299 | 2024-12-19 00:07:00 | METOP-B | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 1d1739e6-2573-3202-8944-63c4d4f41e3b | -1.7569 | -45.8269 | 2024-12-19 00:07:00 | METOP-B | CÂNDIDO MENDES | MARANHÃO | Brasil | 2102606 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 18bdd595-9a0e-3f32-bb31-fa57d8cd5745 | -3.4223 | -41.941002 | 2024-12-19 00:07:00 | METOP-B | MURICI DOS PORTELAS | PIAUÍ | Brasil | 2206696 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| f720a3b9-6b71-3624-bdbf-9bff42c776f5 | -3.6866 | -49.551201 | 2024-12-19 00:07:00 | METOP-B | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6a249fc9-357f-36a8-9730-248e133dcd09 | -3.2162 | -46.7803 | 2024-12-19 00:07:00 | METOP-B | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 79a8628f-1273-3c61-a3ea-892feb7cb78b | -3.689 | -49.562 | 2024-12-19 00:07:00 | METOP-B | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 05072aff-1567-3818-a560-cf3f467fd617 | -1.6067 | -45.845402 | 2024-12-19 00:07:00 | METOP-B | AMAPÁ DO MARANHÃO | MARANHÃO | Brasil | 2100550 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| faa44352-f3b8-33d4-a1f5-c554fd0f25ba | -3.2243 | -46.770599 | 2024-12-19 00:07:00 | METOP-B | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 9fc59e2d-b877-3c80-98c7-55c39673503b | -1.472 | -45.933701 | 2024-12-19 00:07:00 | METOP-B | LUÍS DOMINGUES | MARANHÃO | Brasil | 2106201 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| f2be37a7-ae95-32c0-95fc-cfbc9eb25315 | -3.9979 | -46.364799 | 2024-12-19 00:07:00 | METOP-B | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 79157a39-4822-3b0a-9424-75b1030bb5ae | -3.424 | -41.9487 | 2024-12-19 00:07:00 | METOP-B | MURICI DOS PORTELAS | PIAUÍ | Brasil | 2206696 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 879cb348-5386-32e7-8b90-0cedd0b74d8f | -3.2179 | -46.787899 | 2024-12-19 00:07:00 | METOP-B | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4a8c599a-9ec2-38cd-9a56-620ad2f56a06 | -2.2434 | -44.968102 | 2024-12-19 00:07:00 | METOP-B | PINHEIRO | MARANHÃO | Brasil | 2108603 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| cbedaa72-2604-3e5f-a7a2-482f87fe7c53 | -3.5894 | -44.541 | 2024-12-19 00:07:00 | METOP-B | MIRANDA DO NORTE | MARANHÃO | Brasil | 2106755 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 42b3efbd-7eb4-3510-b5d4-2ba9927cff48 | -3.6104 | -48.972801 | 2024-12-19 00:07:00 | METOP-B | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8f46da1d-b27f-3fbe-9237-3d16f594a2dd | -2.52 | -47.255699 | 2024-12-19 00:07:00 | METOP-B | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7d205a18-e861-3f6a-9e27-7cb99ec0f7e8 | -1.7553 | -45.819901 | 2024-12-19 00:07:00 | METOP-B | CÂNDIDO MENDES | MARANHÃO | Brasil | 2102606 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| dfc954f9-30f3-3bcc-bfe5-d9d54316ad6e | -1.7538 | -45.812901 | 2024-12-19 00:07:00 | METOP-B | CÂNDIDO MENDES | MARANHÃO | Brasil | 2102606 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| e14130d9-750a-363e-b7af-29f5896c2a3e | -1.7636 | -45.810799 | 2024-12-19 00:07:00 | METOP-B | CÂNDIDO MENDES | MARANHÃO | Brasil | 2102606 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 20dc3762-c0ca-3374-917a-26be0b0a1e1c | -3.5977 | -44.532001 | 2024-12-19 00:07:00 | METOP-B | MIRANDA DO NORTE | MARANHÃO | Brasil | 2106755 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 38a0a11f-7ee2-33b9-955a-30b8886b0499 | -3.9881 | -46.366901 | 2024-12-19 00:07:00 | METOP-B | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 1ac3199e-e837-3b76-a1bd-bfff7c6651df | -4.333 | -48.295601 | 2024-12-19 00:07:00 | METOP-B | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 83529f99-f308-3f23-b24a-db6eb6409794 | -3.2135 | -46.8063 | 2024-12-19 00:10:00 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 125.7 |
| d14f7fa8-2137-3964-ba5f-bf5b614af605 | -3.232 | -46.8056 | 2024-12-19 00:10:00 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 263.7 |
| 857f93ba-09bf-37be-bd14-b08091f69353 | -3.2136 | -46.7843 | 2024-12-19 00:10:00 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 120.2 |
| aa8cd3d8-6b46-3e0b-9ad2-16d0ff0dd002 | -3.2321 | -46.7836 | 2024-12-19 00:10:00 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 251.0 |


[Clique aqui para ver as próximas entradas](README3.md)
