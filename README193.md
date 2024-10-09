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

## Dados Diários - Página 193

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 5108d7fc-9e07-3b69-9507-b41704354a31 | -16.1565 | -55.89417 | 2024-10-09 05:06:00 | NOAA-20 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 1.4 |
| 4d3d1b02-ed0e-3b6d-bd34-a754c2bf0ba7 | -16.15594 | -55.89803 | 2024-10-09 05:06:00 | NOAA-20 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 1.4 |
| ae530fa6-c476-3226-b8d0-1fe3b36cfd61 | -16.13082 | -55.85922 | 2024-10-09 05:06:00 | NOAA-20 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 2.4 |
| cedd893e-1134-3782-95dd-fe0024739462 | -16.13024 | -55.86312 | 2024-10-09 05:06:00 | NOAA-20 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 2.4 |
| 26c7aa25-78ba-345f-8070-3353771c9bb0 | -16.12795 | -55.85479 | 2024-10-09 05:06:00 | NOAA-20 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 2.1 |
| f2196f01-a7da-364e-9c9d-c770d19ac344 | -16.12737 | -55.85868 | 2024-10-09 05:06:00 | NOAA-20 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 2.4 |
| b159eb27-471f-3797-8817-3262fc8fb838 | -16.1245 | -55.85428 | 2024-10-09 05:06:00 | NOAA-20 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 1.8 |
| 235d3831-d166-3353-bcd6-ee1e83af4245 | -16.21719 | -54.9959 | 2024-10-09 05:06:00 | NOAA-20 | JUSCIMEIRA | MATO GROSSO | Brasil | 5105200 | 51 | 33 | nan | nan | nan | Cerrado | 6.0 |
| b3b59d7c-3306-3929-9691-8bec66b4a922 | -16.2166 | -55.00007 | 2024-10-09 05:06:00 | NOAA-20 | JUSCIMEIRA | MATO GROSSO | Brasil | 5105200 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 75f4b764-d73b-3f16-b2e7-397781b59d28 | -16.21363 | -54.99533 | 2024-10-09 05:06:00 | NOAA-20 | JUSCIMEIRA | MATO GROSSO | Brasil | 5105200 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| ce0459bd-3b3e-3231-837d-2022e036e39b | -16.60462 | -55.88919 | 2024-10-09 05:06:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 0.8 |
| 3e642712-295e-35f6-99af-de81db7769df | -16.60405 | -55.89312 | 2024-10-09 05:06:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 0.8 |
| d2af0e26-fdfa-330b-9c12-fdbc41d76a0a | -16.60348 | -55.89703 | 2024-10-09 05:06:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 0.3 |
| d2985f95-689e-3fab-9165-cbbc7c6db6bb | -16.60003 | -55.89649 | 2024-10-09 05:06:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 0.3 |
| f0e3e723-e39a-344d-9543-2d41e3000984 | -16.58163 | -55.90161 | 2024-10-09 05:06:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.2 |
| 4c0465da-58fc-3cdf-942b-d20fbb4a3625 | -16.57449 | -56.0716 | 2024-10-09 05:06:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.3 |
| dda4ff0d-d365-350b-9ba6-13a6606a6fc9 | -16.56768 | -55.90836 | 2024-10-09 05:06:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.9 |
| e449a2d1-1058-32fa-9216-ae3b0cdd799d | -16.56423 | -55.90783 | 2024-10-09 05:06:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.0 |
| f3d6a7b8-ff0d-31e8-adc8-4745b29f7691 | -16.54526 | -55.91684 | 2024-10-09 05:06:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.2 |
| 8bdecdc9-2ebc-3950-a989-62ecc1346704 | -16.54468 | -55.92073 | 2024-10-09 05:06:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.4 |
| a3037156-f7d7-33a8-8656-22f8d95e23d5 | -16.53319 | -55.92691 | 2024-10-09 05:06:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.3 |
| 59d70c87-61bc-34c0-9a8c-f029611058a6 | -16.59468 | -55.58035 | 2024-10-09 05:06:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.5 |
| b21b75e1-b3e0-3020-8621-6bf46174aa77 | -16.59177 | -55.57579 | 2024-10-09 05:06:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 3.0 |
| c7ff23d8-b63b-3391-89b5-7b8ed8a09c3a | -15.97622 | -55.61941 | 2024-10-09 05:06:00 | NOAA-20 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| a7609415-cb84-338c-92b6-31ffffed16d1 | -16.92075 | -55.80326 | 2024-10-09 05:06:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 5.9 |
| 904d09c7-1072-3c82-8517-f19d79e33655 | -16.92018 | -55.80724 | 2024-10-09 05:06:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.8 |
| f906ebd6-587e-3fbe-bd6e-dceae19fe6ce | -16.91961 | -55.81121 | 2024-10-09 05:06:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.8 |
| 2860328e-5edb-324a-8c9b-fe74dd406ce3 | -16.91728 | -55.80272 | 2024-10-09 05:06:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 5.9 |
| 4f404bdb-6d26-3fee-8974-dc3aa7d75748 | -16.91671 | -55.80669 | 2024-10-09 05:06:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.8 |
| 28105326-e073-3513-8d7a-ea0785fc3802 | -16.91614 | -55.81067 | 2024-10-09 05:06:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.8 |
| 317aad5b-9895-3b9d-8522-c6209cee6288 | -16.91557 | -55.81464 | 2024-10-09 05:06:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 11.3 |
| eace0e90-e7a4-3189-9719-1789e22c8205 | -16.915 | -55.81861 | 2024-10-09 05:06:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 11.3 |
| 03548c67-6253-3828-814b-b7e7798ac21e | -16.9138 | -55.80218 | 2024-10-09 05:06:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 16.2 |
| 645a0421-4fcc-332e-9a8f-31c794f84e64 | -16.91323 | -55.80616 | 2024-10-09 05:06:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 3.5 |
| df7a545c-807e-31ce-b20f-6eb1619b2148 | -16.91266 | -55.81013 | 2024-10-09 05:06:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 3.5 |
| 57f86da7-cf4e-321c-bcd5-e7cddeb89f7f | -16.91209 | -55.81409 | 2024-10-09 05:06:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 4.4 |
| 587279ea-ebb4-3c7b-8cc4-db7f5e90f6c7 | -16.91189 | -55.80256 | 2024-10-09 05:06:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 12.1 |
| a56919a6-2fc2-3ba6-a649-3fa563382db3 | -16.91153 | -55.81806 | 2024-10-09 05:06:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 4.4 |
| 6b527d86-d3bc-386a-8223-f311416899a8 | -16.91131 | -55.80653 | 2024-10-09 05:06:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 3.3 |
| 8e227e13-e2bb-36e3-9125-dee6fa6e1784 | -16.91072 | -55.81049 | 2024-10-09 05:06:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 3.3 |
| b3ced2a4-3680-3187-8e48-cebcc5ef0624 | -16.91033 | -55.80164 | 2024-10-09 05:06:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 16.2 |
| 699e9086-7bfb-3bd2-b904-fc676e1f56ec | -16.91014 | -55.81445 | 2024-10-09 05:06:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.2 |
| 360c1e14-2559-3ba3-9d82-0f08c69ce8e3 | -16.90976 | -55.80561 | 2024-10-09 05:06:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 3.5 |
| ec91009b-8b60-3db5-adc5-95bb56fb65b8 | -16.90955 | -55.81842 | 2024-10-09 05:06:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.2 |
| 0d3a5d63-ff99-37b2-9b07-cd85e982bd10 | -16.90919 | -55.80958 | 2024-10-09 05:06:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 3.5 |
| bfc72587-5896-3600-9d9f-f8104cda092d | -16.90862 | -55.81355 | 2024-10-09 05:06:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 4.4 |
| b4800266-1fb6-3ce6-8eae-b52b5cca325d | -16.90842 | -55.80201 | 2024-10-09 05:06:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 12.1 |
| bc59c992-bdf2-3e7a-ad97-40da1fc8a429 | -16.90784 | -55.80598 | 2024-10-09 05:06:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 3.3 |
| 80aea006-99be-3987-ba71-8ef0be1a35c9 | -16.90725 | -55.80995 | 2024-10-09 05:06:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 3.3 |
| 11ae60f0-9fd4-3e96-9538-d7fb43c0b8f7 | -16.90667 | -55.81391 | 2024-10-09 05:06:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.2 |
| 8965456f-7b7e-3469-9b6a-df112333a552 | -16.90495 | -55.80147 | 2024-10-09 05:06:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 10.0 |
| 3eafd34d-e95f-3c19-9dc6-b57dcfbb3586 | -16.90436 | -55.80544 | 2024-10-09 05:06:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 3.7 |
| e608f46a-90ba-3b40-8d1b-aa40e9a42f6c | -16.90378 | -55.8094 | 2024-10-09 05:06:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 3.7 |
| 8791c4bb-dfed-3ae8-8ef9-83307a50001b | -16.9032 | -55.81337 | 2024-10-09 05:06:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.4 |
| d8b470d1-f3c2-3e88-9cc5-a61e6db5f689 | -16.90148 | -55.80093 | 2024-10-09 05:06:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 10.0 |
| d0470caf-7514-325d-87a4-d49f0d8169a6 | -16.90089 | -55.8049 | 2024-10-09 05:06:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 3.7 |
| 76c9dfab-206b-3f5d-8c74-f98e1619c906 | -16.90031 | -55.80886 | 2024-10-09 05:06:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 3.7 |
| 18bd1f89-54c8-3402-a3d6-62cb15ab1196 | -16.89972 | -55.81282 | 2024-10-09 05:06:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.4 |
| 0ecadee8-8907-36bc-9cae-6e345203cfb4 | -16.898 | -55.80038 | 2024-10-09 05:06:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 6.3 |
| a63bc9d3-dc60-37ba-ab0b-be54435529c5 | -16.89742 | -55.80435 | 2024-10-09 05:06:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 3.4 |
| 9258bfe9-082a-3b04-92f1-624d68540194 | -16.89684 | -55.80832 | 2024-10-09 05:06:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 3.4 |
| 5eb82fa5-8ec0-33e0-b781-d43255314fc3 | -16.89625 | -55.81229 | 2024-10-09 05:06:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.9 |
| 5f1d7a37-b304-3ef3-804d-c41a750295d0 | -16.89453 | -55.79984 | 2024-10-09 05:06:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 6.3 |
| ac5bb154-55b9-3aa4-97d3-c192acbfa8a3 | -16.89395 | -55.80381 | 2024-10-09 05:06:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 3.4 |
| 70f51ced-af2f-3a67-92b8-9232d049dff2 | -16.89337 | -55.80777 | 2024-10-09 05:06:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 3.4 |
| d7a3f8e7-7c15-3ca8-9ce8-6b018c480193 | -16.89278 | -55.81174 | 2024-10-09 05:06:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.9 |
| 05093e3b-9e38-39ae-9cdf-86501c175603 | -16.8899 | -55.80723 | 2024-10-09 05:06:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.8 |
| eed98f2a-a60c-3846-9f76-95855d243d9a | -16.88931 | -55.8112 | 2024-10-09 05:06:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.4 |
| 555488e7-065b-3081-b65d-a401dabdd8a3 | -16.88873 | -55.81517 | 2024-10-09 05:06:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.4 |
| b80b448f-09c7-39d2-9d92-b17a9e678b6c | -16.88701 | -55.80271 | 2024-10-09 05:06:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.8 |
| 4b7dbb3b-86e0-3f20-91f2-4ad59039eda8 | -16.88585 | -55.81066 | 2024-10-09 05:06:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.4 |
| 5e976ec5-8b23-3729-b383-29a1498f44ba | -16.88526 | -55.81462 | 2024-10-09 05:06:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.4 |
| ac152727-a024-3b4e-94f9-cfb4241b2e19 | -16.88295 | -55.80614 | 2024-10-09 05:06:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.1 |
| 09d43315-5238-32cd-8393-a38249c1fa28 | -16.88179 | -55.81408 | 2024-10-09 05:06:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.8 |
| 0bf374b5-e62d-35df-8e5b-83b7496ff958 | -16.88006 | -55.80162 | 2024-10-09 05:06:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.1 |
| 4ae1ab81-1c9b-3f54-a8ad-7cd0b266bdfc | -16.9824 | -56.62132 | 2024-10-09 05:06:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.1 |
| f538dbba-a5b4-3112-a2ce-7ec1952da0b0 | -16.97113 | -56.6272 | 2024-10-09 05:06:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.0 |
| 401bdfd1-22c9-3b86-a58e-610b9d7b45d8 | -16.71246 | -55.94164 | 2024-10-09 05:06:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.4 |
| 863ae749-f7ab-3ce5-8352-28f74b1f1914 | -16.71075 | -55.95337 | 2024-10-09 05:06:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.7 |
| 040bc597-9932-31de-a54e-e8ad56d595ca | -16.70901 | -55.9411 | 2024-10-09 05:06:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.4 |
| e70a5e2e-4507-356e-8091-9b27cf68454a | -16.70895 | -55.89296 | 2024-10-09 05:06:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.7 |
| f5a771bc-44c8-3db3-ba23-574bf707f36f | -16.70673 | -55.95674 | 2024-10-09 05:06:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.7 |
| 6495a7e7-3e67-3044-b76d-b07172d1b8f4 | -16.7067 | -55.93273 | 2024-10-09 05:06:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.9 |
| 458d264a-adee-3f4b-aead-553c08e4e161 | -16.70613 | -55.93664 | 2024-10-09 05:06:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.9 |
| 61db2abe-c35c-31aa-b77e-c728e8c18a8d | -16.7061 | -55.91258 | 2024-10-09 05:06:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.8 |
| d1bd58dc-ff48-3c56-bb4e-7306bb5e9f7e | -16.70382 | -55.92826 | 2024-10-09 05:06:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.9 |
| fdb1d473-28ee-344c-b594-8fa4f3d44004 | -16.70329 | -55.9562 | 2024-10-09 05:06:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.0 |
| 89b3604c-0e0c-3b3c-8e8f-32bd64d08bb4 | -16.70325 | -55.93218 | 2024-10-09 05:06:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.9 |
| 4fb567f2-abde-3810-9e75-aa7dcc423505 | -16.70322 | -55.90812 | 2024-10-09 05:06:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.3 |
| 3889f8d2-64ed-343c-8ecc-8828290dda70 | -16.70272 | -55.96011 | 2024-10-09 05:06:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.2 |
| 0f3e2d58-c179-32b7-88b5-8778e107a432 | -16.70215 | -55.96402 | 2024-10-09 05:06:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.2 |
| 3f4f7de0-7da6-358e-aac6-8b19064c502e | -16.70037 | -55.92772 | 2024-10-09 05:06:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.1 |
| 4d85ca2b-e7e3-3f3f-9c26-a8be141c107c | -16.69984 | -55.95565 | 2024-10-09 05:06:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.0 |
| e20f4502-243d-3634-beb4-69a6659a9ec0 | -16.6998 | -55.93164 | 2024-10-09 05:06:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.1 |
| be3b3d5d-c9c5-38b7-b873-ec3c6f810362 | -16.69923 | -55.93556 | 2024-10-09 05:06:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.1 |
| 5f559352-2cfe-31bc-868d-ba7f67048c2e | -16.69526 | -55.96292 | 2024-10-09 05:06:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.8 |
| 4fec4e3c-aac5-310b-929e-c7b3fb4b8530 | -16.69124 | -55.96628 | 2024-10-09 05:06:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |
| 1571beb6-a258-398c-9acb-63f12fc2a458 | -16.6878 | -55.96573 | 2024-10-09 05:06:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.1 |
| 873ce720-56a4-3c7b-886a-a8ca3deeed92 | -16.66331 | -55.89843 | 2024-10-09 05:06:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.5 |
| aaa0ae11-2911-3821-bcea-20a1dd696336 | -16.65582 | -55.90127 | 2024-10-09 05:06:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.1 |


[Clique aqui para ver as próximas entradas](README194.md)
