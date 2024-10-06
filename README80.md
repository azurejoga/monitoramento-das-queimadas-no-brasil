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

## Dados Diários - Página 80

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 48428795-d79c-3da5-8035-7c61921abf5d | -10.41492 | -50.72207 | 2024-10-06 04:19:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 7eafcd5e-b87a-357a-b1e6-a7aceb9dd770 | -10.4143 | -50.72569 | 2024-10-06 04:19:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 0326e225-fa00-38e2-838b-956e6b5e826c | -10.41369 | -50.72929 | 2024-10-06 04:19:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| e3db722b-d218-339f-94e9-dd48a126c3fd | -10.41333 | -50.70689 | 2024-10-06 04:19:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 1f6b2a33-5943-34dc-8c13-2cb0507fbc91 | -10.41307 | -50.73291 | 2024-10-06 04:19:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 67c62037-d5f3-33d0-86e0-27fe2112a929 | -10.51513 | -50.96189 | 2024-10-06 04:19:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 83b9afb3-480f-3785-ac71-ec791184a65f | -10.51104 | -50.96112 | 2024-10-06 04:19:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 6.3 |
| c1595b1f-5333-3c39-8986-09ac1a21d1de | -10.45531 | -50.7066 | 2024-10-06 04:19:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 7a478082-b65b-3d02-8c3b-285f41168ef2 | -10.45469 | -50.71017 | 2024-10-06 04:19:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 525b0291-fe17-34e0-b889-67e7c978b952 | -10.45406 | -50.71374 | 2024-10-06 04:19:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 91fa58c5-cc56-36ee-9a00-a1d295f8a08b | -10.45344 | -50.7173 | 2024-10-06 04:19:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 8a268203-2279-3ce5-98a1-e853dae77447 | -10.45282 | -50.72086 | 2024-10-06 04:19:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 3.9 |
| e7424a90-ea6f-336a-ab1d-4c43ba1b6263 | -10.4522 | -50.72443 | 2024-10-06 04:19:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 3.9 |
| e61fa996-3907-37d2-acac-022a77e38120 | -10.4519 | -50.70229 | 2024-10-06 04:19:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 338a78d1-a078-33b0-8d17-88d6c2cc5b10 | -10.45157 | -50.72799 | 2024-10-06 04:19:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 3.8 |
| f55afa51-94a1-3d8b-af1f-832016a614e6 | -10.45128 | -50.70586 | 2024-10-06 04:19:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 49807b17-ba8a-3a40-9532-03baef9bc53c | -10.45095 | -50.73156 | 2024-10-06 04:19:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 5ef36cd1-b4c1-3c8c-bdde-d540cbaaac60 | -10.45065 | -50.70943 | 2024-10-06 04:19:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 4.2 |
| f4aafd1d-ab8d-3deb-b73b-5c842cd0a0de | -10.45002 | -50.71302 | 2024-10-06 04:19:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 0fce79b9-5b8f-3b1b-a8e8-ab6dbc229a78 | -10.4494 | -50.71659 | 2024-10-06 04:19:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 60c96c5c-d445-381b-8272-aed932d80da0 | -10.44877 | -50.72017 | 2024-10-06 04:19:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 5.3 |
| bd516a68-85e6-3896-a833-1b3168f4e942 | -10.44849 | -50.69798 | 2024-10-06 04:19:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 3.9 |
| eab4e253-30a6-3848-a7cc-b65644880145 | -10.44814 | -50.72374 | 2024-10-06 04:19:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 5.3 |
| b5d4ccd9-d6ae-3475-9c7e-da4ed2a031b6 | -10.44787 | -50.70156 | 2024-10-06 04:19:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 8500499b-ecf6-310f-a167-7465c597a6c7 | -10.44752 | -50.72732 | 2024-10-06 04:19:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 2d68ff46-1166-350d-a2f0-0b44ef5a7d73 | -10.44724 | -50.70512 | 2024-10-06 04:19:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 52f52040-258d-3c94-8aae-75ec04d063eb | -10.44689 | -50.7309 | 2024-10-06 04:19:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 3.2 |
| f4b7f1cd-486c-3272-95c4-4eab008891dd | -10.44661 | -50.70871 | 2024-10-06 04:19:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 4.2 |
| f69e590e-b57a-365c-af1a-84798250001f | -11.34774 | -50.81419 | 2024-10-06 04:19:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 32b11d3b-5295-3b27-988a-b0442f80788b | -11.2479 | -51.26615 | 2024-10-06 04:19:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 043eccf5-aa47-3e2e-a469-c69f629ed7bf | -11.24376 | -51.2654 | 2024-10-06 04:19:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| ef0b3869-0c27-31c5-a3d0-4d4b8d6c364e | -11.24341 | -51.19505 | 2024-10-06 04:19:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 5868e2de-b834-3358-848a-c4338d221076 | -11.23929 | -51.19431 | 2024-10-06 04:19:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 104c1dfc-6596-3458-a912-40a9afe7980c | -11.23896 | -51.26844 | 2024-10-06 04:19:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 19f300c9-892d-3ffc-a85b-9f9d275e84d1 | -11.23518 | -51.19358 | 2024-10-06 04:19:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 8732da8d-d378-3087-bd2c-15f9e8d44c5d | -11.21947 | -51.21022 | 2024-10-06 04:19:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 47d04db9-b2a5-3588-bba6-b27cca6ca756 | -13.26324 | -51.27398 | 2024-10-06 04:19:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e6d420bd-a268-3dfa-a310-88378157eeb8 | -13.26192 | -51.2735 | 2024-10-06 04:19:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 4f5fe01b-889e-31f3-b5d8-036e9052735b | -13.25924 | -51.27324 | 2024-10-06 04:19:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| db91f0f0-6384-3940-9342-bca7242f3120 | -13.24929 | -51.27482 | 2024-10-06 04:19:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 3.6 |
| f096c93e-36e9-39ce-b571-e075cff4f410 | -13.24778 | -51.2598 | 2024-10-06 04:19:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 4dd5c611-928d-3cbc-bb2a-061b0c2a197d | -13.24715 | -51.26337 | 2024-10-06 04:19:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 6572f890-399e-3974-80e3-dba8533ec32c | -13.24653 | -51.26694 | 2024-10-06 04:19:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 614595fd-b9b5-369e-866b-285d7a0d7702 | -13.24591 | -51.27051 | 2024-10-06 04:19:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 90a5c28d-ff26-33f0-8caf-fc0d33acfe35 | -3.48648 | -50.80455 | 2024-10-06 04:19:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| fa781d9b-f92b-388f-a7e1-b9defadca279 | -3.48571 | -50.80918 | 2024-10-06 04:19:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 71bbc687-dd23-37cc-8627-3a98e7b59cf2 | -3.44362 | -50.66346 | 2024-10-06 04:19:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| df4e9d66-7e04-30eb-8e62-0d809bf1a295 | -3.44288 | -50.66798 | 2024-10-06 04:19:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 8919b7a2-378c-3e25-a1c3-7d287b240269 | -3.43386 | -50.66642 | 2024-10-06 04:19:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 91e07ca8-e16d-3505-bad1-3a5b865c3e23 | -3.30336 | -50.66036 | 2024-10-06 04:19:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 04218b71-b1f7-37df-87a4-e6cbaaf0c397 | -3.23597 | -50.83969 | 2024-10-06 04:19:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| e9ccb1a5-88e8-3765-9656-a33734ad8c97 | -3.23199 | -50.83679 | 2024-10-06 04:19:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 421e26e3-d1f9-3664-82b9-f7527edc2bc5 | -3.23123 | -50.84151 | 2024-10-06 04:19:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 10.3 |
| b8576a2a-1925-30bc-abe5-dd224b17c26a | -3.23047 | -50.84628 | 2024-10-06 04:19:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 10.3 |
| edee94b7-125d-32a5-a015-019fa7983c6d | -3.22742 | -50.83598 | 2024-10-06 04:19:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 32d3c7ca-a649-3056-83b0-a05d46359899 | -3.22666 | -50.84069 | 2024-10-06 04:19:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 7a8cea2d-45de-3cf9-9e8d-900c6f922be3 | -3.22589 | -50.84544 | 2024-10-06 04:19:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| cbd44c2e-3f35-3697-a156-708207ed0975 | -3.09623 | -51.22863 | 2024-10-06 04:19:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| dda3ad29-1617-3336-9cd6-3ee21d56884f | -2.89956 | -50.71255 | 2024-10-06 04:19:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| bb35fb2f-b626-33f5-8196-4c8132f9f2cf | -2.89881 | -50.71721 | 2024-10-06 04:19:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 1d082676-abcf-33f2-9013-9f7bdd7c81af | -2.89576 | -50.7071 | 2024-10-06 04:19:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 5195dc29-aa85-3d62-b213-07da9b25c64e | -2.895 | -50.71178 | 2024-10-06 04:19:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 699aa6a9-1fd6-32e4-b2d8-fc68e6693dc6 | -2.89424 | -50.71646 | 2024-10-06 04:19:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 2d686f98-9097-3d15-a306-5d2f75f1aea8 | -2.89119 | -50.70636 | 2024-10-06 04:19:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 92a92bf5-b6d2-3e2d-bbb9-4d2b9712bd93 | -2.89043 | -50.71102 | 2024-10-06 04:19:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 13823483-a79e-303a-979e-13f5ff8f4cd3 | -2.88966 | -50.71571 | 2024-10-06 04:19:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 132ef0d5-fc22-3d09-bd33-dab6d2a6b8fa | -2.88586 | -50.71027 | 2024-10-06 04:19:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| bb529ff7-d7e7-3de2-b0fb-ca0cbd27a42a | -4.10464 | -51.10313 | 2024-10-06 04:19:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| f3433ddf-74f0-3d60-bc7e-34f773773a21 | -4.10003 | -51.1024 | 2024-10-06 04:19:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| b0f8b7d8-f7aa-35aa-977f-bb1b7161c7f9 | -4.09921 | -51.10726 | 2024-10-06 04:19:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6cc52ae8-a3c9-36f3-be29-e5d842d0be69 | -4.05574 | -51.11773 | 2024-10-06 04:19:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| c928ae5c-e991-35e8-9518-1939b4236c36 | -4.05549 | -51.11378 | 2024-10-06 04:19:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6137e3a8-6674-36b5-969f-dd4b6b32b1dd | -4.05473 | -51.11827 | 2024-10-06 04:19:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 11670a0f-bc48-3ae7-826e-6d0c79442c31 | -3.91314 | -51.2415 | 2024-10-06 04:19:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 1b45ae2d-883d-3b3a-8028-0123258a9997 | -3.91234 | -51.24642 | 2024-10-06 04:19:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 08287448-4a14-3c6b-b50c-8ef743387a11 | -3.90847 | -51.24074 | 2024-10-06 04:19:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 1119e3b0-4d07-3bd8-a7f8-754e2d868be1 | -3.90767 | -51.24567 | 2024-10-06 04:19:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 5a7778b0-82e0-3aed-b940-42306dc99436 | -9.7314 | -53.1875 | 2024-10-06 04:19:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 756e6772-65b1-39a4-af81-30ff558b3e6f | -10.90446 | -52.37991 | 2024-10-06 04:19:00 | NOAA-20 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 3711e48a-a9c2-3c40-b601-b073b0352e09 | -10.90364 | -52.3844 | 2024-10-06 04:19:00 | NOAA-20 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 7c8e73fa-9f42-3a12-919c-d085d250bdc4 | -10.90282 | -52.38891 | 2024-10-06 04:19:00 | NOAA-20 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 1c012149-2a1d-301a-b632-20d8fc6fbdd1 | -10.90199 | -52.39344 | 2024-10-06 04:19:00 | NOAA-20 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 1458e1e6-6f2d-3783-94fd-fe3e1cdfa758 | -10.89999 | -52.37905 | 2024-10-06 04:19:00 | NOAA-20 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 01485422-d070-307e-9fd1-b58c4e9f7f46 | -10.89917 | -52.38356 | 2024-10-06 04:19:00 | NOAA-20 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 8a0d65e3-cc91-3cda-8268-3b66d0952847 | -10.89827 | -52.37574 | 2024-10-06 04:19:00 | NOAA-20 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 915b10ac-b6c4-386c-8bdb-86237baeb892 | -10.89748 | -52.38021 | 2024-10-06 04:19:00 | NOAA-20 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 532b0c75-7907-36bb-9d3c-e4f2b8438675 | -10.89669 | -52.38477 | 2024-10-06 04:19:00 | NOAA-20 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 1b466528-c624-3970-ad8c-1101f3dd456a | -10.89552 | -52.37822 | 2024-10-06 04:19:00 | NOAA-20 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 7.5 |
| aa45e11f-787c-33d3-8048-3f7029997921 | -10.89469 | -52.38275 | 2024-10-06 04:19:00 | NOAA-20 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 8d8414d4-8a97-3164-99da-c88c7b43c481 | -10.89221 | -52.38396 | 2024-10-06 04:19:00 | NOAA-20 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| c86b4fe4-bb71-3cdf-adfc-1a117eb5e8d4 | -10.8902 | -52.38197 | 2024-10-06 04:19:00 | NOAA-20 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 85045e22-bb22-307b-b951-7b7c13a01a4c | -10.88772 | -52.38316 | 2024-10-06 04:19:00 | NOAA-20 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d38980cf-1e45-3c03-abf6-b46c4d7952e3 | -10.88573 | -52.38115 | 2024-10-06 04:19:00 | NOAA-20 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| a0d55088-d57d-34e2-ae07-8617608999dc | -10.88325 | -52.38228 | 2024-10-06 04:19:00 | NOAA-20 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3d65a9f7-bd0b-306b-aeef-f5b18b3ca813 | -10.88247 | -52.38676 | 2024-10-06 04:19:00 | NOAA-20 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 74b404ce-6a84-3f1a-8afd-88196314390a | -10.88242 | -52.39916 | 2024-10-06 04:19:00 | NOAA-20 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 48dc8e96-28c6-3f6a-9c17-fcb2aacacb8a | -10.88167 | -52.39127 | 2024-10-06 04:19:00 | NOAA-20 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 1c03712a-9131-3283-a1e3-efe01a4c1391 | -10.88087 | -52.39581 | 2024-10-06 04:19:00 | NOAA-20 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 1883bbb8-8e09-3800-bcca-fd1a696c8c43 | -10.88007 | -52.40041 | 2024-10-06 04:19:00 | NOAA-20 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 86e59a76-b9c2-3149-8b62-cc25f4035199 | -10.87961 | -52.38923 | 2024-10-06 04:19:00 | NOAA-20 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |


[Clique aqui para ver as próximas entradas](README81.md)
