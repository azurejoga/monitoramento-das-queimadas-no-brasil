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

## Dados Diários - Página 158

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| c090d56a-087f-3fbf-94bc-f71f681ec5b1 | -16.8292 | -55.9152 | 2024-10-01 07:16:41 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 68.1 |
| 7602ec84-7e65-38b1-b6a3-a3f67e879a6d | -16.8488 | -55.9128 | 2024-10-01 07:16:41 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 80.5 |
| 8ebea99f-222f-3445-a8ce-ddd432accbac | -16.8684 | -55.9103 | 2024-10-01 07:16:41 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 56.8 |
| c34d991c-7cbd-3f1f-b9cc-4ce830bfe239 | -17.0705 | -56.7114 | 2024-10-01 07:16:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 56.3 |
| 5bcee582-ea89-39f1-958d-e8c3650656b4 | -17.0895 | -56.7503 | 2024-10-01 07:16:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 50.9 |
| b56b2dd5-ecd8-3cad-88ea-26386ebc0260 | -17.0898 | -56.7297 | 2024-10-01 07:16:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 74.0 |
| b4645666-3aaa-3536-8602-971bd1ae78b3 | -17.0902 | -56.709 | 2024-10-01 07:16:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 51.9 |
| 053f9ab1-57f2-3941-a1e6-82b67de1b960 | -17.1095 | -56.7273 | 2024-10-01 07:16:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 49.2 |
| 7a97f624-2d07-3929-8dac-ffa2aa8de0bd | -17.0702 | -56.7321 | 2024-10-01 07:16:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 52.6 |
| fa141498-cb36-3dea-a3ed-cd94e931c00e | -18.6973 | -57.333 | 2024-10-01 07:16:51 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 101.9 |
| bcd92853-d2c6-3359-a139-3c2b946f90ac | -18.6977 | -57.3123 | 2024-10-01 07:16:51 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 80.0 |
| ade37c77-be0d-3df6-b9f1-9389659b4cb0 | -18.7172 | -57.3305 | 2024-10-01 07:16:51 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 60.3 |
| f7126aec-1b8b-3b40-a603-6f297d2caebe | -21.5871 | -47.8591 | 2024-10-01 07:17:05 | GOES-16 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 79.4 |
| 43af5ddf-7d9f-33ce-86b2-7c8bf240984c | -21.6078 | -47.854 | 2024-10-01 07:17:05 | GOES-16 | SÃO CARLOS | SÃO PAULO | Brasil | 3548906 | 35 | 33 | nan | nan | nan | Cerrado | 101.6 |
| 77087a46-0d13-3262-adfb-51c59f1d0d17 | -22.37 | -49.3477 | 2024-10-01 07:17:09 | GOES-16 | DUARTINA | SÃO PAULO | Brasil | 3514502 | 35 | 33 | nan | nan | nan | Mata Atlântica | 63.9 |
| d63767a9-6ea5-36ce-977e-3ec9b229621b | -22.3707 | -49.3244 | 2024-10-01 07:17:09 | GOES-16 | DUARTINA | SÃO PAULO | Brasil | 3514502 | 35 | 33 | nan | nan | nan | Mata Atlântica | 180.0 |
| 76f808ad-5d0f-3ddc-a9f3-f01209554bc2 | -22.3713 | -49.3011 | 2024-10-01 07:17:09 | GOES-16 | PIRATININGA | SÃO PAULO | Brasil | 3539400 | 35 | 33 | nan | nan | nan | Mata Atlântica | 121.0 |
| 89a3ba6b-9cbc-301a-82b7-0de2c5956258 | -14.7402 | -48.7721 | 2024-10-01 07:26:29 | GOES-16 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 49.3 |
| cced7b4b-e5e7-349c-a0a7-6119528f6fff | -14.7596 | -48.769 | 2024-10-01 07:26:29 | GOES-16 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 47.3 |
| 505b2f4c-08b7-31ff-ad53-ceb95ca38a4b | -16.474 | -57.3553 | 2024-10-01 07:26:39 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 60.7 |
| 074cfd76-8ae2-3265-a4bd-6b2fc28b0bee | -16.7079 | -57.3696 | 2024-10-01 07:26:40 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 46.0 |
| 8a76cbce-24aa-324b-b030-8aae103a94cd | -16.6316 | -57.2557 | 2024-10-01 07:26:40 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 78.8 |
| 2cee9ecd-3e77-31e0-b90d-a2f852c5b291 | -16.6319 | -57.2352 | 2024-10-01 07:26:40 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 41.3 |
| 8244dbe8-5933-329e-8732-d3eb30fd2cee | -16.7724 | -55.798 | 2024-10-01 07:26:40 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 46.8 |
| bd091db5-a960-3043-ae41-981840376163 | -16.7728 | -55.7773 | 2024-10-01 07:26:40 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 47.7 |
| e6a13f77-cefb-31f4-863a-d9d7a2f70762 | -16.8292 | -55.9152 | 2024-10-01 07:26:41 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 63.3 |
| 6bce50ee-405c-3392-8572-4e38cacc498e | -16.8488 | -55.9128 | 2024-10-01 07:26:41 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 78.6 |
| 8acb6b36-56c8-3f2e-924e-6a0aba58e38e | -17.0898 | -56.7297 | 2024-10-01 07:26:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 69.7 |
| bc3d1f75-1d1a-3de7-87aa-2083bf86aee0 | -17.0902 | -56.709 | 2024-10-01 07:26:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 50.4 |
| e1b83e03-31d5-396e-bb7b-f778a55b0b4b | -17.0702 | -56.7321 | 2024-10-01 07:26:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 50.1 |
| 9c57e8b2-45ea-36f1-9ab8-0dd2b441e4bc | -17.0705 | -56.7114 | 2024-10-01 07:26:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 54.9 |
| 1b904ea3-5655-3f00-8416-230751de9dde | -18.6973 | -57.333 | 2024-10-01 07:26:51 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 101.6 |
| 1a54d096-3411-39b7-8224-80434c06f091 | -18.6977 | -57.3123 | 2024-10-01 07:26:51 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 68.8 |
| 18d5af97-2485-3197-8a50-7527648dbfc5 | -18.7172 | -57.3305 | 2024-10-01 07:26:51 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 64.6 |
| 87dd4a12-42f3-3516-886b-eb770a8c0248 | -21.5871 | -47.8591 | 2024-10-01 07:27:05 | GOES-16 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 76.9 |
| cbc7dfcc-d774-3417-943b-0690b6f3eca6 | -22.3498 | -49.3293 | 2024-10-01 07:27:09 | GOES-16 | DUARTINA | SÃO PAULO | Brasil | 3514502 | 35 | 33 | nan | nan | nan | Mata Atlântica | 57.0 |
| 38de886d-bc4b-33da-9bc8-af60da8a39d7 | -22.3707 | -49.3244 | 2024-10-01 07:27:09 | GOES-16 | DUARTINA | SÃO PAULO | Brasil | 3514502 | 35 | 33 | nan | nan | nan | Mata Atlântica | 146.0 |
| 6fcafba5-8cc6-3ba3-a2b3-ab91b87ed655 | -22.3713 | -49.3011 | 2024-10-01 07:27:09 | GOES-16 | PIRATININGA | SÃO PAULO | Brasil | 3539400 | 35 | 33 | nan | nan | nan | Mata Atlântica | 99.8 |
| 60e5da00-366d-38f7-907a-0ab1a9569d7c | -13.0396 | -51.186 | 2024-10-01 07:36:20 | GOES-16 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 65.4 |
| bb04538e-75ed-35c2-9eb9-27a5b035c044 | -13.0204 | -51.1884 | 2024-10-01 07:36:20 | GOES-16 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 61.8 |
| 27d98a1d-c7ad-32d5-8171-6a3b077c1deb | -14.7402 | -48.7721 | 2024-10-01 07:36:29 | GOES-16 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 51.4 |
| 58069027-1188-3b5b-9d2f-0db4f7f19ba2 | -14.8465 | -49.2863 | 2024-10-01 07:36:29 | GOES-16 | SÃO LUIZ DO NORTE | GOIÁS | Brasil | 5220157 | 52 | 33 | nan | nan | nan | Cerrado | 40.9 |
| 0a3ee8d6-93fb-363c-a429-dc79aff33716 | -16.474 | -57.3553 | 2024-10-01 07:36:39 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 60.4 |
| 03f6a98a-f449-3bd8-9631-3dbc628779e9 | -16.7728 | -55.7773 | 2024-10-01 07:36:40 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 46.5 |
| 8e86bee0-6ead-386e-a003-f3ca574f2ba8 | -16.7079 | -57.3696 | 2024-10-01 07:36:40 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 49.1 |
| eb1e85cb-357e-3455-b8c2-3d822a15ef3c | -16.6515 | -57.233 | 2024-10-01 07:36:40 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 95.9 |
| e29ee751-16e4-3631-8c59-137c08735665 | -16.6512 | -57.2535 | 2024-10-01 07:36:40 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 101.9 |
| 51252bc3-6af8-3bca-866b-74c48e84de14 | -16.6319 | -57.2352 | 2024-10-01 07:36:40 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 138.2 |
| c3f80784-ef54-379c-9d66-b0664039bafb | -16.6316 | -57.2557 | 2024-10-01 07:36:40 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 190.9 |
| 583425b5-a397-31b2-af6c-e71387c4e27a | -16.612 | -57.2579 | 2024-10-01 07:36:40 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 54.7 |
| a04a8181-51bb-31ec-bc66-aa4b33abad69 | -16.6117 | -57.2784 | 2024-10-01 07:36:40 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 49.4 |
| fbd1b09a-5cb6-3dbd-8731-10b79265ab60 | -16.8787 | -57.6971 | 2024-10-01 07:36:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 36.2 |
| 173cd097-d0ee-3704-bbaf-3a8d593eeaeb | -16.8684 | -55.9103 | 2024-10-01 07:36:41 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 46.4 |
| d61fe4c5-af3e-3442-99ed-b5459a8aca9e | -16.8488 | -55.9128 | 2024-10-01 07:36:41 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 68.3 |
| bf3bf4eb-383c-36ea-9d74-54e039a09df5 | -16.8292 | -55.9152 | 2024-10-01 07:36:41 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 67.2 |
| 8bb66ab6-f931-3b8d-9bf3-cf2e9692c032 | -17.0898 | -56.7297 | 2024-10-01 07:36:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 71.2 |
| cd5727e4-130e-3d5c-bec2-2064828680e3 | -17.0705 | -56.7114 | 2024-10-01 07:36:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 54.6 |
| 10c62a97-b646-3e37-ac0d-d7c43dad2bab | -17.0702 | -56.7321 | 2024-10-01 07:36:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 54.5 |
| 09b776b9-75a1-39bb-8d0d-99a73a6c7760 | -18.6977 | -57.3123 | 2024-10-01 07:36:51 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 63.9 |
| 3c5caa9c-8766-3ffa-bdf9-ce1bd2cb5729 | -18.6973 | -57.333 | 2024-10-01 07:36:51 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 97.6 |
| 17b46cf4-6547-329a-a6b8-605ed329a87a | -21.6078 | -47.854 | 2024-10-01 07:37:05 | GOES-16 | SÃO CARLOS | SÃO PAULO | Brasil | 3548906 | 35 | 33 | nan | nan | nan | Cerrado | 68.1 |
| d8af7c52-afc7-38df-bd1f-f803b1905648 | -21.5871 | -47.8591 | 2024-10-01 07:37:05 | GOES-16 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 59.4 |
| 54c12116-bd31-3d80-923c-9bc8b23bd7d4 | -22.3713 | -49.3011 | 2024-10-01 07:37:09 | GOES-16 | PIRATININGA | SÃO PAULO | Brasil | 3539400 | 35 | 33 | nan | nan | nan | Mata Atlântica | 107.7 |
| 3592e6d9-16cf-3f3a-9879-6ed04288ea22 | -22.3707 | -49.3244 | 2024-10-01 07:37:09 | GOES-16 | DUARTINA | SÃO PAULO | Brasil | 3514502 | 35 | 33 | nan | nan | nan | Mata Atlântica | 170.7 |
| 9208e106-ee87-375e-9eb3-963f342ee0b9 | -12.9995 | -51.2976 | 2024-10-01 07:46:19 | GOES-16 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 59.7 |
| 6fd9e2d6-435a-3e7c-b89e-92fceed9dfe3 | -13.0009 | -51.2122 | 2024-10-01 07:46:19 | GOES-16 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 102.0 |
| 192420af-cbaa-3a0b-b721-196ec3d89267 | -13.0012 | -51.1908 | 2024-10-01 07:46:19 | GOES-16 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 89.9 |
| c57d1e75-93bc-3187-a819-35703450b24e | -13.02 | -51.2098 | 2024-10-01 07:46:20 | GOES-16 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 88.9 |
| 4d31f434-5de1-37f2-a019-0be331727cb6 | -13.0204 | -51.1884 | 2024-10-01 07:46:20 | GOES-16 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 127.4 |
| 3dec673d-c861-395b-99b9-236186355222 | -14.7402 | -48.7721 | 2024-10-01 07:46:29 | GOES-16 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 49.4 |
| c145f5b2-f7fe-331c-a998-0f7fcc7b292a | -14.7596 | -48.769 | 2024-10-01 07:46:29 | GOES-16 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 49.1 |
| 2bfefa23-a0e0-3e03-bf1e-f89ddf337584 | -15.1934 | -49.4304 | 2024-10-01 07:46:31 | GOES-16 | SANTA ISABEL | GOIÁS | Brasil | 5219357 | 52 | 33 | nan | nan | nan | Cerrado | 41.1 |
| 72656bd6-0b07-32b9-9537-5b2557c578a5 | -16.6117 | -57.2784 | 2024-10-01 07:46:40 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 60.3 |
| a441e1ca-edfe-306e-ad61-984de027b062 | -16.6316 | -57.2557 | 2024-10-01 07:46:40 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 210.4 |
| ad7f3046-bd61-3985-be47-29d263e951cd | -16.6319 | -57.2352 | 2024-10-01 07:46:40 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 215.9 |
| ecc689f1-44ce-377b-9181-3872cc121904 | -16.6512 | -57.2535 | 2024-10-01 07:46:40 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 86.1 |
| 4697b165-2f62-3208-a152-6df2c337a92d | -16.6515 | -57.233 | 2024-10-01 07:46:40 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 117.0 |
| 2b9ef510-2619-399a-8602-baa347f92782 | -16.8491 | -55.892 | 2024-10-01 07:46:41 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 44.0 |
| d45edd4b-7999-3963-a45c-19c611d2f548 | -16.8983 | -57.6949 | 2024-10-01 07:46:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 36.0 |
| 05ccbfb6-082b-350c-b2e9-39c45f0306f2 | -16.8292 | -55.9152 | 2024-10-01 07:46:41 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 52.9 |
| 59b3f28e-fece-37ba-b8ab-71475dd1b345 | -16.8488 | -55.9128 | 2024-10-01 07:46:41 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 75.8 |
| 4309d339-bc3e-3851-af3c-0f38529c2780 | -17.0705 | -56.7114 | 2024-10-01 07:46:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 58.2 |
| aaf3d67e-2967-30ee-b03b-1e16dabcb284 | -17.0898 | -56.7297 | 2024-10-01 07:46:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 71.6 |
| cba62544-54a7-3ce9-9011-87d3af0e1ffb | -18.6973 | -57.333 | 2024-10-01 07:46:51 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 76.6 |
| 9d4f64f4-3c60-370a-8342-19cee4ecad43 | -18.6977 | -57.3123 | 2024-10-01 07:46:51 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 66.9 |
| e221bff3-e3fa-326c-ba6b-1db0b0441cc9 | -18.7172 | -57.3305 | 2024-10-01 07:46:51 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 57.1 |
| 9bd2ba89-21cb-36d3-8a0e-affff75c3054 | -21.5871 | -47.8591 | 2024-10-01 07:47:05 | GOES-16 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 69.3 |
| 4c92ea64-2049-322b-846d-311fb87acb71 | -21.6078 | -47.854 | 2024-10-01 07:47:05 | GOES-16 | SÃO CARLOS | SÃO PAULO | Brasil | 3548906 | 35 | 33 | nan | nan | nan | Cerrado | 57.8 |
| e1d19c24-ea30-3d79-8c7f-837255e68ed4 | -22.3498 | -49.3293 | 2024-10-01 07:47:09 | GOES-16 | DUARTINA | SÃO PAULO | Brasil | 3514502 | 35 | 33 | nan | nan | nan | Mata Atlântica | 62.9 |
| 3c153d89-67f4-3320-9cc4-e4c2dbeab130 | -22.3707 | -49.3244 | 2024-10-01 07:47:09 | GOES-16 | DUARTINA | SÃO PAULO | Brasil | 3514502 | 35 | 33 | nan | nan | nan | Mata Atlântica | 147.5 |
| 0502989a-fd7d-331d-843b-69d6b9eb2e1d | -22.3713 | -49.3011 | 2024-10-01 07:47:09 | GOES-16 | PIRATININGA | SÃO PAULO | Brasil | 3539400 | 35 | 33 | nan | nan | nan | Mata Atlântica | 99.5 |
| 1e2b29e5-e380-3d26-9981-b0979360c0f2 | -13.0204 | -51.1884 | 2024-10-01 07:56:20 | GOES-16 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 90.0 |
| 784d0ea4-4d56-3790-8011-9b5063ea57f2 | -14.7402 | -48.7721 | 2024-10-01 07:56:29 | GOES-16 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 48.2 |
| 32597907-7ad6-37e9-b643-b5569a9bdd1f | -16.7079 | -57.3696 | 2024-10-01 07:56:40 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 43.9 |
| f313d764-cc8e-335e-8758-5a52333363d7 | -16.6319 | -57.2352 | 2024-10-01 07:56:40 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 149.5 |
| 22ce1a9b-81d3-342b-bfa2-8a85a7339fac | -16.6316 | -57.2557 | 2024-10-01 07:56:40 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 172.9 |
| e6dba90e-79f1-3ca2-9cd3-fe12588b1e5a | -16.612 | -57.2579 | 2024-10-01 07:56:40 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 54.6 |
| bb7a7aee-0c56-319b-8187-86655a3dc04d | -16.6515 | -57.233 | 2024-10-01 07:56:40 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 142.9 |
| d87dfb65-74e1-3f26-90e7-d071ab4fecc3 | -16.6512 | -57.2535 | 2024-10-01 07:56:40 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 107.3 |
| 72ee4d4d-9841-3bbd-99cb-286513605d7f | -16.8787 | -57.6971 | 2024-10-01 07:56:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 35.6 |


[Clique aqui para ver as próximas entradas](README159.md)
