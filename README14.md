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

## Dados Diários - Página 14

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 17d9f800-c9c6-38bd-aba1-1b1f4a7000d8 | -16.751699 | -55.7967 | 2024-10-01 00:50:47 | METOP-B | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 417fdb97-8452-3997-8e54-d088c29e607b | -16.618999 | -55.171398 | 2024-10-01 00:50:47 | METOP-B | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| bfa2705f-dd41-36cc-b7bc-82a554bb7cd8 | -16.621 | -55.181599 | 2024-10-01 00:50:47 | METOP-B | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 3a2f8f2b-d3ab-3170-9dde-cfc027ea7b1e | -16.622999 | -55.191799 | 2024-10-01 00:50:47 | METOP-B | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| b65c9543-5cf6-31a0-a2a7-df9f094e6a68 | -16.7377 | -55.776501 | 2024-10-01 00:50:47 | METOP-B | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 570bf6fa-092b-3560-8207-34640de4cdfe | -16.739799 | -55.787601 | 2024-10-01 00:50:47 | METOP-B | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| e1a162b2-529e-35d8-8ad0-414d6bbfd3d7 | -16.742001 | -55.798698 | 2024-10-01 00:50:47 | METOP-B | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 55764787-5fd3-340c-a04a-cd1a463527e9 | -16.728901 | -55.836201 | 2024-10-01 00:50:48 | METOP-B | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| f7757767-ede3-3b1c-a270-863c5134a63b | -16.7311 | -55.847401 | 2024-10-01 00:50:48 | METOP-B | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 59cc116b-6331-31e6-9903-02a0192f034b | -16.733299 | -55.858601 | 2024-10-01 00:50:48 | METOP-B | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| d7a2bff1-c7ea-396f-acf0-3bee5d9f508b | -16.6584 | -55.944401 | 2024-10-01 00:50:49 | METOP-B | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 81231083-0722-39cb-87f5-b62aabee2f97 | -16.660601 | -55.9557 | 2024-10-01 00:50:49 | METOP-B | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| fd06e001-22b4-3bdb-8fa2-5d48136edc47 | -16.6486 | -55.9464 | 2024-10-01 00:50:49 | METOP-B | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| bec62009-0bba-389d-a284-09588dd71a8c | -16.650801 | -55.957699 | 2024-10-01 00:50:49 | METOP-B | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 721ea798-7fa5-3f31-b55b-84b50113bd3f | -16.632299 | -55.914501 | 2024-10-01 00:50:50 | METOP-B | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| eaa1ece5-a1aa-319d-891f-1ef7b6e8d0a4 | -16.634501 | -55.9258 | 2024-10-01 00:50:50 | METOP-B | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 2a2d0a64-2d62-3a80-afb4-a256818f37bc | -16.6367 | -55.937099 | 2024-10-01 00:50:50 | METOP-B | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 843df586-227f-37bb-8e23-f7c6b148777a | -16.638901 | -55.948399 | 2024-10-01 00:50:50 | METOP-B | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 18e7db49-50db-375b-b095-f9d046a3cd21 | -16.622601 | -55.9165 | 2024-10-01 00:50:50 | METOP-B | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 042dd418-cb0f-3054-aeab-067259768cbb | -16.624701 | -55.927799 | 2024-10-01 00:50:50 | METOP-B | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 4f82e1e1-b262-3f06-84d8-b91b05f2fd87 | -16.6269 | -55.939098 | 2024-10-01 00:50:50 | METOP-B | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 5be5bae6-3f8b-3e23-b8f5-2fab98e8ce4c | -16.629101 | -55.950401 | 2024-10-01 00:50:50 | METOP-B | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 8c916135-8911-3ef9-98f8-4b98586fadda | -16.6106 | -55.907299 | 2024-10-01 00:50:50 | METOP-B | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 45748c43-4f0b-31a1-bbb4-03822c8e20b3 | -16.612801 | -55.918499 | 2024-10-01 00:50:50 | METOP-B | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 9bf65a6b-b529-3b89-8fe8-2573ac10244b | -16.614901 | -55.929798 | 2024-10-01 00:50:50 | METOP-B | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 3f45c344-a1a8-342b-91d2-c26b3d7ba307 | -16.6171 | -55.941101 | 2024-10-01 00:50:50 | METOP-B | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 52984cdf-511c-3992-8455-8b4b60fbd468 | -16.619301 | -55.9524 | 2024-10-01 00:50:50 | METOP-B | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 064f3032-d5fd-3d5d-9e47-ab3d2150ad0e | -16.6215 | -55.963799 | 2024-10-01 00:50:50 | METOP-B | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| e6528b2d-0abd-3989-9f1d-29bede1e7717 | -16.6008 | -55.909302 | 2024-10-01 00:50:50 | METOP-B | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 5e43a07e-ed56-3542-b35e-119e0da773d2 | -16.603001 | -55.920502 | 2024-10-01 00:50:50 | METOP-B | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| a91bc7c8-9fbe-3048-b0dd-de0c1297f9cc | -16.605101 | -55.931801 | 2024-10-01 00:50:50 | METOP-B | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 402ec0c5-dcf7-3f01-afc1-9e17e20b6a55 | -16.6073 | -55.9431 | 2024-10-01 00:50:50 | METOP-B | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 2630c64c-ef73-3611-9061-1c475df9e8bb | -16.609501 | -55.954399 | 2024-10-01 00:50:50 | METOP-B | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| d490e4ac-40e4-3e64-9833-b3d6f09e1c59 | -16.6117 | -55.965801 | 2024-10-01 00:50:50 | METOP-B | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| ad8f9155-084b-3f90-9100-1a67db9f7937 | -16.613899 | -55.9771 | 2024-10-01 00:50:50 | METOP-B | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| e8d63c11-3151-325c-97ca-d6b19a01b9ae | -16.5933 | -55.922501 | 2024-10-01 00:50:50 | METOP-B | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| c7a44b1a-40e9-37d7-b9f4-0f8b8120e468 | -16.5954 | -55.9338 | 2024-10-01 00:50:50 | METOP-B | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| ea53fa34-ca5b-39f9-a39b-945044b40f0b | -16.5998 | -55.956402 | 2024-10-01 00:50:50 | METOP-B | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| ca70b368-6ace-3c0c-a417-49c9fa528e73 | -16.601999 | -55.9678 | 2024-10-01 00:50:50 | METOP-B | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| d688bcde-4c25-3e3c-85cb-c690a584fad6 | -16.6042 | -55.979099 | 2024-10-01 00:50:50 | METOP-B | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| a13dda3b-1e53-3034-874f-3048c8dc88bb | -16.5835 | -55.9245 | 2024-10-01 00:50:50 | METOP-B | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| a78b6351-8831-34df-b53a-4029c68c6da6 | -16.5856 | -55.935799 | 2024-10-01 00:50:50 | METOP-B | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 01878e9d-9794-3898-9822-b64c721099dc | -16.090599 | -53.5187 | 2024-10-01 00:50:51 | METOP-B | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| f5c47e9b-6a1c-3311-92a8-1ff80af60741 | -16.0923 | -53.526901 | 2024-10-01 00:50:51 | METOP-B | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 34983716-f677-399c-8fb9-871a71029ba7 | -16.094 | -53.535198 | 2024-10-01 00:50:51 | METOP-B | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 38bf7699-4c52-3b1a-be3c-44ef080f195f | -16.0825 | -53.529099 | 2024-10-01 00:50:51 | METOP-B | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| c63b9e56-d19c-3ca9-b2a3-b5618fa55794 | -16.892401 | -57.659401 | 2024-10-01 00:50:51 | METOP-B | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| a7045670-f5d5-35c3-a250-a045b2bb5a07 | -16.895201 | -57.674099 | 2024-10-01 00:50:51 | METOP-B | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| a56fac35-741e-393a-ae5a-71f2bbca052d | -14.773 | -48.063 | 2024-10-01 00:50:52 | METOP-B | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 5df86191-9cd0-3089-9b07-853adfd7ce43 | -16.6686 | -57.218399 | 2024-10-01 00:50:53 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 33c17755-3327-3176-8e45-615a591d6aa9 | -16.671101 | -57.232101 | 2024-10-01 00:50:53 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 601e191d-6a07-3aa3-ba60-adc91955a385 | -16.6737 | -57.2458 | 2024-10-01 00:50:53 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 0510ebf0-4325-3b3d-b4d0-8624696aeef9 | -16.6763 | -57.259499 | 2024-10-01 00:50:53 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| afc2fa05-9fae-34a4-928f-068bb48ecb73 | -16.6789 | -57.2733 | 2024-10-01 00:50:53 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| b529b11b-b0af-3b61-8ff3-8cb3fbdd13ec | -16.6562 | -57.206699 | 2024-10-01 00:50:53 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 9264388f-e229-3ea6-bcb7-205028bf9cc7 | -16.6588 | -57.220299 | 2024-10-01 00:50:53 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| b910d813-58e4-379f-961a-97ffa7a21bc8 | -16.6614 | -57.234001 | 2024-10-01 00:50:53 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 02e28d82-4ef0-3517-98ce-24689e40cd46 | -16.6639 | -57.2477 | 2024-10-01 00:50:53 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 59177eeb-ba88-31d6-b7f3-e6a71329a839 | -16.6665 | -57.261398 | 2024-10-01 00:50:53 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| e77917af-f94b-3e84-aec0-45176d642285 | -16.6691 | -57.2752 | 2024-10-01 00:50:53 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| ac8ad3ae-d3cb-3046-b56e-672c7e46503d | -16.6717 | -57.289001 | 2024-10-01 00:50:53 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 1a87762c-97ce-3cf7-a746-5babf8bef67d | -16.6464 | -57.208599 | 2024-10-01 00:50:53 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| eccce66e-edb7-39a4-bafe-7d04316391cc | -16.649 | -57.222198 | 2024-10-01 00:50:53 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 6f0c4d10-deb7-3178-8dd8-8e7d011abddf | -16.6516 | -57.235901 | 2024-10-01 00:50:53 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 54f410b3-e9da-386b-91e1-be9b19687f86 | -16.6541 | -57.249599 | 2024-10-01 00:50:53 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 236080fd-52f2-3e1c-8bf3-dfa4a2aff0c4 | -16.6567 | -57.263302 | 2024-10-01 00:50:53 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 91d24071-098a-3071-b471-877b29f55032 | -16.6593 | -57.2771 | 2024-10-01 00:50:53 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| fb4ed93b-fd52-3b09-b738-d2fb295780cf | -16.6619 | -57.290901 | 2024-10-01 00:50:53 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| e334a284-9936-3530-8c18-2c2a43ddb4d3 | -14.7573 | -48.3493 | 2024-10-01 00:50:54 | METOP-B | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 0966ad1e-0353-31de-9b1d-4ee24a21e804 | -16.6367 | -57.210602 | 2024-10-01 00:50:54 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| d39c2ffb-1e84-37c5-becd-5df71a24e6db | -16.639299 | -57.224201 | 2024-10-01 00:50:54 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 4dd91246-637a-3553-a0cb-7492050e9ed3 | -16.641899 | -57.2379 | 2024-10-01 00:50:54 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| e8e445c5-513b-3b5c-984a-1ade1d3062df | -16.6444 | -57.251598 | 2024-10-01 00:50:54 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| d0600193-55fe-30e3-a51b-f290e7f0435c | -16.646999 | -57.265301 | 2024-10-01 00:50:54 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| a5e3e8c4-1561-31b9-a061-a29550162bfc | -16.649599 | -57.279099 | 2024-10-01 00:50:54 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| c3b0903c-f901-3742-8ed8-f8bf390e505b | -16.652201 | -57.2929 | 2024-10-01 00:50:54 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| fad5febb-e385-3d14-b156-e3dd212ddce9 | -16.6548 | -57.306702 | 2024-10-01 00:50:54 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 8380a8f3-9cf2-3f67-88e9-d59c7486e802 | -16.6269 | -57.212502 | 2024-10-01 00:50:54 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 84261c6e-cb46-3fed-ad17-a73361fd4dbc | -16.629499 | -57.226101 | 2024-10-01 00:50:54 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| a896b7c1-ed2b-39c9-8146-640a53983031 | -16.632099 | -57.239799 | 2024-10-01 00:50:54 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 8fcf8c14-8b9d-3ae6-82ef-1894b69e25ca | -16.6346 | -57.253502 | 2024-10-01 00:50:54 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 38d6524e-55de-36e2-a78c-2e3532e4b4e5 | -16.637199 | -57.2672 | 2024-10-01 00:50:54 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| bff6fab3-a31e-3c51-ad41-0099055e4118 | -16.639799 | -57.280998 | 2024-10-01 00:50:54 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 6a76cb24-b68e-3cf2-9766-e606ccad7a97 | -16.642401 | -57.2948 | 2024-10-01 00:50:54 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 4756426d-90fb-308a-b1e8-845605ae8338 | -16.645 | -57.308601 | 2024-10-01 00:50:54 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 9e43103a-aeec-3381-bd6e-4b35a886be38 | -16.619801 | -57.2281 | 2024-10-01 00:50:54 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| c9140f6b-acc8-3460-88ef-a44017d4f1da | -16.6224 | -57.241798 | 2024-10-01 00:50:54 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 3532a80d-c27a-3baf-9956-f8af68969436 | -16.624901 | -57.255501 | 2024-10-01 00:50:54 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| f25555f5-d8ad-3b16-9cd3-064a505faefb | -16.627501 | -57.269199 | 2024-10-01 00:50:54 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| a70269c5-dc28-3064-b8f5-40cda0e37123 | -16.6301 | -57.283001 | 2024-10-01 00:50:54 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 1a7379ea-af56-33af-b5cb-f29d50deb9a8 | -16.6327 | -57.296799 | 2024-10-01 00:50:54 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 9319c230-fcdb-35eb-ae5e-dee7b109ac78 | -16.6353 | -57.3106 | 2024-10-01 00:50:54 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 11921043-a26d-3060-bbfe-98f78e0fd942 | -16.610001 | -57.23 | 2024-10-01 00:50:54 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 8ddd442f-e9a2-3730-b28f-24b2311e35e7 | -16.6126 | -57.243698 | 2024-10-01 00:50:54 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 97c4e0a8-44a7-3701-94bd-9a0705d2e4d2 | -16.615101 | -57.257401 | 2024-10-01 00:50:54 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| b390b52c-35c1-33de-8da9-8cae9db30ba3 | -16.617701 | -57.271099 | 2024-10-01 00:50:54 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| bb491df5-7dba-3084-8634-ef61cc80da7f | -16.6203 | -57.284901 | 2024-10-01 00:50:54 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 12077c90-88a8-3e1d-9734-1d740f989073 | -16.6229 | -57.298698 | 2024-10-01 00:50:54 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 1d6869df-a867-3d94-a42e-bf7ad0485e2b | -16.6028 | -57.245701 | 2024-10-01 00:50:54 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 273ff837-3d2d-3a85-92c6-d71b6250d0f7 | -16.605301 | -57.259399 | 2024-10-01 00:50:54 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |


[Clique aqui para ver as próximas entradas](README15.md)
