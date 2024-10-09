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

## Dados Diários - Página 12

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| f0c7f6f1-3514-3d6d-847e-6f05ace333e8 | -13.8059 | -43.600399 | 2024-10-09 00:39:13 | METOP-C | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 917f3419-c9db-35c2-aaf8-a5cdeb467420 | -13.8076 | -43.6077 | 2024-10-09 00:39:13 | METOP-C | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| dcc065f6-7e4c-3de1-add3-edddda100f85 | -14.199 | -45.5121 | 2024-10-09 00:39:14 | METOP-C | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 49f98404-45ef-3db7-b8dc-33005f6059f2 | -14.1828 | -45.486 | 2024-10-09 00:39:14 | METOP-C | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| f184f883-72d9-3353-b00e-2ca8c551ac69 | -14.1974 | -45.505001 | 2024-10-09 00:39:14 | METOP-C | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 77887a1b-4962-3908-8dbf-9ab98a795d8b | -13.8749 | -44.123798 | 2024-10-09 00:39:14 | METOP-C | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 6e3e4158-91de-3ad4-af19-1fa391c0acf1 | -14.1844 | -45.493099 | 2024-10-09 00:39:14 | METOP-C | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 961534dc-8516-3b11-a17b-4574880a4093 | -14.186 | -45.500198 | 2024-10-09 00:39:14 | METOP-C | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| ea3c44c7-6b5a-3e5a-b624-9f0fcc723820 | -14.1746 | -45.4953 | 2024-10-09 00:39:14 | METOP-C | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| b55652b0-bb7f-3c23-9507-e63ba7db6abe | -13.8976 | -44.268398 | 2024-10-09 00:39:14 | METOP-C | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| de840c23-a6ae-36b8-8fe8-1e988b52f9bb | -13.8993 | -44.275501 | 2024-10-09 00:39:14 | METOP-C | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| fe68633e-b24a-3434-9972-60f11324cbd1 | -13.9361 | -44.527699 | 2024-10-09 00:39:14 | METOP-C | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| c28ce00b-bac7-3f6e-b3ef-c2e83467e3ed | -13.9377 | -44.534801 | 2024-10-09 00:39:14 | METOP-C | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 7a8750e1-7e38-3a7a-a189-a957c7fbe55a | -13.9393 | -44.541801 | 2024-10-09 00:39:14 | METOP-C | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 2a336bcb-f7ea-318b-ad5a-e3b75268a66e | -13.9264 | -44.530102 | 2024-10-09 00:39:15 | METOP-C | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| ad57c03a-ed35-367c-8692-a2649fa4ccca | -13.928 | -44.537102 | 2024-10-09 00:39:15 | METOP-C | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 70a9fd32-300d-32dc-94b4-b4a3586c4549 | -13.9118 | -44.5112 | 2024-10-09 00:39:15 | METOP-C | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| ceddf0ef-4d70-3d89-9816-73c4bbbcc62d | -13.9134 | -44.518299 | 2024-10-09 00:39:15 | METOP-C | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 3c96e04a-d63c-38b1-a637-50e06b100d72 | -13.915 | -44.525299 | 2024-10-09 00:39:15 | METOP-C | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 4af8b7b0-aafe-36a0-b376-ef7e7d0c596c | -13.9166 | -44.532398 | 2024-10-09 00:39:15 | METOP-C | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 7d697148-9c94-35bf-8dfe-1546f1ee7f9d | -13.9198 | -44.546501 | 2024-10-09 00:39:15 | METOP-C | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| daa62fac-5134-3182-bd93-3abedeffac78 | -13.9214 | -44.553501 | 2024-10-09 00:39:15 | METOP-C | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 93843264-ff2d-3bff-935c-e2521ff2490d | -13.923 | -44.5606 | 2024-10-09 00:39:15 | METOP-C | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| e9dceefe-8f1e-3652-99cb-5360c4b34cba | -13.9246 | -44.5676 | 2024-10-09 00:39:15 | METOP-C | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 41b861f2-2d85-3d71-a275-47a6ba5caa13 | -13.902 | -44.5135 | 2024-10-09 00:39:15 | METOP-C | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 2696d1e0-4103-31c4-9f95-fb19c9375606 | -13.9036 | -44.520599 | 2024-10-09 00:39:15 | METOP-C | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 9f3bf901-5d4b-3cf3-adac-ebf8d9270761 | -13.9052 | -44.527599 | 2024-10-09 00:39:15 | METOP-C | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 3aec9939-e6f5-375b-8090-d5577758988c | -13.9068 | -44.534698 | 2024-10-09 00:39:15 | METOP-C | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| e6f73650-e1f9-351f-902a-749afb5bdf39 | -13.91 | -44.548801 | 2024-10-09 00:39:15 | METOP-C | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| d8264ac6-bed3-36f2-a392-fffc4e7f573a | -13.9132 | -44.562901 | 2024-10-09 00:39:15 | METOP-C | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| f25d83b6-7d64-35f3-9bf1-b1c1ec678a1d | -13.8938 | -44.5229 | 2024-10-09 00:39:15 | METOP-C | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 38ae0c28-6b1c-3157-9235-eb9fd0c21f67 | -13.8954 | -44.5299 | 2024-10-09 00:39:15 | METOP-C | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| b5b52363-1b5b-352e-aabe-934025f2ae2f | -13.897 | -44.536999 | 2024-10-09 00:39:15 | METOP-C | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 402f6574-0556-36c4-909f-0f8dca573dae | -13.9034 | -44.565201 | 2024-10-09 00:39:15 | METOP-C | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 96899c3f-844b-3020-bd15-c35bf3890995 | -13.9147 | -44.614498 | 2024-10-09 00:39:15 | METOP-C | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 0fd4cbb3-9eb3-3c49-a94d-aa892dad09f5 | -13.9163 | -44.621601 | 2024-10-09 00:39:15 | METOP-C | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 08479aca-f8be-3747-91ff-5ad02babbeba | -13.9179 | -44.628601 | 2024-10-09 00:39:15 | METOP-C | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 57ac602d-2f3c-39e5-87a5-c76e2c88537e | -13.884 | -44.5252 | 2024-10-09 00:39:15 | METOP-C | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| e5bd3690-f7d0-382e-9314-eb63992e0e69 | -13.8856 | -44.5322 | 2024-10-09 00:39:15 | METOP-C | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 6721a8e4-bf54-36a1-8b71-6eb135a77d72 | -13.8872 | -44.539299 | 2024-10-09 00:39:15 | METOP-C | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 3ce6f14a-ebeb-3a0e-90d6-76d84c408438 | -13.8888 | -44.546299 | 2024-10-09 00:39:15 | METOP-C | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 3a76d958-b483-3b7a-8aff-b596c9f6cc40 | -13.9049 | -44.616798 | 2024-10-09 00:39:15 | METOP-C | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| d3f60772-23a9-3888-8996-93af943e33ea | -13.9065 | -44.623901 | 2024-10-09 00:39:15 | METOP-C | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 1cb34186-8d42-3d71-8bcc-4a004c1ebd75 | -13.8758 | -44.5345 | 2024-10-09 00:39:15 | METOP-C | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 6766cc12-7bc3-3e48-9267-9063ecacbb1e | -13.8774 | -44.541599 | 2024-10-09 00:39:15 | METOP-C | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 5ebb2f47-e701-3910-aa25-3ec4200c77b7 | -14.0376 | -45.526901 | 2024-10-09 00:39:16 | METOP-C | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| a1783b48-4acf-3d36-8b24-306c5ff2fce1 | -14.0392 | -45.534 | 2024-10-09 00:39:16 | METOP-C | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 51ce871b-0546-36b7-ab49-1171b8156258 | -14.0408 | -45.5411 | 2024-10-09 00:39:16 | METOP-C | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| d7c644cd-5bca-358f-a8e1-4aa638a664bb | -13.8676 | -44.5439 | 2024-10-09 00:39:16 | METOP-C | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 6ddc1979-9cca-3f8a-b816-71ffadcafac1 | -13.8431 | -44.571899 | 2024-10-09 00:39:16 | METOP-C | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| c1272b5f-dd76-31ff-b0dd-1b07eb174455 | -13.8447 | -44.578999 | 2024-10-09 00:39:16 | METOP-C | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 2aeb28bd-0028-3b69-8b53-b0fd1b9799b5 | -13.8349 | -44.581299 | 2024-10-09 00:39:16 | METOP-C | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 577c0741-5cc0-3ad6-82f8-b14cf19764e1 | -13.8365 | -44.588299 | 2024-10-09 00:39:16 | METOP-C | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| d8ad5725-7276-37d1-90d3-0e87669ea4c9 | -13.8267 | -44.590599 | 2024-10-09 00:39:16 | METOP-C | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| a7c372a6-26f2-3770-89b7-276ee2f75049 | -14.9492 | -50.058601 | 2024-10-09 00:39:17 | METOP-C | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| a74e36c0-a721-378c-8462-95bef32bf802 | -13.5701 | -43.741199 | 2024-10-09 00:39:17 | METOP-C | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 69d900ed-efa6-3f19-990b-474ec03582a1 | -13.5717 | -43.748501 | 2024-10-09 00:39:17 | METOP-C | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 7b921e1b-7584-3f34-8df8-3623cd0c1f1d | -13.4334 | -43.197701 | 2024-10-09 00:39:18 | METOP-C | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| 7e81f90a-cf67-3778-b30d-9e42516952b6 | -13.4352 | -43.205299 | 2024-10-09 00:39:18 | METOP-C | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| a3c7d40b-8c03-3482-b8dd-a5b1837544cb | -13.4369 | -43.212799 | 2024-10-09 00:39:18 | METOP-C | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| 04b93593-c45c-3e33-b9f8-34b51b3f3410 | -13.4213 | -43.723 | 2024-10-09 00:39:20 | METOP-C | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 03e28035-a773-3738-9d3e-2af1b13d32f3 | -13.4099 | -43.718102 | 2024-10-09 00:39:20 | METOP-C | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 608fd09d-4e4a-3115-8963-23cff93aaeae | -13.4116 | -43.725399 | 2024-10-09 00:39:20 | METOP-C | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| a320ac63-1c5f-3c88-8256-5333a873a872 | -13.4267 | -43.790699 | 2024-10-09 00:39:20 | METOP-C | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| cfb06eec-f827-3ba4-9916-ab373c38787c | -13.4284 | -43.798 | 2024-10-09 00:39:20 | METOP-C | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 47436b81-7714-3a89-ba07-2293203398b7 | -13.4169 | -43.793098 | 2024-10-09 00:39:20 | METOP-C | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| fd1e5584-b373-3bc1-8489-363e02933e1b | -13.4186 | -43.800301 | 2024-10-09 00:39:20 | METOP-C | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| d7a3f0ea-df74-31b3-b180-59b94d905c5e | -13.3775 | -43.7565 | 2024-10-09 00:39:21 | METOP-C | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 69b02746-88f4-3992-9b79-379cfabc9578 | -13.3792 | -43.763802 | 2024-10-09 00:39:21 | METOP-C | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 3bcf3a69-ea4b-38e2-8999-6aade94a27aa | -13.3744 | -43.787899 | 2024-10-09 00:39:21 | METOP-C | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| fff8d134-f4cb-3f15-bc90-879b0824b6cd | -13.3713 | -44.764 | 2024-10-09 00:39:24 | METOP-C | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| ad3c0499-9117-3515-bf26-9124092902ca | -13.3729 | -44.771 | 2024-10-09 00:39:24 | METOP-C | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| ee1c5d9b-3399-3a1f-aa8d-71b33173b1c7 | -13.543 | -45.4333 | 2024-10-09 00:39:24 | METOP-C | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| ae31daa4-fa48-3f9e-9d2a-27f700b825f5 | -13.5445 | -45.4403 | 2024-10-09 00:39:24 | METOP-C | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 1f5357e7-2fea-3083-a119-35c7f7240ea7 | -13.5461 | -45.447399 | 2024-10-09 00:39:24 | METOP-C | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| f8839628-84db-3369-a979-87f4d01ca367 | -13.3631 | -44.7733 | 2024-10-09 00:39:25 | METOP-C | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| ffe8b82f-7882-3fbb-acf3-d2e5a4a376cd | -12.7807 | -43.409901 | 2024-10-09 00:39:29 | METOP-C | SÍTIO DO MATO | BAHIA | Brasil | 2930758 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 1a7e8809-ea2a-3d9a-8508-4780d0fda157 | -12.4135 | -42.334702 | 2024-10-09 00:39:31 | METOP-C | BROTAS DE MACAÚBAS | BAHIA | Brasil | 2904506 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| 57981a6a-e094-346d-8bd9-8a385a412c07 | -12.3722 | -42.5089 | 2024-10-09 00:39:32 | METOP-C | OLIVEIRA DOS BREJINHOS | BAHIA | Brasil | 2923209 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| fea95ddc-aa95-3bae-ad0c-0f5acff3b839 | -12.8812 | -44.6045 | 2024-10-09 00:39:32 | METOP-C | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 96b7e81b-912c-3d31-840a-3ab76841a9ec | -12.8828 | -44.6115 | 2024-10-09 00:39:32 | METOP-C | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 73b51c26-a984-3281-8c79-6d50158d7378 | -12.8714 | -44.6068 | 2024-10-09 00:39:32 | METOP-C | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 3ffa52ec-3b99-32d1-9fff-4c1ec851d480 | -12.873 | -44.6138 | 2024-10-09 00:39:32 | METOP-C | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| f03d1cae-07b7-3c97-bdd4-fdc7dde68545 | -12.8746 | -44.620899 | 2024-10-09 00:39:32 | METOP-C | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| b41bc166-1e14-3266-9b07-d62b0746b623 | -12.7823 | -44.8941 | 2024-10-09 00:39:34 | METOP-C | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| b36650ea-f2f5-3d77-8bcb-1300abeed1d1 | -12.7677 | -44.875301 | 2024-10-09 00:39:35 | METOP-C | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 2ce2f55c-c2d8-3072-9bbd-89643061a306 | -12.7693 | -44.882301 | 2024-10-09 00:39:35 | METOP-C | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| bb0aa30b-c49d-34e2-a7a8-cebe0b213dc5 | -12.7709 | -44.889301 | 2024-10-09 00:39:35 | METOP-C | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| c4ce3a72-f7bb-3ddd-ae27-0361739d895d | -12.7579 | -44.877602 | 2024-10-09 00:39:35 | METOP-C | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 9bc6b19f-26ed-35f8-9a46-24214fdc8f09 | -12.7595 | -44.884602 | 2024-10-09 00:39:35 | METOP-C | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 9d03fa1d-a962-3a92-b850-73b7964ddc4c | -12.7611 | -44.891602 | 2024-10-09 00:39:35 | METOP-C | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| bd838358-980c-3184-9f4b-4239d3ed8374 | -12.9834 | -46.201 | 2024-10-09 00:39:36 | METOP-C | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 0a759218-fa3f-3a1f-b500-684b23f52741 | -12.985 | -46.208099 | 2024-10-09 00:39:36 | METOP-C | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 7f6881dc-cfd3-38fa-8539-d66c0d621071 | -12.3623 | -44.7258 | 2024-10-09 00:39:41 | METOP-C | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 5951059e-bd7d-3e69-8f17-38cb162a0519 | -12.3639 | -44.732899 | 2024-10-09 00:39:41 | METOP-C | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| a9ee3b5d-f42a-3af7-88d3-3d307e972450 | -12.3744 | -44.959499 | 2024-10-09 00:39:41 | METOP-C | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 5d9faa94-f0f4-3c32-b3f5-e28d59ad7628 | -12.376 | -44.966499 | 2024-10-09 00:39:41 | METOP-C | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 9fb2ce82-60e1-3cda-8c57-c923a11a5759 | -12.3776 | -44.973499 | 2024-10-09 00:39:41 | METOP-C | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 0fa41f16-e975-3840-9f84-5579a32b878f | -12.6621 | -47.027802 | 2024-10-09 00:39:44 | METOP-C | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| c230f439-6e92-31f1-9335-f2bbae6a0559 | -12.6523 | -47.029999 | 2024-10-09 00:39:44 | METOP-C | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | nan |


[Clique aqui para ver as próximas entradas](README13.md)
