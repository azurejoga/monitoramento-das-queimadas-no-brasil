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

## Dados Diários - Página 26

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 71341685-0cb2-3aeb-9afc-100eeda5fefd | -17.060101 | -56.734901 | 2024-10-01 01:44:40 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| dad52d1b-40d8-35e6-80ea-e4fb5756a9f4 | -17.062401 | -56.744301 | 2024-10-01 01:44:40 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 038bca96-ab23-37a5-81ae-3dd8a6d96f8f | -17.064699 | -56.753799 | 2024-10-01 01:44:40 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 1c4a3170-8dbb-3fd1-bdb0-544be25462e2 | -17.066999 | -56.763199 | 2024-10-01 01:44:40 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| f67d9629-03f0-37a9-a15e-cd6b381bd377 | -16.8426 | -55.8978 | 2024-10-01 01:44:40 | METOP-C | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| ed14de82-2f71-38aa-883d-72037b5fe425 | -16.8452 | -55.908401 | 2024-10-01 01:44:40 | METOP-C | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| eb4d7367-a157-3821-be9c-9a726783d81b | -16.847799 | -55.918999 | 2024-10-01 01:44:40 | METOP-C | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| d3b48e9b-ffa6-3aa5-b6bf-3f96c0631529 | -16.8505 | -55.929501 | 2024-10-01 01:44:40 | METOP-C | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 06407b1f-0f20-354c-8218-02bfccfd174e | -16.8531 | -55.940102 | 2024-10-01 01:44:40 | METOP-C | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| e065acaf-ff98-3c93-beeb-1b41f887dc33 | -17.0434 | -56.709 | 2024-10-01 01:44:40 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 8a1d7205-8ebf-3a0a-9475-9044f4ec11a7 | -17.0457 | -56.718399 | 2024-10-01 01:44:40 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| b2d3fe7d-adae-3ab1-bb60-d0a9e123e897 | -17.048 | -56.727901 | 2024-10-01 01:44:40 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 2103b436-7615-30aa-ae4c-1c0ea837f2e7 | -17.050301 | -56.7374 | 2024-10-01 01:44:40 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 8298c363-228a-320c-83b2-e89011d15cbb | -17.0527 | -56.746799 | 2024-10-01 01:44:40 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 5dfcdaea-a499-3e53-bc40-f882e785f1fd | -17.055 | -56.756302 | 2024-10-01 01:44:40 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 03e4feaf-91af-3821-b4bb-5dec3480b45f | -17.057301 | -56.765701 | 2024-10-01 01:44:40 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 4c8749ba-ead7-37da-938f-0b17397be8a6 | -16.832899 | -55.900398 | 2024-10-01 01:44:40 | METOP-C | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| a1c4ddf6-59f1-3d6e-8684-af5c17f3a721 | -16.835501 | -55.910999 | 2024-10-01 01:44:40 | METOP-C | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 4f4d7167-5bdd-3f32-ba18-ae8b006e6f4c | -16.8381 | -55.9216 | 2024-10-01 01:44:40 | METOP-C | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| aaacaaf4-e117-3608-9791-a07fd0fc7a6e | -17.0383 | -56.730499 | 2024-10-01 01:44:40 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| b2f37d46-5069-3850-ae85-45ca5523ac46 | -17.0406 | -56.740002 | 2024-10-01 01:44:40 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| c5f8d54d-001d-3a79-90e6-73ad1dcb3eee | -17.0429 | -56.749401 | 2024-10-01 01:44:40 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 31828e96-4d74-33e3-b4df-f24c0da99cac | -16.643499 | -55.190102 | 2024-10-01 01:44:40 | METOP-C | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 16b725bc-a970-3c3f-b008-6dc93be7e91a | -16.6465 | -55.201801 | 2024-10-01 01:44:40 | METOP-C | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 83659091-3277-3918-b877-9b9e06ed2f4a | -16.825701 | -55.913601 | 2024-10-01 01:44:40 | METOP-C | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| ffb6f79c-580d-3349-a37d-99ae8e969953 | -16.8283 | -55.924198 | 2024-10-01 01:44:40 | METOP-C | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 1c0c23f7-b478-39d1-ae3d-abe26ff22559 | -16.6308 | -55.180901 | 2024-10-01 01:44:40 | METOP-C | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 643bac0b-93dd-3725-b1f3-ef6b59473815 | -16.633801 | -55.192699 | 2024-10-01 01:44:40 | METOP-C | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 3fc5d8a5-0d95-3bc5-afa8-1eaebdb2b492 | -16.636801 | -55.204399 | 2024-10-01 01:44:40 | METOP-C | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| eced0193-ed08-3573-96ed-1aa6a82b5911 | -16.639799 | -55.216099 | 2024-10-01 01:44:40 | METOP-C | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| a49598d2-f992-34a0-8a96-b8639254d5a0 | -16.805401 | -55.873798 | 2024-10-01 01:44:40 | METOP-C | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| ed2e9396-5e8e-346e-ba38-b41e12320c1d | -16.8081 | -55.884399 | 2024-10-01 01:44:40 | METOP-C | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| acd776d5-49b6-3868-8549-45f5ef1ea30c | -16.8186 | -55.9268 | 2024-10-01 01:44:40 | METOP-C | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 69e48b8e-418b-3465-8aa5-1367ebb0f212 | -16.821301 | -55.937302 | 2024-10-01 01:44:40 | METOP-C | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| c975480e-c72c-3eba-a690-efd499594300 | -16.8239 | -55.9478 | 2024-10-01 01:44:40 | METOP-C | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| c98bf711-0fb0-3856-80e8-e9fbaa3a69f4 | -16.8265 | -55.958401 | 2024-10-01 01:44:40 | METOP-C | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 219cbadb-25a1-32e0-928f-167cbb561699 | -16.621099 | -55.183601 | 2024-10-01 01:44:41 | METOP-C | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| ac0f3a9e-74df-397e-9bf6-1e2cc6f0d86a | -16.6241 | -55.195301 | 2024-10-01 01:44:41 | METOP-C | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| fb4b9595-3665-35a3-9c8c-8a0bcdf50a02 | -16.6271 | -55.207001 | 2024-10-01 01:44:41 | METOP-C | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 3cc0d081-c254-3270-8a58-9e73b15a3f77 | -16.7743 | -55.790798 | 2024-10-01 01:44:41 | METOP-C | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| d6c94e5c-aec5-3456-b834-6b650193499b | -16.808901 | -55.929401 | 2024-10-01 01:44:41 | METOP-C | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| e09665b5-b0dc-3ecd-8032-ad9ef4f65e5e | -16.8116 | -55.939899 | 2024-10-01 01:44:41 | METOP-C | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| b2a5191f-7be6-3a7b-a15e-246048abd0c4 | -16.7619 | -55.7826 | 2024-10-01 01:44:41 | METOP-C | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 4b73bdd9-09ac-3566-9983-04383dff003c | -16.764601 | -55.7934 | 2024-10-01 01:44:41 | METOP-C | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 00c5c424-dead-3736-af35-cfbb51297827 | -16.7673 | -55.8041 | 2024-10-01 01:44:41 | METOP-C | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 94049b4a-daa8-375c-b519-9472aca3b91e | -16.77 | -55.814899 | 2024-10-01 01:44:41 | METOP-C | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 3a9d8788-dee1-36c9-8178-c2160070d2bb | -16.7495 | -55.774399 | 2024-10-01 01:44:41 | METOP-C | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 82225081-3654-3752-9ff1-6064c69ff11b | -16.752199 | -55.785198 | 2024-10-01 01:44:41 | METOP-C | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 672710a4-2d83-3774-b68d-c3dcbb14d261 | -16.7549 | -55.796001 | 2024-10-01 01:44:41 | METOP-C | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 77382ff0-c757-352f-a411-8c4411820b01 | -16.757601 | -55.806702 | 2024-10-01 01:44:41 | METOP-C | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| ec906be2-b204-3c70-a741-e903c9da3b6b | -16.760201 | -55.817501 | 2024-10-01 01:44:41 | METOP-C | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 9da7607c-ebff-32ee-b102-61232c122817 | -16.739799 | -55.777 | 2024-10-01 01:44:41 | METOP-C | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 4cce0a07-e536-3a0e-95c0-46cb9b162693 | -16.7425 | -55.7878 | 2024-10-01 01:44:41 | METOP-C | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 0a0468b8-11d2-3f26-91ad-86196e8d1b25 | -16.745199 | -55.798599 | 2024-10-01 01:44:41 | METOP-C | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 93aa6d78-07e3-3bde-b602-4e39bdd775ad | -16.7479 | -55.809299 | 2024-10-01 01:44:41 | METOP-C | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| ccee32d8-8e07-380b-a568-fda71b54cc57 | -16.7505 | -55.820099 | 2024-10-01 01:44:41 | METOP-C | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| dfd33575-0d1f-3ba2-b38b-e1e8e2c45924 | -16.7355 | -55.801201 | 2024-10-01 01:44:41 | METOP-C | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| b1df6a61-9b4e-3d25-9800-85c38a8db471 | -16.738199 | -55.811901 | 2024-10-01 01:44:41 | METOP-C | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| df4a1b6d-9f77-3e4a-8627-b4e921e7f9af | -14.7576 | -48.771099 | 2024-10-01 01:44:43 | METOP-C | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 35ac829c-7b5e-3e5c-b6f2-26fd329ec832 | -14.7386 | -48.741001 | 2024-10-01 01:44:43 | METOP-C | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| fcedefaf-67fe-3721-aaff-4fc33285954d | -14.7481 | -48.773998 | 2024-10-01 01:44:43 | METOP-C | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 81398b2f-83e1-3aa9-af8d-d103fdcdc98c | -14.7291 | -48.7439 | 2024-10-01 01:44:43 | METOP-C | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 0ea56401-7296-3cb8-8ddc-698d29cf6d71 | -14.7196 | -48.746799 | 2024-10-01 01:44:43 | METOP-C | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| cb6ad0f5-c762-36d4-ba71-716b2100cd0d | -16.648199 | -55.949799 | 2024-10-01 01:44:43 | METOP-C | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| b9f8c0ff-9d25-34db-89eb-24fdbf53a61e | -16.650801 | -55.9603 | 2024-10-01 01:44:43 | METOP-C | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 39ad69a4-7ee8-36d7-a106-462dc9b85328 | -16.6534 | -55.970901 | 2024-10-01 01:44:43 | METOP-C | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 73ee0cce-8e8e-3620-b559-78795ea577cb | -16.656099 | -55.9814 | 2024-10-01 01:44:43 | METOP-C | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| fb98b0e2-9c68-3d91-82bc-6b46f8100151 | -16.635799 | -55.941799 | 2024-10-01 01:44:43 | METOP-C | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| bd3f0c67-9754-3e38-892e-da847104914f | -16.6385 | -55.9524 | 2024-10-01 01:44:43 | METOP-C | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 3e9dc3b0-e55d-3c08-879a-d873e42a5edc | -16.6411 | -55.962898 | 2024-10-01 01:44:43 | METOP-C | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 1002e914-d616-3d85-81ff-2f86c0f3714f | -16.6437 | -55.973499 | 2024-10-01 01:44:43 | METOP-C | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| aefbc074-56e7-3395-b822-5df50679b924 | -16.626101 | -55.944401 | 2024-10-01 01:44:44 | METOP-C | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 02c9422a-b743-3967-b054-230eb18c0312 | -16.628799 | -55.955002 | 2024-10-01 01:44:44 | METOP-C | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 6d1ebb23-de63-37ad-9cbf-aa8f84e49584 | -16.6138 | -55.936401 | 2024-10-01 01:44:44 | METOP-C | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 2f45d905-a4c6-336d-87af-06903209e1c0 | -16.6164 | -55.946999 | 2024-10-01 01:44:44 | METOP-C | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 26a2a562-6142-3dd6-9733-8c6dbf3aae12 | -16.6014 | -55.928299 | 2024-10-01 01:44:44 | METOP-C | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| c73ffefc-f179-30f0-9af2-cadee6f157fa | -16.604099 | -55.9389 | 2024-10-01 01:44:44 | METOP-C | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 193a1594-853d-34e4-a234-7040b90f2cc2 | -16.606701 | -55.949501 | 2024-10-01 01:44:44 | METOP-C | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 0729b165-fe52-3064-87b8-424057d36941 | -16.6094 | -55.960098 | 2024-10-01 01:44:44 | METOP-C | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 36b7f723-1a72-30e9-9d25-4ae4db129958 | -16.612 | -55.970699 | 2024-10-01 01:44:44 | METOP-C | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 62f58ded-7286-3d14-8f03-ed245ec8104a | -16.614599 | -55.981201 | 2024-10-01 01:44:44 | METOP-C | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 3282466d-070b-3e45-9544-6e447121d8b5 | -16.594299 | -55.941502 | 2024-10-01 01:44:44 | METOP-C | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| d25b9ed2-7d78-35fa-a203-9a218b8753a3 | -16.596901 | -55.952099 | 2024-10-01 01:44:44 | METOP-C | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 560e447f-238e-375e-aa9e-b816df748154 | -16.6022 | -55.973301 | 2024-10-01 01:44:44 | METOP-C | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| ce378682-24dd-3bf5-92dd-59ddbc0d775e | -16.604799 | -55.983799 | 2024-10-01 01:44:44 | METOP-C | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 1fab1d13-0f99-3c24-ac41-e9dbc506703f | -16.6075 | -55.9944 | 2024-10-01 01:44:44 | METOP-C | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 99570baa-7221-3380-8a6a-9c2772f10cf4 | -16.5846 | -55.944099 | 2024-10-01 01:44:44 | METOP-C | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 96154ace-3831-3f2d-bf29-01b91318d8dd | -16.867701 | -57.691101 | 2024-10-01 01:44:47 | METOP-C | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 536097a4-339d-36bb-9d67-046c3a727d0c | -16.869699 | -57.6996 | 2024-10-01 01:44:47 | METOP-C | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| a1fda9a3-ff6f-38c5-b326-73be8fe6adb0 | -16.820499 | -57.538601 | 2024-10-01 01:44:47 | METOP-C | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 7e2c793d-a7bd-3bb1-82ca-ed0749733470 | -16.758699 | -57.368198 | 2024-10-01 01:44:47 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 7d7fb85c-73c3-3e47-8345-5703725b6b2a | -16.803101 | -57.552299 | 2024-10-01 01:44:47 | METOP-C | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 7de54db0-d073-364a-99a3-7116f76b0a2d | -16.749001 | -57.370701 | 2024-10-01 01:44:47 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 3b8c0ec7-6037-3029-a2f4-58316ec91545 | -16.751101 | -57.379501 | 2024-10-01 01:44:47 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 2a6527f8-ccd5-3382-a7a9-014cc1ee8cd8 | -16.735001 | -57.355499 | 2024-10-01 01:44:47 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 39324df8-1ce9-3134-8773-c2bfba9f1d15 | -16.737101 | -57.364399 | 2024-10-01 01:44:47 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 654d147b-c15b-3d1f-ad15-25aedd6bd07c | -16.747801 | -57.4086 | 2024-10-01 01:44:47 | METOP-C | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 876f7d70-7d8a-3037-82ca-bcb656158d39 | -16.749901 | -57.4174 | 2024-10-01 01:44:47 | METOP-C | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| b9743167-c6a5-3d8a-8c29-45dc3a20d574 | -16.738001 | -57.411098 | 2024-10-01 01:44:48 | METOP-C | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| d112a756-2d6b-35b4-a305-c55798218d3a | -16.740101 | -57.419899 | 2024-10-01 01:44:48 | METOP-C | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |


[Clique aqui para ver as próximas entradas](README27.md)
