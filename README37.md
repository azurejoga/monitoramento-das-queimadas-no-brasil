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

## Dados Diários - Página 37

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| f3f7f41d-af36-3389-9e04-771431a53980 | -5.45346 | -42.80869 | 2025-09-08 04:00:00 | NOAA-20 | NAZÁRIA | PIAUÍ | Brasil | 2206720 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| f9aab516-c9b3-3e8e-9fce-021436b311d5 | -6.13836 | -44.23137 | 2025-09-08 04:00:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| f7e803d4-a7fd-3cec-aec7-6a6d48b3f72e | -4.67471 | -41.01349 | 2025-09-08 04:00:00 | NOAA-20 | PORANGA | CEARÁ | Brasil | 2311009 | 23 | 33 | nan | nan | nan | Caatinga | 1.0 |
| be46b520-a30a-350f-bddf-768fb0c6d562 | -8.29662 | -45.95088 | 2025-09-08 04:00:00 | NOAA-20 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 9e404238-2881-3838-a35f-fc76dd344f85 | -5.41753 | -42.68922 | 2025-09-08 04:00:00 | NOAA-20 | LAGOA DO PIAUÍ | PIAUÍ | Brasil | 2205581 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| d8ba0b00-93c4-30b9-9558-4140a8b3b5ec | -7.2969 | -44.14621 | 2025-09-08 04:00:00 | NOAA-20 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 56ef5530-8f76-3b9f-be7c-e2f8e6ebd110 | -6.46755 | -43.95346 | 2025-09-08 04:00:00 | NOAA-20 | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 3fe4c96a-9f37-33b3-90d0-a3b031f2c54b | -5.73506 | -45.37349 | 2025-09-08 04:00:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 8e4941c2-8280-3e24-a7c2-33a57b40c059 | -6.67033 | -44.56202 | 2025-09-08 04:00:00 | NOAA-20 | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| e29cb703-47d8-3933-b36f-6a7748c087c0 | -6.40542 | -42.9912 | 2025-09-08 04:00:00 | NOAA-20 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| e7367b6a-92a8-314b-84a0-25c99e36f8eb | -7.17314 | -46.18747 | 2025-09-08 04:00:00 | NOAA-20 | NOVA COLINAS | MARANHÃO | Brasil | 2107258 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| c7df7c68-ba88-3881-832e-6130bd10f113 | -4.66066 | -46.3576 | 2025-09-08 04:00:00 | NOAA-20 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 53714b89-4dfd-3a92-853d-5725c3732a0b | -6.19269 | -42.64595 | 2025-09-08 04:00:00 | NOAA-20 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| dbaceed1-5664-31a9-a5eb-05102632ba3c | -6.97381 | -45.56974 | 2025-09-08 04:00:00 | NOAA-20 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 8f84816b-9db9-336c-b22b-510034037999 | -6.13809 | -43.30156 | 2025-09-08 04:00:00 | NOAA-20 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 3.1 |
| 36b794d2-660d-301c-ad5f-566e7d3e2e2e | -7.75589 | -44.0047 | 2025-09-08 04:00:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 2f50a09f-da8a-3bab-9a41-eecab5328bbf | -6.00385 | -46.19136 | 2025-09-08 04:00:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 276b0a39-9aee-3816-91e2-f56e01432aa5 | -6.19665 | -40.97289 | 2025-09-08 04:00:00 | NOAA-20 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| d8a76276-0c70-35ba-80d3-1da0fcd6227a | -6.18513 | -43.59082 | 2025-09-08 04:00:00 | NOAA-20 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 1b4a956c-de07-348c-9bdb-70c629aca0d0 | -6.64475 | -44.80805 | 2025-09-08 04:00:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| f2210284-6f18-3448-aa69-8f0f7678de5d | -6.53381 | -42.42037 | 2025-09-08 04:00:00 | NOAA-20 | ARRAIAL | PIAUÍ | Brasil | 2201002 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 0f60d765-97f4-3a5d-8463-5237501f42fb | -5.21158 | -45.83051 | 2025-09-08 04:00:00 | NOAA-20 | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 1a8b4ca4-77a8-3db7-bc54-5e109771c419 | -6.84493 | -52.85349 | 2025-09-08 04:00:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 7d1d73bd-e67a-3579-93dd-909a2a0e2015 | -7.83148 | -44.85847 | 2025-09-08 04:00:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| d0e5a6c3-76fa-37d0-b9f1-c67f1f9ca8eb | -3.79062 | -48.87389 | 2025-09-08 04:00:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| fe09afd7-82fc-3cbf-8449-335593f4ebd5 | -6.38682 | -42.99236 | 2025-09-08 04:00:00 | NOAA-20 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 96a8d0f0-57f3-3bcb-afda-a6568328c14e | -5.22137 | -43.70042 | 2025-09-08 04:00:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 19b6b07c-1c59-30e6-ace6-7894a5a52e53 | -5.76451 | -42.36116 | 2025-09-08 04:00:00 | NOAA-20 | PASSAGEM FRANCA DO PIAUÍ | PIAUÍ | Brasil | 2207751 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| d0eeb322-1d5c-31f0-a825-0a33b86679d1 | -6.26515 | -42.57896 | 2025-09-08 04:00:00 | NOAA-20 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 2eaba857-13af-3a03-913f-1adaa69881ce | -5.63633 | -43.11802 | 2025-09-08 04:00:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Caatinga | 1.4 |
| a1c9c6c4-26c0-3956-b784-6db1c4dad96f | -6.93248 | -43.23626 | 2025-09-08 04:00:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 33722910-fd15-390b-b67e-ca8f2fa9cb9a | -5.18361 | -42.8142 | 2025-09-08 04:00:00 | NOAA-20 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 7afb26c2-73be-3d57-b4b1-e974cf318466 | -7.57648 | -44.00626 | 2025-09-08 04:00:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 59250e3b-95e0-3157-83d3-6a0c275e86e5 | -4.55749 | -41.78329 | 2025-09-08 04:00:00 | NOAA-20 | CAPITÃO DE CAMPOS | PIAUÍ | Brasil | 2202406 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 45f63245-34d0-3ac3-9ba6-1029f6779288 | -6.30353 | -44.78923 | 2025-09-08 04:00:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 4d22989e-eb65-3d40-bda5-2bd27c751533 | -7.09701 | -43.8995 | 2025-09-08 04:00:00 | NOAA-20 | MARCOS PARENTE | PIAUÍ | Brasil | 2206001 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 54a5a9a4-7e1a-3d43-9afe-ea07e0acd084 | -6.06286 | -43.30418 | 2025-09-08 04:00:00 | NOAA-20 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 1.1 |
| ca786cd7-c8a8-379c-a1c0-b166eb11aa3f | -8.04307 | -44.06764 | 2025-09-08 04:00:00 | NOAA-20 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 8f8296a5-8048-3e76-940b-bffc2cc8e781 | -5.87615 | -43.9649 | 2025-09-08 04:00:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| a93f39c7-8496-36cf-83f0-d9a315170a00 | -6.18884 | -43.59141 | 2025-09-08 04:00:00 | NOAA-20 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| b0f2713b-65ec-3a50-8e75-5128f6822516 | -6.23984 | -43.52567 | 2025-09-08 04:00:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| d92ad140-3c70-3f5e-a4e5-f2469df1f6b9 | -6.62564 | -53.37034 | 2025-09-08 04:00:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 2c32afbb-1c1c-3dd2-bdf0-69d393a8cbec | -7.81743 | -45.42268 | 2025-09-08 04:00:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| c603b695-3485-3de5-8c15-57d28e76fdbe | -9.72111 | -43.9814 | 2025-09-08 04:02:00 | NOAA-20 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 142396b7-0054-3344-a989-97cdc75c9319 | -11.86859 | -50.96784 | 2025-09-08 04:02:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 6952718e-b3a8-34e0-8c91-51a964ff9cdc | -11.27844 | -46.47395 | 2025-09-08 04:02:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 9bbd7ba9-9bc2-3036-9db3-9c6192f59406 | -10.07779 | -48.10398 | 2025-09-08 04:02:00 | NOAA-20 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| baff4787-d677-3a50-ade7-9896e5eebe0a | -11.20973 | -55.01461 | 2025-09-08 04:02:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 97ccaf6a-9239-3c43-89fb-d9e60fa84721 | -10.80149 | -47.73838 | 2025-09-08 04:02:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 51e3300d-4f38-317e-a2a7-ba1e91f5de07 | -9.15019 | -46.07186 | 2025-09-08 04:02:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 501d6d63-13a7-3979-8792-6b95e7c90505 | -12.92639 | -54.77596 | 2025-09-08 04:02:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 10bd95a8-3dc8-3919-a2b4-d0cdbbb95c9e | -11.36473 | -45.59293 | 2025-09-08 04:02:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 67485a02-2f4e-38bb-a571-ac57230ea475 | -11.4229 | -43.65992 | 2025-09-08 04:02:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 869888b4-c78b-3d7d-b4c6-aabcef7d0a4b | -9.07178 | -46.99952 | 2025-09-08 04:02:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| aec85e8b-e7cb-32fb-9425-a57a6cd2455b | -10.13692 | -46.19179 | 2025-09-08 04:02:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 7e250ea1-1328-3ddd-aef1-140cc0e30577 | -10.14056 | -46.21935 | 2025-09-08 04:02:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 4ef43acf-9c13-3705-a088-22549a643c51 | -15.34858 | -49.12364 | 2025-09-08 04:02:00 | NOAA-20 | GOIANÉSIA | GOIÁS | Brasil | 5208608 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 98e5ebe6-9989-36ce-b12b-5d6bb8814644 | -9.60438 | -45.10432 | 2025-09-08 04:02:00 | NOAA-20 | MONTE ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2206605 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 23c24bae-d617-3451-bdde-1ee123072943 | -9.71761 | -43.98348 | 2025-09-08 04:02:00 | NOAA-20 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 0d7dee13-e323-3d14-92be-5c8258937517 | -11.42073 | -43.65138 | 2025-09-08 04:02:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| f8ff8f8b-a4cf-3eef-bacf-f664999a1b5e | -9.14672 | -46.06739 | 2025-09-08 04:02:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 8e6c590b-fe1e-3f24-9878-3b4a0684c2c1 | -12.85368 | -47.98254 | 2025-09-08 04:02:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 17ce9d34-d39a-3697-9e13-0e76541acbfc | -13.69421 | -45.48426 | 2025-09-08 04:02:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f513fe8b-60f8-3b4c-b258-175314cdeb55 | -11.40546 | -50.3923 | 2025-09-08 04:02:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 10.3 |
| 3eee8517-4811-331c-9ebb-2c600416f1d5 | -13.81593 | -46.25401 | 2025-09-08 04:02:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 7f109d9c-3388-32fd-8523-7730569d38fa | -13.81514 | -46.28105 | 2025-09-08 04:02:00 | NOAA-20 | GUARANI DE GOIÁS | GOIÁS | Brasil | 5209408 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 8a6746b5-9421-3ec7-ab37-a081de0144d8 | -11.3277 | -46.55563 | 2025-09-08 04:02:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 50497ecd-9e19-3b7f-8851-28434d075343 | -14.99908 | -48.01086 | 2025-09-08 04:02:00 | NOAA-20 | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b6cbf3b6-45f4-3aaa-ae8b-65ea6e251599 | -13.9202 | -48.02335 | 2025-09-08 04:02:00 | NOAA-20 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 31313866-3592-33cf-8407-b30ad89c9383 | -11.41168 | -50.36915 | 2025-09-08 04:02:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 9780bb3e-9ec7-3e5e-abb4-3fa373dd341e | -14.51865 | -48.76472 | 2025-09-08 04:02:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 644abdc8-e379-3d98-94f5-48fe88e00bc0 | -14.52909 | -53.98797 | 2025-09-08 04:02:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 3.5 |
| f7cfb1e4-4e61-3699-908c-ff71c46f485b | -11.40676 | -50.38559 | 2025-09-08 04:02:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 0f325537-210d-3e87-8294-03a89fe153ae | -11.86116 | -51.06464 | 2025-09-08 04:02:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 0d926ffd-8040-39a3-ba26-9c4f960f5532 | -11.40741 | -50.38224 | 2025-09-08 04:02:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 8.2 |
| b49455c3-10fe-3ac2-ab5a-31ef3b9965b3 | -10.82494 | -47.73713 | 2025-09-08 04:02:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 0a865413-9a0b-3e68-8b48-c1f87dd62b38 | -11.02981 | -45.94186 | 2025-09-08 04:02:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.1 |
| ee8f1adf-a7f8-3dd3-9275-4f63d2ac967a | -15.44671 | -44.34726 | 2025-09-08 04:02:00 | NOAA-20 | JANUÁRIA | MINAS GERAIS | Brasil | 3135209 | 31 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 216b3618-a28f-30eb-88d5-c674b5c42975 | -11.28581 | -46.45626 | 2025-09-08 04:02:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 31.2 |
| c25771f4-57b3-33c9-942d-1ae73d113cf2 | -11.41205 | -43.58949 | 2025-09-08 04:02:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 4f9c5ffe-c8db-324c-a189-5efe99b69468 | -9.80397 | -46.23121 | 2025-09-08 04:02:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 7450d6fd-4e80-31e7-bec4-22b66be52490 | -9.20213 | -46.04253 | 2025-09-08 04:02:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| dc76b749-966d-3993-baab-967d1f184ee6 | -9.88036 | -46.53888 | 2025-09-08 04:02:00 | NOAA-20 | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 8.2 |
| 62dbdc21-2b89-38be-b8fe-ebbf66c7dc94 | -13.03482 | -47.13354 | 2025-09-08 04:02:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ab23dbd8-2345-3620-9d11-a2f3808c0ce6 | -9.14756 | -46.0759 | 2025-09-08 04:02:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 3aac0f7f-af15-359b-a923-d5dcbe38ab87 | -12.93044 | -54.78997 | 2025-09-08 04:02:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 3.3 |
| d1ce8b60-245e-3118-a816-ea5d329fb67b | -12.87215 | -47.98125 | 2025-09-08 04:02:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 63809fc6-7722-360a-8547-0335cf632d55 | -9.2008 | -46.05024 | 2025-09-08 04:02:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 5.0 |
| fcbc61c1-1e6e-3202-a1a3-41be07b5b38e | -9.44256 | -49.44075 | 2025-09-08 04:02:00 | NOAA-20 | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 633e7f85-24ee-3a98-8b0e-fa991a84665c | -11.2153 | -55.02311 | 2025-09-08 04:02:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c22b7c93-5591-3139-8ab9-2ba799c2a84e | -11.41043 | -50.37587 | 2025-09-08 04:02:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 41bc986f-3b18-34ec-8df4-9c0b430a7e6e | -13.71711 | -46.89777 | 2025-09-08 04:02:00 | NOAA-20 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| d7c2b3b9-15d6-3780-b6bf-ac305cd922fa | -13.80933 | -46.26852 | 2025-09-08 04:02:00 | NOAA-20 | GUARANI DE GOIÁS | GOIÁS | Brasil | 5209408 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| f4a13376-e0fb-3da9-9607-1edc3d842508 | -11.27895 | -46.4473 | 2025-09-08 04:02:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 20ea4640-36be-3815-90d6-6ad3a6cb1df9 | -10.73827 | -46.33584 | 2025-09-08 04:02:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| d5f8aade-574c-3561-ad9e-e187aa69618a | -11.14636 | -45.25442 | 2025-09-08 04:02:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| b1745587-d855-3759-bf7e-215633474162 | -9.99223 | -51.66987 | 2025-09-08 04:02:00 | NOAA-20 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 1b6e19c9-1c9b-3379-bc6b-5a10b61ab631 | -14.50445 | -48.80955 | 2025-09-08 04:02:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 1b815a10-d093-30bd-9bda-943233927592 | -11.81703 | -46.76689 | 2025-09-08 04:02:00 | NOAA-20 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| de75492f-f75c-3043-a377-4639c6796538 | -10.28583 | -48.80194 | 2025-09-08 04:02:00 | NOAA-20 | PARAÍSO DO TOCANTINS | TOCANTINS | Brasil | 1716109 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |


[Clique aqui para ver as próximas entradas](README38.md)
